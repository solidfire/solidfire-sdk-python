#!/usr/bin/env python

from unittest.case import TestCase

from hamcrest import assert_that, equal_to

from solidfire.common import ApiVersionExceededError


class TestApiVersionExceededError(TestCase):
    def test_should_map_parameters(self):
        version_err = ApiVersionExceededError(7.0, 8.0)

        assert_that(version_err.api_version, equal_to(7.0))
        assert_that(version_err.current_version, equal_to(8.0))

    def test_repr_evals(self):
        version_err = ApiVersionExceededError(7.0, 8.0)

        assert_that(eval(repr(version_err)), version_err)
