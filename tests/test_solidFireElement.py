#!/usr/bin/env python
from unittest import TestCase

import pytest

from solidfire.element.api.SolidFireElement import SolidFireElement
from test_element import server

__author__ = 'ahaid'


@pytest.skip
class TestSolidFireElement(TestCase):
    def test_list_accounts(self):
        sfe = SolidFireElement
        accounts = server.list_accounts(1, 1)

