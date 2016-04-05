#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2014-2016 NetApp, Inc. All Rights Reserved.
#
# CONFIDENTIALITY NOTICE: THIS SOFTWARE CONTAINS CONFIDENTIAL INFORMATION OF
# NETAPP, INC. USE, DISCLOSURE OR REPRODUCTION IS PROHIBITED WITHOUT THE PRIOR
# EXPRESS WRITTEN PERMISSION OF NETAPP, INC.
"""API Common Library"""

import json
from contextlib import closing

import itertools
import pycurl
import logging

from solidfire.common import model

log = logging.getLogger('solidfire.Element')
log.setLevel(logging.INFO)
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
ch.setFormatter(formatter)
log.addHandler(ch)

atomic_counter = itertools.count()


def setLogLevel(level):
    """
    Set the logging level of Element logger and all handlers.

    >>> from logging
    >>> from solidfire import common
    >>> common.setLogLevel(logging.DEBUG)

    :param level: level must be an int or a str.
    """
    log.setLevel(level)
    for handler in log.handlers:
        handler.setLevel(level)


class ApiServerError(Exception):
    """
    ApiServerError is an exception that occurs on the server and is passes as a
    response back to the sdk.
    """

    def __init__(self, method_name, err_json):
        """
        ApiServerError constructor.

        :param method_name: name of the service method where the error
            occurred.
        :type method_name: str
        :param err_json: the json formatted error received from the service.
        :type err_json: str
        """
        if isinstance(err_json, str) and not err_json.strip():
            err_json = '{}'

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
    def method_name(self):
        """The name of the service method causing the error."""
        return self._method_name

    @property
    def error_name(self):
        """The name of the error."""
        return json.loads(self._err_json)\
            .get('error', {}).get('name', 'Unknown')

    @property
    def error_code(self):
        """The numeric code for this error."""
        return int(json.loads(self._err_json)
                   .get('error', {}).get('code', 500))

    @property
    def message(self):
        """A user-friendly message returned from the server."""
        return json.loads(self._err_json).get('error', {}).get('message', None)


class ApiMethodVersionError(Exception):
    """
    An ApiMethodVersionError occurs when a service method is not compatible
    with the version of the connected server.
    """

    def __init__(self,
                 method_name,
                 api_version,
                 since,
                 deprecated=None):
        """
        ApiMethodVersionError constructor.

        :param method_name: name of the service method where the error
            occurred.
        :type method_name: str

        :param api_version: the version of API used to instantiate the
            connection to the server.
        :type api_version: str or float

        :param since: the earliest version of the API a service method is
            compatible.
        :type since: str or float

        :param deprecated:  the latest version of the API that a method is
            compatible.
        :type deprecated: str or float
        """
        self._method_name = method_name
        self._api_version = float(api_version)
        self._since = float(since) if since is not None else since
        self._deprecated = float(deprecated) \
            if deprecated is not None else deprecated

    def __repr__(self):
        return '%s(method_name="%s", ' \
               'api_version=%s, ' \
               'since=%s, ' \
               'deprecated=%s) ' % (
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
    """
    An ApiParameterVersionError occurs when a parameter supplied to a service
    method is not compatible with the version of the connected server.
    """

    def __init__(self,
                 method_name,
                 api_version,
                 params):
        """
        ApiParameterVersionError constructor.

        :param method_name: name of the service method where the error
            occurred.
        :type method_name: str

        :param api_version: the version of API used to instantiate the
            connection to the server.
        :type api_version: str or float

        :param params: the list of incompatible parameters provided to a
            service method call.  This tuple should include name, value, since,
            and deprecated values for each offending parameter.
        :type params: list of tuple
        """
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
               'params=%s) ' % (
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
    """
    An ApiVersionExceededError occurs when connecting to a server with a
    version lower then the provided api_version.
    """

    def __init__(self,
                 api_version,
                 current_version):
        """
        ApiVersionExceededError constructor.

        :param api_version: the version of API used to instantiate the
            connection to the server.
        :type api_version: str or float

        :param current_version: the current version of the server.
        :type current_version: float
        """
        self._api_version = float(api_version)
        self._current_version = float(current_version)

    def __repr__(self):
        return '%s(api_version=%s, ' \
               'current_version=%s) ' % (
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
            **self.__dict__
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
    """
    An ApiVersionUnsupportedError occurs when connecting to a server unable
    to support the provided api_version.
    """

    def __init__(self,
                 api_version,
                 supported_versions):
        """
        ApiVersionUnsupportedError constructor.

        :param api_version: the version of API used to instantiate the
            connection to the server.
        :type api_version: str or float

        :param supported_versions: the list of supported versions provided by
            a server.
        :type supported_versions: float[]
        """
        self._api_version = float(api_version)
        self._supported_versions = [float(i) for i in supported_versions]

    def __repr__(self):
        return '%s(api_version=%s, ' \
               'supported_versions=%s)' % (
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
    """
    The CurlDispatcher is responsible for connecting, sending, and receiving
    data to a server.
    """
    import pycurl
    pycurl.version_info()

    def __init__(self, endpoint, username, password, verify_ssl):
        """
        The CurlDispatcher constructor.

        :param endpoint: the server URL
        :type endpoint: str

        :param username: the username for authentication
        :type username: str

        :param password: the password for authentication
        :type password: str

        :param verify_ssl: If True, ssl errors will cause an exception to be
            raised, otherwise, if False, they are ignored.
        :type verify_ssl: bool
        """
        self._endpoint = endpoint
        self._credentials = str.format('{u}:{p}', u=username, p=password) \
            if (username or password) else None
        self._verify_ssl = verify_ssl
        self._timeout = 300
        self._connect_timeout = 30

    def timeout(self, timeout_in_sec):
        """
        Set the time to wait for a response before timeout.

        :param timeout_in_sec: the read timeout in seconds.
        :type timeout_in_sec: int

        :raise ValueError: if timeout_in_sec is less than 0
        """
        temp_timeout = int(timeout_in_sec)
        if temp_timeout < 0:
            raise ValueError("Read Timeout less than 0")
        self._timeout = temp_timeout

    def connect_timeout(self, timeout_in_sec):
        """
        Set the time to wait for a connection to be established before timeout.

        :param timeout_in_sec: the connection timeout in seconds.
        :type timeout_in_sec: int

        :raise ValueError: if timeout_in_sec is less than 0
        """
        temp_timeout = int(timeout_in_sec)
        if temp_timeout < 0:
            raise ValueError("Connection Timeout less than 0")
        self._connect_timeout = temp_timeout

    def restore_timeout_defaults(self):
        """
        Restores the Connection and Read Timeout to their original durations of
        30 seconds for connection timeout and 300 seconds (5 minutes) for read
        timeout.
        """
        self._timeout = 300
        self._connect_timeout = 30

    def post(self, data):
        """
        Post data to the associated endpoint and await the server's response.

        :param data: the data to be posted.
        :type data: str or json
        """
        try:
            from io import BytesIO
            assert BytesIO
        except ImportError:
            from io import StringIO as BytesIO

        with closing(CurlDispatcher.pycurl.Curl()) as c:
            c.setopt(c.URL, self._endpoint)
            obuffer = BytesIO()
            c.setopt(c.POSTFIELDS, data)
            c.setopt(c.WRITEFUNCTION, obuffer.write)
            c.setopt(c.CONNECTTIMEOUT, self._connect_timeout)
            c.setopt(c.TIMEOUT, self._timeout)

            if self._credentials:
                c.setopt(c.HTTPAUTH, c.HTTPAUTH_BASIC)
                c.setopt(c.USERPWD, self._credentials)

            if not self._verify_ssl:
                c.setopt(c.SSL_VERIFYPEER, 0)
                c.setopt(c.SSL_VERIFYHOST, 0)

            c.perform()

            return obuffer.getvalue().decode('utf-8')


class ServiceBase(object):
    """
    The base type for API services.
    This performs the sending, encoding and decoding of requests.
    """

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

    def timeout(self, timeout_in_sec):
        """
        Set the time to wait for a response before timeout.

        :param timeout_in_sec: the read timeout in seconds.
        :type timeout_in_sec: int

        :raise ValueError: if timeout_in_sec is less than 0
        """
        self._dispatcher.timeout(timeout_in_sec)

    def connect_timeout(self, timeout_in_sec):
        """
        Set the time to wait for a connection to be established before timeout.

        :param timeout_in_sec: the connection timeout in seconds.
        :type timeout_in_sec: int

        :raise ValueError: if timeout_in_sec is less than 0
        """
        self._dispatcher.connect_timeout(timeout_in_sec)

    def restore_timeout_defaults(self):
        """
        Restores the Connection and Read Timeout to their original durations of
        300 seconds (5 minutes) each.
        """
        self._dispatcher.restore_timeout_defaults()

    def _send_request(self, method_name,
                      result_type,
                      params=None,
                      since=None,
                      deprecated=None):

        self._check_method_version(method_name, since, deprecated)

        if params is None:
            params = {}

        global atomic_counter
        if hasattr(atomic_counter, 'next'):
            atomic_id = atomic_counter.next()
        else:
            atomic_id = atomic_counter.__next__()
        encoded = json.dumps({
            'method': method_name,
            'id': atomic_id if atomic_id > 0 else 0,
            'params': dict(
                (name, model.serialize(val))
                for name, val in params.items()
            ),
        })

        try:
            log.info(msg=encoded)
            response_raw = self._dispatcher.post(encoded)
        except pycurl.error as e:
            json_err = json.dumps(
                {
                    'error':
                        {
                            'name': str(e.__class__).split('\'')[1],
                            'code': 500,
                            'message': e.args[1]
                        }
                }
            )
            raise ApiServerError(method_name, json_err)

        if "401 Unauthorized." in response_raw:
            json_err = json.dumps(
                {
                    'error':
                        {
                            'name': 'AuthorizationError',
                            'code': 401,
                            'message': 'Username or password incorrect.'
                        }
                }
            )
            raise ApiServerError('login', json_err)

        try:
            response = json.loads(response_raw)
            log.debug(msg=response)
        except Exception as e:
            log.error(msg=response_raw)
            response = json.dumps(
                {
                    'error':
                        {
                            'name': 'JSONDecodeError',
                            'code': 500,
                            'message': str(e)
                        }
                }
            )

        if 'error' in response:
            raise ApiServerError(method_name, response['error'])
        else:
            return model.extract(result_type, response['result'])

    def _check_method_version(self,
                              method_name,
                              since,
                              deprecated=None):
        """
        Check method version against the initialized api_version of the
        service.

        :param method_name: service method name performing the check.
        :type method_name: str

        :param since: service method inception version
        :type since: float or str

        :param deprecated: service method deprecation version
        :type deprecated: float or str

        :raise ApiMethodVersionError: if the configured version of the
            ServiceBase is less then the inception version.  Deprecation is
            not currently checked.
        """

        if since is not None and float(since) > self._api_version:
            raise ApiMethodVersionError(method_name,
                                        self._api_version,
                                        since=float(since),
                                        deprecated=deprecated)

    def _check_param_versions(self,
                              method_name,
                              params):
        """
        Checks parameters against the initialized api_version of the service.

        :param method_name: service method name performing the check.
        :type method_name: str

        :param params: the list of versioned parameters, their value, inception
            version, and optionally, their deprecation version as a tuple
        :type params: list of tuple

        :raise ApiParameterVersionError: if the configured version of the
            ServiceBase is less then the inception version of the parameter.
            Deprecation is not currently checked.
        """
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
