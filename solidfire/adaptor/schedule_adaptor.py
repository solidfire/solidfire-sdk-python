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

        return GetScheduleResult(schedule=ScheduleAdaptor.to_schedule(api_result.schedule))

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
        schedules = []
        for schedule in api_result.schedules:
            schedules.append(ScheduleAdaptor.to_schedule(schedule))

        return ListSchedulesResult(schedules=schedules)

    @staticmethod
    def modify_schedule(element, params, since, deprecated):
        """
        Calls to this static method should ONLY originate from the
        modify_schedules method in the Element class. DO NOT CALL THIS
        directly. Documentation here is intentionally brief.
        """

        if params['schedule'].schedule_id is None:
            raise AttributeError("ScheduleID is missing. Cannot modify a "
                                 "schedule without a ScheduleID")

        if params['schedule'].frequency is None:
            raise AttributeError("Frequency is not present. Make sure the "
                                 "schedule object has a value in the "
                                 "frequency property before attempting to "
                                 "create a Schedule.")

        if params['schedule'].schedule_info is None:
            raise AttributeError("Schedule_info is not present. Make sure the "
                                 "schedule object has a value in the "
                                 "schedule_info property before attempting to "
                                 "modify a Schedule.")

        api_schedule = ScheduleAdaptor.to_api_schedule(params['schedule'])

        api_result = element.send_request("ModifySchedule",
                             ApiModifyScheduleResult, api_schedule.to_json(),
                             since, deprecated)

        if api_result.schedule is not None:
            return ModifyScheduleResult(schedule=ScheduleAdaptor.to_schedule(api_result.schedule))
        else:
            return ModifyScheduleResult()

    @staticmethod
    def create_schedule(element, params, since, deprecated):
        """
        Calls to this static method should ONLY originate from the
        create_schedules method in the Element class. DO NOT CALL THIS
        directly. Documentation here is intentionally brief.
        """
        if params['schedule'] is None:
            raise AttributeError("Please provide a valid schedule object "
                                 "instead of None.")
        if params['schedule'].schedule_id is not None:
            raise AttributeError("ScheduleID should not be present. Do "
                                 "not specify ScheduleID when creating a "
                                 "Schedule. One will be assigned upon "
                                 "creation.")

        if params['schedule'].frequency is None:
            raise AttributeError("Frequency is not present. Make sure the "
                                 "schedule object has a value in the "
                                 "frequency property before attempting to "
                                 "create a Schedule.")

        if params['schedule'].schedule_info is None:
            raise AttributeError("Schedule_info is not present. Make sure the "
                                 "schedule object has a value in the "
                                 "schedule_info property before attempting to "
                                 "modify a Schedule.")
        if params["schedule"].frequency.minutes is None:
            params.setdefault("frequency", {})["minutes"] = 0
        if params["schedule"].frequency.hours is None:
            params.setdefault("frequency", {})["hours"] = 0

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
        schedule_info = ScheduleAdaptor.to_schedule_info(
            api.schedule_info)

        frequency = None
        try:
            freq = api.attributes["frequency"]

            if freq == "Time Interval":
                frequency = TimeIntervalFrequency(
                    days=int(api.hours/24),
                    hours=int(api.hours%24),
                    minutes=api.minutes
                )
            elif freq == "Days Of Month":
                frequency = DaysOfMonthFrequency(
                    hours=api.hours,
                    minutes=api.minutes,
                    monthdays=api.monthdays,
                )
            elif freq == "Days Of Week":
                frequency = DaysOfWeekFrequency(
                    hours=api.hours,
                    minutes=api.minutes,
                    weekdays=ScheduleAdaptor.to_weekdays(api.weekdays),
                )
            else:
                raise Exception("Cannot determine frequency")
        except:
            LOG.error("Cannot deserialize Schedule {0}. The frequency "
                      "property has an unknown value.".format(api.schedule_name))

        return Schedule(
            has_error=api.has_error,
            last_run_status=api.last_run_status,
            last_run_time_started=api.last_run_time_started,
            name=api.schedule_name,
            paused=api.paused,
            recurring=api.recurring,
            run_next_interval=api.run_next_interval,
            schedule_id=api.schedule_id,
            starting_date=api.starting_date,
            to_be_deleted=api.to_be_deleted,
            schedule_info=schedule_info,
            frequency=frequency
        )

    @staticmethod
    def to_schedule_info(api):
        """
        Convert an ApiScheduleInfo object into a ScheduleInfo object

        :param api: the ApiScheduleInfo object
        :type api: solidfire.apiactual.ApiScheduleInfo

        :return: solidfire.models.ScheduleInfo
        """

        volume_ids = []
        if api.volume_id is not None:
            volume_ids.append(int(api.volume_id))
        if api.volumes is not None:
            # noinspection PyTypeChecker
            volume_ids.extend([int(vol) for vol in api.volumes])

        info = ScheduleInfo(
            enable_remote_replication=api.enable_remote_replication,
            snapshot_name=api.name,
            retention=api.retention,
            volume_ids=volume_ids
        )
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

        schedule_info = ScheduleAdaptor \
            .to_api_schedule_info(schedule.schedule_info)

        frequency = schedule.frequency
        attributes = {}

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
            minutes = frequency.minutes
            hours = frequency.days * 24 + frequency.hours
            attributes["frequency"] = "Time Interval"
            weekdays = None
            monthdays = None
        if type(frequency) is DaysOfMonthFrequency:
            minutes = frequency.minutes
            hours = frequency.hours
            monthdays = frequency.monthdays
            weekdays = None
            attributes["frequency"] = "Days Of Month"
        if type(frequency) is DaysOfWeekFrequency:
            minutes = frequency.minutes
            hours = frequency.hours
            api_weekdays = []
            for weekday in frequency.weekdays:
                api_weekday = ApiWeekday(day=weekday[1],
                                         offset=1)
                api_weekdays.append(api_weekday)
            weekdays = api_weekdays
            monthdays = None
            attributes["frequency"] = "Days Of Week"


        api = ApiSchedule(has_error=schedule.has_error,
                          last_run_status=schedule.last_run_status,
                          last_run_time_started=schedule.last_run_time_started,
                          schedule_name=schedule.name,
                          paused=schedule.paused,
                          recurring=schedule.recurring,
                          run_next_interval=schedule.run_next_interval,
                          schedule_id=schedule.schedule_id,
                          starting_date=schedule.starting_date,
                          to_be_deleted=schedule.to_be_deleted,
                          schedule_type='Snapshot',
                          attributes=attributes,
                          minutes=minutes,
                          hours=hours,
                          monthdays=monthdays,
                          weekdays=weekdays,
                          schedule_info=schedule_info)
        return api

    @staticmethod
    def to_api_schedule_info(info):
        """
        Converts a ScheduleInfo object into an ApiScheduleInfo object
        
        :param info: the ScheduleInfo object
        :type info: ScheduleInfo

        :return: solidfire.apiactual.ApiScheduleInfo
        """

        volumes=None
        # noinspection PyTypeChecker
        if hasattr(info.volume_ids, '_member_type') or info.volume_ids \
                is None or len(info.volume_ids) == 0:
            raise AttributeError('ScheduleInfo.VolumeIDs are missing. '
                                 'Cannot create or modify a schedule without at '
                                 'least one VolumeID.')


        else:
            volumes = info.volume_ids

        api = ApiScheduleInfo(enable_remote_replication=info.enable_remote_replication,
                              name=info.snapshot_name,
                              retention=info.retention,
                              volumes=volumes)
        return api
