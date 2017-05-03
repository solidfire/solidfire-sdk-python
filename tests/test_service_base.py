#!/usr/bin/env python

from unittest.case import TestCase

from solidfire.common import ServiceBase, ApiParameterVersionError, \
    ApiMethodVersionError
from tests.base_test import SolidFireBaseTest


class NoOpDispatcher(object):
    def post(self, data):
        pass


class PassthroughDispatcher(object):
    def post(self, data):
        return data


class TestServiceBase(SolidFireBaseTest):
    def test_should_default_api_version_to_8(self):
        service = ServiceBase()
        self.assertEquals(service._api_version, 8.0)

    def test_should_map_api_version(self):
        service = ServiceBase(api_version=9.0)
        self.assertEquals(service._api_version, 9.0)

    def test_endpoint_should_be_secure(self):
        service = ServiceBase()
        self.assertTrue("https" in service._dispatcher._endpoint)

    def test_should_construct_endpoint(self):
        service = ServiceBase(mvip="127.0.0.1", api_version=9.0)
        self.assertEquals(service._dispatcher._endpoint, "https://127.0.0.1/json-rpc/9.0")

    def test_should_pass_username_to_dispatcher(self):
        service = ServiceBase(mvip="127.0.0.1",
                              api_version=9.0,
                              username="fake_username")
        self.assertTrue("fake_username" in service._dispatcher._username)

    def test_should_pass_password_to_dispatcher(self):
        service = ServiceBase(mvip="127.0.0.1",
                              api_version=9.0,
                              password="fake_password")
        self.assertTrue("fake_password" in service._dispatcher._password)

    def test_should_default_verify_ssl_to_True(self):
        service = ServiceBase()
        self.assertTrue(service._dispatcher._verify_ssl)

    def test_should_pass_verify_ssl(self):
        service = ServiceBase(verify_ssl=False)
        self.assertFalse(service._dispatcher._verify_ssl)

    def test_should_raise_api_method_version_err(self):
        service = ServiceBase(api_version=9.0)

        with self.assertRaises(ApiMethodVersionError) as context:
            service._check_method_version("aMethod", 10.0)

    def test_should_raise_api_method_version_err_with_no_params(self):
        service = ServiceBase(api_version=9.0, dispatcher=NoOpDispatcher)

        with self.assertRaises(ApiMethodVersionError) as context:
            service.send_request("aMethod", None, since=10.0)
