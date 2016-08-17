"""
Module contains objects directly mapped to the Element API. These are
generated and then moved here before the API is regenerated with changes.
Adaptors are used to transform actual API object into custom object and
vice-versa.
"""
from solidfire.common import model as data_model


class ApiScheduleInfo(data_model.DataObject):
    """

    :param volume_id: (optional) The ID of the volume to be included in the
        snapshot.
    :type volume_id: int

    :param volumes: (optional) A list of volume *ids* to be included in the
        group snapshot.
    :type volumes: int

    :param name: (optional) The snapshot name to be used.
    :type name: str

    :param enable_remote_replication: (optional) Indicates if the snapshot
        should be included in remote replication.
    :type enable_remote_replication: bool

    :param retention: (optional) The amount of time the snapshot will be
        retained in HH:mm:ss.
    :type retention: str
    """

    volume_id = data_model.property(
        "volumeID", int,
        array=False, optional=True,
        documentation="\
        The ID of the volume to be included in the snapshot.\
        "
    )

    volumes = data_model.property(
        "volumes", int,
        array=True, optional=True,
        documentation="\
        A list of volume *ids* to be included in the group snapshot.\
        "
    )

    name = data_model.property(
        "name", str,
        array=False, optional=True,
        documentation="\
        The snapshot name to be used.\
        "
    )

    enable_remote_replication = data_model.property(
        "enableRemoteReplication", bool,
        array=False, optional=True,
        documentation="\
        Indicates if the snapshot should be included in remote replication.\
        "
    )

    retention = data_model.property(
        "retention", str,
        array=False, optional=True,
        documentation="\
        The amount of time the snapshot will be retained in HH:mm:ss.\
        "
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class ApiWeekday(data_model.DataObject):
    """

    :param day: [required]
    :type day: int

    :param offset: [required]
    :type offset: int
    """

    day = data_model.property(
        "day", int,
        array=False, optional=False,
        documentation=None
    )

    offset = data_model.property(
        "offset", int,
        array=False, optional=False,
        documentation=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class ApiSchedule(data_model.DataObject):
    """
    Schedule is an object containing information about each schedule created to
    autonomously make a snapshot of a volume. The return object includes
    information for all schedules. If *schedule_id* is used to identify a
    specific schedule then only information for that *schedule_id* is returned.
    Schedules information is returned with the API method, see *list_schedules*
    on the SolidFire API guide page 245.

    :param attributes: [required] Indicates the frequency of the schedule
        occurrence.

        Valid values are:

        Day of Week

        Day of Month

        Time Interval

    :type attributes: dict

    :param has_error: [required] Indicates whether or not the schedule has
        errors.
    :type has_error: bool

    :param hours: [required] Shows the hours that will elapse before the next
        snapshot is created.

        Valid values are: 0 - 24

    :type hours: int

    :param last_run_status: [required] Indicates the status of the last
        scheduled snapshot.

        Valid values are:

        Success

        Failed

    :type last_run_status: str

    :param last_run_time_start: [required] Indicates the last time the schedule
        started n ISO 8601 date string. Valid values are:

        Success

        Failed

    :type last_run_time_start: str

    :param minutes: [required] Shows the minutes that will elapse before the
        next snapshot is created. Valid values are: 0 - 59
    :type minutes: int

    :param monthdays: [required] Shows the days of the month that the next
        snapshot will be created on. Valid values are: 0 - 31
    :type monthdays: int

    :param paused: [required] Indicates whether or not the schedule is paused.
    :type paused: bool

    :param recurring: [required] Indicates whether or not the schedule is
        recurring.
    :type recurring: bool

    :param run_next_interval: [required] Indicates whether or not the schedule
        will run the next time the scheduler is active. When set to \"true\",
        the schedule will run the next time the scheduler is active and then
        reset back to \"false\".
    :type run_next_interval: bool

    :param schedule_id: [required] Unique ID of the schedule
    :type schedule_id: int

    :param schedule_info: [required] Includes the unique name given to the
        schedule, the retention period for the snapshot that was created, and
        the volume ID of the volume from which the snapshot was created.
    :type schedule_info: ScheduleInfo

    :param schedule_name: [required] Unique name assigned to the schedule.
    :type schedule_name: str

    :param schedule_type: [required] Only \"snapshot\" is supported at this
        time.
    :type schedule_type: str

    :param starting_date: [required] Indicates the date the first time the
        schedule began of will begin. Formatted in UTC time.
    :type starting_date: str

    :param to_be_deleted: [required] Indicates if the schedule is marked for
        deletion.
    :type to_be_deleted: bool

    :param weekdays: [required] Indicates the days of the week that a snapshot
        will be made.
    :type weekdays: Weekday
    """

    attributes = data_model.property(
        "attributes", dict,
        array=False, optional=False,
        documentation="\
        Indicates the frequency of the schedule occurrence.\
        Valid values are:\
        Day of Week\
        Day of Month\
        Time Interval\
        "
    )

    has_error = data_model.property(
        "hasError", bool,
        array=False, optional=False,
        documentation="\
        Indicates whether or not the schedule has errors.\
        "
    )

    hours = data_model.property(
        "hours", int,
        array=False, optional=False,
        documentation="\
        Shows the hours that will elapse before the next snapshot is created.\
        Valid values are: 0 - 24\
        "
    )

    last_run_status = data_model.property(
        "lastRunStatus", str,
        array=False, optional=False,
        documentation="\
        Indicates the status of the last scheduled snapshot.\
        Valid values are:\
        Success\
        Failed\
        "
    )

    last_run_time_start = data_model.property(
        "lastRunTimeStart", str,
        array=False, optional=False,
        documentation="\
        Indicates the last time the schedule started n ISO 8601 date string.\
        Valid values are:\
        Success\
        Failed\
        "
    )

    minutes = data_model.property(
        "minutes", int,
        array=False, optional=False,
        documentation="\
        Shows the minutes that will elapse before the next snapshot is\
        created.\
        Valid values are: 0 - 59\
        "
    )

    monthdays = data_model.property(
        "monthdays", int,
        array=True, optional=False,
        documentation="\
        Shows the days of the month that the next snapshot will be created on.\
        Valid values are: 0 - 31\
        "
    )

    paused = data_model.property(
        "paused", bool,
        array=False, optional=False,
        documentation="\
        Indicates whether or not the schedule is paused.\
        "
    )

    recurring = data_model.property(
        "recurring", bool,
        array=False, optional=False,
        documentation="\
        Indicates whether or not the schedule is recurring.\
        "
    )

    run_next_interval = data_model.property(
        "runNextInterval", bool,
        array=False, optional=False,
        documentation="\
        Indicates whether or not the schedule will run the next time the\
        scheduler is active. When set to \"true\", the schedule will run the\
        next time the scheduler is active and then reset back to \"false\".\
        "
    )

    schedule_id = data_model.property(
        "scheduleID", int,
        array=False, optional=False,
        documentation="\
        Unique ID of the schedule\
        "
    )

    schedule_info = data_model.property(
        "scheduleInfo", ApiScheduleInfo,
        array=False, optional=False,
        documentation="\
        Includes the unique name given to the schedule, the retention period\
        for the snapshot that was created, and the volume ID of the volume\
        from which the snapshot was created.\
        "
    )

    schedule_name = data_model.property(
        "scheduleName", str,
        array=False, optional=False,
        documentation="\
        Unique name assigned to the schedule.\
        "
    )

    schedule_type = data_model.property(
        "scheduleType", str,
        array=False, optional=False,
        documentation="\
        Only \"snapshot\" is supported at this time.\
        "
    )

    starting_date = data_model.property(
        "startingDate", str,
        array=False, optional=False,
        documentation="\
        Indicates the date the first time the schedule began of will begin.\
        Formatted in UTC time.\
        "
    )

    to_be_deleted = data_model.property(
        "toBeDeleted", bool,
        array=False, optional=False,
        documentation="\
        Indicates if the schedule is marked for deletion.\
        "
    )

    weekdays = data_model.property(
        "weekdays", ApiWeekday,
        array=True, optional=False,
        documentation="\
        Indicates the days of the week that a snapshot will be made.\
        "
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class ApiGetScheduleResult(data_model.DataObject):
    """
    The object returned by the \"get_schedule\" API Service call.

    :param schedule: [required] The schedule attributes.
    :type schedule: Schedule
    """

    schedule = data_model.property(
        "schedule", ApiSchedule,
        array=False, optional=False,
        documentation="\
        The schedule attributes.\
        "
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class ApiListSchedulesResult(data_model.DataObject):
    """
    The object returned by the \"list_schedules\" API Service call.

    :param schedules: [required] The list of schedules currently on the
        cluster.
    :type schedules: Schedule
    """

    schedules = data_model.property(
        "schedules", ApiSchedule,
        array=True, optional=False,
        documentation="\
        The list of schedules currently on the cluster.\
        "
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class ApiModifyScheduleResult(data_model.DataObject):
    """
    The object returned by the \"modify_schedule\" API Service call.

    :param schedule: [required] Schedule attributes with modifications.
    :type schedule: Schedule
    """

    schedule = data_model.property(
        "schedule", ApiSchedule,
        array=False, optional=False,
        documentation="\
        Schedule attributes with modifications.\
        "
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)
