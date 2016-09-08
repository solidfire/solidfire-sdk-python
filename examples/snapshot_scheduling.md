#<img src="../img/python.png" height="50" width="50" > SolidFire Python SDK Examples

## Snapshot Scheduling

This example walks through creating a schedule which will control when automatic snapshots will be taken of volumes on the SolidFire cluster.

### Documentation

Further documentation can be found in our PyPI documentation repository. 

### Create a Schedule

In order for automatic snapshots to be taken, create a schedule. There are three types of schedules that can be created:

- Time Interval 
- Days Of Week
- Days Of Month

All three types of schedules are demonstrated here:

**Create a Time Interval Schedule**

This type of schedule will base snapshots on a time interval frequency. Each snapshot will be taken after the specified amount of time has passed. Control the duration by setting days, hours, and minutes on the TimeIntervalFrequency object.


