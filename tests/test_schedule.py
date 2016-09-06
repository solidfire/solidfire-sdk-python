from unittest.case import TestCase

from hamcrest import \
    assert_that, equal_to, is_, greater_than

from solidfire.adaptor import ScheduleAdaptor
from solidfire.custom.models import *
from solidfire.models import *
from solidfire.factory import ElementFactory


class TestSchedule(TestCase):

    def test_create_and_delete_schedule(self):
        sf = ElementFactory.create("192.168.139.165", "admin", "admin")

        vols = sf.list_volumes().volumes
        vol_ids = []
        for vol in vols:
            vol_ids.append(vol.volume_id)

        sched = Schedule()
        sched.name = "mySchedule"
        sched.frequency = TimeIntervalFrequency(hours=4, minutes=30, days=2)
        sched.frequency.hours = 4
        sched.frequency.minutes = 30
        sched.frequency.days = 2
        sched.schedule_info = ScheduleInfo()
        sched.schedule_info.volume_ids = vol_ids

        result = sf.create_schedule(sched)

        new_sched_id = result.schedule_id

        print(new_sched_id)

        new_sched = sf.get_schedule(new_sched_id).schedule

        assert_that(new_sched.name, equal_to("mySchedule"))
        assert_that(type(new_sched.frequency) is (TimeIntervalFrequency),
                    equal_to(True))
        if type(new_sched.frequency) is TimeIntervalFrequency:
            assert_that(new_sched.frequency.hours, equal_to(4))
            assert_that(new_sched.frequency.days, equal_to(2))
            assert_that(new_sched.frequency.minutes, equal_to(30))
        assert_that(new_sched.schedule_info.volume_ids, equal_to(vol_ids))
        assert_that(new_sched.schedule_id, greater_than(0))
        assert_that(new_sched.recurring, equal_to(True))
        assert_that(new_sched.paused, equal_to(False))
        assert_that(new_sched.to_be_deleted, equal_to(False))
        assert_that(new_sched.starting_date, equal_to(None))
        assert_that(new_sched.has_error, equal_to(False))
        assert_that(new_sched.run_next_interval, equal_to(False))
        assert_that(new_sched.schedule_info.snapshot_name, equal_to(None))

        new_sched.to_be_deleted = True
        sf.modify_schedule(new_sched)

        deleted_sched = sf.get_schedule(new_sched_id).schedule
        assert_that(deleted_sched.to_be_deleted, equal_to(True))

    def test_create_but_missing_schedule_info(self):
        sf = ElementFactory.create("192.168.139.165", "admin", "admin")

        sched = Schedule()
        sched.name = "mySchedule"
        sched.frequency = TimeIntervalFrequency(hours=4, minutes=30, days=2)
        sched.frequency.hours = 4
        sched.frequency.minutes = 30
        sched.frequency.days = 2

        result = sf.create_schedule(sched)

    def test_create_but_missing_frequency(self):
        sf = ElementFactory.create("192.168.139.165", "admin", "admin")

        sched = Schedule()
        sched.name = "mySchedule"

        result = sf.create_schedule(sched)

    def test_create_but_missing_schedule_info_volumes(self):
        sf = ElementFactory.create("192.168.139.165", "admin", "admin")

        sched = Schedule()
        sched.name = "mySchedule"
        sched.frequency = TimeIntervalFrequency(hours=4, minutes=30, days=2)
        sched.frequency.hours = 4
        sched.frequency.minutes = 30
        sched.frequency.days = 2
        sched.schedule_info = ScheduleInfo()

        result = sf.create_schedule(sched)

    def test_create_but_time_interval_days_minutes_is_None(self):
        sf = ElementFactory.create("192.168.139.165", "admin", "admin")

        sched = Schedule()
        sched.name = "mySchedule"
        sched.frequency = TimeIntervalFrequency(hours=4)
        sched.schedule_info = ScheduleInfo()
        sched.schedule_info.volume_ids = [1]

        result = sf.create_schedule(sched)

    def test_create_but_time_interval_days_minutes_is_None(self):
        sf = ElementFactory.create("192.168.139.165", "admin", "admin")

        sched = Schedule()
        sched.name = "mySchedule"
        sched.frequency = TimeIntervalFrequency(hours=21, minutes=None,
                                                days=None)
        sched.schedule_info = ScheduleInfo()
        sched.schedule_info.volume_ids = [1]

        print(sched)

        result = sf.create_schedule(sched)

    def test_create_but_schedule_info_volumes_empty(self):
        sf = ElementFactory.create("192.168.139.165", "admin", "admin")

        sched = Schedule()
        sched.name = "mySchedule"
        sched.frequency = TimeIntervalFrequency(hours=4, minutes=30, days=2)
        sched.frequency.hours = 4
        sched.frequency.minutes = 30
        sched.frequency.days = 2
        sched.schedule_info = ScheduleInfo()
        sched.schedule_info.volume_ids = []
        result = sf.create_schedule(sched)


    def test_schedule_to_api_achedule(self):
        freq = TimeIntervalFrequency(hours=4, minutes=30, days=2)
        info = ScheduleInfo(volume_ids = [1, 4])
        sched = Schedule(name="mySchedule", frequency=freq, schedule_info=info)

        api_sched = ScheduleAdaptor.to_api_schedule(sched)

        assert_that(api_sched.schedule_name, equal_to("mySchedule"))
        assert_that(api_sched.hours, equal_to(52))
        assert_that(api_sched.attributes['frequency'],
                    equal_to("Time Interval"))
        assert_that(api_sched.schedule_info.volumes, equal_to([1, 4]))

    def test_lest_schedules(self):
        sf = ElementFactory.create("172.26.64.48", "admin", "admin")

        results = sf.list_schedules()

        for sched in results.schedules:
            assert_that(sched.frequency is None, equal_to(True))

