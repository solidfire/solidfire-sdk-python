#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright &copy; 2014-2016 NetApp, Inc. All Rights Reserved.
#
# DO NOT EDIT THIS CODE BY HAND! It has been generated with jsvcgen.
#
from __future__ import unicode_literals
from __future__ import absolute_import

import logging
from logging import Logger
from solidfire import common
from solidfire.adaptor import ElementServiceAdaptor

from solidfire.common import ServiceBase, ApiVersionExceededError, \
    ApiVersionUnsupportedError
from solidfire.results import AddAccountResult
from solidfire.results import AddClusterAdminResult
from solidfire.results import AddDrivesResult
from solidfire.results import AddLdapClusterAdminResult
from solidfire.results import AddNodesResult
from solidfire.results import AddVirtualNetworkResult
from solidfire.results import AsyncHandleResult
from solidfire.results import ClearClusterFaultsResult
from solidfire.results import CloneMultipleVolumesResult
from solidfire.results import CloneVolumeResult
from solidfire.results import CompleteClusterPairingResult
from solidfire.results import CompleteVolumePairingResult
from solidfire.results import CreateBackupTargetResult
from solidfire.results import CreateGroupSnapshotResult
from solidfire.results import CreateScheduleResult
from solidfire.results import CreateSnapshotResult
from solidfire.results import CreateVolumeAccessGroupResult
from solidfire.results import CreateVolumeResult
from solidfire.results import DeleteGroupSnapshotResult
from solidfire.results import DeleteSnapshotResult
from solidfire.results import DeleteVolumeAccessGroupResult
from solidfire.results import DeleteVolumeResult
from solidfire.results import DisableEncryptionAtRestResult
from solidfire.results import DisableLdapAuthenticationResult
from solidfire.results import DisableSnmpResult
from solidfire.results import EnableEncryptionAtRestResult
from solidfire.results import EnableLdapAuthenticationResult
from solidfire.results import EnableSnmpResult
from solidfire.results import GetAPIResult
from solidfire.results import GetAccountResult
from solidfire.results import GetAsyncResultResult
from solidfire.results import GetBackupTargetResult
from solidfire.results import GetClusterCapacityResult
from solidfire.results import GetClusterConfigResult
from solidfire.results import GetClusterFullThresholdResult
from solidfire.results import GetClusterInfoResult
from solidfire.results import GetClusterStatsResult
from solidfire.results import GetClusterVersionInfoResult
from solidfire.results import GetConfigResult
from solidfire.results import GetCurrentClusterAdminResult
from solidfire.results import GetDriveHardwareInfoResult
from solidfire.results import GetDriveStatsResult
from solidfire.results import GetEfficiencyResult
from solidfire.results import GetLdapConfigurationResult
from solidfire.results import GetLimitsResult
from solidfire.results import GetNetworkConfigResult
from solidfire.results import GetNodeStatsResult
from solidfire.results import GetScheduleResult
from solidfire.results import GetSnmpACLResult
from solidfire.results import GetSnmpInfoResult
from solidfire.results import GetSnmpStateResult
from solidfire.results import GetSnmpTrapInfoResult
from solidfire.results import GetVolumeAccessGroupLunAssignmentsResult
from solidfire.results import GetVolumeEfficiencyResult
from solidfire.results import GetVolumeStatsResult
from solidfire.results import ListAccountsResult
from solidfire.results import ListActiveNodesResult
from solidfire.results import ListActivePairedVolumesResult
from solidfire.results import ListActiveVolumesResult
from solidfire.results import ListAllNodesResult
from solidfire.results import ListBackupTargetsResult
from solidfire.results import ListBulkVolumeJobsResult
from solidfire.results import ListClusterAdminsResult
from solidfire.results import ListClusterFaultsResult
from solidfire.results import ListClusterPairsResult
from solidfire.results import ListDeletedVolumesResult
from solidfire.results import ListDriveHardwareResult
from solidfire.results import ListDrivesResult
from solidfire.results import ListEventsResult
from solidfire.results import ListFibreChannelPortInfoResult
from solidfire.results import ListFibreChannelSessionsResult
from solidfire.results import ListGroupSnapshotsResult
from solidfire.results import ListISCSISessionsResult
from solidfire.results import ListNodeFibreChannelPortInfoResult
from solidfire.results import ListNodeStatsResult
from solidfire.results import ListPendingNodesResult
from solidfire.results import ListSchedulesResult
from solidfire.results import ListSnapshotsResult
from solidfire.results import ListTestsResult
from solidfire.results import ListUtilitiesResult
from solidfire.results import ListVirtualNetworksResult
from solidfire.results import ListVolumeAccessGroupsResult
from solidfire.results import ListVolumeStatsByAccountResult
from solidfire.results import ListVolumeStatsByVolumeAccessGroupResult
from solidfire.results import ListVolumeStatsByVolumeResult
from solidfire.results import ListVolumesForAccountResult
from solidfire.results import ListVolumesResult
from solidfire.results import ModifyAccountResult
from solidfire.results import ModifyBackupTargetResult
from solidfire.results import ModifyClusterAdminResult
from solidfire.results import ModifyClusterFullThresholdResult
from solidfire.results import ModifyGroupSnapshotResult
from solidfire.results import ModifyScheduleResult
from solidfire.results import ModifySnapshotResult
from solidfire.results import ModifyVolumeAccessGroupLunAssignmentsResult
from solidfire.results import ModifyVolumeAccessGroupResult
from solidfire.results import ModifyVolumePairResult
from solidfire.results import ModifyVolumeResult
from solidfire.results import PurgeDeletedVolumeResult
from solidfire.results import RemoveAccountResult
from solidfire.results import RemoveBackupTargetResult
from solidfire.results import RemoveClusterAdminResult
from solidfire.results import RemoveClusterPairResult
from solidfire.results import RemoveNodesResult
from solidfire.results import RemoveVirtualNetworkResult
from solidfire.results import RemoveVolumePairResult
from solidfire.results import ResetDrivesResult
from solidfire.results import RestoreDeletedVolumeResult
from solidfire.results import SetClusterConfigResult
from solidfire.results import SetConfigResult
from solidfire.results import SetNetworkConfigResult
from solidfire.results import SetSnmpACLResult
from solidfire.results import SetSnmpInfoResult
from solidfire.results import SetSnmpTrapInfoResult
from solidfire.results import SnmpSendTestTrapsResult
from solidfire.results import StartBulkVolumeReadResult
from solidfire.results import StartBulkVolumeWriteResult
from solidfire.results import StartClusterPairingResult
from solidfire.results import StartVolumePairingResult
from solidfire.results import TestConnectEnsembleResult
from solidfire.results import TestConnectMvipResult
from solidfire.results import TestConnectSvipResult
from solidfire.results import TestDrivesResult
from solidfire.results import TestLdapAuthenticationResult
from solidfire.results import TestPingResult
from solidfire.results import UpdateBulkVolumeStatusResult

OPTIONAL = None


class Element(ServiceBase):

    """
    The API for controlling a SolidFire cluster.
    """

    def __init__(self, mvip=None, username=None, password=None,
                 api_version=8.0, verify_ssl=True, dispatcher=None):
        """
        Constructor for initializing a connection to an instance of Element OS

        :param mvip: the management IP (IP or hostname)
        :type mvip: str
        :param username: username use to connect to the Element OS instance.
        :type username: str
        :param password: authentication for username
        :type password: str
        :param api_version: specific version of Element OS to connect
        :type api_version: float or str
        :param verify_ssl: disable to avoid ssl connection errors especially
            when using an IP instead of a hostname
        :type verify_ssl: bool
        :param dispatcher: a prebuilt or custom http dispatcher
        :return: a configured and tested instance of Element
        """

        ServiceBase.__init__(self, mvip, username, password, api_version,
                             verify_ssl, dispatcher)

    def add_account(
            self,
            username,
            initiator_secret=OPTIONAL,
            target_secret=OPTIONAL,
            attributes=OPTIONAL,):
        """
        Used to add a new account to the system.
        New volumes can be created under the new account.
        The CHAP settings specified for the account applies to all volumes
        owned by the account.

        :param username: [required] Unique username for this account. (May be 1
            to 64 characters in length).
        :type username: str

        :param initiator_secret: (optional) CHAP secret to use for the
            initiator. Should be 12-16 characters long and impenetrable. The
            CHAP initiator secrets must be unique and cannot be the same as the
            target CHAP secret.

            If not specified, a random secret is created.

        :type initiator_secret: CHAPSecret

        :param target_secret: (optional) CHAP secret to use for the target
            (mutual CHAP authentication). Should be 12-16 characters long and
            impenetrable. The CHAP target secrets must be unique and cannot be
            the same as the initiator CHAP secret.

            If not specified, a random secret is created.

        :type target_secret: CHAPSecret

        :param attributes: (optional) List of Name/Value pairs in JSON object
            format.
        :type attributes: dict

        :returns: a response
        :rtype: AddAccountResult
        """

        params = {
            "username": username,
        }
        if initiator_secret is not None:
            params["initiatorSecret"] = initiator_secret
        if target_secret is not None:
            params["targetSecret"] = target_secret
        if attributes is not None:
            params["attributes"] = attributes

        return self.send_request(
            'AddAccount',
            AddAccountResult,
            params,
        )

    def get_account_by_id(
            self,
            account_id,):
        """
        Returns details about an account, given its AccountID.

        :param account_id: [required] Specifies the account for which details
            are gathered.
        :type account_id: int

        :returns: a response
        :rtype: GetAccountResult
        """

        params = {
            "accountID": account_id,
        }

        return self.send_request(
            'GetAccountByID',
            GetAccountResult,
            params,
        )

    def get_account_by_name(
            self,
            username,):
        """
        Returns details about an account, given its Username.

        :param username: [required] Username for the account.
        :type username: str

        :returns: a response
        :rtype: GetAccountResult
        """

        params = {
            "username": username,
        }

        return self.send_request(
            'GetAccountByName',
            GetAccountResult,
            params,
        )

    def list_accounts(
            self,
            start_account_id=OPTIONAL,
            limit=OPTIONAL,):
        """
        Returns the entire list of accounts, with optional paging support.

        :param start_account_id: (optional) Starting *account_id* to return. If
            no Account exists with this *account_id,* the next Account by
            *account_id* order is used as the start of the list. To page
            through the list, pass the *account_id* of the last Account in the
            previous response + 1
        :type start_account_id: int

        :param limit: (optional) Maximum number of *account_info* objects to
            return.
        :type limit: int

        :returns: a response
        :rtype: ListAccountsResult
        """

        params = {}
        if start_account_id is not None:
            params["startAccountID"] = start_account_id
        if limit is not None:
            params["limit"] = limit

        return self.send_request(
            'ListAccounts',
            ListAccountsResult,
            params,
        )

    def modify_account(
            self,
            account_id,
            username=OPTIONAL,
            status=OPTIONAL,
            initiator_secret=OPTIONAL,
            target_secret=OPTIONAL,
            attributes=OPTIONAL,):
        """
        Used to modify an existing account.
        When locking an account, any existing connections from that account are
        immediately terminated.
        When changing CHAP settings, any existing connections continue to be
        active,
        and the new CHAP values are only used on subsequent connection or
        reconnection.

        :param account_id: [required] *account_id* for the account to modify.
        :type account_id: int

        :param username: (optional) Change the username of the account to this
            value.
        :type username: str

        :param status: (optional) Status of the account.
        :type status: str

        :param initiator_secret: (optional) CHAP secret to use for the
            initiator. Should be 12-16 characters long and impenetrable.
        :type initiator_secret: CHAPSecret

        :param target_secret: (optional) CHAP secret to use for the target
            (mutual CHAP authentication). Should be 12-16 characters long and
            impenetrable.
        :type target_secret: CHAPSecret

        :param attributes: (optional) List of Name/Value pairs in JSON object
            format.
        :type attributes: dict

        :returns: a response
        :rtype: ModifyAccountResult
        """

        params = {
            "accountID": account_id,
        }
        if username is not None:
            params["username"] = username
        if status is not None:
            params["status"] = status
        if initiator_secret is not None:
            params["initiatorSecret"] = initiator_secret
        if target_secret is not None:
            params["targetSecret"] = target_secret
        if attributes is not None:
            params["attributes"] = attributes

        return self.send_request(
            'ModifyAccount',
            ModifyAccountResult,
            params,
        )

    def remove_account(
            self,
            account_id,):
        """
        Used to remove an existing account.
        All Volumes must be deleted and purged on the account before it can be
        removed.
        If volumes on the account are still pending deletion, *remove_account*
        cannot be used until *delete_volume* to delete and purge the volumes.

        :param account_id: [required] *account_id* for the account to remove.
        :type account_id: int

        :returns: a response
        :rtype: RemoveAccountResult
        """

        params = {
            "accountID": account_id,
        }

        return self.send_request(
            'RemoveAccount',
            RemoveAccountResult,
            params,
        )

    def get_account_efficiency(
            self,
            account_id,
            force=OPTIONAL,):
        """
        *get_account_efficiency* is used to retrieve information about a volume
        account. Only the account given as a parameter in this API method is
        used to compute the capacity.

        :param account_id: [required] Specifies the volume account for which
            capacity is computed.
        :type account_id: int

        :param force: (optional)
        :type force: bool

        :returns: a response
        :rtype: GetEfficiencyResult
        """

        params = {
            "accountID": account_id,
        }
        if force is not None:
            params["force"] = force

        return self.send_request(
            'GetAccountEfficiency',
            GetEfficiencyResult,
            params,
        )

    def create_backup_target(
            self,
            name,
            attributes=OPTIONAL,):
        """
        *create_backup_target* allows you to create and store backup target
        information so that you do not need to re-enter it each time a backup
        is created.

        :param name: [required] Name for the backup target.
        :type name: str

        :param attributes: (optional) List of Name/Value pairs in JSON object
            format.
        :type attributes: dict

        :returns: a response
        :rtype: CreateBackupTargetResult
        """

        params = {
            "name": name,
        }
        if attributes is not None:
            params["attributes"] = attributes

        return self.send_request(
            'CreateBackupTarget',
            CreateBackupTargetResult,
            params,
        )

    def get_backup_target(
            self,
            backup_target_id,):
        """
        *get_backup_target* allows you to return information about a specific
        backup target that has been created.

        :param backup_target_id: [required] Unique identifier assigned to the
            backup target.
        :type backup_target_id: int

        :returns: a response
        :rtype: GetBackupTargetResult
        """

        params = {
            "backupTargetID": backup_target_id,
        }

        return self.send_request(
            'GetBackupTarget',
            GetBackupTargetResult,
            params,
        )

    def list_backup_targets(
            self,):
        """
        You can use *list_backup_targets* to retrieve information about all
        backup targets that have been created.

        :returns: a response
        :rtype: ListBackupTargetsResult
        """

        params = {}

        return self.send_request(
            'ListBackupTargets',
            ListBackupTargetsResult,
            params,
        )

    def modify_backup_target(
            self,
            backup_target_id,
            name=OPTIONAL,
            attributes=OPTIONAL,):
        """
        *modify_backup_target* is used to change attributes of a backup target.

        :param backup_target_id: [required] Unique identifier assigned to the
            backup target.
        :type backup_target_id: int

        :param name: (optional) Name for the backup target.
        :type name: str

        :param attributes: (optional) List of Name/Value pairs in JSON object
            format.
        :type attributes: dict

        :returns: a response
        :rtype: ModifyBackupTargetResult
        """

        params = {
            "backupTargetID": backup_target_id,
        }
        if name is not None:
            params["name"] = name
        if attributes is not None:
            params["attributes"] = attributes

        return self.send_request(
            'ModifyBackupTarget',
            ModifyBackupTargetResult,
            params,
        )

    def remove_backup_target(
            self,
            backup_target_id,):
        """
        *remove_backup_target* allows you to delete backup targets.

        :param backup_target_id: [required] Unique target ID of the target to
            remove.
        :type backup_target_id: int

        :returns: a response
        :rtype: RemoveBackupTargetResult
        """

        params = {
            "backupTargetID": backup_target_id,
        }

        return self.send_request(
            'RemoveBackupTarget',
            RemoveBackupTargetResult,
            params,
        )

    def get_cluster_capacity(
            self,):
        """
        Return the high-level capacity measurements for an entire cluster.
        The fields returned from this method can be used to calculate the
        efficiency rates that are displayed in the Element User Interface.

        :returns: a response
        :rtype: GetClusterCapacityResult
        """

        params = {}

        return self.send_request(
            'GetClusterCapacity',
            GetClusterCapacityResult,
            params,
        )

    def get_cluster_info(
            self,):
        """
        Return configuration information about the cluster.

        :returns: a response
        :rtype: GetClusterInfoResult
        """

        params = {}

        return self.send_request(
            'GetClusterInfo',
            GetClusterInfoResult,
            params,
        )

    def get_cluster_version_info(
            self,):
        """
        Return information about the Element software version running on each
        node in the cluster.
        Information about the nodes that are currently in the process of
        upgrading software is also returned.

        :returns: a response
        :rtype: GetClusterVersionInfoResult
        """

        params = {}

        return self.send_request(
            'GetClusterVersionInfo',
            GetClusterVersionInfoResult,
            params,
        )

    def get_limits(
            self,):
        """
        Retrieves the limit values set by the API

        :returns: a response
        :rtype: GetLimitsResult
        """

        params = {}

        return self.send_request(
            'GetLimits',
            GetLimitsResult,
            params,
        )

    def list_events(
            self,
            max_events=OPTIONAL,
            start_event_id=OPTIONAL,
            end_event_id=OPTIONAL,
            event_queue_type=OPTIONAL,):
        """
        *list_events* returns events detected on the cluster, sorted from
        oldest to newest.

        :param max_events: (optional) Specifies the maximum number of events to
            return.
        :type max_events: int

        :param start_event_id: (optional) Identifies the beginning of a range
            of events to return.
        :type start_event_id: int

        :param end_event_id: (optional) Identifies the end of a range of events
            to return.
        :type end_event_id: int

        :param event_queue_type: (optional)
        :type event_queue_type: str

        :returns: a response
        :rtype: ListEventsResult
        """

        params = {}
        if max_events is not None:
            params["maxEvents"] = max_events
        if start_event_id is not None:
            params["startEventID"] = start_event_id
        if end_event_id is not None:
            params["endEventID"] = end_event_id
        if event_queue_type is not None:
            params["eventQueueType"] = event_queue_type

        return self.send_request(
            'ListEvents',
            ListEventsResult,
            params,
        )

    def list_cluster_faults(
            self,
            exceptions=OPTIONAL,
            best_practices=OPTIONAL,
            update=OPTIONAL,
            fault_types=OPTIONAL,):
        """
        *list_cluster_faults* is used to retrieve information about any faults
        detected on the cluster.
        With this method, both current and resolved faults can be retrieved.
        The system caches faults every 30 seconds.

        :param exceptions: (optional)
        :type exceptions: bool

        :param best_practices: (optional) Include faults triggered by
            sub-optimal system configuration. Possible values: true, false
        :type best_practices: bool

        :param update: (optional)
        :type update: bool

        :param fault_types: (optional) Determines the types of faults returned:
            current: List active, unresolved faults. **resolved**: List faults
            that were previously detected and resolved. **all**: (Default) List
            both current and resolved faults. You can see the fault status in
            the 'resolved' field of the Cluster Fault object.
        :type fault_types: str

        :returns: a response
        :rtype: ListClusterFaultsResult
        """

        params = {}
        if exceptions is not None:
            params["exceptions"] = exceptions
        if best_practices is not None:
            params["bestPractices"] = best_practices
        if update is not None:
            params["update"] = update
        if fault_types is not None:
            params["faultTypes"] = fault_types

        return self.send_request(
            'ListClusterFaults',
            ListClusterFaultsResult,
            params,
        )

    def clear_cluster_faults(
            self,
            fault_types=OPTIONAL,):
        """
        *clear_cluster_faults* is used to clear information about both current
        faults that are resolved as well as faults that were previously
        detected and resolved can be cleared.

        :param fault_types: (optional) Determines the types of faults cleared:

            **current**: Faults that are currently detected and have not been
            resolved.

            **resolved**: Faults that were previously detected and resolved.

            **all**: Both current and resolved faults are cleared. The fault
            status can be determined by the \"resolved\" field of the fault
            object.

        :type fault_types: str

        :returns: a response
        :rtype: ClearClusterFaultsResult
        """

        params = {}
        if fault_types is not None:
            params["faultTypes"] = fault_types

        return self.send_request(
            'ClearClusterFaults',
            ClearClusterFaultsResult,
            params,
        )

    def get_cluster_config(
            self,):
        """
        The *get_cluster_config* API method is used to return information about
        the cluster configuration this node uses to communicate with the
        cluster it is a part of.




        **Note**: This method is available only through the per-node API
        endpoint 5.0 or later.

        :returns: a response
        :rtype: GetClusterConfigResult
        """

        params = {}

        return self.send_request(
            'GetClusterConfig',
            GetClusterConfigResult,
            params,
        )

    def get_cluster_full_threshold(
            self,):
        """
        *get_cluster_full_threshold* is used to view the stages set for cluster
        fullness levels. All levels are returned when this method is entered.

        :returns: a response
        :rtype: GetClusterFullThresholdResult
        """

        params = {}

        return self.send_request(
            'GetClusterFullThreshold',
            GetClusterFullThresholdResult,
            params,
        )

    def modify_cluster_full_threshold(
            self,
            stage2_aware_threshold=OPTIONAL,
            stage3_block_threshold_percent=OPTIONAL,
            max_metadata_over_provision_factor=OPTIONAL,):
        """
        *modify_cluster_full_threshold* is used to change the level at which an
        event is generated when the storage cluster approaches the capacity
        utilization requested. The number entered in this setting is used to
        indicate the number of node failures the system is required to recover
        from. For example, on a 10 node cluster, if you want to be alerted when
        the system cannot recover from 3 nodes failures, enter the value of
        \"3\". When this number is reached, a message alert is sent to the
        Event Log in the Cluster Management Console.

        :param stage2_aware_threshold: (optional) Number of nodes worth of
            capacity remaining on the cluster that triggers a notification.
        :type stage2_aware_threshold: int

        :param stage3_block_threshold_percent: (optional) Percent below
            \"Error\" state to raise a cluster \"Warning\" alert.
        :type stage3_block_threshold_percent: int

        :param max_metadata_over_provision_factor: (optional) A value
            representative of the number of times metadata space can be over
            provisioned relative to the amount of space available. For example,
            if there was enough metadata space to store 100 *ti_b* of volumes
            and this number was set to 5, then 500 *ti_b* worth of volumes
            could be created.
        :type max_metadata_over_provision_factor: int

        :returns: a response
        :rtype: ModifyClusterFullThresholdResult
        """

        params = {}
        self._check_param_versions(
            'modify_cluster_full_threshold',
            [
                ("stage3_block_threshold_percent",
                 stage3_block_threshold_percent, 8.0, None),
            ]
        )
        if stage2_aware_threshold is not None:
            params["stage2AwareThreshold"] = stage2_aware_threshold
        if stage3_block_threshold_percent is not None:
            params["stage3BlockThresholdPercent"] = \
                stage3_block_threshold_percent
        if max_metadata_over_provision_factor is not None:
            params["maxMetadataOverProvisionFactor"] = \
                max_metadata_over_provision_factor

        return self.send_request(
            'ModifyClusterFullThreshold',
            ModifyClusterFullThresholdResult,
            params,
        )

    def get_cluster_stats(
            self,):
        """
        *get_cluster_stats* is used to return high-level activity measurements
        for the cluster. Values returned are cumulative from the creation of
        the cluster.

        :returns: a response
        :rtype: GetClusterStatsResult
        """

        params = {}

        return self.send_request(
            'GetClusterStats',
            GetClusterStatsResult,
            params,
        )

    def list_cluster_admins(
            self,):
        """
        *list_cluster_admins* returns the list of all cluster administrators
        for the cluster. There can be several cluster administrators that have
        different levels of permissions. There can be only one primary cluster
        administrator in the system. The primary Cluster Admin is the
        administrator that was created when the cluster was created. LDAP
        administrators can also be created when setting up an LDAP system on
        the cluster.

        :returns: a response
        :rtype: ListClusterAdminsResult
        """

        params = {}

        return self.send_request(
            'ListClusterAdmins',
            ListClusterAdminsResult,
            params,
        )

    def add_cluster_admin(
            self,
            username,
            password,
            access,
            accept_eula=OPTIONAL,
            attributes=OPTIONAL,):
        """
        *add_cluster_admin* adds a new Cluster Admin. A Cluster Admin can be
        used to manage the cluster via the API and management tools. Cluster
        Admins are completely separate and unrelated to standard tenant
        accounts.




        Each Cluster Admin can be restricted to a sub-set of the API. SolidFire
        recommends using multiple Cluster Admins for different users and
        applications. Each Cluster Admin should be given the minimal
        permissions necessary to reduce the potential impact of credential
        compromise.

        :param username: [required] Unique username for this Cluster Admin.
        :type username: str

        :param password: [required] Password used to authenticate this Cluster
            Admin.
        :type password: str

        :param access: [required] Controls which methods this Cluster Admin can
            use. For more details on the levels of access, see \"Access
            Control\" in the Element API Guide.
        :type access: str[]

        :param accept_eula: (optional) Indicate your acceptance of the End User
            License Agreement when creating this cluster admin. To accept the
            EULA, set this parameter to true.
        :type accept_eula: bool

        :param attributes: (optional) List of Name/Value pairs in JSON object
            format.
        :type attributes: dict

        :returns: a response
        :rtype: AddClusterAdminResult
        """

        params = {
            "username": username,
            "password": password,
            "access": access,
        }
        self._check_param_versions(
            'add_cluster_admin',
            [
                ("accept_eula",
                 accept_eula, 9.0, None),
            ]
        )
        if accept_eula is not None:
            params["acceptEula"] = accept_eula
        if attributes is not None:
            params["attributes"] = attributes

        return self.send_request(
            'AddClusterAdmin',
            AddClusterAdminResult,
            params,
        )

    def modify_cluster_admin(
            self,
            cluster_admin_id,
            password=OPTIONAL,
            access=OPTIONAL,
            attributes=OPTIONAL,):
        """
        *modify_cluster_admin* is used to change the settings for a Cluster
        Admin or LDAP Cluster Admin. Access for the administrator Cluster Admin
        account cannot be changed.

        :param cluster_admin_id: [required] *cluster_admin_id* for the Cluster
            Admin or LDAP Cluster Admin to modify.
        :type cluster_admin_id: int

        :param password: (optional) Password used to authenticate this Cluster
            Admin.
        :type password: str

        :param access: (optional) Controls which methods this Cluster Admin can
            use. For more details on the levels of access, see \"Access
            Control\" in the Element API Guide.
        :type access: str[]

        :param attributes: (optional) List of Name/Value pairs in JSON object
            format.
        :type attributes: dict

        :returns: a response
        :rtype: ModifyClusterAdminResult
        """

        params = {
            "clusterAdminID": cluster_admin_id,
        }
        if password is not None:
            params["password"] = password
        if access is not None:
            params["access"] = access
        if attributes is not None:
            params["attributes"] = attributes

        return self.send_request(
            'ModifyClusterAdmin',
            ModifyClusterAdminResult,
            params,
        )

    def remove_cluster_admin(
            self,
            cluster_admin_id,):
        """
        *remove_cluster_admin* is used to remove a Cluster Admin. The \"admin\"
        Cluster Admin cannot be removed.

        :param cluster_admin_id: [required] *cluster_admin_id* for the Cluster
            Admin to remove.
        :type cluster_admin_id: int

        :returns: a response
        :rtype: RemoveClusterAdminResult
        """

        params = {
            "clusterAdminID": cluster_admin_id,
        }

        return self.send_request(
            'RemoveClusterAdmin',
            RemoveClusterAdminResult,
            params,
        )

    def set_cluster_config(
            self,
            cluster,):
        """
        The *set_cluster_config* API method is used to set the configuration
        this node uses to communicate with the cluster it is associated with.
        To see the states in which these objects can be modified see Cluster
        Object on page 109. To display the current cluster interface settings
        for a node, run the *get_cluster_config* API method.




        **Note**: This method is available only through the per-node API
        endpoint 5.0 or later.

        :param cluster: [required] Objects that are changed for the cluster
            interface settings. Only the fields you want changed need to be
            added to this method as objects in the \"cluster\" parameter.
        :type cluster: ClusterConfig

        :returns: a response
        :rtype: SetClusterConfigResult
        """

        params = {
            "cluster": cluster,
        }

        return self.send_request(
            'SetClusterConfig',
            SetClusterConfigResult,
            params,
        )

    def get_snmp_acl(
            self,):
        """
        *get_snmp_acl* is used to return the current SNMP access permissions on
        the cluster nodes.

        :returns: a response
        :rtype: GetSnmpACLResult
        """

        params = {}

        return self.send_request(
            'GetSnmpACL',
            GetSnmpACLResult,
            params,
            since=8.0,
        )

    def set_snmp_acl(
            self,
            networks,
            usm_users,):
        """
        *set_snmp_acl* is used to configure SNMP access permissions on the
        cluster nodes. The values set with this interface apply to all nodes in
        the cluster, and the values that are passed replace, in whole, all
        values set in any previous call to SetSnmpACL. Also note that the
        values set with this interface replace all \"network\" or
        *\"usm_users\"* values set with the older SetSnmpInfo.

        :param networks: [required] List of networks and what type of access
            they have to the SNMP servers running on the cluster nodes. See
            SNMP Network Object for possible \"networks\" values. REQUIRED if
            SNMP *v_* is disabled.
        :type networks: SnmpNetwork[]

        :param usm_users: [required] List of users and the type of access they
            have to the SNMP servers running on the cluster nodes. REQUIRED if
            SNMP v3 is enabled.
        :type usm_users: SnmpV3UsmUser[]

        :returns: a response
        :rtype: SetSnmpACLResult
        """

        params = {
            "networks": networks,
            "usmUsers": usm_users,
        }

        return self.send_request(
            'SetSnmpACL',
            SetSnmpACLResult,
            params,
            since=8.0,
        )

    def get_snmp_trap_info(
            self,):
        """
        *get_snmp_trap_info* is used to return current SNMP trap configuration
        information.

        :returns: a response
        :rtype: GetSnmpTrapInfoResult
        """

        params = {}

        return self.send_request(
            'GetSnmpTrapInfo',
            GetSnmpTrapInfoResult,
            params,
        )

    def set_snmp_trap_info(
            self,
            trap_recipients,
            cluster_fault_traps_enabled,
            cluster_fault_resolved_traps_enabled,
            cluster_event_traps_enabled,):
        """
        *set_snmp_trap_info* is used to enable and disable the generation of
        SolidFire SNMP notifications (traps) and to specify the set of network
        host computers that are to receive the notifications. The values passed
        with each *set_snmp_trap_info* method replaces all values set in any
        previous method to SetSnmpTrapInfo.

        :param trap_recipients: [required] List of hosts that are to receive
            the traps generated by the Cluster Master. At least one object is
            required if any one of the trap types is enabled.
        :type trap_recipients: SnmpTrapRecipient[]

        :param cluster_fault_traps_enabled: [required] If \"true\", when a
            cluster fault is logged a corresponding
            *solid_fire_cluster_fault_notification* is sent to the configured
            list of trap recipients.
        :type cluster_fault_traps_enabled: bool

        :param cluster_fault_resolved_traps_enabled: [required] If \"true\",
            when a cluster fault is logged a corresponding
            *solid_fire_cluster_fault_resolved_notification* is sent to the
            configured list of trap recipients.
        :type cluster_fault_resolved_traps_enabled: bool

        :param cluster_event_traps_enabled: [required] If \"true\", when a
            cluster fault is logged a corresponding
            *solid_fire_cluster_event_notification* is sent to the configured
            list of trap recipients.
        :type cluster_event_traps_enabled: bool

        :returns: a response
        :rtype: SetSnmpTrapInfoResult
        """

        params = {
            "trapRecipients": trap_recipients,
            "clusterFaultTrapsEnabled": cluster_fault_traps_enabled,
            "clusterFaultResolvedTrapsEnabled":
                cluster_fault_resolved_traps_enabled,
            "clusterEventTrapsEnabled": cluster_event_traps_enabled,
        }

        return self.send_request(
            'SetSnmpTrapInfo',
            SetSnmpTrapInfoResult,
            params,
        )

    def enable_snmp(
            self,
            snmp_v3_enabled,):
        """
        *enable_snmp* is used to enable SNMP on the cluster nodes. The values
        set with this interface apply to all nodes in the cluster, and the
        values that are passed replace, in whole, all values set in any
        previous call to EnableSnmp.

        :param snmp_v3_enabled: [required] If set to \"true\", then SNMP v3 is
            enabled on each node in the cluster. If set to \"false\", then SNMP
            v2 is enabled.
        :type snmp_v3_enabled: bool

        :returns: a response
        :rtype: EnableSnmpResult
        """

        params = {
            "snmpV3Enabled": snmp_v3_enabled,
        }

        return self.send_request(
            'EnableSnmp',
            EnableSnmpResult,
            params,
        )

    def disable_snmp(
            self,):
        """
        *disable_snmp* is used to disable SNMP on the cluster nodes.

        :returns: a response
        :rtype: DisableSnmpResult
        """

        params = {}

        return self.send_request(
            'DisableSnmp',
            DisableSnmpResult,
            params,
        )

    def get_snmp_info(
            self,):
        """
        *get_snmp_info* is used to return the current simple network management
        protocol (SNMP) configuration information.




        **Note**: *get_snmp_info* will be available for Element OS 8 and prior
        releases. It will be deprecated after Element OS 8. There are two new
        SNMP API methods that you should migrate over to. They are
        *get_snmp_state* and GetSnmpACL. Please see details in this document
        for their descriptions and usage.

        :returns: a response
        :rtype: GetSnmpInfoResult
        """

        params = {}

        return self.send_request(
            'GetSnmpInfo',
            GetSnmpInfoResult,
            params,
        )

    def set_snmp_info(
            self,
            networks=OPTIONAL,
            enabled=OPTIONAL,
            snmp_v3_enabled=OPTIONAL,
            usm_users=OPTIONAL,):
        """
        *set_snmp_info* is used to configure SNMP v2 and v3 on the cluster
        nodes. The values set with this interface apply to all nodes in the
        cluster, and the values that are passed replace, in whole, all values
        set in any previous call to SetSnmpInfo.




        **Note**: *enable_snmp* and *set_snmp_acl* methods can be used to
        accomplish the same results as SetSnmpInfo. *set_snmp_info* will no
        longer be available after the Element 8 release. Please use
        *enable_snmp* and *set_snmp_acl* in the future.

        :param networks: (optional) List of networks and what type of access
            they have to the SNMP servers running on the cluster nodes. See
            SNMP Network Object for possible \"networks\" values. SNMP v2 only.
        :type networks: SnmpNetwork[]

        :param enabled: (optional) If set to \"true\", then SNMP is enabled on
            each node in the cluster.
        :type enabled: bool

        :param snmp_v3_enabled: (optional) If set to \"true\", then SNMP v3 is
            enabled on each node in the cluster.
        :type snmp_v3_enabled: bool

        :param usm_users: (optional) If SNMP v3 is enabled, this value must be
            passed in place of the \"networks\" parameter. SNMP v3 only.
        :type usm_users: SnmpV3UsmUser[]

        :returns: a response
        :rtype: SetSnmpInfoResult
        """

        params = {}
        if networks is not None:
            params["networks"] = networks
        if enabled is not None:
            params["enabled"] = enabled
        if snmp_v3_enabled is not None:
            params["snmpV3Enabled"] = snmp_v3_enabled
        if usm_users is not None:
            params["usmUsers"] = usm_users

        return self.send_request(
            'SetSnmpInfo',
            SetSnmpInfoResult,
            params,
        )

    def get_snmp_state(
            self,):
        """
        *get_snmp_state* is used to return the current state of the SNMP
        feature.




        **Note**: *get_snmp_state* is new for Element OS 8. Please use this
        method and *set_snmp_acl* to migrate your SNMP functionality in the
        future.

        :returns: a response
        :rtype: GetSnmpStateResult
        """

        params = {}

        return self.send_request(
            'GetSnmpState',
            GetSnmpStateResult,
            params,
            since=8.0,
        )

    def get_api(
            self,):
        """
        Retrieves the current version of the API and a list of all supported
        versions.

        :returns: a response
        :rtype: GetAPIResult
        """

        params = {}

        return self.send_request(
            'GetAPI',
            GetAPIResult,
            params,
        )

    def get_current_cluster_admin(
            self,):
        """
        *get_current_cluster_admin* returns information for the current primary
        cluster administrator. The primary Cluster Admin was ncreated when the
        cluster was created.

        :returns: a response
        :rtype: GetCurrentClusterAdminResult
        """

        params = {}

        return self.send_request(
            'GetCurrentClusterAdmin',
            GetCurrentClusterAdminResult,
            params,
        )

    def enable_encryption_at_rest(
            self,):
        """
        The *enable_encryption_at_rest* method is used to enable the Advanced
        Encryption Standard (AES) 256-bit encryption at rest on the cluster so
        that the cluster can manage the encryption key used for the drives on
        each node. This feature is not enabled by default. Enabling this
        operation allows the cluster to automatically manage encryption keys
        internally for the drives on each node in the cluster. Nodes do not
        store the keys to unlock drives and the keys are never passed over the
        network. Two nodes participating in a cluster are required to access
        the key to disable encryption on a drive. The encryption management
        does not affect performance or efficiency on the cluster. If an
        encryption-enabled drive or node is removed from the cluster with the
        API, all data is secure erased and any data left on the drive cannot be
        read or accessed.
        Enabling or disabling encryption should be performed when the cluster
        is running and in a healthy state. Encryption can be enabled or
        disabled at your discretion and can be performed as often as you need.


            **Note**: This process is asynchronous and returns a response
        before encryption is enabled. The *get_cluster_info* method can be used
        to poll the system to see when the process has completed.


        :returns: a response
        :rtype: EnableEncryptionAtRestResult
        """

        params = {}

        return self.send_request(
            'EnableEncryptionAtRest',
            EnableEncryptionAtRestResult,
            params,
        )

    def disable_encryption_at_rest(
            self,):
        """
        The *disable_encryption_at_rest* method enables you to remove the
        encryption that was previously applied to the cluster using the
        *enable_encryption_at_rest* method.
        Enabling or disabling encryption should be performed when the cluster
        is running and in a healthy state. Encryption can be enabled or
        disabled at your discretion and can be performed as often as you need.


            **Note**: This process is asynchronous and returns a response
        before encryption is disabled. The *get_cluster_info* method can be
        used to poll the system to see when the process has completed.


        :returns: a response
        :rtype: DisableEncryptionAtRestResult
        """

        params = {}

        return self.send_request(
            'DisableEncryptionAtRest',
            DisableEncryptionAtRestResult,
            params,
        )

    def snmp_send_test_traps(
            self,):
        """
        *snmp_send_test_traps* enables you to test SNMP functionality for a
        cluster. This method instructs the cluster to send test SNMP traps to
        the currently configured SNMP manager.

        :returns: a response
        :rtype: SnmpSendTestTrapsResult
        """

        params = {}

        return self.send_request(
            'SnmpSendTestTraps',
            SnmpSendTestTrapsResult,
            params,
        )

    def get_async_result(
            self,
            async_handle,):
        """
        Used to retrieve the result of asynchronous method calls.
        Some method calls are long running and do not complete when the initial
        response is sent.
        To obtain the result of the method call, polling with
        *get_async_result* is required.




        *get_async_result* returns the overall status of the operation (in
        progress, completed, or error) in a standard fashion,
        but the actual data returned for the operation depends on the original
        method call and the return data is documented with each method.




        The result for a completed asynchronous method call can only be
        retrieved once.
        Once the final result has been returned, later attempts returns an
        error.

        :param async_handle: [required] A value that was returned from the
            original asynchronous method call.
        :type async_handle: int

        :returns: a response
        :rtype: GetAsyncResultResult
        """

        params = {
            "asyncHandle": async_handle,
        }

        return self.send_request(
            'GetAsyncResult',
            GetAsyncResultResult,
            params,
        )

    def add_drives(
            self,
            drives,):
        """
        *add_drives* is used to add one or more available drives to the cluster
        enabling the drives to host a portion of the cluster&#39;s data.
        When you add a node to the cluster or install new drives in an existing
        node, the new drives are marked as \"available\" and must be added via
        *add_drives* before they can be utilized.
        Use the *\"list_drives\"* method to display drives that are
        \"available\" to be added.
        When you add multiple drives, it is more efficient to add them in a
        single *\"add_drives\"* method call rather than multiple individual
        methods with a single drive each.
        This reduces the amount of data balancing that must occur to stabilize
        the storage load on the cluster.




        When you add a drive, the system automatically determines the \"type\"
        of drive it should be.




        The method returns immediately. However, it may take some time for the
        data in the cluster to be rebalanced using the newly added drives.
        As the new drive(s) are syncing on the system, you can use the
        *\"list_sync_jobs\"* method to see how the drive(s) are being
        rebalanced and the progress of adding the new drive.

        :param drives: [required] List of drives to add to the cluster.
        :type drives: NewDrive[]

        :returns: a response
        :rtype: AddDrivesResult
        """

        params = {
            "drives": drives,
        }

        return self.send_request(
            'AddDrives',
            AddDrivesResult,
            params,
        )

    def list_drives(
            self,):
        """
        *list_drives* allows you to retrieve the list of the drives that exist
        in the cluster&#39;s active nodes.
        This method returns drives that have been added as volume metadata or
        block drives as well as drives that have not been added and are
        available.

        :returns: a response
        :rtype: ListDrivesResult
        """

        params = {}

        return self.send_request(
            'ListDrives',
            ListDrivesResult,
            params,
        )

    def get_drive_hardware_info(
            self,
            drive_id,):
        """
        *get_drive_hardware_info* returns all the hardware info for the given
        drive. This generally includes manufacturers, vendors, versions, and
        other associated hardware identification information.

        :param drive_id: [required] *drive_id* for the drive information
            requested. *drive_ids* can be obtained via the \"ListDrives\"
            method.
        :type drive_id: int

        :returns: a response
        :rtype: GetDriveHardwareInfoResult
        """

        params = {
            "driveID": drive_id,
        }

        return self.send_request(
            'GetDriveHardwareInfo',
            GetDriveHardwareInfoResult,
            params,
        )

    def list_drive_hardware(
            self,
            force,):
        """
        *list_drive_hardware* returns all the drives connected to a node. Use
        this method on the cluster to return drive hardware information for all
        the drives on all nodes.

        :param force: [required] This must be set to true in order to retrieve
            the drive hardware stats from the cluster.
        :type force: bool

        :returns: a response
        :rtype: ListDriveHardwareResult
        """

        params = {
            "force": force,
        }

        return self.send_request(
            'ListDriveHardware',
            ListDriveHardwareResult,
            params,
        )

    def reset_drives(
            self,
            drives,
            force,):
        """
        *reset_drives* is used to pro-actively initialize drives and remove all
        data currently residing on the drive. The drive can then be reused in
        an existing node or used in an upgraded SolidFire node. This method
        requires the force=true parameter to be included in the method call.




        **Note**: This method is available only through the per-node API
        endpoint 5.0 or later.

        :param drives: [required] List of device names (not driveIDs) to reset.
        :type drives: str

        :param force: [required] The \"force\" parameter must be included on
            this method to successfully reset a drive.
        :type force: bool

        :returns: a response
        :rtype: ResetDrivesResult
        """

        params = {
            "drives": drives,
            "force": force,
        }

        return self.send_request(
            'ResetDrives',
            ResetDrivesResult,
            params,
        )

    def test_drives(
            self,
            force,
            minutes=OPTIONAL,):
        """
        The *test_drives* API method is used to run a hardware validation on
        all the drives on the node. Hardware failures on the drives are
        detected if present and they are reported in the results of the
        validation tests.




        **Note**: This test takes approximately 10 minutes.




        **Note**: This method is available only through the per-node API
        endpoint 5.0 or later.

        :param force: [required] The \"force\" parameter must be included on
            this method to successfully test the drives on the node.
        :type force: bool

        :param minutes: (optional) The number of minutes to run the test can be
            specified.
        :type minutes: int

        :returns: a response
        :rtype: TestDrivesResult
        """

        params = {
            "force": force,
        }
        if minutes is not None:
            params["minutes"] = minutes

        return self.send_request(
            'TestDrives',
            TestDrivesResult,
            params,
        )

    def get_drive_stats(
            self,
            drive_id,):
        """
        *get_drive_stats* return high-level activity measurements for a single
        drive. Values are cumulative from the addition of the drive to the
        cluster. Some values are specific to Block Drives. Statistical data may
        not be returned for both block and metadata drives when running this
        method.
        For more information on which drive type returns which data, see
        Response Example (Block Drive) and Response Example (Volume Metadata
        Drive) in the SolidFire API guide.

        :param drive_id: [required] Specifies the drive for which statistics
            are gathered.
        :type drive_id: int

        :returns: a response
        :rtype: GetDriveStatsResult
        """

        params = {
            "driveID": drive_id,
        }

        return self.send_request(
            'GetDriveStats',
            GetDriveStatsResult,
            params,
        )

    def secure_erase_drives(
            self,
            drives,):
        """
        *secure_erase_drives* is used to remove any residual data from drives
        that have a status of \"available.\" For example, when replacing a
        drive at its end-of-life that contained sensitive data.
        It uses a Security Erase Unit command to write a predetermined pattern
        to the drive and resets the encryption key on the drive. The method may
        take up to two minutes to complete, so it is an asynchronous method.
        The *get_async_result* method can be used to check on the status of the
        secure erase operation.




        Use the *\"list_drives\"* method to obtain the *drive_ids* for the
        drives you want to secure erase.

        :param drives: [required] List of *drive_ids* to secure erase.
        :type drives: int[]

        :returns: a response
        :rtype: AsyncHandleResult
        """

        params = {
            "drives": drives,
        }

        return self.send_request(
            'SecureEraseDrives',
            AsyncHandleResult,
            params,
        )

    def remove_drives(
            self,
            drives,):
        """
        You can use *remove_drives* to proactively remove drives that are part
        of the cluster.
        You may want to use this method when reducing cluster capacity or
        preparing to replace drives nearing the end of their service life.
        Any data on the drives is removed and migrated to other drives in the
        cluster before the drive is removed from the cluster. This is an
        asynchronous method.
        Depending on the total capacity of the drives being removed, it may
        take several minutes to migrate all of the data.
        Use the *\"get_async_result\"* method to check the status of the remove
        operation.




        When removing multiple drives, use a single *\"remove_drives\"* method
        call rather than multiple individual methods with a single drive each.
        This reduces the amount of data balancing that must occur to even
        stabilize the storage load on the cluster.




        You can also remove drives with a \"failed\" status using
        \"RemoveDrives\".
        When you remove a drive with a \"failed\" status it is not returned to
        an \"available\" or \"active\" status.
        The drive is unavailable for use in the cluster.




        Use the *\"list_drives\"* method to obtain the *drive_ids* for the
        drives you want to remove.

        :param drives: [required] List of *drive_ids* to remove from the
            cluster.
        :type drives: int[]

        :returns: a response
        :rtype: AsyncHandleResult
        """

        params = {
            "drives": drives,
        }

        return self.send_request(
            'RemoveDrives',
            AsyncHandleResult,
            params,
        )

    def list_fibre_channel_port_info(
            self,):
        """
        The *list_fibre_channel_port_info* is used to return information about
        the Fibre Channel ports. The API method is intended for use on
        individual nodes; userid and password is required for access to
        individual Fibre Channel nodes. However, this method can be used on the
        cluster if the force=true parameter is included in the method call.
        When used on the cluster, all Fibre Channel interfaces are listed.

        :returns: a response
        :rtype: ListFibreChannelPortInfoResult
        """

        params = {}

        return self.send_request(
            'ListFibreChannelPortInfo',
            ListFibreChannelPortInfoResult,
            params,
            since=8.0,
        )

    def list_node_fibre_channel_port_info(
            self,
            force=OPTIONAL,):
        """
        The *list_node_fibre_channel_port_info* is used to return information
        about the Fibre Channel ports. The API method is intended for use on
        individual nodes; userid and password is required for access to
        individual Fibre Channel nodes. However, this method can be used on the
        cluster if the force=true parameter is included in the method call.
        When used on the cluster, all Fibre Channel interfaces are listed.

        :param force: (optional) Specify force=true to call method on all
            member nodes of the cluster.
        :type force: bool

        :returns: a response
        :rtype: ListNodeFibreChannelPortInfoResult
        """

        params = {}
        if force is not None:
            params["force"] = force

        return self.send_request(
            'ListNodeFibreChannelPortInfo',
            ListNodeFibreChannelPortInfoResult,
            params,
            since=7.0,
        )

    def list_fibre_channel_sessions(
            self,):
        """
        The *list_fibre_channel_sessions* is used to return information about
        the active Fibre Channel sessions on a cluster.

        :returns: a response
        :rtype: ListFibreChannelSessionsResult
        """

        params = {}

        return self.send_request(
            'ListFibreChannelSessions',
            ListFibreChannelSessionsResult,
            params,
            since=7.0,
        )

    def add_ldap_cluster_admin(
            self,
            username,
            access,
            accept_eula=OPTIONAL,
            attributes=OPTIONAL,):
        """
        *add_ldap_cluster_admin* is used to add a new LDAP Cluster Admin. An
        LDAP Cluster Admin can be used to manage the cluster via the API and
        management tools. LDAP Cluster Admins are completely separate and
        unrelated to standard tenant accounts.




        An LDAP group that has been defined in Active Directory can also be
        added using this API method. The access level that is given to the
        group will be passed to the individual users in the LDAP group.

        :param username: [required] The distinguished user name for the new
            LDAP cluster admin.
        :type username: str

        :param access: [required] Controls which methods this Cluster Admin can
            use. For more details on the levels of access, see the Access
            Control appendix in the SolidFire API Reference.
        :type access: str[]

        :param accept_eula: (optional) Indicate your acceptance of the End User
            License Agreement when creating this cluster admin. To accept the
            EULA, set this parameter to true.
        :type accept_eula: bool

        :param attributes: (optional) List of Name/Value pairs in JSON object
            format.
        :type attributes: dict

        :returns: a response
        :rtype: AddLdapClusterAdminResult
        """

        params = {
            "username": username,
            "access": access,
        }
        self._check_param_versions(
            'add_ldap_cluster_admin',
            [
                ("accept_eula",
                 accept_eula, 9.0, None),
            ]
        )
        if accept_eula is not None:
            params["acceptEula"] = accept_eula
        if attributes is not None:
            params["attributes"] = attributes

        return self.send_request(
            'AddLdapClusterAdmin',
            AddLdapClusterAdminResult,
            params,
            since=8.0,
        )

    def test_ldap_authentication(
            self,
            username,
            password,
            ldap_configuration=OPTIONAL,):
        """
        The *test_ldap_authentication* is used to verify the currently enabled
        LDAP authentication configuration settings are correct. If the
        configuration settings are correct, the API call returns a list of the
        groups the tested user is a member of.

        :param username: [required] The username to be tested.
        :type username: str

        :param password: [required] The password for the username to be tester.
        :type password: str

        :param ldap_configuration: (optional) An *ldap_configuration* object to
            be tested. If this parameter is provided, the API call will test
            the provided configuration even if LDAP authentication is currently
            disabled.
        :type ldap_configuration: LdapConfiguration

        :returns: a response
        :rtype: TestLdapAuthenticationResult
        """

        params = {
            "username": username,
            "password": password,
        }
        if ldap_configuration is not None:
            params["ldapConfiguration"] = ldap_configuration

        return self.send_request(
            'TestLdapAuthentication',
            TestLdapAuthenticationResult,
            params,
            since=8.0,
        )

    def get_ldap_configuration(
            self,):
        """
        The *get_ldap_configuration* is used to get the LDAP configuration
        currently active on the cluster.

        :returns: a response
        :rtype: GetLdapConfigurationResult
        """

        params = {}

        return self.send_request(
            'GetLdapConfiguration',
            GetLdapConfigurationResult,
            params,
            since=8.0,
        )

    def enable_ldap_authentication(
            self,
            server_uris,
            auth_type=OPTIONAL,
            group_search_base_dn=OPTIONAL,
            group_search_custom_filter=OPTIONAL,
            group_search_type=OPTIONAL,
            search_bind_dn=OPTIONAL,
            search_bind_password=OPTIONAL,
            user_dntemplate=OPTIONAL,
            user_search_base_dn=OPTIONAL,
            user_search_filter=OPTIONAL,):
        """
        The *enable_ldap_authentication* method is used to configure an LDAP
        server connection to use for LDAP authentication to a SolidFire
        cluster. Users that are members on the LDAP server can then log in to a
        SolidFire storage system using their LDAP authentication userid and
        password.

        :param server_uris: [required] A list of LDAP server *uris* (examples:
            \"ldap://1.2.3.4\" and ldaps://1.2.3.4:123\")
        :type server_uris: str[]

        :param auth_type: (optional) Identifies which user authentcation method
            will be used.

            Must be one of the following:

            **DirectBind**

            **SearchAndBind** (default)

        :type auth_type: str

        :param group_search_base_dn: (optional) The base DN of the tree to
            start the group search (will do a subtree search from here).
        :type group_search_base_dn: str

        :param group_search_custom_filter: (optional) REQUIRED for
            *custom_filter*

            For use with the *custom_filter* search type, an LDAP filter to use
            to return the *dns* of a user&#39;s groups.

            The string can have placeholder text of %USERNAME% and %USERDN% to
            be replaced with their username and full *user_dn* as needed.

        :type group_search_custom_filter: str

        :param group_search_type: (optional) Controls the default group search
            filter used, can be one of the following:

            **NoGroups**: No group support.

            **ActiveDirectory**: (default) Nested membership of all of a
            user&#39;s AD groups.

            **MemberDN**: *member_dn* style groups (single-level).

        :type group_search_type: str

        :param search_bind_dn: (optional) REQUIRED for *search_and_bind*

            A fully qualified DN to log in with to perform an LDAP search for
            the user (needs read access to the LDAP directory).

        :type search_bind_dn: str

        :param search_bind_password: (optional) REQUIRED for *search_and_bind*

            The password for the *search_bind_dn* account used for searching.

        :type search_bind_password: str

        :param user_dntemplate: (optional) REQUIRED for *direct_bind*

            A string that is used to form a fully qualified user DN.

            The string should have the placeholder text \"%USERNAME%\" which
            will be replaced with the username of the authenticating user.

        :type user_dntemplate: str

        :param user_search_base_dn: (optional) REQUIRED for *search_and_bind*
            The base DN of the tree used to start the search (will do a subtree
            search from here).
        :type user_search_base_dn: str

        :param user_search_filter: (optional) REQUIRED for SearchAndBind.

            The LDAP filter to use.

            The string should have the placeholder text \"%USERNAME%\" which
            will be replaced with the username of the authenticating user.

            Example: (&(objectClass=person) (sAMAccountName=%USERNAME%)) will
            use the *s_amaccount_name* field in Active Directory to match the
            nusername entered at cluster login.

        :type user_search_filter: str

        :returns: a response
        :rtype: EnableLdapAuthenticationResult
        """

        params = {
            "serverURIs": server_uris,
        }
        if auth_type is not None:
            params["authType"] = auth_type
        if group_search_base_dn is not None:
            params["groupSearchBaseDN"] = group_search_base_dn
        if group_search_custom_filter is not None:
            params["groupSearchCustomFilter"] = group_search_custom_filter
        if group_search_type is not None:
            params["groupSearchType"] = group_search_type
        if search_bind_dn is not None:
            params["searchBindDN"] = search_bind_dn
        if search_bind_password is not None:
            params["searchBindPassword"] = search_bind_password
        if user_dntemplate is not None:
            params["userDNTemplate"] = user_dntemplate
        if user_search_base_dn is not None:
            params["userSearchBaseDN"] = user_search_base_dn
        if user_search_filter is not None:
            params["userSearchFilter"] = user_search_filter

        return self.send_request(
            'EnableLdapAuthentication',
            EnableLdapAuthenticationResult,
            params,
            since=8.0,
        )

    def disable_ldap_authentication(
            self,):
        """
        The *disable_ldap_authentication* method is used disable LDAP
        authentication and remove all LDAP configuration settings. This call
        will not remove any configured cluster admin accounts (user or group).
        However, those cluster admin accounts will no longer be able to log in.

        :returns: a response
        :rtype: DisableLdapAuthenticationResult
        """

        params = {}

        return self.send_request(
            'DisableLdapAuthentication',
            DisableLdapAuthenticationResult,
            params,
            since=8.0,
        )

    def list_active_nodes(
            self,):
        """
        *list_active_nodes* returns the list of currently active nodes that are
        in the cluster.

        :returns: a response
        :rtype: ListActiveNodesResult
        """

        params = {}

        return self.send_request(
            'ListActiveNodes',
            ListActiveNodesResult,
            params,
        )

    def list_all_nodes(
            self,):
        """
        *list_all_nodes* enables you to retrieve a list of active and pending
        nodes in the cluster.

        :returns: a response
        :rtype: ListAllNodesResult
        """

        params = {}

        return self.send_request(
            'ListAllNodes',
            ListAllNodesResult,
            params,
        )

    def list_pending_nodes(
            self,):
        """
        Gets the list of pending nodes.
        Pending nodes are running and configured to join the cluster, but have
        not been added via the *add_nodes* method.

        :returns: a response
        :rtype: ListPendingNodesResult
        """

        params = {}

        return self.send_request(
            'ListPendingNodes',
            ListPendingNodesResult,
            params,
        )

    def add_nodes(
            self,
            pending_nodes,):
        """
        *add_nodes* is used to add one or more new nodes to the cluster. When a
        node is not configured and starts up for the first time you are
        prompted to configure the node. Once a node is configured it is
        registered as a \"pending node\" with the cluster.




        Adding a node to a cluster that has been set up for virtual networking
        will require a sufficient number of virtual storage IP addresses to
        allocate a virtual IP to the new node. If there are no virtual IP
        addresses available for the new node, the *add_node* operation will not
        complete successfully. Use the *\"modify_virtual_network\"* method to
        add more storage IP addresses to your virtual network.




        The software version on each node in a cluster must be compatible. Run
        the *\"list_all_nodes\"* API to see what versions of software are
        currently running on the cluster nodes. For an explanation of software
        version compatibility, see *\"node* Versioning and Compatibility\" in
        the Element API guide.




        Once a node has been added, the drives on the node are made available
        and can then be added via the *\"add_drives\"* method to increase the
        storage capacity of the cluster.




        **Note**: It may take several seconds after adding a new Node for it to
        start up and register the drives as being available.

        :param pending_nodes: [required] List of *pending_node_ids* for the
            Nodes to be added. You can obtain the list of Pending Nodes via the
            *list_pending_nodes* method.
        :type pending_nodes: int[]

        :returns: a response
        :rtype: AddNodesResult
        """

        params = {
            "pendingNodes": pending_nodes,
        }

        return self.send_request(
            'AddNodes',
            AddNodesResult,
            params,
        )

    def remove_nodes(
            self,
            nodes,):
        """
        *remove_nodes* is used to remove one or more nodes that should no
        longer participate in the cluster. Before removing a node, all drives
        it contains must first be removed with *\"remove_drives\"* method. A
        node cannot be removed until the *remove_drives* process has completed
        and all data has been migrated away from the node.




        Once removed, a node registers itself as a pending node and can be
        added again, or shut down which removes it from the *\"pending* Node\"
        list.

        :param nodes: [required] List of *node_ids* for the nodes to be
            removed.
        :type nodes: int[]

        :returns: a response
        :rtype: RemoveNodesResult
        """

        params = {
            "nodes": nodes,
        }

        return self.send_request(
            'RemoveNodes',
            RemoveNodesResult,
            params,
        )

    def get_network_config(
            self,):
        """
        The *get_network_config* API method is used to display the network
        configuration information for a node.




        **Note**: This method is available only through the per-node API
        endpoint 5.0 or later.

        :returns: a response
        :rtype: GetNetworkConfigResult
        """

        params = {}

        return self.send_request(
            'GetNetworkConfig',
            GetNetworkConfigResult,
            params,
        )

    def set_config(
            self,
            config,):
        """
        The *set_config* API method is used to set all the configuration
        information for the node. This includes the same information available
        via calls to *set_cluster_config* and *set_network_config* in one API
        method.




        **Warning!** Changing the 'bond-mode' on a node can cause a temporary
        loss of network connectivity. Caution should be taken when using this
        method.




        **Note**: This method is available only through the per-node API
        endpoint 5.0 or later.

        :param config: [required] Objects that you want changed for the cluster
            interface settings.
        :type config: Config

        :returns: a response
        :rtype: SetConfigResult
        """

        params = {
            "config": config,
        }

        return self.send_request(
            'SetConfig',
            SetConfigResult,
            params,
        )

    def set_network_config(
            self,
            network,):
        """
        The *\"set_network_config\"* method is used to set the network
        configuration for a node. To see the states in which these objects can
        be modified, see *\"network* Object for 1G and 10G Interfaces\" on page
        109 of the Element API. To display the current network settings for a
        node, run the *\"get_network_config\"* method.




        **WARNING!** Changing the \"bond-mode\" on a node can cause a temporary
        loss of network connectivity. Caution should be taken when using this
        method.




        **Note**: This method is available only through the per-node API
        endpoint 5.0 or later.

        :param network: [required] Objects that will be changed for the node
            network settings.
        :type network: Network

        :returns: a response
        :rtype: SetNetworkConfigResult
        """

        params = {
            "network": network,
        }

        return self.send_request(
            'SetNetworkConfig',
            SetNetworkConfigResult,
            params,
        )

    def get_config(
            self,):
        """
        The *get_config* API method is used to retrieve all the configuration
        information for the node. This one API method includes the same
        information available in both *\"get_cluster_config\"* and
        *\"get_network_config\"* methods.




        **Note**: This method is available only through the per-node API
        endpoint 5.0 or later.

        :returns: a response
        :rtype: GetConfigResult
        """

        params = {}

        return self.send_request(
            'GetConfig',
            GetConfigResult,
            params,
        )

    def get_node_stats(
            self,
            node_id,):
        """
        *get_node_stats* is used to return the high-level activity measurements
        for a single node.

        :param node_id: [required] Specifies the node for which statistics are
            gathered.
        :type node_id: int

        :returns: a response
        :rtype: GetNodeStatsResult
        """

        params = {
            "nodeID": node_id,
        }

        since = None
        deprecated = None

        return ElementServiceAdaptor.get_node_stats(self, params,
                                                    since, deprecated)

    def list_node_stats(
            self,):
        """
        *list_node_stats* is used to return the high-level activity
        measurements for all nodes in a cluster.

        :returns: a response
        :rtype: ListNodeStatsResult
        """

        params = {}

        return self.send_request(
            'ListNodeStats',
            ListNodeStatsResult,
            params,
        )

    def list_cluster_pairs(
            self,):
        """
        *list_cluster_pairs* is used to list all of the clusters a cluster is
        paired with.
        This method returns information about active and pending cluster
        pairings, such as statistics about the current pairing as well as the
        connectivity and latency (in milliseconds) of the cluster pairing.

        :returns: a response
        :rtype: ListClusterPairsResult
        """

        params = {}

        return self.send_request(
            'ListClusterPairs',
            ListClusterPairsResult,
            params,
        )

    def list_active_paired_volumes(
            self,):
        """
        *list_active_paired_volumes* is used to list all of the active volumes
        paired with a volume.
        Volumes listed in the return for this method include volumes with
        active and pending pairings.

        :returns: a response
        :rtype: ListActivePairedVolumesResult
        """

        params = {}

        return self.send_request(
            'ListActivePairedVolumes',
            ListActivePairedVolumesResult,
            params,
        )

    def start_cluster_pairing(
            self,):
        """
        *start_cluster_pairing* is used to create an encoded key from a cluster
        that is used to pair with another cluster.
        The key created from this API method is used in the
        *\"complete_cluster_pairing\"* API method to establish a cluster
        pairing.
        You can pair a cluster with a maximum of four other SolidFire clusters.

        :returns: a response
        :rtype: StartClusterPairingResult
        """

        params = {}

        return self.send_request(
            'StartClusterPairing',
            StartClusterPairingResult,
            params,
        )

    def start_volume_pairing(
            self,
            volume_id,
            mode=OPTIONAL,):
        """
        *start_volume_pairing* is used to create an encoded key from a volume
        that is used to pair with another volume.
        The key that this method creates is used in the
        *\"complete_volume_pairing\"* API method to establish a volume pairing.

        :param volume_id: [required] The ID of the volume on which to start the
            pairing process.
        :type volume_id: int

        :param mode: (optional) The mode of the volume on which to start the
            pairing process. The mode can only be set if the volume is the
            source volume.

            Possible values:

            **Async**: (default if no mode parameter specified) Writes are
            acknowledged when they complete locally. The cluster does not wait
            for writes to be replicated to the target cluster.

            **Sync**: Source acknowledges write when the data is stored locally
            and on the remote cluster.

            **SnapshotsOnly**: Only snapshots created on the source cluster
            will be replicated. Active writes from the source volume will not
            be replicated.



        :type mode: str

        :returns: a response
        :rtype: StartVolumePairingResult
        """

        params = {
            "volumeID": volume_id,
        }
        if mode is not None:
            params["mode"] = mode

        return self.send_request(
            'StartVolumePairing',
            StartVolumePairingResult,
            params,
        )

    def complete_cluster_pairing(
            self,
            cluster_pairing_key,):
        """
        The *complete_cluster_pairing* method is the second step in the cluster
        pairing process.
        Use this method with the encoded key received from the
        *\"start_cluster_pairing\"* API method to complete the cluster pairing
        process.

        :param cluster_pairing_key: [required] A string of characters that is
            returned from the \"StartClusterPairing\" API method.
        :type cluster_pairing_key: str

        :returns: a response
        :rtype: CompleteClusterPairingResult
        """

        params = {
            "clusterPairingKey": cluster_pairing_key,
        }

        return self.send_request(
            'CompleteClusterPairing',
            CompleteClusterPairingResult,
            params,
        )

    def complete_volume_pairing(
            self,
            volume_pairing_key,
            volume_id,):
        """
        *complete_volume_pairing* is used to complete the pairing of two
        volumes.

        :param volume_pairing_key: [required] The key returned from the
            \"StartVolumePairing\" API method.
        :type volume_pairing_key: str

        :param volume_id: [required] The ID of volume on which to complete the
            pairing process.
        :type volume_id: int

        :returns: a response
        :rtype: CompleteVolumePairingResult
        """

        params = {
            "volumePairingKey": volume_pairing_key,
            "volumeID": volume_id,
        }

        return self.send_request(
            'CompleteVolumePairing',
            CompleteVolumePairingResult,
            params,
        )

    def remove_cluster_pair(
            self,
            cluster_pair_id,):
        """
        You can use the *remove_cluster_pair* method to close the open
        connections between two paired clusters.



        **Note**: Before you remove a cluster pair, you must first remove all
        volume pairing to the clusters with the *\"remove_volume_pair\"* API
        method.

        :param cluster_pair_id: [required] Unique identifier used to pair two
            clusters.
        :type cluster_pair_id: int

        :returns: a response
        :rtype: RemoveClusterPairResult
        """

        params = {
            "clusterPairID": cluster_pair_id,
        }

        return self.send_request(
            'RemoveClusterPair',
            RemoveClusterPairResult,
            params,
        )

    def remove_volume_pair(
            self,
            volume_id,):
        """
        *remove_volume_pair* is used to remove the remote pairing between two
        volumes.
        When the volume pairing information is removed, data is no longer
        replicated to or from the volume.
        This method should be run on both the source and target volumes that
        are paired together.

        :param volume_id: [required] ID of the volume on which to stop the
            replication process.
        :type volume_id: int

        :returns: a response
        :rtype: RemoveVolumePairResult
        """

        params = {
            "volumeID": volume_id,
        }

        return self.send_request(
            'RemoveVolumePair',
            RemoveVolumePairResult,
            params,
        )

    def modify_volume_pair(
            self,
            volume_id,
            paused_manual=OPTIONAL,
            mode=OPTIONAL,):
        """
        *modify_volume_pair* is used to pause or restart replication between a
        pair of volumes.

        :param volume_id: [required] Identification number of the volume to be
            modified.
        :type volume_id: int

        :param paused_manual: (optional) Valid values that can be entered:

            **true**: to pause volume replication.

            **false**: to restart volume replication.

            If no value is specified, no change in replication is performed.

        :type paused_manual: bool

        :param mode: (optional) Volume replication mode.

            Possible values:

            **Async**: Writes are acknowledged when they complete locally. The
            cluster does not wait for writes to be replicated to the target
            cluster.

            **Sync**: The source acknowledges the write when the data is stored
            locally and on the remote cluster.

            **SnapshotsOnly**: Only snapshots created on the source cluster
            will be replicated. Active writes from the source volume are not
            replicated.



        :type mode: str

        :returns: a response
        :rtype: ModifyVolumePairResult
        """

        params = {
            "volumeID": volume_id,
        }
        if paused_manual is not None:
            params["pausedManual"] = paused_manual
        if mode is not None:
            params["mode"] = mode

        return self.send_request(
            'ModifyVolumePair',
            ModifyVolumePairResult,
            params,
        )

    def create_snapshot(
            self,
            volume_id,
            snapshot_id=OPTIONAL,
            name=OPTIONAL,
            enable_remote_replication=OPTIONAL,
            retention=OPTIONAL,
            attributes=OPTIONAL,):
        """
        *create_snapshot* is used to create a point-in-time copy of a volume.
        A snapshot can be created from any volume or from an existing snapshot.




        **Note**: Creating a snapshot is allowed if cluster fullness is at
        stage 2 or 3.
        Snapshots are not created when cluster fullness is at stage 4 or 5.

        :param volume_id: [required] ID of the volume image from which to copy.
        :type volume_id: int

        :param snapshot_id: (optional) Unique ID of a snapshot from which the
            new snapshot is made. The *snapshot_id* passed must be a snapshot
            on the given volume. If a *snapshot_id* is not provided, a snapshot
            is created from the volume&#39;s active branch.
        :type snapshot_id: int

        :param name: (optional) A name for the snapshot. If no name is
            provided, the date and time the snapshot was taken is used.
        :type name: str

        :param enable_remote_replication: (optional) Identifies if snapshot is
            enabled for remote replication.
        :type enable_remote_replication: bool

        :param retention: (optional) The amount of time the snapshot will be
            retained. Enter in *hh:mm:ss*
        :type retention: str

        :param attributes: (optional) List of Name/Value pairs in JSON object
            format.
        :type attributes: dict

        :returns: a response
        :rtype: CreateSnapshotResult
        """

        params = {
            "volumeID": volume_id,
        }
        self._check_param_versions(
            'create_snapshot',
            [
                ("enable_remote_replication",
                 enable_remote_replication, 8.0, None),
                ("retention",
                 retention, 8.0, None),
            ]
        )
        if snapshot_id is not None:
            params["snapshotID"] = snapshot_id
        if name is not None:
            params["name"] = name
        if enable_remote_replication is not None:
            params["enableRemoteReplication"] = enable_remote_replication
        if retention is not None:
            params["retention"] = retention
        if attributes is not None:
            params["attributes"] = attributes

        return self.send_request(
            'CreateSnapshot',
            CreateSnapshotResult,
            params,
        )

    def delete_snapshot(
            self,
            snapshot_id,):
        """
        *delete_snapshot* is used to delete a snapshot.
        A snapshot that is currently the \"active\" snapshot cannot be deleted.
        You must rollback and make another snapshot \"active\" before the
        current snapshot can be deleted.
        To rollback a snapshot, use RollbackToSnapshot.

        :param snapshot_id: [required] The ID of the snapshot to delete.
        :type snapshot_id: int

        :returns: a response
        :rtype: DeleteSnapshotResult
        """

        params = {
            "snapshotID": snapshot_id,
        }

        return self.send_request(
            'DeleteSnapshot',
            DeleteSnapshotResult,
            params,
        )

    def list_snapshots(
            self,
            volume_id=OPTIONAL,):
        """
        *list_snapshots* is used to return the attributes of each snapshot
        taken on the volume.

        :param volume_id: (optional) The volume to list snapshots for. If not
            provided, all snapshots for all volumes are returned.
        :type volume_id: int

        :returns: a response
        :rtype: ListSnapshotsResult
        """

        params = {}
        if volume_id is not None:
            params["volumeID"] = volume_id

        return self.send_request(
            'ListSnapshots',
            ListSnapshotsResult,
            params,
        )

    def modify_snapshot(
            self,
            snapshot_id,
            expiration_time=OPTIONAL,
            enable_remote_replication=OPTIONAL,):
        """
        *modify_snapshot* is used to change the attributes currently assigned
        to a snapshot.
        Use this API method to enable the snapshots created on the Read/Write
        (source) volume to be remotely replicated to a target SolidFire storage
        system.

        :param snapshot_id: [required] ID of the snapshot.
        :type snapshot_id: int

        :param expiration_time: (optional) Use to set the time when the
            snapshot should be removed.
        :type expiration_time: str

        :param enable_remote_replication: (optional) Use to enable the snapshot
            created to be replicated to a remote SolidFire cluster. Possible
            values:

            **true**: the snapshot will be replicated to remote storage.

            **false**: Default. No replication.

        :type enable_remote_replication: bool

        :returns: a response
        :rtype: ModifySnapshotResult
        """

        params = {
            "snapshotID": snapshot_id,
        }
        if expiration_time is not None:
            params["expirationTime"] = expiration_time
        if enable_remote_replication is not None:
            params["enableRemoteReplication"] = enable_remote_replication

        return self.send_request(
            'ModifySnapshot',
            ModifySnapshotResult,
            params,
            since=8.0,
        )

    def rollback_to_snapshot(
            self,
            volume_id,
            snapshot_id,
            save_current_state,
            name=OPTIONAL,
            attributes=OPTIONAL,):
        """
        *rollback_to_snapshot* is used to make an existing snapshot the
        \"active\" volume image. This method creates a new
        snapshot from an existing snapshot. The new snapshot becomes \"active\"
        and the existing snapshot is preserved until
        it is manually deleted. The previously \"active\" snapshot is deleted
        unless the parameter *save_current_state* is set with
        a value of \"true.\"
        **Note**: Creating a snapshot is allowed if cluster fullness is at
        stage 2 or 3.
        Snapshots are not created when cluster fullness is at stage 4 or 5.

        :param volume_id: [required] *volume_id* for the volume.
        :type volume_id: int

        :param snapshot_id: [required] ID of a previously created snapshot on
            the given volume.
        :type snapshot_id: int

        :param save_current_state: [required]

            **true**: The previous active volume image is kept.

            **false**: (default) The previous active volume image is deleted.

        :type save_current_state: bool

        :param name: (optional) Name for the snapshot. If no name is given,
            then the name of the snapshot being rolled back to is used with
            \"-copy\" appended to the end of the name.
        :type name: str

        :param attributes: (optional) List of Name/Value pairs in JSON object
            format
        :type attributes: dict

        :returns: a response
        :rtype: CreateSnapshotResult
        """

        params = {
            "volumeID": volume_id,
            "snapshotID": snapshot_id,
            "saveCurrentState": save_current_state,
        }
        if name is not None:
            params["name"] = name
        if attributes is not None:
            params["attributes"] = attributes

        return self.send_request(
            'RollbackToSnapshot',
            CreateSnapshotResult,
            params,
        )

    def create_group_snapshot(
            self,
            volumes,
            name=OPTIONAL,
            enable_remote_replication=OPTIONAL,
            retention=OPTIONAL,
            attributes=OPTIONAL,):
        """
        *create_group_snapshot* is used to create a point-in-time copy of a
        group of volumes.
        The snapshot created can then be used later as a backup or rollback to
        ensure the data on the group of volumes is consistent for the point in
        time in which the snapshot was created.




        **Note**: Creating a group snapshot is allowed if cluster fullness is
        at stage 2 or 3.
        Snapshots are not created when cluster fullness is at stage 4 or 5.

        :param volumes: [required] Unique ID of the volume image from which to
            copy.
        :type volumes: int[]

        :param name: (optional) A name for the snapshot. If no name is
            provided, the date and time the snapshot was taken is used.
        :type name: str

        :param enable_remote_replication: (optional) Identifies if snapshot is
            enabled for remote replication.
        :type enable_remote_replication: bool

        :param retention: (optional) The amount of time the snapshot will be
            retained. Enter in *hh:mm:ss*
        :type retention: str

        :param attributes: (optional) List of Name/Value pairs in JSON object
            format.
        :type attributes: dict

        :returns: a response
        :rtype: CreateGroupSnapshotResult
        """

        params = {
            "volumes": volumes,
        }
        self._check_param_versions(
            'create_group_snapshot',
            [
                ("enable_remote_replication",
                 enable_remote_replication, 8.0, None),
                ("retention",
                 retention, 8.0, None),
            ]
        )
        if name is not None:
            params["name"] = name
        if enable_remote_replication is not None:
            params["enableRemoteReplication"] = enable_remote_replication
        if retention is not None:
            params["retention"] = retention
        if attributes is not None:
            params["attributes"] = attributes

        return self.send_request(
            'CreateGroupSnapshot',
            CreateGroupSnapshotResult,
            params,
        )

    def delete_group_snapshot(
            self,
            group_snapshot_id,
            save_members,):
        """
        *delete_group_snapshot* is used to delete a group snapshot.
        The *save_members* parameter can be used to preserve all the snapshots
        that
        were made for the volumes in the group but the group association will
        be removed.

        :param group_snapshot_id: [required] Unique ID of the group snapshot.
        :type group_snapshot_id: int

        :param save_members: [required]

            **true**: Snapshots are kept, but group association is removed.

            **false**: The group and snapshots are deleted.

        :type save_members: bool

        :returns: a response
        :rtype: DeleteGroupSnapshotResult
        """

        params = {
            "groupSnapshotID": group_snapshot_id,
            "saveMembers": save_members,
        }

        return self.send_request(
            'DeleteGroupSnapshot',
            DeleteGroupSnapshotResult,
            params,
        )

    def list_group_snapshots(
            self,
            volume_id=OPTIONAL,):
        """
        *list_group_snapshots* is used to return information about all group
        snapshots that have been created.

        :param volume_id: (optional) An array of unique volume *ids* to query.
            If this parameter is not specified, all group snapshots on the
            cluster will be included.
        :type volume_id: int

        :returns: a response
        :rtype: ListGroupSnapshotsResult
        """

        params = {}
        if volume_id is not None:
            params["volumeID"] = volume_id

        return self.send_request(
            'ListGroupSnapshots',
            ListGroupSnapshotsResult,
            params,
        )

    def modify_group_snapshot(
            self,
            group_snapshot_id,
            expiration_time=OPTIONAL,
            enable_remote_replication=OPTIONAL,):
        """
        *modify_group_snapshot* is used to change the attributes currently
        assigned to a group snapshot.

        :param group_snapshot_id: [required] ID of the snapshot.
        :type group_snapshot_id: int

        :param expiration_time: (optional) Use to set the time when the
            snapshot should be removed.
        :type expiration_time: str

        :param enable_remote_replication: (optional) Use to enable the snapshot
            created to be replicated to a remote SolidFire cluster. Possible
            values:

            **true**: the snapshot will be replicated to remote storage.

            **false**: Default. No replication.

        :type enable_remote_replication: bool

        :returns: a response
        :rtype: ModifyGroupSnapshotResult
        """

        params = {
            "groupSnapshotID": group_snapshot_id,
        }
        if expiration_time is not None:
            params["expirationTime"] = expiration_time
        if enable_remote_replication is not None:
            params["enableRemoteReplication"] = enable_remote_replication

        return self.send_request(
            'ModifyGroupSnapshot',
            ModifyGroupSnapshotResult,
            params,
            since=8.0,
        )

    def rollback_to_group_snapshot(
            self,
            group_snapshot_id,
            save_current_state,
            name=OPTIONAL,
            attributes=OPTIONAL,):
        """
        *rollback_to_group_snapshot* is used to roll back each individual
        volume in a snapshot group to a copy of their individual snapshots.




        **Note**: Creating a snapshot is allowed if cluster fullness is at
        stage 2 or 3.
        Snapshots are not created when cluster fullness is at stage 4 or 5.

        :param group_snapshot_id: [required] Unique ID of the group snapshot.
        :type group_snapshot_id: int

        :param save_current_state: [required]

            **true**: The previous active volume image is kept.

            **false**: (default) The previous active volume image is deleted.

        :type save_current_state: bool

        :param name: (optional) Name for the snapshot. If no name is given,
            then the name of the snapshot being rolled back to is used with
            \"-copy\" appended to the end of the name.
        :type name: str

        :param attributes: (optional) List of Name/Value pairs in JSON object
            format
        :type attributes: dict

        :returns: a response
        :rtype: CreateGroupSnapshotResult
        """

        params = {
            "groupSnapshotID": group_snapshot_id,
            "saveCurrentState": save_current_state,
        }
        if name is not None:
            params["name"] = name
        if attributes is not None:
            params["attributes"] = attributes

        return self.send_request(
            'RollbackToGroupSnapshot',
            CreateGroupSnapshotResult,
            params,
            since=7.0,
        )

    def get_schedule(
            self,
            schedule_id,):
        """
        *get_schedule* is used to return information about a scheduled snapshot
        that has been created. You can see information about a specified
        schedule if there are many snapshot schedules in the system. You can
        include more than one schedule with this method by specifying
        additional *schedule_ids* to the parameter.

        :param schedule_id: [required] Unique ID of the schedule or multiple
            schedules to display
        :type schedule_id: int

        :returns: a response
        :rtype: GetScheduleResult
        """

        params = {
            "scheduleID": schedule_id,
        }

        since = 8.0
        deprecated = None

        return ElementServiceAdaptor.get_schedule(self, params,
                                                  since, deprecated)

    def list_schedules(
            self,):
        """
        *list_schedule* is used to return information about all scheduled
        snapshots that have been created.

        :returns: a response
        :rtype: ListSchedulesResult
        """

        params = {}

        since = 8.0
        deprecated = None

        return ElementServiceAdaptor.list_schedules(self, params,
                                                    since, deprecated)

    def create_schedule(
            self,
            schedule,):
        """
        *create_schedule* is used to create a schedule that will autonomously
        make a snapshot of a volume at a defined interval.







        The snapshot created can be used later as a backup or rollback to
        ensure the data on a volume or group of volumes is consistent for the
        point in time in which the snapshot was created.







        **Note**: Creating a snapshot is allowed if cluster fullness is at
        stage 2 or 3. Snapshots are not created when cluster fullness is at
        stage 4 or 5.

        :param schedule: [required] The \"Schedule\" object will be used to
            create a new schedule.

            Do not set *schedule_id* property, it will be ignored.

            Frequency property must be of type that inherits from Frequency.
            Valid types are:

            *days_of_month_frequency*

            *days_or_week_frequency*

            *time_interval_frequency*

        :type schedule: Schedule

        :returns: a response
        :rtype: CreateScheduleResult
        """

        params = {
            "schedule": schedule,
        }

        since = 8.0
        deprecated = None

        return ElementServiceAdaptor.create_schedule(self, params,
                                                     since, deprecated)

    def modify_schedule(
            self,
            schedule,):
        """
        *modify_schedule* is used to change the intervals at which a scheduled
        snapshot occurs. This allows for adjustment to the snapshot frequency
        and retention.




        :param schedule: [required] The \"Schedule\" object will be used to
            modify an existing schedule.

            The *schedule_id* property is required.

            Frequency property must be of type that inherits from Frequency.
            Valid types are:

            *days_of_month_frequency*

            *days_or_week_frequency*

            *time_interval_frequency*

        :type schedule: Schedule

        :returns: a response
        :rtype: ModifyScheduleResult
        """

        params = {
            "schedule": schedule,
        }

        since = 8.0
        deprecated = None

        return ElementServiceAdaptor.modify_schedule(self, params,
                                                     since, deprecated)

    def get_raw_stats(
            self,):
        """
        The *get_raw_stats* call is used by SolidFire engineering to
        troubleshoot new features. The data returned from *get_raw_stats* is
        not documented, it changes frequently, and is not guaranteed to be
        accurate. It is not recommended to ever use *get_raw_stats* for
        collecting performance data or any other management integration with a
        SolidFire cluster.
        The data returned from *get_raw_stats* changes frequently, and is not
        guaranteed to accurately show performance from the system. It is not
        recommended to ever use *get_raw_stats* for collecting performance data
        or any other management integration with a SolidFire cluster.

        :returns: a response
        :rtype: Object
        """

        params = {}

        return self.send_request(
            'GetRawStats',
            str,
            params,
        )

    def get_complete_stats(
            self,):
        """
        The *get_complete_stats* API method is used by SolidFire engineering to
        troubleshoot new features. The data returned from *get_complete_stats*
        is not documented, changes frequently, and is not guaranteed to be
        accurate. It is not recommended to ever use *get_complete_stats* for
        collecting performance data or any other management integration with a
        SolidFire cluster.
        The data returned from *get_complete_stats* changes frequently, and is
        not guaranteed to accurately show performance from the system. It is
        not recommended to ever use *get_complete_stats* for collecting
        performance data or any other management integration with a SolidFire
        cluster.

        :returns: a response
        :rtype: Object
        """

        params = {}

        return self.send_request(
            'GetCompleteStats',
            str,
            params,
        )

    def list_tests(
            self,):
        """
        The *list_tests* API method is used to return the tests that are
        available to run on a node.


            **Note**: This method is available only through the per-node API
        endpoint 5.0 or later.


        :returns: a response
        :rtype: ListTestsResult
        """

        params = {}

        return self.send_request(
            'ListTests',
            ListTestsResult,
            params,
        )

    def list_utilities(
            self,):
        """
        The *list_utilities* API method is used to return the tests that are
        available to run on a node.


            **Note**: This method is available only through the per-node API
        endpoint 5.0 or later.


        :returns: a response
        :rtype: ListUtilitiesResult
        """

        params = {}

        return self.send_request(
            'ListUtilities',
            ListUtilitiesResult,
            params,
        )

    def test_connect_ensemble(
            self,
            ensemble=OPTIONAL,):
        """
        The *test_connect_ensemble* API method is used to verify connectivity
        with a sepcified database ensemble. By default it uses the ensemble for
        the cluster the node is associated with. Alternatively you can provide
        a different ensemble to test connectivity with.


            **Note**: This method is available only through the per-node API
        endpoint 5.0 or later.


        :param ensemble: (optional) A comma-separated list of ensemble node
            *cips* for connectivity testing
        :type ensemble: str

        :returns: a response
        :rtype: TestConnectEnsembleResult
        """

        params = {}
        if ensemble is not None:
            params["ensemble"] = ensemble

        return self.send_request(
            'TestConnectEnsemble',
            TestConnectEnsembleResult,
            params,
        )

    def test_connect_mvip(
            self,
            mvip=OPTIONAL,):
        """
        The *test_connect_mvip* API method is used to test the management
        connection to the cluster. The test pings the MVIP and executes a
        simple API method to verify connectivity.


            **Note**: This method is available only through the per-node API
        endpoint 5.0 or later.


        :param mvip: (optional) Optionally, use to test the management
            connection of a different MVIP. This is not needed to test the
            connection to the target cluster.
        :type mvip: str

        :returns: a response
        :rtype: TestConnectMvipResult
        """

        params = {}
        if mvip is not None:
            params["mvip"] = mvip

        return self.send_request(
            'TestConnectMvip',
            TestConnectMvipResult,
            params,
        )

    def test_connect_svip(
            self,
            svip=OPTIONAL,):
        """
        The *test_connect_svip* API method is used to test the storage
        connection to the cluster. The test pings the SVIP using ICMP packets
        and when successful connects as an iSCSI initiator.


            **Note**: This method is available only through the per-node API
        endpoint 5.0 or later.


        :param svip: (optional) Optionally, use to test the storage connection
            of a different SVIP. This is not needed to test the connection to
            the target cluster.
        :type svip: str

        :returns: a response
        :rtype: TestConnectSvipResult
        """

        params = {}
        if svip is not None:
            params["svip"] = svip

        return self.send_request(
            'TestConnectSvip',
            TestConnectSvipResult,
            params,
        )

    def test_ping(
            self,
            attempts=OPTIONAL,
            hosts=OPTIONAL,
            total_timeout_sec=OPTIONAL,
            packet_size=OPTIONAL,
            ping_timeout_msec=OPTIONAL,):
        """
        The *test_ping* API method is used to validate the connection to all
        nodes in the cluster on both 1G and 10G interfaces using ICMP packets.
        The test uses the appropriate MTU sizes for each packet based on the
        MTU settings in the network configuration.


            **Note**: This method is available only through the per-node API
        endpoint 5.0 or later.


        :param attempts: (optional) Specifies the number of times the system
            should repeat the test ping. Default is 5.
        :type attempts: int

        :param hosts: (optional) Specify address or hostnames of devices to
            ping.
        :type hosts: str

        :param total_timeout_sec: (optional) Specifies the length of time the
            ping should wait for a system response before issuing the next ping
            attempt or ending the process.
        :type total_timeout_sec: int

        :param packet_size: (optional) Specify the number of bytes to send in
            the ICMP packet sent to each IP. Number be less than the maximum
            MTU specified in the network configuration.
        :type packet_size: int

        :param ping_timeout_msec: (optional) Specify the number of milliseconds
            to wait for each individual ping response. Default is 500ms.
        :type ping_timeout_msec: int

        :returns: a response
        :rtype: TestPingResult
        """

        params = {}
        if attempts is not None:
            params["attempts"] = attempts
        if hosts is not None:
            params["hosts"] = hosts
        if total_timeout_sec is not None:
            params["totalTimeoutSec"] = total_timeout_sec
        if packet_size is not None:
            params["packetSize"] = packet_size
        if ping_timeout_msec is not None:
            params["pingTimeoutMsec"] = ping_timeout_msec

        return self.send_request(
            'TestPing',
            TestPingResult,
            params,
        )

    def list_virtual_networks(
            self,
            virtual_network_id=OPTIONAL,
            virtual_network_tag=OPTIONAL,
            virtual_network_ids=OPTIONAL,
            virtual_network_tags=OPTIONAL,):
        """
        *list_virtual_networks* is used to get a list of all the configured
        virtual networks for the cluster. This method can be used to verify the
        virtual network settings in the cluster.

        This method does not require any parameters to be passed. But, one or
        more *virtual_network_ids* or *virtual_network_tags* can be passed in
        order to filter the results.

        :param virtual_network_id: (optional) Network ID to filter the list for
            a single virtual network
        :type virtual_network_id: int

        :param virtual_network_tag: (optional) Network Tag to filter the list
            for a single virtual network
        :type virtual_network_tag: int

        :param virtual_network_ids: (optional) *network_ids* to include in the
            list.
        :type virtual_network_ids: int[]

        :param virtual_network_tags: (optional) Network Tags to include in the
            list.
        :type virtual_network_tags: int[]

        :returns: a response
        :rtype: ListVirtualNetworksResult
        """

        params = {}
        if virtual_network_id is not None:
            params["virtualNetworkID"] = virtual_network_id
        if virtual_network_tag is not None:
            params["virtualNetworkTag"] = virtual_network_tag
        if virtual_network_ids is not None:
            params["virtualNetworkIDs"] = virtual_network_ids
        if virtual_network_tags is not None:
            params["virtualNetworkTags"] = virtual_network_tags

        return self.send_request(
            'ListVirtualNetworks',
            ListVirtualNetworksResult,
            params,
            since=7.0,
        )

    def add_virtual_network(
            self,
            virtual_network_tag,
            name,
            address_blocks,
            netmask,
            svip,
            gateway=OPTIONAL,
            namespace=OPTIONAL,
            attributes=OPTIONAL,):
        """
        *add_virtual_network* is used to add a new virtual network to a cluster
        configuration. When a virtual network is added, an interface for each
        node is created and each will require a virtual network IP address. The
        number of IP addresses specified as a parameter for this API method
        must be equal to or greater than the number of nodes in the cluster.
        Virtual network addresses are bulk provisioned by SolidFire and
        assigned to individual nodes automatically. Virtual network addresses
        do not need to be assigned to nodes manually.




        **Note:** The *add_virtual_network* method is used only to create a new
        virtual network. If you want to make changes to a virtual network,
        please use the *modify_virtual_network* method.

        :param virtual_network_tag: [required] A unique virtual network (VLAN)
            tag. Supported values are 1 to 4095 (the number zero (0) is not
            supported).
        :type virtual_network_tag: int

        :param name: [required] User defined name for the new virtual network.
        :type name: str

        :param address_blocks: [required] Unique Range of IP addresses to
            include in the virtual network. Attributes for this parameter are:
            **start:** start of the IP address range. (String)
            **size:** numbre of IP addresses to include in the block. (Integer)

        :type address_blocks: AddressBlock[]

        :param netmask: [required] Unique netmask for the virtual network being
            created.
        :type netmask: str

        :param svip: [required] Unique storage IP address for the virtual
            network being created.
        :type svip: str

        :param gateway: (optional)
        :type gateway: str

        :param namespace: (optional)
        :type namespace: bool

        :param attributes: (optional) List of Name/Value pairs in JSON object
            format.
        :type attributes: dict

        :returns: a response
        :rtype: AddVirtualNetworkResult
        """

        params = {
            "virtualNetworkTag": virtual_network_tag,
            "name": name,
            "addressBlocks": address_blocks,
            "netmask": netmask,
            "svip": svip,
        }
        self._check_param_versions(
            'add_virtual_network',
            [
                ("gateway",
                 gateway, 9.0, None),
                ("namespace",
                 namespace, 9.0, None),
            ]
        )
        if gateway is not None:
            params["gateway"] = gateway
        if namespace is not None:
            params["namespace"] = namespace
        if attributes is not None:
            params["attributes"] = attributes

        return self.send_request(
            'AddVirtualNetwork',
            AddVirtualNetworkResult,
            params,
            since=7.0,
        )

    def modify_virtual_network(
            self,
            virtual_network_id=OPTIONAL,
            virtual_network_tag=OPTIONAL,
            name=OPTIONAL,
            address_blocks=OPTIONAL,
            netmask=OPTIONAL,
            svip=OPTIONAL,
            gateway=OPTIONAL,
            namespace=OPTIONAL,
            attributes=OPTIONAL,):
        """
        *modify_virtual_network* is used to change various attributes of a
        *virtual_network* object. This method can be used to add or remove
        address blocks, change the netmask IP, or modify the name or
        description of the virtual network.




        **Note:** This method requires either the *virtual_network_id* or the
        *virtual_network_tag* as a parameter, but not both.

        :param virtual_network_id: (optional) Unique identifier of the virtual
            network to modify. This is the virtual network ID assigned by the
            SolidFire cluster.
        :type virtual_network_id: int

        :param virtual_network_tag: (optional) Network Tag that identifies the
            virtual network to modify.
        :type virtual_network_tag: int

        :param name: (optional) New name for the virtual network.
        :type name: str

        :param address_blocks: (optional) New *address_block* to set for this
            Virtual Network object. This may contain new address blocks to add
            to the existing object or it may omit unused address blocks that
            need to be removed. Alternatively, existing address blocks may be
            extended or reduced in size. The size of the starting
            *address_blocks* for a Virtual Network object can only be
            increased, and can never be decreased. Attributes for this
            parameter are:

            **start:** start of the IP address range. (String)

            **size:** numbre of IP addresses to include in the block. (Integer)

        :type address_blocks: AddressBlock[]

        :param netmask: (optional) New netmask for this virtual network.
        :type netmask: str

        :param svip: (optional) The storage virtual IP address for this virtual
            network. The svip for Virtual Network cannot be changed. A new
            Virtual Network must be created in order to use a different svip
            address.
        :type svip: str

        :param gateway: (optional)
        :type gateway: str

        :param namespace: (optional)
        :type namespace: bool

        :param attributes: (optional) A new list of Name/Value pairs in JSON
            object format.
        :type attributes: dict

        :returns: a response
        :rtype: AddVirtualNetworkResult
        """

        params = {}
        self._check_param_versions(
            'modify_virtual_network',
            [
                ("gateway",
                 gateway, 9.0, None),
                ("namespace",
                 namespace, 9.0, None),
            ]
        )
        if virtual_network_id is not None:
            params["virtualNetworkID"] = virtual_network_id
        if virtual_network_tag is not None:
            params["virtualNetworkTag"] = virtual_network_tag
        if name is not None:
            params["name"] = name
        if address_blocks is not None:
            params["addressBlocks"] = address_blocks
        if netmask is not None:
            params["netmask"] = netmask
        if svip is not None:
            params["svip"] = svip
        if gateway is not None:
            params["gateway"] = gateway
        if namespace is not None:
            params["namespace"] = namespace
        if attributes is not None:
            params["attributes"] = attributes

        return self.send_request(
            'ModifyVirtualNetwork',
            AddVirtualNetworkResult,
            params,
            since=7.0,
        )

    def remove_virtual_network(
            self,
            virtual_network_id=OPTIONAL,
            virtual_network_tag=OPTIONAL,):
        """
        *remove_virtual_network* is used to remove a previously added virtual
        network.




        **Note:** This method requires either the *virtual_network_id* of the
        *virtual_network_tag* as a parameter, but not both.

        :param virtual_network_id: (optional) Network ID that identifies the
            virtual network to remove.
        :type virtual_network_id: int

        :param virtual_network_tag: (optional) Network Tag that identifies the
            virtual network to remove.
        :type virtual_network_tag: int

        :returns: a response
        :rtype: RemoveVirtualNetworkResult
        """

        params = {}
        if virtual_network_id is not None:
            params["virtualNetworkID"] = virtual_network_id
        if virtual_network_tag is not None:
            params["virtualNetworkTag"] = virtual_network_tag

        return self.send_request(
            'RemoveVirtualNetwork',
            RemoveVirtualNetworkResult,
            params,
            since=7.0,
        )

    def clone_volume(
            self,
            volume_id,
            name,
            new_account_id=OPTIONAL,
            new_size=OPTIONAL,
            access=OPTIONAL,
            snapshot_id=OPTIONAL,
            attributes=OPTIONAL,):
        """
        *clone_volume* is used to create a copy of the volume.
        This method is asynchronous and may take a variable amount of time to
        complete.
        The cloning process begins immediately when the *clone_volume* request
        is made and is representative of the state of the volume when the API
        method is issued.
        *get_async_results* can be used to determine when the cloning process
        is complete and the new volume is available for connections.
        *list_sync_jobs* can be used to see the progress of creating the clone.




        **Note**: The initial attributes and quality of service settings for
        the volume are inherited from the volume being cloned.
        If different settings are required, they can be changed via
        ModifyVolume.




        **Note**: Cloned volumes do not inherit volume access group memberships
        from the source volume.

        :param volume_id: [required] The ID of the volume to clone.
        :type volume_id: int

        :param name: [required] The name for the newly-created volume.
        :type name: str

        :param new_account_id: (optional) *account_id* for the owner of the new
            volume. If unspecified, the *account_id* of the owner of the volume
            being cloned is used.
        :type new_account_id: int

        :param new_size: (optional) New size of the volume, in bytes. May be
            greater or less than the size of the volume being cloned. If
            unspecified, the clone&#39;s volume size will be the same as the
            source volume. Size is rounded up to the nearest 1 MiB.
        :type new_size: int

        :param access: (optional) Access settings for the new volume.

            **readOnly**: Only read operations are allowed.

            **readWrite**: Reads and writes are allowed.

            **locked**: No reads or writes are allowed.

            **replicationTarget**: Identify a volume as the target volume for a
            paired set of volumes. If the volume is not paired, the access
            status is locked.

            If unspecified, the access settings of the clone will be the same
            as the source.

        :type access: str

        :param snapshot_id: (optional) ID of the snapshot to use as the source
            of the clone. If unspecified, the clone will be created with a
            snapshot of the active volume.
        :type snapshot_id: int

        :param attributes: (optional) List of Name/Value pairs in JSON object
            format.
        :type attributes: dict

        :returns: a response
        :rtype: CloneVolumeResult
        """

        params = {
            "volumeID": volume_id,
            "name": name,
        }
        if new_account_id is not None:
            params["newAccountID"] = new_account_id
        if new_size is not None:
            params["newSize"] = new_size
        if access is not None:
            params["access"] = access
        if snapshot_id is not None:
            params["snapshotID"] = snapshot_id
        if attributes is not None:
            params["attributes"] = attributes

        return self.send_request(
            'CloneVolume',
            CloneVolumeResult,
            params,
        )

    def clone_multiple_volumes(
            self,
            volumes,
            access=OPTIONAL,
            group_snapshot_id=OPTIONAL,
            new_account_id=OPTIONAL,):
        """
        *clone_multiple_volumes* is used to create a clone of a group of
        specified volumes. A consistent set of characteristics can be assigned
        to a group of multiple volume when they are cloned together.
        If *group_snapshot_id* is going to be used to clone the volumes in a
        group snapshot, the group snapshot must be created first using the
        *create_group_snapshot* API method or the SolidFire Element WebUI.
        Using *group_snapshot_id* is optional when cloning multiple volumes.




        **Note**: Cloning multiple volumes is allowed if cluster fullness is at
        stage 2 or 3. Clones are not created when cluster fullness is at stage
        4 or 5.

        :param volumes: [required] Array of Unique ID for each volume to
            include in the clone with optional parameters. If optional
            parameters are not specified, the values will be inherited from the
            source volumes.
        :type volumes: CloneMultipleVolumeParams[]

        :param access: (optional) New default access method for the new volumes
            if not overridden by information passed in the volumes array.

            **readOnly**: Only read operations are allowed.

            **readWrite**: Reads and writes are allowed.

            **locked**: No reads or writes are allowed.

            **replicationTarget**: Identify a volume as the target volume for a
            paired set of volumes. If the volume is not paired, the access
            status is locked.

            If unspecified, the access settings of the clone will be the same
            as the source.

        :type access: str

        :param group_snapshot_id: (optional) ID of the group snapshot to use as
            a basis for the clone.
        :type group_snapshot_id: int

        :param new_account_id: (optional) New account ID for the volumes if not
            overridden by information passed in the volumes array.
        :type new_account_id: int

        :returns: a response
        :rtype: CloneMultipleVolumesResult
        """

        params = {
            "volumes": volumes,
        }
        if access is not None:
            params["access"] = access
        if group_snapshot_id is not None:
            params["groupSnapshotID"] = group_snapshot_id
        if new_account_id is not None:
            params["newAccountID"] = new_account_id

        return self.send_request(
            'CloneMultipleVolumes',
            CloneMultipleVolumesResult,
            params,
        )

    def create_volume(
            self,
            name,
            account_id,
            total_size,
            enable512e,
            qos=OPTIONAL,
            attributes=OPTIONAL,):
        """
        *create_volume* is used to create a new (empty) volume on the cluster.
        When the volume is created successfully it is available for connection
        via iSCSI.

        :param name: [required] Name of the volume. Not required to be unique,
            but it is recommended. May be 1 to 64 characters in length.
        :type name: str

        :param account_id: [required] *account_id* for the owner of this
            volume.
        :type account_id: int

        :param total_size: [required] Total size of the volume, in bytes. Size
            is rounded up to the nearest 1MB size.
        :type total_size: int

        :param enable512e: [required] Should the volume provides 512-byte
            sector emulation?
        :type enable512e: bool

        :param qos: (optional) Initial quality of service settings for this
            volume.

            Volumes created without specified *qos* values are created with the
            default values for QoS. Default values for a volume can be found by
            running the *get_default_qos* method.

        :type qos: QoS

        :param attributes: (optional) List of Name/Value pairs in JSON object
            format.
        :type attributes: dict

        :returns: a response
        :rtype: CreateVolumeResult
        """

        params = {
            "name": name,
            "accountID": account_id,
            "totalSize": total_size,
            "enable512e": enable512e,
        }
        if qos is not None:
            params["qos"] = qos
        if attributes is not None:
            params["attributes"] = attributes

        return self.send_request(
            'CreateVolume',
            CreateVolumeResult,
            params,
        )

    def delete_volume(
            self,
            volume_id,):
        """
        *delete_volume* marks an active volume for deletion.
        It is purged (permanently deleted) after the cleanup interval elapses.
        After making a request to delete a volume, any active iSCSI connections
        to the volume is immediately terminated and no further connections are
        allowed while the volume is in this state.
        It is not returned in target discovery requests.




        Any snapshots of a volume that has been marked to delete are not
        affected.
        Snapshots are kept until the volume is purged from the system.




        If a volume is marked for deletion, and it has a bulk volume read or
        bulk volume write operation in progress, the bulk volume operation is
        stopped.




        If the volume you delete is paired with a volume, replication between
        the paired volumes is suspended and no data is transferred to it or
        from it while in a deleted state.
        The remote volume the deleted volume was paired with enters into a
        *paused_misconfigured* state and data is no longer sent to it or from
        the deleted volume.
        Until the deleted volume is purged, it can be restored and data
        transfers resumes.
        If the deleted volume gets purged from the system, the volume it was
        paired with enters into a *stopped_misconfigured* state and the volume
        pairing status is removed.
        The purged volume becomes permanently unavailable.

        :param volume_id: [required] The ID of the volume to delete.
        :type volume_id: int

        :returns: a response
        :rtype: DeleteVolumeResult
        """

        params = {
            "volumeID": volume_id,
        }

        return self.send_request(
            'DeleteVolume',
            DeleteVolumeResult,
            params,
        )

    def get_volume_stats(
            self,
            volume_id,):
        """
        *get_volume_stats* is used to retrieve high-level activity measurements
        for a single volume.
        Values are cumulative from the creation of the volume.

        :param volume_id: [required] Specifies the volume for which statistics
            is gathered.
        :type volume_id: int

        :returns: a response
        :rtype: GetVolumeStatsResult
        """

        params = {
            "volumeID": volume_id,
        }

        return self.send_request(
            'GetVolumeStats',
            GetVolumeStatsResult,
            params,
        )

    def get_volume_efficiency(
            self,
            volume_id,
            force=OPTIONAL,):
        """
        *get_volume_efficiency* is used to retrieve information about a volume.
        Only the volume given as a parameter in this API method is used to
        compute the capacity.

        :param volume_id: [required] Specifies the volume for which capacity is
            computed.
        :type volume_id: int

        :param force: (optional)
        :type force: bool

        :returns: a response
        :rtype: GetVolumeEfficiencyResult
        """

        params = {
            "volumeID": volume_id,
        }
        if force is not None:
            params["force"] = force

        return self.send_request(
            'GetVolumeEfficiency',
            GetVolumeEfficiencyResult,
            params,
        )

    def list_bulk_volume_jobs(
            self,):
        """
        *list_bulk_volume_jobs* is used to return information about each bulk
        volume read or write operation that is occurring in the system.

        :returns: a response
        :rtype: ListBulkVolumeJobsResult
        """

        params = {}

        return self.send_request(
            'ListBulkVolumeJobs',
            ListBulkVolumeJobsResult,
            params,
        )

    def list_active_volumes(
            self,
            start_volume_id=OPTIONAL,
            limit=OPTIONAL,):
        """
        *list_active_volumes* is used to return the list of active volumes
        currently in the system.
        The list of volumes is returned sorted in *volume_id* order and can be
        returned in multiple parts (pages).

        :param start_volume_id: (optional) The ID of the first volume to list.
            This can be useful for paging results. By default, this starts at
            the lowest VolumeID.
        :type start_volume_id: int

        :param limit: (optional) The maximum number of volumes to return from
            the API.
        :type limit: int

        :returns: a response
        :rtype: ListActiveVolumesResult
        """

        params = {}
        if start_volume_id is not None:
            params["startVolumeID"] = start_volume_id
        if limit is not None:
            params["limit"] = limit

        return self.send_request(
            'ListActiveVolumes',
            ListActiveVolumesResult,
            params,
        )

    def list_deleted_volumes(
            self,):
        """
        *list_deleted_volumes* is used to return the entire list of volumes
        that have been marked for deletion and is purged from the system.

        :returns: a response
        :rtype: ListDeletedVolumesResult
        """

        params = {}

        return self.send_request(
            'ListDeletedVolumes',
            ListDeletedVolumesResult,
            params,
        )

    def list_iscsisessions(
            self,):
        """
        *list_iscsisessions* is used to return iSCSI connection information for
        volumes in the cluster.

        :returns: a response
        :rtype: ListISCSISessionsResult
        """

        params = {}

        return self.send_request(
            'ListISCSISessions',
            ListISCSISessionsResult,
            params,
        )

    def list_volumes(
            self,
            start_volume_id=OPTIONAL,
            limit=OPTIONAL,
            volume_status=OPTIONAL,
            accounts=OPTIONAL,
            is_paired=OPTIONAL,
            volume_ids=OPTIONAL,):
        """
        The *list_volumes* method is used to return a list of volumes that are
        in a cluster.
        You can specify the volumes you want to return in the list by using the
        available parameters.

        :param start_volume_id: (optional) The ID of the first volume to list.
            This can be useful for paging results. By default, this starts at
            the lowest VolumeID.
        :type start_volume_id: int

        :param limit: (optional) The maximum number of volumes to return from
            the API.
        :type limit: int

        :param volume_status: (optional) If specified, filter to only volumes
            with the provided status. By default, list all volumes.
        :type volume_status: str

        :param accounts: (optional) If specified, only fetch volumes which
            belong to the provided accounts. By default, list volumes for all
            accounts.
        :type accounts: int[]

        :param is_paired: (optional) If specified, only fetch volumes which are
            paired (if true) or non-paired (if false). By default, list all
            volumes regardless of their pairing status.
        :type is_paired: bool

        :param volume_ids: (optional) If specified, only fetch volumes
            specified in this list. This option cannot be specified if
            *start_volume_id,* limit, or accounts option is specified.
        :type volume_ids: int[]

        :returns: a response
        :rtype: ListVolumesResult
        """

        params = {}
        self._check_param_versions(
            'list_volumes',
            [
                ("volume_ids",
                 volume_ids, 9.0, None),
            ]
        )
        if start_volume_id is not None:
            params["startVolumeID"] = start_volume_id
        if limit is not None:
            params["limit"] = limit
        if volume_status is not None:
            params["volumeStatus"] = volume_status
        if accounts is not None:
            params["accounts"] = accounts
        if is_paired is not None:
            params["isPaired"] = is_paired
        if volume_ids is not None:
            params["volumeIDs"] = volume_ids

        return self.send_request(
            'ListVolumes',
            ListVolumesResult,
            params,
            since=8.0,
        )

    def list_volumes_for_account(
            self,
            account_id,
            start_volume_id=OPTIONAL,
            limit=OPTIONAL,):
        """
        *list_volumes_for_account* returns the list of active AND (pending)
        deleted volumes for an account.

        :param account_id: [required] The ID of the account to list the volumes
            for.
        :type account_id: int

        :param start_volume_id: (optional) The ID of the first volume to list.
            This can be useful for paging results. By default, this starts at
            the lowest VolumeID.
        :type start_volume_id: int

        :param limit: (optional) The maximum number of volumes to return from
            the API.
        :type limit: int

        :returns: a response
        :rtype: ListVolumesForAccountResult
        """

        params = {
            "accountID": account_id,
        }
        if start_volume_id is not None:
            params["startVolumeID"] = start_volume_id
        if limit is not None:
            params["limit"] = limit

        return self.send_request(
            'ListVolumesForAccount',
            ListVolumesForAccountResult,
            params,
            deprecated=8.0
        )

    def list_volume_stats_by_account(
            self,):
        """
        *list_volume_stats_by_account* returns high-level activity measurements
        for every account.
        Values are summed from all the volumes owned by the account.

        :returns: a response
        :rtype: ListVolumeStatsByAccountResult
        """

        params = {}

        return self.send_request(
            'ListVolumeStatsByAccount',
            ListVolumeStatsByAccountResult,
            params,
        )

    def list_volume_stats_by_volume(
            self,):
        """
        *list_volume_stats_by_volume* returns high-level activity measurements
        for every volume, by volume.
        Values are cumulative from the creation of the volume.

        :returns: a response
        :rtype: ListVolumeStatsByVolumeResult
        """

        params = {}

        return self.send_request(
            'ListVolumeStatsByVolume',
            ListVolumeStatsByVolumeResult,
            params,
        )

    def list_volume_stats_by_volume_access_group(
            self,
            volume_access_groups=OPTIONAL,):
        """
        *list_volume_stats_by_volume_access_group* is used to get total
        activity measurements for all of the volumes that are a member of the
        specified volume access group(s).

        :param volume_access_groups: (optional) An array of
            *volume_access_group_ids* for which volume activity is returned. If
            no *volume_access_group_id* is specified, stats for all volume
            access groups is returned.
        :type volume_access_groups: int[]

        :returns: a response
        :rtype: ListVolumeStatsByVolumeAccessGroupResult
        """

        params = {}
        if volume_access_groups is not None:
            params["volumeAccessGroups"] = volume_access_groups

        return self.send_request(
            'ListVolumeStatsByVolumeAccessGroup',
            ListVolumeStatsByVolumeAccessGroupResult,
            params,
        )

    def modify_volume(
            self,
            volume_id,
            account_id=OPTIONAL,
            access=OPTIONAL,
            set_create_time=OPTIONAL,
            qos=OPTIONAL,
            total_size=OPTIONAL,
            attributes=OPTIONAL,):
        """
        *modify_volume* is used to modify settings on an existing volume.
        Modifications can be made to one volume at a time and changes take
        place immediately.
        If an optional parameter is left unspecified, the value will not be
        changed.




        Extending the size of a volume that is being replicated should be done
        in an order.
        The target (Replication Target) volume should first be increased in
        size, then the source (Read/Write) volume can be resized.
        It is recommended that both the target and the source volumes be the
        same size.




        **Note**: If you change access status to locked or target all existing
        iSCSI connections are terminated.

        :param volume_id: [required] *volume_id* for the volume to be modified.
        :type volume_id: int

        :param account_id: (optional) *account_id* to which the volume is
            reassigned. If none is specified, the previous account name is
            used.
        :type account_id: int

        :param access: (optional) Access allowed for the volume.

            **readOnly**: Only read operations are allowed.

            **readWrite**: Reads and writes are allowed.

            **locked**: No reads or writes are allowed.

            **replicationTarget**: Identify a volume as the target volume for a
            paired set of volumes. If the volume is not paired, the access
            status is locked.

            If unspecified, the access settings of the clone will be the same
            as the source.

        :type access: str

        :param set_create_time: (optional) Identify the time at which the
            volume was created.
        :type set_create_time: str

        :param qos: (optional) New quality of service settings for this volume.
        :type qos: QoS

        :param total_size: (optional) New size of the volume in bytes. Size is
            rounded up to the nearest 1MiB size. This parameter can only be
            used to *increase* the size of a volume.
        :type total_size: int

        :param attributes: (optional) List of Name/Value pairs in JSON object
            format.
        :type attributes: dict

        :returns: a response
        :rtype: ModifyVolumeResult
        """

        params = {
            "volumeID": volume_id,
        }
        if account_id is not None:
            params["accountID"] = account_id
        if access is not None:
            params["access"] = access
        if set_create_time is not None:
            params["setCreateTime"] = set_create_time
        if qos is not None:
            params["qos"] = qos
        if total_size is not None:
            params["totalSize"] = total_size
        if attributes is not None:
            params["attributes"] = attributes

        return self.send_request(
            'ModifyVolume',
            ModifyVolumeResult,
            params,
        )

    def purge_deleted_volume(
            self,
            volume_id,):
        """
        *purge_deleted_volume* immediately and permanently purges a volume
        which has been deleted.
        A volume must be deleted using *delete_volume* before it can be purged.
        Volumes are purged automatically after a period of time, so usage of
        this method is not typically required.

        :param volume_id: [required] The ID of the volume to purge.
        :type volume_id: int

        :returns: a response
        :rtype: PurgeDeletedVolumeResult
        """

        params = {
            "volumeID": volume_id,
        }

        return self.send_request(
            'PurgeDeletedVolume',
            PurgeDeletedVolumeResult,
            params,
        )

    def restore_deleted_volume(
            self,
            volume_id,):
        """
        *restore_deleted_volume* marks a deleted volume as active again.
        This action makes the volume immediately available for iSCSI
        connection.

        :param volume_id: [required] *volume_id* for the deleted volume to
            restore.
        :type volume_id: int

        :returns: a response
        :rtype: RestoreDeletedVolumeResult
        """

        params = {
            "volumeID": volume_id,
        }

        return self.send_request(
            'RestoreDeletedVolume',
            RestoreDeletedVolumeResult,
            params,
        )

    def start_bulk_volume_read(
            self,
            volume_id,
            format,
            snapshot_id=OPTIONAL,
            script=OPTIONAL,
            script_parameters=OPTIONAL,
            attributes=OPTIONAL,):
        """
        *start_bulk_volume_read* allows you to initialize a bulk volume read
        session on a specified volume.
        Only two bulk volume processes can run simultaneously on a volume.
        When you initialize the session, data is read from a SolidFire storage
        volume for the purposes of storing the data on an external backup
        source.
        The external data is accessed by a web server running on a SolidFire
        node.
        Communications and server interaction information for external data
        access is passed by a script running on the SolidFire storage system.







        At the start of a bulk volume read operation, a snapshot of the volume
        is made and the snapshot is deleted when the read has completed.
        You can also read a snapshot of the volume by entering the ID of the
        snapshot as a parameter.
        Reading a previous snapshot does not create a new snapshot of the
        volume, nor does the previous snapshot be deleted when the read
        completes.







        **Note**: This process creates a new snapshot if the ID of an existing
        snapshot is not provided.
        Snapshots can be created if cluster fullness is at stage 2 or 3.
        Snapshots are not created when cluster fullness is at stage 4 or 5.

        :param volume_id: [required] ID of the volume to be read.
        :type volume_id: int

        :param format: [required] The format of the volume data. Can be either:

            **uncompressed**: every byte of the volume is returned without any
            compression.

            **native**: opaque data is returned that is smaller and more
            efficiently stored and written on a subsequent bulk volume write.

        :type format: str

        :param snapshot_id: (optional) ID of a previously created snapshot used
            for bulk volume reads. If no ID is entered, a snapshot of the
            current active volume image is made.
        :type snapshot_id: int

        :param script: (optional) Executable name of a script. If no script
            name is given then the key and URL is necessary to access SolidFire
            nodes. The script is run on the primary node and the key and URL is
            returned to the script so the local web server can be contacted.
        :type script: str

        :param script_parameters: (optional) JSON parameters to pass to the
            script.
        :type script_parameters: str

        :param attributes: (optional) JSON attributes for the bulk volume job.
        :type attributes: dict

        :returns: a response
        :rtype: StartBulkVolumeReadResult
        """

        params = {
            "volumeID": volume_id,
            "format": format,
        }
        if snapshot_id is not None:
            params["snapshotID"] = snapshot_id
        if script is not None:
            params["script"] = script
        if script_parameters is not None:
            params["scriptParameters"] = script_parameters
        if attributes is not None:
            params["attributes"] = attributes

        return self.send_request(
            'StartBulkVolumeRead',
            StartBulkVolumeReadResult,
            params,
        )

    def start_bulk_volume_write(
            self,
            volume_id,
            format,
            script=OPTIONAL,
            script_parameters=OPTIONAL,
            attributes=OPTIONAL,):
        """
        *start_bulk_volume_write* allows you to initialize a bulk volume write
        session on a specified volume.
        Only two bulk volume processes can run simultaneously on a volume.
        When the session is initialized, data can be written to a SolidFire
        storage volume from an external backup source.
        The external data is accessed by a web server running on a SolidFire
        node.
        Communications and server interaction information for external data
        access is passed by a script running on the SolidFire storage system.

        :param volume_id: [required] ID of the volume to be written to.
        :type volume_id: int

        :param format: [required] The format of the volume data. Can be either:

            **uncompressed**: every byte of the volume is returned without any
            compression.

            **native**: opaque data is returned that is smaller and more
            efficiently stored and written on a subsequent bulk volume write

        :type format: str

        :param script: (optional) Executable name of a script. If no script
            name is given then the key and URL are necessary to access
            SolidFire nodes. The script runs on the primary node and the key
            and URL is returned to the script so the local web server can be
            contacted.
        :type script: str

        :param script_parameters: (optional) JSON parameters to pass to the
            script.
        :type script_parameters: str

        :param attributes: (optional) JSON attributes for the bulk volume job.
        :type attributes: dict

        :returns: a response
        :rtype: StartBulkVolumeWriteResult
        """

        params = {
            "volumeID": volume_id,
            "format": format,
        }
        if script is not None:
            params["script"] = script
        if script_parameters is not None:
            params["scriptParameters"] = script_parameters
        if attributes is not None:
            params["attributes"] = attributes

        return self.send_request(
            'StartBulkVolumeWrite',
            StartBulkVolumeWriteResult,
            params,
        )

    def update_bulk_volume_status(
            self,
            key,
            status,
            percent_complete=OPTIONAL,
            message=OPTIONAL,
            attributes=OPTIONAL,):
        """
        You can use *update_bulk_volume_status* in a script to return to the
        SolidFire system the status of a bulk volume job that you have started
        with the *\"start_bulk_volume_read\"* or *\"start_bulk_volume_write\"*
        methods.

        :param key: [required] The key assigned during initialization of a
            \"StartBulkVolumeRead\" or \"StartBulkVolumeWrite\" session.
        :type key: str

        :param status: [required] The SolidFire system sets the status of the
            given bulk volume job.

            Possible values:



            **running**: jobs that are still active.

            **complete**: jobs that are done. failed - jobs that have failed.

            **failed**: jobs that have failed.

        :type status: str

        :param percent_complete: (optional) The completed progress of the bulk
            volume job as a percentage.
        :type percent_complete: str

        :param message: (optional) Returns the status of the bulk volume job
            when the job has completed.
        :type message: str

        :param attributes: (optional) JSON attributes  updates what is on the
            bulk volume job.
        :type attributes: dict

        :returns: a response
        :rtype: UpdateBulkVolumeStatusResult
        """

        params = {
            "key": key,
            "status": status,
        }
        if percent_complete is not None:
            params["percentComplete"] = percent_complete
        if message is not None:
            params["message"] = message
        if attributes is not None:
            params["attributes"] = attributes

        return self.send_request(
            'UpdateBulkVolumeStatus',
            UpdateBulkVolumeStatusResult,
            params,
        )

    def create_volume_access_group(
            self,
            name,
            initiators=OPTIONAL,
            volumes=OPTIONAL,
            virtual_network_id=OPTIONAL,
            virtual_network_tags=OPTIONAL,
            attributes=OPTIONAL,):
        """
        Creates a new volume access group.
        The new volume access group must be given a name when it is created.
        Entering initiators and volumes are optional when creating a volume
        access group.
        Once the group is created volumes and initiator IQNs can be added.
        Any initiator IQN that is successfully added to the volume access group
        is able to access any volume in the group without CHAP authentication.

        :param name: [required] Name of the volume access group. It is not
            required to be unique, but recommended.
        :type name: str

        :param initiators: (optional) List of initiators to include in the
            volume access group. If unspecified, the access group will start
            out without configured initiators.
        :type initiators: str[]

        :param volumes: (optional) List of volumes to initially include in the
            volume access group. If unspecified, the access group will start
            without any volumes.
        :type volumes: int[]

        :param virtual_network_id: (optional) The ID of the SolidFire Virtual
            Network ID to associate the volume access group with.
        :type virtual_network_id: int[]

        :param virtual_network_tags: (optional) The ID of the VLAN Virtual
            Network Tag to associate the volume access group with.
        :type virtual_network_tags: int[]

        :param attributes: (optional) List of Name/Value pairs in JSON object
            format.
        :type attributes: dict

        :returns: a response
        :rtype: CreateVolumeAccessGroupResult
        """

        params = {
            "name": name,
        }
        self._check_param_versions(
            'create_volume_access_group',
            [
                ("virtual_network_id",
                 virtual_network_id, 8.0, None),
                ("virtual_network_tags",
                 virtual_network_tags, 8.0, None),
            ]
        )
        if initiators is not None:
            params["initiators"] = initiators
        if volumes is not None:
            params["volumes"] = volumes
        if virtual_network_id is not None:
            params["virtualNetworkID"] = virtual_network_id
        if virtual_network_tags is not None:
            params["virtualNetworkTags"] = virtual_network_tags
        if attributes is not None:
            params["attributes"] = attributes

        return self.send_request(
            'CreateVolumeAccessGroup',
            CreateVolumeAccessGroupResult,
            params,
        )

    def list_volume_access_groups(
            self,
            start_volume_access_group_id=OPTIONAL,
            limit=OPTIONAL,):
        """
        *list_volume_access_groups* is used to return information about the
        volume access groups that are currently in the system.

        :param start_volume_access_group_id: (optional) The lowest
            *volume_access_group_id* to return. This can be useful for paging.
            If unspecified, there is no lower limit (implicitly 0).
        :type start_volume_access_group_id: int

        :param limit: (optional) The maximum number of results to return. This
            can be useful for paging.
        :type limit: int

        :returns: a response
        :rtype: ListVolumeAccessGroupsResult
        """

        params = {}
        if start_volume_access_group_id is not None:
            params["startVolumeAccessGroupID"] = start_volume_access_group_id
        if limit is not None:
            params["limit"] = limit

        return self.send_request(
            'ListVolumeAccessGroups',
            ListVolumeAccessGroupsResult,
            params,
        )

    def delete_volume_access_group(
            self,
            volume_access_group_id,):
        """
        Delete a volume access group from the system.

        :param volume_access_group_id: [required] The ID of the volume access
            group to delete.
        :type volume_access_group_id: int

        :returns: a response
        :rtype: DeleteVolumeAccessGroupResult
        """

        params = {
            "volumeAccessGroupID": volume_access_group_id,
        }

        return self.send_request(
            'DeleteVolumeAccessGroup',
            DeleteVolumeAccessGroupResult,
            params,
        )

    def modify_volume_access_group(
            self,
            volume_access_group_id,
            virtual_network_id=OPTIONAL,
            virtual_network_tags=OPTIONAL,
            name=OPTIONAL,
            initiators=OPTIONAL,
            volumes=OPTIONAL,
            attributes=OPTIONAL,):
        """
        Update initiators and add or remove volumes from a volume access group.
        A specified initiator or volume that duplicates an existing volume or
        initiator in a volume access group is left as-is.
        If a value is not specified for volumes or initiators, the current list
        of initiators and volumes are not changed.




        Often, it is easier to use the convenience functions to modify
        initiators and volumes independently:




        *add_initiators_to_volume_access_group*



        *remove_initiators_from_volume_access_group*



        *add_volumes_to_volume_access_group*



        *remove_volumes_from_volume_access_group*




        :param volume_access_group_id: [required] The ID of the volume access
            group to modify.
        :type volume_access_group_id: int

        :param virtual_network_id: (optional) The ID of the SolidFire Virtual
            Network ID to associate the volume access group with.
        :type virtual_network_id: int[]

        :param virtual_network_tags: (optional) The ID of the VLAN Virtual
            Network Tag to associate the volume access group with.
        :type virtual_network_tags: int[]

        :param name: (optional) Name of the volume access group. It is not
            required to be unique, but recommended.
        :type name: str

        :param initiators: (optional) List of initiators to include in the
            volume access group. If unspecified, the access group&#39;s
            configured initiators will not be modified.
        :type initiators: str[]

        :param volumes: (optional) List of volumes to initially include in the
            volume access group. If unspecified, the access group&#39;s volumes
            will not be modified.
        :type volumes: int[]

        :param attributes: (optional) List of Name/Value pairs in JSON object
            format.
        :type attributes: dict

        :returns: a response
        :rtype: ModifyVolumeAccessGroupResult
        """

        params = {
            "volumeAccessGroupID": volume_access_group_id,
        }
        self._check_param_versions(
            'modify_volume_access_group',
            [
                ("virtual_network_id",
                 virtual_network_id, 8.0, None),
                ("virtual_network_tags",
                 virtual_network_tags, 8.0, None),
            ]
        )
        if virtual_network_id is not None:
            params["virtualNetworkID"] = virtual_network_id
        if virtual_network_tags is not None:
            params["virtualNetworkTags"] = virtual_network_tags
        if name is not None:
            params["name"] = name
        if initiators is not None:
            params["initiators"] = initiators
        if volumes is not None:
            params["volumes"] = volumes
        if attributes is not None:
            params["attributes"] = attributes

        return self.send_request(
            'ModifyVolumeAccessGroup',
            ModifyVolumeAccessGroupResult,
            params,
        )

    def add_initiators_to_volume_access_group(
            self,
            volume_access_group_id,
            initiators,):
        """
        Add initiators to a volume access group.

        :param volume_access_group_id: [required] The ID of the volume access
            group to modify.
        :type volume_access_group_id: int

        :param initiators: [required] List of initiators to add to the volume
            access group.
        :type initiators: str[]

        :returns: a response
        :rtype: ModifyVolumeAccessGroupResult
        """

        params = {
            "volumeAccessGroupID": volume_access_group_id,
            "initiators": initiators,
        }

        return self.send_request(
            'AddInitiatorsToVolumeAccessGroup',
            ModifyVolumeAccessGroupResult,
            params,
        )

    def remove_initiators_from_volume_access_group(
            self,
            volume_access_group_id,
            initiators,):
        """
        Remove initiators from a volume access group.

        :param volume_access_group_id: [required] The ID of the volume access
            group to modify.
        :type volume_access_group_id: int

        :param initiators: [required] List of initiators to remove from the
            volume access group.
        :type initiators: str[]

        :returns: a response
        :rtype: ModifyVolumeAccessGroupResult
        """

        params = {
            "volumeAccessGroupID": volume_access_group_id,
            "initiators": initiators,
        }

        return self.send_request(
            'RemoveInitiatorsFromVolumeAccessGroup',
            ModifyVolumeAccessGroupResult,
            params,
        )

    def add_volumes_to_volume_access_group(
            self,
            volume_access_group_id,
            volumes,):
        """
        Add volumes to a volume access group.

        :param volume_access_group_id: [required] The ID of the volume access
            group to modify.
        :type volume_access_group_id: int

        :param volumes: [required] List of volumes to add to this volume access
            group.
        :type volumes: int[]

        :returns: a response
        :rtype: ModifyVolumeAccessGroupResult
        """

        params = {
            "volumeAccessGroupID": volume_access_group_id,
            "volumes": volumes,
        }

        return self.send_request(
            'AddVolumesToVolumeAccessGroup',
            ModifyVolumeAccessGroupResult,
            params,
        )

    def remove_volumes_from_volume_access_group(
            self,
            volume_access_group_id,
            volumes,):
        """
        Remove volumes from a volume access group.

        :param volume_access_group_id: [required] The ID of the volume access
            group to modify.
        :type volume_access_group_id: int

        :param volumes: [required] List of volumes to remove from this volume
            access group.
        :type volumes: int[]

        :returns: a response
        :rtype: ModifyVolumeAccessGroupResult
        """

        params = {
            "volumeAccessGroupID": volume_access_group_id,
            "volumes": volumes,
        }

        return self.send_request(
            'RemoveVolumesFromVolumeAccessGroup',
            ModifyVolumeAccessGroupResult,
            params,
        )

    def get_volume_access_group_efficiency(
            self,
            volume_access_group_id,):
        """
        *get_volume_access_group_efficiency* is used to retrieve efficiency
        information about a volume access group. Only the volume access group
        provided as parameters in this API method is used to compute the
        capacity.

        :param volume_access_group_id: [required] Specifies the volume access
            group for which capacity is computed.
        :type volume_access_group_id: int

        :returns: a response
        :rtype: GetEfficiencyResult
        """

        params = {
            "volumeAccessGroupID": volume_access_group_id,
        }

        return self.send_request(
            'GetVolumeAccessGroupEfficiency',
            GetEfficiencyResult,
            params,
        )

    def get_volume_access_group_lun_assignments(
            self,
            volume_access_group_id,):
        """
        The *get_volume_access_group_lun_assignments* is used to return
        information LUN mappings of a specified volume access group.

        :param volume_access_group_id: [required] Unique volume access group ID
            used to return information.
        :type volume_access_group_id: int

        :returns: a response
        :rtype: GetVolumeAccessGroupLunAssignmentsResult
        """

        params = {
            "volumeAccessGroupID": volume_access_group_id,
        }

        return self.send_request(
            'GetVolumeAccessGroupLunAssignments',
            GetVolumeAccessGroupLunAssignmentsResult,
            params,
        )

    def modify_volume_access_group_lun_assignments(
            self,
            volume_access_group_id,
            lun_assignments,):
        """
        The *modifyt_volume_access_group_lun_assignments* is used to define
        custom LUN assignments for specific volumes. Only LUN values set on the
        *lun_assignments* parameter will be changed in the volume access group.
        All other LUN assignments will remain unchanged.




        LUN assignment values must be unique for volumes in a volume access
        group. An exception will be seen if LUN assignments are duplicated in a
        volume access group. However, the same LUN values can be used again in
        different volume access groups.




        **Note:** Correct LUN values are 0 - 16383. An exception will be seen
        if an incorrect LUN value is passed. None of the specified LUN
        assignments will be modified if there is an exception.




        **Caution:** If a LUN assignment is changed for a volume with active
        I/O, the I/O could be disrupted. Changes to the server configuration
        may be required in order to change volume LUN assignments.

        :param volume_access_group_id: [required] Unique volume access group ID
            for which the LUN assignments will be modified.
        :type volume_access_group_id: int

        :param lun_assignments: [required] The volume *ids* with new assigned
            LUN values.
        :type lun_assignments: LunAssignment[]

        :returns: a response
        :rtype: ModifyVolumeAccessGroupLunAssignmentsResult
        """

        params = {
            "volumeAccessGroupID": volume_access_group_id,
            "lunAssignments": lun_assignments,
        }

        return self.send_request(
            'ModifyVolumeAccessGroupLunAssignments',
            ModifyVolumeAccessGroupLunAssignmentsResult,
            params,
        )
