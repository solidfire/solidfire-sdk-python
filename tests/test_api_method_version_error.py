#!/usr/bin/env python

from unittest.case import TestCase

from hamcrest import assert_that, equal_to

from solidfire.common import ApiMethodVersionError


class TestApiMethodVersionError(TestCase):
    def test_should_map_parameters(self):
        version_err = ApiMethodVersionError("aMethod", 7.0, 8.0)

        assert_that(version_err.method_name, equal_to('aMethod'))
        assert_that(version_err.api_version, equal_to(7.0))

    def test_should_default_deprecated_to_None(self):
        version_err = ApiMethodVersionError("aMethod", 7.0, 8.0)

        assert_that(version_err._deprecated, equal_to(None))

    def test_repr_evals_no_json(self):
        version_err = ApiMethodVersionError("aMethod", 7.0, 8.0)

        assert_that(eval(repr(version_err)), version_err)

    def test_repr_evals(self):
        version_err = ApiMethodVersionError("aMethod", 7.0, 8.0)

        assert_that(eval(repr(version_err)), version_err)
