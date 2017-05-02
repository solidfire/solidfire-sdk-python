#!/usr/bin/env python
"""Copyright (c) NetApp Inc. 2016."""

import unittest
from solidfire.factory import ElementFactory
from solidfire import Schedule


class SolidFireBaseTest(unittest.TestCase):
    cluster = "10.117.61.42"
    user = "admin"
    pwd = "admin"
