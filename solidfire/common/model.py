#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright &copy; 2014-2016 NetApp, Inc. All Rights Reserved.
#
# CONFIDENTIALITY NOTICE: THIS SOFTWARE CONTAINS CONFIDENTIAL INFORMATION OF
# NETAPP, INC. USE, DISCLOSURE OR REPRODUCTION IS PROHIBITED WITHOUT THE PRIOR
# EXPRESS WRITTEN PERMISSION OF NETAPP, INC.

from __future__ import unicode_literals
import json
from uuid import UUID
from future.utils import with_metaclass

KNOWN_CONVERSIONS = {
    type(set): list,
    UUID: str
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
    if hasattr(val, 'custom_to_json'):
        return_value = val.custom_to_json()
    elif hasattr(val, 'to_json'):
        return_value = val.to_json()
    elif type(val) in KNOWN_CONVERSIONS:
        return_value = KNOWN_CONVERSIONS[type(val)](val)
    elif isinstance(val, dict):
        return_value = dict((k, serialize(v)) for k, v in val.items())
    elif isinstance(val, list):
        return_value = list(serialize(v) for v in val)
    elif hasattr(val, '_optional') and val.optional():
        return_value = None
    else:
        return_value = val

    return return_value


def extract(typ, src):
    """
    DataObject value type converter.

    :param typ: the type to extract.

    :param src: the source to extract as type typ.

    :return: if the type has the ability to extract (convert), otherwise the
        original version is returned.
    """
    if hasattr(typ, 'extract'):
        return_value = typ.extract(src, False)
    elif type(src) == typ:
        return_value = src
    elif typ == UUID:
        return_value = UUID(src)
    elif typ.__init__(src) is not None:
        return_value = typ.__init__(src)
    else:
        return_value = src

    return return_value


class ModelProperty(object):
    """
    ModelProperty metadata container for API data type information.
    """

    def __init__(self, member_name, member_type, array=False, optional=False,
                 documentation=None, dictionaryType = None):
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
        self._dictionaryType = dictionaryType

    def __repr__(self):
        if self._array:
            arr = '[]'
        else:
            arr = ''

        full_type = '{}'.format(self._member_type).replace('\'>', arr + '\'>')
        return full_type

    def extend_json(self, out, data):
        """
        Serialize the property as json-like structure.

        :param out: the resulting output.
        :param data: the data to be converted.
        """
        if data is None or hasattr(data, '_member_type'):  # HACK ALERT
            if not self._optional:
                # We want to catch this error.
                raise ValueError(self._member_name+" is a required parameter.")
                # THE OLD WAY!
                #out[self._member_name] = None
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
        if self._dictionaryType:
            newdict = dict()
            for key in data:
                newdict[key] = extract(self._dictionaryType, data[key])
            return newdict
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
        # Iterate through available properties and start removing them
        # from kwargs
        for name, property in type(self)._properties.items():
            if not property.optional() and name not in kwargs.keys() and name != "secret":
                raise ValueError(name+" is a required parameter.")
            if name in kwargs:
                setattr(self, name, kwargs[name])
                del kwargs[name]
        if(len(kwargs.keys()) != 0):
            raise ValueError("The following params are invalid: "+str(kwargs.keys()))

    def get_properties(self):
        """
        Exposes the type properties for a Data Object.

        :return: the dictionary of property names and thier type information.
        :rtype: dict
        """
        return self._properties

    def __repr__(self):
        """
        Base repr() for all generated objects.
        """
        props = []
        member_items = self._properties
        for name, prop in sorted(member_items.items()):

            if prop.array() and hasattr(self, name):
                try:
                    iter(getattr(self, name))
                except TypeError:
                    attrs = []
                else:
                    attrs = (repr(x) for x in getattr(self, name))
                msg_fmt = '[{arr}]'
                attr_repr = msg_fmt.format(
                    arr=str.join(str(', '), attrs))
            else:
                if hasattr(self, name):
                    attr_repr = getattr(self, name)
                else:
                    attr_repr = None
            msg_fmt = '{name}={repr!r}'
            msg = msg_fmt.format(name=name, repr=attr_repr)
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
            # If it has data
            if data is None:
                pass
            # If it is a chap secret
            elif hasattr(prop.member_type(), 'custom_extract'):
                ctor_dict[name] = prop.member_type().custom_extract(
                    data[prop.member_name()])
            # If it has the right data which matches the data we need, set it
            elif prop.member_name() in data:
                data_val = data[prop.member_name()]
                ctor_dict[name] = prop.extract_from(data_val)
            # If we're dealing with an optional property which hasn't been provided
            elif prop.optional():
                ctor_dict[name] = None
            # If we're dealing with an empty array
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
             array = False, optional = False,
             documentation = None, dictionaryType = None):
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
               })

    return typ(member_name=member_name,
               member_type=member_type,
               array=array,
               optional=optional,
               documentation=documentation,
               dictionaryType=dictionaryType)
