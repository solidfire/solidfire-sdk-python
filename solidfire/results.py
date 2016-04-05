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
from solidfire.models import Account
from solidfire.models import GroupSnapshot
from solidfire.models import GroupSnapshotMembers
from solidfire.models import Snapshot
from solidfire.models import Volume
from solidfire.models import VolumeAccessGroup
from solidfire.models import VolumeStats


class AsyncResult(data_model.DataObject):
    """
    The wrapped object returned by the *\"get_async_result\"* API Service call.




    **Note**: The return value of *get_async_result* is essentially a nested
    version of the standard JSON response with an additional status field.

    :param message: [required] The return value for the original method call if
        the call was completed successfully.
    :type message: str
    """

    message = data_model.property(
        "message", str,
        array=False, optional=False,
        documentation="\
        The return value for the original method call if the call was\
        completed successfully.\
        "
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class DeleteGroupSnapshotResult(data_model.DataObject):
    """
    The object returned by the \"delete_group_snapshot\" API Service call.
    """

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class DeleteSnapshotResult(data_model.DataObject):
    """
    The object returned by the \"delete_snapshot\" API Service call.
    """

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class DeleteVolumeAccessGroupResult(data_model.DataObject):
    """
    The object returned by the \"delete_volume_access_group\" API Service call.
    """

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class DeleteVolumeResult(data_model.DataObject):
    """
    The object returned by the \"delete_volume\" API Service call.
    """

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class GetAPIResult(data_model.DataObject):
    """
    The object returned by the \"get_api\" API Service call.

    :param current_version: [required]
    :type current_version: float

    :param supported_versions: [required]
    :type supported_versions: float
    """

    current_version = data_model.property(
        "currentVersion", float,
        array=False, optional=False,
        documentation=None
    )

    supported_versions = data_model.property(
        "supportedVersions", float,
        array=True, optional=False,
        documentation=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class ModifyAccountResult(data_model.DataObject):
    """
    The object returned by the \"modify_account\" API Service call.
    """

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class ModifyGroupSnapshotResult(data_model.DataObject):
    """
    The object returned by the \"modify_group_snapshot\" API Service call.
    """

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class ModifySnapshotResult(data_model.DataObject):
    """
    The object returned by the \"modify_snapshot\" API Service call.
    """

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class ModifyVolumeAccessGroupResult(data_model.DataObject):
    """
    The object returned by the \"modify_volume_access_group\" API Service call.
    """

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class ModifyVolumeResult(data_model.DataObject):
    """
    The object returned by the \"modify_volume\" API Service call.

    :param curve: (optional) The curve is a set of key-value pairs. The keys
        are I/O sizes in bytes. The values represent the cost performing an IOP
        at a specific I/O size. The curve is calculated relative to a 4096 byte
        operation set at 100 IOPS.
    :type curve: str
    """

    curve = data_model.property(
        "curve", str,
        array=False, optional=True,
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


class PurgeDeletedVolumeResult(data_model.DataObject):
    """
    The object returned by the \"purge_deleted_volume\" API Service call.
    """

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class RemoveAccountResult(data_model.DataObject):
    """
    The object returned by the \"remove_account\" API Service call.
    """

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class RestoreDeletedVolumeResult(data_model.DataObject):
    """
    The object returned by the \"restore_deleted_volume\" API Service call.
    """

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class AddAccountResult(data_model.DataObject):
    """
    The object returned by the \"add_account\" API Service call.

    :param account_id: [required] *account_id* for the newly created Account.
    :type account_id: int
    """

    account_id = data_model.property(
        "accountID", int,
        array=False, optional=False,
        documentation="\
        *account_id* for the newly created Account.\
        "
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class CreateVolumeAccessGroupResult(data_model.DataObject):
    """
    The object returned by the \"create_volume_access_group\" API Service call.

    :param volume_access_group_id: [required] The ID for the newly-created
        volume access group.
    :type volume_access_group_id: int
    """

    volume_access_group_id = data_model.property(
        "volumeAccessGroupID", int,
        array=False, optional=False,
        documentation="\
        The ID for the newly-created volume access group.\
        "
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class CreateVolumeResult(data_model.DataObject):
    """
    The object returned by the \"create_volume\" API Service call.

    :param volume_id: [required] *volume_id* for the newly created volume.
    :type volume_id: int

    :param curve: (optional) The curve is a set of key-value pairs. The keys
        are I/O sizes in bytes. The values represent the cost performing an IOP
        at a specific I/O size. The curve is calculated relative to a 4096 byte
        operation set at 100 IOPS.
    :type curve: str
    """

    volume_id = data_model.property(
        "volumeID", int,
        array=False, optional=False,
        documentation="\
        *volume_id* for the newly created volume.\
        "
    )

    curve = data_model.property(
        "curve", str,
        array=False, optional=True,
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


class GetAccountResult(data_model.DataObject):
    """
    The object returned by the \"get_account\" API Service call.

    :param account: [required] Account details.
    :type account: Account
    """

    account = data_model.property(
        "account", Account,
        array=False, optional=False,
        documentation="\
        Account details.\
        "
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class GetVolumeStatsResult(data_model.DataObject):
    """
    The object returned by the \"get_volume_stats\" API Service call.

    :param volume_stats: [required] Volume activity information.
    :type volume_stats: VolumeStats
    """

    volume_stats = data_model.property(
        "volumeStats", VolumeStats,
        array=False, optional=False,
        documentation="\
        Volume activity information.\
        "
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class ListAccountsResult(data_model.DataObject):
    """
    The object returned by the \"list_accounts\" API Service call.

    :param accounts: [required] List of accounts.
    :type accounts: Account
    """

    accounts = data_model.property(
        "accounts", Account,
        array=True, optional=False,
        documentation="\
        List of accounts.\
        "
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class ListActiveVolumesResult(data_model.DataObject):
    """
    The object returned by the \"list_active_volumes\" API Service call.

    :param volumes: [required] List of active volumes.
    :type volumes: Volume
    """

    volumes = data_model.property(
        "volumes", Volume,
        array=True, optional=False,
        documentation="\
        List of active volumes.\
        "
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class ListDeletedVolumesResult(data_model.DataObject):
    """
    The object returned by the \"list_deleted_volumes\" API Service call.

    :param volumes: [required] List of deleted volumes.
    :type volumes: Volume
    """

    volumes = data_model.property(
        "volumes", Volume,
        array=True, optional=False,
        documentation="\
        List of deleted volumes.\
        "
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class ListGroupSnapshotsResult(data_model.DataObject):
    """
    The object returned by the \"list_group_snapshots\" API Service call.

    :param group_snapshots: [required] List of Group Snapshots.
    :type group_snapshots: GroupSnapshot
    """

    group_snapshots = data_model.property(
        "groupSnapshots", GroupSnapshot,
        array=True, optional=False,
        documentation="\
        List of Group Snapshots.\
        "
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class ListSnapshotsResult(data_model.DataObject):
    """
    The object returned by the \"list_snapshots\" API Service call.

    :param snapshots: [required] Information about each snapshot for each
        volume. If *volume_id* is not provided, all snapshots for all volumes
        is returned. Snapshots that are in a group will be returned with a
        \"groupID\". Snapshots that are enabled for replication.
    :type snapshots: Snapshot
    """

    snapshots = data_model.property(
        "snapshots", Snapshot,
        array=True, optional=False,
        documentation="\
        Information about each snapshot for each volume.\
        If *volume_id* is not provided, all snapshots for all volumes is\
        returned.\
        Snapshots that are in a group will be returned with a \"groupID\".\
        Snapshots that are enabled for replication.\
        "
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class ListVolumeAccessGroupsResult(data_model.DataObject):
    """
    The object returned by the \"list_volume_access_groups\" API Service call.

    :param volume_access_groups: [required] List of volume access groups.
    :type volume_access_groups: VolumeAccessGroup
    """

    volume_access_groups = data_model.property(
        "volumeAccessGroups", VolumeAccessGroup,
        array=True, optional=False,
        documentation="\
        List of volume access groups.\
        "
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class ListVolumeStatsByAccountResult(data_model.DataObject):
    """
    The object returned by the \"list_volume_stats_by_account\" API Service
    call.

    :param volume_stats: [required] List of account activity information.

        **Note**: The *volume_id* member is 0 for each entry, as the values
        represent the summation of all volumes owned by the account.

    :type volume_stats: VolumeStats
    """

    volume_stats = data_model.property(
        "volumeStats", VolumeStats,
        array=True, optional=False,
        documentation="\
        List of account activity information.\
\
\
            **Note**: The *volume_id* member is 0 for each entry, as the\
        values represent the summation of all volumes owned by the account.\
\
        "
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class ListVolumeStatsByVolumeAccessGroupResult(data_model.DataObject):
    """
    The object returned by the \"list_volume_stats_by_volume_access_group\" API
    Service call.

    :param volume_stats: [required] List of account activity information.

        **Note**: The *volume_id* member is 0 for each entry, as the values
        represent the summation of all volumes owned by the account.

    :type volume_stats: VolumeStats
    """

    volume_stats = data_model.property(
        "volumeStats", VolumeStats,
        array=True, optional=False,
        documentation="\
        List of account activity information.\
\
\
            **Note**: The *volume_id* member is 0 for each entry, as the\
        values represent the summation of all volumes owned by the account.\
\
        "
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class ListVolumeStatsByVolumeResult(data_model.DataObject):
    """
    The object returned by the \"list_volume_stats_by_volume\" API Service
    call.

    :param volume_stats: [required] List of account activity information.
    :type volume_stats: VolumeStats
    """

    volume_stats = data_model.property(
        "volumeStats", VolumeStats,
        array=True, optional=False,
        documentation="\
        List of account activity information.\
        "
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class ListVolumesForAccountResult(data_model.DataObject):
    """
    The object returned by the \"list_volumes_for_account\" API Service call.

    :param volumes: [required] List of volumes.
    :type volumes: Volume
    """

    volumes = data_model.property(
        "volumes", Volume,
        array=True, optional=False,
        documentation="\
        List of volumes.\
        "
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class ListVolumesResult(data_model.DataObject):
    """
    The object returned by the \"list_volumes\" API Service call.

    :param volumes: [required] List of volumes.
    :type volumes: Volume
    """

    volumes = data_model.property(
        "volumes", Volume,
        array=True, optional=False,
        documentation="\
        List of volumes.\
        "
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class CreateGroupSnapshotResult(data_model.DataObject):
    """
    The object returned by the \"create_group_snapshot\" API Service call.

    :param group_snapshot_id: [required] Unique ID of the new group snapshot.
    :type group_snapshot_id: int

    :param members: [required] List of checksum, *volume_ids* and
        *snapshot_ids* for each member of the group.
    :type members: GroupSnapshotMembers
    """

    group_snapshot_id = data_model.property(
        "groupSnapshotID", int,
        array=False, optional=False,
        documentation="\
        Unique ID of the new group snapshot.\
        "
    )

    members = data_model.property(
        "members", GroupSnapshotMembers,
        array=True, optional=False,
        documentation="\
        List of checksum, *volume_ids* and *snapshot_ids* for each member of\
        the group.\
        "
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class CreateSnapshotResult(data_model.DataObject):
    """
    The object returned by the \"create_snapshot\" API Service call.

    :param snapshot_id: [required] ID of the newly-created snapshot.
    :type snapshot_id: int

    :param checksum: [required] A string that represents the correct digits in
        the stored snapshot. This checksum can be used later to compare other
        snapshots to detect errors in the data.
    :type checksum: str
    """

    snapshot_id = data_model.property(
        "snapshotID", int,
        array=False, optional=False,
        documentation="\
        ID of the newly-created snapshot.\
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


class GetAsyncResultResult(data_model.DataObject):
    """
    The object returned by the *\"get_async_result\"* API Service call.




    **Note**: The return value of *get_async_result* is essentially a nested
    version of the standard JSON response with an additional status field.

    :param result: [required] The resulting message for the original method
        call if the call was completed successfully.
    :type result: AsyncResult

    :param status: [required] Status of the asynchronous method call

        **running**: The method is still running.

        **complete**: The method is complete and the result or error is
        available.

    :type status: str
    """

    result = data_model.property(
        "result", AsyncResult,
        array=False, optional=False,
        documentation="\
        The resulting message for the original method call if the call was\
        completed successfully.\
        "
    )

    status = data_model.property(
        "status", str,
        array=False, optional=False,
        documentation="\
        Status of the asynchronous method call\
\
\
            **running**: The method is still running.\
\
\
\
            **complete**: The method is complete and the result or error is\
        available.\
\
        "
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class GetVolumeEfficiencyResult(data_model.DataObject):
    """
    The object returned by the \"get_volume_efficiency\" API Service call.

    :param compression: [required] The amount of space being saved by
        compressing data on a single volume. Stated as a ratio where \"1\"
        means data has been stored without being compressed.
    :type compression: float

    :param deduplication: [required] The amount of space being saved on a
        single volume by not duplicating data. Stated as a ratio.
    :type deduplication: float

    :param missing_volumes: [required] The volumes that could not be queried
        for efficiency data. Missing volumes can be caused by GC being less
        than hour old, temporary network loss or restarted services since the
        GC cycle.
    :type missing_volumes: int

    :param thin_provisioning: [required] The ratio of space used to the amount
        of space allocated for storing data. Stated as a ratio.
    :type thin_provisioning: float

    :param timestamp: [required] The last time efficiency data was collected
        after Garbage Collection (GC).
    :type timestamp: str
    """

    compression = data_model.property(
        "compression", float,
        array=False, optional=False,
        documentation="\
        The amount of space being saved by compressing data on a single\
        volume.\
        Stated as a ratio where \"1\" means data has been stored without being\
        compressed.\
        "
    )

    deduplication = data_model.property(
        "deduplication", float,
        array=False, optional=False,
        documentation="\
        The amount of space being saved on a single volume by not duplicating\
        data.\
        Stated as a ratio.\
        "
    )

    missing_volumes = data_model.property(
        "missingVolumes", int,
        array=True, optional=False,
        documentation="\
        The volumes that could not be queried for efficiency data.\
        Missing volumes can be caused by GC being less than hour old,\
        temporary network loss or restarted services since the GC cycle.\
        "
    )

    thin_provisioning = data_model.property(
        "thinProvisioning", float,
        array=False, optional=False,
        documentation="\
        The ratio of space used to the amount of space allocated for storing\
        data.\
        Stated as a ratio.\
        "
    )

    timestamp = data_model.property(
        "timestamp", str,
        array=False, optional=False,
        documentation="\
        The last time efficiency data was collected after Garbage Collection\
        (GC).\
        "
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class CloneVolumeResult(data_model.DataObject):
    """
    The object returned by the \"clone_volume\" API Service call.

    :param clone_id: [required] The ID of the newly-created clone.
    :type clone_id: int

    :param volume_id: [required] The volume ID of the newly-created clone.
    :type volume_id: int

    :param async_handle: [required] Handle value used to track the progress of
        the clone.
    :type async_handle: int
    """

    clone_id = data_model.property(
        "cloneID", int,
        array=False, optional=False,
        documentation="\
        The ID of the newly-created clone.\
        "
    )

    volume_id = data_model.property(
        "volumeID", int,
        array=False, optional=False,
        documentation="\
        The volume ID of the newly-created clone.\
        "
    )

    async_handle = data_model.property(
        "asyncHandle", int,
        array=False, optional=False,
        documentation="\
        Handle value used to track the progress of the clone.\
        "
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)
