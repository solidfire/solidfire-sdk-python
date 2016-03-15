#!/usr/bin/env python

from unittest.case import TestCase

from hamcrest import assert_that, equal_to

from solidfire.common import ApiVersionError


class TestApiVersionError(TestCase):
    def test_should_map_parameters(self):
        version_err = ApiVersionError("aMethod", 7.0)

        assert_that(version_err.method_name, equal_to('aMethod'))
        assert_that(version_err.api_version, equal_to(7.0))

    def test_should_default_since_to_None(self):
        version_err = ApiVersionError("aMethod", 7.0)

        assert_that(version_err._since, equal_to(None))

    def test_should_default_deprecated_to_None(self):
        version_err = ApiVersionError("aMethod", 7.0)

        assert_that(version_err._deprecated, equal_to(None))

    def test_should_default_violation_to_empty_array(self):
        version_err = ApiVersionError("aMethod", 7.0)

        assert_that(version_err._violations, equal_to([]))

    def test_should_map_params_to_violations(self):
        version_err = ApiVersionError(
            "aMethod",
            7.0,
            params=[("aName", "aValue", 8.0, 9.0)]
        )

        assert_that(version_err._violations,
                    equal_to(["aName (version: 8.0)"]))

    def test_repr_evals_no_json(self):
        version_err = ApiVersionError("aMethod", 7.0)

        assert_that(eval(repr(version_err)), version_err)

    def test_repr_evals(self):
        version_err = ApiVersionError(
            "aMethod",
            7.0,
            params=[("aName", "aValue", 8.0, 9.0)]
        )

        assert_that(eval(repr(version_err)), version_err)
