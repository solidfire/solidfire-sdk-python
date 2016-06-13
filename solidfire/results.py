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
from solidfire.models import ClusterAdmin
from solidfire.models import ClusterCapacity
from solidfire.models import ClusterConfig
from solidfire.models import ClusterFaultInfo
from solidfire.models import ClusterInfo
from solidfire.models import ClusterVersionInfo
from solidfire.models import Config
from solidfire.models import DriveInfo
from solidfire.models import EventInfo
from solidfire.models import GroupSnapshot
from solidfire.models import GroupSnapshotMembers
from solidfire.models import ISCSISession
from solidfire.models import Network
from solidfire.models import Node
from solidfire.models import PendingNode
from solidfire.models import Snapshot
from solidfire.models import SoftwareVersionInfo
from solidfire.models import VirtualNetwork
from solidfire.models import Volume
from solidfire.models import VolumeAccessGroup
from solidfire.models import VolumeStats


class AddDrivesResult(data_model.DataObject):
    """
    The object returned by the \"add_drives\" API Service call.
    """

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class AddVirtualNetworkResult(data_model.DataObject):
    """
    The object returned by the \"add_virtual_network\" API Service call.

    :param virtual_network_id: [required] The virtual network ID of the new
        virtual network.
    :type virtual_network_id: int
    """

    virtual_network_id = data_model.property(
        "virtualNetworkID", int,
        array=False, optional=False,
        documentation="\
        The virtual network ID of the new virtual network.\
        "
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


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


class ClearClusterFaultsResult(data_model.DataObject):
    """
    The object returned by the \"clear_cluster_faults\" API Service call.
    """

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


class DisableEncryptionAtRestResult(data_model.DataObject):
    """
    The object returned by the \"disable_encryption_at_rest\" API Service call.
    """

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class EnableEncryptionAtRestResult(data_model.DataObject):
    """
    The object returned by the \"enable_encryption_at_rest\" API Service call.
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


class GetLimitsResult(data_model.DataObject):
    """
    Limits for the cluster

    :param account_count_max: [required]
    :type account_count_max: int

    :param account_name_length_max: [required]
    :type account_name_length_max: int

    :param account_name_length_min: [required]
    :type account_name_length_min: int

    :param bulk_volume_jobs_per_node_max: [required]
    :type bulk_volume_jobs_per_node_max: int

    :param bulk_volume_jobs_per_volume_max: [required]
    :type bulk_volume_jobs_per_volume_max: int

    :param clone_jobs_per_volume_max: [required]
    :type clone_jobs_per_volume_max: int

    :param cluster_pairs_count_max: [required]
    :type cluster_pairs_count_max: int

    :param initiator_name_length_max: [required]
    :type initiator_name_length_max: int

    :param initiators_per_volume_access_group_count_max: [required]
    :type initiators_per_volume_access_group_count_max: int

    :param secret_length_max: [required]
    :type secret_length_max: int

    :param secret_length_min: [required]
    :type secret_length_min: int

    :param snapshot_name_length_max: [required]
    :type snapshot_name_length_max: int

    :param snapshots_per_volume_max: [required]
    :type snapshots_per_volume_max: int

    :param volume_access_group_count_max: [required]
    :type volume_access_group_count_max: int

    :param volume_access_group_lun_max: [required]
    :type volume_access_group_lun_max: int

    :param volume_access_group_name_length_max: [required]
    :type volume_access_group_name_length_max: int

    :param volume_access_group_name_length_min: [required]
    :type volume_access_group_name_length_min: int

    :param volume_access_groups_per_initiator_count_max: [required]
    :type volume_access_groups_per_initiator_count_max: int

    :param volume_access_groups_per_volume_count_max: [required]
    :type volume_access_groups_per_volume_count_max: int

    :param volume_burst_iopsmax: [required]
    :type volume_burst_iopsmax: int

    :param volume_burst_iopsmin: [required]
    :type volume_burst_iopsmin: int

    :param volume_count_max: [required]
    :type volume_count_max: int

    :param volume_max_iopsmax: [required]
    :type volume_max_iopsmax: int

    :param volume_max_iopsmin: [required]
    :type volume_max_iopsmin: int

    :param volume_min_iopsmax: [required]
    :type volume_min_iopsmax: int

    :param volume_min_iopsmin: [required]
    :type volume_min_iopsmin: int

    :param volume_name_length_max: [required]
    :type volume_name_length_max: int

    :param volume_name_length_min: [required]
    :type volume_name_length_min: int

    :param volume_size_max: [required]
    :type volume_size_max: int

    :param volume_size_min: [required]
    :type volume_size_min: int

    :param volumes_per_account_count_max: [required]
    :type volumes_per_account_count_max: int

    :param volumes_per_group_snapshot_max: [required]
    :type volumes_per_group_snapshot_max: int

    :param volumes_per_volume_access_group_count_max: [required]
    :type volumes_per_volume_access_group_count_max: int
    """

    account_count_max = data_model.property(
        "accountCountMax", int,
        array=False, optional=False,
        documentation=None
    )

    account_name_length_max = data_model.property(
        "accountNameLengthMax", int,
        array=False, optional=False,
        documentation=None
    )

    account_name_length_min = data_model.property(
        "accountNameLengthMin", int,
        array=False, optional=False,
        documentation=None
    )

    bulk_volume_jobs_per_node_max = data_model.property(
        "bulkVolumeJobsPerNodeMax", int,
        array=False, optional=False,
        documentation=None
    )

    bulk_volume_jobs_per_volume_max = data_model.property(
        "bulkVolumeJobsPerVolumeMax", int,
        array=False, optional=False,
        documentation=None
    )

    clone_jobs_per_volume_max = data_model.property(
        "cloneJobsPerVolumeMax", int,
        array=False, optional=False,
        documentation=None
    )

    cluster_pairs_count_max = data_model.property(
        "clusterPairsCountMax", int,
        array=False, optional=False,
        documentation=None
    )

    initiator_name_length_max = data_model.property(
        "initiatorNameLengthMax", int,
        array=False, optional=False,
        documentation=None
    )

    initiators_per_volume_access_group_count_max = data_model.property(
        "initiatorsPerVolumeAccessGroupCountMax", int,
        array=False, optional=False,
        documentation=None
    )

    secret_length_max = data_model.property(
        "secretLengthMax", int,
        array=False, optional=False,
        documentation=None
    )

    secret_length_min = data_model.property(
        "secretLengthMin", int,
        array=False, optional=False,
        documentation=None
    )

    snapshot_name_length_max = data_model.property(
        "snapshotNameLengthMax", int,
        array=False, optional=False,
        documentation=None
    )

    snapshots_per_volume_max = data_model.property(
        "snapshotsPerVolumeMax", int,
        array=False, optional=False,
        documentation=None
    )

    volume_access_group_count_max = data_model.property(
        "volumeAccessGroupCountMax", int,
        array=False, optional=False,
        documentation=None
    )

    volume_access_group_lun_max = data_model.property(
        "volumeAccessGroupLunMax", int,
        array=False, optional=False,
        documentation=None
    )

    volume_access_group_name_length_max = data_model.property(
        "volumeAccessGroupNameLengthMax", int,
        array=False, optional=False,
        documentation=None
    )

    volume_access_group_name_length_min = data_model.property(
        "volumeAccessGroupNameLengthMin", int,
        array=False, optional=False,
        documentation=None
    )

    volume_access_groups_per_initiator_count_max = data_model.property(
        "volumeAccessGroupsPerInitiatorCountMax", int,
        array=False, optional=False,
        documentation=None
    )

    volume_access_groups_per_volume_count_max = data_model.property(
        "volumeAccessGroupsPerVolumeCountMax", int,
        array=False, optional=False,
        documentation=None
    )

    volume_burst_iopsmax = data_model.property(
        "volumeBurstIOPSMax", int,
        array=False, optional=False,
        documentation=None
    )

    volume_burst_iopsmin = data_model.property(
        "volumeBurstIOPSMin", int,
        array=False, optional=False,
        documentation=None
    )

    volume_count_max = data_model.property(
        "volumeCountMax", int,
        array=False, optional=False,
        documentation=None
    )

    volume_max_iopsmax = data_model.property(
        "volumeMaxIOPSMax", int,
        array=False, optional=False,
        documentation=None
    )

    volume_max_iopsmin = data_model.property(
        "volumeMaxIOPSMin", int,
        array=False, optional=False,
        documentation=None
    )

    volume_min_iopsmax = data_model.property(
        "volumeMinIOPSMax", int,
        array=False, optional=False,
        documentation=None
    )

    volume_min_iopsmin = data_model.property(
        "volumeMinIOPSMin", int,
        array=False, optional=False,
        documentation=None
    )

    volume_name_length_max = data_model.property(
        "volumeNameLengthMax", int,
        array=False, optional=False,
        documentation=None
    )

    volume_name_length_min = data_model.property(
        "volumeNameLengthMin", int,
        array=False, optional=False,
        documentation=None
    )

    volume_size_max = data_model.property(
        "volumeSizeMax", int,
        array=False, optional=False,
        documentation=None
    )

    volume_size_min = data_model.property(
        "volumeSizeMin", int,
        array=False, optional=False,
        documentation=None
    )

    volumes_per_account_count_max = data_model.property(
        "volumesPerAccountCountMax", int,
        array=False, optional=False,
        documentation=None
    )

    volumes_per_group_snapshot_max = data_model.property(
        "volumesPerGroupSnapshotMax", int,
        array=False, optional=False,
        documentation=None
    )

    volumes_per_volume_access_group_count_max = data_model.property(
        "volumesPerVolumeAccessGroupCountMax", int,
        array=False, optional=False,
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


class ModifyClusterAdminResult(data_model.DataObject):
    """
    The object returned by the \"modify_cluster_admin\" API Service call.
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


class RemoveClusterAdminResult(data_model.DataObject):
    """
    The object returned by the \"remove_cluster_admin\" API Service call.
    """

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class RemoveNodesResult(data_model.DataObject):
    """
    The object returned by the \"remove_nodes\" API Service call.
    """

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class RemoveVirtualNetworkResult(data_model.DataObject):
    """
    The object returned by the \"remove_virtual_network\" API Service call.
    """

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class RestoreDeletedVolumeResult(data_model.DataObject):
    """
    The object returned by the \"restore_deleted_volume\" API Service call.
    """

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class TestDrivesResult(data_model.DataObject):
    """
    The object returned by the \"test_drives\" API Service call.

    :param details: [required]
    :type details: str
    """

    details = data_model.property(
        "details", str,
        array=False, optional=False,
        documentation=None
    )

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


class AddClusterAdminResult(data_model.DataObject):
    """
    The object returned by the \"add_cluster_admin\" API Service call.

    :param cluster_admin_id: [required] *cluster_admin_id* for the newly
        created Cluster Admin.
    :type cluster_admin_id: int
    """

    cluster_admin_id = data_model.property(
        "clusterAdminID", int,
        array=False, optional=False,
        documentation="\
        *cluster_admin_id* for the newly created Cluster Admin.\
        "
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class AddNodesResult(data_model.DataObject):
    """
    The object returned by the \"add_nodes\" API Service call.

    :param nodes: [required] An array of objects mapping the previous
        \"pendingNodeID\" to the \"nodeID\".
    :type nodes: PendingNode
    """

    nodes = data_model.property(
        "nodes", PendingNode,
        array=True, optional=False,
        documentation="\
        An array of objects mapping the previous *\"pending_node_id\"* to the\
        \"nodeID\".\
        "
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class AsyncHandleResult(data_model.DataObject):
    """
    The object returned by the \"async_handle\" API Service call.

    :param async_handle: [required]
    :type async_handle: int
    """

    async_handle = data_model.property(
        "asyncHandle", int,
        array=False, optional=False,
        documentation=None
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


class GetClusterCapacityResult(data_model.DataObject):
    """
    The object returned by the \"get_cluster_capacity\" API Service call.

    :param cluster_capacity: [required]
    :type cluster_capacity: ClusterCapacity
    """

    cluster_capacity = data_model.property(
        "clusterCapacity", ClusterCapacity,
        array=False, optional=False,
        documentation=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class GetClusterConfigResult(data_model.DataObject):
    """
    The object returned by the \"get_cluster_config\" API Service call.

    :param cluster: [required] Cluster configuration information the node uses
        to communicate with the cluster.
    :type cluster: ClusterConfig
    """

    cluster = data_model.property(
        "cluster", ClusterConfig,
        array=False, optional=False,
        documentation="\
        Cluster configuration information the node uses to communicate with\
        the cluster.\
        "
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class GetClusterInfoResult(data_model.DataObject):
    """
    The object returned by the \"get_cluster_info\" API Service call.

    :param cluster_info: [required]
    :type cluster_info: ClusterInfo
    """

    cluster_info = data_model.property(
        "clusterInfo", ClusterInfo,
        array=False, optional=False,
        documentation=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class GetConfigResult(data_model.DataObject):
    """
    The object returned by the \"get_config\" API Service call.

    :param config: [required] The details of the cluster. Values returned in
        \"config\": cluster- Cluster information that identifies how the node
        communicates with the cluster it is associated with. (Object) network -
        Network information for bonding and Ethernet connections. (Object)
    :type config: Config
    """

    config = data_model.property(
        "config", Config,
        array=False, optional=False,
        documentation="\
        The details of the cluster. Values returned in \"config\": cluster-\
        Cluster information that identifies how the node communicates with the\
        cluster it is associated with. (Object) network - Network information\
        for bonding and Ethernet connections. (Object)\
        "
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class GetCurrentClusterAdminResult(data_model.DataObject):
    """
    The object returned by the \"get_current_cluster_admin\" API Service call.

    :param cluster_admin: [required] Information about all cluster and LDAP
        administrators that exist for a cluster.
    :type cluster_admin: ClusterAdmin
    """

    cluster_admin = data_model.property(
        "clusterAdmin", ClusterAdmin,
        array=False, optional=False,
        documentation="\
        Information about all cluster and LDAP administrators that exist for a\
        cluster.\
        "
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class GetNetworkConfigResult(data_model.DataObject):
    """
    The object returned by the \"get_network_config\" API Service call.

    :param network: [required]
    :type network: Network
    """

    network = data_model.property(
        "network", Network,
        array=False, optional=False,
        documentation=None
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


class ListActiveNodesResult(data_model.DataObject):
    """
    The object returned by the \"list_active_nodes\" API Service call.

    :param nodes: [required]
    :type nodes: Node
    """

    nodes = data_model.property(
        "nodes", Node,
        array=True, optional=False,
        documentation=None
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


class ListClusterAdminsResult(data_model.DataObject):
    """
    The object returned by the \"list_cluster_admins\" API Service call.

    :param cluster_admins: [required] Information about the cluster admin.
    :type cluster_admins: ClusterAdmin
    """

    cluster_admins = data_model.property(
        "clusterAdmins", ClusterAdmin,
        array=True, optional=False,
        documentation="\
        Information about the cluster admin.\
        "
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class ListClusterFaultsResult(data_model.DataObject):
    """
    The object returned by the \"list_cluster_faults\" API Service call.

    :param faults: [required]
    :type faults: ClusterFaultInfo
    """

    faults = data_model.property(
        "faults", ClusterFaultInfo,
        array=True, optional=False,
        documentation=None
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


class ListDrivesResult(data_model.DataObject):
    """
    The object returned by the \"list_drives\" API Service call.

    :param drives: [required] Information for the drives that are connected to
        the cluster.
    :type drives: DriveInfo
    """

    drives = data_model.property(
        "drives", DriveInfo,
        array=True, optional=False,
        documentation="\
        Information for the drives that are connected to the cluster.\
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


class ListISCSISessionsResult(data_model.DataObject):
    """
    The object returned by the \"list_iscsisessions\" API Service call.

    :param sessions: [required]
    :type sessions: ISCSISession
    """

    sessions = data_model.property(
        "sessions", ISCSISession,
        array=True, optional=False,
        documentation=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class ListPendingNodesResult(data_model.DataObject):
    """
    The object returned by the \"list_pending_nodes\" API Service call.

    :param pending_nodes: [required]
    :type pending_nodes: PendingNode
    """

    pending_nodes = data_model.property(
        "pendingNodes", PendingNode,
        array=True, optional=False,
        documentation=None
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


class ListVirtualNetworksResult(data_model.DataObject):
    """
    The object returned by the \"list_virtual_networks\" API Service call.

    :param virtual_networks: [required] Object containing virtual network IP
        addresses.
    :type virtual_networks: VirtualNetwork
    """

    virtual_networks = data_model.property(
        "virtualNetworks", VirtualNetwork,
        array=True, optional=False,
        documentation="\
        Object containing virtual network IP addresses.\
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


class SetClusterConfigResult(data_model.DataObject):
    """
    The object returned by the \"set_cluster_config\" API Service call.

    :param cluster: [required] Settings for the cluster. All new and current
        settings are returned.
    :type cluster: ClusterConfig
    """

    cluster = data_model.property(
        "cluster", ClusterConfig,
        array=False, optional=False,
        documentation="\
        Settings for the cluster. All new and current settings are returned.\
        "
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class SetConfigResult(data_model.DataObject):
    """
    The object returned by the \"set_config\" API Service call.

    :param config: [required] The new and current configuration for the node.
    :type config: Config
    """

    config = data_model.property(
        "config", Config,
        array=False, optional=False,
        documentation="\
        The new and current configuration for the node.\
        "
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class SetNetworkConfigResult(data_model.DataObject):
    """
    The object returned by the \"set_network_config\" API Service call.

    :param network: [required]
    :type network: Network
    """

    network = data_model.property(
        "network", Network,
        array=False, optional=False,
        documentation=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class CreateGroupSnapshotResult(data_model.DataObject):
    """
    The object returned by the \"reset_drives\" API Service call.

    :param details: [required] Details of drives that are being reset.
    :type details: ResetDrivesDetails
    """

    details = data_model.property(
        "details", ResetDrivesDetails,
        array=False, optional=False,
        documentation="\
        Details of drives that are being reset.\
        "
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class SetClusterConfigResult(data_model.DataObject):
    """
    The object returned by the \"set_cluster_config\" API Service call.

    :param cluster: [required] Settings for the cluster. All new and current
        settings are returned.
    :type cluster: ClusterConfig
    """

    cluster = data_model.property(
        "cluster", ClusterConfig,
        array=False, optional=False,
        documentation="\
        Settings for the cluster. All new and current settings are returned.\
        "
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class SetConfigResult(data_model.DataObject):
    """
    The object returned by the \"set_config\" API Service call.

    :param config: [required] The new and current configuration for the node.
    :type config: Config
    """

    config = data_model.property(
        "config", Config,
        array=False, optional=False,
        documentation="\
        The new and current configuration for the node.\
        "
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class SetNetworkConfigResult(data_model.DataObject):
    """
    The object returned by the \"set_network_config\" API Service call.

    :param network: [required]
    :type network: Network
    """

    network = data_model.property(
        "network", Network,
        array=False, optional=False,
        documentation=None
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


class GetClusterFullThresholdResult(data_model.DataObject):
    """
    The object returned by the \"get_cluster_full_threshold\" API Service call.

    :param block_fullness: [required] Current computed level of block fullness
        of the cluster. Possible values:

        **stage1Happy**: No alerts or error conditions.

        **stage2Aware**: 3 nodes of capacity available.

        **stage3Low**: 2 nodes of capacity available.

        **stage4Critical**: 1 node of capacity available. No new volumes or
        clones can be created.

        **stage5CompletelyConsumed**: Completely consumed. Cluster is
        read-only, iSCSI connection is maintained but all writes are suspended.

    :type block_fullness: str

    :param fullness: [required] Reflects the highest level of fullness between
        \"blockFullness\" and \"metadataFullness\".
    :type fullness: str

    :param max_metadata_over_provision_factor: [required] A value
        representative of the number of times metadata space can be over
        provisioned relative to the amount of space available. For example, if
        there was enough metadata space to store 100 *ti_b* of volumes and this
        number was set to 5, then 500 *ti_b* worth of volumes could be created.
    :type max_metadata_over_provision_factor: int

    :param metadata_fullness: [required] Current computed level of metadata
        fullness of the cluster.
    :type metadata_fullness: str

    :param slice_reserve_used_threshold_pct: [required] Error condition;
        message sent to \"Alerts\" if the reserved slice utilization is greater
        than the *slice_reserve_used_threshold_pct* value returned.
    :type slice_reserve_used_threshold_pct: int

    :param stage2_aware_threshold: [required] Awareness condition: Value that
        is set for \"Stage 2\" cluster threshold level.
    :type stage2_aware_threshold: int

    :param stage2_block_threshold_bytes: [required] Number of bytes being used
        by the cluster at which a stage2 condition will exist.
    :type stage2_block_threshold_bytes: int

    :param stage3_block_threshold_bytes: [required] Number of bytes being used
        by the cluster at which a stage3 condition will exist.
    :type stage3_block_threshold_bytes: int

    :param stage3_block_threshold_percent: [required] The percent value set for
        stage3. At this percent full, a warning will be posted in the Alerts
        log.
    :type stage3_block_threshold_percent: int

    :param stage3_low_threshold: [required] Error condition; message sent to
        \"Alerts\" that capacity on a cluster is getting low.
    :type stage3_low_threshold: int

    :param stage4_critical_threshold: [required] Error condition; message sent
        to \"Alerts\" that capacity on a cluster is critically low.
    :type stage4_critical_threshold: int

    :param stage4_block_threshold_bytes: [required] Number of bytes being used
        by the cluster at which a stage4 condition will exist.
    :type stage4_block_threshold_bytes: int

    :param stage5_block_threshold_bytes: [required] Number of bytes being used
        by the cluster at which a stage5 condition will exist.
    :type stage5_block_threshold_bytes: int

    :param sum_total_cluster_bytes: [required] Physical capacity of the cluster
        measured in bytes.
    :type sum_total_cluster_bytes: int

    :param sum_total_metadata_cluster_bytes: [required] Total amount of space
        that can be used to store metadata.
    :type sum_total_metadata_cluster_bytes: int

    :param sum_used_cluster_bytes: [required] Number of bytes used on the
        cluster.
    :type sum_used_cluster_bytes: int

    :param sum_used_metadata_cluster_bytes: [required] Amount of space used on
        volume drives to store metadata.
    :type sum_used_metadata_cluster_bytes: int
    """

    block_fullness = data_model.property(
        "blockFullness", str,
        array=False, optional=False,
        documentation="\
        Current computed level of block fullness of the cluster.\
        Possible values:\
\
            **stage1Happy**: No alerts or error conditions.\
\
            **stage2Aware**: 3 nodes of capacity available.\
\
            **stage3Low**: 2 nodes of capacity available.\
\
            **stage4Critical**: 1 node of capacity available. No new volumes\
        or clones can be created.\
\
            **stage5CompletelyConsumed**: Completely consumed. Cluster is\
        read-only, iSCSI connection is maintained but all writes are\
        suspended.\
\
        "
    )

    fullness = data_model.property(
        "fullness", str,
        array=False, optional=False,
        documentation="\
        Reflects the highest level of fullness between *\"block_fullness\"*\
        and \"metadataFullness\".\
        "
    )

    max_metadata_over_provision_factor = data_model.property(
        "maxMetadataOverProvisionFactor", int,
        array=False, optional=False,
        documentation="\
        A value representative of the number of times metadata space can be\
        over provisioned relative to the amount of space available. For\
        example, if there was enough metadata space to store 100 *ti_b* of\
        volumes and this number was set to 5, then 500 *ti_b* worth of volumes\
        could be created.\
        "
    )

    metadata_fullness = data_model.property(
        "metadataFullness", str,
        array=False, optional=False,
        documentation="\
        Current computed level of metadata fullness of the cluster.\
        "
    )

    slice_reserve_used_threshold_pct = data_model.property(
        "sliceReserveUsedThresholdPct", int,
        array=False, optional=False,
        documentation="\
        Error condition; message sent to *\"alerts\"* if the reserved slice\
        utilization is greater than the *slice_reserve_used_threshold_pct*\
        value returned.\
        "
    )

    stage2_aware_threshold = data_model.property(
        "stage2AwareThreshold", int,
        array=False, optional=False,
        documentation="\
        Awareness condition: Value that is set for *\"stage* 2\" cluster\
        threshold level.\
        "
    )

    stage2_block_threshold_bytes = data_model.property(
        "stage2BlockThresholdBytes", int,
        array=False, optional=False,
        documentation="\
        Number of bytes being used by the cluster at which a stage2 condition\
        will exist.\
        "
    )

    stage3_block_threshold_bytes = data_model.property(
        "stage3BlockThresholdBytes", int,
        array=False, optional=False,
        documentation="\
        Number of bytes being used by the cluster at which a stage3 condition\
        will exist.\
        "
    )

    stage3_block_threshold_percent = data_model.property(
        "stage3BlockThresholdPercent", int,
        array=False, optional=False,
        documentation="\
        The percent value set for stage3. At this percent full, a warning will\
        be posted in the Alerts log.\
        "
    )

    stage3_low_threshold = data_model.property(
        "stage3LowThreshold", int,
        array=False, optional=False,
        documentation="\
        Error condition; message sent to *\"alerts\"* that capacity on a\
        cluster is getting low.\
        "
    )

    stage4_critical_threshold = data_model.property(
        "stage4CriticalThreshold", int,
        array=False, optional=False,
        documentation="\
        Error condition; message sent to *\"alerts\"* that capacity on a\
        cluster is critically low.\
        "
    )

    stage4_block_threshold_bytes = data_model.property(
        "stage4BlockThresholdBytes", int,
        array=False, optional=False,
        documentation="\
        Number of bytes being used by the cluster at which a stage4 condition\
        will exist.\
        "
    )

    stage5_block_threshold_bytes = data_model.property(
        "stage5BlockThresholdBytes", int,
        array=False, optional=False,
        documentation="\
        Number of bytes being used by the cluster at which a stage5 condition\
        will exist.\
        "
    )

    sum_total_cluster_bytes = data_model.property(
        "sumTotalClusterBytes", int,
        array=False, optional=False,
        documentation="\
        Physical capacity of the cluster measured in bytes.\
        "
    )

    sum_total_metadata_cluster_bytes = data_model.property(
        "sumTotalMetadataClusterBytes", int,
        array=False, optional=False,
        documentation="\
        Total amount of space that can be used to store metadata.\
        "
    )

    sum_used_cluster_bytes = data_model.property(
        "sumUsedClusterBytes", int,
        array=False, optional=False,
        documentation="\
        Number of bytes used on the cluster.\
        "
    )

    sum_used_metadata_cluster_bytes = data_model.property(
        "sumUsedMetadataClusterBytes", int,
        array=False, optional=False,
        documentation="\
        Amount of space used on volume drives to store metadata.\
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


class ListAllNodesResult(data_model.DataObject):
    """
    The object returned by the \"list_all_nodes\" API Service call.

    :param nodes: [required]
    :type nodes: Node

    :param pending_nodes: [required]
    :type pending_nodes: PendingNode
    """

    nodes = data_model.property(
        "nodes", Node,
        array=True, optional=False,
        documentation=None
    )

    pending_nodes = data_model.property(
        "pendingNodes", PendingNode,
        array=True, optional=False,
        documentation=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class ListEventsResult(data_model.DataObject):
    """
    The object returned by the \"list_events\" API Service call.

    :param event_queue_type: [required]
    :type event_queue_type: str

    :param events: [required]
    :type events: EventInfo
    """

    event_queue_type = data_model.property(
        "eventQueueType", str,
        array=False, optional=False,
        documentation=None
    )

    events = data_model.property(
        "events", EventInfo,
        array=True, optional=False,
        documentation=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class ModifyClusterFullThresholdResult(data_model.DataObject):
    """
    The object returned by the \"modify_cluster_full_threshold\" API Service
    call.

    :param block_fullness: [required] Current computed level of block fullness
        of the cluster. Possible values:

        **stage1Happy**: No alerts or error conditions.

        **stage2Aware**: 3 nodes of capacity available.

        **stage3Low**: 2 nodes of capacity available.

        **stage4Critical**: 1 node of capacity available. No new volumes or
        clones can be created.

        **stage5CompletelyConsumed**: Completely consumed. Cluster is
        read-only, iSCSI connection is maintained but all writes are suspended.

    :type block_fullness: str

    :param fullness: [required] Reflects the highest level of fullness between
        \"blockFullness\" and \"metadataFullness\".
    :type fullness: str

    :param max_metadata_over_provision_factor: [required] A value
        representative of the number of times metadata space can be over
        provisioned relative to the amount of space available. For example, if
        there was enough metadata space to store 100 *ti_b* of volumes and this
        number was set to 5, then 500 *ti_b* worth of volumes could be created.
    :type max_metadata_over_provision_factor: int

    :param metadata_fullness: [required] Current computed level of metadata
        fullness of the cluster.
    :type metadata_fullness: str

    :param slice_reserve_used_threshold_pct: [required] Error condition;
        message sent to \"Alerts\" if the reserved slice utilization is greater
        than the *slice_reserve_used_threshold_pct* value returned.
    :type slice_reserve_used_threshold_pct: int

    :param stage2_aware_threshold: [required] Awareness condition: Value that
        is set for \"Stage 2\" cluster threshold level.
    :type stage2_aware_threshold: int

    :param stage2_block_threshold_bytes: [required] Number of bytes being used
        by the cluster at which a stage2 condition will exist.
    :type stage2_block_threshold_bytes: int

    :param stage3_block_threshold_bytes: [required] Number of bytes being used
        by the cluster at which a stage3 condition will exist.
    :type stage3_block_threshold_bytes: int

    :param stage3_block_threshold_percent: [required] The percent value set for
        stage3. At this percent full, a warning will be posted in the Alerts
        log.
    :type stage3_block_threshold_percent: int

    :param stage3_low_threshold: [required] Error condition; message sent to
        \"Alerts\" that capacity on a cluster is getting low.
    :type stage3_low_threshold: int

    :param stage4_critical_threshold: [required] Error condition; message sent
        to \"Alerts\" that capacity on a cluster is critically low.
    :type stage4_critical_threshold: int

    :param stage4_block_threshold_bytes: [required] Number of bytes being used
        by the cluster at which a stage4 condition will exist.
    :type stage4_block_threshold_bytes: int

    :param stage5_block_threshold_bytes: [required] Number of bytes being used
        by the cluster at which a stage5 condition will exist.
    :type stage5_block_threshold_bytes: int

    :param sum_total_cluster_bytes: [required] Physical capacity of the cluster
        measured in bytes.
    :type sum_total_cluster_bytes: int

    :param sum_total_metadata_cluster_bytes: [required] Total amount of space
        that can be used to store metadata.
    :type sum_total_metadata_cluster_bytes: int

    :param sum_used_cluster_bytes: [required] Number of bytes used on the
        cluster.
    :type sum_used_cluster_bytes: int

    :param sum_used_metadata_cluster_bytes: [required] Amount of space used on
        volume drives to store metadata.
    :type sum_used_metadata_cluster_bytes: int
    """

    block_fullness = data_model.property(
        "blockFullness", str,
        array=False, optional=False,
        documentation="\
        Current computed level of block fullness of the cluster.\
        Possible values:\
\
            **stage1Happy**: No alerts or error conditions.\
\
            **stage2Aware**: 3 nodes of capacity available.\
\
            **stage3Low**: 2 nodes of capacity available.\
\
            **stage4Critical**: 1 node of capacity available. No new volumes\
        or clones can be created.\
\
            **stage5CompletelyConsumed**: Completely consumed. Cluster is\
        read-only, iSCSI connection is maintained but all writes are\
        suspended.\
\
        "
    )

    fullness = data_model.property(
        "fullness", str,
        array=False, optional=False,
        documentation="\
        Reflects the highest level of fullness between *\"block_fullness\"*\
        and \"metadataFullness\".\
        "
    )

    max_metadata_over_provision_factor = data_model.property(
        "maxMetadataOverProvisionFactor", int,
        array=False, optional=False,
        documentation="\
        A value representative of the number of times metadata space can be\
        over provisioned relative to the amount of space available. For\
        example, if there was enough metadata space to store 100 *ti_b* of\
        volumes and this number was set to 5, then 500 *ti_b* worth of volumes\
        could be created.\
        "
    )

    metadata_fullness = data_model.property(
        "metadataFullness", str,
        array=False, optional=False,
        documentation="\
        Current computed level of metadata fullness of the cluster.\
        "
    )

    slice_reserve_used_threshold_pct = data_model.property(
        "sliceReserveUsedThresholdPct", int,
        array=False, optional=False,
        documentation="\
        Error condition; message sent to *\"alerts\"* if the reserved slice\
        utilization is greater than the *slice_reserve_used_threshold_pct*\
        value returned.\
        "
    )

    stage2_aware_threshold = data_model.property(
        "stage2AwareThreshold", int,
        array=False, optional=False,
        documentation="\
        Awareness condition: Value that is set for *\"stage* 2\" cluster\
        threshold level.\
        "
    )

    stage2_block_threshold_bytes = data_model.property(
        "stage2BlockThresholdBytes", int,
        array=False, optional=False,
        documentation="\
        Number of bytes being used by the cluster at which a stage2 condition\
        will exist.\
        "
    )

    stage3_block_threshold_bytes = data_model.property(
        "stage3BlockThresholdBytes", int,
        array=False, optional=False,
        documentation="\
        Number of bytes being used by the cluster at which a stage3 condition\
        will exist.\
        "
    )

    stage3_block_threshold_percent = data_model.property(
        "stage3BlockThresholdPercent", int,
        array=False, optional=False,
        documentation="\
        The percent value set for stage3. At this percent full, a warning will\
        be posted in the Alerts log.\
        "
    )

    stage3_low_threshold = data_model.property(
        "stage3LowThreshold", int,
        array=False, optional=False,
        documentation="\
        Error condition; message sent to *\"alerts\"* that capacity on a\
        cluster is getting low.\
        "
    )

    stage4_critical_threshold = data_model.property(
        "stage4CriticalThreshold", int,
        array=False, optional=False,
        documentation="\
        Error condition; message sent to *\"alerts\"* that capacity on a\
        cluster is critically low.\
        "
    )

    stage4_block_threshold_bytes = data_model.property(
        "stage4BlockThresholdBytes", int,
        array=False, optional=False,
        documentation="\
        Number of bytes being used by the cluster at which a stage4 condition\
        will exist.\
        "
    )

    stage5_block_threshold_bytes = data_model.property(
        "stage5BlockThresholdBytes", int,
        array=False, optional=False,
        documentation="\
        Number of bytes being used by the cluster at which a stage5 condition\
        will exist.\
        "
    )

    sum_total_cluster_bytes = data_model.property(
        "sumTotalClusterBytes", int,
        array=False, optional=False,
        documentation="\
        Physical capacity of the cluster measured in bytes.\
        "
    )

    sum_total_metadata_cluster_bytes = data_model.property(
        "sumTotalMetadataClusterBytes", int,
        array=False, optional=False,
        documentation="\
        Total amount of space that can be used to store metadata.\
        "
    )

    sum_used_cluster_bytes = data_model.property(
        "sumUsedClusterBytes", int,
        array=False, optional=False,
        documentation="\
        Number of bytes used on the cluster.\
        "
    )

    sum_used_metadata_cluster_bytes = data_model.property(
        "sumUsedMetadataClusterBytes", int,
        array=False, optional=False,
        documentation="\
        Amount of space used on volume drives to store metadata.\
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


class GetClusterVersionInfoResult(data_model.DataObject):
    """
    The object returned by the \"get_cluster_version_info\" API Service call.

    :param cluster_apiversion: [required]
    :type cluster_apiversion: str

    :param cluster_version: [required]
    :type cluster_version: str

    :param cluster_version_info: [required]
    :type cluster_version_info: ClusterVersionInfo

    :param software_version_info: [required]
    :type software_version_info: SoftwareVersionInfo
    """

    cluster_apiversion = data_model.property(
        "clusterAPIVersion", str,
        array=False, optional=False,
        documentation=None
    )

    cluster_version = data_model.property(
        "clusterVersion", str,
        array=False, optional=False,
        documentation=None
    )

    cluster_version_info = data_model.property(
        "clusterVersionInfo", ClusterVersionInfo,
        array=True, optional=False,
        documentation=None
    )

    software_version_info = data_model.property(
        "softwareVersionInfo", SoftwareVersionInfo,
        array=False, optional=False,
        documentation=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)
