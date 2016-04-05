#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2014-2016 NetApp, Inc. All Rights Reserved.
#
# DO NOT EDIT THIS CODE BY HAND! It has been generated with jsvcgen.
#
from __future__ import unicode_literals
from __future__ import absolute_import
from solidfire.common import model as data_model
from uuid import UUID


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
    :type volumes: int

    :param initiator_secret: (optional) CHAP secret to use for the initiator.
    :type initiator_secret: str

    :param target_secret: (optional) CHAP secret to use for the target (mutual
        CHAP authentication).
    :type target_secret: str

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
        "initiatorSecret", str,
        array=False, optional=True,
        documentation="\
        CHAP secret to use for the initiator.\
        "
    )

    target_secret = data_model.property(
        "targetSecret", str,
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
    :type snapshot_uuid: str

    :param total_size: [required] Total size of this snapshot in bytes. It is
        equivalent to *total_size* of the volume when this snapshot was taken.
    :type total_size: int

    :param group_snapshot_uuid: [required] The current \"members\" results
        contains information about each snapshot in the group. Each of these
        members will have a \"uuid\" parameter for the snapshot's UUID.
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
        "SnapshotUUID", str,
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
        snapshot's UUID.\
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
    :type volume_access_groups: int

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
    :type volume_access_groups: int

    :param volume_pairs: [required] Information about a paired volume.
        Available only if a volume is paired. @see *volume_pairs* for return
        values.
    :type volume_pairs: VolumePair

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
