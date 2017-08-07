#!/usr/bin/env python
"""Copyright (c) NetApp Inc. 2016."""

import simplejson

from models import ListVolumesResult
from solidfire.common import model
from tests.base_test import SolidFireBaseTest


class TestForwardCompatible(SolidFireBaseTest):

    def test_can_deserialize_when_extra_fields_present_in_json(self):

        with open("ListVolumes.json") as f:
            response = simplejson.load(f)
        list_volumes_result = model.extract(ListVolumesResult, response['result'])
        self.assertTrue(len(list_volumes_result.volumes) > 0)
