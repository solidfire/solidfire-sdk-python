#!/usr/bin/env python

import json

from solidfire.common import ApiServerError
from tests.base_test import SolidFireBaseTest


class TestApiServerError(SolidFireBaseTest):
    def test_should_provide_defaults_with_empty_string(self):
        api_error = ApiServerError('aMethod', '')

        self.assertEqual(api_error.error_name, 'Unknown')
        self.assertEqual(api_error.error_code, 500)
        self.assertEqual(api_error.message, None)

    def test_should_provide_defaults(self):
        api_error = ApiServerError('aMethod', '{}')

        self.assertEqual(api_error.error_name, 'Unknown')
        self.assertEqual(api_error.error_code, 500)
        self.assertEqual(api_error.message, None)

    def test_should_convert_code_to_int(self):
        api_error = ApiServerError('aMethod', '{"error": {"code": "404"}}')
        self.assertEqual(api_error.error_code, 404)

    def test_should_map_provided_json(self):
        api_error = ApiServerError(
            'aMethod',
            '{ \
                "error" : { \
                    "name": "error_name", \
                    "code": 505, \
                    "message": "aMessage" \
                } \
            }',
        )

        self.assertEqual(api_error.error_name, 'error_name')
        self.assertEqual(api_error.error_code, 505)
        self.assertEqual(api_error.message, 'aMessage')

