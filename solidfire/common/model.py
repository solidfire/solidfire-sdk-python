#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2014-2016 NetApp, Inc. All Rights Reserved.
#
# CONFIDENTIALITY NOTICE: THIS SOFTWARE CONTAINS CONFIDENTIAL INFORMATION OF
# NETAPP, INC. USE, DISCLOSURE OR REPRODUCTION IS PROHIBITED WITHOUT THE PRIOR
# EXPRESS WRITTEN PERMISSION OF NETAPP, INC.

from __future__ import unicode_literals
from future.utils import with_metaclass
import json

KNOWN_CONVERSIONS = {
    type(set): list
}


def _as_ascii(val):
    """
    Helper method for enforcing ascii encoding.

    :param val: any string, basestring, or unicode string
    :type val: basestring

    :return: a string
    """
    return str(val.encode('ascii', 'ignore'))


def serialize(val):
    """
    DataObject serializer value based on MetaData attributes.

    :param val: any value

    :return: the serialized value
    """
    if hasattr(val, 'to_json'):
        return val.to_json()
    elif type(val) in KNOWN_CONVERSIONS:
        return KNOWN_CONVERSIONS[type(val)](val)
    elif isinstance(val, dict):
        return dict((k, serialize(v)) for k, v in val.items())
    elif hasattr(val, '_optional') and val.optional():
        return None
    else:
        return val


def extract(typ, src):
    """
    DataObject value type converter.

    :param typ: the type to extract.

    :param src: the source to extract as type typ.

    :return: if the type has the ability to extract (convert), otherwise the
        original version is returned.
    """
    if hasattr(typ, 'extract'):
        return typ.extract(src, False)
    else:
        return src


class ModelProperty(object):
    """
    ModelProperty metadata container for API data type information.
    """
    def __init__(self, member_name, member_type, array=False, optional=False,
                 documentation=None):
        """
        ModelProperty constructor.

        :param member_name: the name of the property.
        :type member_name: str

        :param member_type: the type of the property.
        :type member_type: str

        :param array: is the property an array.
        :type array: bool

        :param optional: is the property optional.
        :type optional: bool

        :param documentation: documentation for the property.
        :type documentation: str
        """
        self._member_name = member_name
        self._member_type = member_type
        self._array = array
        self._optional = optional
        self._documentation = documentation

    def extend_json(self, out, data):
        """
        Serialize the property as json-like structure.

        :param out: the resulting output.
        :param data: the data to be converted.
        """
        if data is None:
            if not self._optional:
                out[self._member_name] = None
        elif self._array:
            out[self._member_name] = [serialize(x) for x in data]
        elif self._optional:
            optional_data = serialize(data)
            if optional_data is not None:
                out[self._member_name] = optional_data
        else:
            out[self._member_name] = serialize(data)

    def extract_from(self, data):
        """
        Deserialize the property from json.

        :param data: the data to be converted.

        :return: the extracted data.
        """
        if self._array:
            return [] if data is None else [extract(self._member_type, x) for x
                                            in data]
        else:
            return None if data is None else extract(self._member_type, data)

    def member_name(self):
        """
        :return: the member name.
        """
        return self._member_name

    def member_type(self):
        """
        :return: the member type.
        """
        return self._member_type

    def array(self):
        """
        :return: is the property an array
        """
        return self._array

    def optional(self):
        """
        :return: is the property optional
        """
        return self._optional

    def documentation(self):
        """
        :return: the property documentation
        """
        return self._documentation

    def known_default(self):
        """
        Helps convert a property to a default value.

        :return: a known default for a type.
        """
        if self._member_type is int:
            return 0
        elif self._member_type is float:
            return 0.0
        elif self._member_type is str:
            return ''
        elif self._member_type is bool:
            return False
        else:
            pass


class MetaDataObject(type):
    """
    MetaDataObject defines a method for attributing ModelProperties to a type.
    """

    def __init__(cls, name, bases, classdict):
        super(MetaDataObject, cls).__init__(name, bases, classdict)
        cls._create_properties()

    def _create_properties(self):
        pass


class DataObject(with_metaclass(MetaDataObject, ModelProperty)):
    """
    DataObject is the base type for all generated types, including the MetaData
    properties, as described from the api descriptors.
    """
    _properties = None

    @classmethod
    def _create_properties(cls):
        """
        Maps api descriptor attributes to the MetaData properties for this
        object.
        """
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
                raise TypeError(msg)
            else:
                setattr(self, k, v)

    def __repr__(self):
        """
        Base repr() for all generated objects.
        """
        props = []
        for name, prop in sorted(type(self)._properties.items()):

            if prop.array() and hasattr(self, name):
                try:
                    iter(getattr(self, name))
                except TypeError:
                    attrs = []
                else:
                    attrs = (repr(x) for x in getattr(self, name))
                msg_fmt = '[{arr}]'
                r = msg_fmt.format(
                    arr=str.join(str(', '), attrs))
            else:
                r = repr(getattr(self, name))
            msg_fmt = '{name}={repr}'
            msg = msg_fmt.format(name=name, repr=r)
            props.append(msg)
        return str.format(str('{cls}({props})'),
                          cls=type(self).__name__,
                          props=str.join(str(', '), props))

    def to_json(self):
        """
        Converts DataObject to json.

        :return: the DataObject as a json structure.
        """
        out = {}
        for name, prop in type(self)._properties.items():
            prop.extend_json(out, getattr(self, name, None))
        return out

    @classmethod
    def extract(cls, data, strict=True):
        """
        Converts json to a DataObject.

        :param data: json data to be deserialized back to a DataObject
        :type data: str

        :param strict: If True, missing values will raise an error, otherwise,
            missing values will None or empty.
        :type strict: bool

        :return: a class deserialized from the data provided.
        """
        ctor_dict = {}
        for name, prop in cls._properties.items():
            if data is None:
                pass
            elif prop.member_name() in data:
                data_val = data[prop.member_name()]
                ctor_dict[name] = prop.extract_from(data_val)
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
    """
    Constructs the type for a DataObject property.

    :param member_name: the name of the property.
    :type member_name: str

    :param member_type: the type of the property.
    :type member_type: type

    :param array: is the property an array.
    :type array: bool

    :param optional: is the property optional.
    :type optional: bool

    :param documentation: documentation for the property.
    :type documentation: str or NoneType

    :return: the constructed type of a property
    """
    msg_fmt = 'Property of type {typ}{arr}'
    msg = msg_fmt.format(
        typ=member_type,
        arr='[]'
        if array else ''
    )
    documentation = documentation or msg
    typ = type(_as_ascii(member_name),
               (ModelProperty,),
               {
                   '__doc__': documentation,
                   '__repr__': repr(_as_ascii(msg))
               })

    return typ(member_name=member_name,
               member_type=member_type,
               array=array,
               optional=optional,
               documentation=documentation
               )
