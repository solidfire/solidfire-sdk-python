#!/usr/bin/env python

from solidfire.common import ApiMethodVersionError
from tests.base_test import SolidFireBaseTest


class TestApiMethodVersionError(SolidFireBaseTest):
    def test_should_map_parameters(self):
        version_err = ApiMethodVersionError("aMethod", 7.0, 8.0)

        self.assertEqual(version_err.method_name, 'aMethod')
        self.assertEqual(version_err.api_version, 7.0)

    def test_should_default_deprecated_to_None(self):
        version_err = ApiMethodVersionError("aMethod", 7.0, 8.0)

        self.assertEqual(version_err._deprecated, None)

