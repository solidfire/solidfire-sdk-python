#!/usr/bin/env python
"""Copyright (c) NetApp Inc. 2016."""

from solidfire.common import ApiServerError, ApiConnectionError
from solidfire.factory import ElementFactory
from tests.base_test import SolidFireBaseTest


class TestRequestsMod(SolidFireBaseTest):
    def test_paved_road(self):
        e = ElementFactory.create(self.cluster, self.user, self.pwd)
        res = e.list_cluster_faults()
        self.assertIsNotNone(res)

    def test_bad_login(self):
        with self.assertRaises(ApiConnectionError) as context:
            ElementFactory.create(self.cluster, "foo", self.pwd)
        self.assertTrue('AuthorizationError' in str(context.exception))

    def test_timeout(self):
        with self.assertRaises(ApiConnectionError) as context:
            ElementFactory.create("10.117.61.132", self.user, self.pwd, timeout=5)
        self.assertTrue('ConnectTimeout' in str(context.exception))

    def test_exception_handler(self):
        with self.assertRaises(ApiServerError) as context:
            sf = ElementFactory.create(self.cluster, self.user, self.pwd)
            sf.add_drives(None)
        self.assertTrue('ApiServerError' in str(context.exception))
