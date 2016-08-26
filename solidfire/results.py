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
from solidfire.models import AddedNode
from solidfire.models import BackupTarget
from solidfire.models import BulkVolumeJob
from solidfire.models import ClusterAdmin
from solidfire.models import ClusterCapacity
from solidfire.models import ClusterConfig
from solidfire.models import ClusterFaultInfo
from solidfire.models import ClusterInfo
from solidfire.models import ClusterStats
from solidfire.models import ClusterVersionInfo
from solidfire.models import Config
from solidfire.models import DriveInfo
from solidfire.models import EventInfo
from solidfire.models import FibreChannelPortList
from solidfire.models import FibreChannelSession
from solidfire.models import GroupCloneVolumeMember
from solidfire.models import GroupSnapshot
from solidfire.models import GroupSnapshotMembers
from solidfire.models import ISCSISession
from solidfire.models import LdapConfiguration
from solidfire.models import Network
from solidfire.models import Node
from solidfire.models import PendingNode
from solidfire.models import Snapshot
from solidfire.models import SnmpNetwork
from solidfire.models import SnmpTrapRecipient
from solidfire.models import SnmpV3UsmUser
from solidfire.models import SoftwareVersionInfo
from solidfire.models import TestConnectEnsembleDetails
from solidfire.models import TestConnectMvipDetails
from solidfire.models import TestConnectSvipDetails
from solidfire.models import VirtualNetwork
from solidfire.models import Volume
from solidfire.models import VolumeAccessGroup
from solidfire.models import VolumeAccessGroupLunAssignments
from solidfire.models import VolumeStats


class AddDrivesResult(data_model.DataObject):
    """
    The object returned by the \"add_drives\" API Service call.
    """

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class AddLdapClusterAdminResult(data_model.DataObject):
    """
    The object returned by the \"add_ldap_cluster_admin\" API Service call.
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


class CompleteClusterPairingResult(data_model.DataObject):
    """
    The object returned by the \"complete_cluster_pairing\" API Service call.

    :param cluster_pair_id: [required] Unique identifier for the cluster pair.
    :type cluster_pair_id: int
    """

    cluster_pair_id = data_model.property(
        "clusterPairID", int,
        array=False, optional=False,
        documentation="\
        Unique identifier for the cluster pair.\
        "
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class CompleteVolumePairingResult(data_model.DataObject):
    """
    The object returned by the \"complete_volume_pairing\" API Service call.
    """

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class CreateScheduleResult(data_model.DataObject):
    """
    The object returned by the \"create_schedule\" API Service call.

    :param schedule_id: [required]
    :type schedule_id: int
    """

    schedule_id = data_model.property(
        "scheduleID", int,
        array=False, optional=False,
        documentation=None
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


class DisableEncryptionAtRestResult(data_model.DataObject):
    """
    The object returned by the \"disable_encryption_at_rest\" API Service call.
    """

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class DisableLdapAuthenticationResult(data_model.DataObject):
    """
    The object returned by the \"disable_ldap_authentication\" API Service
    call.
    """

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class DisableSnmpResult(data_model.DataObject):
    """
    The object returned by the \"disable_snmp\" API Service call.
    """

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class EnableEncryptionAtRestResult(data_model.DataObject):
    """
    The object returned by the \"enable_encryption_at_rest\" API Service call.
    """

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class EnableLdapAuthenticationResult(data_model.DataObject):
    """
    The object returned by the \"enable_ldap_authentication\" API Service call.
    """

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class EnableSnmpResult(data_model.DataObject):
    """
    The object returned by the \"enable_snmp\" API Service call.
    """

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class GetAPIResult(data_model.DataObject):
    """
    The object returned by the \"get_api\" API Service call.

    :param current_version: [required]
    :type current_version: float

    :param supported_versions: [required]
    :type supported_versions: float[]
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


class GetSnmpStateResult(data_model.DataObject):
    """
    The object returned by the \"get_snmp_state\" API Service call.

    :param enabled: [required] If the nodes in the cluster are configured for
        SNMP.
    :type enabled: bool

    :param snmp_v3_enabled: [required] If the node in the cluster is configured
        for SNMP v3.
    :type snmp_v3_enabled: bool
    """

    enabled = data_model.property(
        "enabled", bool,
        array=False, optional=False,
        documentation="\
        If the nodes in the cluster are configured for SNMP.\
        "
    )

    snmp_v3_enabled = data_model.property(
        "snmpV3Enabled", bool,
        array=False, optional=False,
        documentation="\
        If the node in the cluster is configured for SNMP v3.\
        "
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class ListFibreChannelPortInfoResult(data_model.DataObject):
    """
    *list_fibre_channel_port_info_result* is used to return information about
    the Fibre Channel ports.

    :param fibre_channel_port_info: [required] Used to return information about
        the Fibre Channel ports.
    :type fibre_channel_port_info: dict
    """

    fibre_channel_port_info = data_model.property(
        "fibreChannelPortInfo", dict,
        array=False, optional=False,
        documentation="\
        Used to return information about the Fibre Channel ports.\
        "
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class ListTestsResult(data_model.DataObject):
    """
    The object returned by the \"list_tests\" API Service call.

    :param tests: [required] List of tests that can be performed on the node.
    :type tests: str[]
    """

    tests = data_model.property(
        "tests", str,
        array=True, optional=False,
        documentation="\
        List of tests that can be performed on the node.\
        "
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class ListUtilitiesResult(data_model.DataObject):
    """
    The object returned by the \"list_utilities\" API Service call.

    :param utilities: [required] List of utilities currently available to run
        on the node.
    :type utilities: str[]
    """

    utilities = data_model.property(
        "utilities", str,
        array=True, optional=False,
        documentation="\
        List of utilities currently available to run on the node.\
        "
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class ModifyAccountResult(data_model.DataObject):
    """
    The object returned by the \"modify_account\" API Service call.
    """

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class ModifyBackupTargetResult(data_model.DataObject):
    """
    The object returned by the \"modify_backup_target\" API Service call.
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


class ModifyVolumeAccessGroupLunAssignmentsResult(data_model.DataObject):
    """
    The object returned by the \"modify_volume_access_group_lun_assignments\"
    API Service call.
    """

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class ModifyVolumeAccessGroupResult(data_model.DataObject):
    """
    The object returned by the \"modify_volume_access_group\" API Service call.
    """

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class ModifyVolumePairResult(data_model.DataObject):
    """
    The object returned by the \"modify_volume_pair\" API Service call.
    """

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class ModifyVolumeResult(data_model.DataObject):
    """
    The object returned by the \"modify_volume\" API Service call.

    :param curve: [required] The curve is a set of key-value pairs. The keys
        are I/O sizes in bytes. The values represent the cost performing an IOP
        at a specific I/O size. The curve is calculated relative to a 4096 byte
        operation set at 100 IOPS.
    :type curve: dict
    """

    curve = data_model.property(
        "curve", dict,
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


class RemoveBackupTargetResult(data_model.DataObject):
    """
    The object returned by the \"remove_backup_target\" API Service call.
    """

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class RemoveClusterAdminResult(data_model.DataObject):
    """
    The object returned by the \"remove_cluster_admin\" API Service call.
    """

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class RemoveClusterPairResult(data_model.DataObject):
    """
    The object returned by the \"remove_cluster_pair\" API Service call.
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


class RemoveVolumePairResult(data_model.DataObject):
    """
    The object returned by the \"remove_volume_pair\" API Service call.
    """

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class RestoreDeletedVolumeResult(data_model.DataObject):
    """
    The object returned by the \"restore_deleted_volume\" API Service call.
    """

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class SetSnmpACLResult(data_model.DataObject):
    """
    The object returned by the \"set_snmp_acl\" API Service call.
    """

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class SetSnmpInfoResult(data_model.DataObject):
    """
    The object returned by the \"set_snmp_info\" API Service call.
    """

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class SetSnmpTrapInfoResult(data_model.DataObject):
    """
    The object returned by the \"set_snmp_trap_info\" API Service call.
    """

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class SnmpSendTestTrapsResult(data_model.DataObject):
    """
    The object returned by the \"snmp_send_test_traps\" API Service call.

    :param status: [required]
    :type status: str
    """

    status = data_model.property(
        "status", str,
        array=False, optional=False,
        documentation=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class StartClusterPairingResult(data_model.DataObject):
    """
    The object returned by the \"start_cluster_pairing\" API Service call.

    :param cluster_pairing_key: [required] A string of characters that is used
        by the \"CompleteClusterPairing\" API method.
    :type cluster_pairing_key: str

    :param cluster_pair_id: [required] Unique identifier for the cluster pair.
    :type cluster_pair_id: int
    """

    cluster_pairing_key = data_model.property(
        "clusterPairingKey", str,
        array=False, optional=False,
        documentation="\
        A string of characters that is used by the\
        *\"complete_cluster_pairing\"* API method.\
        "
    )

    cluster_pair_id = data_model.property(
        "clusterPairID", int,
        array=False, optional=False,
        documentation="\
        Unique identifier for the cluster pair.\
        "
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class StartVolumePairingResult(data_model.DataObject):
    """
    The object returned by the \"start_volume_pairing\" API Service call.

    :param volume_pairing_key: [required] A string of characters that is used
        by the \"CompleteVolumePairing\" API method.
    :type volume_pairing_key: str
    """

    volume_pairing_key = data_model.property(
        "volumePairingKey", str,
        array=False, optional=False,
        documentation="\
        A string of characters that is used by the\
        *\"complete_volume_pairing\"* API method.\
        "
    )

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


class TestLdapAuthenticationResult(data_model.DataObject):
    """
    The object returned by the \"test_ldap_authentication\" API Service call.

    :param groups: [required] List of LDAP groups that the tested user is a
        member of.
    :type groups: str[]

    :param user_dn: [required] The tested user&#39;s full LDAP distinguished
        name.
    :type user_dn: str
    """

    groups = data_model.property(
        "groups", str,
        array=True, optional=False,
        documentation="\
        List of LDAP groups that the tested user is a member of.\
        "
    )

    user_dn = data_model.property(
        "userDN", str,
        array=False, optional=False,
        documentation="\
        The tested user&#39;s full LDAP distinguished name.\
        "
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
    :type nodes: AddedNode[]
    """

    nodes = data_model.property(
        "nodes", AddedNode,
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


class CreateBackupTargetResult(data_model.DataObject):
    """
    The object returned by the \"create_backup_target\" API Service call.

    :param backup_target_id: [required] Unique identifier assigned to the
        backup target.
    :type backup_target_id: int
    """

    backup_target_id = data_model.property(
        "backupTargetID", int,
        array=False, optional=False,
        documentation="\
        Unique identifier assigned to the backup target.\
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

    :param curve: [required] The curve is a set of key-value pairs. The keys
        are I/O sizes in bytes. The values represent the cost performing an IOP
        at a specific I/O size. The curve is calculated relative to a 4096 byte
        operation set at 100 IOPS.
    :type curve: dict
    """

    volume_id = data_model.property(
        "volumeID", int,
        array=False, optional=False,
        documentation="\
        *volume_id* for the newly created volume.\
        "
    )

    curve = data_model.property(
        "curve", dict,
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


class FibreChannelPortInfoResult(data_model.DataObject):
    """
    Used to return information about the Fibre Channel ports.

    :param result: [required] Used to return information about the Fibre
        Channel ports.
    :type result: FibreChannelPortList
    """

    result = data_model.property(
        "result", FibreChannelPortList,
        array=False, optional=False,
        documentation="\
        Used to return information about the Fibre Channel ports.\
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


class GetBackupTargetResult(data_model.DataObject):
    """
    The object returned by the \"get_backup_target\" API Service call.

    :param backup_target: [required] Object returned for backup target.
    :type backup_target: BackupTarget
    """

    backup_target = data_model.property(
        "backupTarget", BackupTarget,
        array=False, optional=False,
        documentation="\
        Object returned for backup target.\
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


class GetClusterStatsResult(data_model.DataObject):
    """
    The object returned by the \"get_cluster_stats\" API Service call.

    :param cluster_stats: [required]
    :type cluster_stats: ClusterStats
    """

    cluster_stats = data_model.property(
        "clusterStats", ClusterStats,
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


class GetNodeStatsResult(data_model.DataObject):
    """
    The object returned by the \"get_node_stats\" API Service call.

    :param node_stats: [required] Node activity information.
    :type node_stats: NodeStatsInfo
    """

    node_stats = data_model.property(
        "nodeStats", NodeStatsInfo,
        array=False, optional=False,
        documentation="\
        Node activity information.\
        "
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class GetScheduleResult(data_model.DataObject):
    """
    The object returned by the \"get_schedule\" API Service call.

    :param schedule: [required] The schedule attributes.
    :type schedule: Schedule
    """

    schedule = data_model.property(
        "schedule", Schedule,
        array=False, optional=False,
        documentation="\
        The schedule attributes.\
        "
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class GetSnmpTrapInfoResult(data_model.DataObject):
    """
    The object returned by the \"get_snmp_trap_info\" API Service call.

    :param trap_recipients: [required] List of hosts that are to receive the
        traps generated by the cluster.
    :type trap_recipients: SnmpTrapRecipient[]

    :param cluster_fault_traps_enabled: [required] If \"true\", when a cluster
        fault is logged a corresponding *solid_fire_cluster_fault_notification*
        is sent to the configured list of trap recipients.
    :type cluster_fault_traps_enabled: bool

    :param cluster_fault_resolved_traps_enabled: [required] If \"true\", when a
        cluster fault is logged a corresponding
        *solid_fire_cluster_fault_resolved_notification* is sent to the
        configured list of trap recipients.
    :type cluster_fault_resolved_traps_enabled: bool

    :param cluster_event_traps_enabled: [required] If \"true\", when a cluster
        fault is logged a corresponding *solid_fire_cluster_event_notification*
        is sent to the configured list of trap recipients.
    :type cluster_event_traps_enabled: bool
    """

    trap_recipients = data_model.property(
        "trapRecipients", SnmpTrapRecipient,
        array=True, optional=False,
        documentation="\
        List of hosts that are to receive the traps generated by the cluster.\
        "
    )

    cluster_fault_traps_enabled = data_model.property(
        "clusterFaultTrapsEnabled", bool,
        array=False, optional=False,
        documentation="\
        If \"true\", when a cluster fault is logged a corresponding\
        *solid_fire_cluster_fault_notification* is sent to the configured list\
        of trap recipients.\
        "
    )

    cluster_fault_resolved_traps_enabled = data_model.property(
        "clusterFaultResolvedTrapsEnabled", bool,
        array=False, optional=False,
        documentation="\
        If \"true\", when a cluster fault is logged a corresponding\
        *solid_fire_cluster_fault_resolved_notification* is sent to the\
        configured list of trap recipients.\
        "
    )

    cluster_event_traps_enabled = data_model.property(
        "clusterEventTrapsEnabled", bool,
        array=False, optional=False,
        documentation="\
        If \"true\", when a cluster fault is logged a corresponding\
        *solid_fire_cluster_event_notification* is sent to the configured list\
        of trap recipients.\
        "
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class GetVolumeAccessGroupLunAssignmentsResult(data_model.DataObject):
    """
    The object returned by the \"get_volume_access_group_lun_assignments\" API
    Service call.

    :param volume_access_group_lun_assignments: [required] List of all physical
        Fibre Channel ports, or a port for a single node.
    :type volume_access_group_lun_assignments: VolumeAccessGroupLunAssignments
    """

    volume_access_group_lun_assignments = data_model.property(
        "volumeAccessGroupLunAssignments", VolumeAccessGroupLunAssignments,
        array=False, optional=False,
        documentation="\
        List of all physical Fibre Channel ports, or a port for a single node.\
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
    :type accounts: Account[]
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
    :type nodes: Node[]
    """

    nodes = data_model.property(
        "nodes", Node,
        array=True, optional=False,
        documentation=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class ListActivePairedVolumesResult(data_model.DataObject):
    """
    The object returned by the \"list_active_paired_volumes\" API Service call.

    :param volumes: [required] Volume information for the paired volumes.
    :type volumes: Volume[]
    """

    volumes = data_model.property(
        "volumes", Volume,
        array=True, optional=False,
        documentation="\
        Volume information for the paired volumes.\
        "
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class ListActiveVolumesResult(data_model.DataObject):
    """
    The object returned by the \"list_active_volumes\" API Service call.

    :param volumes: [required] List of active volumes.
    :type volumes: Volume[]
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


class ListBackupTargetsResult(data_model.DataObject):
    """
    The object returned by the \"list_backup_targets\" API Service call.

    :param backup_targets: [required] Objects returned for each backup target.
    :type backup_targets: BackupTarget[]
    """

    backup_targets = data_model.property(
        "backupTargets", BackupTarget,
        array=True, optional=False,
        documentation="\
        Objects returned for each backup target.\
        "
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class ListBulkVolumeJobsResult(data_model.DataObject):
    """
    The object returned by the \"list_bulk_volume_jobs\" API Service call.

    :param bulk_volume_jobs: [required] An array of information for each bulk
        volume job.
    :type bulk_volume_jobs: BulkVolumeJob[]
    """

    bulk_volume_jobs = data_model.property(
        "bulkVolumeJobs", BulkVolumeJob,
        array=True, optional=False,
        documentation="\
        An array of information for each bulk volume job.\
        "
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class ListClusterAdminsResult(data_model.DataObject):
    """
    The object returned by the \"list_cluster_admins\" API Service call.

    :param cluster_admins: [required] Information about the cluster admin.
    :type cluster_admins: ClusterAdmin[]
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
    :type faults: ClusterFaultInfo[]
    """

    faults = data_model.property(
        "faults", ClusterFaultInfo,
        array=True, optional=False,
        documentation=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class ListClusterPairsResult(data_model.DataObject):
    """
    The object returned by the \"list_cluster_pairs\" API Service call.

    :param cluster_pairs: [required] Information about each paired cluster.
    :type cluster_pairs: PairedCluster[]
    """

    cluster_pairs = data_model.property(
        "clusterPairs", PairedCluster,
        array=True, optional=False,
        documentation="\
        Information about each paired cluster.\
        "
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class ListDeletedVolumesResult(data_model.DataObject):
    """
    The object returned by the \"list_deleted_volumes\" API Service call.

    :param volumes: [required] List of deleted volumes.
    :type volumes: Volume[]
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
    :type drives: DriveInfo[]
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


class ListFibreChannelSessionsResult(data_model.DataObject):
    """
    Used to return information about the Fibre Channel sessions.

    :param sessions: [required] A list of *fibre_channel_session* objects with
        information about the Fibre Channel session.
    :type sessions: FibreChannelSession[]
    """

    sessions = data_model.property(
        "sessions", FibreChannelSession,
        array=True, optional=False,
        documentation="\
        A list of *fibre_channel_session* objects with information about the\
        Fibre Channel session.\
        "
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class ListGroupSnapshotsResult(data_model.DataObject):
    """
    The object returned by the \"list_group_snapshots\" API Service call.

    :param group_snapshots: [required] List of Group Snapshots.
    :type group_snapshots: GroupSnapshot[]
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
    :type sessions: ISCSISession[]
    """

    sessions = data_model.property(
        "sessions", ISCSISession,
        array=True, optional=False,
        documentation=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class ListNodeStatsResult(data_model.DataObject):
    """
    The object returned by the \"list_node_stats\" API Service call.

    :param node_stats: [required] Node activity information for all nodes.
    :type node_stats: NodeStatsNodes
    """

    node_stats = data_model.property(
        "nodeStats", NodeStatsNodes,
        array=False, optional=False,
        documentation="\
        Node activity information for all nodes.\
        "
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class ListPendingNodesResult(data_model.DataObject):
    """
    The object returned by the \"list_pending_nodes\" API Service call.

    :param pending_nodes: [required]
    :type pending_nodes: PendingNode[]
    """

    pending_nodes = data_model.property(
        "pendingNodes", PendingNode,
        array=True, optional=False,
        documentation=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class ListSchedulesResult(data_model.DataObject):
    """
    The object returned by the \"list_schedules\" API Service call.

    :param schedules: [required] The list of schedules currently on the
        cluster.
    :type schedules: Schedule[]
    """

    schedules = data_model.property(
        "schedules", Schedule,
        array=True, optional=False,
        documentation="\
        The list of schedules currently on the cluster.\
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
    :type snapshots: Snapshot[]
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
    :type virtual_networks: VirtualNetwork[]
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
    :type volume_access_groups: VolumeAccessGroup[]
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

    :type volume_stats: VolumeStats[]
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

    :type volume_stats: VolumeStats[]
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
    :type volume_stats: VolumeStats[]
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
    :type volumes: Volume[]
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
    :type volumes: Volume[]
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
        documentation="\
        Contains a list of information about the Fibre Channel ports.\
        "
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


class StartBulkVolumeReadResult(data_model.DataObject):
    """
    The object returned by the \"start_bulk_volume_read\" API Service call.

    :param async_handle: [required] ID of the async process to be checked for
        completion.
    :type async_handle: int

    :param key: [required] Opaque key uniquely identifying the session.
    :type key: str

    :param url: [required] URL to access the node&#39;s web server
    :type url: str
    """

    async_handle = data_model.property(
        "asyncHandle", int,
        array=False, optional=False,
        documentation="\
        ID of the async process to be checked for completion.\
        "
    )

    key = data_model.property(
        "key", str,
        array=False, optional=False,
        documentation="\
        Opaque key uniquely identifying the session.\
        "
    )

    url = data_model.property(
        "url", str,
        array=False, optional=False,
        documentation="\
        URL to access the node&#39;s web server\
        "
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class StartBulkVolumeWriteResult(data_model.DataObject):
    """
    The object returned by the \"start_bulk_volume_write\" API Service call.

    :param async_handle: [required] ID of the async process to be checked for
        completion.
    :type async_handle: int

    :param key: [required] Opaque key uniquely identifying the session.
    :type key: str

    :param url: [required] URL to access the node&#39;s web server
    :type url: str
    """

    async_handle = data_model.property(
        "asyncHandle", int,
        array=False, optional=False,
        documentation="\
        ID of the async process to be checked for completion.\
        "
    )

    key = data_model.property(
        "key", str,
        array=False, optional=False,
        documentation="\
        Opaque key uniquely identifying the session.\
        "
    )

    url = data_model.property(
        "url", str,
        array=False, optional=False,
        documentation="\
        URL to access the node&#39;s web server\
        "
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class TestConnectEnsembleResult(data_model.DataObject):
    """
    The object returned by the \"test_connect_ensemble\" API Service call.

    :param details: [required]
    :type details: TestConnectEnsembleDetails

    :param duration: [required] The length of time required to run the test.
    :type duration: str

    :param result: [required] The results of the entire test
    :type result: str
    """

    details = data_model.property(
        "details", TestConnectEnsembleDetails,
        array=False, optional=False,
        documentation=None
    )

    duration = data_model.property(
        "duration", str,
        array=False, optional=False,
        documentation="\
        The length of time required to run the test.\
        "
    )

    result = data_model.property(
        "result", str,
        array=False, optional=False,
        documentation="\
        The results of the entire test\
        "
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class TestConnectMvipResult(data_model.DataObject):
    """
    The object returned by the \"test_connect_mvip\" API Service call.

    :param details: [required] Information about the test operation
    :type details: TestConnectMvipDetails

    :param duration: [required] The length of time required to run the test.
    :type duration: str

    :param result: [required] The results of the entire test
    :type result: str
    """

    details = data_model.property(
        "details", TestConnectMvipDetails,
        array=False, optional=False,
        documentation="\
        Information about the test operation\
        "
    )

    duration = data_model.property(
        "duration", str,
        array=False, optional=False,
        documentation="\
        The length of time required to run the test.\
        "
    )

    result = data_model.property(
        "result", str,
        array=False, optional=False,
        documentation="\
        The results of the entire test\
        "
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class TestConnectSvipResult(data_model.DataObject):
    """
    The object returned by the \"test_connect_svip\" API Service call.

    :param details: [required] Information about the test operation
    :type details: TestConnectSvipDetails

    :param duration: [required] The length of time required to run the test.
    :type duration: str

    :param result: [required] The results of the entire test
    :type result: str
    """

    details = data_model.property(
        "details", TestConnectSvipDetails,
        array=False, optional=False,
        documentation="\
        Information about the test operation\
        "
    )

    duration = data_model.property(
        "duration", str,
        array=False, optional=False,
        documentation="\
        The length of time required to run the test.\
        "
    )

    result = data_model.property(
        "result", str,
        array=False, optional=False,
        documentation="\
        The results of the entire test\
        "
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class TestPingResult(data_model.DataObject):
    """
    The object returned by the \"test_ping\" API Service call.

    :param result: [required] Result of the ping test.
    :type result: str

    :param duration: [required] The total duration of the ping test.
    :type duration: str

    :param details: [required] List of each IP the node was able to communicate
        with.
    :type details: str
    """

    result = data_model.property(
        "result", str,
        array=False, optional=False,
        documentation="\
        Result of the ping test.\
        "
    )

    duration = data_model.property(
        "duration", str,
        array=False, optional=False,
        documentation="\
        The total duration of the ping test.\
        "
    )

    details = data_model.property(
        "details", str,
        array=False, optional=False,
        documentation="\
        List of each IP the node was able to communicate with.\
        "
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class UpdateBulkVolumeStatusResult(data_model.DataObject):
    """
    The object returned by the \"update_bulk_volume_status\" API Service call.

    :param status: [required] Status of the session requested. Returned status:

        **** **active** **done** **failed**

    :type status: str

    :param url: [required] The URL to access the node&#39;s web server provided
        only if the session is still active.
    :type url: str

    :param attributes: [required] Returns attributes that were specified in the
        *bulk_volume_status_update* method. Values are returned if they have
        changed or not.
    :type attributes: dict
    """

    status = data_model.property(
        "status", str,
        array=False, optional=False,
        documentation="\
        Status of the session requested. Returned status:\
\
\
\
        ****\
        **active**\
        **done**\
        **failed**\
        "
    )

    url = data_model.property(
        "url", str,
        array=False, optional=False,
        documentation="\
        The URL to access the node&#39;s web server provided only if the\
        session is still active.\
        "
    )

    attributes = data_model.property(
        "attributes", dict,
        array=False, optional=False,
        documentation="\
        Returns attributes that were specified in the\
        *bulk_volume_status_update* method. Values are returned if they have\
        changed or not.\
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
    :type members: GroupSnapshotMembers[]
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


class GetSnmpACLResult(data_model.DataObject):
    """
    The object returned by the \"get_snmp_acl\" API Service call.

    :param networks: [required] List of networks and what type of access they
        have to the SNMP servers running on the cluster nodes. Present if SNMP
        v3 is disabled.
    :type networks: SnmpNetwork[]

    :param usm_users: [required] List of users and the type of access they have
        to the SNMP servers running on the cluster nodes. Present if SNMP v3 is
        enabled.
    :type usm_users: SnmpV3UsmUser[]
    """

    networks = data_model.property(
        "networks", SnmpNetwork,
        array=True, optional=False,
        documentation="\
        List of networks and what type of access they have to the SNMP servers\
        running on the cluster nodes. Present if SNMP v3 is disabled.\
        "
    )

    usm_users = data_model.property(
        "usmUsers", SnmpV3UsmUser,
        array=True, optional=False,
        documentation="\
        List of users and the type of access they have to the SNMP servers\
        running on the cluster nodes. Present if SNMP v3 is enabled.\
        "
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class GetSnmpInfoResult(data_model.DataObject):
    """
    The object returned by the \"get_snmp_info\" API Service call.

    :param networks: [required] List of networks and access types enabled for
        SNMP.

        **Note**: \"networks\" will only be present if SNMP V3 is disabled.

    :type networks: SnmpNetwork[]

    :param enabled: [required] If the nodes in the cluster are configured for
        SNMP.
    :type enabled: bool

    :param snmp_v3_enabled: [required] If the nodes in the cluster are
        configured for SNMP v3.
    :type snmp_v3_enabled: bool

    :param usm_users: [required] If SNMP v3 is enabled, the values returned is
        a list of user access parameters for SNMP information from the cluster.
        This will be returned instead of the \"networks\" parameter.
    :type usm_users: SnmpV3UsmUser[]
    """

    networks = data_model.property(
        "networks", SnmpNetwork,
        array=True, optional=False,
        documentation="\
        List of networks and access types enabled for SNMP.\
\
\
\
\
        **Note**: \"networks\" will only be present if SNMP V3 is disabled.\
        "
    )

    enabled = data_model.property(
        "enabled", bool,
        array=False, optional=False,
        documentation="\
        If the nodes in the cluster are configured for SNMP.\
        "
    )

    snmp_v3_enabled = data_model.property(
        "snmpV3Enabled", bool,
        array=False, optional=False,
        documentation="\
        If the nodes in the cluster are configured for SNMP v3.\
        "
    )

    usm_users = data_model.property(
        "usmUsers", SnmpV3UsmUser,
        array=True, optional=False,
        documentation="\
        If SNMP v3 is enabled, the values returned is a list of user access\
        parameters for SNMP information from the cluster. This will be\
        returned instead of the \"networks\" parameter.\
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
    :type missing_volumes: int[]

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
    :type nodes: Node[]

    :param pending_nodes: [required]
    :type pending_nodes: PendingNode[]
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
    :type events: EventInfo[]
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


class ListNodeFibreChannelPortInfoResult(data_model.DataObject):
    """
    List of fibre channel port info results grouped by node.

    :param nodes: [required] List of fibre channel port info results grouped by
        node.
    :type nodes: NodeFibreChannelPortInfoResult[]
    """

    nodes = data_model.property(
        "nodes", NodeFibreChannelPortInfoResult,
        array=True, optional=False,
        documentation="\
        List of fibre channel port info results grouped by node.\
        "
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


class CloneMultipleVolumesResult(data_model.DataObject):
    """
    The object returned by the \"clone_multiple_volumes\" API Service call.

    :param async_handle: [required] A value returned from an asynchronous
        method call.
    :type async_handle: int

    :param group_clone_id: [required] Unique ID of the new group clone.
    :type group_clone_id: int

    :param members: [required] List of *volume_ids* for the source and
        destination volume pairs.
    :type members: GroupCloneVolumeMember[]
    """

    async_handle = data_model.property(
        "asyncHandle", int,
        array=False, optional=False,
        documentation="\
        A value returned from an asynchronous method call.\
        "
    )

    group_clone_id = data_model.property(
        "groupCloneID", int,
        array=False, optional=False,
        documentation="\
        Unique ID of the new group clone.\
        "
    )

    members = data_model.property(
        "members", GroupCloneVolumeMember,
        array=True, optional=False,
        documentation="\
        List of *volume_ids* for the source and destination volume pairs.\
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
    :type cluster_version_info: ClusterVersionInfo[]

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
