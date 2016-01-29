#!/usr/bin/python
# -*- coding: utf-8 -*-
"""API Common Library"""

import json
from contextlib import closing

from solidfire.common.api import model


class ApiServerError(Exception):
    def __init__(self, method_name, err_json):
        self._method_name = method_name
        self._err_name = err_json.get('name', 'Unknown')
        self._code = err_json.get('code', 500)
        self._message = err_json.get('message', None)

    def __repr__(self):
        return str.format(
                '\n\tMethod: {_method_name}\n'
                '\tCode: {_code}\n'
                '\tName: {_err_name}\n'
                '\tMessage: {_message}',
                **self.__dict__
        )

    def __str__(self):
        return repr(self)

    @property
    def error_name(self):
        """The name of the error."""
        return self._err_name

    @property
    def error_code(self):
        """The numeric code for this error."""
        return self._code

    @property
    def message(self):
        """A user-friendly message returned from the server."""
        return self._message


class ApiVersionError(Exception):
    def __init__(self,
                 method_name,
                 api_version,
                 params=None,
                 since=None,
                 deprecated=None):
        self._method_name = method_name
        self._api_version = api_version
        self._params = params
        self._since = since
        self._deprecated = deprecated
        if self._params is not None:
            self._violations = []
            for (name, value, since, deprecated) in self._params:
                self._violations.append(name + ' (version: ' + str(since) + ')')

    def __repr__(self):
        if self._params is not None:
            return str.format(
                    '\n\tInvalid Parameter:'
                    '\n\tMethod: {_method_name}\n'
                    '\tApi Version: {_api_version}\n'
                    '\tInvalid Parameters: {_violations}\n',
                    **self.__dict__
            )
        else:
            return str.format(
                    '\n\tInvalid Method:'
                    '\n\tMethod Name: {_method_name}\n'
                    '\tService Api Version: {_api_version}\n'
                    '\tMethod Exists Since: {_since}\n'
                    '\tMethod Deprecated: {_deprecated}',
                    **self.__dict__
            )

    def __str__(self):
        return repr(self)

    @property
    def method_name(self):
        """The name of the service method causing the error."""
        return self._method_name


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

        self._api_version = api_version
        if not dispatcher:
            endpoint = str.format('https://{mvip}/json-rpc/{api_version}',
                                  mvip=mvip, api_version=api_version)
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
            'params': dict((name, model.serialize(val)) for name, val in
                           params.items()),
        })
        response_raw = self._dispatcher.post(encoded)
        response = json.loads(response_raw)
        if 'error' in response:
            raise ApiServerError(method_name, response['error'])
        else:
            return model.extract(result_type, response['result'])

    def _check_method_version(self, method_name, since, deprecated=None):
        if since > self._api_version:
            raise ApiVersionError(method_name,
                                  self._api_version,
                                  params=None,
                                  since=since,
                                  deprecated=deprecated)

    def _check_param_versions(self, method_name,
                              params):
        invalid = []
        for (name, value, since, deprecated) in params:
            if value is not None and since > self._api_version:
                invalid.append((name, value, since, deprecated))

        raise ApiVersionError(method_name,
                              self._api_version,
                              invalid)
