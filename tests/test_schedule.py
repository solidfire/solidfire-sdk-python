import unittest

from solidfire.common import ApiServerError

from solidfire.adaptor import ScheduleAdaptor
from solidfire.custom.models import *
from solidfire.models import *
from solidfire.factory import ElementFactory
import logging
from solidfire import common
from tests.base_test import SolidFireBaseTest

common.setLogLevel(logging.DEBUG)


class TestSchedule(SolidFireBaseTest):

    @classmethod
    def setUpClass(cls):
        cls.sf = ElementFactory.create(cls.cluster, cls.user, cls.pwd)
        cls.scheduleName = "pythonSDKUnitTestSchedule"

    def test_create_and_delete_schedule(self):
    
        vols = self.sf.list_volumes().volumes
        vol_ids = []
        for vol in vols:
            vol_ids.append(vol.volume_id)

        sched = Schedule(
            schedule_info=ScheduleInfo(volume_ids=vol_ids),
            name=self.scheduleName,
            frequency=TimeIntervalFrequency(hours=4, minutes=30, days=2)
        )

        result = self.sf.create_schedule(sched)

        new_sched_id = result.schedule_id

        new_sched = self.sf.get_schedule(new_sched_id).schedule

        self.assertEquals(new_sched.name, self.scheduleName)
        self.assertEquals(type(new_sched.frequency) is TimeIntervalFrequency,
                          True)
        if type(new_sched.frequency) is TimeIntervalFrequency:
            self.assertEquals(new_sched.frequency.hours, 4)
            self.assertEquals(new_sched.frequency.days, 2)
            self.assertEquals(new_sched.frequency.minutes, 30)
        self.assertEquals(new_sched.last_run_time_started, None)
        self.assertEquals(new_sched.schedule_info.volume_ids, vol_ids)
        self.assertGreater(new_sched.schedule_id, 0)
        self.assertEquals(new_sched.recurring, False)
        self.assertEquals(new_sched.paused, False)
        self.assertEquals(new_sched.to_be_deleted, False)
        self.assertEquals(new_sched.starting_date, None)
        self.assertEquals(new_sched.has_error, False)
        self.assertEquals(new_sched.run_next_interval, False)
        self.assertEquals(new_sched.schedule_info.snapshot_name, None)

        new_sched.to_be_deleted = True
        self.sf.modify_schedule(new_sched)

        deleted_sched = self.sf.get_schedule(new_sched_id).schedule
        self.assertEquals(deleted_sched.to_be_deleted, True)

    def test_create_but_missing_schedule_info(self):
        sf = ElementFactory.create(self.cluster, self.user, self.pwd)

        with self.assertRaises(TypeError) as context:
            sched = Schedule(
                name=self.scheduleName,
                frequency=TimeIntervalFrequency(hours=4, minutes=None, days=None)
            )

        self.assertTrue("missing 1 required positional argument: 'schedule_info'" in str(context.exception))

    def test_create_but_missing_frequency(self):
        sf = ElementFactory.create(self.cluster, self.user, self.pwd)

        with self.assertRaises(TypeError) as context:
            sched = Schedule(name=self.scheduleName)

        self.assertTrue("missing 2 required positional arguments: 'schedule_info' and 'frequency'" in str(context.exception))

    def test_create_but_volume_does_not_exist(self):
        sf = ElementFactory.create(self.cluster, self.user, self.pwd)

        sched = Schedule(
            schedule_info=ScheduleInfo(volume_ids=[1]),
            name=self.scheduleName,
            frequency=TimeIntervalFrequency(hours=4, minutes=None, days=None)
        )
        with self.assertRaises(ApiServerError) as context:
            result = self.sf.create_schedule(sched)

        self.assertTrue("xVolumeIDDoesNotExist" in str(context.exception))

    def test_create_but_schedule_info_volumes_empty(self):
        sf = ElementFactory.create(self.cluster, self.user, self.pwd)

        sched = Schedule(
            schedule_info=ScheduleInfo(),
            name=self.scheduleName,
            frequency=TimeIntervalFrequency(hours=4, minutes=30, days=2)
        )

        with self.assertRaises(AttributeError) as context:
            self.sf.create_schedule(sched)

        self.assertTrue('ScheduleInfo.VolumeIDs are missing.' in str(context.exception))

    def test_schedule_to_api_achedule(self):
        freq = TimeIntervalFrequency(hours=4, minutes=30, days=2)
        info = ScheduleInfo(volume_ids=[1, 4])
        sched = Schedule(name=self.scheduleName, frequency=freq, schedule_info=info)

        api_sched = ScheduleAdaptor.to_api_schedule(sched)

        self.assertEquals(api_sched.schedule_name, self.scheduleName)
        self.assertEquals(api_sched.hours, 52)
        self.assertEquals(api_sched.attributes['frequency'],
                          "Time Interval")
        self.assertEquals(api_sched.schedule_info.volumes, [1, 4])

    def test_lest_schedules(self):
        sf = ElementFactory.create(self.cluster, self.user, self.pwd)

        results = self.sf.list_schedules()

        for sched in results.schedules:
            freq = sched.frequency
            self.assertNotEqual(freq, None)

    @unittest.skip("Test seems to depend on a specific cluster or configuration.")
    def test_get_schedule(self):
        sf = ElementFactory.create(self.cluster, self.user, self.pwd)
        results = self.sf.get_schedule(786)

        for sched in results.schedules:
            self.assertEquals(sched.frequency is None, True)

    def test_change_frequency_dom_to_dow(self):
        sf = ElementFactory.create(self.cluster, self.user, self.pwd)

        vols = self.sf.list_volumes().volumes
        vol_ids = []
        for vol in vols:
            vol_ids.append(vol.volume_id)

        sched = Schedule(
            schedule_info=ScheduleInfo(
                volume_ids=vol_ids),
            name=self.scheduleName,
            frequency=DaysOfMonthFrequency(
                hours=4,
                minutes=30,
                monthdays=[2])
        )

        result = self.sf.create_schedule(sched)

        new_sched_id = result.schedule_id

        new_sched = self.sf.get_schedule(new_sched_id).schedule

        new_sched.frequency = DaysOfWeekFrequency(hours=5, weekdays=[
            Weekday.from_id(1), Weekday.from_id(4)])

        modified_sched = self.sf.modify_schedule(new_sched).schedule

    def test_change_frequency_dow_to_dom(self):
        sf = ElementFactory.create(self.cluster, self.user, self.pwd)

        vols = self.sf.list_volumes().volumes
        vol_ids = []
        for vol in vols:
            vol_ids.append(vol.volume_id)

        sched = Schedule(
            schedule_info=ScheduleInfo(
                volume_ids=vol_ids),
            name=self.scheduleName,
            frequency=DaysOfWeekFrequency(hours=4, minutes=30,
                                          weekdays=[
                                              Weekday.from_id(1),
                                              Weekday.from_id(4)])
        )

        result = self.sf.create_schedule(sched)

        new_sched_id = result.schedule_id

        new_sched = self.sf.get_schedule(new_sched_id).schedule

        new_sched.frequency = DaysOfMonthFrequency(hours=5, monthdays=[4, 5])

        modified_sched = self.sf.modify_schedule(new_sched).schedule

    def test_change_frequency_dow_to_ti(self):
        sf = ElementFactory.create(self.cluster, self.user, self.pwd)

        vols = self.sf.list_volumes().volumes
        vol_ids = []
        for vol in vols:
            vol_ids.append(vol.volume_id)

        sched = Schedule(
            schedule_info=ScheduleInfo(
                volume_ids=vol_ids),
            name=self.scheduleName,
            frequency=DaysOfWeekFrequency(hours=4, minutes=30,
                                          weekdays=[
                                              Weekday.from_id(1),
                                              Weekday.from_id(4)])
        )

        result = self.sf.create_schedule(sched)

        new_sched_id = result.schedule_id

        new_sched = self.sf.get_schedule(new_sched_id).schedule

        new_sched.frequency = TimeIntervalFrequency(hours=5, days=1)

        modified_sched = self.sf.modify_schedule(new_sched).schedule

    def test_change_frequency_ti_to_dom(self):
        sf = ElementFactory.create(self.cluster, self.user, self.pwd)

        vols = self.sf.list_volumes().volumes
        vol_ids = []
        for vol in vols:
            vol_ids.append(vol.volume_id)

        sched = Schedule(
            schedule_info=ScheduleInfo(
                volume_ids=vol_ids),
            name=self.scheduleName,
            frequency=TimeIntervalFrequency(hours=5, days=1)
        )

        result = self.sf.create_schedule(sched)

        new_sched_id = result.schedule_id

        new_sched = self.sf.get_schedule(new_sched_id).schedule

        new_sched.frequency = DaysOfWeekFrequency(hours=4, minutes=30,
                                                  weekdays=[
                                                      Weekday.from_id(1),
                                                      Weekday.from_id(4)])

        modified_sched = self.sf.modify_schedule(new_sched).schedule

    @classmethod
    def tearDownClass(cls):
        for schedule in cls.sf.list_schedules().schedules:
            if schedule.name == cls.scheduleName:
                schedule.to_be_deleted = True
                cls.sf.modify_schedule(schedule)
