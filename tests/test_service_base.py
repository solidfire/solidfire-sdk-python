#!/usr/bin/env python

from unittest.case import TestCase

from hamcrest import \
    assert_that, equal_to, starts_with, calling, is_, not_, raises, ends_with

from solidfire.common import ServiceBase, ApiParameterVersionError, \
    ApiMethodVersionError


class NoOpDispatcher(object):
    def post(self, data):
        pass


class PassthroughDispatcher(object):
    def post(self, data):
        return data


class TestServiceBase(TestCase):
    def test_should_default_api_version_to_8(self):
        service = ServiceBase()
        assert_that(service._api_version, equal_to(8.0))

    def test_should_map_api_version(self):
        service = ServiceBase(api_version=9.0)
        assert_that(service._api_version, equal_to(9.0))

    def test_endpoint_should_be_secure(self):
        service = ServiceBase()
        assert_that(service._dispatcher._endpoint, starts_with("https"))

    def test_should_construct_endpoint(self):
        service = ServiceBase(mvip="127.0.0.1", api_version=9.0)
        assert_that(service._dispatcher._endpoint,
                    equal_to("https://127.0.0.1/json-rpc/9.0"))

    def test_should_pass_username_to_dispatcher(self):
        service = ServiceBase(mvip="127.0.0.1",
                              api_version=9.0,
                              username="fake_username")
        assert_that(service._dispatcher._credentials,
                    starts_with("fake_username"))

    def test_should_pass_password_to_dispatcher(self):
        service = ServiceBase(mvip="127.0.0.1",
                              api_version=9.0,
                              password="fake_password")
        assert_that(service._dispatcher._credentials,
                    ends_with("fake_password"))

    def test_should_default_verify_ssl_to_True(self):
        service = ServiceBase()
        assert_that(service._dispatcher._verify_ssl, is_(True))

    def test_should_pass_verify_ssl(self):
        service = ServiceBase(verify_ssl=False)
        assert_that(service._dispatcher._verify_ssl, is_(False))


class ServiceBaseCheckMethodVersion(TestCase):
    def test_should_not_raise_api_parameter_version_err_with_no_since(self):
        service = ServiceBase(api_version=9.0)
        assert_that(
            calling(service._check_method_version).with_args("aMethod", None),
            not_(raises(ApiParameterVersionError))
        )

    def test_should_not_raise_api_parameter_version_err_with_lower_version(
            self):
        service = ServiceBase(api_version=9.0)
        assert_that(
            calling(service._check_method_version).with_args("aMethod", 8.0),
            not_(raises(ApiParameterVersionError))
        )

    def test_should_not_raise_api_parameter_version_err_with_version_match(
            self):
        service = ServiceBase(api_version=9.0)
        assert_that(
            calling(service._check_method_version).with_args("aMethod", 9.0),
            not_(raises(ApiParameterVersionError))
        )

    def test_should_raise_api_method_version_err(self):
        service = ServiceBase(api_version=9.0)
        assert_that(
            calling(service._check_method_version).with_args("aMethod", 10.0),
            raises(ApiMethodVersionError)
        )


class ServiceBaseCheckParamVersion(TestCase):
    def test_should_not_raise_api_parameter_version_err_with_no_params(self):
        service = ServiceBase(api_version=9.0)
        assert_that(
            calling(service._check_param_versions).with_args("aMethod", None),
            not_(raises(ApiParameterVersionError))
        )

    def test_should_not_raise_api_method_version_err_with_empty_params(
            self):
        service = ServiceBase(api_version=9.0)
        assert_that(
            calling(service._check_param_versions).with_args("aMethod", []),
            not_(raises(ApiMethodVersionError))
        )

    def test_should_not_raise_api_parameter_version_err_with_lesser_version(
            self):
        service = ServiceBase(api_version=9.0)
        assert_that(
            calling(service._check_param_versions).with_args(
                "aMethod", [("aParam", "aValue", 8.0, None)]),
            not_(raises(ApiParameterVersionError))
        )

    def test_should_not_raise_api_parameter_version_err_with_matching_version(
            self):
        service = ServiceBase(api_version=9.0)
        assert_that(
            calling(service._check_param_versions).with_args(
                "aMethod", [("aParam", "aValue", 9.0, None)]),
            not_(raises(ApiParameterVersionError))
        )

    def test_should_raise_api_parameter_version_err_with_greater_version(self):
        service = ServiceBase(api_version=9.0)
        assert_that(
            calling(service._check_param_versions).with_args(
                "aMethod", [("aParam", "aValue", 10.0, None)]),
            raises(ApiParameterVersionError,
                   ".*Invalid Parameters: \['aParam \(version: 10.0\)'\]"
                   )
        )

    def test_should_raise_api_parameter_version_err_with_multiple_greater(
            self):
        service = ServiceBase(api_version=9.0)
        assert_that(
            calling(service._check_param_versions).with_args(
                "aMethod",
                [
                    ("aParam", "aValue", 10.0, None),
                    ("2ndParam", "2ndValue", 11.0, None)
                ]),
            raises(ApiParameterVersionError,
                   ".*Invalid Parameters: \["
                   "'aParam \(version: 10.0\)', "
                   "'2ndParam \(version: 11.0\)'"
                   "\]"
                   )
        )


class ServiceBaseSendRequest(TestCase):
    def test_should_raise_api_method_version_err_with_no_params(self):
        service = ServiceBase(api_version=9.0, dispatcher=NoOpDispatcher)
        assert_that(
            calling(
                service.send_request
            ).with_args("aMethod", None, since=10.0),
            raises(ApiMethodVersionError)
        )
