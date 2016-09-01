#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright &copy; 2014-2016 NetApp, Inc. All Rights Reserved.
#
# CONFIDENTIALITY NOTICE: THIS SOFTWARE CONTAINS CONFIDENTIAL INFORMATION OF
# NETAPP, INC. USE, DISCLOSURE OR REPRODUCTION IS PROHIBITED WITHOUT THE PRIOR
# EXPRESS WRITTEN PERMISSION OF NETAPP, INC.
"""Module implements Schedule Simplification conversion logic."""
from solidfire.apiactual import ApiSchedule, ApiScheduleInfo, ApiWeekday, \
    ApiGetScheduleResult, ApiListSchedulesResult, ApiModifyScheduleResult, \
    ApiCreateScheduleResult
from solidfire.custom.models import Weekday, DaysOfMonthFrequency, \
    DaysOfWeekFrequency, TimeIntervalFrequency
from solidfire.models import Schedule, Frequency, ScheduleInfo
from solidfire.results import GetScheduleResult, ListSchedulesResult, \
    CreateScheduleResult, ModifyScheduleResult


class ScheduleAdaptor:
    """
    This class contains the implementation of the schedule specific adaptor
    calls for simplifying Snapshot Scheduling.
    """

    @staticmethod
    def get_schedule(element, params, since, deprecated):
        """

        :param element:
        :param params:
        :param since:
        :param deprecated:
        :return:
        """
        api_result = element.send_request("GetSchedule",
                                          ApiGetScheduleResult, params,
                                          since, deprecated)

        result = GetScheduleResult()

        result.schedule = ScheduleAdaptor.to_schedule(api_result.schedule)

        return result

    @staticmethod
    def list_schedules(element, params, since, deprecated):
        """

        :param element:
        :param params:
        :param since:
        :param deprecated:
        :return:
        """

        api_result = element.send_request("ListSchedules",
                                          ApiListSchedulesResult, params,
                                          since, deprecated)

        result = ListSchedulesResult()

        schedules = []
        for schedule in api_result.schedules:
            schedules.append(ScheduleAdaptor.to_schedule(schedule))

        result.schedules = schedules

        return result

    @staticmethod
    def modify_schedule(element, params, since, deprecated):
        """

        :param element:
        :param params:
        :param since:
        :param deprecated:
        :return:
        """

        if hasattr(params['schedule'].schedule_id, '_member_type'):
            raise AttributeError("ScheduleID is missing. Cannot modify a "
                                 "schedule without a ScheduleID")

        api_schedule = ScheduleAdaptor.to_api_schedule(params['schedule'])

        element.send_request("ModifySchedule",
                             ApiModifyScheduleResult, api_schedule.to_json(),
                             since, deprecated)

        return ModifyScheduleResult()

    @staticmethod
    def create_schedule(element, params, since, deprecated):
        """

        :param element:
        :param params:
        :param since:
        :param deprecated:
        :return:
        """
        if not hasattr(params['schedule'].schedule_id, '_member_type'):
            raise AttributeError("ScheduleID should not be present. Do "
                                 "not specify ScheduleID when creating a "
                                 "Schedule. One will be assigned upon "
                                 "creation.")

        api_schedule = ScheduleAdaptor.to_api_schedule(params['schedule'])

        api_result = element.send_request("CreateSchedule",
                                          CreateScheduleResult,
                                          api_schedule.to_json(),
                                          since, deprecated)

        return api_result

    @staticmethod
    def to_schedule(api):
        """

        :param api:
        :type api: solidfire.apiactual.ApiSchedule
        :return:
        """
        schedule = Schedule()

        schedule.has_error = api.has_error
        schedule.last_run_status = api.last_run_status
        schedule.last_run_time_start = api.last_run_time_start
        schedule.name = api.schedule_name
        schedule.paused = api.paused
        schedule.recurring = api.recurring
        schedule.run_next_interval = api.run_next_interval
        schedule.schedule_id = api.schedule_id
        schedule.starting_date = api.starting_date
        schedule.to_be_deleted = api.to_be_deleted

        schedule.schedule_info = ScheduleAdaptor.to_schedule_info(
            api.schedule_info)

        freq = api.attributes["frequency"]

        if freq == "Time Interval":
            schedule.frequency = TimeIntervalFrequency()
            schedule.frequency.days = int(api.hours / 24)
            schedule.frequency.hours = int(api.hours % 24)
            schedule.frequency.minutes = api.minutes
        elif freq == "Days Of Month":
            schedule.Frequency = DaysOfMonthFrequency()
            schedule.frequency.hours = api.hours,
            schedule.frequency.minutes = api.minutes,
            schedule.frequency.monthdays = api.monthdays
        elif freq == "Days Of Week":
            schedule.Frequency = DaysOfWeekFrequency()
            schedule.frequency.hours = api.hours
            schedule.frequency.minutes = api.minutes
            schedule.frequency.weekdays = ScheduleAdaptor \
                .to_weekdays(api.weekdays)

        return schedule

    @staticmethod
    def to_schedule_info(api):
        """

        :param api:
        :type api: solidfire.apiactual.ApiScheduleInfo
        :return:
        """
        info = ScheduleInfo()
        info.enable_remote_replication = api.enable_remote_replication
        info.snapshot_name = api.name
        info.retention = api.retention

        volume_ids = []
        if api.volume_id is not None:
            volume_ids.append(api.volume_id)
        if api.volumes is not None:
            # noinspection PyTypeChecker
            volume_ids.extend(api.volumes)

        info.volume_ids = volume_ids

        return info

    @staticmethod
    def to_weekdays(api):
        """

        :param api:
        :type api: solidfire.apiactual.ApiWeekday[]
        :return:
        """
        weekdays = []
        for api_day in api:
            weekdays.append(Weekday.from_id(api_day.day))
        return weekdays

    @staticmethod
    def to_api_schedule(schedule):
        """

        :param schedule:
        :type schedule: Schedule
        :return:
        """
        api = ApiSchedule()
        api.has_error = schedule.has_error
        api.last_run_status = schedule.last_run_status
        api.last_run_time_start = schedule.last_run_time_start
        api.schedule_name = schedule.name
        api.paused = schedule.paused
        api.recurring = schedule.recurring
        api.run_next_interval = schedule.run_next_interval
        api.schedule_id = schedule.schedule_id
        api.starting_date = schedule.starting_date
        api.to_be_deleted = schedule.to_be_deleted
        api.schedule_type = 'Snapshot'

        api.schedule_info = ScheduleAdaptor \
            .to_api_schedule_info(schedule.schedule_info)

        frequency = schedule.frequency
        api.attributes = {}

        if type(frequency) is TimeIntervalFrequency:
            api.minutes = frequency.minutes
            api.hours = frequency.days * 24 + frequency.hours
            api.attributes["frequency"] = "Time Interval"
        if type(frequency) is DaysOfMonthFrequency:
            api.minutes = frequency.minutes
            api.hours = frequency.hours
            api.monthdays = frequency.monthdays
            api.attributes["frequency"] = "Days Of Month"
        if type(frequency) is DaysOfWeekFrequency:
            api.minutes = frequency.minutes
            api.hours = frequency.hours
            api_weekdays = []
            for weekday in frequency.weekdays:
                api_weekday = ApiWeekday()
                api_weekday.day = weekday[1]
                api_weekday.offset = 1
                api_weekdays.append(api_weekday)

            api.weekdays = api_weekdays
            api.attributes["frequency"] = "Days Of Week"
        return api

    @staticmethod
    def to_api_schedule_info(info):
        """

        :param info:
        :type info: ScheduleInfo
        :return:
        """
        api = ApiScheduleInfo()
        api.enable_remote_replication = info.enable_remote_replication
        api.name = info.snapshot_name
        api.retention = info.retention

        # noinspection PyTypeChecker
        if info.volume_ids is None or len(info.volume_ids) == 0:
            raise AttributeError('ScheduleInfo.VolumeIDs are missing. '
                                 'Cannot create or modify a schedule without at '
                                 'least one VolumeID.')
        else:
            api.volumes = info.volume_ids

        return api
