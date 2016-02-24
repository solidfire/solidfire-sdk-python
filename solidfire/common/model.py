#!/usr/bin/python
# -*- coding: utf-8 -*-
import json
from future.utils import with_metaclass

KNOWN_CONVERSIONS = {
    type(set): list
}


def serialize(val):
    if hasattr(val, 'to_json'):
        return val.to_json()
    elif type(val) in KNOWN_CONVERSIONS:
        return KNOWN_CONVERSIONS[type(val)](val)
    elif isinstance(val, dict):
        return dict((k, serialize(v)) for k, v in val.items())
    else:
        return val


def extract(typ, src):
    if hasattr(typ, 'extract'):
        return typ.extract(src, False)
    else:
        return src


class ModelProperty(object):
    def __init__(self, member_name, member_type, array=False, optional=False,
                 documentation=None):
        self._member_name = member_name
        self._member_type = member_type
        self._array = array
        self._optional = optional
        self._documentation = documentation

    def extend_json(self, out, data):
        if data is None:
            if not self._optional:
                out[self._member_name] = None
        elif self._array:
            out[self._member_name] = [serialize(x) for x in data]
        else:
            out[self._member_name] = serialize(data)

    def extract_from(self, data):
        if self._array:
            return [] if data is None else [extract(self._member_type, x) for x
                                            in data]
        else:
            return extract(self._member_type, data)

    def member_name(self):
        return self._member_name

    def member_type(self):
        return self._member_type

    def array(self):
        return self._array

    def optional(self):
        return self._optional

    def documentation(self):
        return self._documentation


class MetaDataObject(type):
    def __init__(cls, name, bases, classdict):
        super(MetaDataObject, cls).__init__(name, bases, classdict)
        cls._create_properties()


class DataObject(with_metaclass(MetaDataObject, ModelProperty)):
    _properties = None

    @classmethod
    def _create_properties(cls):
        cls._properties = {}
        for name in dir(cls):
            prop = getattr(cls, name, None)
            if isinstance(prop, ModelProperty):
                cls._properties[name] = prop

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            if k not in type(self)._properties:
                msg_fmt = 'Key "{k}" is not a valid property'
                msg = msg_fmt.format(k)
                raise TypeError()
            else:
                setattr(self, k, v)

    def __repr__(self):
        props = []
        for name, prop in sorted(type(self)._properties.items()):
            if prop.array():
                attrs = (repr(x) for x in getattr(self, name))
                msg_fmt = '[{arr}]'
                r = msg_fmt.format(arr=str.join(', ', attrs))
            else:
                r = repr(getattr(self, name))
            msg_fmt = '{name}={repr}'
            msg = msg_fmt.format(name=name, repr=r)
            props.append(msg)
        return str.format('{cls}({props})', cls=type(self).__name__,
                          props=str.join(', ', props))

    def to_json(self):
        out = {}
        for name, prop in type(self)._properties.items():
            prop.extend_json(out, getattr(self, name, None))
        return out

    @classmethod
    def extract(cls, data, strict=True):
        ctor_dict = {}
        for name, prop in cls._properties.items():
            if prop.member_name() in data:
                ctor_dict[name] = prop.extract_from(data[prop.member_name()])
            elif prop.optional():
                ctor_dict[name] = None
            elif prop.array():
                ctor_dict[name] = []
            elif not strict:
                ctor_dict[name] = None
            else:
                msg_fmt = 'Can not create {typ}: ' \
                          'missing required property "{name}" in {data}'
                msg = msg_fmt.format(typ=cls.__name__,
                                     name=prop.member_name(),
                                     data=json.dumps(data)
                                     )
                raise TypeError(msg)
        return cls(**ctor_dict)


def property(member_name, member_type,
             array=False, optional=False,
             documentation=None):
    msg_fmt = 'Property of type {typ}{arr}'
    msg = msg_fmt.format(
        typ=member_type,
        arr='[]'.encode('ascii', 'ignore')
            if array else ''.encode('ascii', 'ignore')
    )
    documentation = documentation or msg
    typ = type(member_name,
               (ModelProperty,),
               {
                   '__doc__': documentation,
                   '__repr__': documentation
               })

    return typ(member_name=member_name,
               member_type=member_type,
               array=array,
               optional=optional,
               documentation=documentation
               )
