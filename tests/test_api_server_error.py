#!/usr/bin/env python

import json
from unittest.case import TestCase

from hamcrest import *

from solidfire.common import ApiServerError


class TestApiServerError(TestCase):
    def test_should_provide_defaults_with_None(self):
        api_error = ApiServerError('aMethod', None)

        assert_that(api_error.error_name, equal_to('Unknown'))
        assert_that(api_error.error_code, equal_to(500))
        assert_that(api_error.message, equal_to(None))

    def test_should_provide_defaults_with_empty_string(self):
        api_error = ApiServerError('aMethod', "")

        assert_that(api_error.error_name, equal_to('Unknown'))
        assert_that(api_error.error_code, equal_to(500))
        assert_that(api_error.message, equal_to(None))

    def test_should_provide_defaults_with_empty_string2(self):
        api_error = ApiServerError('aMethod', '')

        assert_that(api_error.error_name, equal_to('Unknown'))
        assert_that(api_error.error_code, equal_to(500))
        assert_that(api_error.message, equal_to(None))

    def test_should_provide_defaults_with_empty_dict(self):
        api_error = ApiServerError('aMethod', {})

        assert_that(api_error.error_name, equal_to('Unknown'))
        assert_that(api_error.error_code, equal_to(500))
        assert_that(api_error.message, equal_to(None))

    def test_should_provide_defaults(self):
        api_error = ApiServerError('aMethod', json.loads('{}'))

        assert_that(api_error.error_name, equal_to('Unknown'))
        assert_that(api_error.error_code, equal_to(500))
        assert_that(api_error.message, equal_to(None))

    def test_should_convert_code_to_int(self):
        api_error = ApiServerError('aMethod', json.loads('{"code": "404"}'))
        assert_that(api_error.error_code,
                    equal_to(404) and not (equal_to("404")))

    def test_should_map_provided_json(self):
        api_error = ApiServerError(
            'aMethod',
            json.loads('{ \
                            "name": "error_name", \
                            "code": 505, \
                            "message": "aMessage" \
                        }',
                       )
        )

        assert_that(api_error.error_name, equal_to('error_name'))
        assert_that(api_error.error_code, equal_to(505))
        assert_that(api_error.message, equal_to('aMessage'))

    def test_should_map_json(self):
        api_error = ApiServerError(
            'aMethod',
            json.loads(
                '{ \
                    "name": "error_name", \
                    "code": 505, \
                    "message": "aMessage" \
                 }',
            )
        )

        assert_that(api_error.error_name, equal_to('error_name'))
        assert_that(api_error.error_code, equal_to(505))
        assert_that(api_error.message, equal_to('aMessage'))

    def test_repr_evals_no_json(self):
        api_error = ApiServerError('aMethod', json.loads('{}', ))

        assert_that(eval(repr(api_error)), api_error)

    def test_repr_evals(self):
        api_error = ApiServerError(
            'aMethod',
            json.loads(
                '{ \
                    "name": "error_name", \
                    "code": 505, \
                    "message": "aMessage" \
                 }',
            )
        )

        assert_that(eval(repr(api_error)), api_error)

