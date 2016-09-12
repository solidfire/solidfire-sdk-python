|sf-python-logo| SolidFire Python SDK Examples
==============================================

Snapshot Scheduling
-------------------

These examples walk through all interactions with a Schedule. Schedules
control when automatic Snapshots will be taken of volumes on the
SolidFire cluster.

Examples for:

-  `List all Schedules <#list-all-schedules>`__
-  `Get one Schedule <#get-one-schedule>`__
-  `Create a Schedule <#create-a-schedule>`__
-  `Modify a Schedule <#modify-a-schedule>`__

Documentation
~~~~~~~~~~~~~

Further documentation for each method and type can be found in our PyPI
documentation repository.

List all Schedules
~~~~~~~~~~~~~~~~~~

To list all the schedules on a cluster:

.. code:: python

    from solidfire.factory import ElementFactory

    # Create connection to SF Cluster
    sfe = ElementFactory.create("ip-address-of-cluster", "username", "password")

    # Send the request and gather the result
    list_schedules_result = sfe.list_schedules()

    # iterate the schedules array on the result object and display each Schedule 
    for schedule in list_schedules_result.schedules:
        print(schedule)

Get one Schedule
~~~~~~~~~~~~~~~~

To get a single schedule:

.. code:: python

    from solidfire.factory import ElementFactory

    # Create connection to SF Cluster
    sfe = ElementFactory.create("ip-address-of-cluster", "username", "password")

    # Send the request with the schedule_id and gather the result
    get_schedule_result = sfe.get_schedule(schedule_id=56)

    # Display the schedule from the result object
    print(get_schedule_result.schedule)

Create a Schedule
~~~~~~~~~~~~~~~~~

In order for automatic snapshots to be taken, you need to create a
schedule. There are three types of schedules that can be created:

-  `Time Interval <#time-interval-schedule>`__
-  `Days Of Week <#days-of-week-schedule>`__
-  `Days Of Month <#days-of-month-schedule>`__

All three types of schedules are demonstrated here:

Time Interval Schedule
^^^^^^^^^^^^^^^^^^^^^^

This type of schedule will base snapshots on a time interval frequency.
Each snapshot will be taken after the specified amount of time has
passed. Control the duration by setting days, hours, and minutes on the
TimeIntervalFrequency object.

.. code:: python

    from solidfire.custom.models import TimeIntervalFrequency
    from solidfire.models import Schedule

    sched = Schedule()
    sched.name = "SnapshotEvery3AndAHalfDays"
    sched.frequency = TimeIntervalFrequency(days=3, hours=12)

Days Of Week Schedule
^^^^^^^^^^^^^^^^^^^^^

This type of schedule will base snapshots on a weekly frequency. Each
snapshot will be taken on the specified weekdays at the time specified
in the hours and minutes properties. Control the schedule by setting
weekdays, hours, and minutes on the DaysOfWeekFrequency object.

.. code:: python

    from solidfire.custom.models import DaysOfWeekFrequency, Weekday
    from solidfire.models import Schedule

    sched = Schedule()
    sched.name = "SnapshotOnMonWedFriAt3am"
    sched.frequency = DaysOfWeekFrequency(
                weekdays=[
                    Weekday.from_name("Monday"),
                    Weekday.from_name("Wednesday"),
                    Weekday.from_name("Friday")], 
                hours=3)

Days Of Month Schedule
^^^^^^^^^^^^^^^^^^^^^^

This type of schedule will base snapshots on a monthly frequency. Each
snapshot will be taken on the specified month days at the time specified
in the hours and minutes properties. Control the schedule by setting
monthdays, hours, and minutes on the DaysOfMonthFrequency object.

.. code:: python

    from solidfire.custom.models import DaysOfMonthFrequency
    from solidfire.models import Schedule

    sched = Schedule()
    sched.name = "SnapshotOn7th14thAnd21stAt0130Hours"
    sched.frequency = DaysOfMonthFrequency(
                monthdays=[7,14,21], 
                hours=3,
                monutes=30)

Create a Schedule (cont.)
^^^^^^^^^^^^^^^^^^^^^^^^^

After creating the schedule and setting the frequency to Time Interval,
Days Of Week, or Days Of Month, complete the object by setting the
schedule\_info property. This controls information about the resulting
snapshot such as which volumes are in it, its name, and how long it
should be retained.

Continuing on with the `Time Interval <#time-interval-schedule>`__
example from above:

.. code:: python

    from solidfire.custom.models import TimeIntervalFrequency
    from solidfire.models import Schedule, ScheduleInfo
    from solidfire.factory import ElementFactory

    sched = Schedule()
    sched.name = "SnapshotEvery12Hours"
    sched.frequency = TimeIntervalFrequency(hours=12)
    sched.schedule_info = ScheduleInfo(
        volume_ids = [1, 3, 5],
        snapshot_name = '12th hour snapshot',
        retention="72:00:00" # in HH:mm:ss format
    )
    # When should the schedule start?
    sched.starting_date = "2016-12-01T00:00:00Z"

    # Create connection to SF Cluster
    sfe = ElementFactory.create("ip-address-of-cluster", "username", "password")

    # Call the create_schedule method with the newly created schedule object
    create_schedule_result = sfe.create_schedule(sched)

    # Grab the schedule ID from the result object
    new_schedule_id = create_schedule_result.schedule_id

At this point we have created a new schedule called SnapshotEvery12Hours
that creates a snapshot whose name is prepended with "12th hour
snapshot" every 12 hours for volumes 1, 3, and 5 that is retained for 72
hours.

Modify a Schedule
~~~~~~~~~~~~~~~~~

To modify a schedule, first you must have a valid schedule object with
its schedule\_id set. You can create one manually but it is preferred to
retrieve it from the cluster, modify the properties needed and then send
it back. Here is an example:

.. code:: python

    from solidfire.factory import ElementFactory

    # Create connection to SF Cluster
    sfe = ElementFactory.create("ip-address-of-cluster", "username", "password")

    # Send the request with the schedule_id and gather the result
    get_schedule_result = sfe.get_schedule(schedule_id=new_schedule_id)

    # set a schedule variable from the schedule in the result for ease of use
    sched = get_schedule_result.schedule

    # display the retrieved schedule
    print(sched)

    # set paused to True in order to pause the schedule
    sched.paused = True

    # send the request to modify this schedule
    sfe.modify_schedule(sched)

    # Send another get_schedule request and gather the result
    get_modified_schedule_result = sfe.get_schedule(schedule_id=56)

    # display the newly modified schedule
    print(get_modified_schedule_result.schedule)

This is the output:

::

    Schedule(frequency=TimeIntervalFrequency(days=0, hours=12, minutes=0), has_error=False, last_run_status='Success', last_run_time_start=None, name='SnapshotsEvery12Hours', paused=False, recurring=False, run_next_interval=False, schedule_id=56, schedule_info=ScheduleInfo(enable_remote_replication=None, retention='72:00:00', snapshot_name='12th hour snapshot', volume_ids='[1, 3, 5]'), starting_date='2016-12-01T00:00:00Z', to_be_deleted=False)

    Schedule(frequency=TimeIntervalFrequency(days=0, hours=12, minutes=0), has_error=False, last_run_status='Success', last_run_time_start=None, name='SnapshotsEvery12Hours', paused=True, recurring=False, run_next_interval=False, schedule_id=56, schedule_info=ScheduleInfo(enable_remote_replication=None, retention='72:00:00', snapshot_name='12th hour snapshot', volume_ids='[1, 3, 5]'), starting_date='2016-12-01T00:00:00Z', to_be_deleted=False)

Notice the *paused* field changes from ``False`` to ``True``

.. |sf-python-logo| image:: https://raw.githubusercontent.com/solidfire/solidfire-sdk-python/release1.1/img/python.png
    :height: 50px