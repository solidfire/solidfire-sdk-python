#!/usr/bin/python
# -*- coding: utf-8 -*-
"""API Common Library"""

import json
from contextlib import closing

import pycurl
from json.decoder import JSONDecodeError

from solidfire.common import model


class ApiServerError(Exception):
    def __init__(self, method_name, err_json):
        from past.builtins import basestring
        if err_json is None:
            err_json = json.loads('{}')
        if err_json is {}:
            err_json = json.loads('{}')
        if isinstance(err_json, basestring) and not err_json.strip():
            err_json = json.loads('{}')

        self._method_name = method_name
        self._err_json = err_json

    def __repr__(self):
        return '%s(method_name="%s", err_json=%s)' % (
            self.__class__.__name__,
            self._method_name,
            self._err_json
        )

    def __str__(self):
        return repr(self)

    @property
    def error_name(self):
        """The name of the error."""
        return self._err_json.get('name', 'Unknown')

    @property
    def error_code(self):
        """The numeric code for this error."""
        return int(self._err_json.get('code', 500))

    @property
    def message(self):
        """A user-friendly message returned from the server."""
        return self._err_json.get('message', None)


class ApiMethodVersionError(Exception):
    def __init__(self,
                 method_name,
                 api_version,
                 since,
                 deprecated=None):
        self._method_name = method_name
        self._api_version = float(api_version)
        self._since = float(since) if since is not None else since
        self._deprecated = float(deprecated) \
            if deprecated is not None else deprecated

    def __repr__(self):
        return '%s(method_name="%s", ' \
               'api_version=%s, ' \
               'since=%s, ' \
               'deprecated=%s, ' % (
                   self.__class__.__name__,
                   self._method_name,
                   self._api_version,
                   self._since,
                   self._deprecated
               )

    def __str__(self):
        return str.format(
            '\n    Invalid Method:\n'
            '    Method Name: {_method_name}\n'
            '    Service Api Version: {_api_version}\n'
            '    Method Exists Since: {_since}\n'
            '    Method Deprecated: {_deprecated}\n',
            **self.__dict__
        )

    @property
    def method_name(self):
        """The name of the service method causing the error."""
        return self._method_name

    @property
    def api_version(self):
        """The version of the Element API Service"""
        return self._api_version

    @property
    def since(self):
        """The version a service was introduced"""
        return self._since

    @property
    def deprecated(self):
        """The version a service was deprecated"""
        return self._deprecated


class ApiParameterVersionError(Exception):
    def __init__(self,
                 method_name,
                 api_version,
                 params):
        self._method_name = method_name
        self._api_version = float(api_version)
        self._params = params
        self._violations = []
        if params is not None:
            for (name, value, since, deprecated) in params:
                self._violations.append(
                    name + ' (version: ' + str(since) + ')'
                )

    def __repr__(self):
        return '%s(method_name="%s", ' \
               'api_version=%s, ' \
               'params=%s, ' % (
                   self.__class__.__name__,
                   self._method_name,
                   self._api_version,
                   self._params,
               )

    def __str__(self):
        return str.format(
            '\n    Invalid Parameter:\n'
            '    Method: {_method_name}\n'
            '    Api Version: {_api_version}\n'
            '    Invalid Parameters: {_violations}\n',
            **self.__dict__
        )

    @property
    def method_name(self):
        """The name of the service method causing the error."""
        return self._method_name

    @property
    def api_version(self):
        """The version of the Element API Service"""
        return self._api_version

    @property
    def params(self):
        """The parameters checked with a service call"""
        return self._params

    @property
    def violations(self):
        """The parameters violated with the service call"""
        return self._violations


class ApiVersionExceededError(Exception):
    def __init__(self,
                 api_version,
                 current_version):
        self._api_version = float(api_version)
        self._current_version = float(current_version)

    def __repr__(self):
        return '%s(api_version=%s, ' \
               'current_version=%s, ' % (
                   self.__class__.__name__,
                   self._api_version,
                   self._current_version
               )

    def __str__(self):
        return str.format(
            '\n    Version Exceeded:\n'
            '    Provided Api Version: {_api_version}\n'
            '    Max Version: {current_version}\n',
            current_version=self._current_version,
            **self.__dict__,
        )

    @property
    def api_version(self):
        """The version of the Element API Service"""
        return self._api_version

    @property
    def current_version(self):
        """The current version of the connected Element OS"""
        return self._current_version


class ApiVersionUnsupportedError(Exception):
    def __init__(self,
                 api_version,
                 supported_versions):
        self._api_version = float(api_version)
        self._supported_versions = [float(i) for i in supported_versions]

    def __repr__(self):
        return '%s(api_version=%s, ' \
               'supported_versions=%s' % (
                   self.__class__.__name__,
                   self._api_version,
                   self._supported_versions
               )

    def __str__(self):
        return str.format(
            '\n    Version Unsupported:\n'
            '    Provided Api Version: {_api_version}\n'
            '    Supported Version: {_supported_versions}\n',
            **self.__dict__
        )

    @property
    def api_version(self):
        """The version of the Element API Service"""
        return self._api_version

    @property
    def supported_versions(self):
        """The versions supported by the connected Element OS"""
        return self._supported_versions


class CurlDispatcher(object):
    import pycurl
    pycurl.version_info()
    try:
        from io import BytesIO
    except ImportError:
        from io import StringIO as BytesIO

    def __init__(self, endpoint, username, password, verify_ssl):
        self._endpoint = endpoint
        self._credentials = str.format('{u}:{p}', u=username, p=password) \
            if (username or password) else None
        self._verify_ssl = verify_ssl

    def post(self, data):
        """Post data to the associated endpoint
        and await the server's response.
        :param data: """
        with closing(CurlDispatcher.pycurl.Curl()) as c:
            c.setopt(c.URL, self._endpoint)
            obuffer = CurlDispatcher.BytesIO()
            c.setopt(c.POSTFIELDS, data)
            c.setopt(c.WRITEFUNCTION, obuffer.write)

            if self._credentials:
                c.setopt(c.HTTPAUTH, c.HTTPAUTH_BASIC)
                c.setopt(c.USERPWD, self._credentials)

            if not self._verify_ssl:
                c.setopt(c.SSL_VERIFYPEER, 0)
                c.setopt(c.SSL_VERIFYHOST, 0)

            c.perform()

            return obuffer.getvalue().decode('utf-8')


class ServiceBase(object):
    """The base type for API services.
    This performs the sending, encoding and decoding of requests."""

    def __init__(self, mvip=None, username=None, password=None,
                 api_version=8.0, verify_ssl=True, dispatcher=None):
        """
        Constructor for initializing a connection to an instance of Element OS

        :param mvip: the management IP (IP or hostname)
        :type mvip: str
        :param username: username use to connect to the Element OS instance.
        :type username: str
        :param password: authentication for username
        :type password: str
        :param api_version: specific version of Element OS to connect.
        :type api_version: float
        :param verify_ssl: disable to avoid ssl connection errors especially
            when using an IP instead of a hostname
        :type verify_ssl: bool
        :param dispatcher: a prebuilt or custom http dispatcher
        :return: a configured connection to an Element OS instance
        """

        self._api_version = float(api_version)
        if not dispatcher:
            endpoint = str.format('https://{mvip}/json-rpc/{api_version}',
                                  mvip=mvip, api_version=self._api_version)
            dispatcher = CurlDispatcher(endpoint, username, password,
                                        verify_ssl)
        self._dispatcher = dispatcher

    def _send_request(self, method_name,
                      result_type,
                      params=None,
                      since=None,
                      deprecated=None):

        self._check_method_version(method_name, since, deprecated)

        if params is None:
            params = {}
        encoded = json.dumps({
            'method': method_name,
            'id': 1,
            'params': dict(
                (name, model.serialize(val)) for name, val in params.items()
            ),
        })

        json_err = None
        try:
            response_raw = self._dispatcher.post(encoded)
        except pycurl.error as e:
            json_err = json.dumps(
                {'error':
                     { 'name': str(e.__class__).split('\'')[1],
                       'code': 500,
                       'message': e.args[1]
                       }
                 }
            )
        if json_err is not None:
            raise ApiServerError('', json_err)

        try:
            response = json.loads(response_raw)
        except JSONDecodeError as e:
            json_err = json.dumps(
                {'error':
                     { 'name': 'JSONDecodeError',
                       'code': 500,
                       'message': str(e)
                       }
                 }
            )
        if json_err is not None:
            raise ApiServerError('', json_err)

        if 'error' in response:
            raise ApiServerError(method_name, response['error'])
        else:
            return model.extract(result_type, response['result'])

    def _check_method_version(self,
                              method_name,
                              since,
                              deprecated=None):
        if since is not None and float(since) > self._api_version:
            raise ApiMethodVersionError(method_name,
                                        self._api_version,
                                        since=float(since),
                                        deprecated=deprecated)

    def check_param_versions(self,
                             method_name,
                             params):
        invalid = []
        if params is None:
            params = []
        for (name, value, since, deprecated) in params:
            if value is not None and float(since) > self._api_version:
                invalid.append((name, value, float(since), deprecated))

        if len(invalid) > 0:
            raise ApiParameterVersionError(method_name,
                                           self._api_version,
                                           invalid)
