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
    ApiGetScheduleResult, ApiListSchedulesResult, ApiModifyScheduleResult
from solidfire.custom import Weekday, FrequencyTypes
from solidfire.models import Schedule, Frequency, ScheduleInfo
from solidfire.results import GetScheduleResult, ListSchedulesResult, \
    CreateScheduleResult


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
        api_result = element.send_request("GetSchedule", params,
                                          ApiGetScheduleResult,
                                          since, deprecated)

        result = GetScheduleResult()

        result.schedule = to_schedule(api_result.schedule)

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

        api_result = element.send_request("ListSchedules", params,
                                          ApiListSchedulesResult,
                                          since, deprecated)

        result = ListSchedulesResult()

        schedules = []
        for schedule in api_result.schedules:
            schedules.append(to_schedule(schedule))

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

        if params['schedule'].schedule_id is None:
            raise AttributeError("ScheduleID should not be present. Do "
                                 "not specify ScheduleID when creating a "
                                 "Schedule. One will be assigned upon "
                                 "creation.")

        api_schedule = to_api_schedule(params['schedule'])

        api_params = {
            'Attributes': api_schedule.attributes,
            'Hours': api_schedule.hours,
            'Minutes': api_schedule.minutes,
            'Monthdays': api_schedule.monthdays,
            'Paused': api_schedule.paused,
            'Recurring': api_schedule.recurring,
            'ScheduleInfo': api_schedule.schedule_info,
            'ScheduleName': api_schedule.schedule_name,
            'ScheduleType': api_schedule.schedule_type,
            'StartingDate': api_schedule.starting_date,
            'Weekdays': api_schedule.weekdays
        }

        result = element.send_request("CreateSchedule", api_params,
                                      CreateScheduleResult,
                                      since, deprecated)

        return result

    @staticmethod
    def create_schedule(element, params, since, deprecated):
        """

        :param element:
        :param params:
        :param since:
        :param deprecated:
        :return:
        """
        if params['Schedule'].schedule_id is not None:
            raise AttributeError("ScheduleID is missing. Cannot modify a "
                                 "schedule without a ScheduleID")

        api_schedule = to_api_schedule(params['Schedule'])

        api_params = {
            'RunNextInterval': api_schedule.run_next_interval,
            'ScheduleID': api_schedule.schedule_id,
            'ToBeDeleted': api_schedule.to_be_deleted,
            'Attributes': api_schedule.attributes,
            'Hours': api_schedule.hours,
            'Minutes': api_schedule.minutes,
            'Monthdays': api_schedule.monthdays,
            'Paused': api_schedule.paused,
            'Recurring': api_schedule.recurring,
            'ScheduleInfo': api_schedule.schedule_info,
            'ScheduleName': api_schedule.schedule_name,
            'ScheduleType': api_schedule.schedule_type,
            'StartingDate': api_schedule.starting_date,
            'Weekdays': api_schedule.weekdays
        }

        result = element.send_request("ModifySchedule", api_params,
                                      ApiModifyScheduleResult,
                                      since, deprecated)

        result.schedule = to_schedule(result.schedule)

        return result


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

    schedule.schedule_info = to_schedule_info(api.schedule_info)

    freq = api.attributes["frequency"]

    if freq == "Time Interval":
        schedule.frequency = Frequency() \
            .set_type(Frequency.types().Time_Interval)
        schedule.frequency.days = api.hours / 24,
        schedule.frequency.hours = api.hours % 24,
        schedule.frequency.minutes = api.minutes
    elif freq == "Days Of Month":
        schedule.Frequency = Frequency() \
            .set_type(Frequency.types().Days_Of_Month)
        schedule.frequency.hours = api.hours,
        schedule.frequency.minutes = api.minutes,
        schedule.frequency.monthdays = api.monthdays
    elif freq == "Days Of Week":
        schedule.Frequency = Frequency() \
            .set_type(Frequency.types().Days_Of_Week)
        schedule.frequency.hours = api.hours,
        schedule.frequency.minutes = api.minutes,
        schedule.frequency.weekdays = to_weekdays(api.weekdays)

    return schedule


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

    api.schedule_info = to_api_schedule_info(schedule.schedule_info)

    frequency = schedule.frequency
    api.attributes = {"frequency", frequency.freq_type}

    if frequency.freq_type is FrequencyTypes.Time_Interval:
        api.minutes = frequency.minutes
        api.hours = frequency.days * 24 + frequency.hours
    if frequency.freq_type is FrequencyTypes.Days_Of_Month:
        api.minutes = frequency.minutes
        api.hours = frequency.hours
        api.monthdays = frequency.monthdays
    if frequency.freq_type is FrequencyTypes.Days_Of_Week:
        api.minutes = frequency.minutes
        api.hours = frequency.hours

        api_weekdays = []
        for weekday in frequency.weekdays:
            api_weekday = ApiWeekday()
            api_weekday.day = weekday[1]
            api_weekday.offset = 1
            api_weekdays.append(api_weekday)

        api.weekdays = api_weekdays

    return api


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
