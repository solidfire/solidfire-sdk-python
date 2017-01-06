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
from solidfire.models import Schedule, Frequency, ScheduleInfo, GetScheduleResult, ListSchedulesResult, \
    CreateScheduleResult, ModifyScheduleResult
import logging


LOG = logging.getLogger('solidfire.Element')

class ScheduleAdaptor:
    """
    This class contains the implementation of the schedule specific adaptor
    calls for simplifying Snapshot Scheduling.
    """

    @staticmethod
    def get_schedule(element, params, since, deprecated):
        """
        Calls to this static method should ONLY originate from the
        get_schedule method in the Element class. DO NOT CALL THIS directly.
        Documentation here is intentionally brief.
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
        Calls to this static method should ONLY originate from the
        list_schedules method in the Element class. DO NOT CALL THIS directly.
        Documentation here is intentionally brief.
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
        Calls to this static method should ONLY originate from the
        modify_schedules method in the Element class. DO NOT CALL THIS
        directly. Documentation here is intentionally brief.
        """

        if hasattr(params['schedule'].schedule_id, '_member_type') or \
                params['schedule'].schedule_id is None:
            raise AttributeError("ScheduleID is missing. Cannot modify a "
                                 "schedule without a ScheduleID")

        if hasattr(params['schedule'].frequency, '_member_type') or \
                params['schedule'].frequency is None:
            raise AttributeError("Frequency is not present. Make sure the "
                                 "schedule object has a value in the "
                                 "frequency property before attempting to "
                                 "modify a Schedule.")

        if hasattr(params['schedule'].schedule_info, '_member_type'):
            raise AttributeError("Schedule_info is not present. Make sure the "
                                 "schedule object has a value in the "
                                 "schedule_info property before attempting to "
                                 "modify a Schedule.")

        api_schedule = ScheduleAdaptor.to_api_schedule(params['schedule'])

        element.send_request("ModifySchedule",
                             ApiModifyScheduleResult, api_schedule.to_json(),
                             since, deprecated)

        return ModifyScheduleResult()

    @staticmethod
    def create_schedule(element, params, since, deprecated):
        """
        Calls to this static method should ONLY originate from the
        create_schedules method in the Element class. DO NOT CALL THIS
        directly. Documentation here is intentionally brief.
        """
        if not hasattr(params['schedule'].schedule_id, '_member_type'):
            raise AttributeError("ScheduleID should not be present. Do "
                                 "not specify ScheduleID when creating a "
                                 "Schedule. One will be assigned upon "
                                 "creation.")

        if hasattr(params['schedule'].frequency, '_member_type') or \
                params['schedule'].frequency is None:
            raise AttributeError("Frequency is not present. Make sure the "
                                 "schedule object has a value in the "
                                 "frequency property before attempting to "
                                 "create a Schedule.")

        if hasattr(params['schedule'].schedule_info, '_member_type'):
            raise AttributeError("Schedule_info is not present. Make sure the "
                                 "schedule object has a value in the "
                                 "schedule_info property before attempting to "
                                 "modify a Schedule.")

        api_schedule = ScheduleAdaptor.to_api_schedule(params['schedule'])

        api_result = element.send_request("CreateSchedule",
                                          CreateScheduleResult,
                                          api_schedule.to_json(),
                                          since, deprecated)

        return api_result

    @staticmethod
    def to_schedule(api):
        """
        Converts an ApiSchedule object into a Schedule object

        :param api: the ApiSchedule object to be converted
        :type api: solidfire.apiactual.ApiSchedule

        :return: solidfire.models.Schedule
        """
        schedule = Schedule()

        schedule.has_error = api.has_error
        schedule.last_run_status = api.last_run_status
        schedule.last_run_time_started = api.last_run_time_started
        schedule.name = api.schedule_name
        schedule.paused = api.paused
        schedule.recurring = api.recurring
        schedule.run_next_interval = api.run_next_interval
        schedule.schedule_id = api.schedule_id
        schedule.starting_date = api.starting_date
        schedule.to_be_deleted = api.to_be_deleted

        schedule.schedule_info = ScheduleAdaptor.to_schedule_info(
            api.schedule_info)

        try:
            freq = api.attributes["frequency"]

            if freq == "Time Interval":
                schedule.frequency = TimeIntervalFrequency()
                schedule.frequency.days = int(api.hours / 24)
                schedule.frequency.hours = int(api.hours % 24)
                schedule.frequency.minutes = api.minutes
                schedule.frequency.weekdays = None
                schedule.frequency.monthdays = None
            elif freq == "Days Of Month":
                schedule.frequency = DaysOfMonthFrequency()
                schedule.frequency.hours = api.hours
                schedule.frequency.minutes = api.minutes
                schedule.frequency.monthdays = api.monthdays
                schedule.frequency.weekdays = None
            elif freq == "Days Of Week":
                schedule.frequency = DaysOfWeekFrequency()
                schedule.frequency.hours = api.hours
                schedule.frequency.minutes = api.minutes
                schedule.frequency.weekdays = ScheduleAdaptor \
                    .to_weekdays(api.weekdays)
                schedule.frequency.monthdays = None
            else:
                raise Exception("Cannot determine frequency")
        except:
            LOG.error("Cannot deserialize Schedule {0}. The frequency "
                      "property has an unknown value.".format(
                schedule.name))

        return schedule

    @staticmethod
    def to_schedule_info(api):
        """
        Convert an ApiScheduleInfo object into a ScheduleInfo object

        :param api: the ApiScheduleInfo object
        :type api: solidfire.apiactual.ApiScheduleInfo

        :return: solidfire.models.ScheduleInfo
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
        Converts an ApiWeekday object array into a Weekday object array

        :param api: array of ApiWeekday objects
        :type api: solidfire.apiactual.ApiWeekday[]

        :return: solidfire.custom.models.Weekday[]
        """
        weekdays = []
        for api_day in api:
            weekdays.append(Weekday.from_id(api_day.day))
        return weekdays

    @staticmethod
    def to_api_schedule(schedule):
        """
        Converts a Schedule object into an ApiSchedule object
        :param schedule: the Schedule object
        :type schedule: Schedule

        :return: solidfire.apiactual.ApiSchedule
        """
        api = ApiSchedule()
        api.has_error = schedule.has_error
        api.last_run_status = schedule.last_run_status
        api.last_run_time_started = schedule.last_run_time_started
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
            if hasattr(frequency.days, '_member_type') or frequency.days is \
                    None:
                frequency.days = 0
            if hasattr(frequency.hours, '_member_type') or frequency.hours is \
                    None:
                frequency.hours = 0
            if hasattr(frequency.minutes, '_member_type') or \
                            frequency.minutes is None:
                frequency.minutes = 0
            api.minutes = frequency.minutes
            api.hours = frequency.days * 24 + frequency.hours
            api.attributes["frequency"] = "Time Interval"
            api.weekdays = None
            api.monthdays = None
        if type(frequency) is DaysOfMonthFrequency:
            api.minutes = frequency.minutes
            api.hours = frequency.hours
            api.monthdays = frequency.monthdays
            api.weekdays = None
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
            api.monthdays = None
            api.attributes["frequency"] = "Days Of Week"
        return api

    @staticmethod
    def to_api_schedule_info(info):
        """
        Converts a ScheduleInfo object into an ApiScheduleInfo object
        
        :param info: the ScheduleInfo object
        :type info: ScheduleInfo

        :return: solidfire.apiactual.ApiScheduleInfo
        """
        api = ApiScheduleInfo()
        api.enable_remote_replication = info.enable_remote_replication
        api.name = info.snapshot_name
        api.retention = info.retention

        # noinspection PyTypeChecker
        if hasattr(info.volume_ids, '_member_type') or info.volume_ids \
                is None or len(info.volume_ids) == 0:
            raise AttributeError('ScheduleInfo.VolumeIDs are missing. '
                                 'Cannot create or modify a schedule without at '
                                 'least one VolumeID.')


        else:
            api.volumes = info.volume_ids

        return api
