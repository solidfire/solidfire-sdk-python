#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright &copy; 2014-2016 NetApp, Inc. All Rights Reserved.
#
# DO NOT EDIT THIS CODE BY HAND! It has been generated with jsvcgen.
#
from __future__ import unicode_literals
from __future__ import absolute_import
from solidfire.common import model as data_model
from uuid import UUID
from solidfire.custom.models import CHAPSecret as UserDefinedCHAPSecret
from solidfire.custom.models import Frequency as UserDefinedFrequency


class CHAPSecret(UserDefinedCHAPSecret):
    def __init__(self, **kwargs):
        self = UserDefinedCHAPSecret()
        data_model.DataObject.__init__(self, **kwargs)


class Frequency(UserDefinedFrequency):
    def __init__(self, **kwargs):
        self = UserDefinedFrequency()
        data_model.DataObject.__init__(self, **kwargs)


class AddressBlock(data_model.DataObject):
    """
    Unique Range of IP addresses to include in the virtual network.

    :param start: [required] Start of the IP address range.
    :type start: str

    :param size: [required] Number of IP addresses to include in the block.
    :type size: int
    """

    start = data_model.property(
        "start", str,
        array=False, optional=False,
        documentation="\
        Start of the IP address range.\
        "
    )

    size = data_model.property(
        "size", int,
        array=False, optional=False,
        documentation="\
        Number of IP addresses to include in the block.\
        "
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class PhysicalAdapter(data_model.DataObject):
    """

    :param address: (optional)
    :type address: str

    :param mac_address: (optional)
    :type mac_address: str

    :param mac_address_permanent: (optional)
    :type mac_address_permanent: str

    :param mtu: (optional)
    :type mtu: str

    :param netmask: (optional)
    :type netmask: str

    :param network: (optional)
    :type network: str

    :param up_and_running: (optional)
    :type up_and_running: bool
    """

    address = data_model.property(
        "address", str,
        array=False, optional=True,
        documentation=None
    )

    mac_address = data_model.property(
        "macAddress", str,
        array=False, optional=True,
        documentation=None
    )

    mac_address_permanent = data_model.property(
        "macAddressPermanent", str,
        array=False, optional=True,
        documentation=None
    )

    mtu = data_model.property(
        "mtu", str,
        array=False, optional=True,
        documentation=None
    )

    netmask = data_model.property(
        "netmask", str,
        array=False, optional=True,
        documentation=None
    )

    network = data_model.property(
        "network", str,
        array=False, optional=True,
        documentation=None
    )

    up_and_running = data_model.property(
        "upAndRunning", bool,
        array=False, optional=True,
        documentation=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class Platform(data_model.DataObject):
    """

    :param node_type: [required] SolidFire&#39;s name for this platform.
    :type node_type: str

    :param chassis_type: [required] Name of the chassis (example: \"R620\").
    :type chassis_type: str

    :param cpu_model: [required] The model of CPU used on this platform.
    :type cpu_model: str

    :param node_memory_gb: [required] The amount of memory on this platform in
        GiB.
    :type node_memory_gb: int
    """

    node_type = data_model.property(
        "nodeType", str,
        array=False, optional=False,
        documentation="\
        SolidFire&#39;s name for this platform.\
        "
    )

    chassis_type = data_model.property(
        "chassisType", str,
        array=False, optional=False,
        documentation="\
        Name of the chassis (example: \"R620\").\
        "
    )

    cpu_model = data_model.property(
        "cpuModel", str,
        array=False, optional=False,
        documentation="\
        The model of CPU used on this platform.\
        "
    )

    node_memory_gb = data_model.property(
        "nodeMemoryGB", int,
        array=False, optional=False,
        documentation="\
        The amount of memory on this platform in GiB.\
        "
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class QoS(data_model.DataObject):
    """
    Quality of Service (QoS) values are used on SolidFire volumes to provision
    performance expectations.
    Minimum, maximum and burst *qos* values can be set within the ranges
    specified in the *qos* table below.




    Volumes created without specified *qos* values are created with the Default
    values listed below.
    Default values can be found by running the *get_default_qos* method.




    **minIOPS** Min: 100/50 (v7.0/v8.0), Default: 100, Max: 15,000



    **maxIOPS** Min: 100/50 (v7.0/v8.0), Default: 15,000, Max: 100,000



    **burstIOPS** Min: 100/50 (v7.0/v8.0), Default: 15,000, Max: 100,000




    :param min_iops: (optional) Desired minimum 4KB IOPS to guarantee. The
        allowed IOPS will only drop below this level if all volumes have been
        capped at their minimum IOPS value and there is still insufficient
        performance capacity.
    :type min_iops: int

    :param max_iops: (optional) Desired maximum 4KB IOPS allowed over an
        extended period of time.
    :type max_iops: int

    :param burst_iops: (optional) Maximum \"peak\" 4KB IOPS allowed for short
        periods of time. Allows for bursts of I/O activity over the normal max
        IOPS value.
    :type burst_iops: int

    :param burst_time: (optional) The length of time burst IOPS is allowed. The
        value returned is represented in time units of seconds.

        **Note**: this value is calculated by the system based on IOPS set for
        QoS.

    :type burst_time: int
    """

    min_iops = data_model.property(
        "minIOPS", int,
        array=False, optional=True,
        documentation="\
        Desired minimum 4KB IOPS to guarantee.\
        The allowed IOPS will only drop below this level if all volumes have\
        been capped\
        at their minimum IOPS value and there is still insufficient\
        performance capacity.\
        "
    )

    max_iops = data_model.property(
        "maxIOPS", int,
        array=False, optional=True,
        documentation="\
        Desired maximum 4KB IOPS allowed over an extended period of time.\
        "
    )

    burst_iops = data_model.property(
        "burstIOPS", int,
        array=False, optional=True,
        documentation="\
        Maximum \"peak\" 4KB IOPS allowed for short periods of time.\
        Allows for bursts of I/O activity over the normal max IOPS value.\
        "
    )

    burst_time = data_model.property(
        "burstTime", int,
        array=False, optional=True,
        documentation="\
        The length of time burst IOPS is allowed.\
        The value returned is represented in time units of seconds.\
\
\
            **Note**: this value is calculated by the system based on IOPS set\
        for QoS.\
\
        "
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class ResetDriveDetails(data_model.DataObject):
    """

    :param drive: [required] Drive name
    :type drive: str

    :param return_code: [required]
    :type return_code: int

    :param stderr: [required]
    :type stderr: str

    :param stdout: [required]
    :type stdout: str
    """

    drive = data_model.property(
        "drive", str,
        array=False, optional=False,
        documentation="\
        Drive name\
        "
    )

    return_code = data_model.property(
        "returnCode", int,
        array=False, optional=False,
        documentation=None
    )

    stderr = data_model.property(
        "stderr", str,
        array=False, optional=False,
        documentation=None
    )

    stdout = data_model.property(
        "stdout", str,
        array=False, optional=False,
        documentation=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class SnapshotReplication(data_model.DataObject):
    """

    :param state: [required] The state of the snapshot replication.
    :type state: str

    :param state_details: [required] Reserved for future use.
    :type state_details: str
    """

    state = data_model.property(
        "state", str,
        array=False, optional=False,
        documentation="\
        The state of the snapshot replication.\
        "
    )

    state_details = data_model.property(
        "stateDetails", str,
        array=False, optional=False,
        documentation="\
        Reserved for future use.\
        "
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class VolumeQOS(data_model.DataObject):
    """
    Quality of Service (QoS) Result values are used on SolidFire volumes to
    provision performance expectations.

    :param min_iops: [required] Desired minimum 4KB IOPS to guarantee. The
        allowed IOPS will only drop below this level if all volumes have been
        capped at their min IOPS value and there is still insufficient
        performance capacity.
    :type min_iops: int

    :param max_iops: [required] Desired maximum 4KB IOPS allowed over an
        extended period of time.
    :type max_iops: int

    :param burst_iops: [required] Maximum \"peak\" 4KB IOPS allowed for short
        periods of time. Allows for bursts of I/O activity over the normal max
        IOPS value.
    :type burst_iops: int

    :param burst_time: [required] The length of time burst IOPS is allowed. The
        value returned is represented in time units of seconds.

        **Note**: this value is calculated by the system based on IOPS set for
        QoS.

    :type burst_time: int

    :param curve: [required] The curve is a set of key-value pairs. The keys
        are I/O sizes in bytes. The values represent the cost performing an IOP
        at a specific I/O size. The curve is calculated relative to a 4096 byte
        operation set at 100 IOPS.
    :type curve: str
    """

    min_iops = data_model.property(
        "minIOPS", int,
        array=False, optional=False,
        documentation="\
        Desired minimum 4KB IOPS to guarantee.\
        The allowed IOPS will only drop below this level if all volumes have\
        been capped\
        at their min IOPS value and there is still insufficient performance\
        capacity.\
        "
    )

    max_iops = data_model.property(
        "maxIOPS", int,
        array=False, optional=False,
        documentation="\
        Desired maximum 4KB IOPS allowed over an extended period of time.\
        "
    )

    burst_iops = data_model.property(
        "burstIOPS", int,
        array=False, optional=False,
        documentation="\
        Maximum \"peak\" 4KB IOPS allowed for short periods of time.\
        Allows for bursts of I/O activity over the normal max IOPS value.\
        "
    )

    burst_time = data_model.property(
        "burstTime", int,
        array=False, optional=False,
        documentation="\
        The length of time burst IOPS is allowed.\
        The value returned is represented in time units of seconds.\
\
\
            **Note**: this value is calculated by the system based on IOPS set\
        for QoS.\
\
        "
    )

    curve = data_model.property(
        "curve", str,
        array=False, optional=False,
        documentation="\
        The curve is a set of key-value pairs.\
        The keys are I/O sizes in bytes.\
        The values represent the cost performing an IOP at a specific I/O\
        size.\
        The curve is calculated relative to a 4096 byte operation set at 100\
        IOPS.\
        "
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class ClusterCapacity(data_model.DataObject):
    """
    High level capacity measurements for the entire cluster.

    :param active_block_space: [required] The amount of space on the block
        drives. This includes additional information such as metadata entries
        and space which can be cleaned up.
    :type active_block_space: int

    :param active_sessions: [required] Number of active iSCSI sessions
        communicating with the cluster
    :type active_sessions: int

    :param average_iops: [required] Average IPS for the cluster since midnight
        Coordinated Universal Time (UTC).
    :type average_iops: int

    :param cluster_recent_iosize: [required] The average size of IOPS to all
        volumes in the cluster.
    :type cluster_recent_iosize: int

    :param current_iops: [required] Average IOPS for all volumes in the cluster
        over the last 5 seconds.
    :type current_iops: int

    :param max_iops: [required] Estimated maximum IOPS capability of the
        current cluster.
    :type max_iops: int

    :param max_over_provisionable_space: [required] The maximum amount of
        provisionable space. This is a computed value. You cannot create new
        volumes if the current provisioned space plus the new volume size would
        exceed this number: *max_over_provisionable_space* =
        *max_provisioned_space* * *get_cluster_full*
    :type max_over_provisionable_space: int

    :param max_provisioned_space: [required] The total amount of provisionable
        space if all volumes are 100% filled (no thin provisioned metadata).
    :type max_provisioned_space: int

    :param max_used_metadata_space: [required] The amount of bytes on volume
        drives used to store metadata.
    :type max_used_metadata_space: int

    :param max_used_space: [required] The total amount of space on all active
        block drives.
    :type max_used_space: int

    :param non_zero_blocks: [required] Total number of 4KiB blocks with data
        after the last garbage collection operation has completed.
    :type non_zero_blocks: int

    :param peak_active_sessions: [required] Peak number of iSCSI connections
        since midnight UTC.
    :type peak_active_sessions: int

    :param peak_iops: [required] The highest value for *current_iops* since
        midnight UTC.
    :type peak_iops: int

    :param provisioned_space: [required] Total amount of space provisioned in
        all volumes on the cluster.
    :type provisioned_space: int

    :param snapshot_non_zero_blocks: [required] Total number of 4KiB blocks in
        snapshots with data.
    :type snapshot_non_zero_blocks: int

    :param timestamp: [required] The date and time this cluster capacity sample
        was taken.
    :type timestamp: str

    :param total_ops: [required] The total number of I/O operations performed
        throughout the lifetime of the cluster
    :type total_ops: int

    :param unique_blocks: [required] The total number of blocks stored on the
        block drives. The value includes replicated blocks.
    :type unique_blocks: int

    :param unique_blocks_used_space: [required] The total amount of data the
        *unique_blocks* take up on the block drives. This number is always
        consistent with the *unique_blocks* value.
    :type unique_blocks_used_space: int

    :param used_metadata_space: [required] The total amount of bytes on volume
        drives used to store metadata
    :type used_metadata_space: int

    :param used_metadata_space_in_snapshots: [required] The amount of bytes on
        volume drives used for storing unique data in snapshots. This number
        provides an estimate of how much metadata space would be regained by
        deleting all snapshots on the system.
    :type used_metadata_space_in_snapshots: int

    :param used_space: [required] Total amount of space used by all block
        drives in the system.
    :type used_space: int

    :param zero_blocks: [required] Total number of 4KiB blocks without data
        after the last round of garabage collection operation has completed.
    :type zero_blocks: int
    """

    active_block_space = data_model.property(
        "activeBlockSpace", int,
        array=False, optional=False,
        documentation="\
        The amount of space on the block drives.\
        This includes additional information such as metadata entries and\
        space which can be cleaned up.\
        "
    )

    active_sessions = data_model.property(
        "activeSessions", int,
        array=False, optional=False,
        documentation="\
        Number of active iSCSI sessions communicating with the cluster\
        "
    )

    average_iops = data_model.property(
        "averageIOPS", int,
        array=False, optional=False,
        documentation="\
        Average IPS for the cluster since midnight Coordinated Universal Time\
        (UTC).\
        "
    )

    cluster_recent_iosize = data_model.property(
        "clusterRecentIOSize", int,
        array=False, optional=False,
        documentation="\
        The average size of IOPS to all volumes in the cluster.\
        "
    )

    current_iops = data_model.property(
        "currentIOPS", int,
        array=False, optional=False,
        documentation="\
        Average IOPS for all volumes in the cluster over the last 5 seconds.\
        "
    )

    max_iops = data_model.property(
        "maxIOPS", int,
        array=False, optional=False,
        documentation="\
        Estimated maximum IOPS capability of the current cluster.\
        "
    )

    max_over_provisionable_space = data_model.property(
        "maxOverProvisionableSpace", int,
        array=False, optional=False,
        documentation="\
        The maximum amount of provisionable space.\
        This is a computed value.\
        You cannot create new volumes if the current provisioned space plus\
        the new volume size would exceed this number:\
        *max_over_provisionable_space* = *max_provisioned_space* *\
        *get_cluster_full*\
        "
    )

    max_provisioned_space = data_model.property(
        "maxProvisionedSpace", int,
        array=False, optional=False,
        documentation="\
        The total amount of provisionable space if all volumes are 100% filled\
        (no thin provisioned metadata).\
        "
    )

    max_used_metadata_space = data_model.property(
        "maxUsedMetadataSpace", int,
        array=False, optional=False,
        documentation="\
        The amount of bytes on volume drives used to store metadata.\
        "
    )

    max_used_space = data_model.property(
        "maxUsedSpace", int,
        array=False, optional=False,
        documentation="\
        The total amount of space on all active block drives.\
        "
    )

    non_zero_blocks = data_model.property(
        "nonZeroBlocks", int,
        array=False, optional=False,
        documentation="\
        Total number of 4KiB blocks with data after the last garbage\
        collection operation has completed.\
        "
    )

    peak_active_sessions = data_model.property(
        "peakActiveSessions", int,
        array=False, optional=False,
        documentation="\
        Peak number of iSCSI connections since midnight UTC.\
        "
    )

    peak_iops = data_model.property(
        "peakIOPS", int,
        array=False, optional=False,
        documentation="\
        The highest value for *current_iops* since midnight UTC.\
        "
    )

    provisioned_space = data_model.property(
        "provisionedSpace", int,
        array=False, optional=False,
        documentation="\
        Total amount of space provisioned in all volumes on the cluster.\
        "
    )

    snapshot_non_zero_blocks = data_model.property(
        "snapshotNonZeroBlocks", int,
        array=False, optional=False,
        documentation="\
        Total number of 4KiB blocks in snapshots with data.\
        "
    )

    timestamp = data_model.property(
        "timestamp", str,
        array=False, optional=False,
        documentation="\
        The date and time this cluster capacity sample was taken.\
        "
    )

    total_ops = data_model.property(
        "totalOps", int,
        array=False, optional=False,
        documentation="\
        The total number of I/O operations performed throughout the lifetime\
        of the cluster\
        "
    )

    unique_blocks = data_model.property(
        "uniqueBlocks", int,
        array=False, optional=False,
        documentation="\
        The total number of blocks stored on the block drives.\
        The value includes replicated blocks.\
        "
    )

    unique_blocks_used_space = data_model.property(
        "uniqueBlocksUsedSpace", int,
        array=False, optional=False,
        documentation="\
        The total amount of data the *unique_blocks* take up on the block\
        drives.\
        This number is always consistent with the *unique_blocks* value.\
        "
    )

    used_metadata_space = data_model.property(
        "usedMetadataSpace", int,
        array=False, optional=False,
        documentation="\
        The total amount of bytes on volume drives used to store metadata\
        "
    )

    used_metadata_space_in_snapshots = data_model.property(
        "usedMetadataSpaceInSnapshots", int,
        array=False, optional=False,
        documentation="\
        The amount of bytes on volume drives used for storing unique data in\
        snapshots.\
        This number provides an estimate of how much metadata space would be\
        regained by deleting all snapshots on the system.\
        "
    )

    used_space = data_model.property(
        "usedSpace", int,
        array=False, optional=False,
        documentation="\
        Total amount of space used by all block drives in the system.\
        "
    )

    zero_blocks = data_model.property(
        "zeroBlocks", int,
        array=False, optional=False,
        documentation="\
        Total number of 4KiB blocks without data after the last round of\
        garabage collection operation has completed.\
        "
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class DriveStats(data_model.DataObject):
    """

    :param active_sessions: [required]
    :type active_sessions: int

    :param failed_die_count: [required]
    :type failed_die_count: int

    :param life_remaining_percent: [required]
    :type life_remaining_percent: int

    :param lifetime_read_bytes: [required]
    :type lifetime_read_bytes: int

    :param lifetime_write_bytes: [required]
    :type lifetime_write_bytes: int

    :param power_on_hours: [required]
    :type power_on_hours: int

    :param read_bytes: [required]
    :type read_bytes: int

    :param read_ops: [required]
    :type read_ops: int

    :param reallocated_sectors: [required]
    :type reallocated_sectors: int

    :param reserve_capacity_percent: [required]
    :type reserve_capacity_percent: int

    :param timestamp: [required]
    :type timestamp: str

    :param total_capacity: [required]
    :type total_capacity: int

    :param used_memory: [required]
    :type used_memory: int

    :param write_bytes: [required]
    :type write_bytes: int

    :param write_ops: [required]
    :type write_ops: int

    :param used_capacity: (optional)
    :type used_capacity: int
    """

    active_sessions = data_model.property(
        "activeSessions", int,
        array=False, optional=False,
        documentation=None
    )

    failed_die_count = data_model.property(
        "failedDieCount", int,
        array=False, optional=False,
        documentation=None
    )

    life_remaining_percent = data_model.property(
        "lifeRemainingPercent", int,
        array=False, optional=False,
        documentation=None
    )

    lifetime_read_bytes = data_model.property(
        "lifetimeReadBytes", int,
        array=False, optional=False,
        documentation=None
    )

    lifetime_write_bytes = data_model.property(
        "lifetimeWriteBytes", int,
        array=False, optional=False,
        documentation=None
    )

    power_on_hours = data_model.property(
        "powerOnHours", int,
        array=False, optional=False,
        documentation=None
    )

    read_bytes = data_model.property(
        "readBytes", int,
        array=False, optional=False,
        documentation=None
    )

    read_ops = data_model.property(
        "readOps", int,
        array=False, optional=False,
        documentation=None
    )

    reallocated_sectors = data_model.property(
        "reallocatedSectors", int,
        array=False, optional=False,
        documentation=None
    )

    reserve_capacity_percent = data_model.property(
        "reserveCapacityPercent", int,
        array=False, optional=False,
        documentation=None
    )

    timestamp = data_model.property(
        "timestamp", str,
        array=False, optional=False,
        documentation=None
    )

    total_capacity = data_model.property(
        "totalCapacity", int,
        array=False, optional=False,
        documentation=None
    )

    used_capacity = data_model.property(
        "usedCapacity", int,
        array=False, optional=True,
        documentation=None
    )

    used_memory = data_model.property(
        "usedMemory", int,
        array=False, optional=False,
        documentation=None
    )

    write_bytes = data_model.property(
        "writeBytes", int,
        array=False, optional=False,
        documentation=None
    )

    write_ops = data_model.property(
        "writeOps", int,
        array=False, optional=False,
        documentation=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class DrivesHardware(data_model.DataObject):
    """

    :param drive_hardware: [required]
    :type drive_hardware: DriveHardware
    """

    drive_hardware = data_model.property(
        "driveHardware", DriveHardware,
        array=True, optional=False,
        documentation=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class NetworkConfig(data_model.DataObject):
    """

    :param _default: (optional)
    :type _default: bool

    :param address: (optional)
    :type address: str

    :param auto: (optional)
    :type auto: bool

    :param bond_downdelay: (optional)
    :type bond_downdelay: int

    :param bond_fail_over_mac: (optional)
    :type bond_fail_over_mac: str

    :param bond_primary_reselect: (optional)
    :type bond_primary_reselect: str

    :param bond_lacp_rate: (optional)
    :type bond_lacp_rate: str

    :param bond_miimon: (optional)
    :type bond_miimon: int

    :param bond_mode: (optional)
    :type bond_mode: str

    :param bond_slaves: (optional)
    :type bond_slaves: str

    :param bond_updelay: (optional)
    :type bond_updelay: int

    :param broadcast: (optional)
    :type broadcast: str

    :param dns_nameservers: (optional)
    :type dns_nameservers: str

    :param dns_search: (optional)
    :type dns_search: str

    :param family: (optional)
    :type family: str

    :param gateway: (optional)
    :type gateway: str

    :param mac_address: (optional)
    :type mac_address: str

    :param mac_address_permanent: (optional)
    :type mac_address_permanent: str

    :param method: (optional)
    :type method: str

    :param mtu: (optional)
    :type mtu: str

    :param netmask: (optional)
    :type netmask: str

    :param network: (optional)
    :type network: str

    :param physical: (optional)
    :type physical: PhysicalAdapter

    :param routes: (optional)
    :type routes: str

    :param status: (optional)
    :type status: str

    :param symmetric_route_rules: (optional)
    :type symmetric_route_rules: str

    :param up_and_running: (optional)
    :type up_and_running: bool
    """

    _default = data_model.property(
        "#default", bool,
        array=False, optional=True,
        documentation=None
    )

    address = data_model.property(
        "address", str,
        array=False, optional=True,
        documentation=None
    )

    auto = data_model.property(
        "auto", bool,
        array=False, optional=True,
        documentation=None
    )

    bond_downdelay = data_model.property(
        "bond-downdelay", int,
        array=False, optional=True,
        documentation=None
    )

    bond_fail_over_mac = data_model.property(
        "bond-fail_over_mac", str,
        array=False, optional=True,
        documentation=None
    )

    bond_primary_reselect = data_model.property(
        "bond-primary_reselect", str,
        array=False, optional=True,
        documentation=None
    )

    bond_lacp_rate = data_model.property(
        "bond-lacp_rate", str,
        array=False, optional=True,
        documentation=None
    )

    bond_miimon = data_model.property(
        "bond-miimon", int,
        array=False, optional=True,
        documentation=None
    )

    bond_mode = data_model.property(
        "bond-mode", str,
        array=False, optional=True,
        documentation=None
    )

    bond_slaves = data_model.property(
        "bond-slaves", str,
        array=False, optional=True,
        documentation=None
    )

    bond_updelay = data_model.property(
        "bond-updelay", int,
        array=False, optional=True,
        documentation=None
    )

    broadcast = data_model.property(
        "broadcast", str,
        array=False, optional=True,
        documentation=None
    )

    dns_nameservers = data_model.property(
        "dns-nameservers", str,
        array=False, optional=True,
        documentation=None
    )

    dns_search = data_model.property(
        "dns-search", str,
        array=False, optional=True,
        documentation=None
    )

    family = data_model.property(
        "family", str,
        array=False, optional=True,
        documentation=None
    )

    gateway = data_model.property(
        "gateway", str,
        array=False, optional=True,
        documentation=None
    )

    mac_address = data_model.property(
        "macAddress", str,
        array=False, optional=True,
        documentation=None
    )

    mac_address_permanent = data_model.property(
        "macAddressPermanent", str,
        array=False, optional=True,
        documentation=None
    )

    method = data_model.property(
        "method", str,
        array=False, optional=True,
        documentation=None
    )

    mtu = data_model.property(
        "mtu", str,
        array=False, optional=True,
        documentation=None
    )

    netmask = data_model.property(
        "netmask", str,
        array=False, optional=True,
        documentation=None
    )

    network = data_model.property(
        "network", str,
        array=False, optional=True,
        documentation=None
    )

    physical = data_model.property(
        "physical", PhysicalAdapter,
        array=False, optional=True,
        documentation=None
    )

    routes = data_model.property(
        "routes", str,
        array=True, optional=True,
        documentation=None
    )

    status = data_model.property(
        "status", str,
        array=False, optional=True,
        documentation=None
    )

    symmetric_route_rules = data_model.property(
        "symmetricRouteRules", str,
        array=True, optional=True,
        documentation=None
    )

    up_and_running = data_model.property(
        "upAndRunning", bool,
        array=False, optional=True,
        documentation=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class NewDrive(data_model.DataObject):
    """

    :param drive_id: [required] A unique identifier for this drive.
    :type drive_id: int
    """

    drive_id = data_model.property(
        "driveID", int,
        array=False, optional=False,
        documentation="\
        A unique identifier for this drive.\
        "
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class RemoteReplication(data_model.DataObject):
    """
    Details on the volume replication.

    :param mode: [required] Volume replication mode.

        Possible values:

        **Async**: Writes are acknowledged when they complete locally. The
        cluster does not wait for writes to be replicated to the target
        cluster.

        **Sync**: Source acknowledges write when the data is stored locally and
        on the remote cluster.

        **SnapshotsOnly**: Only snapshots created on the source cluster will be
        replicated. Active writes from the source volume will not be
        replicated.



    :type mode: str

    :param pause_limit: [required] The number of occurring write ops before
        auto-pausing, on a per volume pair level.
    :type pause_limit: int

    :param remote_service_id: [required] The remote slice service ID.
    :type remote_service_id: int

    :param resume_details: [required] Reserved for future use.
    :type resume_details: str

    :param snapshot_replication: [required] The details of snapshot
        replication.
    :type snapshot_replication: SnapshotReplication

    :param state: [required] The state of the volume replication.
    :type state: str

    :param state_details: [required] Reserved for future use.
    :type state_details: str
    """

    mode = data_model.property(
        "mode", str,
        array=False, optional=False,
        documentation="\
        Volume replication mode.\
\
\
\
        Possible values:\
\
\
\
        **Async**: Writes are acknowledged when they complete locally. The\
        cluster does not wait for writes to be replicated to the target\
        cluster.\
\
\
\
        **Sync**: Source acknowledges write when the data is stored locally\
        and on the remote cluster.\
\
\
\
        **SnapshotsOnly**: Only snapshots created on the source cluster will\
        be replicated. Active writes from the source volume will not be\
        replicated.\
\
\
\
        "
    )

    pause_limit = data_model.property(
        "pauseLimit", int,
        array=False, optional=False,
        documentation="\
        The number of occurring write ops before auto-pausing, on a per volume\
        pair level.\
        "
    )

    remote_service_id = data_model.property(
        "remoteServiceID", int,
        array=False, optional=False,
        documentation="\
        The remote slice service ID.\
        "
    )

    resume_details = data_model.property(
        "resumeDetails", str,
        array=False, optional=False,
        documentation="\
        Reserved for future use.\
        "
    )

    snapshot_replication = data_model.property(
        "snapshotReplication", SnapshotReplication,
        array=False, optional=False,
        documentation="\
        The details of snapshot replication.\
        "
    )

    state = data_model.property(
        "state", str,
        array=False, optional=False,
        documentation="\
        The state of the volume replication.\
        "
    )

    state_details = data_model.property(
        "stateDetails", str,
        array=False, optional=False,
        documentation="\
        Reserved for future use.\
        "
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class ResetDrivesDetails(data_model.DataObject):
    """

    :param drives: [required] Details of a single drive that is being reset.
    :type drives: ResetDriveDetails
    """

    drives = data_model.property(
        "drives", ResetDriveDetails,
        array=True, optional=False,
        documentation="\
        Details of a single drive that is being reset.\
        "
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class ClusterAdmin(data_model.DataObject):
    """

    :param access: [required]
    :type access: str

    :param cluster_admin_id: [required]
    :type cluster_admin_id: int

    :param username: [required]
    :type username: str

    :param attributes: [required] List of Name/Value pairs in JSON object
        format.
    :type attributes: dict
    """

    access = data_model.property(
        "access", str,
        array=True, optional=False,
        documentation=None
    )

    cluster_admin_id = data_model.property(
        "clusterAdminID", int,
        array=False, optional=False,
        documentation=None
    )

    username = data_model.property(
        "username", str,
        array=False, optional=False,
        documentation=None
    )

    attributes = data_model.property(
        "attributes", dict,
        array=False, optional=False,
        documentation="\
        List of Name/Value pairs in JSON object format.\
        "
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class ClusterVersionInfo(data_model.DataObject):
    """
    Version information for a node in the cluster.

    :param node_id: [required]
    :type node_id: int

    :param node_version: [required]
    :type node_version: str

    :param node_internal_revision: [required]
    :type node_internal_revision: str
    """

    node_id = data_model.property(
        "nodeID", int,
        array=False, optional=False,
        documentation=None
    )

    node_version = data_model.property(
        "nodeVersion", str,
        array=False, optional=False,
        documentation=None
    )

    node_internal_revision = data_model.property(
        "nodeInternalRevision", str,
        array=False, optional=False,
        documentation=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class Network(data_model.DataObject):
    """

    :param bond10_g: (optional)
    :type bond10_g: NetworkConfig

    :param bond1_g: (optional)
    :type bond1_g: NetworkConfig
    """

    bond10_g = data_model.property(
        "Bond10G", NetworkConfig,
        array=False, optional=True,
        documentation=None
    )

    bond1_g = data_model.property(
        "Bond1G", NetworkConfig,
        array=False, optional=True,
        documentation=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class DriveInfo(data_model.DataObject):
    """

    :param capacity: [required] Total capacity of the drive, in bytes.
    :type capacity: int

    :param drive_id: [required] *drive_id* for this drive.
    :type drive_id: int

    :param node_id: [required] *node_id* where this drive is located.
    :type node_id: int

    :param serial: [required] Drive serial number.
    :type serial: str

    :param slot: [required] Slot number in the server chassis where this drive
        is located, or -1 if *satadimm* used for internal metadata drive.
    :type slot: int

    :param status: [required]
    :type status: str

    :param type: [required]
    :type type: str

    :param attributes: [required] List of Name/Value pairs in JSON object
        format.
    :type attributes: dict
    """

    capacity = data_model.property(
        "capacity", int,
        array=False, optional=False,
        documentation="\
        Total capacity of the drive, in bytes.\
        "
    )

    drive_id = data_model.property(
        "driveID", int,
        array=False, optional=False,
        documentation="\
        *drive_id* for this drive.\
        "
    )

    node_id = data_model.property(
        "nodeID", int,
        array=False, optional=False,
        documentation="\
        *node_id* where this drive is located.\
        "
    )

    serial = data_model.property(
        "serial", str,
        array=False, optional=False,
        documentation="\
        Drive serial number.\
        "
    )

    slot = data_model.property(
        "slot", int,
        array=False, optional=False,
        documentation="\
        Slot number in the server chassis where this drive is located, or -1\
        if *satadimm* used for internal metadata drive.\
        "
    )

    status = data_model.property(
        "status", str,
        array=False, optional=False,
        documentation=None
    )

    type = data_model.property(
        "type", str,
        array=False, optional=False,
        documentation=None
    )

    attributes = data_model.property(
        "attributes", dict,
        array=False, optional=False,
        documentation="\
        List of Name/Value pairs in JSON object format.\
        "
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class GroupSnapshotMembers(data_model.DataObject):
    """
    List of checksum, *volume_ids* and *snapshot_ids* for each member of the
    group.

    :param volume_id: [required] The source volume ID for the snapshot.
    :type volume_id: int

    :param snapshot_id: [required] Unique ID of a snapshot from which the new
        snapshot is made. The *snapshot_id* passed must be a snapshot on the
        given volume.
    :type snapshot_id: int

    :param snapshot_uuid: [required] Universal Unique ID of an existing
        snapshot.
    :type snapshot_uuid: str

    :param checksum: [required] A string that represents the correct digits in
        the stored snapshot. This checksum can be used later to compare other
        snapshots to detect errors in the data.
    :type checksum: str
    """

    volume_id = data_model.property(
        "volumeID", int,
        array=False, optional=False,
        documentation="\
        The source volume ID for the snapshot.\
        "
    )

    snapshot_id = data_model.property(
        "snapshotID", int,
        array=False, optional=False,
        documentation="\
        Unique ID of a snapshot from which the new snapshot is made.\
        The *snapshot_id* passed must be a snapshot on the given volume.\
        "
    )

    snapshot_uuid = data_model.property(
        "SnapshotUUID", str,
        array=False, optional=False,
        documentation="\
        Universal Unique ID of an existing snapshot.\
        "
    )

    checksum = data_model.property(
        "checksum", str,
        array=False, optional=False,
        documentation="\
        A string that represents the correct digits in the stored snapshot.\
        This checksum can be used later to compare other snapshots to detect\
        errors in the data.\
        "
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class GroupSnapshot(data_model.DataObject):
    """
    Group Snapshot object represents a point-in-time copy of a group of
    volumes.

    :param group_snapshot_id: [required] Unique ID of the new group snapshot.
    :type group_snapshot_id: int

    :param group_snapshot_uuid: [required] UUID of the group snapshot.
    :type group_snapshot_uuid: UUID

    :param members: [required] List of *volume_ids* and *snapshot_ids* for each
        member of the group.
    :type members: GroupSnapshotMembers

    :param name: [required] Name of the group snapshot, or, if none was given,
        the UTC formatted day and time on which the snapshot was created.
    :type name: str

    :param create_time: [required] The UTC formatted day and time on which the
        snapshot was created.
    :type create_time: str

    :param status: [required] Status of the snapshot. Possible values:

        **Preparing**: A snapshot that is being prepared for use and is not yet
        writable.

        **Done**: A snapshot that has finished being prepared and is now usable

    :type status: str

    :param attributes: [required] List of Name/Value pairs in JSON object
        format.
    :type attributes: dict
    """

    group_snapshot_id = data_model.property(
        "groupSnapshotID", int,
        array=False, optional=False,
        documentation="\
        Unique ID of the new group snapshot.\
        "
    )

    group_snapshot_uuid = data_model.property(
        "groupSnapshotUUID", UUID,
        array=False, optional=False,
        documentation="\
        UUID of the group snapshot.\
        "
    )

    members = data_model.property(
        "members", GroupSnapshotMembers,
        array=True, optional=False,
        documentation="\
        List of *volume_ids* and *snapshot_ids* for each member of the group.\
        "
    )

    name = data_model.property(
        "name", str,
        array=False, optional=False,
        documentation="\
        Name of the group snapshot, or, if none was given, the UTC formatted\
        day and time on which the snapshot was created.\
        "
    )

    create_time = data_model.property(
        "createTime", str,
        array=False, optional=False,
        documentation="\
        The UTC formatted day and time on which the snapshot was created.\
        "
    )

    status = data_model.property(
        "status", str,
        array=False, optional=False,
        documentation="\
        Status of the snapshot.\
        Possible values:\
\
\
            **Preparing**: A snapshot that is being prepared for use and is\
        not yet writable.\
\
\
\
            **Done**: A snapshot that has finished being prepared and is now\
        usable\
\
        "
    )

    attributes = data_model.property(
        "attributes", dict,
        array=False, optional=False,
        documentation="\
        List of Name/Value pairs in JSON object format.\
        "
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class MetadataHosts(data_model.DataObject):
    """
    The volume services on which the volume metadata resides.

    :param dead_secondaries: [required] Secondary metadata (slice) services
        that are in a dead state.
    :type dead_secondaries: int

    :param live_secondaries: [required] Secondary metadata (slice) services
        that are currently in a \"live\" state.
    :type live_secondaries: int

    :param primary: [required] The primary metadata (slice) services hosting
        the volume.
    :type primary: int
    """

    dead_secondaries = data_model.property(
        "deadSecondaries", int,
        array=True, optional=False,
        documentation="\
        Secondary metadata (slice) services that are in a dead state.\
        "
    )

    live_secondaries = data_model.property(
        "liveSecondaries", int,
        array=True, optional=False,
        documentation="\
        Secondary metadata (slice) services that are currently in a \"live\"\
        state.\
        "
    )

    primary = data_model.property(
        "primary", int,
        array=False, optional=False,
        documentation="\
        The primary metadata (slice) services hosting the volume.\
        "
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class NodeDriveHardware(data_model.DataObject):
    """

    :param node_id: [required]
    :type node_id: int

    :param result: [required]
    :type result: DrivesHardware
    """

    node_id = data_model.property(
        "nodeID", int,
        array=False, optional=False,
        documentation=None
    )

    result = data_model.property(
        "result", DrivesHardware,
        array=False, optional=False,
        documentation=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class VolumePair(data_model.DataObject):
    """
    The Volume Pair Info is an object containing information about a volume
    that is paired on a remote cluster.
    If the volume is not paired, this object is null.

    :param cluster_pair_id: [required] The remote cluster a volume is paired
        with.
    :type cluster_pair_id: int

    :param remote_volume_id: [required] The *volume_id* on the remote cluster a
        volume is paired with.
    :type remote_volume_id: int

    :param remote_slice_id: [required] The *slice_id* on the remote cluster a
        volume is paired with.
    :type remote_slice_id: int

    :param remote_volume_name: [required] The last-observed name of the volume
        on the remote cluster a volume is paired with.
    :type remote_volume_name: str

    :param volume_pair_uuid: [required] A UUID in canonical form.
    :type volume_pair_uuid: UUID

    :param remote_replication: [required] Details about the replication
        configuration for this volume pair.
    :type remote_replication: RemoteReplication
    """

    cluster_pair_id = data_model.property(
        "clusterPairID", int,
        array=False, optional=False,
        documentation="\
        The remote cluster a volume is paired with.\
        "
    )

    remote_volume_id = data_model.property(
        "remoteVolumeID", int,
        array=False, optional=False,
        documentation="\
        The *volume_id* on the remote cluster a volume is paired with.\
        "
    )

    remote_slice_id = data_model.property(
        "remoteSliceID", int,
        array=False, optional=False,
        documentation="\
        The *slice_id* on the remote cluster a volume is paired with.\
        "
    )

    remote_volume_name = data_model.property(
        "remoteVolumeName", str,
        array=False, optional=False,
        documentation="\
        The last-observed name of the volume on the remote cluster a volume is\
        paired with.\
        "
    )

    volume_pair_uuid = data_model.property(
        "volumePairUUID", UUID,
        array=False, optional=False,
        documentation="\
        A UUID in canonical form.\
        "
    )

    remote_replication = data_model.property(
        "remoteReplication", RemoteReplication,
        array=False, optional=False,
        documentation="\
        Details about the replication configuration for this volume pair.\
        "
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class SoftwareVersionInfo(data_model.DataObject):
    """

    :param current_version: [required]
    :type current_version: str

    :param node_id: [required]
    :type node_id: int

    :param package_name: [required]
    :type package_name: str

    :param pending_version: [required]
    :type pending_version: str

    :param start_time: [required]
    :type start_time: str
    """

    current_version = data_model.property(
        "currentVersion", str,
        array=False, optional=False,
        documentation=None
    )

    node_id = data_model.property(
        "nodeID", int,
        array=False, optional=False,
        documentation=None
    )

    package_name = data_model.property(
        "packageName", str,
        array=False, optional=False,
        documentation=None
    )

    pending_version = data_model.property(
        "pendingVersion", str,
        array=False, optional=False,
        documentation=None
    )

    start_time = data_model.property(
        "startTime", str,
        array=False, optional=False,
        documentation=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class VolumeAccessGroup(data_model.DataObject):
    """
    A volume access group is a useful way of grouping volumes and initiators
    together for ease of management.




    Volume Access Group Limits:




    - A volume access group can contain up to sixty-four initiator IQNs.
    - An initiator can only belong to only one volume access group.
    - A volume access group can contain up to two thousand volumes.
    - Each volume access group can belong to a maximum of four other volume
      access groups.

    :param volume_access_group_id: [required] Unique ID for this volume access
        group.
    :type volume_access_group_id: int

    :param name: [required] Name of the volume access group.
    :type name: str

    :param initiators: [required] List of unique initiator names belonging to
        the volume access group.
    :type initiators: str

    :param volumes: [required] List of volumes belonging to the volume access
        group.
    :type volumes: int
    """

    volume_access_group_id = data_model.property(
        "volumeAccessGroupID", int,
        array=False, optional=False,
        documentation="\
        Unique ID for this volume access group.\
        "
    )

    name = data_model.property(
        "name", str,
        array=False, optional=False,
        documentation="\
        Name of the volume access group.\
        "
    )

    initiators = data_model.property(
        "initiators", str,
        array=True, optional=False,
        documentation="\
        List of unique initiator names belonging to the volume access group.\
        "
    )

    volumes = data_model.property(
        "volumes", int,
        array=True, optional=False,
        documentation="\
        List of volumes belonging to the volume access group.\
        "
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class VirtualNetwork(data_model.DataObject):
    """

    :param virtual_network_id: [required] SolidFire unique identifier for a
        virtual network.
    :type virtual_network_id: int

    :param virtual_network_tag: [required] VLAN Tag identifier.
    :type virtual_network_tag: int

    :param address_blocks: [required] Range of address blocks currently
        assigned to the virtual network. **available:** Binary string in \"1\"s
        and \"0\"s. 1 equals the IP is available and 0 equals the IP is not
        available. The string is read from right to left with the digit to the
        far right being the first IP address in the list of addressBlocks.
        **size:** the size of this block of addresses. **start:** first IP
        address in the block.
    :type address_blocks: AddressBlock

    :param attributes: [required] List of Name/Value pairs in JSON object
        format.
    :type attributes: dict

    :param name: [required] The name assigned to the virtual network.
    :type name: str

    :param netmask: [required] IP address of the netmask for the virtual
        network.
    :type netmask: str

    :param svip: [required] Storage IP address for the virtual network.
    :type svip: str
    """

    virtual_network_id = data_model.property(
        "virtualNetworkID", int,
        array=False, optional=False,
        documentation="\
        SolidFire unique identifier for a virtual network.\
        "
    )

    virtual_network_tag = data_model.property(
        "virtualNetworkTag", int,
        array=False, optional=False,
        documentation="\
        VLAN Tag identifier.\
        "
    )

    address_blocks = data_model.property(
        "addressBlocks", AddressBlock,
        array=True, optional=False,
        documentation="\
        Range of address blocks currently assigned to the virtual network.\
        **available:** Binary string in \"1\"s and \"0\"s. 1 equals the IP is\
        available and 0 equals the IP is not available. The string is read\
        from right to left with the digit to the far right being the first IP\
        address in the list of addressBlocks.\
        **size:** the size of this block of addresses.\
        **start:** first IP address in the block.\
        "
    )

    attributes = data_model.property(
        "attributes", dict,
        array=False, optional=False,
        documentation="\
        List of Name/Value pairs in JSON object format.\
        "
    )

    name = data_model.property(
        "name", str,
        array=False, optional=False,
        documentation="\
        The name assigned to the virtual network.\
        "
    )

    netmask = data_model.property(
        "netmask", str,
        array=False, optional=False,
        documentation="\
        IP address of the netmask for the virtual network.\
        "
    )

    svip = data_model.property(
        "svip", str,
        array=False, optional=False,
        documentation="\
        Storage IP address for the virtual network.\
        "
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class Weekday(data_model.DataObject):
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


class ClusterCapacity(data_model.DataObject):
    """
    High level capacity measurements for the entire cluster.

    :param active_block_space: [required] The amount of space on the block
        drives. This includes additional information such as metadata entries
        and space which can be cleaned up.
    :type active_block_space: int

    :param active_sessions: [required] Number of active iSCSI sessions
        communicating with the cluster
    :type active_sessions: int

    :param average_iops: [required] Average IPS for the cluster since midnight
        Coordinated Universal Time (UTC).
    :type average_iops: int

    :param cluster_recent_iosize: [required] The average size of IOPS to all
        volumes in the cluster.
    :type cluster_recent_iosize: int

    :param current_iops: [required] Average IOPS for all volumes in the cluster
        over the last 5 seconds.
    :type current_iops: int

    :param max_iops: [required] Estimated maximum IOPS capability of the
        current cluster.
    :type max_iops: int

    :param max_over_provisionable_space: [required] The maximum amount of
        provisionable space. This is a computed value. You cannot create new
        volumes if the current provisioned space plus the new volume size would
        exceed this number: *max_over_provisionable_space* =
        *max_provisioned_space* * *get_cluster_full*
    :type max_over_provisionable_space: int

    :param max_provisioned_space: [required] The total amount of provisionable
        space if all volumes are 100% filled (no thin provisioned metadata).
    :type max_provisioned_space: int

    :param max_used_metadata_space: [required] The amount of bytes on volume
        drives used to store metadata.
    :type max_used_metadata_space: int

    :param max_used_space: [required] The total amount of space on all active
        block drives.
    :type max_used_space: int

    :param non_zero_blocks: [required] Total number of 4KiB blocks with data
        after the last garbage collection operation has completed.
    :type non_zero_blocks: int

    :param peak_active_sessions: [required] Peak number of iSCSI connections
        since midnight UTC.
    :type peak_active_sessions: int

    :param peak_iops: [required] The highest value for *current_iops* since
        midnight UTC.
    :type peak_iops: int

    :param provisioned_space: [required] Total amount of space provisioned in
        all volumes on the cluster.
    :type provisioned_space: int

    :param snapshot_non_zero_blocks: [required] Total number of 4KiB blocks in
        snapshots with data.
    :type snapshot_non_zero_blocks: int

    :param timestamp: [required] The date and time this cluster capacity sample
        was taken.
    :type timestamp: str

    :param total_ops: [required] The total number of I/O operations performed
        throughout the lifetime of the cluster
    :type total_ops: int

    :param unique_blocks: [required] The total number of blocks stored on the
        block drives. The value includes replicated blocks.
    :type unique_blocks: int

    :param unique_blocks_used_space: [required] The total amount of data the
        *unique_blocks* take up on the block drives. This number is always
        consistent with the *unique_blocks* value.
    :type unique_blocks_used_space: int

    :param used_metadata_space: [required] The total amount of bytes on volume
        drives used to store metadata
    :type used_metadata_space: int

    :param used_metadata_space_in_snapshots: [required] The amount of bytes on
        volume drives used for storing unique data in snapshots. This number
        provides an estimate of how much metadata space would be regained by
        deleting all snapshots on the system.
    :type used_metadata_space_in_snapshots: int

    :param used_space: [required] Total amount of space used by all block
        drives in the system.
    :type used_space: int

    :param zero_blocks: [required] Total number of 4KiB blocks without data
        after the last round of garabage collection operation has completed.
    :type zero_blocks: int
    """

    active_block_space = data_model.property(
        "activeBlockSpace", int,
        array=False, optional=False,
        documentation="\
        The amount of space on the block drives.\
        This includes additional information such as metadata entries and\
        space which can be cleaned up.\
        "
    )

    active_sessions = data_model.property(
        "activeSessions", int,
        array=False, optional=False,
        documentation="\
        Number of active iSCSI sessions communicating with the cluster\
        "
    )

    average_iops = data_model.property(
        "averageIOPS", int,
        array=False, optional=False,
        documentation="\
        Average IPS for the cluster since midnight Coordinated Universal Time\
        (UTC).\
        "
    )

    cluster_recent_iosize = data_model.property(
        "clusterRecentIOSize", int,
        array=False, optional=False,
        documentation="\
        The average size of IOPS to all volumes in the cluster.\
        "
    )

    current_iops = data_model.property(
        "currentIOPS", int,
        array=False, optional=False,
        documentation="\
        Average IOPS for all volumes in the cluster over the last 5 seconds.\
        "
    )

    max_iops = data_model.property(
        "maxIOPS", int,
        array=False, optional=False,
        documentation="\
        Estimated maximum IOPS capability of the current cluster.\
        "
    )

    max_over_provisionable_space = data_model.property(
        "maxOverProvisionableSpace", int,
        array=False, optional=False,
        documentation="\
        The maximum amount of provisionable space.\
        This is a computed value.\
        You cannot create new volumes if the current provisioned space plus\
        the new volume size would exceed this number:\
        *max_over_provisionable_space* = *max_provisioned_space* *\
        *get_cluster_full*\
        "
    )

    max_provisioned_space = data_model.property(
        "maxProvisionedSpace", int,
        array=False, optional=False,
        documentation="\
        The total amount of provisionable space if all volumes are 100% filled\
        (no thin provisioned metadata).\
        "
    )

    max_used_metadata_space = data_model.property(
        "maxUsedMetadataSpace", int,
        array=False, optional=False,
        documentation="\
        The amount of bytes on volume drives used to store metadata.\
        "
    )

    max_used_space = data_model.property(
        "maxUsedSpace", int,
        array=False, optional=False,
        documentation="\
        The total amount of space on all active block drives.\
        "
    )

    non_zero_blocks = data_model.property(
        "nonZeroBlocks", int,
        array=False, optional=False,
        documentation="\
        Total number of 4KiB blocks with data after the last garbage\
        collection operation has completed.\
        "
    )

    peak_active_sessions = data_model.property(
        "peakActiveSessions", int,
        array=False, optional=False,
        documentation="\
        Peak number of iSCSI connections since midnight UTC.\
        "
    )

    peak_iops = data_model.property(
        "peakIOPS", int,
        array=False, optional=False,
        documentation="\
        The highest value for *current_iops* since midnight UTC.\
        "
    )

    provisioned_space = data_model.property(
        "provisionedSpace", int,
        array=False, optional=False,
        documentation="\
        Total amount of space provisioned in all volumes on the cluster.\
        "
    )

    snapshot_non_zero_blocks = data_model.property(
        "snapshotNonZeroBlocks", int,
        array=False, optional=False,
        documentation="\
        Total number of 4KiB blocks in snapshots with data.\
        "
    )

    timestamp = data_model.property(
        "timestamp", str,
        array=False, optional=False,
        documentation="\
        The date and time this cluster capacity sample was taken.\
        "
    )

    total_ops = data_model.property(
        "totalOps", int,
        array=False, optional=False,
        documentation="\
        The total number of I/O operations performed throughout the lifetime\
        of the cluster\
        "
    )

    unique_blocks = data_model.property(
        "uniqueBlocks", int,
        array=False, optional=False,
        documentation="\
        The total number of blocks stored on the block drives.\
        The value includes replicated blocks.\
        "
    )

    unique_blocks_used_space = data_model.property(
        "uniqueBlocksUsedSpace", int,
        array=False, optional=False,
        documentation="\
        The total amount of data the *unique_blocks* take up on the block\
        drives.\
        This number is always consistent with the *unique_blocks* value.\
        "
    )

    used_metadata_space = data_model.property(
        "usedMetadataSpace", int,
        array=False, optional=False,
        documentation="\
        The total amount of bytes on volume drives used to store metadata\
        "
    )

    used_metadata_space_in_snapshots = data_model.property(
        "usedMetadataSpaceInSnapshots", int,
        array=False, optional=False,
        documentation="\
        The amount of bytes on volume drives used for storing unique data in\
        snapshots.\
        This number provides an estimate of how much metadata space would be\
        regained by deleting all snapshots on the system.\
        "
    )

    used_space = data_model.property(
        "usedSpace", int,
        array=False, optional=False,
        documentation="\
        Total amount of space used by all block drives in the system.\
        "
    )

    zero_blocks = data_model.property(
        "zeroBlocks", int,
        array=False, optional=False,
        documentation="\
        Total number of 4KiB blocks without data after the last round of\
        garabage collection operation has completed.\
        "
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class FibreChannelPortList(data_model.DataObject):
    """
    List of all Fibre Channel ports.

    :param fibre_channel_ports: [required] List of all physical Fibre Channel
        ports.
    :type fibre_channel_ports: FibreChannelPortInfo[]
    """

    fibre_channel_ports = data_model.property(
        "fibreChannelPorts", FibreChannelPortInfo,
        array=True, optional=False,
        documentation="\
        List of all physical Fibre Channel ports.\
        "
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class NetworkConfig(data_model.DataObject):
    """

    :param _default: (optional)
    :type _default: bool

    :param address: (optional)
    :type address: str

    :param auto: (optional)
    :type auto: bool

    :param bond_downdelay: (optional)
    :type bond_downdelay: int

    :param bond_fail_over_mac: (optional)
    :type bond_fail_over_mac: str

    :param bond_primary_reselect: (optional)
    :type bond_primary_reselect: str

    :param bond_lacp_rate: (optional)
    :type bond_lacp_rate: str

    :param bond_miimon: (optional)
    :type bond_miimon: int

    :param bond_mode: (optional)
    :type bond_mode: str

    :param bond_slaves: (optional)
    :type bond_slaves: str

    :param bond_updelay: (optional)
    :type bond_updelay: int

    :param broadcast: (optional)
    :type broadcast: str

    :param dns_nameservers: (optional)
    :type dns_nameservers: str

    :param dns_search: (optional)
    :type dns_search: str

    :param family: (optional)
    :type family: str

    :param gateway: (optional)
    :type gateway: str

    :param mac_address: (optional)
    :type mac_address: str

    :param mac_address_permanent: (optional)
    :type mac_address_permanent: str

    :param method: (optional)
    :type method: str

    :param mtu: (optional)
    :type mtu: str

    :param netmask: (optional)
    :type netmask: str

    :param network: (optional)
    :type network: str

    :param physical: (optional)
    :type physical: PhysicalAdapter

    :param routes: (optional)
    :type routes: str[]

    :param status: (optional)
    :type status: str

    :param symmetric_route_rules: (optional)
    :type symmetric_route_rules: str[]

    :param up_and_running: (optional)
    :type up_and_running: bool
    """

    _default = data_model.property(
        "#default", bool,
        array=False, optional=True,
        documentation=None
    )

    address = data_model.property(
        "address", str,
        array=False, optional=True,
        documentation=None
    )

    auto = data_model.property(
        "auto", bool,
        array=False, optional=True,
        documentation=None
    )

    bond_downdelay = data_model.property(
        "bond-downdelay", int,
        array=False, optional=True,
        documentation=None
    )

    bond_fail_over_mac = data_model.property(
        "bond-fail_over_mac", str,
        array=False, optional=True,
        documentation=None
    )

    bond_primary_reselect = data_model.property(
        "bond-primary_reselect", str,
        array=False, optional=True,
        documentation=None
    )

    bond_lacp_rate = data_model.property(
        "bond-lacp_rate", str,
        array=False, optional=True,
        documentation=None
    )

    bond_miimon = data_model.property(
        "bond-miimon", int,
        array=False, optional=True,
        documentation=None
    )

    bond_mode = data_model.property(
        "bond-mode", str,
        array=False, optional=True,
        documentation=None
    )

    bond_slaves = data_model.property(
        "bond-slaves", str,
        array=False, optional=True,
        documentation=None
    )

    bond_updelay = data_model.property(
        "bond-updelay", int,
        array=False, optional=True,
        documentation=None
    )

    broadcast = data_model.property(
        "broadcast", str,
        array=False, optional=True,
        documentation=None
    )

    dns_nameservers = data_model.property(
        "dns-nameservers", str,
        array=False, optional=True,
        documentation=None
    )

    dns_search = data_model.property(
        "dns-search", str,
        array=False, optional=True,
        documentation=None
    )

    family = data_model.property(
        "family", str,
        array=False, optional=True,
        documentation=None
    )

    gateway = data_model.property(
        "gateway", str,
        array=False, optional=True,
        documentation=None
    )

    mac_address = data_model.property(
        "macAddress", str,
        array=False, optional=True,
        documentation=None
    )

    mac_address_permanent = data_model.property(
        "macAddressPermanent", str,
        array=False, optional=True,
        documentation=None
    )

    method = data_model.property(
        "method", str,
        array=False, optional=True,
        documentation=None
    )

    mtu = data_model.property(
        "mtu", str,
        array=False, optional=True,
        documentation=None
    )

    netmask = data_model.property(
        "netmask", str,
        array=False, optional=True,
        documentation=None
    )

    network = data_model.property(
        "network", str,
        array=False, optional=True,
        documentation=None
    )

    physical = data_model.property(
        "physical", PhysicalAdapter,
        array=False, optional=True,
        documentation=None
    )

    routes = data_model.property(
        "routes", str,
        array=True, optional=True,
        documentation=None
    )

    status = data_model.property(
        "status", str,
        array=False, optional=True,
        documentation=None
    )

    symmetric_route_rules = data_model.property(
        "symmetricRouteRules", str,
        array=True, optional=True,
        documentation=None
    )

    up_and_running = data_model.property(
        "upAndRunning", bool,
        array=False, optional=True,
        documentation=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class NewDrive(data_model.DataObject):
    """

    :param drive_id: [required] A unique identifier for this drive.
    :type drive_id: int
    """

    drive_id = data_model.property(
        "driveID", int,
        array=False, optional=False,
        documentation="\
        A unique identifier for this drive.\
        "
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class PairedCluster(data_model.DataObject):
    """

    :param cluster_name: [required] Name of the other cluster in the pair
    :type cluster_name: str

    :param cluster_pair_id: [required] Unique ID given to each cluster in the
        pair.
    :type cluster_pair_id: int

    :param cluster_pair_uuid: [required] Universally unique identifier.
    :type cluster_pair_uuid: UUID

    :param latency: [required] Number, in milliseconds, of latency between
        clusters.
    :type latency: int

    :param mvip: [required] IP of the management connection for paired
        clusters.
    :type mvip: str

    :param status: [required] Can be one of the following:

        **Connected**

        **Misconfigured**

        **Disconnected**

    :type status: str

    :param version: [required] The Element OS version of the other cluster in
        the pair.
    :type version: str
    """

    cluster_name = data_model.property(
        "clusterName", str,
        array=False, optional=False,
        documentation="\
        Name of the other cluster in the pair\
        "
    )

    cluster_pair_id = data_model.property(
        "clusterPairID", int,
        array=False, optional=False,
        documentation="\
        Unique ID given to each cluster in the pair.\
        "
    )

    cluster_pair_uuid = data_model.property(
        "clusterPairUUID", UUID,
        array=False, optional=False,
        documentation="\
        Universally unique identifier.\
        "
    )

    latency = data_model.property(
        "latency", int,
        array=False, optional=False,
        documentation="\
        Number, in milliseconds, of latency between clusters.\
        "
    )

    mvip = data_model.property(
        "mvip", str,
        array=False, optional=False,
        documentation="\
        IP of the management connection for paired clusters.\
        "
    )

    status = data_model.property(
        "status", str,
        array=False, optional=False,
        documentation="\
        Can be one of the following:\
\
\
            **Connected**\
\
\
\
            **Misconfigured**\
\
\
\
            **Disconnected**\
\
        "
    )

    version = data_model.property(
        "version", str,
        array=False, optional=False,
        documentation="\
        The Element OS version of the other cluster in the pair.\
        "
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class RemoteReplication(data_model.DataObject):
    """
    Details on the volume replication.

    :param mode: [required] Volume replication mode.

        Possible values:

        **Async**: Writes are acknowledged when they complete locally. The
        cluster does not wait for writes to be replicated to the target
        cluster.

        **Sync**: Source acknowledges write when the data is stored locally and
        on the remote cluster.

        **SnapshotsOnly**: Only snapshots created on the source cluster will be
        replicated. Active writes from the source volume will not be
        replicated.



    :type mode: str

    :param pause_limit: [required] The number of occurring write ops before
        auto-pausing, on a per volume pair level.
    :type pause_limit: int

    :param remote_service_id: [required] The remote slice service ID.
    :type remote_service_id: int

    :param resume_details: [required] Reserved for future use.
    :type resume_details: str

    :param snapshot_replication: [required] The details of snapshot
        replication.
    :type snapshot_replication: SnapshotReplication

    :param state: [required] The state of the volume replication.
    :type state: str

    :param state_details: [required] Reserved for future use.
    :type state_details: str
    """

    mode = data_model.property(
        "mode", str,
        array=False, optional=False,
        documentation="\
        Volume replication mode.\
\
\
\
        Possible values:\
\
\
\
        **Async**: Writes are acknowledged when they complete locally. The\
        cluster does not wait for writes to be replicated to the target\
        cluster.\
\
\
\
        **Sync**: Source acknowledges write when the data is stored locally\
        and on the remote cluster.\
\
\
\
        **SnapshotsOnly**: Only snapshots created on the source cluster will\
        be replicated. Active writes from the source volume will not be\
        replicated.\
\
\
\
        "
    )

    pause_limit = data_model.property(
        "pauseLimit", int,
        array=False, optional=False,
        documentation="\
        The number of occurring write ops before auto-pausing, on a per volume\
        pair level.\
        "
    )

    remote_service_id = data_model.property(
        "remoteServiceID", int,
        array=False, optional=False,
        documentation="\
        The remote slice service ID.\
        "
    )

    resume_details = data_model.property(
        "resumeDetails", str,
        array=False, optional=False,
        documentation="\
        Reserved for future use.\
        "
    )

    snapshot_replication = data_model.property(
        "snapshotReplication", SnapshotReplication,
        array=False, optional=False,
        documentation="\
        The details of snapshot replication.\
        "
    )

    state = data_model.property(
        "state", str,
        array=False, optional=False,
        documentation="\
        The state of the volume replication.\
        "
    )

    state_details = data_model.property(
        "stateDetails", str,
        array=False, optional=False,
        documentation="\
        Reserved for future use.\
        "
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class ClusterAdmin(data_model.DataObject):
    """
    The object containing information about a backup target.

    :param name: [required] Name for the backup target.
    :type name: str

    :param backup_target_id: [required] Unique identifier assigned to the
        backup target.
    :type backup_target_id: int

    :param attributes: (optional) List of Name/Value pairs in JSON object
        format.
    :type attributes: dict
    """

    name = data_model.property(
        "name", str,
        array=False, optional=False,
        documentation="\
        Name for the backup target.\
        "
    )

    backup_target_id = data_model.property(
        "backupTargetID", int,
        array=False, optional=False,
        documentation="\
        Unique identifier assigned to the backup target.\
        "
    )

    attributes = data_model.property(
        "attributes", dict,
        array=False, optional=True,
        documentation="\
        List of Name/Value pairs in JSON object format.\
        "
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class BulkVolumeJob(data_model.DataObject):
    """

    :param bulk_volume_id: [required] The internal bulk volume job ID.
    :type bulk_volume_id: int

    :param create_time: [required] Timestamp created for the bulk volume job.
    :type create_time: str

    :param elapsed_time: [required] The number of seconds since the job began.
    :type elapsed_time: int

    :param format: [required] Format is either \"compressed\" or \"native\".
    :type format: str

    :param key: [required] The unique key created by the bulk volume session.
    :type key: str

    :param percent_complete: [required] The completed percentage reported by
        the operation.
    :type percent_complete: int

    :param remaining_time: [required] The estimated time remaining in seconds.
    :type remaining_time: int

    :param src_volume_id: [required] The source volume ID.
    :type src_volume_id: int

    :param status: [required] Can be one of the following:

        **preparing**

        **active**

        **done**

        **failed**

    :type status: str

    :param script: [required] The name of the script if one is provided.
    :type script: str

    :param snapshot_id: [required] ID of the snapshot if a snapshot is in the
        source of the bulk volume job.
    :type snapshot_id: int

    :param type: [required] Can be one of the following:

        **read**

        **write**

    :type type: str

    :param attributes: [required] JSON attributes on the bulk volume job.
    :type attributes: dict
    """

    bulk_volume_id = data_model.property(
        "bulkVolumeID", int,
        array=False, optional=False,
        documentation="\
        The internal bulk volume job ID.\
        "
    )

    create_time = data_model.property(
        "createTime", str,
        array=False, optional=False,
        documentation="\
        Timestamp created for the bulk volume job.\
        "
    )

    elapsed_time = data_model.property(
        "elapsedTime", int,
        array=False, optional=False,
        documentation="\
        The number of seconds since the job began.\
        "
    )

    format = data_model.property(
        "format", str,
        array=False, optional=False,
        documentation="\
        Format is either \"compressed\" or \"native\".\
        "
    )

    key = data_model.property(
        "key", str,
        array=False, optional=False,
        documentation="\
        The unique key created by the bulk volume session.\
        "
    )

    percent_complete = data_model.property(
        "percentComplete", int,
        array=False, optional=False,
        documentation="\
        The completed percentage reported by the operation.\
        "
    )

    remaining_time = data_model.property(
        "remainingTime", int,
        array=False, optional=False,
        documentation="\
        The estimated time remaining in seconds.\
        "
    )

    src_volume_id = data_model.property(
        "srcVolumeID", int,
        array=False, optional=False,
        documentation="\
        The source volume ID.\
        "
    )

    status = data_model.property(
        "status", str,
        array=False, optional=False,
        documentation="\
        Can be one of the following:\
\
\
            **preparing**\
\
\
\
            **active**\
\
\
\
            **done**\
\
\
\
            **failed**\
\
        "
    )

    script = data_model.property(
        "script", str,
        array=False, optional=False,
        documentation="\
        The name of the script if one is provided.\
        "
    )

    snapshot_id = data_model.property(
        "snapshotID", int,
        array=False, optional=False,
        documentation="\
        ID of the snapshot if a snapshot is in the source of the bulk volume\
        job.\
        "
    )

    type = data_model.property(
        "type", str,
        array=False, optional=False,
        documentation="\
        Can be one of the following:\
\
\
            **read**\
\
\
\
            **write**\
\
        "
    )

    attributes = data_model.property(
        "attributes", dict,
        array=False, optional=False,
        documentation="\
        JSON attributes on the bulk volume job.\
        "
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class ClusterAdmin(data_model.DataObject):
    """

    :param access: [required]
    :type access: str[]

    :param cluster_admin_id: [required]
    :type cluster_admin_id: int

    :param username: [required]
    :type username: str

    :param attributes: [required] List of Name/Value pairs in JSON object
        format.
    :type attributes: dict
    """

    access = data_model.property(
        "access", str,
        array=True, optional=False,
        documentation=None
    )

    cluster_admin_id = data_model.property(
        "clusterAdminID", int,
        array=False, optional=False,
        documentation=None
    )

    username = data_model.property(
        "username", str,
        array=False, optional=False,
        documentation=None
    )

    attributes = data_model.property(
        "attributes", dict,
        array=False, optional=False,
        documentation="\
        List of Name/Value pairs in JSON object format.\
        "
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class ClusterVersionInfo(data_model.DataObject):
    """
    Version information for a node in the cluster.

    :param node_id: [required]
    :type node_id: int

    :param node_version: [required]
    :type node_version: str

    :param node_internal_revision: [required]
    :type node_internal_revision: str
    """

    node_id = data_model.property(
        "nodeID", int,
        array=False, optional=False,
        documentation=None
    )

    node_version = data_model.property(
        "nodeVersion", str,
        array=False, optional=False,
        documentation=None
    )

    node_internal_revision = data_model.property(
        "nodeInternalRevision", str,
        array=False, optional=False,
        documentation=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class GroupCloneVolumeMember(data_model.DataObject):
    """
    Represents the relationship between the source Volume and cloned Volume
    IDs.

    :param volume_id: [required] The *volume_id* of the cloned volume.
    :type volume_id: int

    :param src_volume_id: [required] The *volume_id* of the source volume.
    :type src_volume_id: int
    """

    volume_id = data_model.property(
        "volumeID", int,
        array=False, optional=False,
        documentation="\
        The *volume_id* of the cloned volume.\
        "
    )

    src_volume_id = data_model.property(
        "srcVolumeID", int,
        array=False, optional=False,
        documentation="\
        The *volume_id* of the source volume.\
        "
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class LunAssignment(data_model.DataObject):
    """
    *volume_id* and Lun assignment.

    :param volume_id: [required] The volume ID assigned to the Lun.
    :type volume_id: int

    :param lun: [required] Correct LUN values are 0 - 16383. An exception will
        be seen if an incorrect LUN value is passed.
    :type lun: int
    """

    volume_id = data_model.property(
        "volumeID", int,
        array=False, optional=False,
        documentation="\
        The volume ID assigned to the Lun.\
        "
    )

    lun = data_model.property(
        "lun", int,
        array=False, optional=False,
        documentation="\
        Correct LUN values are 0 - 16383. An exception will be seen if an\
        incorrect LUN value is passed.\
        "
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class Network(data_model.DataObject):
    """

    :param bond10_g: (optional)
    :type bond10_g: NetworkConfig

    :param bond1_g: (optional)
    :type bond1_g: NetworkConfig
    """

    bond10_g = data_model.property(
        "Bond10G", NetworkConfig,
        array=False, optional=True,
        documentation=None
    )

    bond1_g = data_model.property(
        "Bond1G", NetworkConfig,
        array=False, optional=True,
        documentation=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class NodeStatsInfo(data_model.DataObject):
    """

    :param c_bytes_in: [required] Bytes in on the cluster interface.
    :type c_bytes_in: int

    :param c_bytes_out: [required] Bytes out on the cluster interface.
    :type c_bytes_out: int

    :param cpu: [required] CPU Usage %
    :type cpu: int

    :param m_bytes_in: [required] Bytes in on the management interface.
    :type m_bytes_in: int

    :param m_bytes_out: [required] Bytes out on the management interface.
    :type m_bytes_out: int

    :param network_utilization_cluster: [required] Network interface
        utilization (in %) for the cluster network interface.
    :type network_utilization_cluster: int

    :param network_utilization_storage: [required] Network interface
        utilization (in %) for the storage network interface.
    :type network_utilization_storage: int

    :param node_id: [required]
    :type node_id: int

    :param s_bytes_in: [required] Bytes in on the storage interface.
    :type s_bytes_in: int

    :param s_bytes_out: [required] Bytes out on the storage interface.
    :type s_bytes_out: int

    :param timestamp: [required] Current time in UTC format ISO 8691 date
        string.
    :type timestamp: str

    :param used_memory: [required] Total memory usage in bytes.
    :type used_memory: int
    """

    c_bytes_in = data_model.property(
        "cBytesIn", int,
        array=False, optional=False,
        documentation="\
        Bytes in on the cluster interface.\
        "
    )

    c_bytes_out = data_model.property(
        "cBytesOut", int,
        array=False, optional=False,
        documentation="\
        Bytes out on the cluster interface.\
        "
    )

    cpu = data_model.property(
        "cpu", int,
        array=False, optional=False,
        documentation="\
        CPU Usage %\
        "
    )

    m_bytes_in = data_model.property(
        "mBytesIn", int,
        array=False, optional=False,
        documentation="\
        Bytes in on the management interface.\
        "
    )

    m_bytes_out = data_model.property(
        "mBytesOut", int,
        array=False, optional=False,
        documentation="\
        Bytes out on the management interface.\
        "
    )

    network_utilization_cluster = data_model.property(
        "networkUtilizationCluster", int,
        array=False, optional=False,
        documentation="\
        Network interface utilization (in %) for the cluster network\
        interface.\
        "
    )

    network_utilization_storage = data_model.property(
        "networkUtilizationStorage", int,
        array=False, optional=False,
        documentation="\
        Network interface utilization (in %) for the storage network\
        interface.\
        "
    )

    node_id = data_model.property(
        "nodeID", int,
        array=False, optional=False,
        documentation=None
    )

    s_bytes_in = data_model.property(
        "sBytesIn", int,
        array=False, optional=False,
        documentation="\
        Bytes in on the storage interface.\
        "
    )

    s_bytes_out = data_model.property(
        "sBytesOut", int,
        array=False, optional=False,
        documentation="\
        Bytes out on the storage interface.\
        "
    )

    timestamp = data_model.property(
        "timestamp", str,
        array=False, optional=False,
        documentation="\
        Current time in UTC format ISO 8691 date string.\
        "
    )

    used_memory = data_model.property(
        "usedMemory", int,
        array=False, optional=False,
        documentation="\
        Total memory usage in bytes.\
        "
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class TestConnectMvipDetails(data_model.DataObject):
    """

    :param ping_bytes: [required] Details of the ping tests with 56 Bytes and
        1500 Bytes.
    :type ping_bytes: str

    :param mvip: [required] The MVIP tested against.
    :type mvip: str

    :param connected: [required] Whether the test could connect to the MVIP.
    :type connected: bool
    """

    ping_bytes = data_model.property(
        "pingBytes", str,
        array=False, optional=False,
        documentation="\
        Details of the ping tests with 56 Bytes and 1500 Bytes.\
        "
    )

    mvip = data_model.property(
        "mvip", str,
        array=False, optional=False,
        documentation="\
        The MVIP tested against.\
        "
    )

    connected = data_model.property(
        "connected", bool,
        array=False, optional=False,
        documentation="\
        Whether the test could connect to the MVIP.\
        "
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class TestConnectSvipDetails(data_model.DataObject):
    """

    :param ping_bytes: [required] Details of the ping tests with 56 Bytes and
        1500 Bytes.
    :type ping_bytes: str

    :param svip: [required] The SVIP tested against.
    :type svip: str

    :param connected: [required] Whether the test could connect to the MVIP.
    :type connected: bool
    """

    ping_bytes = data_model.property(
        "pingBytes", str,
        array=False, optional=False,
        documentation="\
        Details of the ping tests with 56 Bytes and 1500 Bytes.\
        "
    )

    svip = data_model.property(
        "svip", str,
        array=False, optional=False,
        documentation="\
        The SVIP tested against.\
        "
    )

    connected = data_model.property(
        "connected", bool,
        array=False, optional=False,
        documentation="\
        Whether the test could connect to the MVIP.\
        "
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class CloneMultipleVolumeParams(data_model.DataObject):
    """

    :param volume_id: [required] Required parameter for \"volumes\" array:
        volumeID.
    :type volume_id: int

    :param access: (optional) Access settings for the new volume.

        **readOnly**: Only read operations are allowed.

        **readWrite**: Reads and writes are allowed.

        **locked**: No reads or writes are allowed.

        **replicationTarget**: Identify a volume as the target volume for a
        paired set of volumes. If the volume is not paired, the access status
        is locked.

        If unspecified, the access settings of the clone will be the same as
        the source.

    :type access: str

    :param name: (optional) New name for the clone.
    :type name: str

    :param new_account_id: (optional) Account ID for the new volume.
    :type new_account_id: int

    :param new_size: (optional) New size Total size of the volume, in bytes.
        Size is rounded up to the nearest 1MB size.
    :type new_size: int

    :param attributes: (optional) List of Name/Value pairs in JSON object
        format.
    :type attributes: dict
    """

    volume_id = data_model.property(
        "volumeID", int,
        array=False, optional=False,
        documentation="\
        Required parameter for \"volumes\" array: volumeID.\
        "
    )

    access = data_model.property(
        "access", str,
        array=False, optional=True,
        documentation="\
        Access settings for the new volume.\
\
\
            **readOnly**: Only read operations are allowed.\
\
\
\
            **readWrite**: Reads and writes are allowed.\
\
\
\
            **locked**: No reads or writes are allowed.\
\
\
\
            **replicationTarget**: Identify a volume as the target volume for\
        a paired set of volumes. If the volume is not paired, the access\
        status is locked.\
\
\
\
\
\
        If unspecified, the access settings of the clone will be the same as\
        the source.\
        "
    )

    name = data_model.property(
        "name", str,
        array=False, optional=True,
        documentation="\
        New name for the clone.\
        "
    )

    new_account_id = data_model.property(
        "newAccountID", int,
        array=False, optional=True,
        documentation="\
        Account ID for the new volume.\
        "
    )

    new_size = data_model.property(
        "newSize", int,
        array=False, optional=True,
        documentation="\
        New size Total size of the volume, in bytes. Size is rounded up to the\
        nearest 1MB size.\
        "
    )

    attributes = data_model.property(
        "attributes", dict,
        array=False, optional=True,
        documentation="\
        List of Name/Value pairs in JSON object format.\
        "
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class DriveInfo(data_model.DataObject):
    """

    :param capacity: [required] Total capacity of the drive, in bytes.
    :type capacity: int

    :param drive_id: [required] *drive_id* for this drive.
    :type drive_id: int

    :param node_id: [required] *node_id* where this drive is located.
    :type node_id: int

    :param serial: [required] Drive serial number.
    :type serial: str

    :param slot: [required] Slot number in the server chassis where this drive
        is located, or -1 if *satadimm* used for internal metadata drive.
    :type slot: int

    :param status: [required]
    :type status: str

    :param type: [required]
    :type type: str

    :param attributes: [required] List of Name/Value pairs in JSON object
        format.
    :type attributes: dict
    """

    capacity = data_model.property(
        "capacity", int,
        array=False, optional=False,
        documentation="\
        Total capacity of the drive, in bytes.\
        "
    )

    drive_id = data_model.property(
        "driveID", int,
        array=False, optional=False,
        documentation="\
        *drive_id* for this drive.\
        "
    )

    node_id = data_model.property(
        "nodeID", int,
        array=False, optional=False,
        documentation="\
        *node_id* where this drive is located.\
        "
    )

    serial = data_model.property(
        "serial", str,
        array=False, optional=False,
        documentation="\
        Drive serial number.\
        "
    )

    slot = data_model.property(
        "slot", int,
        array=False, optional=False,
        documentation="\
        Slot number in the server chassis where this drive is located, or -1\
        if *satadimm* used for internal metadata drive.\
        "
    )

    status = data_model.property(
        "status", str,
        array=False, optional=False,
        documentation=None
    )

    type = data_model.property(
        "type", str,
        array=False, optional=False,
        documentation=None
    )

    attributes = data_model.property(
        "attributes", dict,
        array=False, optional=False,
        documentation="\
        List of Name/Value pairs in JSON object format.\
        "
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class FibreChannelSession(data_model.DataObject):
    """
    *fibre_channel_session* contains information about each Fibre Channel
    session that is visible to the cluster and what target ports it is visible
    on.

    :param initiator_wwpn: [required] The WWPN of the initiator which is logged
        into the target port.
    :type initiator_wwpn: str

    :param node_id: [required] The node owning the Fibre Channel session.
    :type node_id: int

    :param service_id: [required] The service ID of the *fservice* owning this
        Fibre Channel session
    :type service_id: int

    :param target_wwpn: [required] The WWPN of the target port involved in this
        session.
    :type target_wwpn: str

    :param volume_access_group_id: [required] The ID of the volume access group
        to which the *initiator_wwpn* belongs. If not in a volume access group,
        the value will be null.
    :type volume_access_group_id: int
    """

    initiator_wwpn = data_model.property(
        "initiatorWWPN", str,
        array=False, optional=False,
        documentation="\
        The WWPN of the initiator which is logged into the target port.\
        "
    )

    node_id = data_model.property(
        "nodeID", int,
        array=False, optional=False,
        documentation="\
        The node owning the Fibre Channel session.\
        "
    )

    service_id = data_model.property(
        "serviceID", int,
        array=False, optional=False,
        documentation="\
        The service ID of the *fservice* owning this Fibre Channel session\
        "
    )

    target_wwpn = data_model.property(
        "targetWWPN", str,
        array=False, optional=False,
        documentation="\
        The WWPN of the target port involved in this session.\
        "
    )

    volume_access_group_id = data_model.property(
        "volumeAccessGroupID", int,
        array=False, optional=False,
        documentation="\
        The ID of the volume access group to which the *initiator_wwpn*\
        belongs. If not in a volume access group, the value will be null.\
        "
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class GroupSnapshotMembers(data_model.DataObject):
    """
    List of checksum, *volume_ids* and *snapshot_ids* for each member of the
    group.

    :param volume_id: [required] The source volume ID for the snapshot.
    :type volume_id: int

    :param snapshot_id: [required] Unique ID of a snapshot from which the new
        snapshot is made. The *snapshot_id* passed must be a snapshot on the
        given volume.
    :type snapshot_id: int

    :param snapshot_uuid: [required] Universal Unique ID of an existing
        snapshot.
    :type snapshot_uuid: str

    :param checksum: [required] A string that represents the correct digits in
        the stored snapshot. This checksum can be used later to compare other
        snapshots to detect errors in the data.
    :type checksum: str
    """

    volume_id = data_model.property(
        "volumeID", int,
        array=False, optional=False,
        documentation="\
        The source volume ID for the snapshot.\
        "
    )

    snapshot_id = data_model.property(
        "snapshotID", int,
        array=False, optional=False,
        documentation="\
        Unique ID of a snapshot from which the new snapshot is made.\
        The *snapshot_id* passed must be a snapshot on the given volume.\
        "
    )

    snapshot_uuid = data_model.property(
        "SnapshotUUID", str,
        array=False, optional=False,
        documentation="\
        Universal Unique ID of an existing snapshot.\
        "
    )

    checksum = data_model.property(
        "checksum", str,
        array=False, optional=False,
        documentation="\
        A string that represents the correct digits in the stored snapshot.\
        This checksum can be used later to compare other snapshots to detect\
        errors in the data.\
        "
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class GroupSnapshot(data_model.DataObject):
    """
    Group Snapshot object represents a point-in-time copy of a group of
    volumes.

    :param group_snapshot_id: [required] Unique ID of the new group snapshot.
    :type group_snapshot_id: int

    :param group_snapshot_uuid: [required] UUID of the group snapshot.
    :type group_snapshot_uuid: UUID

    :param members: [required] List of *volume_ids* and *snapshot_ids* for each
        member of the group.
    :type members: GroupSnapshotMembers[]

    :param name: [required] Name of the group snapshot, or, if none was given,
        the UTC formatted day and time on which the snapshot was created.
    :type name: str

    :param create_time: [required] The UTC formatted day and time on which the
        snapshot was created.
    :type create_time: str

    :param status: [required] Status of the snapshot. Possible values:

        **Preparing**: A snapshot that is being prepared for use and is not yet
        writable.

        **Done**: A snapshot that has finished being prepared and is now usable

    :type status: str

    :param attributes: [required] List of Name/Value pairs in JSON object
        format.
    :type attributes: dict
    """

    group_snapshot_id = data_model.property(
        "groupSnapshotID", int,
        array=False, optional=False,
        documentation="\
        Unique ID of the new group snapshot.\
        "
    )

    group_snapshot_uuid = data_model.property(
        "groupSnapshotUUID", UUID,
        array=False, optional=False,
        documentation="\
        UUID of the group snapshot.\
        "
    )

    members = data_model.property(
        "members", GroupSnapshotMembers,
        array=True, optional=False,
        documentation="\
        List of *volume_ids* and *snapshot_ids* for each member of the group.\
        "
    )

    name = data_model.property(
        "name", str,
        array=False, optional=False,
        documentation="\
        Name of the group snapshot, or, if none was given, the UTC formatted\
        day and time on which the snapshot was created.\
        "
    )

    create_time = data_model.property(
        "createTime", str,
        array=False, optional=False,
        documentation="\
        The UTC formatted day and time on which the snapshot was created.\
        "
    )

    status = data_model.property(
        "status", str,
        array=False, optional=False,
        documentation="\
        Status of the snapshot.\
        Possible values:\
\
\
            **Preparing**: A snapshot that is being prepared for use and is\
        not yet writable.\
\
\
\
            **Done**: A snapshot that has finished being prepared and is now\
        usable\
\
        "
    )

    attributes = data_model.property(
        "attributes", dict,
        array=False, optional=False,
        documentation="\
        List of Name/Value pairs in JSON object format.\
        "
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class MetadataHosts(data_model.DataObject):
    """
    The volume services on which the volume metadata resides.

    :param dead_secondaries: [required] Secondary metadata (slice) services
        that are in a dead state.
    :type dead_secondaries: int[]

    :param live_secondaries: [required] Secondary metadata (slice) services
        that are currently in a \"live\" state.
    :type live_secondaries: int[]

    :param primary: [required] The primary metadata (slice) services hosting
        the volume.
    :type primary: int
    """

    dead_secondaries = data_model.property(
        "deadSecondaries", int,
        array=True, optional=False,
        documentation="\
        Secondary metadata (slice) services that are in a dead state.\
        "
    )

    live_secondaries = data_model.property(
        "liveSecondaries", int,
        array=True, optional=False,
        documentation="\
        Secondary metadata (slice) services that are currently in a \"live\"\
        state.\
        "
    )

    primary = data_model.property(
        "primary", int,
        array=False, optional=False,
        documentation="\
        The primary metadata (slice) services hosting the volume.\
        "
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class VolumePair(data_model.DataObject):
    """
    The Volume Pair Info is an object containing information about a volume
    that is paired on a remote cluster.
    If the volume is not paired, this object is null.

    :param cluster_pair_id: [required] The remote cluster a volume is paired
        with.
    :type cluster_pair_id: int

    :param remote_volume_id: [required] The *volume_id* on the remote cluster a
        volume is paired with.
    :type remote_volume_id: int

    :param remote_slice_id: [required] The *slice_id* on the remote cluster a
        volume is paired with.
    :type remote_slice_id: int

    :param remote_volume_name: [required] The last-observed name of the volume
        on the remote cluster a volume is paired with.
    :type remote_volume_name: str

    :param volume_pair_uuid: [required] A UUID in canonical form.
    :type volume_pair_uuid: UUID

    :param remote_replication: [required] Details about the replication
        configuration for this volume pair.
    :type remote_replication: RemoteReplication
    """

    cluster_pair_id = data_model.property(
        "clusterPairID", int,
        array=False, optional=False,
        documentation="\
        The remote cluster a volume is paired with.\
        "
    )

    remote_volume_id = data_model.property(
        "remoteVolumeID", int,
        array=False, optional=False,
        documentation="\
        The *volume_id* on the remote cluster a volume is paired with.\
        "
    )

    remote_slice_id = data_model.property(
        "remoteSliceID", int,
        array=False, optional=False,
        documentation="\
        The *slice_id* on the remote cluster a volume is paired with.\
        "
    )

    remote_volume_name = data_model.property(
        "remoteVolumeName", str,
        array=False, optional=False,
        documentation="\
        The last-observed name of the volume on the remote cluster a volume is\
        paired with.\
        "
    )

    volume_pair_uuid = data_model.property(
        "volumePairUUID", UUID,
        array=False, optional=False,
        documentation="\
        A UUID in canonical form.\
        "
    )

    remote_replication = data_model.property(
        "remoteReplication", RemoteReplication,
        array=False, optional=False,
        documentation="\
        Details about the replication configuration for this volume pair.\
        "
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class SoftwareVersionInfo(data_model.DataObject):
    """

    :param current_version: [required]
    :type current_version: str

    :param node_id: [required]
    :type node_id: int

    :param package_name: [required]
    :type package_name: str

    :param pending_version: [required]
    :type pending_version: str

    :param start_time: [required]
    :type start_time: str
    """

    current_version = data_model.property(
        "currentVersion", str,
        array=False, optional=False,
        documentation=None
    )

    node_id = data_model.property(
        "nodeID", int,
        array=False, optional=False,
        documentation=None
    )

    package_name = data_model.property(
        "packageName", str,
        array=False, optional=False,
        documentation=None
    )

    pending_version = data_model.property(
        "pendingVersion", str,
        array=False, optional=False,
        documentation=None
    )

    start_time = data_model.property(
        "startTime", str,
        array=False, optional=False,
        documentation=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class VolumeAccessGroup(data_model.DataObject):
    """
    A volume access group is a useful way of grouping volumes and initiators
    together for ease of management.




    Volume Access Group Limits:




    - A volume access group can contain up to sixty-four initiator IQNs.
    - An initiator can only belong to only one volume access group.
    - A volume access group can contain up to two thousand volumes.
    - Each volume access group can belong to a maximum of four other volume
      access groups.

    :param volume_access_group_id: [required] Unique ID for this volume access
        group.
    :type volume_access_group_id: int

    :param name: [required] Name of the volume access group.
    :type name: str

    :param initiators: [required] List of unique initiator names belonging to
        the volume access group.
    :type initiators: str[]

    :param volumes: [required] List of volumes belonging to the volume access
        group.
    :type volumes: int[]
    """

    volume_access_group_id = data_model.property(
        "volumeAccessGroupID", int,
        array=False, optional=False,
        documentation="\
        Unique ID for this volume access group.\
        "
    )

    name = data_model.property(
        "name", str,
        array=False, optional=False,
        documentation="\
        Name of the volume access group.\
        "
    )

    initiators = data_model.property(
        "initiators", str,
        array=True, optional=False,
        documentation="\
        List of unique initiator names belonging to the volume access group.\
        "
    )

    volumes = data_model.property(
        "volumes", int,
        array=True, optional=False,
        documentation="\
        List of volumes belonging to the volume access group.\
        "
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class VolumeAccessGroupLunAssignments(data_model.DataObject):
    """
    *volume_access_group* ID and Lun to be assigned to all volumes within it.

    :param volume_access_group_id: [required] Unique volume access group ID for
        which the LUN assignments will be modified.
    :type volume_access_group_id: int

    :param lun_assignments: [required] The volume *ids* with assigned LUN
        values.
    :type lun_assignments: LunAssignment[]

    :param deleted_lun_assignments: [required] The volume *ids* with deleted
        LUN values.
    :type deleted_lun_assignments: LunAssignment[]
    """

    volume_access_group_id = data_model.property(
        "volumeAccessGroupID", int,
        array=False, optional=False,
        documentation="\
        Unique volume access group ID for which the LUN assignments will be\
        modified.\
        "
    )

    lun_assignments = data_model.property(
        "lunAssignments", LunAssignment,
        array=True, optional=False,
        documentation="\
        The volume *ids* with assigned LUN values.\
        "
    )

    deleted_lun_assignments = data_model.property(
        "deletedLunAssignments", LunAssignment,
        array=True, optional=False,
        documentation="\
        The volume *ids* with deleted LUN values.\
        "
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class VirtualNetwork(data_model.DataObject):
    """

    :param virtual_network_id: [required] SolidFire unique identifier for a
        virtual network.
    :type virtual_network_id: int

    :param virtual_network_tag: [required] VLAN Tag identifier.
    :type virtual_network_tag: int

    :param address_blocks: [required] Range of address blocks currently
        assigned to the virtual network.

        **available:** Binary string in \"1\"s and \"0\"s. 1 equals the IP is
        available and 0 equals the IP is not available. The string is read from
        right to left with the digit to the far right being the first IP
        address in the list of addressBlocks.

        **size:** the size of this block of addresses.

        **start:** first IP address in the block.

    :type address_blocks: AddressBlock[]

    :param name: [required] The name assigned to the virtual network.
    :type name: str

    :param netmask: [required] IP address of the netmask for the virtual
        network.
    :type netmask: str

    :param svip: [required] Storage IP address for the virtual network.
    :type svip: str
    """

    virtual_network_id = data_model.property(
        "virtualNetworkID", int,
        array=False, optional=False,
        documentation="\
        SolidFire unique identifier for a virtual network.\
        "
    )

    virtual_network_tag = data_model.property(
        "virtualNetworkTag", int,
        array=False, optional=False,
        documentation="\
        VLAN Tag identifier.\
        "
    )

    address_blocks = data_model.property(
        "addressBlocks", AddressBlock,
        array=True, optional=False,
        documentation="\
        Range of address blocks currently assigned to the virtual network.\
\
\
            **available:** Binary string in \"1\"s and \"0\"s. 1 equals the IP\
        is available and 0 equals the IP is not available. The string is read\
        from right to left with the digit to the far right being the first IP\
        address in the list of addressBlocks.\
\
\
\
            **size:** the size of this block of addresses.\
\
\
\
            **start:** first IP address in the block.\
\
        "
    )

    attributes = data_model.property(
        "attributes", dict,
        array=False, optional=False,
        documentation="\
        List of Name/Value pairs in JSON object format.\
        "
    )

    name = data_model.property(
        "name", str,
        array=False, optional=False,
        documentation="\
        The name assigned to the virtual network.\
        "
    )

    netmask = data_model.property(
        "netmask", str,
        array=False, optional=False,
        documentation="\
        IP address of the netmask for the virtual network.\
        "
    )

    svip = data_model.property(
        "svip", str,
        array=False, optional=False,
        documentation="\
        Storage IP address for the virtual network.\
        "
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class Account(data_model.DataObject):
    """
    The object containing information about an account.
    This object only includes \"configured\" information about the account, not
    any runtime or usage information.

    :param account_id: [required] Unique *account_id* for the account.
    :type account_id: int

    :param username: [required] User name for the account.
    :type username: str

    :param status: [required] Current status of the account.
    :type status: str

    :param volumes: [required] List of *volume_ids* for Volumes owned by this
        account.
    :type volumes: int[]

    :param initiator_secret: (optional) CHAP secret to use for the initiator.
    :type initiator_secret: CHAPSecret

    :param target_secret: (optional) CHAP secret to use for the target (mutual
        CHAP authentication).
    :type target_secret: CHAPSecret

    :param attributes: (optional) List of Name/Value pairs in JSON object
        format.
    :type attributes: dict
    """

    account_id = data_model.property(
        "accountID", int,
        array=False, optional=False,
        documentation="\
        Unique *account_id* for the account.\
        "
    )

    username = data_model.property(
        "username", str,
        array=False, optional=False,
        documentation="\
        User name for the account.\
        "
    )

    status = data_model.property(
        "status", str,
        array=False, optional=False,
        documentation="\
        Current status of the account.\
        "
    )

    volumes = data_model.property(
        "volumes", int,
        array=True, optional=False,
        documentation="\
        List of *volume_ids* for Volumes owned by this account.\
        "
    )

    initiator_secret = data_model.property(
        "initiatorSecret", CHAPSecret,
        array=False, optional=True,
        documentation="\
        CHAP secret to use for the initiator.\
        "
    )

    target_secret = data_model.property(
        "targetSecret", CHAPSecret,
        array=False, optional=True,
        documentation="\
        CHAP secret to use for the target (mutual CHAP authentication).\
        "
    )

    attributes = data_model.property(
        "attributes", dict,
        array=False, optional=True,
        documentation="\
        List of Name/Value pairs in JSON object format.\
        "
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class EventInfo(data_model.DataObject):
    """

    :param event_id: [required]
    :type event_id: int

    :param severity: [required]
    :type severity: int

    :param event_info_type: [required]
    :type event_info_type: str

    :param message: [required]
    :type message: str

    :param service_id: [required]
    :type service_id: int

    :param node_id: [required]
    :type node_id: int

    :param drive_id: [required]
    :type drive_id: int

    :param time_of_report: [required]
    :type time_of_report: str

    :param time_of_publish: [required]
    :type time_of_publish: str

    :param details: [required]
    :type details: str
    """

    event_id = data_model.property(
        "eventID", int,
        array=False, optional=False,
        documentation=None
    )

    severity = data_model.property(
        "severity", int,
        array=False, optional=False,
        documentation=None
    )

    event_info_type = data_model.property(
        "eventInfoType", str,
        array=False, optional=False,
        documentation=None
    )

    message = data_model.property(
        "message", str,
        array=False, optional=False,
        documentation=None
    )

    service_id = data_model.property(
        "serviceID", int,
        array=False, optional=False,
        documentation=None
    )

    node_id = data_model.property(
        "nodeID", int,
        array=False, optional=False,
        documentation=None
    )

    drive_id = data_model.property(
        "driveID", int,
        array=False, optional=False,
        documentation=None
    )

    time_of_report = data_model.property(
        "timeOfReport", str,
        array=False, optional=False,
        documentation=None
    )

    time_of_publish = data_model.property(
        "timeOfPublish", str,
        array=False, optional=False,
        documentation=None
    )

    details = data_model.property(
        "details", str,
        array=False, optional=False,
        documentation=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class ClusterConfig(data_model.DataObject):
    """
    Cluster Config object returns information the node uses to communicate with
    the cluster.

    :param cipi: [required] Network interface used for cluster communication.
    :type cipi: str

    :param cluster: [required] Unique cluster name.
    :type cluster: str

    :param ensemble: [required] Nodes that are participating in the cluster.
    :type ensemble: str[]

    :param mipi: [required] Network interface used for node management.
    :type mipi: str

    :param name: [required] Unique cluster name.
    :type name: str

    :param role: [required] Identifies the role of the node
    :type role: str

    :param sipi: [required] Network interface used for storage.
    :type sipi: str

    :param state: [required]
    :type state: str

    :param node_id: (optional)
    :type node_id: int

    :param pending_node_id: (optional)
    :type pending_node_id: int
    """

    cipi = data_model.property(
        "cipi", str,
        array=False, optional=False,
        documentation="\
        Network interface used for cluster communication.\
        "
    )

    cluster = data_model.property(
        "cluster", str,
        array=False, optional=False,
        documentation="\
        Unique cluster name.\
        "
    )

    ensemble = data_model.property(
        "ensemble", str,
        array=True, optional=False,
        documentation="\
        Nodes that are participating in the cluster.\
        "
    )

    mipi = data_model.property(
        "mipi", str,
        array=False, optional=False,
        documentation="\
        Network interface used for node management.\
        "
    )

    name = data_model.property(
        "name", str,
        array=False, optional=False,
        documentation="\
        Unique cluster name.\
        "
    )

    node_id = data_model.property(
        "nodeID", int,
        array=False, optional=True,
        documentation=None
    )

    pending_node_id = data_model.property(
        "pendingNodeID", int,
        array=False, optional=True,
        documentation=None
    )

    role = data_model.property(
        "role", str,
        array=False, optional=False,
        documentation="\
        Identifies the role of the node\
        "
    )

    sipi = data_model.property(
        "sipi", str,
        array=False, optional=False,
        documentation="\
        Network interface used for storage.\
        "
    )

    state = data_model.property(
        "state", str,
        array=False, optional=False,
        documentation=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class ClusterInfo(data_model.DataObject):
    """
    Cluster Info object returns information the node uses to communicate with
    the cluster.

    :param attributes: [required] List of Name/Value pairs in JSON object
        format.
    :type attributes: dict

    :param encryption_at_rest_state: [required] Encryption at rest state.
    :type encryption_at_rest_state: str

    :param ensemble: [required] Array of Node IP addresses that are
        participating in the cluster.
    :type ensemble: str[]

    :param mvip: [required] Management network interface.
    :type mvip: str

    :param mvip_node_id: [required] Node holding the master MVIP address
    :type mvip_node_id: int

    :param name: [required] Unique cluster name.
    :type name: str

    :param rep_count: [required] Number of replicas of each piece of data to
        store in the cluster. Valid value is 2
    :type rep_count: int

    :param state: [required]
    :type state: str

    :param svip: [required] Storage virtual IP
    :type svip: str

    :param svip_node_id: [required] Node holding the master SVIP address.
    :type svip_node_id: int

    :param unique_id: [required] Unique ID for the cluster.
    :type unique_id: str

    :param uuid: [required]
    :type uuid: UUID
    """

    attributes = data_model.property(
        "attributes", dict,
        array=False, optional=False,
        documentation="\
        List of Name/Value pairs in JSON object format.\
        "
    )

    encryption_at_rest_state = data_model.property(
        "encryptionAtRestState", str,
        array=False, optional=False,
        documentation="\
        Encryption at rest state.\
        "
    )

    ensemble = data_model.property(
        "ensemble", str,
        array=True, optional=False,
        documentation="\
        Array of Node IP addresses that are participating in the cluster.\
        "
    )

    mvip = data_model.property(
        "mvip", str,
        array=False, optional=False,
        documentation="\
        Management network interface.\
        "
    )

    mvip_node_id = data_model.property(
        "mvipNodeID", int,
        array=False, optional=False,
        documentation="\
        Node holding the master MVIP address\
        "
    )

    name = data_model.property(
        "name", str,
        array=False, optional=False,
        documentation="\
        Unique cluster name.\
        "
    )

    rep_count = data_model.property(
        "repCount", int,
        array=False, optional=False,
        documentation="\
        Number of replicas of each piece of data to store in the cluster.\
        Valid value is 2\
        "
    )

    state = data_model.property(
        "state", str,
        array=False, optional=False,
        documentation=None
    )

    svip = data_model.property(
        "svip", str,
        array=False, optional=False,
        documentation="\
        Storage virtual IP\
        "
    )

    svip_node_id = data_model.property(
        "svipNodeID", int,
        array=False, optional=False,
        documentation="\
        Node holding the master SVIP address.\
        "
    )

    unique_id = data_model.property(
        "uniqueID", str,
        array=False, optional=False,
        documentation="\
        Unique ID for the cluster.\
        "
    )

    uuid = data_model.property(
        "uuid", UUID,
        array=False, optional=False,
        documentation=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class PendingNode(data_model.DataObject):
    """
    A \"pending node\" is one that has not yet joined the cluster.
    It can be added to a cluster using the *add_node* method.

    :param pending_node_id: [required]
    :type pending_node_id: int

    :param assigned_node_id: [required]
    :type assigned_node_id: int

    :param name: [required] The host name for this node.
    :type name: str

    :param compatible: [required]
    :type compatible: bool

    :param platform_info: [required] Information about the platform this node
        is.
    :type platform_info: Platform

    :param cip: [required] IP address used for both intra- and inter-cluster
        communication.
    :type cip: str

    :param cipi: [required] The machine&#39;s name for the \"cip\" interface.
    :type cipi: str

    :param mip: [required] IP address used for cluster management (hosting the
        API and web site).
    :type mip: str

    :param mipi: [required] The machine&#39;s name for the \"mip\" interface.
    :type mipi: str

    :param sip: [required] IP address used for iSCSI traffic.
    :type sip: str

    :param sipi: [required] The machine&#39;s name for the \"sip\" interface.
    :type sipi: str

    :param software_version: [required] The version of SolidFire software this
        node is currently running.
    :type software_version: str

    :param uuid: [required] UUID of node.
    :type uuid: UUID
    """

    pending_node_id = data_model.property(
        "pendingNodeID", int,
        array=False, optional=False,
        documentation=None
    )

    assigned_node_id = data_model.property(
        "AssignedNodeID", int,
        array=False, optional=False,
        documentation=None
    )

    name = data_model.property(
        "name", str,
        array=False, optional=False,
        documentation="\
        The host name for this node.\
        "
    )

    compatible = data_model.property(
        "compatible", bool,
        array=False, optional=False,
        documentation=None
    )

    platform_info = data_model.property(
        "platformInfo", Platform,
        array=False, optional=False,
        documentation="\
        Information about the platform this node is.\
        "
    )

    cip = data_model.property(
        "cip", str,
        array=False, optional=False,
        documentation="\
        IP address used for both intra- and inter-cluster communication.\
        "
    )

    cipi = data_model.property(
        "cipi", str,
        array=False, optional=False,
        documentation="\
        The machine&#39;s name for the \"cip\" interface.\
        "
    )

    mip = data_model.property(
        "mip", str,
        array=False, optional=False,
        documentation="\
        IP address used for cluster management (hosting the API and web site).\
        "
    )

    mipi = data_model.property(
        "mipi", str,
        array=False, optional=False,
        documentation="\
        The machine&#39;s name for the \"mip\" interface.\
        "
    )

    sip = data_model.property(
        "sip", str,
        array=False, optional=False,
        documentation="\
        IP address used for iSCSI traffic.\
        "
    )

    sipi = data_model.property(
        "sipi", str,
        array=False, optional=False,
        documentation="\
        The machine&#39;s name for the \"sip\" interface.\
        "
    )

    software_version = data_model.property(
        "softwareVersion", str,
        array=False, optional=False,
        documentation="\
        The version of SolidFire software this node is currently running.\
        "
    )

    uuid = data_model.property(
        "uuid", UUID,
        array=False, optional=False,
        documentation="\
        UUID of node.\
        "
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class Snapshot(data_model.DataObject):
    """
    Snapshots is an object containing information about each snapshot made for
    a volume.
    The return object includes information for the active snapshot as well as
    each snapshot created for the volume.

    :param snapshot_id: [required] Unique ID for this snapshot.
    :type snapshot_id: int

    :param volume_id: [required] The volume this snapshot was taken of.
    :type volume_id: int

    :param name: [required] A name for this snapshot. It is not necessarily
        unique.
    :type name: str

    :param checksum: [required] A string that represents the correct digits in
        the stored snapshot. This checksum can be used later to compare other
        snapshots to detect errors in the data.
    :type checksum: str

    :param enable_remote_replication: [required] Identifies if snapshot is
        enabled for remote replication.
    :type enable_remote_replication: bool

    :param expiration_reason: [required] Indicates how the snapshot expiration
        was set. Possible values:

        **api**: expiration time was set by using the API.

        **none**: there is no expiration time set.

        **test**: expiration time was set for testing.

    :type expiration_reason: str

    :param expiration_time: [required] The time at which this snapshot will
        expire and be purged from the cluster.
    :type expiration_time: str

    :param remote_statuses: [required] Current remote status of the snapshot
        *remote_status:* Possible values:

        **Present**: Snapshot exists on a remote cluster

        **Not Present**: Snapshot does not exist on remote cluster

        **Syncing**: This is a target cluster and it is currently replicating
        the snapshot

        **Deleted**: This is a target cluster, the snapshot has been deleted,
        and it still exists on the source.

        **volumePairUUID**: universal identifier of the volume pair

    :type remote_statuses: str

    :param status: [required] Current status of the snapshot

        **Preparing**: A snapshot that is being prepared for use and is not yet
        writable.

        **Done**: A snapshot that has finished being prepared and is now
        usable.

        **Active**: This snapshot is the active branch.

    :type status: str

    :param snapshot_uuid: [required] Universal Unique ID of an existing
        snapshot.
    :type snapshot_uuid: UUID

    :param total_size: [required] Total size of this snapshot in bytes. It is
        equivalent to *total_size* of the volume when this snapshot was taken.
    :type total_size: int

    :param group_snapshot_uuid: [required] The current \"members\" results
        contains information about each snapshot in the group. Each of these
        members will have a \"uuid\" parameter for the snapshot&#39;s UUID.
    :type group_snapshot_uuid: UUID

    :param create_time: [required] The time this snapshot was taken.
    :type create_time: str

    :param attributes: [required] List of Name/Value pairs in JSON object
        format.
    :type attributes: dict

    :param group_id: (optional) If present, the ID of the group this snapshot
        is a part of. If not present, this snapshot is not part of a group.
    :type group_id: int
    """

    snapshot_id = data_model.property(
        "snapshotID", int,
        array=False, optional=False,
        documentation="\
        Unique ID for this snapshot.\
        "
    )

    volume_id = data_model.property(
        "volumeID", int,
        array=False, optional=False,
        documentation="\
        The volume this snapshot was taken of.\
        "
    )

    name = data_model.property(
        "name", str,
        array=False, optional=False,
        documentation="\
        A name for this snapshot.\
        It is not necessarily unique.\
        "
    )

    checksum = data_model.property(
        "checksum", str,
        array=False, optional=False,
        documentation="\
        A string that represents the correct digits in the stored snapshot.\
        This checksum can be used later to compare other snapshots to detect\
        errors in the data.\
        "
    )

    enable_remote_replication = data_model.property(
        "enableRemoteReplication", bool,
        array=False, optional=False,
        documentation="\
        Identifies if snapshot is enabled for remote replication.\
        "
    )

    expiration_reason = data_model.property(
        "expirationReason", str,
        array=False, optional=False,
        documentation="\
        Indicates how the snapshot expiration was set. Possible values:\
\
\
            **api**: expiration time was set by using the API.\
\
\
\
            **none**: there is no expiration time set.\
\
\
\
            **test**: expiration time was set for testing.\
\
        "
    )

    expiration_time = data_model.property(
        "expirationTime", str,
        array=False, optional=False,
        documentation="\
        The time at which this snapshot will expire and be purged from the\
        cluster.\
        "
    )

    remote_statuses = data_model.property(
        "remoteStatuses", str,
        array=False, optional=False,
        documentation="\
        Current remote status of the snapshot *remote_status:* Possible\
        values:\
\
\
            **Present**: Snapshot exists on a remote cluster\
\
\
\
            **Not Present**: Snapshot does not exist on remote cluster\
\
\
\
            **Syncing**: This is a target cluster and it is currently\
        replicating the snapshot\
\
\
\
            **Deleted**: This is a target cluster, the snapshot has been\
        deleted, and it still exists on the source.\
\
\
\
            **volumePairUUID**: universal identifier of the volume pair\
\
        "
    )

    status = data_model.property(
        "status", str,
        array=False, optional=False,
        documentation="\
        Current status of the snapshot\
\
\
            **Preparing**: A snapshot that is being prepared for use and is\
        not yet writable.\
\
\
\
            **Done**: A snapshot that has finished being prepared and is now\
        usable.\
\
\
\
            **Active**: This snapshot is the active branch.\
\
        "
    )

    snapshot_uuid = data_model.property(
        "SnapshotUUID", UUID,
        array=False, optional=False,
        documentation="\
        Universal Unique ID of an existing snapshot.\
        "
    )

    total_size = data_model.property(
        "totalSize", int,
        array=False, optional=False,
        documentation="\
        Total size of this snapshot in bytes.\
        It is equivalent to *total_size* of the volume when this snapshot was\
        taken.\
        "
    )

    group_id = data_model.property(
        "groupID", int,
        array=False, optional=True,
        documentation="\
        If present, the ID of the group this snapshot is a part of.\
        If not present, this snapshot is not part of a group.\
        "
    )

    group_snapshot_uuid = data_model.property(
        "groupSnapshotUUID", UUID,
        array=False, optional=False,
        documentation="\
        The current \"members\" results contains information about each\
        snapshot in the group.\
        Each of these members will have a \"uuid\" parameter for the\
        snapshot&#39;s UUID.\
        "
    )

    create_time = data_model.property(
        "createTime", str,
        array=False, optional=False,
        documentation="\
        The time this snapshot was taken.\
        "
    )

    attributes = data_model.property(
        "attributes", dict,
        array=False, optional=False,
        documentation="\
        List of Name/Value pairs in JSON object format.\
        "
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class VolumeStats(data_model.DataObject):
    """
    Contains statistical data for an individual volume.

    :param account_id: [required] *account_id* of the volume owner.
    :type account_id: int

    :param actual_iops: [required] Current actual IOPS to the volume in the
        last 500 milliseconds.
    :type actual_iops: int

    :param average_iopsize: [required] Average size in bytes of recent I/O to
        the volume in the last 500 milliseconds.
    :type average_iopsize: int

    :param burst_iopscredit: [required] The total number of IOP credits
        available to the user. When users are not using up to the max IOPS,
        credits are accrued.
    :type burst_iopscredit: int

    :param client_queue_depth: [required] The number of outstanding read and
        write operations to the cluster.
    :type client_queue_depth: int

    :param desired_metadata_hosts: [required] The volume services being
        migrated to if the volume metadata is getting migrated between volume
        services. A \"null\" value means the volume is not migrating.
    :type desired_metadata_hosts: MetadataHosts

    :param latency_usec: [required] The observed latency time, in microseconds,
        to complete operations to a volume.

        A \"0\" (zero) value means there is no I/O to the volume.

    :type latency_usec: int

    :param metadata_hosts: [required] The volume services on which the volume
        metadata resides.
    :type metadata_hosts: MetadataHosts

    :param non_zero_blocks: [required] The number of 4KiB blocks with data
        after the last garbage collection operation has completed.
    :type non_zero_blocks: int

    :param read_bytes: [required] Total bytes read by clients.
    :type read_bytes: int

    :param read_latency_usec: [required] The average time, in microseconds, to
        complete read operations.
    :type read_latency_usec: int

    :param read_ops: [required] Total read operations.
    :type read_ops: int

    :param throttle: [required] A floating value between 0 and 1 that
        represents how much the system is throttling clients below their max
        IOPS because of re-replication of data, transient errors and snapshots
        taken.
    :type throttle: float

    :param timestamp: [required] The current time in UTC.
    :type timestamp: str

    :param total_latency_usec: [required] The average time, in microseconds, to
        complete read and write operations to a volume.
    :type total_latency_usec: int

    :param unaligned_reads: [required] For 512e volumes, the number of read
        operations that were not on a 4k sector boundary. High numbers of
        unaligned reads may indicate improper partition alignment.
    :type unaligned_reads: int

    :param unaligned_writes: [required] For 512e volumes, the number of write
        operations that were not on a 4k sector boundary. High numbers of
        unaligned writes may indicate improper partition alignment.
    :type unaligned_writes: int

    :param volume_access_groups: [required] List of volume access group(s) to
        which a volume belongs.
    :type volume_access_groups: int[]

    :param volume_id: [required] Volume ID of the volume.
    :type volume_id: int

    :param volume_size: [required] Total provisioned capacity in bytes.
    :type volume_size: int

    :param volume_utilization: [required] A floating value that describes how
        much the client is using the volume.

        Values:

        0 = Client is not using the volume

        1 = Client is using their max

        >1 = Client is using their burst

    :type volume_utilization: float

    :param write_bytes: [required] Total bytes written by clients.
    :type write_bytes: int

    :param write_latency_usec: [required] The average time, in microseconds, to
        complete write operations.
    :type write_latency_usec: int

    :param write_ops: [required] Total write operations occurring on the
        volume.
    :type write_ops: int

    :param zero_blocks: [required] Total number of 4KiB blocks without data
        after the last round of garbage collection operation has completed.
    :type zero_blocks: int

    :param async_delay: (optional) The length of time since the volume was last
        synced with the remote cluster. If the volume is not paired, this is
        null.



        **Note**: A target volume in an active replication state always has an
        async delay of 0 (zero).

        Target volumes are system-aware during replication and assume async
        delay is accurate at all times.

    :type async_delay: str
    """

    account_id = data_model.property(
        "accountID", int,
        array=False, optional=False,
        documentation="\
        *account_id* of the volume owner.\
        "
    )

    actual_iops = data_model.property(
        "actualIOPS", int,
        array=False, optional=False,
        documentation="\
        Current actual IOPS to the volume in the last 500 milliseconds.\
        "
    )

    async_delay = data_model.property(
        "asyncDelay", str,
        array=False, optional=True,
        documentation="\
        The length of time since the volume was last synced with the remote\
        cluster.\
        If the volume is not paired, this is null.\
\
\
\
\
\
\
            **Note**: A target volume in an active replication state always\
        has an async delay of 0 (zero).\
\
\
\
            Target volumes are system-aware during replication and assume\
        async delay is accurate at all times.\
\
        "
    )

    average_iopsize = data_model.property(
        "averageIOPSize", int,
        array=False, optional=False,
        documentation="\
        Average size in bytes of recent I/O to the volume in the last 500\
        milliseconds.\
        "
    )

    burst_iopscredit = data_model.property(
        "burstIOPSCredit", int,
        array=False, optional=False,
        documentation="\
        The total number of IOP credits available to the user.\
        When users are not using up to the max IOPS, credits are accrued.\
        "
    )

    client_queue_depth = data_model.property(
        "clientQueueDepth", int,
        array=False, optional=False,
        documentation="\
        The number of outstanding read and write operations to the cluster.\
        "
    )

    desired_metadata_hosts = data_model.property(
        "desiredMetadataHosts", MetadataHosts,
        array=False, optional=False,
        documentation="\
        The volume services being migrated to if the volume metadata is\
        getting migrated between volume services.\
        A \"null\" value means the volume is not migrating.\
        "
    )

    latency_usec = data_model.property(
        "latencyUSec", int,
        array=False, optional=False,
        documentation="\
        The observed latency time, in microseconds, to complete operations to\
        a volume.\
\
\
\
        A \"0\" (zero) value means there is no I/O to the volume.\
        "
    )

    metadata_hosts = data_model.property(
        "metadataHosts", MetadataHosts,
        array=False, optional=False,
        documentation="\
        The volume services on which the volume metadata resides.\
        "
    )

    non_zero_blocks = data_model.property(
        "nonZeroBlocks", int,
        array=False, optional=False,
        documentation="\
        The number of 4KiB blocks with data after the last garbage collection\
        operation has completed.\
        "
    )

    read_bytes = data_model.property(
        "readBytes", int,
        array=False, optional=False,
        documentation="\
        Total bytes read by clients.\
        "
    )

    read_latency_usec = data_model.property(
        "readLatencyUSec", int,
        array=False, optional=False,
        documentation="\
        The average time, in microseconds, to complete read operations.\
        "
    )

    read_ops = data_model.property(
        "readOps", int,
        array=False, optional=False,
        documentation="\
        Total read operations.\
        "
    )

    throttle = data_model.property(
        "throttle", float,
        array=False, optional=False,
        documentation="\
        A floating value between 0 and 1 that represents how much the system\
        is throttling clients\
        below their max IOPS because of re-replication of data, transient\
        errors and snapshots taken.\
        "
    )

    timestamp = data_model.property(
        "timestamp", str,
        array=False, optional=False,
        documentation="\
        The current time in UTC.\
        "
    )

    total_latency_usec = data_model.property(
        "totalLatencyUSec", int,
        array=False, optional=False,
        documentation="\
        The average time, in microseconds, to complete read and write\
        operations to a volume.\
        "
    )

    unaligned_reads = data_model.property(
        "unalignedReads", int,
        array=False, optional=False,
        documentation="\
        For 512e volumes, the number of read operations that were not on a 4k\
        sector boundary.\
        High numbers of unaligned reads may indicate improper partition\
        alignment.\
        "
    )

    unaligned_writes = data_model.property(
        "unalignedWrites", int,
        array=False, optional=False,
        documentation="\
        For 512e volumes, the number of write operations that were not on a 4k\
        sector boundary.\
        High numbers of unaligned writes may indicate improper partition\
        alignment.\
        "
    )

    volume_access_groups = data_model.property(
        "volumeAccessGroups", int,
        array=True, optional=False,
        documentation="\
        List of volume access group(s) to which a volume belongs.\
        "
    )

    volume_id = data_model.property(
        "volumeID", int,
        array=False, optional=False,
        documentation="\
        Volume ID of the volume.\
        "
    )

    volume_size = data_model.property(
        "volumeSize", int,
        array=False, optional=False,
        documentation="\
        Total provisioned capacity in bytes.\
        "
    )

    volume_utilization = data_model.property(
        "volumeUtilization", float,
        array=False, optional=False,
        documentation="\
        A floating value that describes how much the client is using the\
        volume.\
\
\
\
\
        Values:\
\
\
\
        0 = Client is not using the volume\
\
\
\
        1 = Client is using their max\
\
\
\
        >1 = Client is using their burst\
        "
    )

    write_bytes = data_model.property(
        "writeBytes", int,
        array=False, optional=False,
        documentation="\
        Total bytes written by clients.\
        "
    )

    write_latency_usec = data_model.property(
        "writeLatencyUSec", int,
        array=False, optional=False,
        documentation="\
        The average time, in microseconds, to complete write operations.\
        "
    )

    write_ops = data_model.property(
        "writeOps", int,
        array=False, optional=False,
        documentation="\
        Total write operations occurring on the volume.\
        "
    )

    zero_blocks = data_model.property(
        "zeroBlocks", int,
        array=False, optional=False,
        documentation="\
        Total number of 4KiB blocks without data after the last round of\
        garbage collection operation has completed.\
        "
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class ClusterFaultInfo(data_model.DataObject):
    """

    :param severity: [required]
    :type severity: str

    :param type: [required]
    :type type: str

    :param code: [required]
    :type code: str

    :param details: [required]
    :type details: str

    :param node_hardware_fault_id: [required]
    :type node_hardware_fault_id: int

    :param node_id: [required]
    :type node_id: int

    :param service_id: [required]
    :type service_id: int

    :param drive_id: [required]
    :type drive_id: int

    :param resolved: [required]
    :type resolved: bool

    :param cluster_fault_id: [required]
    :type cluster_fault_id: int

    :param date: [required]
    :type date: str

    :param resolved_date: [required]
    :type resolved_date: str

    :param data: [required]
    :type data: str
    """

    severity = data_model.property(
        "severity", str,
        array=False, optional=False,
        documentation=None
    )

    type = data_model.property(
        "type", str,
        array=False, optional=False,
        documentation=None
    )

    code = data_model.property(
        "code", str,
        array=False, optional=False,
        documentation=None
    )

    details = data_model.property(
        "details", str,
        array=False, optional=False,
        documentation=None
    )

    node_hardware_fault_id = data_model.property(
        "nodeHardwareFaultID", int,
        array=False, optional=False,
        documentation=None
    )

    node_id = data_model.property(
        "nodeID", int,
        array=False, optional=False,
        documentation=None
    )

    service_id = data_model.property(
        "serviceID", int,
        array=False, optional=False,
        documentation=None
    )

    drive_id = data_model.property(
        "driveID", int,
        array=False, optional=False,
        documentation=None
    )

    resolved = data_model.property(
        "resolved", bool,
        array=False, optional=False,
        documentation=None
    )

    cluster_fault_id = data_model.property(
        "clusterFaultID", int,
        array=False, optional=False,
        documentation=None
    )

    date = data_model.property(
        "date", str,
        array=False, optional=False,
        documentation=None
    )

    resolved_date = data_model.property(
        "resolvedDate", str,
        array=False, optional=False,
        documentation=None
    )

    data = data_model.property(
        "data", str,
        array=False, optional=False,
        documentation=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class ISCSISession(data_model.DataObject):
    """

    :param account_id: [required]
    :type account_id: int

    :param account_name: [required]
    :type account_name: str

    :param drive_id: [required]
    :type drive_id: int

    :param initiator_ip: [required]
    :type initiator_ip: str

    :param initiator_name: [required]
    :type initiator_name: str

    :param node_id: [required]
    :type node_id: int

    :param service_id: [required]
    :type service_id: int

    :param session_id: [required]
    :type session_id: int

    :param target_name: [required]
    :type target_name: str

    :param target_ip: [required]
    :type target_ip: str

    :param virtual_network_id: [required]
    :type virtual_network_id: str

    :param volume_id: [required]
    :type volume_id: int
    """

    account_id = data_model.property(
        "accountID", int,
        array=False, optional=False,
        documentation=None
    )

    account_name = data_model.property(
        "accountName", str,
        array=False, optional=False,
        documentation=None
    )

    drive_id = data_model.property(
        "driveID", int,
        array=False, optional=False,
        documentation=None
    )

    initiator_ip = data_model.property(
        "initiatorIP", str,
        array=False, optional=False,
        documentation=None
    )

    initiator_name = data_model.property(
        "initiatorName", str,
        array=False, optional=False,
        documentation=None
    )

    node_id = data_model.property(
        "nodeID", int,
        array=False, optional=False,
        documentation=None
    )

    service_id = data_model.property(
        "serviceID", int,
        array=False, optional=False,
        documentation=None
    )

    session_id = data_model.property(
        "sessionID", int,
        array=False, optional=False,
        documentation=None
    )

    target_name = data_model.property(
        "targetName", str,
        array=False, optional=False,
        documentation=None
    )

    target_ip = data_model.property(
        "targetIP", str,
        array=False, optional=False,
        documentation=None
    )

    virtual_network_id = data_model.property(
        "virtualNetworkID", str,
        array=False, optional=False,
        documentation=None
    )

    volume_id = data_model.property(
        "volumeID", int,
        array=False, optional=False,
        documentation=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class Node(data_model.DataObject):
    """
    A node refers to an individual machine in a cluster.
    Each active node hosts a master service, which is responsible for managing
    the drives and other services on its node.
    After a node is made active, its drives will become available for addition
    to the cluster.

    :param node_id: [required] The unique identifier for this node.
    :type node_id: int

    :param associated_master_service_id: [required] The master service
        responsible for controlling other services on this node.
    :type associated_master_service_id: int

    :param associated_fservice_id: [required]
    :type associated_fservice_id: int

    :param fibre_channel_target_port_group: [required]
    :type fibre_channel_target_port_group: str

    :param name: [required]
    :type name: str

    :param platform_info: [required] Information about the platform this node
        is.
    :type platform_info: Platform

    :param software_version: [required] The version of SolidFire software this
        node is currently running.
    :type software_version: str

    :param cip: [required] IP address used for both intra- and inter-cluster
        communication.
    :type cip: str

    :param cipi: [required] The machine&#39;s name for the \"cip\" interface.
    :type cipi: str

    :param mip: [required] IP address used for cluster management (hosting the
        API and web site).
    :type mip: str

    :param mipi: [required] The machine&#39;s name for the \"mip\" interface.
    :type mipi: str

    :param sip: [required] IP address used for iSCSI traffic.
    :type sip: str

    :param sipi: [required] The machine&#39;s name for the \"sip\" interface.
    :type sipi: str

    :param uuid: [required] UUID of node.
    :type uuid: UUID

    :param attributes: [required]
    :type attributes: dict
    """

    node_id = data_model.property(
        "nodeID", int,
        array=False, optional=False,
        documentation="\
        The unique identifier for this node.\
        "
    )

    associated_master_service_id = data_model.property(
        "associatedMasterServiceID", int,
        array=False, optional=False,
        documentation="\
        The master service responsible for controlling other services on this\
        node.\
        "
    )

    associated_fservice_id = data_model.property(
        "associatedFServiceID", int,
        array=False, optional=False,
        documentation=None
    )

    fibre_channel_target_port_group = data_model.property(
        "fibreChannelTargetPortGroup", str,
        array=False, optional=False,
        documentation=None
    )

    name = data_model.property(
        "name", str,
        array=False, optional=False,
        documentation=None
    )

    platform_info = data_model.property(
        "platformInfo", Platform,
        array=False, optional=False,
        documentation="\
        Information about the platform this node is.\
        "
    )

    software_version = data_model.property(
        "softwareVersion", str,
        array=False, optional=False,
        documentation="\
        The version of SolidFire software this node is currently running.\
        "
    )

    cip = data_model.property(
        "cip", str,
        array=False, optional=False,
        documentation="\
        IP address used for both intra- and inter-cluster communication.\
        "
    )

    cipi = data_model.property(
        "cipi", str,
        array=False, optional=False,
        documentation="\
        The machine&#39;s name for the \"cip\" interface.\
        "
    )

    mip = data_model.property(
        "mip", str,
        array=False, optional=False,
        documentation="\
        IP address used for cluster management (hosting the API and web site).\
        "
    )

    mipi = data_model.property(
        "mipi", str,
        array=False, optional=False,
        documentation="\
        The machine&#39;s name for the \"mip\" interface.\
        "
    )

    sip = data_model.property(
        "sip", str,
        array=False, optional=False,
        documentation="\
        IP address used for iSCSI traffic.\
        "
    )

    sipi = data_model.property(
        "sipi", str,
        array=False, optional=False,
        documentation="\
        The machine&#39;s name for the \"sip\" interface.\
        "
    )

    uuid = data_model.property(
        "uuid", UUID,
        array=False, optional=False,
        documentation="\
        UUID of node.\
        "
    )

    attributes = data_model.property(
        "attributes", dict,
        array=False, optional=False,
        documentation=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class Config(data_model.DataObject):
    """

    :param cluster: [required]
    :type cluster: ClusterConfig

    :param network: [required]
    :type network: Network
    """

    cluster = data_model.property(
        "cluster", ClusterConfig,
        array=False, optional=False,
        documentation=None
    )

    network = data_model.property(
        "network", Network,
        array=False, optional=False,
        documentation=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class Volume(data_model.DataObject):
    """
    Volumes Info is an object containing information about a volume.
    The return objects only include \"configured\" information about the volume
    and not runtime or usage information.
    Information about paired volumes will also be returned.

    :param volume_id: [required] Unique *volume_id* for the volume.
    :type volume_id: int

    :param name: [required] Name of the volume as provided at creation time.
    :type name: str

    :param account_id: [required] Unique *account_id* for the account.
    :type account_id: int

    :param create_time: [required] UTC formatted time the volume was created.
    :type create_time: str

    :param status: [required] Current status of the volume init: A volume that
        is being initialized and is not ready for connections. active: An
        active volume ready for connections.
    :type status: str

    :param access: [required] Access allowed for the volume

        **readOnly**: Only read operations are allowed.

        **readWrite**: Reads and writes are allowed.

        **locked**: No reads or writes are allowed.

        **replicationTarget**: Designated as a target volume in a replicated
        volume pair.

    :type access: str

    :param enable512e: [required] If \"true\", the volume provides 512 byte
        sector emulation.
    :type enable512e: bool

    :param iqn: [required] Volume iSCSI Qualified Name.
    :type iqn: str

    :param scsi_euidevice_id: [required] Globally unique SCSI device identifier
        for the volume in EUI-64 based 16-byte format.
    :type scsi_euidevice_id: str

    :param scsi_naadevice_id: [required] Globally unique SCSI device identifier
        for the volume in NAA IEEE Registered Extended format.
    :type scsi_naadevice_id: str

    :param qos: [required] Quality of service settings for this volume.
    :type qos: VolumeQOS

    :param volume_access_groups: [required] List of volume access groups to
        which a volume belongs.
    :type volume_access_groups: int[]

    :param volume_pairs: [required] Information about a paired volume.
        Available only if a volume is paired. @see *volume_pairs* for return
        values.
    :type volume_pairs: VolumePair[]

    :param slice_count: [required] The number of slices backing this volume. In
        the current software, this value will always be 1.
    :type slice_count: int

    :param total_size: [required] Total size of this volume in bytes.
    :type total_size: int

    :param block_size: [required] Size of the blocks on the volume.
    :type block_size: int

    :param virtual_volume_id: [required] Virtual volume ID this volume backs.
    :type virtual_volume_id: UUID

    :param attributes: [required] List of Name/Value pairs in JSON object
        format.
    :type attributes: dict

    :param delete_time: (optional) The time this volume was deleted. If this
        has no value, the volume has not yet been deleted.
    :type delete_time: str

    :param purge_time: (optional) The time this volume will be purged from the
        system. If this has no value, the volume has not yet been deleted (and
        is not scheduled for purging).
    :type purge_time: str
    """

    volume_id = data_model.property(
        "volumeID", int,
        array=False, optional=False,
        documentation="\
        Unique *volume_id* for the volume.\
        "
    )

    name = data_model.property(
        "name", str,
        array=False, optional=False,
        documentation="\
        Name of the volume as provided at creation time.\
        "
    )

    account_id = data_model.property(
        "accountID", int,
        array=False, optional=False,
        documentation="\
        Unique *account_id* for the account.\
        "
    )

    create_time = data_model.property(
        "createTime", str,
        array=False, optional=False,
        documentation="\
        UTC formatted time the volume was created.\
        "
    )

    status = data_model.property(
        "status", str,
        array=False, optional=False,
        documentation="\
        Current status of the volume\
        init: A volume that is being initialized and is not ready for\
        connections.\
        active: An active volume ready for connections.\
        "
    )

    access = data_model.property(
        "access", str,
        array=False, optional=False,
        documentation="\
        Access allowed for the volume\
\
\
            **readOnly**: Only read operations are allowed.\
\
\
\
            **readWrite**: Reads and writes are allowed.\
\
\
\
            **locked**: No reads or writes are allowed.\
\
\
\
            **replicationTarget**: Designated as a target volume in a\
        replicated volume pair.\
\
        "
    )

    enable512e = data_model.property(
        "enable512e", bool,
        array=False, optional=False,
        documentation="\
        If \"true\", the volume provides 512 byte sector emulation.\
        "
    )

    iqn = data_model.property(
        "iqn", str,
        array=False, optional=False,
        documentation="\
        Volume iSCSI Qualified Name.\
        "
    )

    scsi_euidevice_id = data_model.property(
        "scsiEUIDeviceID", str,
        array=False, optional=False,
        documentation="\
        Globally unique SCSI device identifier for the volume in EUI-64 based\
        16-byte format.\
        "
    )

    scsi_naadevice_id = data_model.property(
        "scsiNAADeviceID", str,
        array=False, optional=False,
        documentation="\
        Globally unique SCSI device identifier for the volume in NAA IEEE\
        Registered Extended format.\
        "
    )

    qos = data_model.property(
        "qos", VolumeQOS,
        array=False, optional=False,
        documentation="\
        Quality of service settings for this volume.\
        "
    )

    volume_access_groups = data_model.property(
        "volumeAccessGroups", int,
        array=True, optional=False,
        documentation="\
        List of volume access groups to which a volume belongs.\
        "
    )

    volume_pairs = data_model.property(
        "volumePairs", VolumePair,
        array=True, optional=False,
        documentation="\
        Information about a paired volume.\
        Available only if a volume is paired.\
        @see *volume_pairs* for return values.\
        "
    )

    delete_time = data_model.property(
        "deleteTime", str,
        array=False, optional=True,
        documentation="\
        The time this volume was deleted.\
        If this has no value, the volume has not yet been deleted.\
        "
    )

    purge_time = data_model.property(
        "purgeTime", str,
        array=False, optional=True,
        documentation="\
        The time this volume will be purged from the system.\
        If this has no value, the volume has not yet been deleted (and is not\
        scheduled for purging).\
        "
    )

    slice_count = data_model.property(
        "sliceCount", int,
        array=False, optional=False,
        documentation="\
        The number of slices backing this volume.\
        In the current software, this value will always be 1.\
        "
    )

    total_size = data_model.property(
        "totalSize", int,
        array=False, optional=False,
        documentation="\
        Total size of this volume in bytes.\
        "
    )

    block_size = data_model.property(
        "blockSize", int,
        array=False, optional=False,
        documentation="\
        Size of the blocks on the volume.\
        "
    )

    virtual_volume_id = data_model.property(
        "virtualVolumeID", UUID,
        array=False, optional=False,
        documentation="\
        Virtual volume ID this volume backs.\
        "
    )

    attributes = data_model.property(
        "attributes", dict,
        array=False, optional=False,
        documentation="\
        List of Name/Value pairs in JSON object format.\
        "
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)
