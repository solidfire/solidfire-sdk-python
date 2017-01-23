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
    ApiVersionUnsupportedError, ApiParameterVersionError

from solidfire.models import *

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

    def get_account_by_id(
            self,
            account_id,):
        """
        Returns details about an account, given its AccountID.
        :param accountID: [required] Specifies the account for which details are gathered. 
        :type accountID: int
        """

        self._check_connection_type("get_account_by_id", "Cluster")

        params = { 
            "accountID": account_id,
        }
        
        # There is no adaptor.
        return self.send_request(
            'GetAccountByID',
            GetAccountResult,
            params,
            since=1
        )

    def get_account_by_name(
            self,
            username,):
        """
        Returns details about an account, given its Username.
        :param username: [required] Username for the account. 
        :type username: str
        """

        self._check_connection_type("get_account_by_name", "Cluster")

        params = { 
            "username": username,
        }
        
        # There is no adaptor.
        return self.send_request(
            'GetAccountByName',
            GetAccountResult,
            params,
            since=1
        )

    def get_account_efficiency(
            self,
            account_id,):
        """
        GetAccountEfficiency is used to retrieve information about a volume account. Only the account given as a parameter in this API method is used to compute the capacity.
        :param accountID: [required] Specifies the volume account for which capacity is computed. 
        :type accountID: int
        """

        self._check_connection_type("get_account_efficiency", "Cluster")

        params = { 
            "accountID": account_id,
        }
        
        # There is no adaptor.
        return self.send_request(
            'GetAccountEfficiency',
            GetEfficiencyResult,
            params,
            since=6
        )

    def list_accounts(
            self,
            start_account_id=OPTIONAL,
            limit=OPTIONAL,):
        """
        Returns the entire list of accounts, with optional paging support.
        :param startAccountID:  Starting AccountID to return. If no Account exists with this AccountID, the next Account by AccountID order is used as the start of the list. To page through the list, pass the AccountID of the last Account in the previous response + 1 
        :type startAccountID: int

        :param limit:  Maximum number of AccountInfo objects to return. 
        :type limit: int
        """

        self._check_connection_type("list_accounts", "Cluster")

        params = { 
        }
        if start_account_id is not None:
            params["startAccountID"] = start_account_id
        if limit is not None:
            params["limit"] = limit
        
        # There is no adaptor.
        return self.send_request(
            'ListAccounts',
            ListAccountsResult,
            params,
            since=1
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
        When locking an account, any existing connections from that account are immediately terminated.
        When changing CHAP settings, any existing connections continue to be active,
        and the new CHAP values are only used on subsequent connection or reconnection.
        :param accountID: [required] AccountID for the account to modify. 
        :type accountID: int

        :param username:  Change the username of the account to this value. 
        :type username: str

        :param status:  Status of the account. 
        :type status: str

        :param initiatorSecret:  CHAP secret to use for the initiator. Should be 12-16 characters long and impenetrable. 
        :type initiatorSecret: CHAPSecret

        :param targetSecret:  CHAP secret to use for the target (mutual CHAP authentication). Should be 12-16 characters long and impenetrable. 
        :type targetSecret: CHAPSecret

        :param attributes:  List of Name/Value pairs in JSON object format. 
        :type attributes: dict
        """

        self._check_connection_type("modify_account", "Cluster")

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
        
        # There is no adaptor.
        return self.send_request(
            'ModifyAccount',
            ModifyAccountResult,
            params,
            since=1
        )

    def remove_account(
            self,
            account_id,):
        """
        Used to remove an existing account.
        All Volumes must be deleted and purged on the account before it can be removed.
        If volumes on the account are still pending deletion, RemoveAccount cannot be used until DeleteVolume to delete and purge the volumes.
        :param accountID: [required] AccountID for the account to remove. 
        :type accountID: int
        """

        self._check_connection_type("remove_account", "Cluster")

        params = { 
            "accountID": account_id,
        }
        
        # There is no adaptor.
        return self.send_request(
            'RemoveAccount',
            RemoveAccountResult,
            params,
            since=1
        )

    def add_account(
            self,
            username,
            initiator_secret=OPTIONAL,
            target_secret=OPTIONAL,
            attributes=OPTIONAL,):
        """
        Used to add a new account to the system.
        New volumes can be created under the new account.
        The CHAP settings specified for the account applies to all volumes owned by the account.
        :param username: [required] Unique username for this account. (May be 1 to 64 characters in length). 
        :type username: str

        :param initiatorSecret:  CHAP secret to use for the initiator. Should be 12-16 characters long and impenetrable. The CHAP initiator secrets must be unique and cannot be the same as the target CHAP secret.  If not specified, a random secret is created. 
        :type initiatorSecret: CHAPSecret

        :param targetSecret:  CHAP secret to use for the target (mutual CHAP authentication). Should be 12-16 characters long and impenetrable. The CHAP target secrets must be unique and cannot be the same as the initiator CHAP secret.  If not specified, a random secret is created. 
        :type targetSecret: CHAPSecret

        :param attributes:  List of Name/Value pairs in JSON object format. 
        :type attributes: dict
        """

        self._check_connection_type("add_account", "Cluster")

        params = { 
            "username": username,
        }
        if initiator_secret is not None:
            params["initiatorSecret"] = initiator_secret
        if target_secret is not None:
            params["targetSecret"] = target_secret
        if attributes is not None:
            params["attributes"] = attributes
        
        # There is no adaptor.
        return self.send_request(
            'AddAccount',
            AddAccountResult,
            params,
            since=1
        )

    def create_backup_target(
            self,
            name,
            attributes=OPTIONAL,):
        """
        CreateBackupTarget allows you to create and store backup target information so that you do not need to re-enter it each time a backup is created.
        :param name: [required] Name for the backup target. 
        :type name: str

        :param attributes:  List of Name/Value pairs in JSON object format. 
        :type attributes: dict
        """

        self._check_connection_type("create_backup_target", "Cluster")

        params = { 
            "name": name,
        }
        if attributes is not None:
            params["attributes"] = attributes
        
        # There is no adaptor.
        return self.send_request(
            'CreateBackupTarget',
            CreateBackupTargetResult,
            params,
            since=6
        )

    def get_backup_target(
            self,
            backup_target_id,):
        """
        GetBackupTarget allows you to return information about a specific backup target that has been created.
        :param backupTargetID: [required] Unique identifier assigned to the backup target. 
        :type backupTargetID: int
        """

        self._check_connection_type("get_backup_target", "Cluster")

        params = { 
            "backupTargetID": backup_target_id,
        }
        
        # There is no adaptor.
        return self.send_request(
            'GetBackupTarget',
            GetBackupTargetResult,
            params,
            since=6
        )

    def list_backup_targets(
            self,):
        """
        You can use ListBackupTargets to retrieve information about all backup targets that have been created.        """

        self._check_connection_type("list_backup_targets", "Cluster")

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'ListBackupTargets',
            ListBackupTargetsResult,
            params,
            since=6
        )

    def modify_backup_target(
            self,
            backup_target_id,
            name=OPTIONAL,
            attributes=OPTIONAL,):
        """
        ModifyBackupTarget is used to change attributes of a backup target.
        :param backupTargetID: [required] Unique identifier assigned to the backup target. 
        :type backupTargetID: int

        :param name:  Name for the backup target. 
        :type name: str

        :param attributes:  List of Name/Value pairs in JSON object format. 
        :type attributes: dict
        """

        self._check_connection_type("modify_backup_target", "Cluster")

        params = { 
            "backupTargetID": backup_target_id,
        }
        if name is not None:
            params["name"] = name
        if attributes is not None:
            params["attributes"] = attributes
        
        # There is no adaptor.
        return self.send_request(
            'ModifyBackupTarget',
            ModifyBackupTargetResult,
            params,
            since=6
        )

    def remove_backup_target(
            self,
            backup_target_id,):
        """
        RemoveBackupTarget allows you to delete backup targets.
        :param backupTargetID: [required] Unique target ID of the target to remove. 
        :type backupTargetID: int
        """

        self._check_connection_type("remove_backup_target", "Cluster")

        params = { 
            "backupTargetID": backup_target_id,
        }
        
        # There is no adaptor.
        return self.send_request(
            'RemoveBackupTarget',
            RemoveBackupTargetResult,
            params,
            since=6
        )

    def modify_cluster_full_threshold(
            self,
            stage2_aware_threshold=OPTIONAL,
            stage3_block_threshold_percent=OPTIONAL,
            max_metadata_over_provision_factor=OPTIONAL,):
        """
        ModifyClusterFullThreshold is used to change the level at which an event is generated when the storage cluster approaches the capacity utilization requested. The number entered in this setting is used to indicate the number of node failures the system is required to recover from. For example, on a 10 node cluster, if you want to be alerted when the system cannot recover from 3 nodes failures, enter the value of "3". When this number is reached, a message alert is sent to the Event Log in the Cluster Management Console.
        :param stage2AwareThreshold:  Number of nodes worth of capacity remaining on the cluster that triggers a notification. 
        :type stage2AwareThreshold: int

        :param stage3BlockThresholdPercent:  Percent below "Error" state to raise a cluster "Warning" alert. 
        :type stage3BlockThresholdPercent: int

        :param maxMetadataOverProvisionFactor:  A value representative of the number of times metadata space can be over provisioned relative to the amount of space available. For example, if there was enough metadata space to store 100 TiB of volumes and this number was set to 5, then 500 TiB worth of volumes could be created. 
        :type maxMetadataOverProvisionFactor: int
        """

        self._check_connection_type("modify_cluster_full_threshold", "Cluster")

        params = { 
        }
        if stage2_aware_threshold is not None:
            params["stage2AwareThreshold"] = stage2_aware_threshold
        if stage3_block_threshold_percent is not None:
            if self.api_version < 8.0:
                raise ApiParameterVersionError("modify_cluster_full_threshold", 8.0,
                    [("stage3_block_threshold_percent", stage3_block_threshold_percent, 8.0, False)])
            else:
                params["stage3BlockThresholdPercent"] = stage3_block_threshold_percent
        if max_metadata_over_provision_factor is not None:
            params["maxMetadataOverProvisionFactor"] = max_metadata_over_provision_factor
        
        # There is no adaptor.
        return self.send_request(
            'ModifyClusterFullThreshold',
            ModifyClusterFullThresholdResult,
            params,
            since=1
        )

    def remove_cluster_admin(
            self,
            cluster_admin_id,):
        """
        RemoveClusterAdmin is used to remove a Cluster Admin. The "admin" Cluster Admin cannot be removed.
        :param clusterAdminID: [required] ClusterAdminID for the Cluster Admin to remove. 
        :type clusterAdminID: int
        """

        self._check_connection_type("remove_cluster_admin", "Cluster")

        params = { 
            "clusterAdminID": cluster_admin_id,
        }
        
        # There is no adaptor.
        return self.send_request(
            'RemoveClusterAdmin',
            RemoveClusterAdminResult,
            params,
            since=1
        )

    def set_ntp_info(
            self,
            servers,
            broadcastclient=OPTIONAL,):
        """
        SetNtpInfo is used to configure the NTP on cluster nodes. The values set with this interface apply to all nodes in the cluster. The nodes can only be configured as a server where a host is selected to administrate the networking and/or a broadcast client where each host sends each message to each peer.
        :param servers: [required] List of NTP servers to add to each node's NTP configuration. 
        :type servers: str

        :param broadcastclient:  Enable every node in the cluster as a broadcase client. 
        :type broadcastclient: bool
        """

        self._check_connection_type("set_ntp_info", "Cluster")

        params = { 
            "servers": servers,
        }
        if broadcastclient is not None:
            params["broadcastclient"] = broadcastclient
        
        # There is no adaptor.
        return self.send_request(
            'SetNtpInfo',
            SetNtpInfoResult,
            params,
            since=1
        )

    def set_snmp_acl(
            self,
            networks,
            usm_users,):
        """
        SetSnmpACL is used to configure SNMP access permissions on the cluster nodes. The values set with this interface apply to all nodes in the cluster, and the values that are passed replace, in whole, all values set in any previous call to SetSnmpACL. Also note that the values set with this interface replace all "network" or "usmUsers" values set with the older SetSnmpInfo.
        :param networks: [required] List of networks and what type of access they have to the SNMP servers running on the cluster nodes. See SNMP Network Object for possible "networks" values. REQUIRED if SNMP v# is disabled. 
        :type networks: SnmpNetwork

        :param usmUsers: [required] List of users and the type of access they have to the SNMP servers running on the cluster nodes. REQUIRED if SNMP v3 is enabled. 
        :type usmUsers: SnmpV3UsmUser
        """

        self._check_connection_type("set_snmp_acl", "Cluster")

        params = { 
            "networks": networks,
            "usmUsers": usm_users,
        }
        
        # There is no adaptor.
        return self.send_request(
            'SetSnmpACL',
            SetSnmpACLResult,
            params,
            since=8
        )

    def set_snmp_trap_info(
            self,
            trap_recipients,
            cluster_fault_traps_enabled,
            cluster_fault_resolved_traps_enabled,
            cluster_event_traps_enabled,):
        """
        SetSnmpTrapInfo is used to enable and disable the generation of SolidFire SNMP notifications (traps) and to specify the set of network host computers that are to receive the notifications. The values passed with each SetSnmpTrapInfo method replaces all values set in any previous method to SetSnmpTrapInfo.
        :param trapRecipients: [required] List of hosts that are to receive the traps generated by the Cluster Master. At least one object is required if any one of the trap types is enabled. 
        :type trapRecipients: SnmpTrapRecipient

        :param clusterFaultTrapsEnabled: [required] If "true", when a cluster fault is logged a corresponding solidFireClusterFaultNotification is sent to the configured list of trap recipients. 
        :type clusterFaultTrapsEnabled: bool

        :param clusterFaultResolvedTrapsEnabled: [required] If "true", when a cluster fault is logged a corresponding solidFireClusterFaultResolvedNotification is sent to the configured list of trap recipients. 
        :type clusterFaultResolvedTrapsEnabled: bool

        :param clusterEventTrapsEnabled: [required] If "true", when a cluster fault is logged a corresponding solidFireClusterEventNotification is sent to the configured list of trap recipients. 
        :type clusterEventTrapsEnabled: bool
        """

        self._check_connection_type("set_snmp_trap_info", "Cluster")

        params = { 
            "trapRecipients": trap_recipients,
            "clusterFaultTrapsEnabled": cluster_fault_traps_enabled,
            "clusterFaultResolvedTrapsEnabled": cluster_fault_resolved_traps_enabled,
            "clusterEventTrapsEnabled": cluster_event_traps_enabled,
        }
        
        # There is no adaptor.
        return self.send_request(
            'SetSnmpTrapInfo',
            SetSnmpTrapInfoResult,
            params,
            since=5
        )

    def snmp_send_test_traps(
            self,):
        """
        SnmpSendTestTraps enables you to test SNMP functionality for a cluster. This method instructs the cluster to send test SNMP traps to the currently configured SNMP manager.        """

        self._check_connection_type("snmp_send_test_traps", "Cluster")

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'SnmpSendTestTraps',
            SnmpSendTestTrapsResult,
            params,
            since=6
        )

    def add_cluster_admin(
            self,
            username,
            password,
            access,
            accept_eula=OPTIONAL,
            attributes=OPTIONAL,):
        """
        AddClusterAdmin adds a new Cluster Admin. A Cluster Admin can be used to manage the cluster via the API and management tools. Cluster Admins are completely separate and unrelated to standard tenant accounts.
        
        Each Cluster Admin can be restricted to a sub-set of the API. SolidFire recommends using multiple Cluster Admins for different users and applications. Each Cluster Admin should be given the minimal permissions necessary to reduce the potential impact of credential compromise.
        :param username: [required] Unique username for this Cluster Admin. 
        :type username: str

        :param password: [required] Password used to authenticate this Cluster Admin. 
        :type password: str

        :param access: [required] Controls which methods this Cluster Admin can use. For more details on the levels of access, see "Access Control" in the Element API Guide. 
        :type access: str

        :param acceptEula:  Indicate your acceptance of the End User License Agreement when creating this cluster admin. To accept the EULA, set this parameter to true. 
        :type acceptEula: bool

        :param attributes:  List of Name/Value pairs in JSON object format. 
        :type attributes: dict
        """

        self._check_connection_type("add_cluster_admin", "Cluster")

        params = { 
            "username": username,
            "password": password,
            "access": access,
        }
        if accept_eula is not None:
            params["acceptEula"] = accept_eula
        if attributes is not None:
            params["attributes"] = attributes
        
        # There is no adaptor.
        return self.send_request(
            'AddClusterAdmin',
            AddClusterAdminResult,
            params,
            since=1
        )

    def clear_cluster_faults(
            self,
            fault_types=OPTIONAL,):
        """
        ClearClusterFaults is used to clear information about both current faults that are resolved as well as faults that were previously detected and resolved can be cleared.
        :param faultTypes:  Determines the types of faults cleared: current: Faults that are currently detected and have not been resolved. resolved: Faults that were previously detected and resolved. all: Both current and resolved faults are cleared. The fault status can be determined by the "resolved" field of the fault object. 
        :type faultTypes: str
        """

        self._check_connection_type("clear_cluster_faults", "Cluster")

        params = { 
        }
        if fault_types is not None:
            params["faultTypes"] = fault_types
        
        # There is no adaptor.
        return self.send_request(
            'ClearClusterFaults',
            ClearClusterFaultsResult,
            params,
            since=1
        )

    def create_cluster(
            self,
            mvip,
            svip,
            rep_count,
            username,
            password,
            nodes,
            accept_eula=OPTIONAL,
            attributes=OPTIONAL,):
        """
        The CreateCluster method is used to initialize the node in a cluster that has ownership of the "mvip" and "svip" addresses. Each new cluster is initialized using the MIP of the first node in the cluster. This method also automatically adds all the nodes being configured into the cluster. The method is used only once each time a new cluster is initialized.
        
        Note: You need to log into the node that is used as the master node for the cluster. Once logged in, run the GetBootstrapConfig method on the node to get the IP addresses for the rest of the nodes that you want to include in the cluster. Then run the CreateCluster method.
        :param acceptEula:  Indicate your acceptance of the End User License Agreement when creating this cluster. To accept the EULA, set this parameter to true. 
        :type acceptEula: bool

        :param mvip: [required] Floating (virtual) IP address for the cluster on the management network. 
        :type mvip: str

        :param svip: [required] Floating (virtual) IP address for the cluster on the storage (iSCSI) network. 
        :type svip: str

        :param repCount: [required] Number of replicas of each piece of data to store in the cluster. Valid value is "2". 
        :type repCount: int

        :param username: [required] User name for the cluster admin. 
        :type username: str

        :param password: [required] Initial password for the cluster admin account. 
        :type password: str

        :param nodes: [required] CIP/SIP addresses of the initial set of nodes making up the cluster. This node's IP must be in the list. 
        :type nodes: str

        :param attributes:  List of Name/Value pairs in JSON object format. 
        :type attributes: dict
        """

        self._check_connection_type("create_cluster", "Both")

        params = { 
            "mvip": mvip,
            "svip": svip,
            "repCount": rep_count,
            "username": username,
            "password": password,
            "nodes": nodes,
        }
        if accept_eula is not None:
            params["acceptEula"] = accept_eula
        if attributes is not None:
            params["attributes"] = attributes
        
        # There is no adaptor.
        return self.send_request(
            'CreateCluster',
            CreateClusterResult,
            params
        )

    def get_cluster_config(
            self,):
        """
        The GetClusterConfig API method is used to return information about the cluster configuration this node uses to communicate with the cluster it is a part of.
        
        Note: This method is available only through the per-node API endpoint 5.0 or later.        """

        self._check_connection_type("get_cluster_config", "Node")

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'GetClusterConfig',
            GetClusterConfigResult,
            params,
            since=5
        )

    def get_snmp_state(
            self,):
        """
        GetSnmpState is used to return the current state of the SNMP feature.
        
        Note: GetSnmpState is new for Element OS 8. Please use this method and SetSnmpACL to migrate your SNMP functionality in the future.        """

        self._check_connection_type("get_snmp_state", "Cluster")

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'GetSnmpState',
            GetSnmpStateResult,
            params,
            since=8
        )

    def set_cluster_config(
            self,
            cluster,):
        """
        The SetClusterConfig API method is used to set the configuration this node uses to communicate with the cluster it is associated with. To see the states in which these objects can be modified see Cluster Object on page 109. To display the current cluster interface settings for a node, run the GetClusterConfig API method.
        
        Note: This method is available only through the per-node API endpoint 5.0 or later.
        :param cluster: [required] Objects that are changed for the cluster interface settings. Only the fields you want changed need to be added to this method as objects in the "cluster" parameter. 
        :type cluster: ClusterConfig
        """

        self._check_connection_type("set_cluster_config", "Node")

        params = { 
            "cluster": cluster,
        }
        
        # There is no adaptor.
        return self.send_request(
            'SetClusterConfig',
            SetClusterConfigResult,
            params,
            since=5
        )

    def set_snmp_info(
            self,
            networks=OPTIONAL,
            enabled=OPTIONAL,
            snmp_v3_enabled=OPTIONAL,
            usm_users=OPTIONAL,):
        """
        SetSnmpInfo is used to configure SNMP v2 and v3 on the cluster nodes. The values set with this interface apply to all nodes in the cluster, and the values that are passed replace, in whole, all values set in any previous call to SetSnmpInfo.
        
        Note: EnableSnmp and SetSnmpACL methods can be used to accomplish the same results as SetSnmpInfo. SetSnmpInfo will no longer be available after the Element 8 release. Please use EnableSnmp and SetSnmpACL in the future.
        :param networks:  List of networks and what type of access they have to the SNMP servers running on the cluster nodes. See SNMP Network Object for possible "networks" values. SNMP v2 only. 
        :type networks: SnmpNetwork

        :param enabled:  If set to "true", then SNMP is enabled on each node in the cluster. 
        :type enabled: bool

        :param snmpV3Enabled:  If set to "true", then SNMP v3 is enabled on each node in the cluster. 
        :type snmpV3Enabled: bool

        :param usmUsers:  If SNMP v3 is enabled, this value must be passed in place of the "networks" parameter. SNMP v3 only. 
        :type usmUsers: SnmpV3UsmUser
        """

        self._check_connection_type("set_snmp_info", "Cluster")

        params = { 
        }
        if networks is not None:
            params["networks"] = networks
        if enabled is not None:
            params["enabled"] = enabled
        if snmp_v3_enabled is not None:
            params["snmpV3Enabled"] = snmp_v3_enabled
        if usm_users is not None:
            params["usmUsers"] = usm_users
        
        # There is no adaptor.
        return self.send_request(
            'SetSnmpInfo',
            SetSnmpInfoResult,
            params,
            since=1
        )

    def create_support_bundle(
            self,
            bundle_name=OPTIONAL,
            extra_args=OPTIONAL,
            timeout_sec=OPTIONAL,):
        """
        CreateSupportBundle is used to create a support bundle file under the node's directory. When the bundle has been successfully created, the bundle is stored on the node as a tar.gz file.
        :param bundleName:  Unique name for each support bundle created. If no name is provided, then 'supportbundle' and the node name is used as a file name. 
        :type bundleName: str

        :param extraArgs:  This parameter is fed to the sf_make_support_bundle script. Should be used only at the request of SolidFire Support. 
        :type extraArgs: str

        :param timeoutSec:  The number of seconds to let the support bundle script run before timing out and stopping. Default is 1500 seconds. 
        :type timeoutSec: int
        """

        self._check_connection_type("create_support_bundle", "Node")

        params = { 
        }
        if bundle_name is not None:
            params["bundleName"] = bundle_name
        if extra_args is not None:
            params["extraArgs"] = extra_args
        if timeout_sec is not None:
            params["timeoutSec"] = timeout_sec
        
        # There is no adaptor.
        return self.send_request(
            'CreateSupportBundle',
            CreateSupportBundleResult,
            params,
            since=8
        )

    def delete_all_support_bundles(
            self,):
        """
        DeleteAllSupportBundles is used to delete all support bundles generated with the CreateSupportBundle API method.        """

        self._check_connection_type("delete_all_support_bundles", "Node")

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'DeleteAllSupportBundles',
            DeleteAllSupportBundlesResult,
            params,
            since=8
        )

    def disable_encryption_at_rest(
            self,):
        """
        The DisableEncryptionAtRest method enables you to remove the encryption that was previously applied to the cluster using the EnableEncryptionAtRest method.
        This disable method is asynchronous and returns a response before encryption is disabled.
        You can use the GetClusterInfo method to poll the system to see when the process has completed.        """

        self._check_connection_type("disable_encryption_at_rest", "Cluster")

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'DisableEncryptionAtRest',
            DisableEncryptionAtRestResult,
            params,
            since=5
        )

    def disable_snmp(
            self,):
        """
        DisableSnmp is used to disable SNMP on the cluster nodes.        """

        self._check_connection_type("disable_snmp", "Cluster")

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'DisableSnmp',
            DisableSnmpResult,
            params,
            since=8
        )

    def enable_snmp(
            self,
            snmp_v3_enabled,):
        """
        EnableSnmp is used to enable SNMP on the cluster nodes. The values set with this interface apply to all nodes in the cluster, and the values that are passed replace, in whole, all values set in any previous call to EnableSnmp.
        :param snmpV3Enabled: [required] If set to "true", then SNMP v3 is enabled on each node in the cluster. If set to "false", then SNMP v2 is enabled. 
        :type snmpV3Enabled: bool
        """

        self._check_connection_type("enable_snmp", "Cluster")

        params = { 
            "snmpV3Enabled": snmp_v3_enabled,
        }
        
        # There is no adaptor.
        return self.send_request(
            'EnableSnmp',
            EnableSnmpResult,
            params,
            since=8
        )

    def get_api(
            self,):
        """
        Retrieves the current version of the API and a list of all supported versions.        """

        self._check_connection_type("get_api", "Both")

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'GetAPI',
            GetAPIResult,
            params,
            since=1.0
        )

    def get_cluster_capacity(
            self,):
        """
        Return the high-level capacity measurements for an entire cluster.
        The fields returned from this method can be used to calculate the efficiency rates that are displayed in the Element User Interface.        """

        self._check_connection_type("get_cluster_capacity", "Cluster")

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'GetClusterCapacity',
            GetClusterCapacityResult,
            params,
            since=1
        )

    def get_cluster_full_threshold(
            self,):
        """
        GetClusterFullThreshold is used to view the stages set for cluster fullness levels. All levels are returned when this method is entered.        """

        self._check_connection_type("get_cluster_full_threshold", "Cluster")

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'GetClusterFullThreshold',
            GetClusterFullThresholdResult,
            params,
            since=1
        )

    def get_cluster_info(
            self,):
        """
        Return configuration information about the cluster.        """

        self._check_connection_type("get_cluster_info", "Cluster")

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'GetClusterInfo',
            GetClusterInfoResult,
            params,
            since=1
        )

    def get_cluster_master_node_id(
            self,):
        """
        GetClusterMasterNodeID is used to return the ID of the node that can perform cluster-wide administration tasks and holds the storage virtual IP (SVIP) and management virtual IP (MVIP).        """

        self._check_connection_type("get_cluster_master_node_id", "Cluster")

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'GetClusterMasterNodeID',
            GetClusterMasterNodeIDResult,
            params,
            since=1
        )

    def get_cluster_state(
            self,
            force,):
        """
        The GetClusterState method is used to indicate if a node is part of a cluster or not. The three states are: <br><strong>Available:</strong> Node has not been configured with a cluster name.<br><strong>Pending:</strong> Node is pending for a specific named cluster and can be added.<br><strong>Active:</strong> Node is active and a member of a cluster and may not be added to another cluster.
        :param force: [required] To run this command, the force parameter must be set to true. 
        :type force: bool
        """

        self._check_connection_type("get_cluster_state", "Cluster")

        params = { 
            "force": force,
        }
        
        # There is no adaptor.
        return self.send_request(
            'GetClusterState',
            GetClusterStateResult,
            params,
            since=5
        )

    def get_cluster_stats(
            self,):
        """
        GetClusterStats is used to return high-level activity measurements for the cluster. Values returned are cumulative from the creation of the cluster.        """

        self._check_connection_type("get_cluster_stats", "Cluster")

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'GetClusterStats',
            GetClusterStatsResult,
            params,
            since=1
        )

    def get_cluster_version_info(
            self,):
        """
        Return information about the Element software version running on each node in the cluster.
        Information about the nodes that are currently in the process of upgrading software is also returned.        """

        self._check_connection_type("get_cluster_version_info", "Cluster")

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'GetClusterVersionInfo',
            GetClusterVersionInfoResult,
            params,
            since=1
        )

    def get_current_cluster_admin(
            self,):
        """
        GetCurrentClusterAdmin returns information for the current primary cluster administrator. The primary Cluster Admin was ncreated when the cluster was created.        """

        self._check_connection_type("get_current_cluster_admin", "Cluster")

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'GetCurrentClusterAdmin',
            GetCurrentClusterAdminResult,
            params,
            since=6
        )

    def get_limits(
            self,):
        """
        GetLimits enables you to retrieve the limit values set by the API. These values might change between releases of  Element, but do not change without an update to the system. Knowing the limit values set by the API can be useful when writing API scripts for user-facing tools.NOTE: The GetLimits method returns the limits for the current software version regardless of the API endpoint version used to pass the method.        """

        self._check_connection_type("get_limits", "Cluster")

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'GetLimits',
            GetLimitsResult,
            params,
            since=1
        )

    def get_ntp_info(
            self,):
        """
        GetNtpInfo is used to return the current network time protocol (NTP) configuration information.        """

        self._check_connection_type("get_ntp_info", "Cluster")

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'GetNtpInfo',
            GetNtpInfoResult,
            params,
            since=1
        )

    def get_snmp_acl(
            self,):
        """
        GetSnmpACL is used to return the current SNMP access permissions on the cluster nodes.        """

        self._check_connection_type("get_snmp_acl", "Cluster")

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'GetSnmpACL',
            GetSnmpACLResult,
            params,
            since=8
        )

    def get_snmp_trap_info(
            self,):
        """
        GetSnmpTrapInfo is used to return current SNMP trap configuration information.        """

        self._check_connection_type("get_snmp_trap_info", "Cluster")

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'GetSnmpTrapInfo',
            GetSnmpTrapInfoResult,
            params,
            since=5
        )

    def get_system_status(
            self,):
        """        """

        self._check_connection_type("get_system_status", "Node")

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'GetSystemStatus',
            GetSystemStatusResult,
            params,
            since=5
        )

    def list_cluster_admins(
            self,):
        """
        ListClusterAdmins returns the list of all cluster administrators for the cluster. There can be several cluster administrators that have different levels of permissions. There can be only one primary cluster administrator in the system. The primary Cluster Admin is the administrator that was created when the cluster was created. LDAP administrators can also be created when setting up an LDAP system on the cluster.        """

        self._check_connection_type("list_cluster_admins", "Cluster")

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'ListClusterAdmins',
            ListClusterAdminsResult,
            params,
            since=1
        )

    def list_events(
            self,
            max_events=OPTIONAL,
            start_event_id=OPTIONAL,
            end_event_id=OPTIONAL,
            event_queue_type=OPTIONAL,):
        """
        ListEvents returns events detected on the cluster, sorted from oldest to newest.
        :param maxEvents:  Specifies the maximum number of events to return. 
        :type maxEvents: int

        :param startEventID:  Identifies the beginning of a range of events to return. 
        :type startEventID: int

        :param endEventID:  Identifies the end of a range of events to return. 
        :type endEventID: int

        :param eventQueueType:  
        :type eventQueueType: str
        """

        self._check_connection_type("list_events", "Cluster")

        params = { 
        }
        if max_events is not None:
            params["maxEvents"] = max_events
        if start_event_id is not None:
            params["startEventID"] = start_event_id
        if end_event_id is not None:
            params["endEventID"] = end_event_id
        if event_queue_type is not None:
            if self.api_version < 9.0:
                raise ApiParameterVersionError("list_events", 9.0,
                    [("event_queue_type", event_queue_type, 9.0, False)])
            else:
                params["eventQueueType"] = event_queue_type
        
        # There is no adaptor.
        return self.send_request(
            'ListEvents',
            ListEventsResult,
            params,
            since=1
        )

    def list_sync_jobs(
            self,):
        """
        ListSyncJobs is used to return information about synchronization jobs that are running on a SolidFire cluster. Synchronization jobs that are returned with this method are, "slice," "clone" and "remote."        """

        self._check_connection_type("list_sync_jobs", "Cluster")

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'ListSyncJobs',
            ListSyncJobsResult,
            params,
            since=1
        )

    def modify_cluster_admin(
            self,
            cluster_admin_id,
            password=OPTIONAL,
            access=OPTIONAL,
            attributes=OPTIONAL,):
        """
        ModifyClusterAdmin is used to change the settings for a Cluster Admin or LDAP Cluster Admin. Access for the administrator Cluster Admin account cannot be changed.
        :param clusterAdminID: [required] ClusterAdminID for the Cluster Admin or LDAP Cluster Admin to modify. 
        :type clusterAdminID: int

        :param password:  Password used to authenticate this Cluster Admin. 
        :type password: str

        :param access:  Controls which methods this Cluster Admin can use. For more details on the levels of access, see "Access Control" in the Element API Guide. 
        :type access: str

        :param attributes:  List of Name/Value pairs in JSON object format. 
        :type attributes: dict
        """

        self._check_connection_type("modify_cluster_admin", "Cluster")

        params = { 
            "clusterAdminID": cluster_admin_id,
        }
        if password is not None:
            params["password"] = password
        if access is not None:
            params["access"] = access
        if attributes is not None:
            params["attributes"] = attributes
        
        # There is no adaptor.
        return self.send_request(
            'ModifyClusterAdmin',
            ModifyClusterAdminResult,
            params,
            since=1
        )

    def enable_encryption_at_rest(
            self,):
        """
        The EnableEncryptionAtRest method is used to enable the Advanced Encryption Standard (AES) 256-bit encryption at rest on the cluster so that the cluster can manage the encryption key used for the drives on each node. This feature is not enabled by default. Enabling this operation allows the cluster to automatically manage encryption keys internally for the drives on each node in the cluster. Nodes do not store the keys to unlock drives and the keys are never passed over the network. Two nodes participating in a cluster are required to access the key to disable encryption on a drive. The encryption management does not affect performance or efficiency on the cluster. If an encryption-enabled drive or node is removed from the cluster with the API, all data is secure erased and any data left on the drive cannot be read or accessed.
        Enabling or disabling encryption should be performed when the cluster is running and in a healthy state. Encryption can be enabled or disabled at your discretion and can be performed as often as you need.
        Note: This process is asynchronous and returns a response before encryption is enabled. The GetClusterInfo method can be used to poll the system to see when the process has completed.        """

        self._check_connection_type("enable_encryption_at_rest", "Cluster")

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'EnableEncryptionAtRest',
            EnableEncryptionAtRestResult,
            params,
            since=5
        )

    def get_snmp_info(
            self,):
        """
        GetSnmpInfo is used to return the current simple network management protocol (SNMP) configuration information.
        
        Note: GetSnmpInfo will be available for Element OS 8 and prior releases. It will be deprecated after Element OS 8. There are two new SNMP API methods that you should migrate over to. They are GetSnmpState and GetSnmpACL. Please see details in this document for their descriptions and usage.        """

        self._check_connection_type("get_snmp_info", "Cluster")

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'GetSnmpInfo',
            GetSnmpInfoResult,
            params,
            since=1
        )

    def list_cluster_faults(
            self,
            exceptions=OPTIONAL,
            best_practices=OPTIONAL,
            update=OPTIONAL,
            fault_types=OPTIONAL,):
        """
        ListClusterFaults is used to retrieve information about any faults detected on the cluster.
        With this method, both current and resolved faults can be retrieved. The system caches faults every 30 seconds.
        :param exceptions:  
        :type exceptions: bool

        :param bestPractices:  Include faults triggered by sub-optimal system configuration. Possible values: true, false 
        :type bestPractices: bool

        :param update:  
        :type update: bool

        :param faultTypes:  Determines the types of faults returned: current: List active, unresolved faults. resolved: List faults that were previously detected and resolved. all: (Default) List both current and resolved faults. You can see the fault status in the 'resolved' field of the Cluster Fault object. 
        :type faultTypes: str
        """

        self._check_connection_type("list_cluster_faults", "Cluster")

        params = { 
        }
        if exceptions is not None:
            params["exceptions"] = exceptions
        if best_practices is not None:
            params["bestPractices"] = best_practices
        if update is not None:
            params["update"] = update
        if fault_types is not None:
            params["faultTypes"] = fault_types
        
        # There is no adaptor.
        return self.send_request(
            'ListClusterFaults',
            ListClusterFaultsResult,
            params,
            since=1
        )

    def get_drive_hardware_info(
            self,
            drive_id,):
        """
        GetDriveHardwareInfo returns all the hardware info for the given drive. This generally includes manufacturers, vendors, versions, and other associated hardware identification information.
        :param driveID: [required] DriveID for the drive information requested. DriveIDs can be obtained via the "ListDrives" method. 
        :type driveID: int
        """

        self._check_connection_type("get_drive_hardware_info", "Cluster")

        params = { 
            "driveID": drive_id,
        }
        
        # There is no adaptor.
        return self.send_request(
            'GetDriveHardwareInfo',
            GetDriveHardwareInfoResult,
            params,
            since=1
        )

    def get_drive_stats(
            self,
            drive_id,):
        """
        GetDriveStats return high-level activity measurements for a single drive. Values are cumulative from the addition of the drive to the cluster. Some values are specific to Block Drives. Statistical data may not be returned for both block and metadata drives when running this method.
        For more information on which drive type returns which data, see Response Example (Block Drive) and Response Example (Volume Metadata Drive) in the SolidFire API guide.
        :param driveID: [required] Specifies the drive for which statistics are gathered. 
        :type driveID: int
        """

        self._check_connection_type("get_drive_stats", "Cluster")

        params = { 
            "driveID": drive_id,
        }
        
        # There is no adaptor.
        return self.send_request(
            'GetDriveStats',
            GetDriveStatsResult,
            params,
            since=1
        )

    def list_drive_hardware(
            self,
            force,):
        """
        ListDriveHardware returns all the drives connected to a node. Use this method on the cluster to return drive hardware information for all the drives on all nodes.
        :param force: [required] To run this command, the force parameter must be set to true. 
        :type force: bool
        """

        self._check_connection_type("list_drive_hardware", "Cluster")

        params = { 
            "force": force,
        }
        
        # There is no adaptor.
        return self.send_request(
            'ListDriveHardware',
            ListDriveHardwareResult,
            params,
            since=7
        )

    def list_drives(
            self,):
        """
        ListDrives allows you to retrieve the list of the drives that exist in the cluster's active nodes.
        This method returns drives that have been added as volume metadata or block drives as well as drives that have not been added and are available.        """

        self._check_connection_type("list_drives", "Cluster")

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'ListDrives',
            ListDrivesResult,
            params,
            since=1
        )

    def add_drives(
            self,
            drives,):
        """
        AddDrives is used to add one or more available drives to the cluster enabling the drives to host a portion of the cluster's data.
        When you add a node to the cluster or install new drives in an existing node, the new drives are marked as "available" and must be added via AddDrives before they can be utilized.
        Use the "ListDrives" method to display drives that are "available" to be added.
        When you add multiple drives, it is more efficient to add them in a single "AddDrives" method call rather than multiple individual methods with a single drive each.
        This reduces the amount of data balancing that must occur to stabilize the storage load on the cluster.
        
        When you add a drive, the system automatically determines the "type" of drive it should be.
        
        The method returns immediately. However, it may take some time for the data in the cluster to be rebalanced using the newly added drives.
        As the new drive(s) are syncing on the system, you can use the "ListSyncJobs" method to see how the drive(s) are being rebalanced and the progress of adding the new drive.
        :param drives: [required] List of drives to add to the cluster. 
        :type drives: NewDrive
        """

        self._check_connection_type("add_drives", "Cluster")

        params = { 
            "drives": drives,
        }
        
        # There is no adaptor.
        return self.send_request(
            'AddDrives',
            AddDrivesResult,
            params,
            since=1
        )

    def get_drive_config(
            self,):
        """
        GetDriveConfig is used to display drive information for expected slice and block drive counts as well as the number of slices and block drives that are currently connected to the node.
        
        Note: This method is available only through the per-node API endpoint 5.0 or later.        """

        self._check_connection_type("get_drive_config", "Node")

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'GetDriveConfig',
            GetDriveConfigResult,
            params,
            since=2
        )

    def remove_drives(
            self,
            drives,):
        """
        You can use RemoveDrives to proactively remove drives that are part of the cluster.
        You may want to use this method when reducing cluster capacity or preparing to replace drives nearing the end of their service life.
        Any data on the drives is removed and migrated to other drives in the cluster before the drive is removed from the cluster. This is an asynchronous method.
        Depending on the total capacity of the drives being removed, it may take several minutes to migrate all of the data.
        Use the "GetAsyncResult" method to check the status of the remove operation.
        
        When removing multiple drives, use a single "RemoveDrives" method call rather than multiple individual methods with a single drive each.
        This reduces the amount of data balancing that must occur to even stabilize the storage load on the cluster.
        
        You can also remove drives with a "failed" status using "RemoveDrives".
        When you remove a drive with a "failed" status it is not returned to an "available" or "active" status.
        The drive is unavailable for use in the cluster.
        
        Use the "ListDrives" method to obtain the driveIDs for the drives you want to remove.
        :param drives: [required] List of driveIDs to remove from the cluster. 
        :type drives: int
        """

        self._check_connection_type("remove_drives", "Cluster")

        params = { 
            "drives": drives,
        }
        
        # There is no adaptor.
        return self.send_request(
            'RemoveDrives',
            AsyncHandleResult,
            params,
            since=1
        )

    def reset_drives(
            self,
            drives,
            force,):
        """
        ResetDrives is used to pro-actively initialize drives and remove all data currently residing on the drive. The drive can then be reused in an existing node or used in an upgraded SolidFire node. This method requires the force=true parameter to be included in the method call.
        
        Note: This method is available only through the per-node API endpoint 5.0 or later.
        :param drives: [required] List of device names (not driveIDs) to reset. 
        :type drives: str

        :param force: [required] The "force" parameter must be included on this method to successfully reset a drive. 
        :type force: bool
        """

        self._check_connection_type("reset_drives", "Node")

        params = { 
            "drives": drives,
            "force": force,
        }
        
        # There is no adaptor.
        return self.send_request(
            'ResetDrives',
            ResetDrivesResult,
            params,
            since=6
        )

    def secure_erase_drives(
            self,
            drives,):
        """
        SecureEraseDrives is used to remove any residual data from drives that have a status of "available." For example, when replacing a drive at its end-of-life that contained sensitive data.
        It uses a Security Erase Unit command to write a predetermined pattern to the drive and resets the encryption key on the drive. The method may take up to two minutes to complete, so it is an asynchronous method.
        The GetAsyncResult method can be used to check on the status of the secure erase operation.
        
        Use the "ListDrives" method to obtain the driveIDs for the drives you want to secure erase.
        :param drives: [required] List of driveIDs to secure erase. 
        :type drives: int
        """

        self._check_connection_type("secure_erase_drives", "Cluster")

        params = { 
            "drives": drives,
        }
        
        # There is no adaptor.
        return self.send_request(
            'SecureEraseDrives',
            AsyncHandleResult,
            params,
            since=5
        )

    def test_drives(
            self,
            minutes=OPTIONAL,):
        """
        The TestDrives API method is used to run a hardware validation on all the drives on the node. Hardware failures on the drives are detected if present and they are reported in the results of the validation tests.
        
        Note: This test takes approximately 10 minutes.
        
        Note: This method is available only through the per-node API endpoint 5.0 or later.
        :param minutes:  The number of minutes to run the test can be specified. 
        :type minutes: int
        """

        self._check_connection_type("test_drives", "Node")

        params = { 
        }
        if minutes is not None:
            params["minutes"] = minutes
        
        # There is no adaptor.
        return self.send_request(
            'TestDrives',
            TestDrivesResult,
            params,
            since=5
        )

    def get_cluster_hardware_info(
            self,
            type=OPTIONAL,):
        """
        You can use the GetClusterHardwareInfo method to retrieve the hardware status and information for all Fibre Channel nodes, iSCSI nodes and drives in the cluster. This generally includes manufacturers, vendors, versions, and other associated hardware identification information.
        :param type:  Include only a certain type of hardware information in the response. Can be one of the following:drives: List only drive information in the response.nodes: List only node information in the response.all: Include both drive and node information in the response.If this parameter is omitted, a type of "all" is assumed. 
        :type type: str
        """

        self._check_connection_type("get_cluster_hardware_info", "Cluster")

        params = { 
        }
        if type is not None:
            params["type"] = type
        
        # There is no adaptor.
        return self.send_request(
            'GetClusterHardwareInfo',
            GetClusterHardwareInfoResult,
            params,
            since=1
        )

    def get_hardware_config(
            self,):
        """
        GetHardwareConfig enables you to display the hardware configuration information for a node. NOTE: This method is available only through the per-node API endpoint 5.0 or later.        """

        self._check_connection_type("get_hardware_config", "Node")

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'GetHardwareConfig',
            GetHardwareConfigResult,
            params,
            since=5
        )

    def get_node_hardware_info(
            self,
            node_id,):
        """
        GetNodeHardwareInfo is used to return all the hardware info and status for the node specified. This generally includes manufacturers, vendors, versions, and other associated hardware identification information.
        :param nodeID: [required] The ID of the node for which hardware information is being requested.  Information about a  node is returned if a   node is specified. 
        :type nodeID: int
        """

        self._check_connection_type("get_node_hardware_info", "Cluster")

        params = { 
            "nodeID": node_id,
        }
        
        # There is no adaptor.
        return self.send_request(
            'GetNodeHardwareInfo',
            GetNodeHardwareInfoResult,
            params,
            since=1
        )

    def get_nvram_info(
            self,):
        """
        GetNvramInfo allows you to retrieve information from each node about the NVRAM card.          """

        self._check_connection_type("get_nvram_info", "Node")

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'GetNvramInfo',
            GetNvramInfoResult,
            params,
            since=5
        )

    def create_initiators(
            self,
            initiators,):
        """
        CreateInitiators enables you to create multiple new initiator IQNs or World Wide Port Names (WWPNs) and optionally assign them aliases and attributes. When you use CreateInitiators to create new initiators, you can also add them to volume access groups.
        If CreateInitiators fails to create one of the initiators provided in the parameter, the method returns an error and does not create any initiators (no partial completion is possible).
        :param initiators: [required] A list of Initiator objects containing characteristics of each new initiator 
        :type initiators: CreateInitiator
        """

        self._check_connection_type("create_initiators", "Cluster")

        params = { 
            "initiators": initiators,
        }
        
        # There is no adaptor.
        return self.send_request(
            'CreateInitiators',
            CreateInitiatorsResult,
            params,
            since=9
        )

    def delete_initiators(
            self,
            initiators,):
        """
        DeleteInitiators enables you to delete one or more initiators from the system (and from any associated volumes or volume access groups).
        If DeleteInitiators fails to delete one of the initiators provided in the parameter, the system returns an error and does not delete any initiators (no partial completion is possible).
        :param initiators: [required] An array of IDs of initiators to delete. 
        :type initiators: int
        """

        self._check_connection_type("delete_initiators", "Cluster")

        params = { 
            "initiators": initiators,
        }
        
        # There is no adaptor.
        return self.send_request(
            'DeleteInitiators',
            DeleteInitiatorsResult,
            params,
            since=9
        )

    def list_initiators(
            self,
            start_initiator_id=OPTIONAL,
            limit=OPTIONAL,
            initiators=OPTIONAL,):
        """
        ListInitiators enables you to list initiator IQNs or World Wide Port Names (WWPNs).
        :param startInitiatorID:  The initiator ID at which to begin the listing. You can supply this parameter or the "initiators" parameter, but not both. 
        :type startInitiatorID: int

        :param limit:  The maximum number of initiator objects to return. 
        :type limit: int

        :param initiators:  A list of initiator IDs to retrieve. You can supply this parameter or the "startInitiatorID" parameter, but not both. 
        :type initiators: int
        """

        self._check_connection_type("list_initiators", "Cluster")

        params = { 
        }
        if start_initiator_id is not None:
            params["startInitiatorID"] = start_initiator_id
        if limit is not None:
            params["limit"] = limit
        if initiators is not None:
            params["initiators"] = initiators
        
        # There is no adaptor.
        return self.send_request(
            'ListInitiators',
            ListInitiatorsResult,
            params,
            since=9
        )

    def modify_initiators(
            self,
            initiators,):
        """
        ModifyInitiators enables you to change the attributes of an existing initiator. You cannot change the name of an existing initiator. If you need to change the name of an initiator, delete the existing initiator with DeleteInitiators and create a new one with CreateInitiators.
        If ModifyInitiators fails to change one of the initiators provided in the parameter, the method returns an error and does not create any initiators (no partial completion is possible).
        :param initiators: [required] A list of Initiator objects containing characteristics of each initiator to modify. 
        :type initiators: ModifyInitiator
        """

        self._check_connection_type("modify_initiators", "Cluster")

        params = { 
            "initiators": initiators,
        }
        
        # There is no adaptor.
        return self.send_request(
            'ModifyInitiators',
            ModifyInitiatorsResult,
            params,
            since=9
        )

    def disable_ldap_authentication(
            self,):
        """
        The DisableLdapAuthentication method is used disable LDAP authentication and remove all LDAP configuration settings. This call will not remove any configured cluster admin accounts (user or group). However, those cluster admin accounts will no longer be able to log in.        """

        self._check_connection_type("disable_ldap_authentication", "Cluster")

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'DisableLdapAuthentication',
            DisableLdapAuthenticationResult,
            params,
            since=7
        )

    def get_ldap_configuration(
            self,):
        """
        The GetLdapConfiguration is used to get the LDAP configuration currently active on the cluster.        """

        self._check_connection_type("get_ldap_configuration", "Cluster")

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'GetLdapConfiguration',
            GetLdapConfigurationResult,
            params,
            since=7
        )

    def test_ldap_authentication(
            self,
            username,
            password,
            ldap_configuration=OPTIONAL,):
        """
        The TestLdapAuthentication is used to verify the currently enabled LDAP authentication configuration settings are correct. If the configuration settings are correct, the API call returns a list of the groups the tested user is a member of.
        :param username: [required] The username to be tested. 
        :type username: str

        :param password: [required] The password for the username to be tester. 
        :type password: str

        :param ldapConfiguration:  An ldapConfiguration object to be tested. If this parameter is provided, the API call will test the provided configuration even if LDAP authentication is currently disabled. 
        :type ldapConfiguration: LdapConfiguration
        """

        self._check_connection_type("test_ldap_authentication", "Cluster")

        params = { 
            "username": username,
            "password": password,
        }
        if ldap_configuration is not None:
            params["ldapConfiguration"] = ldap_configuration
        
        # There is no adaptor.
        return self.send_request(
            'TestLdapAuthentication',
            TestLdapAuthenticationResult,
            params,
            since=7
        )

    def add_ldap_cluster_admin(
            self,
            username,
            access,
            accept_eula=OPTIONAL,
            attributes=OPTIONAL,):
        """
        AddLdapClusterAdmin is used to add a new LDAP Cluster Admin. An LDAP Cluster Admin can be used to manage the cluster via the API and management tools. LDAP Cluster Admins are completely separate and unrelated to standard tenant accounts.
        
        An LDAP group that has been defined in Active Directory can also be added using this API method. The access level that is given to the group will be passed to the individual users in the LDAP group.
        :param username: [required] The distinguished user name for the new LDAP cluster admin. 
        :type username: str

        :param access: [required] Controls which methods this Cluster Admin can use. For more details on the levels of access, see the Access Control appendix in the SolidFire API Reference. 
        :type access: str

        :param acceptEula:  Indicate your acceptance of the End User License Agreement when creating this cluster admin. To accept the EULA, set this parameter to true. 
        :type acceptEula: bool

        :param attributes:  List of Name/Value pairs in JSON object format. 
        :type attributes: dict
        """

        self._check_connection_type("add_ldap_cluster_admin", "Cluster")

        params = { 
            "username": username,
            "access": access,
        }
        if accept_eula is not None:
            params["acceptEula"] = accept_eula
        if attributes is not None:
            params["attributes"] = attributes
        
        # There is no adaptor.
        return self.send_request(
            'AddLdapClusterAdmin',
            AddLdapClusterAdminResult,
            params,
            since=8
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
        The EnableLdapAuthentication method is used to configure an LDAP server connection to use for LDAP authentication to a SolidFire cluster. Users that are members on the LDAP server can then log in to a SolidFire storage system using their LDAP authentication userid and password.
        :param authType:  Identifies which user authentcation method will be used.  Must be one of the following: DirectBind SearchAndBind (default) 
        :type authType: str

        :param groupSearchBaseDN:  The base DN of the tree to start the group search (will do a subtree search from here). 
        :type groupSearchBaseDN: str

        :param groupSearchCustomFilter:  REQUIRED for CustomFilter For use with the CustomFilter search type, an LDAP filter to use to return the DNs of a user's groups. The string can have placeholder text of %USERNAME% and %USERDN% to be replaced with their username and full userDN as needed. 
        :type groupSearchCustomFilter: str

        :param groupSearchType:  Controls the default group search filter used, can be one of the following: NoGroups: No group support. ActiveDirectory: (default) Nested membership of all of a user's AD groups. MemberDN: MemberDN style groups (single-level). 
        :type groupSearchType: str

        :param searchBindDN:  REQUIRED for SearchAndBind A fully qualified DN to log in with to perform an LDAP search for the user (needs read access to the LDAP directory). 
        :type searchBindDN: str

        :param searchBindPassword:  REQUIRED for SearchAndBind The password for the searchBindDN account used for searching. 
        :type searchBindPassword: str

        :param serverURIs: [required] A list of LDAP server URIs (examples: "ldap://1.2.3.4" and ldaps://1.2.3.4:123") 
        :type serverURIs: str

        :param userDNTemplate:  REQUIRED for DirectBind A string that is used to form a fully qualified user DN. The string should have the placeholder text "%USERNAME%" which will be replaced with the username of the authenticating user. 
        :type userDNTemplate: str

        :param userSearchBaseDN:  REQUIRED for SearchAndBind The base DN of the tree used to start the search (will do a subtree search from here). 
        :type userSearchBaseDN: str

        :param userSearchFilter:  REQUIRED for SearchAndBind. The LDAP filter to use. The string should have the placeholder text "%USERNAME%" which will be replaced with the username of the authenticating user. Example: (&(objectClass=person) (sAMAccountName=%USERNAME%)) will use the sAMAccountName field in Active Directory to match the nusername entered at cluster login. 
        :type userSearchFilter: str
        """

        self._check_connection_type("enable_ldap_authentication", "Cluster")

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
        
        # There is no adaptor.
        return self.send_request(
            'EnableLdapAuthentication',
            EnableLdapAuthenticationResult,
            params,
            since=7
        )

    def get_login_session_info(
            self,):
        """
        GetLoginSessionInfo is used to return the period of time a log in authentication is valid for both log in shells and the TUI.        """

        self._check_connection_type("get_login_session_info", "Cluster")

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'GetLoginSessionInfo',
            GetLoginSessionInfoResult,
            params,
            since=7
        )

    def get_remote_logging_hosts(
            self,):
        """
        GetRemoteLoggingHosts is used to retrieve the current list of log servers.        """

        self._check_connection_type("get_remote_logging_hosts", "Cluster")

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'GetRemoteLoggingHosts',
            GetRemoteLoggingHostsResult,
            params,
            since=1
        )

    def set_login_session_info(
            self,
            timeout,):
        """
        SetLoginSessionInfo is used to set the period of time a log in authentication is valid. After the log in period elapses without activity on the system the authentication will expire. New log in credentials will be required for continued access to the cluster once the timeout period has elapsed.
        :param timeout: [required] Cluster authentication expiration period. Formatted in HH:mm:ss. For example: 01:30:00, 00:90:00, and 00:00:5400 can all be used to equal a 90 minute timeout period. Default is 30 minutes. 
        :type timeout: str
        """

        self._check_connection_type("set_login_session_info", "Cluster")

        params = { 
            "timeout": timeout,
        }
        
        # There is no adaptor.
        return self.send_request(
            'SetLoginSessionInfo',
            SetLoginSessionInfoResult,
            params,
            since=7
        )

    def set_remote_logging_hosts(
            self,
            remote_hosts,):
        """
        RemoteLoggingHosts is used to configure remote logging from the nodes in the storage cluster to a centralized log server or servers. Remote logging is performed over TCP using the default port 514. This API does not add to the existing logging hosts. Rather, it replaces what currently exists with new values specified by this API method. You can use the GetRemoteLoggingHosts to determine what the current logging hosts are and then use the SetRemoteLoggingHosts to set the desired list of current and new logging hosts.
        :param remoteHosts: [required] List of hosts to send log messages to. 
        :type remoteHosts: LoggingServer
        """

        self._check_connection_type("set_remote_logging_hosts", "Cluster")

        params = { 
            "remoteHosts": remote_hosts,
        }
        
        # There is no adaptor.
        return self.send_request(
            'SetRemoteLoggingHosts',
            SetRemoteLoggingHostsResult,
            params,
            since=1
        )

    def list_fibre_channel_port_info(
            self,):
        """
        The ListFibreChannelPortInfo is used to return information about the Fibre Channel ports. The API method is intended for use on individual nodes; userid and password is required for access to individual Fibre Channel nodes.        """

        self._check_connection_type("list_fibre_channel_port_info", "Cluster")

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'ListFibreChannelPortInfo',
            ListFibreChannelPortInfoResult,
            params,
            since=8
        )

    def list_fibre_channel_sessions(
            self,):
        """
        The ListFibreChannelSessions is used to return information about the active Fibre Channel sessions on a cluster.        """

        self._check_connection_type("list_fibre_channel_sessions", "Cluster")

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'ListFibreChannelSessions',
            ListFibreChannelSessionsResult,
            params,
            since=7
        )

    def list_iscsisessions(
            self,):
        """
        ListISCSISessions is used to return iSCSI connection information for volumes in the cluster.        """

        self._check_connection_type("list_iscsisessions", "Cluster")

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'ListISCSISessions',
            ListISCSISessionsResult,
            params,
            since=1
        )

    def list_network_interfaces(
            self,):
        """
        The ListNetworkInterfaces API method is used to return information about each network interface on a node. The API method is intended for use on individual nodes.         """

        self._check_connection_type("list_network_interfaces", "Node")

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'ListNetworkInterfaces',
            ListNetworkInterfacesResult,
            params,
            since=7
        )

    def list_node_fibre_channel_port_info(
            self,):
        """
        The ListNodeFibreChannelPortInfo is used to return information about the Fibre Channel ports. The API method is intended for use on individual nodes; userid and password is required for access to individual Fibre Channel nodes.        """

        self._check_connection_type("list_node_fibre_channel_port_info", "Node")

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'ListNodeFibreChannelPortInfo',
            ListNodeFibreChannelPortInfoResult,
            params,
            since=7
        )

    def get_node_stats(
            self,
            node_id,):
        """
        GetNodeStats is used to return the high-level activity measurements for a single node.
        :param nodeID: [required] Specifies the node for which statistics are gathered. 
        :type nodeID: int
        """

        self._check_connection_type("get_node_stats", "Cluster")

        params = { 
            "nodeID": node_id,
        }
        
        # There is an adaptor!
        since = 1
        deprecated = None

        return ElementServiceAdaptor.get_node_stats(self, params,
                                                  since, deprecated)

    def get_origin(
            self,
            force,):
        """
        GetOrigin enables you to retrieve the origination certificate for where the node was built.NOTE: The GetOrigin method may return "null" if there is no origination certification.
        :param force: [required] 
        :type force: bool
        """

        self._check_connection_type("get_origin", "Cluster")

        params = { 
            "force": force,
        }
        
        # There is no adaptor.
        return self.send_request(
            'GetOrigin',
            GetOriginResult,
            params,
            since=9
        )

    def list_active_nodes(
            self,):
        """
        ListActiveNodes returns the list of currently active nodes that are in the cluster.        """

        self._check_connection_type("list_active_nodes", "Cluster")

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'ListActiveNodes',
            ListActiveNodesResult,
            params,
            since=1
        )

    def list_all_nodes(
            self,):
        """
        ListAllNodes enables you to retrieve a list of active and pending nodes in the cluster.        """

        self._check_connection_type("list_all_nodes", "Cluster")

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'ListAllNodes',
            ListAllNodesResult,
            params,
            since=1
        )

    def list_node_stats(
            self,):
        """
        ListNodeStats is used to return the high-level activity measurements for all nodes in a cluster.        """

        self._check_connection_type("list_node_stats", "Cluster")

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'ListNodeStats',
            ListNodeStatsResult,
            params,
            since=6
        )

    def list_pending_active_nodes(
            self,):
        """
        ListPendingActiveNodes returns the list of nodes in the cluster that are currently in the PendingActive state, between the pending and active states. These are nodes that are currently being returned to the factory image.        """

        self._check_connection_type("list_pending_active_nodes", "Cluster")

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'ListPendingActiveNodes',
            ListPendingActiveNodesResult,
            params,
            since=9
        )

    def list_pending_nodes(
            self,):
        """
        Gets the list of pending nodes.
        Pending nodes are running and configured to join the cluster, but have not been added via the AddNodes method.        """

        self._check_connection_type("list_pending_nodes", "Cluster")

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'ListPendingNodes',
            ListPendingNodesResult,
            params,
            since=1
        )

    def get_bootstrap_config(
            self,):
        """
        GetBootstrapConfig returns the cluster name and node name from the bootstrap configuration file. This API method should be performed on an individual node before it has been configured into a cluster. The resulting information from this method is used in the Cluster Configuration UI when the cluster is eventually created.        """

        self._check_connection_type("get_bootstrap_config", "Both")

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'GetBootstrapConfig',
            GetBootstrapConfigResult,
            params,
            since=2
        )

    def add_nodes(
            self,
            pending_nodes,):
        """
        AddNodes is used to add one or more new nodes to the cluster. When a node is not configured and starts up for the first time you are prompted to configure the node. Once a node is configured it is registered as a "pending node" with the cluster.
        
        Adding a node to a cluster that has been set up for virtual networking will require a sufficient number of virtual storage IP addresses to allocate a virtual IP to the new node. If there are no virtual IP addresses available for the new node, the AddNode operation will not complete successfully. Use the "ModifyVirtualNetwork" method to add more storage IP addresses to your virtual network.
        
        The software version on each node in a cluster must be compatible. Run the "ListAllNodes" API to see what versions of software are currently running on the cluster nodes. For an explanation of software version compatibility, see "Node Versioning and Compatibility" in the Element API guide.
        
        Once a node has been added, the drives on the node are made available and can then be added via the "AddDrives" method to increase the storage capacity of the cluster.
        
        Note: It may take several seconds after adding a new Node for it to start up and register the drives as being available.
        :param pendingNodes: [required] List of PendingNodeIDs for the Nodes to be added. You can obtain the list of Pending Nodes via the ListPendingNodes method. 
        :type pendingNodes: int
        """

        self._check_connection_type("add_nodes", "Cluster")

        params = { 
            "pendingNodes": pending_nodes,
        }
        
        # There is no adaptor.
        return self.send_request(
            'AddNodes',
            AddNodesResult,
            params,
            since=1
        )

    def get_config(
            self,):
        """
        The GetConfig API method is used to retrieve all the configuration information for the node. This one API method includes the same information available in both "GetClusterConfig" and "GetNetworkConfig" methods.
        
        Note: This method is available only through the per-node API endpoint 5.0 or later.        """

        self._check_connection_type("get_config", "Node")

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'GetConfig',
            GetConfigResult,
            params,
            since=5
        )

    def get_network_config(
            self,):
        """
        The GetNetworkConfig API method is used to display the network configuration information for a node.
        
        Note: This method is available only through the per-node API endpoint 5.0 or later.        """

        self._check_connection_type("get_network_config", "Node")

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'GetNetworkConfig',
            GetNetworkConfigResult,
            params,
            since=5
        )

    def get_pending_operation(
            self,):
        """
        GetPendingOperation is used to detect an operation on a node that is currently in progress. This method can also be used to report back when an operation has completed.
        
        Note: This method is available only through the per-node API endpoint 5.0 or later.        """

        self._check_connection_type("get_pending_operation", "Node")

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'GetPendingOperation',
            GetPendingOperationResult,
            params,
            since=5
        )

    def remove_nodes(
            self,
            nodes,):
        """
        RemoveNodes is used to remove one or more nodes that should no longer participate in the cluster. Before removing a node, all drives it contains must first be removed with "RemoveDrives" method. A node cannot be removed until the RemoveDrives process has completed and all data has been migrated away from the node.
        
        Once removed, a node registers itself as a pending node and can be added again, or shut down which removes it from the "Pending Node" list.
        :param nodes: [required] List of NodeIDs for the nodes to be removed. 
        :type nodes: int
        """

        self._check_connection_type("remove_nodes", "Cluster")

        params = { 
            "nodes": nodes,
        }
        
        # There is no adaptor.
        return self.send_request(
            'RemoveNodes',
            RemoveNodesResult,
            params,
            since=1
        )

    def set_config(
            self,
            config,):
        """
        The SetConfig API method is used to set all the configuration information for the node. This includes the same information available via calls to SetClusterConfig and SetNetworkConfig in one API method.
        
        Warning! Changing the 'bond-mode' on a node can cause a temporary loss of network connectivity. Caution should be taken when using this method.
        
        Note: This method is available only through the per-node API endpoint 5.0 or later.
        :param config: [required] Objects that you want changed for the cluster interface settings. 
        :type config: Config
        """

        self._check_connection_type("set_config", "Node")

        params = { 
            "config": config,
        }
        
        # There is no adaptor.
        return self.send_request(
            'SetConfig',
            SetConfigResult,
            params,
            since=5
        )

    def set_network_config(
            self,
            network,):
        """
        The "SetNetworkConfig" method is used to set the network configuration for a node. To see the states in which these objects can be modified, see "Network Object for 1G and 10G Interfaces" on page 109 of the Element API. To display the current network settings for a node, run the "GetNetworkConfig" method.
        
        WARNING! Changing the "bond-mode" on a node can cause a temporary loss of network connectivity. Caution should be taken when using this method.
        
        Note: This method is available only through the per-node API endpoint 5.0 or later.
        :param network: [required] Objects that will be changed for the node network settings. 
        :type network: Network
        """

        self._check_connection_type("set_network_config", "Node")

        params = { 
            "network": network,
        }
        
        # There is no adaptor.
        return self.send_request(
            'SetNetworkConfig',
            SetNetworkConfigResult,
            params,
            since=5
        )

    def complete_cluster_pairing(
            self,
            cluster_pairing_key,):
        """
        The CompleteClusterPairing method is the second step in the cluster pairing process.
        Use this method with the encoded key received from the "StartClusterPairing" API method to complete the cluster pairing process.
        :param clusterPairingKey: [required] A string of characters that is returned from the "StartClusterPairing" API method. 
        :type clusterPairingKey: str
        """

        self._check_connection_type("complete_cluster_pairing", "Cluster")

        params = { 
            "clusterPairingKey": cluster_pairing_key,
        }
        
        # There is no adaptor.
        return self.send_request(
            'CompleteClusterPairing',
            CompleteClusterPairingResult,
            params,
            since=6
        )

    def complete_volume_pairing(
            self,
            volume_pairing_key,
            volume_id,):
        """
        CompleteVolumePairing is used to complete the pairing of two volumes.
        :param volumePairingKey: [required] The key returned from the "StartVolumePairing" API method. 
        :type volumePairingKey: str

        :param volumeID: [required] The ID of volume on which to complete the pairing process. 
        :type volumeID: int
        """

        self._check_connection_type("complete_volume_pairing", "Cluster")

        params = { 
            "volumePairingKey": volume_pairing_key,
            "volumeID": volume_id,
        }
        
        # There is no adaptor.
        return self.send_request(
            'CompleteVolumePairing',
            CompleteVolumePairingResult,
            params,
            since=6
        )

    def list_active_paired_volumes(
            self,):
        """
        ListActivePairedVolumes is used to list all of the active volumes paired with a volume.
        Volumes listed in the return for this method include volumes with active and pending pairings.        """

        self._check_connection_type("list_active_paired_volumes", "Cluster")

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'ListActivePairedVolumes',
            ListActivePairedVolumesResult,
            params,
            since=6
        )

    def list_cluster_pairs(
            self,):
        """
        ListClusterPairs is used to list all of the clusters a cluster is paired with.
        This method returns information about active and pending cluster pairings, such as statistics about the current pairing as well as the connectivity and latency (in milliseconds) of the cluster pairing.        """

        self._check_connection_type("list_cluster_pairs", "Cluster")

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'ListClusterPairs',
            ListClusterPairsResult,
            params,
            since=6
        )

    def remove_volume_pair(
            self,
            volume_id,):
        """
        RemoveVolumePair is used to remove the remote pairing between two volumes.
        When the volume pairing information is removed, data is no longer replicated to or from the volume.
        This method should be run on both the source and target volumes that are paired together.
        :param volumeID: [required] ID of the volume on which to stop the replication process. 
        :type volumeID: int
        """

        self._check_connection_type("remove_volume_pair", "Cluster")

        params = { 
            "volumeID": volume_id,
        }
        
        # There is no adaptor.
        return self.send_request(
            'RemoveVolumePair',
            RemoveVolumePairResult,
            params,
            since=6
        )

    def start_cluster_pairing(
            self,):
        """
        StartClusterPairing is used to create an encoded key from a cluster that is used to pair with another cluster.
        The key created from this API method is used in the "CompleteClusterPairing" API method to establish a cluster pairing.
        You can pair a cluster with a maximum of four other SolidFire clusters.        """

        self._check_connection_type("start_cluster_pairing", "Cluster")

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'StartClusterPairing',
            StartClusterPairingResult,
            params,
            since=6
        )

    def modify_volume_pair(
            self,
            volume_id,
            paused_manual=OPTIONAL,
            mode=OPTIONAL,):
        """
        ModifyVolumePair is used to pause or restart replication between a pair of volumes.
        :param volumeID: [required] Identification number of the volume to be modified. 
        :type volumeID: int

        :param pausedManual:  Valid values that can be entered: true: to pause volume replication. false: to restart volume replication. If no value is specified, no change in replication is performed. 
        :type pausedManual: bool

        :param mode:  Volume replication mode. Possible values: Async: Writes are acknowledged when they complete locally. The cluster does not wait for writes to be replicated to the target cluster. Sync: The source acknowledges the write when the data is stored locally and on the remote cluster. SnapshotsOnly: Only snapshots created on the source cluster will be replicated. Active writes from the source volume are not replicated. 
        :type mode: str
        """

        self._check_connection_type("modify_volume_pair", "Cluster")

        params = { 
            "volumeID": volume_id,
        }
        if paused_manual is not None:
            params["pausedManual"] = paused_manual
        if mode is not None:
            params["mode"] = mode
        
        # There is no adaptor.
        return self.send_request(
            'ModifyVolumePair',
            ModifyVolumePairResult,
            params,
            since=6
        )

    def remove_cluster_pair(
            self,
            cluster_pair_id,):
        """
        You can use the RemoveClusterPair method to close the open connections between two paired clusters.
        Note: Before you remove a cluster pair, you must first remove all volume pairing to the clusters with the "RemoveVolumePair" API method.
        :param clusterPairID: [required] Unique identifier used to pair two clusters. 
        :type clusterPairID: int
        """

        self._check_connection_type("remove_cluster_pair", "Cluster")

        params = { 
            "clusterPairID": cluster_pair_id,
        }
        
        # There is no adaptor.
        return self.send_request(
            'RemoveClusterPair',
            RemoveClusterPairResult,
            params,
            since=6
        )

    def start_volume_pairing(
            self,
            volume_id,
            mode=OPTIONAL,):
        """
        StartVolumePairing is used to create an encoded key from a volume that is used to pair with another volume.
        The key that this method creates is used in the "CompleteVolumePairing" API method to establish a volume pairing.
        :param volumeID: [required] The ID of the volume on which to start the pairing process. 
        :type volumeID: int

        :param mode:  The mode of the volume on which to start the pairing process. The mode can only be set if the volume is the source volume. Possible values: Async: (default if no mode parameter specified) Writes are acknowledged when they complete locally. The cluster does not wait for writes to be replicated to the target cluster. Sync: Source acknowledges write when the data is stored locally and on the remote cluster. SnapshotsOnly: Only snapshots created on the source cluster will be replicated. Active writes from the source volume will not be replicated. 
        :type mode: str
        """

        self._check_connection_type("start_volume_pairing", "Cluster")

        params = { 
            "volumeID": volume_id,
        }
        if mode is not None:
            if self.api_version < 8.0:
                raise ApiParameterVersionError("start_volume_pairing", 8.0,
                    [("mode", mode, 8.0, False)])
            else:
                params["mode"] = mode
        
        # There is no adaptor.
        return self.send_request(
            'StartVolumePairing',
            StartVolumePairingResult,
            params,
            since=6
        )

    def list_protocol_endpoints(
            self,
            protocol_endpoint_ids=OPTIONAL,):
        """
        Gets protocol endpoints in the system
        If protocolEndpointIDs isn't specified all protocol endpoints
        are returned. Else the supplied protocolEndpointIDs are.
        :param protocolEndpointIDs:  
        :type protocolEndpointIDs: UUID
        """

        self._check_connection_type("list_protocol_endpoints", "Cluster")

        params = { 
        }
        if protocol_endpoint_ids is not None:
            params["protocolEndpointIDs"] = protocol_endpoint_ids
        
        # There is no adaptor.
        return self.send_request(
            'ListProtocolEndpoints',
            ListProtocolEndpointsResult,
            params,
            since=9
        )

    def reset_node(
            self,
            build,
            force,
            option,):
        """
        Allows you to reset a node to the SolidFire factory settings. All data will be deleted from the node when you call this method. A node participating in a cluster cannot be reset.
        :param build: [required] Used to specify the URL to a remote Element software image to which the node will be reset. 
        :type build: str

        :param force: [required] The force parameter must be included in order to successfully reset the node. 
        :type force: bool

        :param option: [required] Used to enter specifications for running the reset operation. 
        :type option: str
        """

        self._check_connection_type("reset_node", "Cluster")

        params = { 
            "build": build,
            "force": force,
            "option": option,
        }
        
        # There is no adaptor.
        return self.send_request(
            'ResetNode',
            ResetNodeResult,
            params,
            since=5
        )

    def restart_networking(
            self,
            force,):
        """
        The RestartNetworking API method is used to restart the networking services on a node.WARNING! This method restarts all networking services on a node, causing temporary loss of networking connectivity. Exercise caution when using this method.
        :param force: [required] The "force" parameter must be included on this method to successfully restart the networking. 
        :type force: bool
        """

        self._check_connection_type("restart_networking", "Node")

        params = { 
            "force": force,
        }
        
        # There is no adaptor.
        return self.send_request(
            'RestartNetworking',
            dict,
            params,
            since=5
        )

    def restart_services(
            self,
            force,
            service=OPTIONAL,
            action=OPTIONAL,):
        """
        The RestartServices API method is used to restart the  Element services on a node.Caution: This method causes temporary node services interruption. Exercise caution when using this method.
        :param force: [required] The "force" parameter must be included on this method to successfully restart services on a node.    
        :type force: bool

        :param service:  Service name to be restarted. 
        :type service: str

        :param action:  Action to perform on the service (start, stop, restart). 
        :type action: str
        """

        self._check_connection_type("restart_services", "Node")

        params = { 
            "force": force,
        }
        if service is not None:
            params["service"] = service
        if action is not None:
            params["action"] = action
        
        # There is no adaptor.
        return self.send_request(
            'RestartServices',
            dict,
            params,
            since=5
        )

    def shutdown(
            self,
            nodes,
            option=OPTIONAL,):
        """
        The Shutdown API method enables you to restart or shutdown a node that has not yet been added to a cluster. To use this method, login in to the MIP for the pending node and enter the "shutdown" method with either the "restart" or "halt" options in the following table.
        :param nodes: [required] List of NodeIDs for the nodes to be shutdown. 
        :type nodes: int

        :param option:  Action to take for the node shutdown:restart: Restarts the node.halt: Performs full power-off of the node. 
        :type option: str
        """

        self._check_connection_type("shutdown", "Cluster")

        params = { 
            "nodes": nodes,
        }
        if option is not None:
            params["option"] = option
        
        # There is no adaptor.
        return self.send_request(
            'Shutdown',
            ShutdownResult,
            params,
            since=1
        )

    def list_services(
            self,):
        """
        List the services in the cluster.        """

        self._check_connection_type("list_services", "Cluster")

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'ListServices',
            ListServicesResult,
            params,
            since=1
        )

    def delete_snapshot(
            self,
            snapshot_id,):
        """
        DeleteSnapshot is used to delete a snapshot.
        A snapshot that is currently the "active" snapshot cannot be deleted.
        You must rollback and make another snapshot "active" before the current snapshot can be deleted.
        To rollback a snapshot, use RollbackToSnapshot.
        :param snapshotID: [required] The ID of the snapshot to delete. 
        :type snapshotID: int
        """

        self._check_connection_type("delete_snapshot", "Cluster")

        params = { 
            "snapshotID": snapshot_id,
        }
        
        # There is no adaptor.
        return self.send_request(
            'DeleteSnapshot',
            DeleteSnapshotResult,
            params,
            since=6
        )

    def get_schedule(
            self,
            schedule_id,):
        """
        GetSchedule is used to return information about a scheduled snapshot that has been created. You can see information about a specified schedule if there are many snapshot schedules in the system. You can include more than one schedule with this method by specifying additional scheduleIDs to the parameter.
        :param scheduleID: [required] Unique ID of the schedule or multiple schedules to display 
        :type scheduleID: int
        """

        self._check_connection_type("get_schedule", "Cluster")

        params = { 
            "scheduleID": schedule_id,
        }
        
        # There is an adaptor!
        since = 8
        deprecated = None

        return ElementServiceAdaptor.get_schedule(self, params,
                                                  since, deprecated)

    def list_group_snapshots(
            self,
            volume_id=OPTIONAL,):
        """
        ListGroupSnapshots is used to return information about all group snapshots that have been created.
        :param volumeID:  An array of unique volume IDs to query. If this parameter is not specified, all group snapshots on the cluster will be included. 
        :type volumeID: int
        """

        self._check_connection_type("list_group_snapshots", "Cluster")

        params = { 
        }
        if volume_id is not None:
            params["volumeID"] = volume_id
        
        # There is no adaptor.
        return self.send_request(
            'ListGroupSnapshots',
            ListGroupSnapshotsResult,
            params,
            since=7
        )

    def list_schedules(
            self,):
        """
        ListSchedule is used to return information about all scheduled snapshots that have been created.        """

        self._check_connection_type("list_schedules", "Cluster")

        params = { 
        }
        
        # There is an adaptor!
        since = 8
        deprecated = None

        return ElementServiceAdaptor.list_schedules(self, params,
                                                  since, deprecated)

    def list_snapshots(
            self,
            volume_id=OPTIONAL,):
        """
        ListSnapshots is used to return the attributes of each snapshot taken on the volume.
        :param volumeID:  The volume to list snapshots for. If not provided, all snapshots for all volumes are returned. 
        :type volumeID: int
        """

        self._check_connection_type("list_snapshots", "Cluster")

        params = { 
        }
        if volume_id is not None:
            params["volumeID"] = volume_id
        
        # There is no adaptor.
        return self.send_request(
            'ListSnapshots',
            ListSnapshotsResult,
            params,
            since=6
        )

    def create_group_snapshot(
            self,
            volumes,
            name=OPTIONAL,
            enable_remote_replication=OPTIONAL,
            retention=OPTIONAL,
            attributes=OPTIONAL,):
        """
        CreateGroupSnapshot is used to create a point-in-time copy of a group of volumes.
        The snapshot created can then be used later as a backup or rollback to ensure the data on the group of volumes is consistent for the point in time in which the snapshot was created.
        
        Note: Creating a group snapshot is allowed if cluster fullness is at stage 2 or 3.
        Snapshots are not created when cluster fullness is at stage 4 or 5.
        :param volumes: [required] Unique ID of the volume image from which to copy. 
        :type volumes: int

        :param name:  A name for the snapshot. If no name is provided, the date and time the snapshot was taken is used. 
        :type name: str

        :param enableRemoteReplication:  Identifies if snapshot is enabled for remote replication. 
        :type enableRemoteReplication: bool

        :param retention:  The amount of time the snapshot will be retained. Enter in HH:mm:ss 
        :type retention: str

        :param attributes:  List of Name/Value pairs in JSON object format. 
        :type attributes: dict
        """

        self._check_connection_type("create_group_snapshot", "Cluster")

        params = { 
            "volumes": volumes,
        }
        if name is not None:
            params["name"] = name
        if enable_remote_replication is not None:
            if self.api_version < 8.0:
                raise ApiParameterVersionError("create_group_snapshot", 8.0,
                    [("enable_remote_replication", enable_remote_replication, 8.0, False)])
            else:
                params["enableRemoteReplication"] = enable_remote_replication
        if retention is not None:
            if self.api_version < 8.0:
                raise ApiParameterVersionError("create_group_snapshot", 8.0,
                    [("retention", retention, 8.0, False)])
            else:
                params["retention"] = retention
        if attributes is not None:
            params["attributes"] = attributes
        
        # There is no adaptor.
        return self.send_request(
            'CreateGroupSnapshot',
            CreateGroupSnapshotResult,
            params,
            since=7
        )

    def create_schedule(
            self,
            schedule,):
        """
        CreateSchedule is used to create a schedule that will autonomously make a snapshot of a volume at a defined interval.
        
        The snapshot created can be used later as a backup or rollback to ensure the data on a volume or group of volumes is consistent for the point in time in which the snapshot was created. 
        
        Note: Creating a snapshot is allowed if cluster fullness is at stage 2 or 3. Snapshots are not created when cluster fullness is at stage 4 or 5.
        :param schedule: [required] The "Schedule" object will be used to create a new schedule. Do not set ScheduleID property, it will be ignored. Frequency property must be of type that inherits from Frequency. Valid types are: DaysOfMonthFrequency DaysOrWeekFrequency TimeIntervalFrequency 
        :type schedule: Schedule
        """

        self._check_connection_type("create_schedule", "Cluster")

        params = { 
            "schedule": schedule,
        }
        
        # There is an adaptor!
        since = 8
        deprecated = None

        return ElementServiceAdaptor.create_schedule(self, params,
                                                  since, deprecated)

    def create_snapshot(
            self,
            volume_id,
            snapshot_id=OPTIONAL,
            name=OPTIONAL,
            enable_remote_replication=OPTIONAL,
            retention=OPTIONAL,
            attributes=OPTIONAL,):
        """
        CreateSnapshot is used to create a point-in-time copy of a volume.
        A snapshot can be created from any volume or from an existing snapshot.
        
        Note: Creating a snapshot is allowed if cluster fullness is at stage 2 or 3.
        Snapshots are not created when cluster fullness is at stage 4 or 5.
        :param volumeID: [required] ID of the volume image from which to copy. 
        :type volumeID: int

        :param snapshotID:  Unique ID of a snapshot from which the new snapshot is made. The snapshotID passed must be a snapshot on the given volume. If a SnapshotID is not provided, a snapshot is created from the volume's active branch. 
        :type snapshotID: int

        :param name:  A name for the snapshot. If no name is provided, the date and time the snapshot was taken is used. 
        :type name: str

        :param enableRemoteReplication:  Identifies if snapshot is enabled for remote replication. 
        :type enableRemoteReplication: bool

        :param retention:  The amount of time the snapshot will be retained. Enter in HH:mm:ss 
        :type retention: str

        :param attributes:  List of Name/Value pairs in JSON object format. 
        :type attributes: dict
        """

        self._check_connection_type("create_snapshot", "Cluster")

        params = { 
            "volumeID": volume_id,
        }
        if snapshot_id is not None:
            params["snapshotID"] = snapshot_id
        if name is not None:
            params["name"] = name
        if enable_remote_replication is not None:
            if self.api_version < 8.0:
                raise ApiParameterVersionError("create_snapshot", 8.0,
                    [("enable_remote_replication", enable_remote_replication, 8.0, False)])
            else:
                params["enableRemoteReplication"] = enable_remote_replication
        if retention is not None:
            if self.api_version < 8.0:
                raise ApiParameterVersionError("create_snapshot", 8.0,
                    [("retention", retention, 8.0, False)])
            else:
                params["retention"] = retention
        if attributes is not None:
            params["attributes"] = attributes
        
        # There is no adaptor.
        return self.send_request(
            'CreateSnapshot',
            CreateSnapshotResult,
            params,
            since=6
        )

    def delete_group_snapshot(
            self,
            group_snapshot_id,
            save_members,):
        """
        DeleteGroupSnapshot is used to delete a group snapshot.
        The saveMembers parameter can be used to preserve all the snapshots that
        were made for the volumes in the group but the group association will be removed.
        :param groupSnapshotID: [required] Unique ID of the group snapshot. 
        :type groupSnapshotID: int

        :param saveMembers: [required] true: Snapshots are kept, but group association is removed. false: The group and snapshots are deleted. 
        :type saveMembers: bool
        """

        self._check_connection_type("delete_group_snapshot", "Cluster")

        params = { 
            "groupSnapshotID": group_snapshot_id,
            "saveMembers": save_members,
        }
        
        # There is no adaptor.
        return self.send_request(
            'DeleteGroupSnapshot',
            DeleteGroupSnapshotResult,
            params,
            since=7
        )

    def modify_group_snapshot(
            self,
            group_snapshot_id,
            expiration_time=OPTIONAL,
            enable_remote_replication=OPTIONAL,):
        """
        ModifyGroupSnapshot is used to change the attributes currently assigned to a group snapshot.
        :param groupSnapshotID: [required] ID of the snapshot. 
        :type groupSnapshotID: int

        :param expirationTime:  Use to set the time when the snapshot should be removed. 
        :type expirationTime: str

        :param enableRemoteReplication:  Use to enable the snapshot created to be replicated to a remote SolidFire cluster. Possible values: true: the snapshot will be replicated to remote storage. false: Default. No replication. 
        :type enableRemoteReplication: bool
        """

        self._check_connection_type("modify_group_snapshot", "Cluster")

        params = { 
            "groupSnapshotID": group_snapshot_id,
        }
        if expiration_time is not None:
            params["expirationTime"] = expiration_time
        if enable_remote_replication is not None:
            params["enableRemoteReplication"] = enable_remote_replication
        
        # There is no adaptor.
        return self.send_request(
            'ModifyGroupSnapshot',
            ModifyGroupSnapshotResult,
            params,
            since=8
        )

    def modify_schedule(
            self,
            schedule,):
        """
        ModifySchedule is used to change the intervals at which a scheduled snapshot occurs. This allows for adjustment to the snapshot frequency and retention.
        :param schedule: [required] The "Schedule" object will be used to modify an existing schedule. The ScheduleID property is required. Frequency property must be of type that inherits from Frequency. Valid types are: DaysOfMonthFrequency DaysOrWeekFrequency TimeIntervalFrequency 
        :type schedule: Schedule
        """

        self._check_connection_type("modify_schedule", "Cluster")

        params = { 
            "schedule": schedule,
        }
        
        # There is an adaptor!
        since = 8
        deprecated = None

        return ElementServiceAdaptor.modify_schedule(self, params,
                                                  since, deprecated)

    def modify_snapshot(
            self,
            snapshot_id,
            expiration_time=OPTIONAL,
            enable_remote_replication=OPTIONAL,):
        """
        ModifySnapshot is used to change the attributes currently assigned to a snapshot.
        Use this API method to enable the snapshots created on the Read/Write (source) volume to be remotely replicated to a target SolidFire storage system.
        :param snapshotID: [required] ID of the snapshot. 
        :type snapshotID: int

        :param expirationTime:  Use to set the time when the snapshot should be removed. 
        :type expirationTime: str

        :param enableRemoteReplication:  Use to enable the snapshot created to be replicated to a remote SolidFire cluster. Possible values: true: the snapshot will be replicated to remote storage. false: Default. No replication. 
        :type enableRemoteReplication: bool
        """

        self._check_connection_type("modify_snapshot", "Cluster")

        params = { 
            "snapshotID": snapshot_id,
        }
        if expiration_time is not None:
            params["expirationTime"] = expiration_time
        if enable_remote_replication is not None:
            params["enableRemoteReplication"] = enable_remote_replication
        
        # There is no adaptor.
        return self.send_request(
            'ModifySnapshot',
            ModifySnapshotResult,
            params,
            since=8
        )

    def rollback_to_group_snapshot(
            self,
            group_snapshot_id,
            save_current_state,
            name=OPTIONAL,
            attributes=OPTIONAL,):
        """
        RollbackToGroupSnapshot is used to roll back each individual volume in a snapshot group to a copy of their individual snapshots.
        
        Note: Creating a snapshot is allowed if cluster fullness is at stage 2 or 3.
        Snapshots are not created when cluster fullness is at stage 4 or 5.
        :param groupSnapshotID: [required] Unique ID of the group snapshot. 
        :type groupSnapshotID: int

        :param saveCurrentState: [required] true: The previous active volume image is kept. false: (default) The previous active volume image is deleted. 
        :type saveCurrentState: bool

        :param name:  Name for the snapshot. If no name is given, then the name of the snapshot being rolled back to is used with  "-copy" appended to the end of the name. 
        :type name: str

        :param attributes:  List of Name/Value pairs in JSON object format 
        :type attributes: dict
        """

        self._check_connection_type("rollback_to_group_snapshot", "Cluster")

        params = { 
            "groupSnapshotID": group_snapshot_id,
            "saveCurrentState": save_current_state,
        }
        if name is not None:
            params["name"] = name
        if attributes is not None:
            params["attributes"] = attributes
        
        # There is no adaptor.
        return self.send_request(
            'RollbackToGroupSnapshot',
            CreateGroupSnapshotResult,
            params,
            since=7
        )

    def rollback_to_snapshot(
            self,
            volume_id,
            snapshot_id,
            save_current_state,
            name=OPTIONAL,
            attributes=OPTIONAL,):
        """
        RollbackToSnapshot is used to make an existing snapshot the "active" volume image. This method creates a new 
        snapshot from an existing snapshot. The new snapshot becomes "active" and the existing snapshot is preserved until 
        it is manually deleted. The previously "active" snapshot is deleted unless the parameter saveCurrentState is set with 
        a value of "true."
        Note: Creating a snapshot is allowed if cluster fullness is at stage 2 or 3.
        Snapshots are not created when cluster fullness is at stage 4 or 5.
        :param volumeID: [required] VolumeID for the volume. 
        :type volumeID: int

        :param snapshotID: [required] ID of a previously created snapshot on the given volume. 
        :type snapshotID: int

        :param saveCurrentState: [required] true: The previous active volume image is kept. false: (default) The previous active volume image is deleted. 
        :type saveCurrentState: bool

        :param name:  Name for the snapshot. If no name is given, then the name of the snapshot being rolled back to is used with  "-copy" appended to the end of the name. 
        :type name: str

        :param attributes:  List of Name/Value pairs in JSON object format 
        :type attributes: dict
        """

        self._check_connection_type("rollback_to_snapshot", "Cluster")

        params = { 
            "volumeID": volume_id,
            "snapshotID": snapshot_id,
            "saveCurrentState": save_current_state,
        }
        if name is not None:
            params["name"] = name
        if attributes is not None:
            params["attributes"] = attributes
        
        # There is no adaptor.
        return self.send_request(
            'RollbackToSnapshot',
            CreateSnapshotResult,
            params,
            since=6
        )

    def get_complete_stats(
            self,):
        """
        The GetCompleteStats API method is used by SolidFire engineering to troubleshoot new features. The data returned from GetCompleteStats is not documented, changes frequently, and is not guaranteed to be accurate. It is not recommended to ever use GetCompleteStats for collecting performance data or any other management integration with a SolidFire cluster.
        The data returned from GetCompleteStats changes frequently, and is not guaranteed to accurately show performance from the system. It is not recommended to ever use GetCompleteStats for collecting performance data or any other management integration with a SolidFire cluster.        """

        self._check_connection_type("get_complete_stats", "Cluster")

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'GetCompleteStats',
            str,
            params,
            since=1
        )

    def get_hardware_info(
            self,):
        """
        GetHardwareInfo allows you to return hardware information and status for a single node. This generally includes manufacturers, vendors, versions, drives, and other associated hardware identification information.        """

        self._check_connection_type("get_hardware_info", "Node")

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'GetHardwareInfo',
            GetHardwareInfoResult,
            params,
            since=9
        )

    def get_raw_stats(
            self,):
        """
        The GetRawStats call is used by SolidFire engineering to troubleshoot new features. The data returned from GetRawStats is not documented, it changes frequently, and is not guaranteed to be accurate. It is not recommended to ever use GetRawStats for collecting performance data or any other management integration with a SolidFire cluster.
        The data returned from GetRawStats changes frequently, and is not guaranteed to accurately show performance from the system. It is not recommended to ever use GetRawStats for collecting performance data or any other management integration with a SolidFire cluster.        """

        self._check_connection_type("get_raw_stats", "Cluster")

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'GetRawStats',
            str,
            params,
            since=1
        )

    def list_drive_stats(
            self,
            drives=OPTIONAL,):
        """
        ListDriveStats enables you to retrieve  high-level activity measurements for multiple drives in the cluster. By default, this method returns statistics for all drives in the cluster, and these measurements are cumulative from the addition of the drive to the cluster. Some values this method returns are specific to block drives, and some are specific to metadata drives. For more information on what data each drive type returns, see the response examples for the GetDriveStats method.
        :param drives:  Optional list of DriveIDs for which to return drive statistics. If you omit this parameter, measurements for all drives are returned. 
        :type drives: int
        """

        self._check_connection_type("list_drive_stats", "Cluster")

        params = { 
        }
        if drives is not None:
            params["drives"] = drives
        
        # There is no adaptor.
        return self.send_request(
            'ListDriveStats',
            ListDriveStatsResult,
            params,
            since=9
        )

    def list_volume_stats(
            self,
            volume_ids=OPTIONAL,):
        """
        :param volumeIDs:  
        :type volumeIDs: int
        """

        self._check_connection_type("list_volume_stats", "Cluster")

        params = { 
        }
        if volume_ids is not None:
            params["volumeIDs"] = volume_ids
        
        # There is no adaptor.
        return self.send_request(
            'ListVolumeStats',
            ListVolumeStatsResult,
            params,
            since=7
        )

    def list_volume_stats_by_virtual_volume(
            self,
            virtual_volume_ids=OPTIONAL,):
        """
        ListVolumeStatsByVirtualVolume enables you to list statistics for volumes, sorted by virtual volumes.
        :param virtualVolumeIDs:  A list of virtual volume  IDs for which to retrieve information. If you specify this parameter, the method returns information about only these virtual volumes. 
        :type virtualVolumeIDs: UUID
        """

        self._check_connection_type("list_volume_stats_by_virtual_volume", "Cluster")

        params = { 
        }
        if virtual_volume_ids is not None:
            params["virtualVolumeIDs"] = virtual_volume_ids
        
        # There is no adaptor.
        return self.send_request(
            'ListVolumeStatsByVirtualVolume',
            ListVolumeStatsByVirtualVolumeResult,
            params,
            since=9
        )

    def create_storage_container(
            self,
            name,
            initiator_secret=OPTIONAL,
            target_secret=OPTIONAL,):
        """
        Creates a new VVols storage container.
        :param name: [required] Name of the storage container. 
        :type name: str

        :param initiatorSecret:  The secret for CHAP authentication for the initiator 
        :type initiatorSecret: str

        :param targetSecret:  The secret for CHAP authentication for the target 
        :type targetSecret: str
        """

        self._check_connection_type("create_storage_container", "Cluster")

        params = { 
            "name": name,
        }
        if initiator_secret is not None:
            params["initiatorSecret"] = initiator_secret
        if target_secret is not None:
            params["targetSecret"] = target_secret
        
        # There is no adaptor.
        return self.send_request(
            'CreateStorageContainer',
            CreateStorageContainerResult,
            params,
            since=9
        )

    def delete_storage_containers(
            self,
            storage_container_ids,):
        """
        Deletes a storage container from the system.
        :param storageContainerIDs: [required] list of storageContainerID of the storage container to delete. 
        :type storageContainerIDs: UUID
        """

        self._check_connection_type("delete_storage_containers", "Cluster")

        params = { 
            "storageContainerIDs": storage_container_ids,
        }
        
        # There is no adaptor.
        return self.send_request(
            'DeleteStorageContainers',
            DeleteStorageContainerResult,
            params,
            since=9
        )

    def get_storage_container_efficiency(
            self,
            storage_container_id,):
        """
        GetStorageContainerEfficiency enables you to retrieve efficiency information about a virtual volume storage container.
        :param storageContainerID: [required] The ID of the storage container for which to retrieve efficiency information. 
        :type storageContainerID: UUID
        """

        self._check_connection_type("get_storage_container_efficiency", "Cluster")

        params = { 
            "storageContainerID": storage_container_id,
        }
        
        # There is no adaptor.
        return self.send_request(
            'GetStorageContainerEfficiency',
            GetStorageContainerEfficiencyResult,
            params,
            since=9
        )

    def list_storage_containers(
            self,
            storage_container_ids=OPTIONAL,):
        """
        Gets information for all storage containers currently in the system.
        :param storageContainerIDs:  List of storage containers to get 
        :type storageContainerIDs: UUID
        """

        self._check_connection_type("list_storage_containers", "Cluster")

        params = { 
        }
        if storage_container_ids is not None:
            params["storageContainerIDs"] = storage_container_ids
        
        # There is no adaptor.
        return self.send_request(
            'ListStorageContainers',
            ListStorageContainersResult,
            params,
            since=9
        )

    def modify_storage_container(
            self,
            storage_container_id,
            initiator_secret=OPTIONAL,
            target_secret=OPTIONAL,):
        """
        Modifies an existing storage container.
        :param storageContainerID: [required] 
        :type storageContainerID: UUID

        :param initiatorSecret:  
        :type initiatorSecret: str

        :param targetSecret:  
        :type targetSecret: str
        """

        self._check_connection_type("modify_storage_container", "Cluster")

        params = { 
            "storageContainerID": storage_container_id,
        }
        if initiator_secret is not None:
            params["initiatorSecret"] = initiator_secret
        if target_secret is not None:
            params["targetSecret"] = target_secret
        
        # There is no adaptor.
        return self.send_request(
            'ModifyStorageContainer',
            ModifyStorageContainerResult,
            params,
            since=9
        )

    def list_tests(
            self,):
        """
        The ListTests API method is used to return the tests that are available to run on a node.
        Note: This method is available only through the per-node API endpoint 5.0 or later.        """

        self._check_connection_type("list_tests", "Node")

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'ListTests',
            ListTestsResult,
            params,
            since=5
        )

    def list_utilities(
            self,):
        """
        The ListUtilities API method is used to return the tests that are available to run on a node.
        Note: This method is available only through the per-node API endpoint 5.0 or later.        """

        self._check_connection_type("list_utilities", "Node")

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'ListUtilities',
            ListUtilitiesResult,
            params,
            since=5
        )

    def test_connect_ensemble(
            self,
            ensemble=OPTIONAL,):
        """
        The TestConnectEnsemble API method is used to verify connectivity with a sepcified database ensemble. By default it uses the ensemble for the cluster the node is associated with. Alternatively you can provide a different ensemble to test connectivity with.
        Note: This method is available only through the per-node API endpoint 5.0 or later.
        :param ensemble:  A comma-separated list of ensemble node CIPs for connectivity testing 
        :type ensemble: str
        """

        self._check_connection_type("test_connect_ensemble", "Node")

        params = { 
        }
        if ensemble is not None:
            params["ensemble"] = ensemble
        
        # There is no adaptor.
        return self.send_request(
            'TestConnectEnsemble',
            TestConnectEnsembleResult,
            params,
            since=5
        )

    def test_connect_mvip(
            self,
            mvip=OPTIONAL,):
        """
        The TestConnectMvip API method is used to test the management connection to the cluster. The test pings the MVIP and executes a simple API method to verify connectivity.
        Note: This method is available only through the per-node API endpoint 5.0 or later.
        :param mvip:  Optionally, use to test the management connection of a different MVIP. This is not needed to test the connection to the target cluster. 
        :type mvip: str
        """

        self._check_connection_type("test_connect_mvip", "Node")

        params = { 
        }
        if mvip is not None:
            params["mvip"] = mvip
        
        # There is no adaptor.
        return self.send_request(
            'TestConnectMvip',
            TestConnectMvipResult,
            params,
            since=5
        )

    def test_connect_svip(
            self,
            svip=OPTIONAL,):
        """
        The TestConnectSvip API method is used to test the storage connection to the cluster. The test pings the SVIP using ICMP packets and when successful connects as an iSCSI initiator.
        Note: This method is available only through the per-node API endpoint 5.0 or later.
        :param svip:  Optionally, use to test the storage connection of a different SVIP. This is not needed to test the connection to the target cluster. 
        :type svip: str
        """

        self._check_connection_type("test_connect_svip", "Node")

        params = { 
        }
        if svip is not None:
            params["svip"] = svip
        
        # There is no adaptor.
        return self.send_request(
            'TestConnectSvip',
            TestConnectSvipResult,
            params,
            since=5
        )

    def test_ping(
            self,
            attempts=OPTIONAL,
            hosts=OPTIONAL,
            total_timeout_sec=OPTIONAL,
            packet_size=OPTIONAL,
            ping_timeout_msec=OPTIONAL,):
        """
        The TestPing API method is used to validate the connection to all nodes in the cluster on both 1G and 10G interfaces using ICMP packets. The test uses the appropriate MTU sizes for each packet based on the MTU settings in the network configuration.
        Note: This method is available only through the per-node API endpoint 5.0 or later.
        :param attempts:  Specifies the number of times the system should repeat the test ping. Default is 5. 
        :type attempts: int

        :param hosts:  Specify address or hostnames of devices to ping. 
        :type hosts: str

        :param totalTimeoutSec:  Specifies the length of time the ping should wait for a system response before issuing the next ping attempt or ending the process. 
        :type totalTimeoutSec: int

        :param packetSize:  Specify the number of bytes to send in the ICMP packet sent to each IP. Number be less than the maximum MTU specified in the network configuration. 
        :type packetSize: int

        :param pingTimeoutMsec:  Specify the number of milliseconds to wait for each individual ping response. Default is 500ms. 
        :type pingTimeoutMsec: int
        """

        self._check_connection_type("test_ping", "Node")

        params = { 
        }
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
        
        # There is no adaptor.
        return self.send_request(
            'TestPing',
            TestPingResult,
            params,
            since=5
        )

    def list_virtual_networks(
            self,
            virtual_network_id=OPTIONAL,
            virtual_network_tag=OPTIONAL,
            virtual_network_ids=OPTIONAL,
            virtual_network_tags=OPTIONAL,):
        """
        ListVirtualNetworks is used to get a list of all the configured virtual networks for the cluster. This method can be used to verify the virtual network settings in the cluster.
        
        This method does not require any parameters to be passed. But, one or more VirtualNetworkIDs or VirtualNetworkTags can be passed in order to filter the results.
        :param virtualNetworkID:  Network ID to filter the list for a single virtual network 
        :type virtualNetworkID: int

        :param virtualNetworkTag:  Network Tag to filter the list for a single virtual network 
        :type virtualNetworkTag: int

        :param virtualNetworkIDs:  NetworkIDs to include in the list. 
        :type virtualNetworkIDs: int

        :param virtualNetworkTags:  Network Tags to include in the list. 
        :type virtualNetworkTags: int
        """

        self._check_connection_type("list_virtual_networks", "Cluster")

        params = { 
        }
        if virtual_network_id is not None:
            params["virtualNetworkID"] = virtual_network_id
        if virtual_network_tag is not None:
            params["virtualNetworkTag"] = virtual_network_tag
        if virtual_network_ids is not None:
            params["virtualNetworkIDs"] = virtual_network_ids
        if virtual_network_tags is not None:
            params["virtualNetworkTags"] = virtual_network_tags
        
        # There is no adaptor.
        return self.send_request(
            'ListVirtualNetworks',
            ListVirtualNetworksResult,
            params,
            since=7
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
        AddVirtualNetwork is used to add a new virtual network to a cluster configuration. When a virtual network is added, an interface for each node is created and each will require a virtual network IP address. The number of IP addresses specified as a parameter for this API method must be equal to or greater than the number of nodes in the cluster. Virtual network addresses are bulk provisioned by SolidFire and assigned to individual nodes automatically. Virtual network addresses do not need to be assigned to nodes manually.
        
        Note: The AddVirtualNetwork method is used only to create a new virtual network. If you want to make changes to a virtual network, please use the ModifyVirtualNetwork method.
        :param virtualNetworkTag: [required] A unique virtual network (VLAN) tag. Supported values are 1 to 4095 (the number zero (0) is not supported). 
        :type virtualNetworkTag: int

        :param name: [required] User defined name for the new virtual network. 
        :type name: str

        :param addressBlocks: [required] Unique Range of IP addresses to include in the virtual network. Attributes for this parameter are: start: start of the IP address range. (String) size: numbre of IP addresses to include in the block. (Integer) 
        :type addressBlocks: AddressBlock

        :param netmask: [required] Unique netmask for the virtual network being created. 
        :type netmask: str

        :param svip: [required] Unique storage IP address for the virtual network being created. 
        :type svip: str

        :param gateway:   
        :type gateway: str

        :param namespace:   
        :type namespace: bool

        :param attributes:  List of Name/Value pairs in JSON object format. 
        :type attributes: dict
        """

        self._check_connection_type("add_virtual_network", "Cluster")

        params = { 
            "virtualNetworkTag": virtual_network_tag,
            "name": name,
            "addressBlocks": address_blocks,
            "netmask": netmask,
            "svip": svip,
        }
        if gateway is not None:
            if self.api_version < 9.0:
                raise ApiParameterVersionError("add_virtual_network", 9.0,
                    [("gateway", gateway, 9.0, False)])
            else:
                params["gateway"] = gateway
        if namespace is not None:
            if self.api_version < 9.0:
                raise ApiParameterVersionError("add_virtual_network", 9.0,
                    [("namespace", namespace, 9.0, False)])
            else:
                params["namespace"] = namespace
        if attributes is not None:
            params["attributes"] = attributes
        
        # There is no adaptor.
        return self.send_request(
            'AddVirtualNetwork',
            AddVirtualNetworkResult,
            params,
            since=7
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
        ModifyVirtualNetwork is used to change various attributes of a VirtualNetwork object. This method can be used to add or remove address blocks, change the netmask IP, or modify the name or description of the virtual network.
        
        Note: This method requires either the VirtualNetworkID or the VirtualNetworkTag as a parameter, but not both.
        :param virtualNetworkID:  Unique identifier of the virtual network to modify. This is the virtual network ID assigned by the SolidFire cluster. 
        :type virtualNetworkID: int

        :param virtualNetworkTag:  Network Tag that identifies the virtual network to modify. 
        :type virtualNetworkTag: int

        :param name:  New name for the virtual network. 
        :type name: str

        :param addressBlocks:  New addressBlock to set for this Virtual Network object. This may contain new address blocks to add to the existing object or it may omit unused address blocks that need to be removed. Alternatively, existing address blocks may be extended or reduced in size. The size of the starting addressBlocks for a Virtual Network object can only be increased, and can never be decreased. Attributes for this parameter are: start: start of the IP address range. (String) size: numbre of IP addresses to include in the block. (Integer) 
        :type addressBlocks: AddressBlock

        :param netmask:  New netmask for this virtual network. 
        :type netmask: str

        :param svip:  The storage virtual IP address for this virtual network. The svip for Virtual Network cannot be changed. A new Virtual Network must be created in order to use a different svip address. 
        :type svip: str

        :param gateway:   
        :type gateway: str

        :param namespace:   
        :type namespace: bool

        :param attributes:  A new list of Name/Value pairs in JSON object format. 
        :type attributes: dict
        """

        self._check_connection_type("modify_virtual_network", "Cluster")

        params = { 
        }
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
            if self.api_version < 9.0:
                raise ApiParameterVersionError("modify_virtual_network", 9.0,
                    [("gateway", gateway, 9.0, False)])
            else:
                params["gateway"] = gateway
        if namespace is not None:
            if self.api_version < 9.0:
                raise ApiParameterVersionError("modify_virtual_network", 9.0,
                    [("namespace", namespace, 9.0, False)])
            else:
                params["namespace"] = namespace
        if attributes is not None:
            params["attributes"] = attributes
        
        # There is no adaptor.
        return self.send_request(
            'ModifyVirtualNetwork',
            AddVirtualNetworkResult,
            params,
            since=7
        )

    def remove_virtual_network(
            self,
            virtual_network_id=OPTIONAL,
            virtual_network_tag=OPTIONAL,):
        """
        RemoveVirtualNetwork is used to remove a previously added virtual network.
        
        Note: This method requires either the VirtualNetworkID of the VirtualNetworkTag as a parameter, but not both.
        :param virtualNetworkID:  Network ID that identifies the virtual network to remove. 
        :type virtualNetworkID: int

        :param virtualNetworkTag:  Network Tag that identifies the virtual network to remove. 
        :type virtualNetworkTag: int
        """

        self._check_connection_type("remove_virtual_network", "Cluster")

        params = { 
        }
        if virtual_network_id is not None:
            params["virtualNetworkID"] = virtual_network_id
        if virtual_network_tag is not None:
            params["virtualNetworkTag"] = virtual_network_tag
        
        # There is no adaptor.
        return self.send_request(
            'RemoveVirtualNetwork',
            RemoveVirtualNetworkResult,
            params,
            since=7
        )

    def enable_feature(
            self,
            feature,):
        """
        EnableFeature allows you to enable cluster features that are disabled by default.
        :param feature: [required] Valid values: vvols: Enable the Virtual Volumes (VVOLs) cluster feature. 
        :type feature: str
        """

        self._check_connection_type("enable_feature", "Cluster")

        params = { 
            "feature": feature,
        }
        
        # There is no adaptor.
        return self.send_request(
            'EnableFeature',
            EnableFeatureResult,
            params,
            since=9
        )

    def get_feature_status(
            self,
            feature=OPTIONAL,):
        """
        GetFeatureStatus allows you to retrieve the status of a cluster feature.
        :param feature:  Valid values: vvols: Find the status of the Virtual Volumes (VVOLs) cluster feature. 
        :type feature: str
        """

        self._check_connection_type("get_feature_status", "Cluster")

        params = { 
        }
        if feature is not None:
            params["feature"] = feature
        
        # There is no adaptor.
        return self.send_request(
            'GetFeatureStatus',
            GetFeatureStatusResult,
            params,
            since=9
        )

    def get_virtual_volume_count(
            self,):
        """
        Enables retrieval of the number of virtual volumes currently in the system.        """

        self._check_connection_type("get_virtual_volume_count", "Cluster")

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'GetVirtualVolumeCount',
            GetVirtualVolumeCountResult,
            params,
            since=9
        )

    def list_virtual_volume_bindings(
            self,
            virtual_volume_binding_ids=OPTIONAL,):
        """
        ListVirtualVolumeBindings returns a list of VVol bindings.
        :param virtualVolumeBindingIDs:  
        :type virtualVolumeBindingIDs: int
        """

        self._check_connection_type("list_virtual_volume_bindings", "Cluster")

        params = { 
        }
        if virtual_volume_binding_ids is not None:
            params["virtualVolumeBindingIDs"] = virtual_volume_binding_ids
        
        # There is no adaptor.
        return self.send_request(
            'ListVirtualVolumeBindings',
            ListVirtualVolumeBindingsResult,
            params,
            since=9
        )

    def list_virtual_volume_hosts(
            self,
            virtual_volume_host_ids=OPTIONAL,):
        """
        ListVirtualVolumeHosts returns a list of known ESX hosts.
        :param virtualVolumeHostIDs:  
        :type virtualVolumeHostIDs: UUID
        """

        self._check_connection_type("list_virtual_volume_hosts", "Cluster")

        params = { 
        }
        if virtual_volume_host_ids is not None:
            params["virtualVolumeHostIDs"] = virtual_volume_host_ids
        
        # There is no adaptor.
        return self.send_request(
            'ListVirtualVolumeHosts',
            ListVirtualVolumeHostsResult,
            params,
            since=9
        )

    def list_virtual_volume_tasks(
            self,
            virtual_volume_task_ids=OPTIONAL,):
        """
        ListVirtualVolumeTasks returns a list of VVol Async Tasks.
        :param virtualVolumeTaskIDs:  
        :type virtualVolumeTaskIDs: UUID
        """

        self._check_connection_type("list_virtual_volume_tasks", "Cluster")

        params = { 
        }
        if virtual_volume_task_ids is not None:
            params["virtualVolumeTaskIDs"] = virtual_volume_task_ids
        
        # There is no adaptor.
        return self.send_request(
            'ListVirtualVolumeTasks',
            ListVirtualVolumeTasksResult,
            params,
            since=9
        )

    def list_virtual_volumes(
            self,
            details=OPTIONAL,
            limit=OPTIONAL,
            recursive=OPTIONAL,
            start_virtual_volume_id=OPTIONAL,
            virtual_volume_ids=OPTIONAL,):
        """
        ListVirtualVolumes enables you to list the virtual volumes currently in the system. You can use this method to list all virtual volumes, or only list a subset.
        :param details:  Possible values:true: Include more details about each VVOL in the response.false: Include the standard level of detail about each VVOL in the response. 
        :type details: bool

        :param limit:  The maximum number of virtual volumes to list. 
        :type limit: int

        :param recursive:  Possible values:true: Include information about the children of each VVOL in the response.false: Do not include information about the children of each VVOL in the response. 
        :type recursive: bool

        :param startVirtualVolumeID:  The ID of the virtual volume at which to begin the list. 
        :type startVirtualVolumeID: UUID

        :param virtualVolumeIDs:  A list of virtual volume  IDs for which to retrieve information. If you specify this parameter, the method returns information about only these virtual volumes. 
        :type virtualVolumeIDs: UUID
        """

        self._check_connection_type("list_virtual_volumes", "Cluster")

        params = { 
        }
        if details is not None:
            params["details"] = details
        if limit is not None:
            params["limit"] = limit
        if recursive is not None:
            params["recursive"] = recursive
        if start_virtual_volume_id is not None:
            params["startVirtualVolumeID"] = start_virtual_volume_id
        if virtual_volume_ids is not None:
            params["virtualVolumeIDs"] = virtual_volume_ids
        
        # There is no adaptor.
        return self.send_request(
            'ListVirtualVolumes',
            ListVirtualVolumesResult,
            params,
            since=9
        )

    def cancel_clone(
            self,
            clone_id,):
        """
        Cancels a currently running clone operation. This method does not return anything.
        :param cloneID: [required] 
        :type cloneID: int
        """

        self._check_connection_type("cancel_clone", "Cluster")

        params = { 
            "cloneID": clone_id,
        }
        
        # There is no adaptor.
        return self.send_request(
            'CancelClone',
            CancelCloneResult,
            params,
            since=9
        )

    def cancel_group_clone(
            self,
            group_clone_id,):
        """
        CancelGroupClone enables you to stop an ongoing CloneMultipleVolumes process for a group of clones. When you cancel a group clone operation, the system completes and removes the operation's associated asyncHandle. This method does not return anything.
        :param groupCloneID: [required] cloneID for the ongoing clone process. 
        :type groupCloneID: int
        """

        self._check_connection_type("cancel_group_clone", "Cluster")

        params = { 
            "groupCloneID": group_clone_id,
        }
        
        # There is no adaptor.
        return self.send_request(
            'CancelGroupClone',
            CancelGroupCloneResult,
            params,
            since=9
        )

    def copy_volume(
            self,
            volume_id,
            dst_volume_id,
            snapshot_id=OPTIONAL,):
        """
        Copies one volume to another.
        :param volumeID: [required] Source volume to copy. 
        :type volumeID: int

        :param dstVolumeID: [required] Destination volume for the copy. 
        :type dstVolumeID: int

        :param snapshotID:  Snapshot ID of the source volume to create the copy from. 
        :type snapshotID: int
        """

        self._check_connection_type("copy_volume", "Cluster")

        params = { 
            "volumeID": volume_id,
            "dstVolumeID": dst_volume_id,
        }
        if snapshot_id is not None:
            params["snapshotID"] = snapshot_id
        
        # There is no adaptor.
        return self.send_request(
            'CopyVolume',
            CopyVolumeResult,
            params,
            since=9
        )

    def delete_volumes(
            self,
            account_ids=OPTIONAL,
            volume_access_group_ids=OPTIONAL,
            volume_ids=OPTIONAL,):
        """
        DeleteVolumes marks multiple (up to 500) active volumes for deletion. Once marked, the volumes are purged (permanently deleted) after the cleanup interval elapses.The cleanup interval can be set in the SetClusterSettings method. For more information on using this method, see SetClusterSettings on page 1. After making a request to delete volumes, any active iSCSI connections to the volumes are immediately terminated and no further connections are allowed while the volumes are in this state. A marked volume is not returned in target discovery requests. Any snapshots of a volume that has been marked for deletion are not affected. Snapshots are kept until the volume is purged from the system. If a volume is marked for deletion and has a bulk volume read or bulk volume write operation in progress, the bulk volume read or write operation is stopped. If the volumes you delete are paired with a volume, replication between the paired volumes is suspended and no data is transferred to them or from them while in a deleted state. The remote volumes the deleted volumes were paired with enter into a PausedMisconfigured state and data is no longer sent to them or from the deleted volumes. Until the deleted volumes are purged, they can be restored and data transfers resume. If the deleted volumes are purged from the system, the volumes they were paired with enter into a StoppedMisconfigured state and the volume pairing status is removed. The purged volumes become permanently unavailable.
        :param accountIDs:  A list of account IDs. All volumes from these accounts are deleted from the system.  
        :type accountIDs: int

        :param volumeAccessGroupIDs:  A list of volume access group IDs. All of the volumes from all of the volume access groups you specify in this list are deleted from the system. 
        :type volumeAccessGroupIDs: int

        :param volumeIDs:  The list of IDs of the volumes to delete from the system. 
        :type volumeIDs: int
        """

        self._check_connection_type("delete_volumes", "Cluster")

        params = { 
        }
        if account_ids is not None:
            params["accountIDs"] = account_ids
        if volume_access_group_ids is not None:
            params["volumeAccessGroupIDs"] = volume_access_group_ids
        if volume_ids is not None:
            params["volumeIDs"] = volume_ids
        
        # There is no adaptor.
        return self.send_request(
            'DeleteVolumes',
            DeleteVolumesResult,
            params,
            since=9
        )

    def get_default_qos(
            self,):
        """
        GetDefaultQoS is used to retrieve the default QoS values that are set for a volume if QoS is not supplied.        """

        self._check_connection_type("get_default_qos", "Cluster")

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'GetDefaultQoS',
            VolumeQOS,
            params,
            since=1
        )

    def get_volume_count(
            self,):
        """
        GetVolumeCount enables you to retrieve the number of volumes currently in the system.        """

        self._check_connection_type("get_volume_count", "Cluster")

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'GetVolumeCount',
            GetVolumeCountResult,
            params,
            since=9
        )

    def get_volume_efficiency(
            self,
            volume_id,):
        """
        GetVolumeEfficiency is used to retrieve information about a volume.
        Only the volume given as a parameter in this API method is used to compute the capacity.
        :param volumeID: [required] Specifies the volume for which capacity is computed. 
        :type volumeID: int
        """

        self._check_connection_type("get_volume_efficiency", "Cluster")

        params = { 
            "volumeID": volume_id,
        }
        
        # There is no adaptor.
        return self.send_request(
            'GetVolumeEfficiency',
            GetVolumeEfficiencyResult,
            params,
            since=6
        )

    def get_volume_stats(
            self,
            volume_id,):
        """
        GetVolumeStats is used to retrieve high-level activity measurements for a single volume.
        Values are cumulative from the creation of the volume.
        :param volumeID: [required] Specifies the volume for which statistics is gathered. 
        :type volumeID: int
        """

        self._check_connection_type("get_volume_stats", "Cluster")

        params = { 
            "volumeID": volume_id,
        }
        
        # There is no adaptor.
        return self.send_request(
            'GetVolumeStats',
            GetVolumeStatsResult,
            params,
            since=1
        )

    def list_active_volumes(
            self,
            start_volume_id=OPTIONAL,
            limit=OPTIONAL,):
        """
        ListActiveVolumes is used to return the list of active volumes currently in the system.
        The list of volumes is returned sorted in VolumeID order and can be returned in multiple parts (pages).
        :param startVolumeID:  The ID of the first volume to list. This can be useful for paging results. By default, this starts at the lowest VolumeID. 
        :type startVolumeID: int

        :param limit:  The maximum number of volumes to return from the API. 
        :type limit: int
        """

        self._check_connection_type("list_active_volumes", "Cluster")

        params = { 
        }
        if start_volume_id is not None:
            params["startVolumeID"] = start_volume_id
        if limit is not None:
            params["limit"] = limit
        
        # There is no adaptor.
        return self.send_request(
            'ListActiveVolumes',
            ListActiveVolumesResult,
            params,
            since=1
        )

    def list_async_results(
            self,
            async_result_types=OPTIONAL,):
        """
        You can use ListAsyncResults to list the results of all currently running and completed asynchronous methods on the system. Querying asynchronous results with ListAsyncResults does not cause completed asyncHandles to expire; you can use GetAsyncResult to query any of the asyncHandles returned by ListAsyncResults.
        :param asyncResultTypes:  An optional list of types of results. You can use this list to restrict the results to only these types of operations. Possible values:BulkVolume: Copy operations between volumes, such as backups or restores.Clone: Volume cloning operations.DriveRemoval: Operations involving the system copying data from a drive in preparation to remove it from the cluster.RtfiPendingNode: Operations involving the system installing compatible software on a node before adding it to the cluster. 
        :type asyncResultTypes: str
        """

        self._check_connection_type("list_async_results", "Cluster")

        params = { 
        }
        if async_result_types is not None:
            params["asyncResultTypes"] = async_result_types
        
        # There is no adaptor.
        return self.send_request(
            'ListAsyncResults',
            ListAsyncResultsResult,
            params,
            since=9
        )

    def list_bulk_volume_jobs(
            self,):
        """
        ListBulkVolumeJobs is used to return information about each bulk volume read or write operation that is occurring in the system.        """

        self._check_connection_type("list_bulk_volume_jobs", "Cluster")

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'ListBulkVolumeJobs',
            ListBulkVolumeJobsResult,
            params,
            since=6
        )

    def list_deleted_volumes(
            self,):
        """
        ListDeletedVolumes is used to return the entire list of volumes that have been marked for deletion and is purged from the system.        """

        self._check_connection_type("list_deleted_volumes", "Cluster")

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'ListDeletedVolumes',
            ListDeletedVolumesResult,
            params,
            since=1
        )

    def list_volume_stats_by_account(
            self,):
        """
        ListVolumeStatsByAccount returns high-level activity measurements for every account.
        Values are summed from all the volumes owned by the account.        """

        self._check_connection_type("list_volume_stats_by_account", "Cluster")

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'ListVolumeStatsByAccount',
            ListVolumeStatsByAccountResult,
            params,
            since=1
        )

    def list_volume_stats_by_volume(
            self,):
        """
        ListVolumeStatsByVolume returns high-level activity measurements for every volume, by volume.
        Values are cumulative from the creation of the volume.        """

        self._check_connection_type("list_volume_stats_by_volume", "Cluster")

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'ListVolumeStatsByVolume',
            ListVolumeStatsByVolumeResult,
            params,
            since=1
        )

    def list_volume_stats_by_volume_access_group(
            self,
            volume_access_groups=OPTIONAL,):
        """
        ListVolumeStatsByVolumeAccessGroup is used to get total activity measurements for all of the volumes that are a member of the specified volume access group(s).
        :param volumeAccessGroups:  An array of VolumeAccessGroupIDs for which volume activity is returned. If no VolumeAccessGroupID is specified, stats for all volume access groups is returned. 
        :type volumeAccessGroups: int
        """

        self._check_connection_type("list_volume_stats_by_volume_access_group", "Cluster")

        params = { 
        }
        if volume_access_groups is not None:
            params["volumeAccessGroups"] = volume_access_groups
        
        # There is no adaptor.
        return self.send_request(
            'ListVolumeStatsByVolumeAccessGroup',
            ListVolumeStatsByVolumeAccessGroupResult,
            params,
            since=5
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
        The ListVolumes method is used to return a list of volumes that are in a cluster.
        You can specify the volumes you want to return in the list by using the available parameters.
        :param startVolumeID:  The ID of the first volume to list. This can be useful for paging results. By default, this starts at the lowest VolumeID. 
        :type startVolumeID: int

        :param limit:  The maximum number of volumes to return from the API. 
        :type limit: int

        :param volumeStatus:  If specified, filter to only volumes with the provided status. By default, list all volumes. 
        :type volumeStatus: str

        :param accounts:  If specified, only fetch volumes which belong to the provided accounts. By default, list volumes for all accounts. 
        :type accounts: int

        :param isPaired:  If specified, only fetch volumes which are paired (if true) or non-paired (if false). By default, list all volumes regardless of their pairing status. 
        :type isPaired: bool

        :param volumeIDs:  If specified, only fetch volumes specified in this list. This option cannot be specified if startVolumeID, limit, or accounts option is specified. 
        :type volumeIDs: int
        """

        self._check_connection_type("list_volumes", "Cluster")

        params = { 
        }
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
            if self.api_version < 9.0:
                raise ApiParameterVersionError("list_volumes", 9.0,
                    [("volume_ids", volume_ids, 9.0, False)])
            else:
                params["volumeIDs"] = volume_ids
        
        # There is no adaptor.
        return self.send_request(
            'ListVolumes',
            ListVolumesResult,
            params,
            since=8
        )

    def list_volumes_for_account(
            self,
            account_id,
            start_volume_id=OPTIONAL,
            limit=OPTIONAL,):
        """
        ListVolumesForAccount returns the list of active AND (pending) deleted volumes for an account.
        :param accountID: [required] The ID of the account to list the volumes for. 
        :type accountID: int

        :param startVolumeID:  The ID of the first volume to list. This can be useful for paging results. By default, this starts at the lowest VolumeID. 
        :type startVolumeID: int

        :param limit:  The maximum number of volumes to return from the API. 
        :type limit: int
        """

        self._check_connection_type("list_volumes_for_account", "Cluster")

        params = { 
            "accountID": account_id,
        }
        if start_volume_id is not None:
            params["startVolumeID"] = start_volume_id
        if limit is not None:
            params["limit"] = limit
        
        # There is no adaptor.
        return self.send_request(
            'ListVolumesForAccount',
            ListVolumesForAccountResult,
            params,
            since=1
        )

    def modify_volumes(
            self,
            volume_ids,
            account_id=OPTIONAL,
            access=OPTIONAL,
            qos=OPTIONAL,
            total_size=OPTIONAL,
            attributes=OPTIONAL,):
        """
        ModifyVolumes allows you to configure up to 500 existing volumes at one time. Changes take place immediately. If ModifyVolumes fails to modify any of the specified volumes, none of the specified volumes are changed.If you do not specify QoS values when you modify volumes, the QoS values for each volume remain unchanged. You can retrieve default QoS values for a newly created volume by running the GetDefaultQoS method.When you need to increase the size of volumes that are being replicated, do so in the following order to prevent replication errors:Increase the size of the "Replication Target" volume.Increase the size of the source or "Read / Write" volume. recommends that both the target and source volumes be the same size.NOTE: If you change access status to locked or replicationTarget all existing iSCSI connections are terminated.
        :param volumeIDs: [required] A list of volumeIDs for the volumes to be modified. 
        :type volumeIDs: int

        :param accountID:  AccountID to which the volume is reassigned. If none is specified, the previous account name is used. 
        :type accountID: int

        :param access:  Access allowed for the volume. Possible values:readOnly: Only read operations are allowed.readWrite: Reads and writes are allowed.locked: No reads or writes are allowed.If not specified, the access value does not change.replicationTarget: Identify a volume as the target volume for a paired set of volumes. If the volume is not paired, the access status is locked.If a value is not specified, the access value does not change.  
        :type access: str

        :param qos:  New quality of service settings for this volume.If not specified, the QoS settings are not changed. 
        :type qos: QoS

        :param totalSize:  New size of the volume in bytes. 1000000000 is equal to 1GB. Size is rounded up to the nearest 1MB in size. This parameter can only be used to increase the size of a volume. 
        :type totalSize: int

        :param attributes:  
        :type attributes: dict
        """

        self._check_connection_type("modify_volumes", "Cluster")

        params = { 
            "volumeIDs": volume_ids,
        }
        if account_id is not None:
            params["accountID"] = account_id
        if access is not None:
            params["access"] = access
        if qos is not None:
            params["qos"] = qos
        if total_size is not None:
            params["totalSize"] = total_size
        if attributes is not None:
            params["attributes"] = attributes
        
        # There is no adaptor.
        return self.send_request(
            'ModifyVolumes',
            ModifyVolumesResult,
            params,
            since=9
        )

    def purge_deleted_volume(
            self,
            volume_id,):
        """
        PurgeDeletedVolume immediately and permanently purges a volume which has been deleted.
        A volume must be deleted using DeleteVolume before it can be purged.
        Volumes are purged automatically after a period of time, so usage of this method is not typically required.
        :param volumeID: [required] The ID of the volume to purge. 
        :type volumeID: int
        """

        self._check_connection_type("purge_deleted_volume", "Cluster")

        params = { 
            "volumeID": volume_id,
        }
        
        # There is no adaptor.
        return self.send_request(
            'PurgeDeletedVolume',
            PurgeDeletedVolumeResult,
            params,
            since=1
        )

    def purge_deleted_volumes(
            self,
            volume_ids=OPTIONAL,
            account_ids=OPTIONAL,
            volume_access_group_ids=OPTIONAL,):
        """
        PurgeDeletedVolumes immediately and permanently purges volumes that have been deleted; you can use this method to purge up to 500 volumes at one time. You must delete volumes using DeleteVolumes before they can be purged. Volumes are purged by the system automatically after a period of time, so usage of this method is not typically required.
        :param volumeIDs:  A list of volumeIDs of volumes to be purged from the system. 
        :type volumeIDs: int

        :param accountIDs:  A list of accountIDs. All of the volumes from all of the specified accounts are purged from the system. 
        :type accountIDs: int

        :param volumeAccessGroupIDs:  A list of volumeAccessGroupIDs. All of the volumes from all of the specified Volume Access Groups are purged from the system. 
        :type volumeAccessGroupIDs: int
        """

        self._check_connection_type("purge_deleted_volumes", "Cluster")

        params = { 
        }
        if volume_ids is not None:
            params["volumeIDs"] = volume_ids
        if account_ids is not None:
            params["accountIDs"] = account_ids
        if volume_access_group_ids is not None:
            params["volumeAccessGroupIDs"] = volume_access_group_ids
        
        # There is no adaptor.
        return self.send_request(
            'PurgeDeletedVolumes',
            PurgeDeletedVolumesResult,
            params,
            since=9
        )

    def restore_deleted_volume(
            self,
            volume_id,):
        """
        RestoreDeletedVolume marks a deleted volume as active again.
        This action makes the volume immediately available for iSCSI connection.
        :param volumeID: [required] VolumeID for the deleted volume to restore. 
        :type volumeID: int
        """

        self._check_connection_type("restore_deleted_volume", "Cluster")

        params = { 
            "volumeID": volume_id,
        }
        
        # There is no adaptor.
        return self.send_request(
            'RestoreDeletedVolume',
            RestoreDeletedVolumeResult,
            params,
            since=1
        )

    def set_default_qos(
            self,
            min_iops=OPTIONAL,
            max_iops=OPTIONAL,
            burst_iops=OPTIONAL,):
        """
        SetDefaultQoS enables you to configure the default Quality of Service (QoS) values (measured in inputs and outputs per second, or IOPS) for all volumes not yet created.
        :param minIOPS:  The minimum number of sustained IOPS that are provided by the cluster to a volume. 
        :type minIOPS: int

        :param maxIOPS:  The maximum number of sustained IOPS that are provided by the cluster to a volume. 
        :type maxIOPS: int

        :param burstIOPS:  The maximum number of IOPS allowed in a short burst scenario. 
        :type burstIOPS: int
        """

        self._check_connection_type("set_default_qos", "Cluster")

        params = { 
        }
        if min_iops is not None:
            params["minIOPS"] = min_iops
        if max_iops is not None:
            params["maxIOPS"] = max_iops
        if burst_iops is not None:
            params["burstIOPS"] = burst_iops
        
        # There is no adaptor.
        return self.send_request(
            'SetDefaultQoS',
            SetDefaultQoSResult,
            params,
            since=9
        )

    def clone_multiple_volumes(
            self,
            volumes,
            access=OPTIONAL,
            group_snapshot_id=OPTIONAL,
            new_account_id=OPTIONAL,):
        """
        CloneMultipleVolumes is used to create a clone of a group of specified volumes. A consistent set of characteristics can be assigned to a group of multiple volume when they are cloned together.
        If groupSnapshotID is going to be used to clone the volumes in a group snapshot, the group snapshot must be created first using the CreateGroupSnapshot API method or the SolidFire Element WebUI. Using groupSnapshotID is optional when cloning multiple volumes.
        
        Note: Cloning multiple volumes is allowed if cluster fullness is at stage 2 or 3. Clones are not created when cluster fullness is at stage 4 or 5.
        :param volumes: [required] Array of Unique ID for each volume to include in the clone with optional parameters. If optional parameters are not specified, the values will be inherited from the source volumes. 
        :type volumes: CloneMultipleVolumeParams

        :param access:  New default access method for the new volumes if not overridden by information passed in the volumes array. readOnly: Only read operations are allowed. readWrite: Reads and writes are allowed. locked: No reads or writes are allowed. replicationTarget: Identify a volume as the target volume for a paired set of volumes. If the volume is not paired, the access status is locked.  If unspecified, the access settings of the clone will be the same as the source. 
        :type access: str

        :param groupSnapshotID:  ID of the group snapshot to use as a basis for the clone. 
        :type groupSnapshotID: int

        :param newAccountID:  New account ID for the volumes if not overridden by information passed in the volumes array. 
        :type newAccountID: int
        """

        self._check_connection_type("clone_multiple_volumes", "Cluster")

        params = { 
            "volumes": volumes,
        }
        if access is not None:
            params["access"] = access
        if group_snapshot_id is not None:
            params["groupSnapshotID"] = group_snapshot_id
        if new_account_id is not None:
            params["newAccountID"] = new_account_id
        
        # There is no adaptor.
        return self.send_request(
            'CloneMultipleVolumes',
            CloneMultipleVolumesResult,
            params,
            since=7
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
        CloneVolume is used to create a copy of the volume.
        This method is asynchronous and may take a variable amount of time to complete.
        The cloning process begins immediately when the CloneVolume request is made and is representative of the state of the volume when the API method is issued.
        GetAsyncResults can be used to determine when the cloning process is complete and the new volume is available for connections.
        ListSyncJobs can be used to see the progress of creating the clone.
        
        Note: The initial attributes and quality of service settings for the volume are inherited from the volume being cloned.
        If different settings are required, they can be changed via ModifyVolume.
        
        Note: Cloned volumes do not inherit volume access group memberships from the source volume.
        :param volumeID: [required] The ID of the volume to clone. 
        :type volumeID: int

        :param name: [required] The name for the newly-created volume. 
        :type name: str

        :param newAccountID:  AccountID for the owner of the new volume. If unspecified, the AccountID of the owner of the volume being cloned is used. 
        :type newAccountID: int

        :param newSize:  New size of the volume, in bytes. May be greater or less than the size of the volume being cloned. If unspecified, the clone's volume size will be the same as the source volume. Size is rounded up to the nearest 1 MiB. 
        :type newSize: int

        :param access:  Access settings for the new volume. readOnly: Only read operations are allowed. readWrite: Reads and writes are allowed. locked: No reads or writes are allowed. replicationTarget: Identify a volume as the target volume for a paired set of volumes. If the volume is not paired, the access status is locked.  If unspecified, the access settings of the clone will be the same as the source. 
        :type access: str

        :param snapshotID:  ID of the snapshot to use as the source of the clone. If unspecified, the clone will be created with a snapshot of the active volume. 
        :type snapshotID: int

        :param attributes:  List of Name/Value pairs in JSON object format. 
        :type attributes: dict
        """

        self._check_connection_type("clone_volume", "Cluster")

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
        
        # There is no adaptor.
        return self.send_request(
            'CloneVolume',
            CloneVolumeResult,
            params,
            since=1
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
        CreateVolume is used to create a new (empty) volume on the cluster.
        When the volume is created successfully it is available for connection via iSCSI.
        :param name: [required] Name of the volume. Not required to be unique, but it is recommended. May be 1 to 64 characters in length. 
        :type name: str

        :param accountID: [required] AccountID for the owner of this volume. 
        :type accountID: int

        :param totalSize: [required] Total size of the volume, in bytes. Size is rounded up to the nearest 1MB size. 
        :type totalSize: int

        :param enable512e: [required] Should the volume provides 512-byte sector emulation? 
        :type enable512e: bool

        :param qos:  Initial quality of service settings for this volume.  Volumes created without specified QoS values are created with the default values for QoS. Default values for a volume can be found by running the GetDefaultQoS method. 
        :type qos: QoS

        :param attributes:  List of Name/Value pairs in JSON object format. 
        :type attributes: dict
        """

        self._check_connection_type("create_volume", "Cluster")

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
        
        # There is no adaptor.
        return self.send_request(
            'CreateVolume',
            CreateVolumeResult,
            params,
            since=1
        )

    def delete_volume(
            self,
            volume_id,):
        """
        DeleteVolume marks an active volume for deletion.
        It is purged (permanently deleted) after the cleanup interval elapses.
        After making a request to delete a volume, any active iSCSI connections to the volume is immediately terminated and no further connections are allowed while the volume is in this state.
        It is not returned in target discovery requests.
        
        Any snapshots of a volume that has been marked to delete are not affected.
        Snapshots are kept until the volume is purged from the system.
        
        If a volume is marked for deletion, and it has a bulk volume read or bulk volume write operation in progress, the bulk volume operation is stopped.
        
        If the volume you delete is paired with a volume, replication between the paired volumes is suspended and no data is transferred to it or from it while in a deleted state.
        The remote volume the deleted volume was paired with enters into a PausedMisconfigured state and data is no longer sent to it or from the deleted volume.
        Until the deleted volume is purged, it can be restored and data transfers resumes.
        If the deleted volume gets purged from the system, the volume it was paired with enters into a StoppedMisconfigured state and the volume pairing status is removed.
        The purged volume becomes permanently unavailable.
        :param volumeID: [required] The ID of the volume to delete. 
        :type volumeID: int
        """

        self._check_connection_type("delete_volume", "Cluster")

        params = { 
            "volumeID": volume_id,
        }
        
        # There is no adaptor.
        return self.send_request(
            'DeleteVolume',
            DeleteVolumeResult,
            params,
            since=1
        )

    def get_async_result(
            self,
            async_handle,):
        """
        Used to retrieve the result of asynchronous method calls.
        Some method calls are long running and do not complete when the initial response is sent.
        To obtain the result of the method call, polling with GetAsyncResult is required.
        
        GetAsyncResult returns the overall status of the operation (in progress, completed, or error) in a standard fashion,
        but the actual data returned for the operation depends on the original method call and the return data is documented with each method.
        
        The result for a completed asynchronous method call can only be retrieved once.
        Once the final result has been returned, later attempts returns an error.
        :param asyncHandle: [required] A value that was returned from the original asynchronous method call. 
        :type asyncHandle: int
        """

        self._check_connection_type("get_async_result", "Cluster")

        params = { 
            "asyncHandle": async_handle,
        }
        
        # There is no adaptor.
        return self.send_request(
            'GetAsyncResult',
            GetAsyncResultResult,
            params,
            since=1
        )

    def modify_volume(
            self,
            volume_id,
            account_id=OPTIONAL,
            access=OPTIONAL,
            qos=OPTIONAL,
            total_size=OPTIONAL,
            attributes=OPTIONAL,):
        """
        ModifyVolume is used to modify settings on an existing volume.
        Modifications can be made to one volume at a time and changes take place immediately.
        If an optional parameter is left unspecified, the value will not be changed.
        
        Extending the size of a volume that is being replicated should be done in an order.
        The target (Replication Target) volume should first be increased in size, then the source (Read/Write) volume can be resized.
        It is recommended that both the target and the source volumes be the same size.
        
        Note: If you change access status to locked or target all existing iSCSI connections are terminated.
        :param volumeID: [required] VolumeID for the volume to be modified. 
        :type volumeID: int

        :param accountID:  AccountID to which the volume is reassigned. If none is specified, the previous account name is used. 
        :type accountID: int

        :param access:  Access allowed for the volume. readOnly: Only read operations are allowed. readWrite: Reads and writes are allowed. locked: No reads or writes are allowed. replicationTarget: Identify a volume as the target volume for a paired set of volumes. If the volume is not paired, the access status is locked.  If unspecified, the access settings of the clone will be the same as the source. 
        :type access: str

        :param qos:  New quality of service settings for this volume. 
        :type qos: QoS

        :param totalSize:  New size of the volume in bytes. Size is rounded up to the nearest 1MiB size. This parameter can only be used to *increase* the size of a volume. 
        :type totalSize: int

        :param attributes:  List of Name/Value pairs in JSON object format. 
        :type attributes: dict
        """

        self._check_connection_type("modify_volume", "Cluster")

        params = { 
            "volumeID": volume_id,
        }
        if account_id is not None:
            params["accountID"] = account_id
        if access is not None:
            params["access"] = access
        if qos is not None:
            params["qos"] = qos
        if total_size is not None:
            params["totalSize"] = total_size
        if attributes is not None:
            params["attributes"] = attributes
        
        # There is no adaptor.
        return self.send_request(
            'ModifyVolume',
            ModifyVolumeResult,
            params,
            since=1
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
        StartBulkVolumeRead allows you to initialize a bulk volume read session on a specified volume.
        Only two bulk volume processes can run simultaneously on a volume.
        When you initialize the session, data is read from a SolidFire storage volume for the purposes of storing the data on an external backup source.
        The external data is accessed by a web server running on a SolidFire node.
        Communications and server interaction information for external data access is passed by a script running on the SolidFire storage system.
        
        At the start of a bulk volume read operation, a snapshot of the volume is made and the snapshot is deleted when the read has completed.
        You can also read a snapshot of the volume by entering the ID of the snapshot as a parameter.
        Reading a previous snapshot does not create a new snapshot of the volume, nor does the previous snapshot be deleted when the read completes.
        
        Note: This process creates a new snapshot if the ID of an existing snapshot is not provided.
        Snapshots can be created if cluster fullness is at stage 2 or 3.
        Snapshots are not created when cluster fullness is at stage 4 or 5.
        :param volumeID: [required] ID of the volume to be read. 
        :type volumeID: int

        :param format: [required] The format of the volume data. Can be either: uncompressed: every byte of the volume is returned without any compression. native: opaque data is returned that is smaller and more efficiently stored and written on a subsequent bulk volume write. 
        :type format: str

        :param snapshotID:  ID of a previously created snapshot used for bulk volume reads. If no ID is entered, a snapshot of the current active volume image is made. 
        :type snapshotID: int

        :param script:  Executable name of a script. If no script name is given then the key and URL is necessary to access SolidFire nodes. The script is run on the primary node and the key and URL is returned to the script so the local web server can be contacted. 
        :type script: str

        :param scriptParameters:  JSON parameters to pass to the script. 
        :type scriptParameters: str

        :param attributes:  JSON attributes for the bulk volume job. 
        :type attributes: dict
        """

        self._check_connection_type("start_bulk_volume_read", "Cluster")

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
        
        # There is no adaptor.
        return self.send_request(
            'StartBulkVolumeRead',
            StartBulkVolumeReadResult,
            params,
            since=6
        )

    def start_bulk_volume_write(
            self,
            volume_id,
            format,
            script=OPTIONAL,
            script_parameters=OPTIONAL,
            attributes=OPTIONAL,):
        """
        StartBulkVolumeWrite allows you to initialize a bulk volume write session on a specified volume.
        Only two bulk volume processes can run simultaneously on a volume.
        When the session is initialized, data can be written to a SolidFire storage volume from an external backup source.
        The external data is accessed by a web server running on a SolidFire node.
        Communications and server interaction information for external data access is passed by a script running on the SolidFire storage system.
        :param volumeID: [required] ID of the volume to be written to. 
        :type volumeID: int

        :param format: [required] The format of the volume data. Can be either: uncompressed: every byte of the volume is returned without any compression. native: opaque data is returned that is smaller and more efficiently stored and written on a subsequent bulk volume write 
        :type format: str

        :param script:  Executable name of a script. If no script name is given then the key and URL are necessary to access SolidFire nodes. The script runs on the primary node and the key and URL is returned to the script so the local web server can be contacted. 
        :type script: str

        :param scriptParameters:  JSON parameters to pass to the script. 
        :type scriptParameters: str

        :param attributes:  JSON attributes for the bulk volume job. 
        :type attributes: dict
        """

        self._check_connection_type("start_bulk_volume_write", "Cluster")

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
        
        # There is no adaptor.
        return self.send_request(
            'StartBulkVolumeWrite',
            StartBulkVolumeWriteResult,
            params,
            since=6
        )

    def update_bulk_volume_status(
            self,
            key,
            status,
            percent_complete=OPTIONAL,
            message=OPTIONAL,
            attributes=OPTIONAL,):
        """
        You can use UpdateBulkVolumeStatus in a script to return to the SolidFire system the status of a bulk volume job that you have started with the "StartBulkVolumeRead" or "StartBulkVolumeWrite" methods.
        :param key: [required] The key assigned during initialization of a "StartBulkVolumeRead" or "StartBulkVolumeWrite" session. 
        :type key: str

        :param status: [required] The SolidFire system sets the status of the given bulk volume job. Possible values: running: jobs that are still active. complete: jobs that are done. failed - jobs that have failed. failed: jobs that have failed. 
        :type status: str

        :param percentComplete:  The completed progress of the bulk volume job as a percentage. 
        :type percentComplete: str

        :param message:  Returns the status of the bulk volume job when the job has completed. 
        :type message: str

        :param attributes:  JSON attributes  updates what is on the bulk volume job. 
        :type attributes: dict
        """

        self._check_connection_type("update_bulk_volume_status", "Cluster")

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
        
        # There is no adaptor.
        return self.send_request(
            'UpdateBulkVolumeStatus',
            UpdateBulkVolumeStatusResult,
            params,
            since=6
        )

    def add_initiators_to_volume_access_group(
            self,
            volume_access_group_id,
            initiators,):
        """
        Add initiators to a volume access group.
        :param volumeAccessGroupID: [required] The ID of the volume access group to modify. 
        :type volumeAccessGroupID: int

        :param initiators: [required] List of initiators to add to the volume access group. 
        :type initiators: str
        """

        self._check_connection_type("add_initiators_to_volume_access_group", "Cluster")

        params = { 
            "volumeAccessGroupID": volume_access_group_id,
            "initiators": initiators,
        }
        
        # There is no adaptor.
        return self.send_request(
            'AddInitiatorsToVolumeAccessGroup',
            ModifyVolumeAccessGroupResult,
            params,
            since=5
        )

    def add_volumes_to_volume_access_group(
            self,
            volume_access_group_id,
            volumes,):
        """
        Add volumes to a volume access group.
        :param volumeAccessGroupID: [required] The ID of the volume access group to modify. 
        :type volumeAccessGroupID: int

        :param volumes: [required] List of volumes to add to this volume access group. 
        :type volumes: int
        """

        self._check_connection_type("add_volumes_to_volume_access_group", "Cluster")

        params = { 
            "volumeAccessGroupID": volume_access_group_id,
            "volumes": volumes,
        }
        
        # There is no adaptor.
        return self.send_request(
            'AddVolumesToVolumeAccessGroup',
            ModifyVolumeAccessGroupResult,
            params,
            since=5
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
        Entering initiators and volumes are optional when creating a volume access group.
        Once the group is created volumes and initiator IQNs can be added.
        Any initiator IQN that is successfully added to the volume access group is able to access any volume in the group without CHAP authentication.
        :param name: [required] Name of the volume access group. It is not required to be unique, but recommended. 
        :type name: str

        :param initiators:  List of initiators to include in the volume access group. If unspecified, the access group will start out without configured initiators. 
        :type initiators: str

        :param volumes:  List of volumes to initially include in the volume access group. If unspecified, the access group will start without any volumes. 
        :type volumes: int

        :param virtualNetworkID:  The ID of the SolidFire Virtual Network ID to associate the volume access group with. 
        :type virtualNetworkID: int

        :param virtualNetworkTags:  The ID of the VLAN Virtual Network Tag to associate the volume access group with. 
        :type virtualNetworkTags: int

        :param attributes:  List of Name/Value pairs in JSON object format. 
        :type attributes: dict
        """

        self._check_connection_type("create_volume_access_group", "Cluster")

        params = { 
            "name": name,
        }
        if initiators is not None:
            params["initiators"] = initiators
        if volumes is not None:
            params["volumes"] = volumes
        if virtual_network_id is not None:
            if self.api_version < 8.0:
                raise ApiParameterVersionError("create_volume_access_group", 8.0,
                    [("virtual_network_id", virtual_network_id, 8.0, False)])
            else:
                params["virtualNetworkID"] = virtual_network_id
        if virtual_network_tags is not None:
            if self.api_version < 8.0:
                raise ApiParameterVersionError("create_volume_access_group", 8.0,
                    [("virtual_network_tags", virtual_network_tags, 8.0, False)])
            else:
                params["virtualNetworkTags"] = virtual_network_tags
        if attributes is not None:
            params["attributes"] = attributes
        
        # There is no adaptor.
        return self.send_request(
            'CreateVolumeAccessGroup',
            CreateVolumeAccessGroupResult,
            params,
            since=5
        )

    def delete_volume_access_group(
            self,
            volume_access_group_id,):
        """
        Delete a volume access group from the system.
        :param volumeAccessGroupID: [required] The ID of the volume access group to delete. 
        :type volumeAccessGroupID: int
        """

        self._check_connection_type("delete_volume_access_group", "Cluster")

        params = { 
            "volumeAccessGroupID": volume_access_group_id,
        }
        
        # There is no adaptor.
        return self.send_request(
            'DeleteVolumeAccessGroup',
            DeleteVolumeAccessGroupResult,
            params,
            since=5
        )

    def get_volume_access_group_efficiency(
            self,
            volume_access_group_id,):
        """
        GetVolumeAccessGroupEfficiency is used to retrieve efficiency information about a volume access group. Only the volume access group provided as parameters in this API method is used to compute the capacity.
        :param volumeAccessGroupID: [required] Specifies the volume access group for which capacity is computed. 
        :type volumeAccessGroupID: int
        """

        self._check_connection_type("get_volume_access_group_efficiency", "Cluster")

        params = { 
            "volumeAccessGroupID": volume_access_group_id,
        }
        
        # There is no adaptor.
        return self.send_request(
            'GetVolumeAccessGroupEfficiency',
            GetEfficiencyResult,
            params,
            since=6
        )

    def get_volume_access_group_lun_assignments(
            self,
            volume_access_group_id,):
        """
        The GetVolumeAccessGroupLunAssignments is used to return information LUN mappings of a specified volume access group.
        :param volumeAccessGroupID: [required] Unique volume access group ID used to return information. 
        :type volumeAccessGroupID: int
        """

        self._check_connection_type("get_volume_access_group_lun_assignments", "Cluster")

        params = { 
            "volumeAccessGroupID": volume_access_group_id,
        }
        
        # There is no adaptor.
        return self.send_request(
            'GetVolumeAccessGroupLunAssignments',
            GetVolumeAccessGroupLunAssignmentsResult,
            params,
            since=7
        )

    def list_volume_access_groups(
            self,
            start_volume_access_group_id=OPTIONAL,
            limit=OPTIONAL,):
        """
        ListVolumeAccessGroups is used to return information about the volume access groups that are currently in the system.
        :param startVolumeAccessGroupID:  The lowest VolumeAccessGroupID to return. This can be useful for paging. If unspecified, there is no lower limit (implicitly 0). 
        :type startVolumeAccessGroupID: int

        :param limit:  The maximum number of results to return. This can be useful for paging. 
        :type limit: int
        """

        self._check_connection_type("list_volume_access_groups", "Cluster")

        params = { 
        }
        if start_volume_access_group_id is not None:
            params["startVolumeAccessGroupID"] = start_volume_access_group_id
        if limit is not None:
            params["limit"] = limit
        
        # There is no adaptor.
        return self.send_request(
            'ListVolumeAccessGroups',
            ListVolumeAccessGroupsResult,
            params,
            since=5
        )

    def remove_initiators_from_volume_access_group(
            self,
            volume_access_group_id,
            initiators,):
        """
        Remove initiators from a volume access group.
        :param volumeAccessGroupID: [required] The ID of the volume access group to modify. 
        :type volumeAccessGroupID: int

        :param initiators: [required] List of initiators to remove from the volume access group. 
        :type initiators: str
        """

        self._check_connection_type("remove_initiators_from_volume_access_group", "Cluster")

        params = { 
            "volumeAccessGroupID": volume_access_group_id,
            "initiators": initiators,
        }
        
        # There is no adaptor.
        return self.send_request(
            'RemoveInitiatorsFromVolumeAccessGroup',
            ModifyVolumeAccessGroupResult,
            params,
            since=5
        )

    def remove_volumes_from_volume_access_group(
            self,
            volume_access_group_id,
            volumes,):
        """
        Remove volumes from a volume access group.
        :param volumeAccessGroupID: [required] The ID of the volume access group to modify. 
        :type volumeAccessGroupID: int

        :param volumes: [required] List of volumes to remove from this volume access group. 
        :type volumes: int
        """

        self._check_connection_type("remove_volumes_from_volume_access_group", "Cluster")

        params = { 
            "volumeAccessGroupID": volume_access_group_id,
            "volumes": volumes,
        }
        
        # There is no adaptor.
        return self.send_request(
            'RemoveVolumesFromVolumeAccessGroup',
            ModifyVolumeAccessGroupResult,
            params,
            since=5
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
        A specified initiator or volume that duplicates an existing volume or initiator in a volume access group is left as-is.
        If a value is not specified for volumes or initiators, the current list of initiators and volumes are not changed.
        
        Often, it is easier to use the convenience functions to modify initiators and volumes independently:
        
        AddInitiatorsToVolumeAccessGroup
        RemoveInitiatorsFromVolumeAccessGroup
        AddVolumesToVolumeAccessGroup
        RemoveVolumesFromVolumeAccessGroup
        :param volumeAccessGroupID: [required] The ID of the volume access group to modify. 
        :type volumeAccessGroupID: int

        :param virtualNetworkID:  The ID of the SolidFire Virtual Network ID to associate the volume access group with. 
        :type virtualNetworkID: int

        :param virtualNetworkTags:  The ID of the VLAN Virtual Network Tag to associate the volume access group with. 
        :type virtualNetworkTags: int

        :param name:  Name of the volume access group. It is not required to be unique, but recommended. 
        :type name: str

        :param initiators:  List of initiators to include in the volume access group. If unspecified, the access group's configured initiators will not be modified. 
        :type initiators: str

        :param volumes:  List of volumes to initially include in the volume access group. If unspecified, the access group's volumes will not be modified. 
        :type volumes: int

        :param attributes:  List of Name/Value pairs in JSON object format. 
        :type attributes: dict
        """

        self._check_connection_type("modify_volume_access_group", "Cluster")

        params = { 
            "volumeAccessGroupID": volume_access_group_id,
        }
        if virtual_network_id is not None:
            if self.api_version < 8.0:
                raise ApiParameterVersionError("modify_volume_access_group", 8.0,
                    [("virtual_network_id", virtual_network_id, 8.0, False)])
            else:
                params["virtualNetworkID"] = virtual_network_id
        if virtual_network_tags is not None:
            if self.api_version < 8.0:
                raise ApiParameterVersionError("modify_volume_access_group", 8.0,
                    [("virtual_network_tags", virtual_network_tags, 8.0, False)])
            else:
                params["virtualNetworkTags"] = virtual_network_tags
        if name is not None:
            params["name"] = name
        if initiators is not None:
            params["initiators"] = initiators
        if volumes is not None:
            params["volumes"] = volumes
        if attributes is not None:
            params["attributes"] = attributes
        
        # There is no adaptor.
        return self.send_request(
            'ModifyVolumeAccessGroup',
            ModifyVolumeAccessGroupResult,
            params,
            since=5
        )

    def modify_volume_access_group_lun_assignments(
            self,
            volume_access_group_id,
            lun_assignments,):
        """
        The ModifytVolumeAccessGroupLunAssignments is used to define custom LUN assignments for specific volumes. Only LUN values set on the lunAssignments parameter will be changed in the volume access group. All other LUN assignments will remain unchanged.
        
        LUN assignment values must be unique for volumes in a volume access group. An exception will be seen if LUN assignments are duplicated in a volume access group. However, the same LUN values can be used again in different volume access groups.
        
        Note: Correct LUN values are 0 - 16383. An exception will be seen if an incorrect LUN value is passed. None of the specified LUN assignments will be modified if there is an exception.
        
        Caution: If a LUN assignment is changed for a volume with active I/O, the I/O could be disrupted. Changes to the server configuration may be required in order to change volume LUN assignments.
        :param volumeAccessGroupID: [required] Unique volume access group ID for which the LUN assignments will be modified. 
        :type volumeAccessGroupID: int

        :param lunAssignments: [required] The volume IDs with new assigned LUN values. 
        :type lunAssignments: LunAssignment
        """

        self._check_connection_type("modify_volume_access_group_lun_assignments", "Cluster")

        params = { 
            "volumeAccessGroupID": volume_access_group_id,
            "lunAssignments": lun_assignments,
        }
        
        # There is no adaptor.
        return self.send_request(
            'ModifyVolumeAccessGroupLunAssignments',
            ModifyVolumeAccessGroupLunAssignmentsResult,
            params,
            since=7
        )

    def get_ipmi_config(
            self,
            force,
            chassis_type=OPTIONAL,):
        """
        GetIpmiConfig enables you to retrieve hardware sensor information from sensors that are in your node.
        :param chassisType:  Used to display information for each node chassis type. Valid values:all - returns sensor information for each chassis type. {chassis type} - returns sensor information for a specified chassis type. 
        :type chassisType: str

        :param force: [required] 
        :type force: bool
        """

        self._check_connection_type("get_ipmi_config", "Cluster")

        params = { 
            "force": force,
        }
        if chassis_type is not None:
            params["chassisType"] = chassis_type
        
        # There is no adaptor.
        return self.send_request(
            'GetIpmiConfig',
            GetIpmiConfigResult,
            params,
            since=9
        )

    def get_ipmi_info(
            self,
            force,):
        """
        GetIpmiInfo allows you to display a detailed reporting of sensors (objects) for node fans, intake and exhaust temperatures, and power supplies  that are monitored by . 
        :param force: [required] 
        :type force: bool
        """

        self._check_connection_type("get_ipmi_info", "Cluster")

        params = { 
            "force": force,
        }
        
        # There is no adaptor.
        return self.send_request(
            'GetIpmiInfo',
            GetIpmiInfoResult,
            params,
            since=9
        )

    def invoke_sfapi(
            self,
            method,
            parameters=OPTIONAL,):
        """
        This will invoke any API method supported by the SolidFire API for the version and port the connection is using.
        Returns a nested hashtable of key/value pairs that contain the result of the invoked method.
        :param method: [required] The name of the method to invoke. This is case sensitive. 
        :type method: str

        :param parameters:  An object, normally a dictionary or hashtable of the key/value pairs, to be passed as the params for the method being invoked. 
        :type parameters: dict
        """

        self._check_connection_type("invoke_sfapi", "Both")

        params = { 
            "method": method,
        }
        if parameters is not None:
            params["parameters"] = parameters
        
        # There is an adaptor!
        since = 1.0
        deprecated = None

        return ElementServiceAdaptor.invoke_sfapi(self, params,
                                                  since, deprecated)

