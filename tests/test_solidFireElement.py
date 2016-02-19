#!/usr/bin/env python
from unittest import TestCase

import pytest

from solidfire import Element
from test_element import server

__author__ = 'ahaid'


@pytest.skip
class TestSolidFireElement(TestCase):
    def test_list_accounts(self):
        sfe = Element
        accounts = server.list_accounts(1, 1)

