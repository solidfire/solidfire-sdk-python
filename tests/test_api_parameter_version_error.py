#!/usr/bin/env python

from solidfire.common import ApiParameterVersionError
from tests.base_test import SolidFireBaseTest


class TestApiParameterVersionError(SolidFireBaseTest):
    def test_should_map_parameters(self):
        version_err = ApiParameterVersionError("aMethod", 7.0, [])

        self.assertEqual(version_err.method_name, 'aMethod')
        self.assertEqual(version_err.api_version, 7.0)

    def test_should_default_violation_to_empty_array(self):
        version_err = ApiParameterVersionError("aMethod", 7.0, [])

        self.assertEqual(version_err._violations, [])

    def test_should_map_params_to_violations(self):
        version_err = ApiParameterVersionError(
            "aMethod",
            7.0,
            params=[("aName", "aValue", 8.0, None)]
        )

        self.assertEqual(version_err._violations,
                    ["aName (version: 8.0)"])

