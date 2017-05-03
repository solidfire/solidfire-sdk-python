#!/usr/bin/env python
from solidfire.common import ApiVersionUnsupportedError

from tests.base_test import SolidFireBaseTest


class TestApiVersionUnsupportedError(SolidFireBaseTest):
    def test_should_map_parameters(self):
        version_err = ApiVersionUnsupportedError(8.0, [6.0, 7.0])

        self.assertEqual(version_err.api_version, 8.0)
        self.assertEqual(version_err.supported_versions, [6.0, 7.0])

