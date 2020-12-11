#!/usr/bin/env python

import json

from solidfire.common import ApiServerError
from solidfire.factory import ElementFactory
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

    def test_should_handle_space(self):
        api_error = ApiServerError('aMethod', ' ')

        self.assertEqual(api_error.error_name, 'Unknown')
        self.assertEqual(api_error.error_code, 500)
        self.assertEqual(api_error.message, None)

    def test_should_handle_number(self):
        api_error = ApiServerError('aMethod', 1)

        self.assertEqual(api_error.error_name, 'Unknown')
        self.assertEqual(api_error.error_code, 500)
        self.assertEqual(api_error.message, None)

    def test_should_handle_dict(self):
        api_error = ApiServerError('aMethod', {})

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


    def test_should_map_dict(self):
        method_name = "api_method_name"
        response = dict()
        response["error"] = {}
        response["error"]["code"] = 777
        response["error"]["name"] = "error_name"
        response["error"]["message"] = "error_message"
        api_error = ApiServerError(method_name, json.dumps(response))
        self.assertEqual(api_error.error_name, response["error"]["name"])
        self.assertEqual(api_error.error_code, response["error"]["code"])
        self.assertEqual(api_error.message, response["error"]["message"])
        self.assertEqual(api_error.method_name, method_name)

    #following tests needs working clusters to ping
    def test_should_map_API_errors(self):
        sf = ElementFactory.create(self.cluster, self.user, self.password)
        try:
            sf.get_account_by_name("hfeiruhguireshgruieshiurehsiuvhreush") #impossible name, intended API error
        except ApiServerError as error:
            err_tmp = json.loads(error._err_json)
            err_tmp.pop('id', None)
            dct_tmp = json.loads('{"error": {"code": 500, "message": "xUnknownAccount", "name": "xUnknownAccount"}}')
            self.assertEqual(sorted(err_tmp.items()) == sorted(dct_tmp.items()), True)
            self.assertEqual(error.method_name, "GetAccountByName")
            self.assertEqual(error.error_name, "xUnknownAccount")
            self.assertEqual(error.message, "xUnknownAccount")
            self.assertEqual(error.error_code, 500)

        try:
            sf.get_async_result("999999999") #impossible async handle, intended API error
        except ApiServerError as error:
            err_tmp = json.loads(error._err_json)
            err_tmp.pop('id', None)
            dct_tmp = json.loads( '{"error": {"code": 500, "message": "Async handle 999999999 does not exist.", "name": "xAsyncHandleDoesNotExist"}}')
            self.assertEqual(sorted(err_tmp.items()) == sorted(dct_tmp.items()), True)
            self.assertEqual(error.method_name, "GetAsyncResult")
            self.assertEqual(error.error_name, "xAsyncHandleDoesNotExist")
            self.assertEqual(error.message, "Async handle 999999999 does not exist.")
            self.assertEqual(error.error_code, 500)

        snap_mirror_enabled = sf.get_feature_status(feature="SnapMirror").features[0].enabled

        if not snap_mirror_enabled:
            try:
                sf.create_snap_mirror_endpoint("8.8.8.8", "admin", "admin") #bad ID, intended API error
            except ApiServerError as error:
                err_tmp = json.loads(error._err_json)
                err_tmp.pop('id', None)
                dct_tmp = json.loads('{"error": {"code": 500, "message": "SnapMirror feature not enabled, use the EnableFeature API method to enable it", "name": "xFeatureNotEnabled"}}')
                self.assertEqual(sorted(err_tmp.items()) == sorted(dct_tmp.items()), True)
                self.assertEqual(error.method_name, "CreateSnapMirrorEndpoint")
                self.assertEqual(error.error_name, "xFeatureNotEnabled")#
                self.assertEqual(error.message, "SnapMirror feature not enabled, use the EnableFeature API method to enable it")#
                self.assertEqual(error.error_code, 500)
