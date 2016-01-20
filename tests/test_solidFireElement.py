#!/usr/bin/env python3

# from unittest import TestCase

from solidfire.element.api.SolidFireElement import SolidFireElement


__author__ = 'ahaid'


class TestSolidFireElement(TestCase):
    def test_list_accounts(self):
        sfe = SolidFireElement
        accounts = sfe.list_accounts(sfe, 1, 1)

        self.fail()
