from solidfire.common import ApiServerError

from solidfire.factory import ElementFactory
from tests.base_test import SolidFireBaseTest


class TestRequiredParameters(SolidFireBaseTest):
    def test_paved_road(self):
        e = ElementFactory.create(self.cluster, self.user, self.password)
        with self.assertRaises(ApiServerError):
            e.add_account(username=None)
