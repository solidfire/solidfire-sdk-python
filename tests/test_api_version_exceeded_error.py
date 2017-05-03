#!/usr/bin/env python
from solidfire.common import ApiVersionExceededError

from tests.base_test import SolidFireBaseTest


class TestApiVersionExceededError(SolidFireBaseTest):
    def test_should_map_parameters(self):
        version_err = ApiVersionExceededError(7.0, 8.0)

        self.assertEquals(version_err.api_version, 7.0)
        self.assertEquals(version_err.current_version, 8.0)

