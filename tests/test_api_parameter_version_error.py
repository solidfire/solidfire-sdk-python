#!/usr/bin/env python

from unittest.case import TestCase

from hamcrest import assert_that, equal_to

from solidfire.common import ApiParameterVersionError


class TestApiParameterVersionError(TestCase):
    def test_should_map_parameters(self):
        version_err = ApiParameterVersionError("aMethod", 7.0, [])

        assert_that(version_err.method_name, equal_to('aMethod'))
        assert_that(version_err.api_version, equal_to(7.0))

    def test_should_default_violation_to_empty_array(self):
        version_err = ApiParameterVersionError("aMethod", 7.0, [])

        assert_that(version_err._violations, equal_to([]))

    def test_should_map_params_to_violations(self):
        version_err = ApiParameterVersionError(
            "aMethod",
            7.0,
            params=[("aName", "aValue", 8.0, None)]
        )

        assert_that(version_err._violations,
                    equal_to(["aName (version: 8.0)"]))

    def test_repr_evals_no_params(self):
        version_err = ApiParameterVersionError("aMethod", 7.0, [])

        assert_that(eval(repr(version_err)), version_err)

    def test_repr_evals(self):
        version_err = ApiParameterVersionError(
            "aMethod",
            7.0,
            params=[("aName", "aValue", 8.0, None)]
        )

        assert_that(eval(repr(version_err)), version_err)
