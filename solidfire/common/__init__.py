#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright &copy; 2014-2016 NetApp, Inc. All Rights Reserved.
#
# CONFIDENTIALITY NOTICE: THIS SOFTWARE CONTAINS CONFIDENTIAL INFORMATION OF
# NETAPP, INC. USE, DISCLOSURE OR REPRODUCTION IS PROHIBITED WITHOUT THE PRIOR
# EXPRESS WRITTEN PERMISSION OF NETAPP, INC.
"""API Common Library"""

import itertools
import json
import logging

import requests
from requests.auth import HTTPBasicAuth
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

from solidfire.common import model

LOG = logging.getLogger('solidfire.Element')
LOG.setLevel(logging.INFO)
CH = logging.StreamHandler()
CH.setLevel(logging.INFO)
FORMATTER = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
CH.setFormatter(FORMATTER)
LOG.addHandler(CH)

ATOMIC_COUNTER = itertools.count()


def setLogLevel(level):
    """
    Set the logging level of Element logger and all handlers.

    >>> from logging
    >>> from solidfire import common
    >>> common.setLogLevel(logging.DEBUG)

    :param level: level must be an int or a str.
    """
    LOG.setLevel(level)
    for handler in LOG.handlers:
        handler.setLevel(level)


class SdkOperationError(Exception):
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)


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
        #if isinstance(err_json, str):
        #    err_json = '{}'

        self._method_name = method_name
        self._err_json = err_json
        Exception.__init__(self)

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
        maybeDict = json.loads(self._err_json)
        if isinstance(maybeDict, str):
            maybeDict = json.loads(maybeDict)
        return maybeDict.get('error', {}).get('name', 'Unknown')

    @property
    def error_code(self):
        """The numeric code for this error."""
        maybeDict = json.loads(self._err_json)
        if isinstance(maybeDict, str):
            maybeDict = json.loads(maybeDict)
        return int(maybeDict.get('error', {}).get('code', 500))

    @property
    def message(self):
        """A user-friendly message returned from the server."""
        try:
            json_err = json.loads(self._err_json)
            return json_err.get('error', {}).get('message', None)
        except:
            return self._err_json


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
        Exception.__init__(self)

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
        Exception.__init__(self)

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
        Exception.__init__(self)

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
        Exception.__init__(self)

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

class ApiConnectionError(Exception):
    def __init__(self, message):
        super(ApiConnectionError, self).__init__(message)

class CurlDispatcher(object):
    """
    The CurlDispatcher is responsible for connecting, sending, and receiving
    data to a server.
    """

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
        self._username = username
        self._password = password
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
        auth = None
        if self._username is None or self._password is None:
            raise ValueError("Username or Password is not set")
        else:
            auth = HTTPBasicAuth(self._username, self._password)
        resp = requests.post(self._endpoint, data=data, json=None,
                             verify=self._verify_ssl, timeout=self._timeout,
                             auth=auth)
        if resp.text == '':
             return {"code": resp.status_code, "name":  resp.reason, "message": ""}
        return resp.text


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
        self._private_keys = ["clusterPairingKey", "volumePairingKey", "password", "initiatorSecret", "scriptParameters", "targetSecret", "searchBindPassword"]

        endpoint = str.format('https://{mvip}/json-rpc/{api_version}',
                              mvip=mvip, api_version=self._api_version)
        if 'https' in endpoint:
            self._port = 443
        else:
            self._port = ''

        if not dispatcher:
            dispatcher = CurlDispatcher(endpoint, username, password,
                                        verify_ssl)
        self._dispatcher = dispatcher

        if mvip is not None:
            mvipArr = mvip.split(':')
            if len(mvipArr) == 2:
                self._port = mvipArr[1]

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

    @property
    def api_version(self):
        """
        Returns the version of the Element API

        :return: the version of the Element API
        :rtype: float
        """
        return self._api_version

    def send_request(self, method_name,
                     result_type,
                     params=None,
                     since=None,
                     deprecated=None,
                     return_response_raw=False):
        """
        :param method_name: the name of the API method to call
        :type method_name: str

        :param result_type: the type of the result object returned from the API
            method called.
        :type result_type: DataObject

        :param params: the parameters supplied to the API call.
        :type params: dict

        :param since: the first version this service was available
        :type since: str or float

        :param deprecated: the final version this service was available
        :type deprecated: str or float

        :return: the result of the API service call
        :rtype: DataObject
        """

        self._check_method_version(method_name, since, deprecated)

        if params is None:
            params = {}

        global ATOMIC_COUNTER
        if hasattr(ATOMIC_COUNTER, 'next'):
            atomic_id = ATOMIC_COUNTER.next()
        else:
            atomic_id = ATOMIC_COUNTER.__next__()

        request_dict = {
            'method': method_name,
            'id': atomic_id if atomic_id > 0 else 0,
            'params': dict(
                 (name, model.serialize(val))
                 for name, val in params.items()
             ),
        }
        obfuscated_request_raw = json.dumps(self._obfuscate_keys(request_dict))
        encoded = json.dumps(request_dict)

        try:
            LOG.info(msg=obfuscated_request_raw)
            response_raw = self._dispatcher.post(encoded)
        except requests.ConnectionError as e:
            if ("Errno 8" in str(e)):
                raise ApiConnectionError("Unknown host based on target.")
            elif ("Errno 60" in str(e)):
                raise ApiConnectionError("Connection timed out.")
            elif ("Errno 61" in str(e)):
                raise ApiConnectionError("Connection Refused. Confirm your target is a SolidFire cluster or node.")
            elif ("Errno 51" in str(e)):
                raise ApiConnectionError("Network is unreachable")
            raise ApiConnectionError(e)
        except requests.exceptions.ChunkedEncodingError as error:
            raise ApiConnectionError(error.args)
        except Exception as error:
            # if 2 <= len(error.args):
            #     json_err = json.dumps(
            #         {
            #             'error':
            #                 {
            #                     'name': str(error.__class__).split('\'')[1],
            #                     'code': 500,
            #                     'message': error.args[1].__str__()
            #                 }
            #         }
            #     )
            # else:
            #     json_err = json.dumps(
            #         {
            #             'error':
            #                 {
            #                     'name': str(error.__class__).split('\'')[1],
            #                     'code': 500,
            #                     'message': error.args.__str__()
            #                 }
            #         }
            #     )
            raise ApiServerError(method_name, error)


        # noinspection PyBroadException
        LOG.debug(msg=response_raw)
        if isinstance(response_raw, dict): #if isinstance(response_raw, dict) and "name" in response_raw and "code" in response_raw:
            response = {
                    'error': response_raw
                }
        else:
            try:
                response = json.loads(response_raw)
                LOG.debug(msg=response_raw)
            except Exception as error:
                LOG.error(msg=response_raw)
                if "401 Unauthorized." in response_raw:
                    # json_err = {
                    #         'error':
                    #             {
                    #                 'name': 'AuthorizationError',
                    #                 'code': 401,
                    #                 'message': 'Username or password incorrect.'
                    #             }
                    #     }
                    #raise ApiConnectionError(json_err)
                    raise ApiConnectionError("Bad Credentials")


                if "404 Not Found" in response_raw:
                    # json_err = {
                    #         'error':
                    #             {
                    #                 'name': 'NotFoundError',
                    #                 'code': 404,
                    #                 'message': 'The connection was not found.'
                    #             }
                    #     }
                    # raise ApiConnectionError(json_err)
                    raise ApiConnectionError("404 Not Found")
                response =  {
                        'error':
                            {
                                'name': 'JSONDecodeError',
                                'code': 400,
                                'message': str(error)
                            }
                    }

        if return_response_raw:
            return response_raw

        if 'error' in response:
            if response["error"]["code"] == 400:
                raise requests.HTTPError(str(response["error"]["code"]) + " " + response["error"]["name"] + " " +
                                         response["error"]["message"])
            else:
                raise ApiServerError(method_name,
                                     str(response["error"]["code"]) + " " + response["error"]["name"] + " " +
                                     response["error"]["message"])
        else:
            return model.extract(result_type, response['result'])

    # For logging purposes, there are a set of keys we don't want to be in plain text.
    # This goes through the response and obfuscates the secret keys.
    def _obfuscate_keys(self, response, obfuscate = False):
        if type(response) == dict:
            private_dict = dict()
            for key in response:
                if key in self._private_keys:
                    private_dict[key] = self._obfuscate_keys(response[key], True)
                else:
                    private_dict[key] = self._obfuscate_keys(response[key])
            return private_dict
        if type(response) == list:
            return [self._obfuscate_keys(item) for item in response]
        if obfuscate:
            return "*****"
        else:
            return response

    def _check_connection_type(self, method_name,
                               connection_type):
        """
        Check the connection type to verify that it is right.

        :param connection_type: connection type the method expects.
        :type connection_type: str
        """
        if(connection_type == "Cluster" and int(self._port) == 442):
            error = method_name+" cannot be called on a node connection. It is a cluster-only method."
            raise ApiConnectionError(error)
        elif(connection_type == "Node" and int(self._port) == 443):
            error = method_name+" cannot be called on a cluster connection. It is a node-only method."
            raise ApiConnectionError(error)


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
