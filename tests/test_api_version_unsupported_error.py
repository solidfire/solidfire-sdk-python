#!/usr/bin/env python

from unittest.case import TestCase

from hamcrest import assert_that, equal_to

from solidfire.common import ApiVersionUnsupportedError


class TestApiVersionUnsupportedError(TestCase):
    def test_should_map_parameters(self):
        version_err = ApiVersionUnsupportedError(8.0, [6.0, 7.0])

        assert_that(version_err.api_version, equal_to(8.0))
        assert_that(version_err.supported_versions, equal_to([6.0, 7.0]))

    def test_repr_evals(self):
        version_err = ApiVersionUnsupportedError(8.0, [6.0, 7.0])

        assert_that(eval(repr(version_err)), version_err)
