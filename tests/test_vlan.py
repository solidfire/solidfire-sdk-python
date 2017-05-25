import unittest

from solidfire.factory import ElementFactory
from tests.base_test import SolidFireBaseTest


class TestSchedule(SolidFireBaseTest):

    @unittest.skip
    def test_create_and_delete_schedule(self):
        sf = ElementFactory.create("172.26.64.48", "admin", "admin")

        vlans = sf.list_virtual_networks().virtual_networks

        for vlan in vlans:
            print(vlan)
            the_vlan = vlan

        sf.modify_virtual_network(
            virtual_network_id=the_vlan.virtual_network_id, name="VLAN-3332")


        vlans = sf.list_virtual_networks().virtual_networks

        for vlan in vlans:
            print(vlan)
