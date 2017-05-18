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

    def add_account(
            self,
            username,
            initiator_secret=OPTIONAL,
            target_secret=OPTIONAL,
            attributes=OPTIONAL,):
        """
        You can use AddAccount to add a new account to the system. You can create new volumes under the new account. The CHAP settings you specify for the account apply to all volumes owned by the account.
        :param username: [required] Specifies the username for this account. (Might be 1 to 64 characters in length). 
        :type username: str

        :param initiatorSecret:  The CHAP secret to use for the initiator. This secret must be 12-16 characters in length and should be impenetrable. The initiator CHAP secret must be unique and cannot be the same as the target CHAP secret. If unspecified, a random secret is created. 
        :type initiatorSecret: CHAPSecret

        :param targetSecret:  The CHAP secret to use for the target (mutual CHAP authentication). This secret must be 12-16 characters in length and should be impenetrable. The target CHAP secret must be unique and cannot be the same as the initiator CHAP secret. If unspecified, a random secret is created. 
        :type targetSecret: CHAPSecret

        :param attributes:  List of name-value pairs in JSON object format. 
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
            since=1.0
        )

    def get_account_by_id(
            self,
            account_id,):
        """
        GetAccountByID enables you to return details about a specific account, given its accountID.
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
            since=1.0
        )

    def get_account_by_name(
            self,
            username,):
        """
        GetAccountByName enables you to retrieve details about a specific account, given its username.
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
            since=1.0
        )

    def get_account_efficiency(
            self,
            account_id,):
        """
        GetAccountEfficiency enables you to retrieve efficiency statistics about a volume account. This method returns efficiency information
        only for the account you specify as a parameter.
        :param accountID: [required] Specifies the volume account for which efficiency statistics are returned. 
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
            since=6.0
        )

    def list_accounts(
            self,
            start_account_id=OPTIONAL,
            limit=OPTIONAL,
            include_storage_containers=OPTIONAL,):
        """
        ListAccounts returns the entire list of accounts, with optional paging support.
        :param startAccountID:  Starting AccountID to return. If no account exists with this AccountID, the next account by AccountID order is used as the start of the list. To page through the list, pass the AccountID of the last account in the previous response + 1. 
        :type startAccountID: int

        :param limit:  Maximum number of AccountInfo objects to return. 
        :type limit: int

        :param includeStorageContainers:  Includes storage containers in the response by default. To exclude storage containers, set to false. 
        :type includeStorageContainers: bool
        """

        self._check_connection_type("list_accounts", "Cluster")

        params = { 
        }
        if start_account_id is not None:
            params["startAccountID"] = start_account_id
        if limit is not None:
            params["limit"] = limit
        if include_storage_containers is not None:
            if self.api_version < 9.0:
                raise ApiParameterVersionError("list_accounts", 9.0,
                    [("include_storage_containers", include_storage_containers, 9.0, False)])
            else:
                params["includeStorageContainers"] = include_storage_containers
        
        # There is no adaptor.
        return self.send_request(
            'ListAccounts',
            ListAccountsResult,
            params,
            since=1.0
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
        ModifyAccount enables you to modify an existing account.
        When you lock an account, any existing connections from that account are immediately terminated. When you change an account's
        CHAP settings, any existing connections remain active, and the new CHAP settings are used on subsequent connections or
        reconnections.
        To clear an account's attributes, specify {} for the attributes parameter.
        :param accountID: [required] Specifies the AccountID for the account to be modified. 
        :type accountID: int

        :param username:  Specifies the username associated with the account. (Might be 1 to 64 characters in length). 
        :type username: str

        :param status:  Sets the status for the account. Possible values are: active: The account is active and connections are allowed. locked: The account is locked and connections are refused. 
        :type status: str

        :param initiatorSecret:  Specifies the CHAP secret to use for the initiator. This secret must be 12-16 characters in length and should be impenetrable. The initiator CHAP secret must be unique and cannot be the same as the target CHAP secret. 
        :type initiatorSecret: CHAPSecret

        :param targetSecret:  Specifies the CHAP secret to use for the target (mutual CHAP authentication). This secret must be 12-16 characters in length and should be impenetrable. The target CHAP secret must be unique and cannot be the same as the initiator CHAP secret. 
        :type targetSecret: CHAPSecret

        :param attributes:  List of name-value pairs in JSON object format. 
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
            since=1.0
        )

    def remove_account(
            self,
            account_id,):
        """
        RemoveAccount enables you to remove an existing account. You must delete and purge all volumes associated with the account
        using DeleteVolume before you can remove the account. If volumes on the account are still pending deletion, you cannot use
        RemoveAccount to remove the account.
        :param accountID: [required] Specifies the AccountID for the account to be removed. 
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
            since=1.0
        )

    def get_async_result(
            self,
            async_handle,
            keep_result=OPTIONAL,):
        """
        You can use GetAsyncResult to retrieve the result of asynchronous method calls. Some method calls require some time to run, and
        might not be finished when the system sends the initial response. To obtain the status or result of the method call, use
        GetAsyncResult to poll the asyncHandle value returned by the method.
        GetAsyncResult returns the overall status of the operation (in progress, completed, or error) in a standard fashion, but the actual
        data returned for the operation depends on the original method call and the return data is documented with each method.
        :param asyncHandle: [required] A value that was returned from the original asynchronous method call. 
        :type asyncHandle: int

        :param keepResult:  If true, GetAsyncResult does not remove the asynchronous result upon returning it, enabling future queries to that asyncHandle. 
        :type keepResult: bool
        """

        self._check_connection_type("get_async_result", "Cluster")

        params = { 
            "asyncHandle": async_handle,
        }
        if keep_result is not None:
            params["keepResult"] = keep_result
        
        # There is no adaptor.
        return self.send_request(
            'GetAsyncResult',
            dict,
            params,
            since=1.0
        )

    def list_async_results(
            self,
            async_result_types=OPTIONAL,):
        """
        You can use ListAsyncResults to list the results of all currently running and completed asynchronous methods on the system.
        Querying asynchronous results with ListAsyncResults does not cause completed asyncHandles to expire; you can use GetAsyncResult
        to query any of the asyncHandles returned by ListAsyncResults.
        :param asyncResultTypes:  An optional list of types of results. You can use this list to restrict the results to only these types of operations. Possible values are: BulkVolume: Copy operations between volumes, such as backups or restores. Clone: Volume cloning operations. DriveRemoval: Operations involving the system copying data from a drive in preparation to remove it from the cluster. RtfiPendingNode: Operations involving the system installing compatible software on a node before adding it to the cluster 
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
            since=9.0
        )

    def create_backup_target(
            self,
            name,
            attributes=OPTIONAL,):
        """
        CreateBackupTarget enables you to create and store backup target information so that you do not need to re-enter it each time a backup is created.
        :param name: [required] The name of the backup target. 
        :type name: str

        :param attributes:  List of name-value pairs in JSON object format. 
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
            since=6.0
        )

    def get_backup_target(
            self,
            backup_target_id,):
        """
        GetBackupTarget enables you to return information about a specific backup target that you have created.
        :param backupTargetID: [required] The unique identifier assigned to the backup target. 
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
            since=6.0
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
            since=6.0
        )

    def modify_backup_target(
            self,
            backup_target_id,
            name=OPTIONAL,
            attributes=OPTIONAL,):
        """
        ModifyBackupTarget enables you to change attributes of a backup target.
        :param backupTargetID: [required] The unique target ID for the target to modify. 
        :type backupTargetID: int

        :param name:  The new name for the backup target. 
        :type name: str

        :param attributes:  List of name-value pairs in JSON object format. 
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
            since=6.0
        )

    def remove_backup_target(
            self,
            backup_target_id,):
        """
        RemoveBackupTarget allows you to delete backup targets.
        :param backupTargetID: [required] The unique target ID of the target to remove. 
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
            since=6.0
        )

    def clear_cluster_faults(
            self,
            fault_types=OPTIONAL,):
        """
        You can use the ClearClusterFaults method to clear information about both current and previously detected faults. Both resolved
        and unresolved faults can be cleared.
        :param faultTypes:  Determines the types of faults cleared. Possible values are: current: Faults that are currently detected and have not been resolved. resolved: (Default) Faults that were previously detected and resolved. all: Both current and resolved faults are cleared. The fault status can be determined by the resolved field of the fault object. 
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
            since=1.0
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
        The CreateCluster method enables you to initialize the node in a cluster that has ownership of the "mvip" and "svip" addresses. Each new cluster is initialized using the management IP (MIP) of the first node in the cluster. This method also automatically adds all the nodes being configured into the cluster. You only need to use this method once each time a new cluster is initialized.
        Note: You need to log in to the node that is used as the master node for the cluster. After you log in, run the GetBootstrapConfig method on the node to get the IP addresses for the rest of the nodes that you want to include in the
        cluster. Then, run the CreateCluster method.
        :param acceptEula:  Required to indicate your acceptance of the End User License Agreement when creating this cluster. To accept the EULA, set this parameter to true. 
        :type acceptEula: bool

        :param mvip: [required] Floating (virtual) IP address for the cluster on the management network. 
        :type mvip: str

        :param svip: [required] Floating (virtual) IP address for the cluster on the storage (iSCSI) network. 
        :type svip: str

        :param repCount: [required] Number of replicas of each piece of data to store in the cluster. Valid value is "2". 
        :type repCount: int

        :param username: [required] Username for the cluster admin. 
        :type username: str

        :param password: [required] Initial password for the cluster admin account. 
        :type password: str

        :param nodes: [required] CIP/SIP addresses of the initial set of nodes making up the cluster. This node's IP must be in the list. 
        :type nodes: str

        :param attributes:  List of name-value pairs in JSON object format. 
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
            params,
            since=None
        )

    def create_support_bundle(
            self,
            bundle_name=OPTIONAL,
            extra_args=OPTIONAL,
            timeout_sec=OPTIONAL,):
        """
        CreateSupportBundle enables you to create a support bundle file under the node's directory. After creation, the bundle is stored on the node as a tar.gz file.
        :param bundleName:  The unique name for the support bundle. If no name is provided, "supportbundle" and the node name are used as the filename. 
        :type bundleName: str

        :param extraArgs:  Passed to the sf_make_support_bundle script. You should use this parameter only at the request of NetApp SolidFire Support. 
        :type extraArgs: str

        :param timeoutSec:  The number of seconds to allow the support bundle script to run before stopping. The default value is 1500 seconds. 
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
            since=8.0
        )

    def delete_all_support_bundles(
            self,):
        """
        DeleteAllSupportBundles enables you to delete all support bundles generated with the CreateSupportBundle API method.        """

        self._check_connection_type("delete_all_support_bundles", "Node")

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'DeleteAllSupportBundles',
            DeleteAllSupportBundlesResult,
            params,
            since=8.0
        )

    def disable_encryption_at_rest(
            self,):
        """
        The DisableEncryptionAtRest method enables you to remove the encryption that was previously applied to the cluster using the EnableEncryptionAtRest method. This disable method is asynchronous and returns a response before encryption is disabled. You can use the GetClusterInfo method to poll the system to see when the process has completed.        """

        self._check_connection_type("disable_encryption_at_rest", "Cluster")

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'DisableEncryptionAtRest',
            DisableEncryptionAtRestResult,
            params,
            since=5.0
        )

    def enable_encryption_at_rest(
            self,):
        """
        You can use the EnableEncryptionAtRest method to enable the Advanced Encryption Standard (AES) 256-bit encryption at rest on the cluster, so that the cluster can manage the encryption key used for the drives on each node. This feature is not enabled by default.
        When you enable Encryption at Rest, the cluster automatically manages encryption keys internally for the drives on each node in the cluster. Nodes do not store the keys to unlock drives and the keys are never passed over the network. Two nodes participating in a cluster are required to access the key to disable encryption on a drive. The encryption management does not affect performance or efficiency on the cluster. If an encryption-enabled drive or node is removed from the cluster with the API, Encryption at Rest is disabled and the data is not secure erased. Data can be secure erased using the SecureEraseDrives API method.
        Note: If you have a node type with a model number ending in "-NE", the EnableEncryptionAtRest method call fails with a response of "Encryption not allowed. Cluster detected non-encryptable node".
        You should only enable or disable encryption when the cluster is running and in a healthy state. You can enable or disable encryption at your discretion and as often as you need.
        Note: This process is asynchronous and returns a response before encryption is enabled. You can use the GetClusterInfo
        method to poll the system to see when the process has completed.        """

        self._check_connection_type("enable_encryption_at_rest", "Cluster")

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'EnableEncryptionAtRest',
            EnableEncryptionAtRestResult,
            params,
            since=5.0
        )

    def get_api(
            self,):
        """
        You can use the GetAPI method to return a list of all the API methods and supported API endpoints that can be used in the system.        """

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
        You can use the GetClusterCapacity method to return the high-level capacity measurements for an entire cluster. You can use the fields returned from this method to calculate the efficiency rates that are displayed in the Element OS Web UI. You can use the following calculations in scripts to return the efficiency rates for thin provisioning, deduplication, compression, and overall efficiency.        """

        self._check_connection_type("get_cluster_capacity", "Cluster")

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'GetClusterCapacity',
            GetClusterCapacityResult,
            params,
            since=1.0
        )

    def get_cluster_config(
            self,):
        """
        The GetClusterConfig API method enables you to return information about the cluster configuration this node uses to communicate with the cluster that it is a part of.        """

        self._check_connection_type("get_cluster_config", "Node")

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'GetClusterConfig',
            GetClusterConfigResult,
            params,
            since=5.0
        )

    def get_cluster_full_threshold(
            self,):
        """
        You can use GetClusterFullThreshold to view the stages set for cluster fullness levels. This method returns all fullness metrics for the
        cluster.
        Note: When a cluster reaches the Error stage of block cluster fullness, the maximum IOPS on all volumes are reduced linearly to the volume's minimum IOPS as the cluster approaches the Critical stage. This helps prevent the cluster from
        reaching the Critical stage of block cluster fullness.        """

        self._check_connection_type("get_cluster_full_threshold", "Cluster")

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'GetClusterFullThreshold',
            GetClusterFullThresholdResult,
            params,
            since=1.0
        )

    def get_cluster_info(
            self,):
        """
        GetClusterInfo enables you to return configuration information about the cluster.        """

        self._check_connection_type("get_cluster_info", "Cluster")

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'GetClusterInfo',
            GetClusterInfoResult,
            params,
            since=1.0
        )

    def get_cluster_master_node_id(
            self,):
        """
        GetClusterMasterNodeID enables you to retrieve the ID of the node that can perform cluster-wide administration tasks and holds the
        storage virtual IP address (SVIP) and management virtual IP address (MVIP).        """

        self._check_connection_type("get_cluster_master_node_id", "Cluster")

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'GetClusterMasterNodeID',
            GetClusterMasterNodeIDResult,
            params,
            since=1.0
        )

    def get_cluster_state(
            self,
            force,):
        """
        The GetClusterState API method enables you to indicate if a node is part of a cluster or not. The three states are:
        Available: Node has not been configured with a cluster name.
        Pending: Node is pending for a specific named cluster and can be added.
        Active: Node is an active member of a cluster and may not be added to another
        cluster.
        Note: This method is available only through the per-node API endpoint 5.0 or later.
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
            since=5.0
        )

    def get_cluster_stats(
            self,):
        """
        GetClusterStats enables you to retrieve high-level activity measurements for the cluster. Values returned are cumulative from the
        creation of the cluster.        """

        self._check_connection_type("get_cluster_stats", "Cluster")

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'GetClusterStats',
            GetClusterStatsResult,
            params,
            since=1.0
        )

    def get_cluster_version_info(
            self,):
        """
        GetClusterVersionInfo enables you to retrieve information about the Element software version running on each node in the cluster.
        This method also returns information about nodes that are currently in the process of upgrading software.        """

        self._check_connection_type("get_cluster_version_info", "Cluster")

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'GetClusterVersionInfo',
            GetClusterVersionInfoResult,
            params,
            since=1.0
        )

    def get_complete_stats(
            self,):
        """
        NetApp engineering uses the GetCompleteStats API method to troubleshoot new features. The data returned from GetCompleteStats is not documented, changes frequently, and is not guaranteed to be accurate. NetApp does not recommend using GetCompleteStats for collecting performance data or any other
        management integration with a SolidFire cluster.        """

        self._check_connection_type("get_complete_stats", "Cluster")

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'GetCompleteStats',
            dict,
            params,
            since=1.0
        )

    def get_limits(
            self,):
        """
        GetLimits enables you to retrieve the limit values set by the API. These values might change between releases of Element OS, but do not change without an update to the system. Knowing the limit values set by the API can be useful when writing API scripts for user-facing tools.
        Note: The GetLimits method returns the limits for the current software version regardless of the API endpoint version used to pass the method.        """

        self._check_connection_type("get_limits", "Cluster")

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'GetLimits',
            GetLimitsResult,
            params,
            since=1.0
        )

    def get_ntp_info(
            self,):
        """
        GetNtpInfo enables you to return the current network time protocol (NTP) configuration information.        """

        self._check_connection_type("get_ntp_info", "Cluster")

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'GetNtpInfo',
            GetNtpInfoResult,
            params,
            since=1.0
        )

    def get_raw_stats(
            self,):
        """
        NetApp engineering uses the GetRawStats API method to troubleshoot new features. The data returned from GetRawStats is not documented, changes frequently, and is not guaranteed to be accurate. NetApp does not recommend using GetCompleteStats for collecting performance data or any other
        management integration with a SolidFire cluster.        """

        self._check_connection_type("get_raw_stats", "Cluster")

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'GetRawStats',
            dict,
            params,
            since=1.0
        )

    def get_system_status(
            self,):
        """
        GetSystemStatus enables you to return whether a reboot ir required or not.        """

        self._check_connection_type("get_system_status", "Node")

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'GetSystemStatus',
            GetSystemStatusResult,
            params,
            since=5.0
        )

    def list_cluster_faults(
            self,
            best_practices=OPTIONAL,
            fault_types=OPTIONAL,):
        """
        ListClusterFaults enables you to retrieve information about any faults detected on the cluster. With this method, you can retrieve both current faults as well as faults that have been resolved. The system caches faults every 30 seconds.
        :param bestPractices:  Specifies whether to include faults triggered by suboptimal system configuration. Possible values are: true false 
        :type bestPractices: bool

        :param faultTypes:  Determines the types of faults returned. Possible values are: current: List active, unresolved faults. resolved: List faults that were previously detected and resolved. all: (Default) List both current and resolved faults. You can see the fault status in the resolved field of the Cluster Fault object. 
        :type faultTypes: str
        """

        self._check_connection_type("list_cluster_faults", "Cluster")

        params = { 
        }
        if best_practices is not None:
            params["bestPractices"] = best_practices
        if fault_types is not None:
            params["faultTypes"] = fault_types
        
        # There is no adaptor.
        return self.send_request(
            'ListClusterFaults',
            ListClusterFaultsResult,
            params,
            since=1.0
        )

    def list_events(
            self,
            max_events=OPTIONAL,
            start_event_id=OPTIONAL,
            end_event_id=OPTIONAL,):
        """
        ListEvents returns events detected on the cluster, sorted from oldest to newest.
        :param maxEvents:  Specifies the maximum number of events to return. 
        :type maxEvents: int

        :param startEventID:  Identifies the beginning of a range of events to return. 
        :type startEventID: int

        :param endEventID:  Identifies the end of a range of events to return. 
        :type endEventID: int
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
        
        # There is no adaptor.
        return self.send_request(
            'ListEvents',
            ListEventsResult,
            params,
            since=1.0
        )

    def list_sync_jobs(
            self,):
        """
        ListSyncJobs enables you to return information about synchronization jobs that are running on a SolidFire cluster. The type of
        synchronization jobs that are returned with this method are slice, clone, and remote.        """

        self._check_connection_type("list_sync_jobs", "Cluster")

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'ListSyncJobs',
            ListSyncJobsResult,
            params,
            since=1.0
        )

    def modify_cluster_full_threshold(
            self,
            stage2_aware_threshold=OPTIONAL,
            stage3_block_threshold_percent=OPTIONAL,
            max_metadata_over_provision_factor=OPTIONAL,):
        """
        You can use ModifyClusterFullThreshold to change the level at which the system generates an event when the storage cluster approaches a certain capacity utilization. You can use the threshold setting to indicate the acceptable amount of utilized block storage before the system generates a warning. For example, if you want to be alerted when the system reaches 3% below the "Error" level block storage utilization, enter a value of "3" for the stage3BlockThresholdPercent parameter. If this level is reached, the system sends an alert to the Event Log in the Cluster Management Console.
        :param stage2AwareThreshold:  The number of nodes of capacity remaining in the cluster before the system triggers a capacity notification. 
        :type stage2AwareThreshold: int

        :param stage3BlockThresholdPercent:  The percentage of block storage utilization below the "Error" threshold that causes the system to trigger a cluster "Warning" alert. 
        :type stage3BlockThresholdPercent: int

        :param maxMetadataOverProvisionFactor:  A value representative of the number of times metadata space can be overprovisioned relative to the amount of space available. For example, if there was enough metadata space to store 100 TiB of volumes and this number was set to 5, then 500 TiB worth of volumes can be created. 
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
            since=1.0
        )

    def set_cluster_config(
            self,
            cluster,):
        """
        The SetClusterConfig API method enables you to set the configuration this node uses to communicate with the cluster it is associated with. To see the states in which these objects can be modified, see Cluster Object Attributes. To display the current cluster
        interface settings for a node, run the GetClusterConfig API method.
        Note: This method is available only through the per-node API endpoint 5.0 or later.
        :param cluster: [required] Objects that are changed for the cluster interface settings. 
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
            since=5.0
        )

    def set_ntp_info(
            self,
            servers,
            broadcastclient=OPTIONAL,):
        """
        SetNtpInfo enables you to configure NTP on cluster nodes. The values you set with this interface apply to all nodes in the cluster. If an NTP broadcast server periodically broadcasts time information on your network, you can optionally configure nodes as broadcast clients.
        Note: NetApp recommends using NTP servers that are internal to your network, rather than the installation defaults.
        :param servers: [required] List of NTP servers to add to each nodes NTP configuration. 
        :type servers: str

        :param broadcastclient:  Enables every node in the cluster as a broadcast client. 
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
            since=1.0
        )

    def add_cluster_admin(
            self,
            username,
            password,
            access,
            accept_eula=OPTIONAL,
            attributes=OPTIONAL,):
        """
        You can use AddClusterAdmin to add a new cluster admin account. A cluster ddmin can manage the cluster using the API and management tools. Cluster admins are completely separate and unrelated to standard tenant accounts.
        Each cluster admin can be restricted to a subset of the API. NetApp recommends using multiple cluster admin accounts for different users and applications. You should give each cluster admin the minimal permissions necessary; this reduces the potential impact of credential compromise.
        You must accept the End User License Agreement (EULA) by setting the acceptEula parameter to true to add a cluster administrator account to the system.
        :param username: [required] Unique username for this cluster admin. Must be between 1 and 1024 characters in length. 
        :type username: str

        :param password: [required] Password used to authenticate this cluster admin. 
        :type password: str

        :param access: [required] Controls which methods this cluster admin can use. For more details on the levels of access, see Access Control in the Element API Reference Guide. 
        :type access: str

        :param acceptEula:  Required to indicate your acceptance of the End User License Agreement when creating this cluster. To accept the EULA, set this parameter to true. 
        :type acceptEula: bool

        :param attributes:  List of name-value pairs in JSON object format. 
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
            since=1.0
        )

    def get_current_cluster_admin(
            self,):
        """
        GetCurrentClusterAdmin returns information for the current primary cluster administrator. The primary Cluster Admin was created when the cluster was created.        """

        self._check_connection_type("get_current_cluster_admin", "Cluster")

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'GetCurrentClusterAdmin',
            GetCurrentClusterAdminResult,
            params,
            since=6.0
        )

    def list_cluster_admins(
            self,):
        """
        ListClusterAdmins returns the list of all cluster administrators for the cluster. There can be several cluster administrator accounts with different levels of permissions. There can be only one primary cluster administrator in the system. The primary Cluster Admin is the administrator that was created when the cluster was created. You can also create LDAP administrators when setting up an LDAP system on the cluster.        """

        self._check_connection_type("list_cluster_admins", "Cluster")

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'ListClusterAdmins',
            ListClusterAdminsResult,
            params,
            since=1.0
        )

    def modify_cluster_admin(
            self,
            cluster_admin_id,
            password=OPTIONAL,
            access=OPTIONAL,
            attributes=OPTIONAL,):
        """
        You can use ModifyClusterAdmin to change the settings for a cluster admin or LDAP cluster admin. You cannot change access for the administrator cluster admin account.
        :param clusterAdminID: [required] ClusterAdminID for the cluster admin or LDAP cluster admin to modify. 
        :type clusterAdminID: int

        :param password:  Password used to authenticate this cluster admin. 
        :type password: str

        :param access:  Controls which methods this cluster admin can use. For more details, see Access Control in the Element API Reference Guide. 
        :type access: str

        :param attributes:  List of name-value pairs in JSON object format. 
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
            since=1.0
        )

    def remove_cluster_admin(
            self,
            cluster_admin_id,):
        """
        You can use RemoveClusterAdmin to remove a Cluster Admin. You cannot remove the administrator cluster admin account.
        :param clusterAdminID: [required] ClusterAdminID for the cluster admin to remove. 
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
            since=1.0
        )

    def add_drives(
            self,
            drives,
            force_during_upgrade=OPTIONAL,):
        """
        AddDrives enables you to add one or more available drives to the cluster, enabling the drives to host a portion of the cluster's data.
        When you add a node to the cluster or install new drives in an existing node, the new drives are marked as "available" and must be
        added via AddDrives before they can be utilized. Use the ListDrives method to display drives that are "available" to be added. When
        you add multiple drives, it is more efficient to add them in a single AddDrives method call rather than multiple individual methods
        with a single drive each. This reduces the amount of data balancing that must occur to stabilize the storage load on the cluster.
        When you add a drive, the system automatically determines the "type" of drive it should be.
        The method is asynchronous and returns immediately. However, it can take some time for the data in the cluster to be rebalanced
        using the newly added drives. As the new drives are syncing on the system, you can use the ListSyncJobs method to see how the
        drives are being rebalanced and the progress of adding the new drive. You can also use the GetAsyncResult method to query the
        method's returned asyncHandle.
        :param drives: [required] Returns information about each drive to be added to the cluster. Possible values are: driveID: The ID of the drive to add. (Integer) type: (Optional) The type of drive to add. Valid values are "slice" or "block". If omitted, the system assigns the correct type. (String) 
        :type drives: NewDrive

        :param forceDuringUpgrade:  Allows the user to force the addition of drives during an upgrade. 
        :type forceDuringUpgrade: bool
        """

        self._check_connection_type("add_drives", "Cluster")

        params = { 
            "drives": drives,
        }
        if force_during_upgrade is not None:
            params["forceDuringUpgrade"] = force_during_upgrade
        
        # There is no adaptor.
        return self.send_request(
            'AddDrives',
            AddDrivesResult,
            params,
            since=1.0
        )

    def get_drive_config(
            self,):
        """
        GetDriveConfig enables you to display drive information for expected slice and block drive counts as well as the number of slices
        and block drives that are currently connected to the node.
        Note: This method is available only through the per-node API endpoint 5.0 or later.        """

        self._check_connection_type("get_drive_config", "Node")

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'GetDriveConfig',
            GetDriveConfigResult,
            params,
            since=2.0
        )

    def get_drive_hardware_info(
            self,
            drive_id,):
        """
        GetDriveHardwareInfo returns all the hardware information for the given drive. This generally includes details about manufacturers, vendors, versions, and
        other associated hardware identification information.
        :param driveID: [required] DriveID for the drive information requested. You can get DriveIDs by using the ListDrives method. 
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
            since=1.0
        )

    def get_drive_stats(
            self,
            drive_id,):
        """
        GetDriveStats returns high-level activity measurements for a single drive. Values are cumulative from the addition of the drive to the
        cluster. Some values are specific to block drives. You might not obtain statistical data for both block and metadata drives when you
        run this method. 
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
            since=1.0
        )

    def list_drive_hardware(
            self,
            force,):
        """
        ListDriveHardware returns all the drives connected to a node. Use this method on individual nodes to return drive hardware
        information or use this method on the cluster master node MVIP to see information for all the drives on all nodes.
        Note: The "securitySupported": true line of the method response does not imply that the drives are capable of
        encryption; only that the security status can be queried. If you have a node type with a model number ending in "-NE",
        commands to enable security features on these drives will fail. See the EnableEncryptionAtRest method for more information.
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
            since=7.0
        )

    def list_drives(
            self,):
        """
        ListDrives enables you to retrieve the list of the drives that exist in the cluster's active nodes. This method returns drives that have
        been added as volume metadata or block drives as well as drives that have not been added and are available.        """

        self._check_connection_type("list_drives", "Cluster")

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'ListDrives',
            ListDrivesResult,
            params,
            since=1.0
        )

    def list_drive_stats(
            self,
            drives=OPTIONAL,):
        """
        ListDriveStats enables you to retrieve high-level activity measurements for multiple drives in the cluster. By default, this method returns statistics for all drives in the cluster, and these measurements are cumulative from the addition of the drive to the cluster. Some values this method returns are specific to block drives, and some are specific to metadata drives.
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
            since=9.0
        )

    def remove_drives(
            self,
            drives,
            force_during_upgrade=OPTIONAL,):
        """
        You can use RemoveDrives to proactively remove drives that are part of the cluster. You might want to use this method when
        reducing cluster capacity or preparing to replace drives nearing the end of their service life. Any data on the drives is removed and
        migrated to other drives in the cluster before the drive is removed from the cluster. This is an asynchronous method. Depending on
        the total capacity of the drives being removed, it might take several minutes to migrate all of the data. Use the GetAsyncResult
        method to check the status of the remove operation.
        When removing multiple drives, use a single RemoveDrives method call rather than multiple individual methods with a single drive
        each. This reduces the amount of data balancing that must occur to even stabilize the storage load on the cluster.
        You can also remove drives with a "failed" status using RemoveDrives. When you remove a drive with a "failed" status it is not
        returned to an "available" or active status. The drive is unavailable for use in the cluster.
        Use the ListDrives method to obtain the driveIDs for the drives you want to remove.
        :param drives: [required] List of driveIDs to remove from the cluster. 
        :type drives: int

        :param forceDuringUpgrade:  If you want to remove a drive during upgrade, this must be set to true. 
        :type forceDuringUpgrade: bool
        """

        self._check_connection_type("remove_drives", "Cluster")

        params = { 
            "drives": drives,
        }
        if force_during_upgrade is not None:
            params["forceDuringUpgrade"] = force_during_upgrade
        
        # There is no adaptor.
        return self.send_request(
            'RemoveDrives',
            AsyncHandleResult,
            params,
            since=1.0
        )

    def reset_drives(
            self,
            drives,
            force,):
        """
        ResetDrives enables you to proactively initialize drives and remove all data currently residing on a drive. The drive can then be reused
        in an existing node or used in an upgraded node. This method requires the force parameter to be included in the method call.
        :param drives: [required] List of device names (not driveIDs) to reset. 
        :type drives: str

        :param force: [required] Required parameter to successfully reset a drive. 
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
            since=6.0
        )

    def secure_erase_drives(
            self,
            drives,):
        """
        SecureEraseDrives enables you to remove any residual data from drives that have a status of "available." You might want to use this method when replacing a drive nearing the end of its service life that contained sensitive data. This method uses a Security Erase Unit command to write a predetermined pattern to the drive and resets the encryption key on the drive. This asynchronous method might take up to two minutes to complete. You can use GetAsyncResult to check on the status of the secure erase operation.
        You can use the ListDrives method to obtain the driveIDs for the drives you want to secure erase.
        :param drives: [required] List of driveIDs to be secure erased. 
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
            since=5.0
        )

    def test_drives(
            self,
            minutes=OPTIONAL,
            force=OPTIONAL,):
        """
        You can use the TestDrives API method to run a hardware validation on all drives on the node. This method detects hardware
        failures on the drives (if present) and reports them in the results of the validation tests.
        You can only use the TestDrives method on nodes that are not "active" in a cluster.
        Note: This test takes approximately 10 minutes.
        Note: This method is available only through the per-node API endpoint 5.0 or later.
        :param minutes:  Specifies the number of minutes to run the test. 
        :type minutes: int

        :param force:  Required parameter to successfully test the drives on the node. 
        :type force: bool
        """

        self._check_connection_type("test_drives", "Node")

        params = { 
        }
        if minutes is not None:
            params["minutes"] = minutes
        if force is not None:
            params["force"] = force
        
        # There is no adaptor.
        return self.send_request(
            'TestDrives',
            TestDrivesResult,
            params,
            since=5.0
        )

    def get_cluster_hardware_info(
            self,
            type=OPTIONAL,):
        """
        You can use the GetClusterHardwareInfo method to retrieve the hardware status and information for all Fibre Channel nodes, iSCSI
        nodes and drives in the cluster. This generally includes details about manufacturers, vendors, versions, and other associated hardware
        identification information.
        :param type:  Includes only a certain type of hardware information in the response. Possible values are: drives: List only drive information in the response. nodes: List only node information in the response. all: Include both drive and node information in the response. If this parameter is omitted, a type of "all" is assumed. 
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
            since=1.0
        )

    def get_hardware_config(
            self,):
        """
        GetHardwareConfig enables you to display the hardware configuration information for a node.
        Note: This method is available only through the per-node API endpoint 5.0 or later.        """

        self._check_connection_type("get_hardware_config", "Node")

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'GetHardwareConfig',
            GetHardwareConfigResult,
            params,
            since=5.0
        )

    def get_hardware_info(
            self,):
        """
        The GetHardwareInfo API method enables you to return hardware information and status for a single node. This generally includes details about manufacturers, vendors, versions, drives, and other associated hardware identification information.        """

        self._check_connection_type("get_hardware_info", "Node")

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'GetHardwareInfo',
            GetHardwareInfoResult,
            params,
            since=9.0
        )

    def get_node_hardware_info(
            self,
            node_id,):
        """
        GetNodeHardwareInfo enables you to return all the hardware information and status for the node specified. This generally includes details about
        manufacturers, vendors, versions, and other associated hardware identification information.
        :param nodeID: [required] The ID of the node for which hardware information is being requested. Information about a Fibre Channel node is returned if a Fibre Channel node is specified. 
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
            since=1.0
        )

    def get_nvram_info(
            self,
            force=OPTIONAL,):
        """
        GetNvramInfo enables you to retrieve information from each node about the NVRAM card.
        :param force:  Required parameter to successfully run on all nodes in the cluster. 
        :type force: bool
        """

        self._check_connection_type("get_nvram_info", "Node")

        params = { 
        }
        if force is not None:
            params["force"] = force
        
        # There is no adaptor.
        return self.send_request(
            'GetNvramInfo',
            GetNvramInfoResult,
            params,
            since=5.0
        )

    def add_initiators_to_volume_access_group(
            self,
            volume_access_group_id,
            initiators,):
        """
        AddInitiatorsToVolumeAccessGroup enables you
        to add initiators to a specified volume access group.
        :param volumeAccessGroupID: [required] The ID of the volume access group to modify. 
        :type volumeAccessGroupID: int

        :param initiators: [required] The list of initiators to add to the volume access group. 
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
            since=5.0
        )

    def create_initiators(
            self,
            initiators,):
        """
        CreateInitiators enables you to create multiple new initiator IQNs or World Wide Port Names (WWPNs) and optionally assign them
        aliases and attributes. When you use CreateInitiators to create new initiators, you can also add them to volume access groups.
        If CreateInitiators fails to create one of the initiators provided in the parameter, the method returns an error and does not create
        any initiators (no partial completion is possible).
        :param initiators: [required] A list of objects containing characteristics of each new initiator. Values are: name: (Required) The name of the initiator (IQN or WWPN) to create. (String) alias: (Optional) The friendly name to assign to this initiator. (String) attributes: (Optional) A set of JSON attributes to assign to this initiator. (JSON Object) volumeAccessGroupID: (Optional) The ID of the volume access group into to which this newly created initiator will be added. (Integer) 
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
            since=9.0
        )

    def delete_initiators(
            self,
            initiators,):
        """
        DeleteInitiators enables you to delete one or more initiators from the system (and from any associated volumes or volume access
        groups).
        If DeleteInitiators fails to delete one of the initiators provided in the parameter, the system returns an error and does not delete any
        initiators (no partial completion is possible).
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
            since=9.0
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

        :param initiators:  A list of initiator IDs to retrieve. You can provide a value for this parameter or the "startInitiatorID" parameter, but not both. 
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
            since=9.0
        )

    def modify_initiators(
            self,
            initiators,):
        """
        ModifyInitiators enables you to change the attributes of one or more existing initiators. You cannot change the name of an existing
        initiator. If you need to change the name of an initiator, delete it first with DeleteInitiators and create a new one with
        CreateInitiators.
        If ModifyInitiators fails to change one of the initiators provided in the parameter, the method returns an error and does not modify
        any initiators (no partial completion is possible).
        :param initiators: [required] A list of objects containing characteristics of each initiator to modify. Values are: initiatorID: (Required) The ID of the initiator to modify. (Integer) alias: (Optional) A new friendly name to assign to the initiator. (String) attributes: (Optional) A new set of JSON attributes to assign to the initiator. (JSON Object) volumeAccessGroupID: (Optional) The ID of the volume access group into to which the initiator should be added. If the initiator was previously in a different volume access group, it is removed from the old volume access group. If this key is present but null, the initiator is removed from its current volume access group, but not placed in any new volume access group. (Integer) 
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
            since=9.0
        )

    def remove_initiators_from_volume_access_group(
            self,
            volume_access_group_id,
            initiators,
            delete_orphan_initiators=OPTIONAL,):
        """
        RemoveInitiatorsFromVolumeAccessGroup enables
        you to remove initiators from a specified volume access
        group.
        :param volumeAccessGroupID: [required] The ID of the volume access group from which the initiators are removed. 
        :type volumeAccessGroupID: int

        :param initiators: [required] The list of initiators to remove from the volume access group. 
        :type initiators: str

        :param deleteOrphanInitiators:  true: Delete initiator objects after they are removed from a volume access group. false: Do not delete initiator objects after they are removed from a volume access group. 
        :type deleteOrphanInitiators: bool
        """

        self._check_connection_type("remove_initiators_from_volume_access_group", "Cluster")

        params = { 
            "volumeAccessGroupID": volume_access_group_id,
            "initiators": initiators,
        }
        if delete_orphan_initiators is not None:
            params["deleteOrphanInitiators"] = delete_orphan_initiators
        
        # There is no adaptor.
        return self.send_request(
            'RemoveInitiatorsFromVolumeAccessGroup',
            ModifyVolumeAccessGroupResult,
            params,
            since=5.0
        )

    def add_ldap_cluster_admin(
            self,
            username,
            access,
            accept_eula=OPTIONAL,
            attributes=OPTIONAL,):
        """
        AddLdapClusterAdmin enables you to add a new LDAP cluster administrator user. An LDAP cluster administrator can manage the
        cluster via the API and management tools. LDAP cluster admin accounts are completely separate and unrelated to standard tenant
        accounts.
        You can also use this method to add an LDAP group that has been defined in Active Directory. The access level that is given to the group is passed to the individual users in the LDAP group.
        :param username: [required] The distinguished user name for the new LDAP cluster admin. 
        :type username: str

        :param access: [required] Controls which methods this Cluster Admin can use. For more details on the levels of access, see the Access Control appendix in the SolidFire API Reference. 
        :type access: str

        :param acceptEula:  Accept the End User License Agreement. Set to true to add a cluster administrator account to the system. If omitted or set to false, the method call fails. 
        :type acceptEula: bool

        :param attributes:  List of name-value pairs in JSON object format. 
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
            since=8.0
        )

    def disable_ldap_authentication(
            self,):
        """
        The DisableLdapAuthentication method enables you to disable LDAP authentication and remove all LDAP configuration settings. This method does not remove any configured cluster admin accounts (user or group). However, those cluster admin accounts will no longer be able to log in.        """

        self._check_connection_type("disable_ldap_authentication", "Cluster")

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'DisableLdapAuthentication',
            DisableLdapAuthenticationResult,
            params,
            since=7.0
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
        The EnableLdapAuthentication method enables you to configure an LDAP directory connection to use for LDAP authentication to a cluster. Users that are members of the LDAP directory can then log in to the storage system using their LDAP credentials.
        :param authType:  Identifies which user authentication method to use. Must be one of the following: DirectBind SearchAndBind 
        :type authType: str

        :param groupSearchBaseDN:  The base DN of the tree to start the group search (will do a subtree search from here). 
        :type groupSearchBaseDN: str

        :param groupSearchCustomFilter:  For use with the CustomFilter search type, an LDAP filter to use to return the DNs of a users groups. The string can have placeholder text of %USERNAME% and %USERDN% to be replaced with their username and full userDN as needed. 
        :type groupSearchCustomFilter: str

        :param groupSearchType:  Controls the default group search filter used, and must be one of the following: NoGroups: No group support. ActiveDirectory: Nested membership of all of a users AD groups. MemberDN: MemberDN style groups (single level). 
        :type groupSearchType: str

        :param searchBindDN:  A fully qualified DN to log in with to perform an LDAP search for the user (needs read access to the LDAP directory). 
        :type searchBindDN: str

        :param searchBindPassword:  The password for the searchBindDN account used for searching. 
        :type searchBindPassword: str

        :param serverURIs: [required] A comma-separated list of LDAP server URIs (examples: "ldap://1.2.3.4" and ldaps://1.2.3.4:123") 
        :type serverURIs: str

        :param userDNTemplate:  A string that is used to form a fully qualified user DN. The string should have the placeholder text %USERNAME%, which is replaced with the username of the authenticating user. 
        :type userDNTemplate: str

        :param userSearchBaseDN:  The base DN of the tree to start the search (will do a subtree search from here). 
        :type userSearchBaseDN: str

        :param userSearchFilter:  The LDAP filter to use. The string should have the placeholder text %USERNAME% which is replaced with the username of the authenticating user. Example: (&(objectClass=person)(sAMAccountName=%USERNAME%)) will use the sAMAccountName field in Active Directory to match the username entered at cluster login. 
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
            since=7.0
        )

    def get_ldap_configuration(
            self,):
        """
        The GetLdapConfiguration method enables you to get the currently active LDAP configuration on the cluster.        """

        self._check_connection_type("get_ldap_configuration", "Cluster")

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'GetLdapConfiguration',
            GetLdapConfigurationResult,
            params,
            since=7.0
        )

    def test_ldap_authentication(
            self,
            username,
            password,
            ldap_configuration=OPTIONAL,):
        """
        The TestLdapAuthentication method enables you to validate the currently enabled LDAP authentication settings. If the configuration is
        correct, the API call returns the group membership of the tested user.
        :param username: [required] The username to be tested. 
        :type username: str

        :param password: [required] The password for the username to be tested. 
        :type password: str

        :param ldapConfiguration:  An ldapConfiguration object to be tested. If specified, the API call tests the provided configuration even if LDAP authentication is disabled. 
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
            since=7.0
        )

    def get_login_session_info(
            self,):
        """
        GetLoginSessionInfo enables you to return the period of time a log in authentication session is valid for both log in shells and the TUI.        """

        self._check_connection_type("get_login_session_info", "Cluster")

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'GetLoginSessionInfo',
            GetLoginSessionInfoResult,
            params,
            since=7.0
        )

    def get_remote_logging_hosts(
            self,):
        """
        GetRemoteLoggingHosts enables you to retrieve the current list of log servers.        """

        self._check_connection_type("get_remote_logging_hosts", "Cluster")

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'GetRemoteLoggingHosts',
            GetRemoteLoggingHostsResult,
            params,
            since=1.0
        )

    def set_login_session_info(
            self,
            timeout,):
        """
        You can use SetLoginSessionInfo to set the period of time that a session's login authentication is valid. After the log in period elapses without activity on the system, the authentication expires. New login credentials are required for continued access to the cluster after the timeout period has elapsed.
        :param timeout: [required] Cluster authentication expiration period. Formatted in HH:mm:ss. For example, 01:30:00, 00:90:00, and 00:00:5400 can be used to equal a 90 minute timeout period. The default value is 30 minutes. 
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
            since=7.0
        )

    def set_remote_logging_hosts(
            self,
            remote_hosts,):
        """
        SetRemoteLoggingHosts enables you to configure remote logging from the nodes in the storage cluster to a centralized log server or servers. Remote logging is performed over TCP using the default port 514. This API does not add to the existing logging hosts. Rather, it replaces what currently exists with new values specified by this API method. You can use GetRemoteLoggingHosts to determine what the current logging hosts are, and then use SetRemoteLoggingHosts to set the desired list of current and new logging hosts.
        :param remoteHosts: [required] A list of hosts to send log messages to. 
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
            since=1.0
        )

    def list_fibre_channel_port_info(
            self,):
        """
        ListFibreChannelPortInfo enables you to retrieve information about the Fibre Channel ports on a node.  The API method is intended for use on individual nodes; userid and password authentication is required for access to individual Fibre Channel nodes.        """

        self._check_connection_type("list_fibre_channel_port_info", "Cluster")

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'ListFibreChannelPortInfo',
            ListFibreChannelPortInfoResult,
            params,
            since=8.0
        )

    def list_fibre_channel_sessions(
            self,):
        """
        ListFibreChannelSessions enables you to retrieve information about the active Fibre Channel sessions on a cluster.         """

        self._check_connection_type("list_fibre_channel_sessions", "Cluster")

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'ListFibreChannelSessions',
            ListFibreChannelSessionsResult,
            params,
            since=7.0
        )

    def list_iscsisessions(
            self,):
        """
        You can use ListISCSISessions to return iSCSI information for volumes in the cluster.        """

        self._check_connection_type("list_iscsisessions", "Cluster")

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'ListISCSISessions',
            ListISCSISessionsResult,
            params,
            since=1.0
        )

    def list_network_interfaces(
            self,):
        """
        ListNetworkInterfaces enables you to retrieve information about each network interface on a node. The API method is intended for use on individual nodes; userid and password authentication is required for access to individual nodes.        """

        self._check_connection_type("list_network_interfaces", "Node")

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'ListNetworkInterfaces',
            ListNetworkInterfacesResult,
            params,
            since=7.0
        )

    def list_node_fibre_channel_port_info(
            self,):
        """
        The ListNodeFibreChannelPortInfo API method enables you to retrieve information about the Fibre Channel ports on a node. The API method is intended for use on individual nodes; userid and password authentication is required for access to individual Fibre Channel nodes.        """

        self._check_connection_type("list_node_fibre_channel_port_info", "Node")

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'ListNodeFibreChannelPortInfo',
            ListNodeFibreChannelPortInfoResult,
            params,
            since=7.0
        )

    def add_nodes(
            self,
            pending_nodes,
            auto_install=OPTIONAL,):
        """
        AddNodes enables you to add one or more new nodes to a cluster. When a node that is not configured starts up for the first time, you are prompted to configure the node. After you configure the node, it is registered as a "pending node" with the cluster. 
        Note: It might take several seconds after adding a new node for it to start up and register its drives as available.
        :param pendingNodes: [required]  List of pending NodeIDs for the nodes to be added. You can  obtain the list of pending nodes using the ListPendingNodes method. 
        :type pendingNodes: int

        :param autoInstall:  Whether these nodes should be autoinstalled 
        :type autoInstall: bool
        """

        self._check_connection_type("add_nodes", "Cluster")

        params = { 
            "pendingNodes": pending_nodes,
        }
        if auto_install is not None:
            params["autoInstall"] = auto_install
        
        # There is no adaptor.
        return self.send_request(
            'AddNodes',
            AddNodesResult,
            params,
            since=1.0
        )

    def get_bootstrap_config(
            self,):
        """
        GetBootstrapConfig returns cluster and node information from the bootstrap configuration file. Use this API method on an individual node before it has been joined with a cluster. You can use the information this method returns in the cluster configuration interface when you create a cluster.        """

        self._check_connection_type("get_bootstrap_config", "Both")

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'GetBootstrapConfig',
            GetBootstrapConfigResult,
            params,
            since=2.0
        )

    def get_config(
            self,):
        """
        The GetConfig API method enables you to retrieve all configuration information for a node. This method includes the same information available in both the GetClusterConfig and GetNetworkConfig API methods.
        Note: This method is available only through the per-node API endpoint 5.0 or later.        """

        self._check_connection_type("get_config", "Node")

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'GetConfig',
            GetConfigResult,
            params,
            since=5.0
        )

    def get_network_config(
            self,):
        """
        The GetNetworkConfig API method enables you to display the network configuration information for a node.
        Note: This method is available only through the per-node API endpoint 5.0 or later.        """

        self._check_connection_type("get_network_config", "Node")

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'GetNetworkConfig',
            GetNetworkConfigResult,
            params,
            since=5.0
        )

    def get_node_stats(
            self,
            node_id,):
        """
        GetNodeStats enables you to retrieve the high-level activity measurements for a single node.
        :param nodeID: [required] Specifies the node for which statistics are gathered. 
        :type nodeID: int
        """

        self._check_connection_type("get_node_stats", "Cluster")

        params = { 
            "nodeID": node_id,
        }
        
        # There is an adaptor!
        since = 1.0
        deprecated = None

        return ElementServiceAdaptor.get_node_stats(self, params,
                                                  since, deprecated)

    def get_origin(
            self,):
        """
        GetOrigin enables you to retrieve the origination certificate for where the node was built. This method might return null if there is no origination certification.        """

        self._check_connection_type("get_origin", "Cluster")

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'GetOrigin',
            GetOriginResult,
            params,
            since=9.0
        )

    def get_pending_operation(
            self,):
        """
        You can use GetPendingOperation to detect an operation on a node that is currently in progress. You can also use this method to report back when an operation has completed. 
        Note: method is available only through the per-node API endpoint 5.0 or later.        """

        self._check_connection_type("get_pending_operation", "Node")

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'GetPendingOperation',
            GetPendingOperationResult,
            params,
            since=5.0
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
            since=1.0
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
            since=1.0
        )

    def list_node_stats(
            self,):
        """
        ListNodeStats enables you to view the high-level activity measurements for all nodes in a cluster.        """

        self._check_connection_type("list_node_stats", "Cluster")

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'ListNodeStats',
            ListNodeStatsResult,
            params,
            since=6.0
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
            since=9.0
        )

    def list_pending_nodes(
            self,):
        """
        ListPendingNodes returns a list of the currently pending nodes in the system. Pending nodes are nodes that are running and configured to join the cluster, but have not yet been added via the AddNodes API method.        """

        self._check_connection_type("list_pending_nodes", "Cluster")

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'ListPendingNodes',
            ListPendingNodesResult,
            params,
            since=1.0
        )

    def remove_nodes(
            self,
            nodes,):
        """
        You can use RemoveNodes to remove one or more nodes that should no longer participate in the cluster. Before removing a node, you must remove all drives the node contains using the RemoveDrives method. You cannot remove a node until the RemoveDrives process has completed and all data has been migrated away from the node.
        After you remove a node, it registers itself as a pending node. You can add the node again or shut it down (shutting the node down removes it from the Pending Node list).
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
            since=1.0
        )

    def set_config(
            self,
            config,):
        """
        The SetConfig API method enables you to set all the configuration information for the node. This includes the same information available via calls to SetClusterConfig and SetNetworkConfig in one API method. 
        Note: This method is available only through the per-node API endpoint 5.0 or later.
        Caution: Changing the "bond-mode" on a node can cause a temporary loss of network connectivity. Exercise caution when using this method.
        :param config: [required] Objects that you want changed for the cluster interface settings. 
        :type config: ConfigParams
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
            since=5.0
        )

    def set_network_config(
            self,
            network,):
        """
        The SetNetworkConfig API method enables you to set the network configuration for a node. To display the current network settings for a node, run the GetNetworkConfig API method. 
        Note: This method is available only through the per-node API endpoint 5.0 or later.
        Changing the "bond-mode" on a node can cause a temporary loss of network connectivity. Exercise caution when using this method.
        :param network: [required] An object containing node network settings to modify. 
        :type network: NetworkParams
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
            since=5.0
        )

    def complete_cluster_pairing(
            self,
            cluster_pairing_key,):
        """
        You can use the CompleteClusterPairing method with the encoded key received from the  StartClusterPairing method to complete the cluster pairing process. The CompleteClusterPairing method is the second step in the cluster pairing process. 
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
            since=6.0
        )

    def complete_volume_pairing(
            self,
            volume_pairing_key,
            volume_id,):
        """
        You can use the CompleteVolumePairing method to complete the pairing of two volumes.
        :param volumePairingKey: [required] The key returned from the StartVolumePairing method. 
        :type volumePairingKey: str

        :param volumeID: [required] The ID of the volume on which to complete the pairing process. 
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
            since=6.0
        )

    def list_active_paired_volumes(
            self,
            start_volume_id=OPTIONAL,
            limit=OPTIONAL,):
        """
        ListActivePairedVolumes enables you to list all the active volumes paired with a volume. This method returns information about volumes with active and pending pairings.
        :param startVolumeID:  The beginning of the range of active paired volumes to return. 
        :type startVolumeID: int

        :param limit:  Maximum number of active paired volumes to return. 
        :type limit: int
        """

        self._check_connection_type("list_active_paired_volumes", "Cluster")

        params = { 
        }
        if start_volume_id is not None:
            params["startVolumeID"] = start_volume_id
        if limit is not None:
            params["limit"] = limit
        
        # There is no adaptor.
        return self.send_request(
            'ListActivePairedVolumes',
            ListActivePairedVolumesResult,
            params,
            since=6.0
        )

    def list_cluster_pairs(
            self,):
        """
        You can use the ListClusterPairs method to list all the clusters that a cluster is paired with. This method returns information about active and pending cluster pairings, such as statistics about the current pairing as well as the connectivity and latency (in milliseconds) of the cluster pairing.        """

        self._check_connection_type("list_cluster_pairs", "Cluster")

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'ListClusterPairs',
            ListClusterPairsResult,
            params,
            since=6.0
        )

    def modify_volume_pair(
            self,
            volume_id,
            paused_manual=OPTIONAL,
            mode=OPTIONAL,
            pause_limit=OPTIONAL,):
        """
        ModifyVolumePair enables you to pause or restart replication between a pair of volumes.
        :param volumeID: [required] The ID of the volume to be modified. 
        :type volumeID: int

        :param pausedManual:  Specifies whether to pause or restart volume replication process. Valid values are:  true: Pauses volume replication false: Restarts volume replication 
        :type pausedManual: bool

        :param mode:  Specifies the volume replication mode. Possible values are: Async: Writes are acknowledged when they complete locally. The cluster does not wait for writes to be replicated to the target cluster. Sync: The source acknowledges the write when the data is stored locally and on the remote cluster. SnapshotsOnly: Only snapshots created on the source cluster are replicated. Active writes from the source volume are not replicated. 
        :type mode: str

        :param pauseLimit:  Internal use only. 
        :type pauseLimit: int
        """

        self._check_connection_type("modify_volume_pair", "Cluster")

        params = { 
            "volumeID": volume_id,
        }
        if paused_manual is not None:
            params["pausedManual"] = paused_manual
        if mode is not None:
            params["mode"] = mode
        if pause_limit is not None:
            params["pauseLimit"] = pause_limit
        
        # There is no adaptor.
        return self.send_request(
            'ModifyVolumePair',
            ModifyVolumePairResult,
            params,
            since=6.0
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
            since=6.0
        )

    def remove_volume_pair(
            self,
            volume_id,):
        """
        RemoveVolumePair enables you to remove the remote pairing between two volumes. Use this method on both the source and target volumes that are paired together. When you remove the volume pairing information, data is no longer replicated to or from the volume.
        :param volumeID: [required] The ID of the volume on which to stop the replication process. 
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
            since=6.0
        )

    def start_cluster_pairing(
            self,):
        """
        You can use the StartClusterPairing method to create an encoded key from a cluster that is used to pair with another cluster. The key created from this API method is used in the CompleteClusterPairing API method to establish a cluster pairing. You can pair a cluster with a maximum of four other clusters.         """

        self._check_connection_type("start_cluster_pairing", "Cluster")

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'StartClusterPairing',
            StartClusterPairingResult,
            params,
            since=6.0
        )

    def start_volume_pairing(
            self,
            volume_id,
            mode=OPTIONAL,):
        """
        StartVolumePairing enables you to create an encoded key from a volume that is used to pair with another volume. The key that this
        method creates is used in the CompleteVolumePairing API method to establish a volume pairing.
        :param volumeID: [required] The ID of the volume on which to start the pairing process. 
        :type volumeID: int

        :param mode:  The mode of the volume on which to start the pairing process. The mode can only be set if the volume is the source volume. Possible values are: Async: (default if no mode parameter specified) Writes are acknowledged when they complete locally. The cluster does not wait for writes to be replicated to the target cluster. Sync: Source acknowledges write when the data is stored locally and on the remote cluster. SnapshotsOnly: Only snapshots created on the source cluster will be replicated. Active writes from the source volume are not replicated. 
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
            since=6.0
        )

    def reset_node(
            self,
            build,
            force,):
        """
        The ResetNode API method enables you to reset a node to the factory settings. All data, packages (software upgrades, and so on),
        configurations, and log files are deleted from the node when you call this method. However, network settings for the node are
        preserved during this operation. Nodes that are participating in a cluster cannot be reset to the factory settings.
        The ResetNode API can only be used on nodes that are in an "Available" state. It cannot be used on nodes that are "Active" in a
        cluster, or in a "Pending" state.
        Caution: This method clears any data that is on the node. Exercise caution when using this method.
        Note: This method is available only through the per-node API endpoint 5.0 or later.
        :param build: [required] Specifies the URL to a remote Element software image to which the node will be reset. 
        :type build: str

        :param force: [required] Required parameter to successfully reset the node. 
        :type force: bool
        """

        self._check_connection_type("reset_node", "Node")

        params = { 
            "build": build,
            "force": force,
        }
        
        # There is no adaptor.
        return self.send_request(
            'ResetNode',
            ResetNodeResult,
            params,
            since=5.0
        )

    def restart_networking(
            self,
            force,):
        """
        The RestartNetworking API method enables you to restart the networking services on a node.
        Warning: This method restarts all networking services on a node, causing temporary loss of networking connectivity.
        Exercise caution when using this method.
        Note: This method is available only through the per-node API endpoint 5.0 or later.
        :param force: [required] Required parameter to successfully reset the node. 
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
            since=5.0
        )

    def shutdown(
            self,
            nodes,
            option=OPTIONAL,):
        """
        The Shutdown API method enables you to restart or shutdown a node that has not yet been added to a cluster. To use this method,
        log in to the MIP for the pending node, and enter the "shutdown" method with either the "restart" or "halt" options.
        :param nodes: [required] List of NodeIDs for the nodes to be shutdown. 
        :type nodes: int

        :param option:  Specifies the action to take for the node shutdown. Possible values are: restart: Restarts the node. halt: Shuts down the node. 
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
            since=1.0
        )

    def create_schedule(
            self,
            schedule,):
        """
        CreateSchedule enables you to schedule an automatic snapshot of a volume at a defined interval.
        You can use the created snapshot later as a backup or rollback to ensure the data on a volume or group of volumes is consistent for
        the point in time in which the snapshot was created.
        If you schedule a snapshot to run at a time period that is not divisible by 5 minutes, the snapshot runs at the next time period
        that is divisible by 5 minutes. For example, if you schedule a snapshot to run at 12:42:00 UTC, it runs at 12:45:00 UTC.
        Note: You can create snapshots if cluster fullness is at stage 1, 2 or 3. You cannot create snapshots after cluster fullness reaches stage 4 or 5.
        :param schedule: [required] The "Schedule" object will be used to create a new schedule. Do not set ScheduleID property, it will be ignored. Frequency property must be of type that inherits from Frequency. Valid types are: DaysOfMonthFrequency DaysOrWeekFrequency TimeIntervalFrequency 
        :type schedule: Schedule
        """

        self._check_connection_type("create_schedule", "Cluster")

        params = { 
            "schedule": schedule,
        }
        
        # There is an adaptor!
        since = 8.0
        deprecated = None

        return ElementServiceAdaptor.create_schedule(self, params,
                                                  since, deprecated)

    def get_schedule(
            self,
            schedule_id,):
        """
        You can use the GetSchedule method to retrieve information about a scheduled snapshot. You can see information about a specific
        schedule if there are many snapshot schedules in the system. You also retrieve information about more than one schedule with this
        method by specifying additional scheduleIDs in the parameter.
        :param scheduleID: [required] Specifies the unique ID of the schedule or multiple schedules to display. 
        :type scheduleID: int
        """

        self._check_connection_type("get_schedule", "Cluster")

        params = { 
            "scheduleID": schedule_id,
        }
        
        # There is an adaptor!
        since = 8.0
        deprecated = None

        return ElementServiceAdaptor.get_schedule(self, params,
                                                  since, deprecated)

    def list_schedules(
            self,):
        """
        ListSchedule enables you to retrieve information about all scheduled snapshots that have been created.        """

        self._check_connection_type("list_schedules", "Cluster")

        params = { 
        }
        
        # There is an adaptor!
        since = 8.0
        deprecated = None

        return ElementServiceAdaptor.list_schedules(self, params,
                                                  since, deprecated)

    def modify_schedule(
            self,
            schedule,):
        """
        ModifySchedule enables you to change the intervals at which a scheduled snapshot occurs. This allows for adjustment to the snapshot frequency and retention.
        :param schedule: [required] The "Schedule" object will be used to modify an existing schedule. The ScheduleID property is required. Frequency property must be of type that inherits from Frequency. Valid types are: DaysOfMonthFrequency DaysOrWeekFrequency TimeIntervalFrequency 
        :type schedule: Schedule
        """

        self._check_connection_type("modify_schedule", "Cluster")

        params = { 
            "schedule": schedule,
        }
        
        # There is an adaptor!
        since = 8.0
        deprecated = None

        return ElementServiceAdaptor.modify_schedule(self, params,
                                                  since, deprecated)

    def get_ipmi_config(
            self,
            chassis_type=OPTIONAL,):
        """
        GetIpmiConfig enables you to retrieve hardware sensor information from sensors that are in your node.
        :param chassisType:  Displays information for each node chassis type. Valid values are: all: Returns sensor information for each chassis type. {chassis type}: Returns sensor information for a specified chassis type. 
        :type chassisType: str
        """

        self._check_connection_type("get_ipmi_config", "Cluster")

        params = { 
        }
        if chassis_type is not None:
            params["chassisType"] = chassis_type
        
        # There is no adaptor.
        return self.send_request(
            'GetIpmiConfig',
            GetIpmiConfigResult,
            params,
            since=9.0
        )

    def get_ipmi_info(
            self,):
        """
        GetIpmiInfo enables you to display a detailed reporting of sensors (objects) for node fans, intake and exhaust temperatures, and power supplies that are monitored by the system.        """

        self._check_connection_type("get_ipmi_info", "Cluster")

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'GetIpmiInfo',
            GetIpmiInfoResult,
            params,
            since=9.0
        )

    def list_services(
            self,):
        """
        You can use ListServices to return the services information for nodes, drives, current software, and other services that are running on the cluster.        """

        self._check_connection_type("list_services", "Cluster")

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'ListServices',
            ListServicesResult,
            params,
            since=1.0
        )

    def restart_services(
            self,
            force,
            service=OPTIONAL,
            action=OPTIONAL,):
        """
        The RestartServices API method enables you to restart the services on a node.
        Caution: This method causes temporary node services interruption. Exercise caution when using this method.
        Note: This method is available only through the per-node API endpoint 5.0 or later.
        :param force: [required] Required parameter to successfully restart services on a node. 
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
            since=5.0
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
        :type parameters: str
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

    def create_group_snapshot(
            self,
            volumes,
            name=OPTIONAL,
            enable_remote_replication=OPTIONAL,
            retention=OPTIONAL,
            attributes=OPTIONAL,):
        """
        CreateGroupSnapshot enables you to create a point-in-time copy of a group of volumes. You can use this snapshot later as a backup or rollback to ensure the data on the group of volumes is consistent for the point in time that you created the snapshot.
        Note: Creating a group snapshot is allowed if cluster fullness is at stage 2 or 3. Snapshots are not created when cluster fullness is at stage 4 or 5.
        :param volumes: [required] Unique ID of the volume image from which to copy. 
        :type volumes: int

        :param name:  Name for the group snapshot. If unspecified, the date and time the group snapshot was taken is used. 
        :type name: str

        :param enableRemoteReplication:  Replicates the snapshot created to remote storage. Possible values are: true: The snapshot is replicated to remote storage. false: Default. The snapshot is not replicated. 
        :type enableRemoteReplication: bool

        :param retention:  Specifies the amount of time for which the snapshots are retained. The format is HH:mm:ss. 
        :type retention: str

        :param attributes:  List of name-value pairs in JSON object format. 
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
            since=7.0
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
        CreateSnapshot enables you to create a point-in-time copy of a volume. You can create a snapshot from any volume or from an existing snapshot. If you do not provide a SnapshotID with this API method, a snapshot is created from the volume's active branch.
        If the volume from which the snapshot is created is being replicated to a remote cluster, the snapshot can also be replicated to the same target. Use the enableRemoteReplication parameter to enable snapshot replication.
        Note: Creating a snapshot is allowed if cluster fullness is at stage 2 or 3. Snapshots are not created when cluster fullness is at stage 4 or 5.
        :param volumeID: [required] Specifies the unique ID of the volume image from which to copy. 
        :type volumeID: int

        :param snapshotID:  Specifies the unique ID of a snapshot from which the new snapshot is made. The snapshotID passed must be a snapshot on the given volume. 
        :type snapshotID: int

        :param name:  Specifies a name for the snapshot. If unspecified, the date and time the snapshot was taken is used. 
        :type name: str

        :param enableRemoteReplication:  Replicates the snapshot created to a remote cluster. Possible values are: true: The snapshot is replicated to remote storage. false: Default. The snapshot is not replicated. 
        :type enableRemoteReplication: bool

        :param retention:  Specifies the amount of time for which the snapshot is retained. The format is HH:mm:ss. 
        :type retention: str

        :param attributes:  List of name-value pairs in JSON object format. 
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
            since=6.0
        )

    def delete_group_snapshot(
            self,
            group_snapshot_id,
            save_members,):
        """
        DeleteGroupSnapshot enables you to delete a group snapshot. You can use the saveMembers parameter to preserve all the snapshots that were made for the volumes in the group, but the group association is removed.
        :param groupSnapshotID: [required] Specifies the unique ID of the group snapshot. 
        :type groupSnapshotID: int

        :param saveMembers: [required] Specifies whether to preserve snapshots or delete them. Valid values are: true: Snapshots are preserved, but group association is removed. false: The group and snapshots are deleted. 
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
            since=7.0
        )

    def delete_snapshot(
            self,
            snapshot_id,):
        """
        DeleteSnapshot enables you to delete a snapshot. A snapshot that is currently the "active" snapshot cannot be deleted. You must
        rollback and make another snapshot "active" before the current snapshot can be deleted. For more details on rolling back snapshots, see RollbackToSnapshot.
        :param snapshotID: [required] The ID of the snapshot to be deleted. 
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
            since=6.0
        )

    def list_group_snapshots(
            self,
            volumes=OPTIONAL,
            group_snapshot_id=OPTIONAL,):
        """
        ListGroupSnapshots enables you to get information about all group snapshots that have been created.
        :param volumes:  An array of unique volume IDs to query. If you do not specify this parameter, all group snapshots on the cluster are included. 
        :type volumes: int

        :param groupSnapshotID:  Retrieves information for a specific group snapshot ID. 
        :type groupSnapshotID: int
        """

        self._check_connection_type("list_group_snapshots", "Cluster")

        params = { 
        }
        if volumes is not None:
            params["volumes"] = volumes
        if group_snapshot_id is not None:
            if self.api_version < 9.0:
                raise ApiParameterVersionError("list_group_snapshots", 9.0,
                    [("group_snapshot_id", group_snapshot_id, 9.0, False)])
            else:
                params["groupSnapshotID"] = group_snapshot_id
        
        # There is no adaptor.
        return self.send_request(
            'ListGroupSnapshots',
            ListGroupSnapshotsResult,
            params,
            since=7.0
        )

    def list_snapshots(
            self,
            volume_id=OPTIONAL,
            snapshot_id=OPTIONAL,):
        """
        ListSnapshots enables you to return the attributes of each snapshot taken on the volume. Information about snapshots that reside on the target cluster is displayed on the source cluster when this method is called from the source cluster.
        :param volumeID:  Retrieves snapshots for a volume. If volumeID is not provided, all snapshots for all volumes are returned. 
        :type volumeID: int

        :param snapshotID:  Retrieves information for a specific snapshot ID. 
        :type snapshotID: int
        """

        self._check_connection_type("list_snapshots", "Cluster")

        params = { 
        }
        if volume_id is not None:
            params["volumeID"] = volume_id
        if snapshot_id is not None:
            params["snapshotID"] = snapshot_id
        
        # There is no adaptor.
        return self.send_request(
            'ListSnapshots',
            ListSnapshotsResult,
            params,
            since=6.0
        )

    def modify_group_snapshot(
            self,
            group_snapshot_id,
            expiration_time=OPTIONAL,
            enable_remote_replication=OPTIONAL,):
        """
        ModifyGroupSnapshot enables you to change the attributes of a group of snapshots. You can also use this method to enable snapshots created on the Read/Write (source) volume to be remotely replicated to a target SolidFire storage system.
        :param groupSnapshotID: [required] Specifies the ID of the group of snapshots. 
        :type groupSnapshotID: int

        :param expirationTime:  Sets the time when the snapshot should be removed. If unspecified, the current time is used. 
        :type expirationTime: str

        :param enableRemoteReplication:  Replicates the snapshot created to a remote cluster. Possible values are: true: The snapshot is replicated to remote storage. false: Default. The snapshot is not replicated. 
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
            since=8.0
        )

    def modify_snapshot(
            self,
            snapshot_id,
            expiration_time=OPTIONAL,
            enable_remote_replication=OPTIONAL,):
        """
        ModifySnapshot enables you to change the attributes currently assigned to a snapshot. You can use this method to enable snapshots created on
        the Read/Write (source) volume to be remotely replicated to a target SolidFire storage system.
        :param snapshotID: [required] Specifies the ID of the snapshot. 
        :type snapshotID: int

        :param expirationTime:  Sets the time when the snapshot should be removed. 
        :type expirationTime: str

        :param enableRemoteReplication:  Replicates the snapshot created to a remote cluster. Possible values are: true: The snapshot is replicated to remote storage. false: Default. The snapshot is not replicated. 
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
            since=8.0
        )

    def rollback_to_group_snapshot(
            self,
            group_snapshot_id,
            save_current_state,
            name=OPTIONAL,
            attributes=OPTIONAL,):
        """
        RollbackToGroupSnapshot enables you to roll back all individual volumes in a snapshot group to each volume's individual snapshot.
        Note: Rolling back to a group snapshot creates a temporary snapshot of each volume within the group snapshot.
        Snapshots are allowed if cluster fullness is at stage 2 or 3. Snapshots are not created when cluster fullness is at stage 4 or 5.
        :param groupSnapshotID: [required] Specifies the unique ID of the group snapshot. 
        :type groupSnapshotID: int

        :param saveCurrentState: [required] Specifies whether to save an active volume image or delete it. Values are: true: The previous active volume image is kept. false: (default) The previous active volume image is deleted. 
        :type saveCurrentState: bool

        :param name:  Name for the group snapshot of the volume's current state that is created if "saveCurrentState" is set to true. If you do not give a name, the name of the snapshots (group and individual volume) are set to a timestamp of the time that the rollback occurred. 
        :type name: str

        :param attributes:  List of name-value pairs in JSON object format. 
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
            RollbackToGroupSnapshotResult,
            params,
            since=7.0
        )

    def rollback_to_snapshot(
            self,
            volume_id,
            snapshot_id,
            save_current_state,
            name=OPTIONAL,
            attributes=OPTIONAL,):
        """
        RollbackToSnapshot enables you to make an existing snapshot of the "active" volume image. This method creates a new snapshot
        from an existing snapshot. The new snapshot becomes "active" and the existing snapshot is preserved until you delete it.
        The previously "active" snapshot is deleted unless you set the parameter saveCurrentState to true.
        Note: Creating a snapshot is allowed if cluster fullness is at stage 2 or 3. Snapshots are not created when cluster fullness is
        at stage 4 or 5.
        :param volumeID: [required] VolumeID for the volume. 
        :type volumeID: int

        :param snapshotID: [required] The ID of a previously created snapshot on the given volume. 
        :type snapshotID: int

        :param saveCurrentState: [required] Specifies whether to save an active volume image or delete it. Values are: true: The previous active volume image is kept. false: (default) The previous active volume image is deleted. 
        :type saveCurrentState: bool

        :param name:  Name for the snapshot. If unspecified, the name of the snapshot being rolled back to is used with "- copy" appended to the end of the name. 
        :type name: str

        :param attributes:  List of name-value pairs in JSON object format. 
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
            RollbackToSnapshotResult,
            params,
            since=6.0
        )

    def disable_snmp(
            self,):
        """
        You can use DisableSnmp to disable SNMP on the cluster nodes.        """

        self._check_connection_type("disable_snmp", "Cluster")

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'DisableSnmp',
            DisableSnmpResult,
            params,
            since=8.0
        )

    def enable_snmp(
            self,
            snmp_v3_enabled,):
        """
        EnableSnmp enables you to enable SNMP on cluster nodes. When you enable SNMP, the action applies to all nodes in the cluster, and
        the values that are passed replace, in whole, all values set in any previous call to EnableSnmp.
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
            since=8.0
        )

    def get_snmp_acl(
            self,):
        """
        GetSnmpACL enables you to return the current SNMP access permissions on the cluster nodes.        """

        self._check_connection_type("get_snmp_acl", "Cluster")

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'GetSnmpACL',
            GetSnmpACLResult,
            params,
            since=8.0
        )

    def get_snmp_info(
            self,):
        """
        GetSnmpInfo enables you to retrieve the current simple network management protocol (SNMP) configuration information.
        Note: GetSnmpInfo is available for Element OS 8 and prior releases. It is deprecated for versions later than Element OS 8.
        NetApp recommends that you migrate to the GetSnmpState and SetSnmpACL methods. See details in the Element API Reference Guide
        for their descriptions and usage.        """

        self._check_connection_type("get_snmp_info", "Cluster")

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'GetSnmpInfo',
            GetSnmpInfoResult,
            params,
            since=1.0
        )

    def get_snmp_state(
            self,):
        """
        You can use GetSnmpState to return the current state of the SNMP feature.        """

        self._check_connection_type("get_snmp_state", "Cluster")

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'GetSnmpState',
            GetSnmpStateResult,
            params,
            since=8.0
        )

    def get_snmp_trap_info(
            self,):
        """
        You can use GetSnmpTrapInfo to return current SNMP trap configuration information.        """

        self._check_connection_type("get_snmp_trap_info", "Cluster")

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'GetSnmpTrapInfo',
            GetSnmpTrapInfoResult,
            params,
            since=5.0
        )

    def set_snmp_acl(
            self,
            networks,
            usm_users,):
        """
        SetSnmpACL enables you to configure SNMP access permissions on the cluster nodes. The values you set with this interface apply to all
        nodes in the cluster, and the values that are passed replace, in whole, all values set in any previous call to SetSnmpACL. Also note
        that the values set with this interface replace all network or usmUsers values set with the older SetSnmpInfo.
        :param networks: [required] List of networks and what type of access they have to the SNMP servers running on the cluster nodes. See SNMP Network Object for possible "networks" values. This parameter is required if SNMP v3 is disabled. 
        :type networks: SnmpNetwork

        :param usmUsers: [required] List of users and the type of access they have to the SNMP servers running on the cluster nodes. 
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
            since=8.0
        )

    def set_snmp_info(
            self,
            networks=OPTIONAL,
            enabled=OPTIONAL,
            snmp_v3_enabled=OPTIONAL,
            usm_users=OPTIONAL,):
        """
        SetSnmpInfo enables you to configure SNMP version 2 and version 3 on cluster nodes. The values you set with this interface apply to
        all nodes in the cluster, and the values that are passed replace, in whole, all values set in any previous call to SetSnmpInfo.
        Note: SetSnmpInfo is deprecated. Use the EnableSnmp and SetSnmpACL methods instead.
        :param networks:  List of networks and what type of access they have to the SNMP servers running on the cluster nodes. See the SNMP Network Object for possible "networks" values. This parameter is required only for SNMP v2. 
        :type networks: SnmpNetwork

        :param enabled:  If set to true, SNMP is enabled on each node in the cluster. 
        :type enabled: bool

        :param snmpV3Enabled:  If set to true, SNMP v3 is enabled on each node in the cluster. 
        :type snmpV3Enabled: bool

        :param usmUsers:  If SNMP v3 is enabled, this value must be passed in place of the networks parameter. This parameter is required only for SNMP v3. 
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
            since=1.0
        )

    def set_snmp_trap_info(
            self,
            trap_recipients,
            cluster_fault_traps_enabled,
            cluster_fault_resolved_traps_enabled,
            cluster_event_traps_enabled,):
        """
        You can use SetSnmpTrapInfo to enable and disable the generation of cluster SNMP notifications (traps) and to specify the set of network host computers that receive the notifications. The values you pass with each SetSnmpTrapInfo method call replace all values set in any previous call to SetSnmpTrapInfo.
        :param trapRecipients: [required] List of hosts that are to receive the traps generated by the Cluster Master. At least one object is required if any one of the trap types is enabled. 
        :type trapRecipients: SnmpTrapRecipient

        :param clusterFaultTrapsEnabled: [required] If the value is set to true, a corresponding solidFireClusterFaultNotification is sent to the configured list of trap recipients when a cluster fault is logged. The default value is false. 
        :type clusterFaultTrapsEnabled: bool

        :param clusterFaultResolvedTrapsEnabled: [required] If the value is set to true, a corresponding solidFireClusterFaultResolvedNotification is sent to the configured list of trap recipients when a cluster fault is resolved. The default value is false. 
        :type clusterFaultResolvedTrapsEnabled: bool

        :param clusterEventTrapsEnabled: [required] If the value is set to true, a corresponding solidFireClusterEventNotification is sent to the configured list of trap recipients when a cluster event is logged. The default value is false. 
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
            since=5.0
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
            since=6.0
        )

    def create_storage_container(
            self,
            name,
            initiator_secret=OPTIONAL,
            target_secret=OPTIONAL,
            account_id=OPTIONAL,):
        """
        CreateStorageContainer enables you to create a Virtual Volume (VVol) storage container. Storage containers are associated with a SolidFire storage system account, and are used for reporting and resource allocation. Storage containers can only be associated with virtual volumes. You need at least one storage container to use the Virtual Volumes feature.
        :param name: [required] The name of the storage container. Follows SolidFire account naming restrictions. 
        :type name: str

        :param initiatorSecret:  The secret for CHAP authentication for the initiator. 
        :type initiatorSecret: str

        :param targetSecret:  The secret for CHAP authentication for the target. 
        :type targetSecret: str

        :param accountID:  Non-storage container account that will become a storage container. 
        :type accountID: int
        """

        self._check_connection_type("create_storage_container", "Cluster")

        params = { 
            "name": name,
        }
        if initiator_secret is not None:
            params["initiatorSecret"] = initiator_secret
        if target_secret is not None:
            params["targetSecret"] = target_secret
        if account_id is not None:
            params["accountID"] = account_id
        
        # There is no adaptor.
        return self.send_request(
            'CreateStorageContainer',
            CreateStorageContainerResult,
            params,
            since=9.0
        )

    def delete_storage_containers(
            self,
            storage_container_ids,):
        """
        DeleteStorageContainers enables you to remove up to 2000 Virtual Volume (VVol) storage containers from the system at one time.
        The storage containers you remove must not contain any VVols.
        :param storageContainerIDs: [required] A list of IDs of the storage containers to delete. You can specify up to 2000 IDs in the list. 
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
            since=9.0
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
            since=9.0
        )

    def list_storage_containers(
            self,
            storage_container_ids=OPTIONAL,):
        """
        ListStorageContainers enables you to retrieve information about all virtual volume storage containers known to the system.
        :param storageContainerIDs:  A list of storage container IDs for which to retrieve information. If you omit this parameter, the method returns information about all storage containers in the system. 
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
            since=9.0
        )

    def modify_storage_container(
            self,
            storage_container_id,
            initiator_secret=OPTIONAL,
            target_secret=OPTIONAL,):
        """
        ModifyStorageContainer enables you to make changes to an existing virtual volume storage container.
        :param storageContainerID: [required] The unique ID of the virtual volume storage container to modify. 
        :type storageContainerID: UUID

        :param initiatorSecret:  The new secret for CHAP authentication for the initiator. 
        :type initiatorSecret: str

        :param targetSecret:  The new secret for CHAP authentication for the target. 
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
            since=9.0
        )

    def list_tests(
            self,):
        """
        You can use the ListTests API method to return the tests that are available to run on a node.
        Note: This method is available only through the per-node API endpoint 5.0 or later.        """

        self._check_connection_type("list_tests", "Node")

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'ListTests',
            ListTestsResult,
            params,
            since=5.0
        )

    def list_utilities(
            self,):
        """
        You can use the ListUtilities API method to return the operations that are available to run on a node. 
        Note: This method is available only through the per-node API endpoint 5.0 or later.        """

        self._check_connection_type("list_utilities", "Node")

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'ListUtilities',
            ListUtilitiesResult,
            params,
            since=5.0
        )

    def test_connect_ensemble(
            self,
            ensemble=OPTIONAL,):
        """
        The TestConnectEnsemble API method enables you to verify connectivity with a specified database ensemble. By default, it uses the ensemble for the cluster that the node is associated with. Alternatively, you can provide a different ensemble to test connectivity with.
        Note: This method is available only through the per-node API endpoint 5.0 or later.
        :param ensemble:  Uses a comma-separated list of ensemble node cluster IP addresses to test connectivity. This parameter is optional. 
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
            since=5.0
        )

    def test_connect_mvip(
            self,
            mvip=OPTIONAL,):
        """
        The TestConnectMvip API method enables you to test the
        management connection to the cluster. The test pings the MVIP and executes a simple API method to verify connectivity.
        Note: This method is available only through the per-node API endpoint 5.0 or later.
        :param mvip:  If specified, tests the management connection of a different MVIP. You do not need to use this value when testing the connection to the target cluster. This parameter is optional. 
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
            since=5.0
        )

    def test_connect_svip(
            self,
            svip=OPTIONAL,):
        """
        The TestConnectSvip API method enables you to test the storage connection to the cluster. The test pings the SVIP using ICMP packets, and when successful, connects as an iSCSI initiator.
        Note: This method is available only through the per-node API endpoint 5.0 or later.
        :param svip:  If specified, tests the storage connection of a different SVIP. You do not need to use this value when testing the connection to the target cluster. This parameter is optional. 
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
            since=5.0
        )

    def test_ping(
            self,
            attempts=OPTIONAL,
            hosts=OPTIONAL,
            total_timeout_sec=OPTIONAL,
            packet_size=OPTIONAL,
            ping_timeout_msec=OPTIONAL,
            prohibit_fragmentation=OPTIONAL,):
        """
        You can use the TestPing API method to validate the
        connection to all the nodes in a cluster on both 1G and 10G interfaces by using ICMP packets. The test uses the appropriate MTU sizes for each packet based on the MTU settings in the network configuration.
        Note: This method is available only through the per-node API endpoint 5.0 or later.
        :param attempts:  Specifies the number of times the system should repeat the test ping. The default value is 5. 
        :type attempts: int

        :param hosts:  Specifies a comma-separated list of addresses or hostnames of devices to ping. 
        :type hosts: str

        :param totalTimeoutSec:  Specifies the length of time the ping should wait for a system response before issuing the next ping attempt or ending the process. 
        :type totalTimeoutSec: int

        :param packetSize:  Specifies the number of bytes to send in the ICMP packet that is sent to each IP. The number must be less than the maximum MTU specified in the network configuration. 
        :type packetSize: int

        :param pingTimeoutMsec:  Specifies the number of milliseconds to wait for each individual ping response. The default value is 500 ms. 
        :type pingTimeoutMsec: int

        :param prohibitFragmentation:  Specifies that the Do not Fragment (DF) flag is enabled for the ICMP packets. 
        :type prohibitFragmentation: bool
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
        if prohibit_fragmentation is not None:
            params["prohibitFragmentation"] = prohibit_fragmentation
        
        # There is no adaptor.
        return self.send_request(
            'TestPing',
            TestPingResult,
            params,
            since=5.0
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
        You can use the AddVirtualNetwork method to add a new virtual network to a cluster configuration. When you add a virtual network,
        an interface for each node is created and each interface will require a virtual network IP address. The number of IP addresses you
        specify as a parameter for this API method must be equal to or greater than the number of nodes in the cluster. The system bulk
        provisions virtual network addresses and assigns them to individual nodes automatically. You do not need to assign virtual
        network addresses to nodes manually.
        Note: You can use AddVirtualNetwork only to create a new virtual network. If you want to make changes to an
        existing virtual network, use ModifyVirtualNetwork.
        Note: Virtual network parameters must be unique to each virtual network when setting the namespace parameter to false.
        :param virtualNetworkTag: [required] A unique virtual network (VLAN) tag. Supported values are 1 through 4094.The number zero (0) is not supported. 
        :type virtualNetworkTag: int

        :param name: [required] A user-defined name for the new virtual network. 
        :type name: str

        :param addressBlocks: [required] Unique range of IP addresses to include in the virtual network. Attributes for this parameter are: start: The start of the IP address range. (String) size: The number of IP addresses to include in the block. (Integer) 
        :type addressBlocks: AddressBlockParams

        :param netmask: [required] Unique network mask for the virtual network being created. 
        :type netmask: str

        :param svip: [required] Unique storage IP address for the virtual network being created. 
        :type svip: str

        :param gateway:  The IP address of a gateway of the virtual network. This parameter is only valid if the "namespace" parameter is set to true. 
        :type gateway: str

        :param namespace:  When set to true, enables the Routable Storage VLANs functionality by creating and configuring a namespace and the virtual network contained by it. 
        :type namespace: bool

        :param attributes:  List of name-value pairs in JSON object format. 
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
            since=7.0
        )

    def list_virtual_networks(
            self,
            virtual_network_id=OPTIONAL,
            virtual_network_tag=OPTIONAL,
            virtual_network_ids=OPTIONAL,
            virtual_network_tags=OPTIONAL,):
        """
        ListVirtualNetworks enables you to list all configured virtual networks for the cluster. You can use this method to verify the virtual
        network settings in the cluster.
        There are no required parameters for this method. However, to filter the results, you can pass one or more VirtualNetworkID or
        VirtualNetworkTag values.
        :param virtualNetworkID:  Network ID to filter the list for a single virtual network. 
        :type virtualNetworkID: int

        :param virtualNetworkTag:  Network tag to filter the list for a single virtual network. 
        :type virtualNetworkTag: int

        :param virtualNetworkIDs:  Network IDs to include in the list. 
        :type virtualNetworkIDs: int

        :param virtualNetworkTags:  Network tag to include in the list. 
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
            since=7.0
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
        You can use ModifyVirtualNetwork to change the attributes of an existing virtual network. This method enables you to add or remove
        address blocks, change the netmask, or modify the name or description of the virtual network. You can also use it to enable or
        disable namespaces, as well as add or remove a gateway if namespaces are enabled on the virtual network.
        Note: This method requires either the VirtualNetworkID or the VirtualNetworkTag as a parameter, but not both.
        Caution: Enabling or disabling the Routable Storage VLANs functionality for an existing virtual network by changing the
        "namespace" parameter disrupts any traffic handled by the virtual network. NetApp strongly recommends changing the
        "namespace" parameter only during a scheduled maintenance window.
        :param virtualNetworkID:  The unique identifier of the virtual network to modify. This is the virtual network ID assigned by the cluster.  Note: This parameter is optional but either virtualNetworkID or virtualNetworkTag must be specified with this API method. 
        :type virtualNetworkID: int

        :param virtualNetworkTag:  The network tag that identifies the virtual network to modify. Note: This parameter is optional but either virtualNetworkID or virtualNetworkTag must be specified with this API method. 
        :type virtualNetworkTag: int

        :param name:  The new name for the virtual network. 
        :type name: str

        :param addressBlocks:  The new addressBlock to set for this virtual network. This might contain new address blocks to add to the existing object or omit unused address blocks that need to be removed. Alternatively, you can extend or reduce the size of existing address blocks. You can only increase the size of the starting addressBlocks for a virtual network object; you can never decrease it. Attributes for this parameter are: start: The start of the IP address range. (String) size: The number of IP addresses to include in the block. (Integer) 
        :type addressBlocks: AddressBlockParams

        :param netmask:  New network mask for this virtual network. 
        :type netmask: str

        :param svip:  The storage virtual IP address for this virtual network. The svip for a virtual network cannot be changed. You must create a new virtual network to use a different svip address. 
        :type svip: str

        :param gateway:  The IP address of a gateway of the virtual network. This parameter is only valid if the "namespace" parameter is set to true. 
        :type gateway: str

        :param namespace:  When set to true, enables Routable Storage VLANs functionality by recreating the virtual network and configuring a namespace to contain it. When set to false, disables the VRF functionality for the virtual network. Changing this value disrupts traffic running through this virtual network. 
        :type namespace: bool

        :param attributes:  A new list of name-value pairs in JSON object format. 
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
            since=7.0
        )

    def remove_virtual_network(
            self,
            virtual_network_id=OPTIONAL,
            virtual_network_tag=OPTIONAL,):
        """
        RemoveVirtualNetwork enables you to remove a previously added virtual network.
        Note: This method requires either the virtualNetworkID or the virtualNetworkTag as a parameter, but not both.
        :param virtualNetworkID:  Network ID that identifies the virtual network to remove. 
        :type virtualNetworkID: int

        :param virtualNetworkTag:  Network tag that identifies the virtual network to remove. 
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
            since=7.0
        )

    def enable_feature(
            self,
            feature,):
        """
        You can use EnableFeature to enable cluster features that are disabled by default.
        :param feature: [required] Indicates which feature to enable. Valid value is: vvols: Enable the NetApp SolidFire VVols cluster feature. 
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
            since=9.0
        )

    def get_feature_status(
            self,
            feature=OPTIONAL,):
        """
        GetFeatureStatus enables you to retrieve the status of a cluster feature.
        :param feature:  Specifies the feature for which the status is returned. Valid value is: vvols: Retrieve status for the NetApp SolidFire VVols cluster feature. 
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
            since=9.0
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
            since=9.0
        )

    def list_protocol_endpoints(
            self,
            protocol_endpoint_ids=OPTIONAL,):
        """
        ListProtocolEndpoints enables you to retrieve information about all protocol endpoints in the cluster. Protocol endpoints govern
        access to their associated virtual volume storage containers.
        :param protocolEndpointIDs:  A list of protocol endpoint IDs for which to retrieve information. If you omit this parameter, the method returns information about all protocol endpoints. 
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
            since=9.0
        )

    def list_virtual_volume_bindings(
            self,
            virtual_volume_binding_ids=OPTIONAL,):
        """
        ListVirtualVolumeBindings returns a list of all virtual volumes in the cluster that are bound to protocol endpoints.
        :param virtualVolumeBindingIDs:  A list of virtual volume binding IDs for which to retrieve information. If you omit this parameter, the method returns information about all virtual volume bindings. 
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
            since=9.0
        )

    def list_virtual_volume_hosts(
            self,
            virtual_volume_host_ids=OPTIONAL,):
        """
        ListVirtualVolumeHosts returns a list of all virtual volume hosts known to the cluster. A virtual volume host is a VMware ESX host
        that has initiated a session with the VASA API provider.
        :param virtualVolumeHostIDs:  A list of virtual volume host IDs for which to retrieve information. If you omit this parameter, the method returns information about all virtual volume hosts. 
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
            since=9.0
        )

    def list_virtual_volumes(
            self,
            details=OPTIONAL,
            limit=OPTIONAL,
            recursive=OPTIONAL,
            start_virtual_volume_id=OPTIONAL,
            virtual_volume_ids=OPTIONAL,):
        """
        ListVirtualVolumes enables you to list the virtual volumes currently in the system. You can use this method to list all virtual volumes,
        or only list a subset.
        :param details:  Specifies the level of detail about each virtual volume that is returned. Possible values are: true: Include more details about each virtual volume in the response. false: Include the standard level of detail about each virtual volume in the response. 
        :type details: bool

        :param limit:  The maximum number of virtual volumes to list. 
        :type limit: int

        :param recursive:  Specifies whether to include information about the children of each virtual volume in the response. Possible values are: true: Include information about the children of each virtual volume in the response. false: Do not include information about the children of each virtual volume in the response. 
        :type recursive: bool

        :param startVirtualVolumeID:  The ID of the virtual volume at which to begin the list. 
        :type startVirtualVolumeID: UUID

        :param virtualVolumeIDs:  A list of virtual volume IDs for which to retrieve information. If you specify this parameter, the method returns information about only these virtual volumes. 
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
            since=9.0
        )

    def list_virtual_volume_tasks(
            self,
            virtual_volume_task_ids=OPTIONAL,):
        """
        ListVirtualVolumeTasks returns a list of virtual volume tasks in the system.
        :param virtualVolumeTaskIDs:  A list of virtual volume task IDs for which to retrieve information. If you omit this parameter, the method returns information about all virtual volume tasks. 
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
            since=9.0
        )

    def list_volume_stats_by_virtual_volume(
            self,
            virtual_volume_ids=OPTIONAL,):
        """
        ListVolumeStatsByVirtualVolume enables you to list volume statistics for any volumes in the system that are associated with virtual volumes. Statistics are cumulative from the creation of the volume.
        :param virtualVolumeIDs:  A list of one or more virtual volume IDs for which to retrieve information. If you specify this parameter, the method returns information about only these virtual volumes. 
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
            since=9.0
        )

    def add_volumes_to_volume_access_group(
            self,
            volume_access_group_id,
            volumes,):
        """
        AddVolumesToVolumeAccessGroup enables you to add
        volumes to a specified volume access group.
        :param volumeAccessGroupID: [required] The ID of the volume access group to which volumes are added. 
        :type volumeAccessGroupID: int

        :param volumes: [required] The list of volumes to add to the volume access group. 
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
            since=5.0
        )

    def cancel_clone(
            self,
            clone_id,):
        """
        CancelClone enables you to stop an ongoing CloneVolume or CopyVolume process. When you cancel a group clone operation, the
        system completes and removes the operation's associated asyncHandle.
        :param cloneID: [required] The cloneID for the ongoing clone process. 
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
            since=9.0
        )

    def cancel_group_clone(
            self,
            group_clone_id,):
        """
        CancelGroupClone enables you to stop an ongoing CloneMultipleVolumes process occurring on a group of volumes. When you cancel
        a group clone operation, the system completes and removes the operation's associated asyncHandle.
        :param groupCloneID: [required] The cloneID for the ongoing clone process. 
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
            since=9.0
        )

    def clone_multiple_volumes(
            self,
            volumes,
            access=OPTIONAL,
            group_snapshot_id=OPTIONAL,
            new_account_id=OPTIONAL,):
        """
        CloneMultipleVolumes enables you to create a clone of a group of specified volumes. You can assign a consistent set of characteristics
        to a group of multiple volumes when they are cloned together.
        Before using groupSnapshotID to clone the volumes in a group snapshot, you must create the group snapshot by using the
        CreateGroupSnapshot API method or the Element OS Web UI. Using groupSnapshotID is optional when cloning multiple volumes.
        Note: Cloning multiple volumes is allowed if cluster fullness is at stage 2 or 3. Clones are not created when cluster fullness is
        at stage 4 or 5.
        :param volumes: [required] Unique ID for each volume to include in the clone. If optional parameters are not specified, the values are inherited from the source volumes. Required parameter for "volumes" array: volumeID Optional parameters for "volumes" array: access: Can be one of readOnly, readWrite, locked, or replicationTarget attributes: List of name-value pairs in JSON object format. name: New name for the clone. newAccountID: Account ID for the new volumes. newSize: New size Total size of the volume, in bytes. Size is rounded up to the nearest 1MB. 
        :type volumes: CloneMultipleVolumeParams

        :param access:  New default access method for the new volumes if not overridden by information passed in the volume's array. 
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
            since=7.0
        )

    def clone_volume(
            self,
            volume_id,
            name,
            new_account_id=OPTIONAL,
            new_size=OPTIONAL,
            access=OPTIONAL,
            snapshot_id=OPTIONAL,
            attributes=OPTIONAL,
            enable512e=OPTIONAL,):
        """
        CloneVolume enables you to create a copy of a volume. This method is asynchronous and might take a variable amount of time to complete. The cloning process begins immediately when you make the CloneVolume request and is representative of the state of the volume when the API method is issued. You can use the GetAsyncResult method to determine when the cloning process is complete and the new volume is available for connections. You can use ListSyncJobs to see the progress of creating the clone.
        Note: The initial attributes and QoS settings for the volume are inherited from the volume being cloned. You can change these settings with ModifyVolume.
        Note: Cloned volumes do not inherit volume access group memberships from the source volume.
        :param volumeID: [required] VolumeID for the volume to be cloned. 
        :type volumeID: int

        :param name: [required] The name of the new cloned volume. Might be 1 to 64 characters in length. 
        :type name: str

        :param newAccountID:  AccountID for the owner of the new volume. If unspecified, the accountID of the owner of the volume being cloned is used. 
        :type newAccountID: int

        :param newSize:  New size of the volume, in bytes. Might be greater or less than the size of the volume being cloned. If unspecified, the volume size is not changed. Size is rounded to the nearest 1MB. 
        :type newSize: int

        :param access:  Specifies the level of access allowed for the new volume. Possible values are: readOnly: Only read operations are allowed. readWrite: Reads and writes are allowed. locked: No reads or writes are allowed. If unspecified, the level of access of the volume being cloned is used. replicationTarget: Identify a volume as the target volume for a paired set of volumes. If the volume is not paired, the access status is locked. If a value is not specified, the access value does not change. 
        :type access: str

        :param snapshotID:  ID of the snapshot that is used as the source of the clone. If no ID is provided, the current active volume is used. 
        :type snapshotID: int

        :param attributes:  List of name-value pairs in JSON object format. 
        :type attributes: dict

        :param enable512e:  Should the volume provide 512-byte sector emulation? 
        :type enable512e: bool
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
        if enable512e is not None:
            params["enable512e"] = enable512e
        
        # There is no adaptor.
        return self.send_request(
            'CloneVolume',
            CloneVolumeResult,
            params,
            since=1.0
        )

    def copy_volume(
            self,
            volume_id,
            dst_volume_id,
            snapshot_id=OPTIONAL,):
        """
        CopyVolume enables you to overwrite the data contents of an existing volume with the data contents of another volume (or
        snapshot). Attributes of the destination volume such as IQN, QoS settings, size, account, and volume access group membership are
        not changed. The destination volume must already exist and must be the same size as the source volume.
        NetApp strongly recommends that clients unmount the destination volume before the CopyVolume operation begins. If the
        destination volume is modified during the copy operation, the changes will be lost.
        This method is asynchronous and may take a variable amount of time to complete. You can use the GetAsyncResult method to
        determine when the process has finished, and ListSyncJobs to see the progress of the copy.
        :param volumeID: [required] VolumeID of the volume to be read from. 
        :type volumeID: int

        :param dstVolumeID: [required] VolumeID of the volume to be overwritten. 
        :type dstVolumeID: int

        :param snapshotID:  ID of the snapshot that is used as the source of the clone. If no ID is provided, the current active volume is used. 
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
            since=9.0
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
        CreateVolume enables you to create a new (empty) volume on the cluster. As soon as the volume creation is complete, the volume is
        available for connection via iSCSI.
        :param name: [required] The name of the volume access group (might be user specified). Not required to be unique, but recommended. Might be 1 to 64 characters in length. 
        :type name: str

        :param accountID: [required] AccountID for the owner of this volume. 
        :type accountID: int

        :param totalSize: [required] Total size of the volume, in bytes. Size is rounded up to the nearest 1MB size. 
        :type totalSize: int

        :param enable512e: [required] Specifies whether 512e emulation is enabled or not. Possible values are: true: The volume provides 512-byte sector emulation. false: 512e emulation is not enabled. 
        :type enable512e: bool

        :param qos:  Initial quality of service settings for this volume. Default values are used if none are specified. Valid settings are: minIOPS maxIOPS burstIOPS You can get the default values for a volume by using the GetDefaultQoS method. 
        :type qos: QoS

        :param attributes:  The list of name-value pairs in JSON object format. Total attribute size must be less than 1000B, or 1KB, including JSON formatting characters. 
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
            since=1.0
        )

    def delete_volume(
            self,
            volume_id,):
        """
        DeleteVolume marks an active volume for deletion. When marked, the volume is purged (permanently deleted) after the cleanup
        interval elapses. After making a request to delete a volume, any active iSCSI connections to the volume are immediately terminated
        and no further connections are allowed while the volume is in this state. A marked volume is not returned in target discovery
        requests.
        Any snapshots of a volume that has been marked for deletion are not affected. Snapshots are kept until the volume is purged from
        the system.
        If a volume is marked for deletion and has a bulk volume read or bulk volume write operation in progress, the bulk volume read or
        write operation is stopped.
        If the volume you delete is paired with a volume, replication between the paired volumes is suspended and no data is transferred
        to it or from it while in a deleted state. The remote volume that the deleted volume was paired with enters into a PausedMisconfigured state and data is no longer sent to it or from the deleted volume. Until the deleted volume is purged, it can be restored and data transfers resume. If the deleted volume gets purged from the system, the volume it was paired with enters into a StoppedMisconfigured state and the volume pairing status is removed. The purged volume becomes permanently unavailable.
        :param volumeID: [required] The ID of the volume to be deleted. 
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
            since=1.0
        )

    def delete_volumes(
            self,
            account_ids=OPTIONAL,
            volume_access_group_ids=OPTIONAL,
            volume_ids=OPTIONAL,):
        """
        DeleteVolumes marks multiple (up to 500) active volumes for deletion.
        Once marked, the volumes are purged (permanently deleted) after the cleanup interval elapses.
        The cleanup interval can be set in the SetClusterSettings method.
        For more information on using this method, see SetClusterSettings on page 1.
        After making a request to delete volumes, any active iSCSI connections to the volumes are immediately terminated
        and no further connections are allowed while the volumes are in this state.
        A marked volume is not returned in target discovery requests.
        Any snapshots of a volume that has been marked for deletion are not affected.
        Snapshots are kept until the volume is purged from the system.
        If a volume is marked for deletion and has a bulk volume read or bulk volume write operation in progress,
        the bulk volume read or write operation is stopped.
        If the volumes you delete are paired with a volume, replication between the paired volumes is suspended
        and no data is transferred to them or from them while in a deleted state.
        The remote volumes the deleted volumes were paired with enter into a PausedMisconfigured state
        and data is no longer sent to them or from the deleted volumes.
        Until the deleted volumes are purged, they can be restored and data transfers resume.
        If the deleted volumes are purged from the system, the volumes they were paired with enter into a
        StoppedMisconfigured state and the volume pairing status is removed.
        The purged volumes become permanently unavailable.
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
            since=9.0
        )

    def get_default_qos(
            self,):
        """
        GetDefaultQoS enables you to retrieve the default QoS values for a newly created volume.        """

        self._check_connection_type("get_default_qos", "Cluster")

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'GetDefaultQoS',
            VolumeQOS,
            params,
            since=1.0
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
            since=9.0
        )

    def get_volume_efficiency(
            self,
            volume_id,):
        """
        GetVolumeEfficiency enables you to retrieve information about a volume. Only the volume you give as a parameter in this API method is used to compute the capacity.
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
            since=6.0
        )

    def get_volume_stats(
            self,
            volume_id,):
        """
        GetVolumeStats enables  you to retrieve high-level activity measurements for a single volume. Values are cumulative from the creation of the volume.
        :param volumeID: [required] Specifies the volume for which statistics are gathered. 
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
            since=1.0
        )

    def list_active_volumes(
            self,
            start_volume_id=OPTIONAL,
            limit=OPTIONAL,
            include_virtual_volumes=OPTIONAL,):
        """
        ListActiveVolumes enables you to return the list of active volumes currently in the system. The list of volumes is returned sorted in
        VolumeID order and can be returned in multiple parts (pages).
        :param startVolumeID:  Starting VolumeID to return. If no volume exists with this VolumeID, the next volume by VolumeID order is used as the start of the list. To page through the list, pass the VolumeID of the last volume in the previous response + 1. 
        :type startVolumeID: int

        :param limit:  Maximum number of Volume Info objects to return. A value of 0 (zero) returns all volumes (unlimited). 
        :type limit: int

        :param includeVirtualVolumes:  Specifies that virtual volumes are included in the response by default. To exclude virtual volumes, set to false. 
        :type includeVirtualVolumes: bool
        """

        self._check_connection_type("list_active_volumes", "Cluster")

        params = { 
        }
        if start_volume_id is not None:
            params["startVolumeID"] = start_volume_id
        if limit is not None:
            params["limit"] = limit
        if include_virtual_volumes is not None:
            if self.api_version < 9.0:
                raise ApiParameterVersionError("list_active_volumes", 9.0,
                    [("include_virtual_volumes", include_virtual_volumes, 9.0, False)])
            else:
                params["includeVirtualVolumes"] = include_virtual_volumes
        
        # There is no adaptor.
        return self.send_request(
            'ListActiveVolumes',
            ListActiveVolumesResult,
            params,
            since=1.0
        )

    def list_bulk_volume_jobs(
            self,):
        """
        ListBulkVolumeJobs enables you to retrieve information about each bulk volume read or write operation that is occurring in the
        system.        """

        self._check_connection_type("list_bulk_volume_jobs", "Cluster")

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'ListBulkVolumeJobs',
            ListBulkVolumeJobsResult,
            params,
            since=6.0
        )

    def list_deleted_volumes(
            self,
            include_virtual_volumes=OPTIONAL,):
        """
        ListDeletedVolumes enables you to retrieve the list of volumes that have been marked for deletion and purged from the system.
        :param includeVirtualVolumes:  Specifies that virtual volumes are included in the response by default. To exclude virtual volumes, set to false. 
        :type includeVirtualVolumes: bool
        """

        self._check_connection_type("list_deleted_volumes", "Cluster")

        params = { 
        }
        if include_virtual_volumes is not None:
            if self.api_version < 9.0:
                raise ApiParameterVersionError("list_deleted_volumes", 9.0,
                    [("include_virtual_volumes", include_virtual_volumes, 9.0, False)])
            else:
                params["includeVirtualVolumes"] = include_virtual_volumes
        
        # There is no adaptor.
        return self.send_request(
            'ListDeletedVolumes',
            ListDeletedVolumesResult,
            params,
            since=1.0
        )

    def list_volumes(
            self,
            start_volume_id=OPTIONAL,
            limit=OPTIONAL,
            volume_status=OPTIONAL,
            accounts=OPTIONAL,
            is_paired=OPTIONAL,
            volume_ids=OPTIONAL,
            volume_name=OPTIONAL,
            include_virtual_volumes=OPTIONAL,):
        """
        The ListVolumes method enables you to retrieve a list of volumes that are in a cluster. You can specify the volumes you want to
        return in the list by using the available parameters.
        :param startVolumeID:  Only volumes with an ID greater than or equal to this value are returned. Mutually exclusive with the volumeIDs parameter. 
        :type startVolumeID: int

        :param limit:  Specifies the maximum number of volume results that are returned. Mutually exclusive with the volumeIDs parameter. 
        :type limit: int

        :param volumeStatus:  Only volumes with a status equal to the status value are returned. Possible values are: creating snapshotting active deleted 
        :type volumeStatus: str

        :param accounts:  Returns only the volumes owned by the accounts you specify here. Mutually exclusive with the volumeIDs parameter. 
        :type accounts: int

        :param isPaired:  Returns volumes that are paired or not paired. Possible values are: true: Returns all paired volumes. false: Returns all volumes that are not paired. 
        :type isPaired: bool

        :param volumeIDs:  A list of volume IDs. If you supply this parameter, other parameters operate only on this set of volumes. Mutually exclusive with the accounts, startVolumeID, and limit parameters. 
        :type volumeIDs: int

        :param volumeName:  Only volume object information matching the volume name is returned. 
        :type volumeName: str

        :param includeVirtualVolumes:  Specifies that virtual volumes are included in the response by default. To exclude virtual volumes, set to false. 
        :type includeVirtualVolumes: bool
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
        if volume_name is not None:
            params["volumeName"] = volume_name
        if include_virtual_volumes is not None:
            if self.api_version < 9.0:
                raise ApiParameterVersionError("list_volumes", 9.0,
                    [("include_virtual_volumes", include_virtual_volumes, 9.0, False)])
            else:
                params["includeVirtualVolumes"] = include_virtual_volumes
        
        # There is no adaptor.
        return self.send_request(
            'ListVolumes',
            ListVolumesResult,
            params,
            since=8.0
        )

    def list_volumes_for_account(
            self,
            account_id,
            start_volume_id=OPTIONAL,
            limit=OPTIONAL,
            include_virtual_volumes=OPTIONAL,):
        """
        ListVolumesForAccount returns the list of active and (pending) deleted volumes for an account.
        :param accountID: [required] Returns all volumes owned by this AccountID. 
        :type accountID: int

        :param startVolumeID:  The ID of the first volume to list. This can be useful for paging results. By default, this starts at the lowest VolumeID. 
        :type startVolumeID: int

        :param limit:  The maximum number of volumes to return from the API. 
        :type limit: int

        :param includeVirtualVolumes:  Specifies that virtual volumes are included in the response by default. To exclude virtual volumes, set to false. 
        :type includeVirtualVolumes: bool
        """

        self._check_connection_type("list_volumes_for_account", "Cluster")

        params = { 
            "accountID": account_id,
        }
        if start_volume_id is not None:
            params["startVolumeID"] = start_volume_id
        if limit is not None:
            params["limit"] = limit
        if include_virtual_volumes is not None:
            if self.api_version < 9.0:
                raise ApiParameterVersionError("list_volumes_for_account", 9.0,
                    [("include_virtual_volumes", include_virtual_volumes, 9.0, True)])
            else:
                params["includeVirtualVolumes"] = include_virtual_volumes
        
        # There is no adaptor.
        return self.send_request(
            'ListVolumesForAccount',
            ListVolumesForAccountResult,
            params,
            since=1.0
        )

    def list_volume_stats(
            self,
            volume_ids=OPTIONAL,):
        """
        ListVolumeStats returns high-level activity measurements for a single volume, list of volumes, or all volumes (if you omit the volumeIDs parameter). Measurement values are cumulative from the creation of the volume.
        :param volumeIDs:  A list of volume IDs of volumes from which to retrieve activity information. 
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
            since=7.0
        )

    def list_volume_stats_by_account(
            self,
            accounts=OPTIONAL,
            include_virtual_volumes=OPTIONAL,):
        """
        ListVolumeStatsByAccount returns high-level activity measurements for every account. Values are summed from all the volumes owned by the account.
        :param accounts:  One or more account ids by which to filter the result. 
        :type accounts: int

        :param includeVirtualVolumes:  Includes virtual volumes in the response by default. To exclude virtual volumes, set to false. 
        :type includeVirtualVolumes: bool
        """

        self._check_connection_type("list_volume_stats_by_account", "Cluster")

        params = { 
        }
        if accounts is not None:
            params["accounts"] = accounts
        if include_virtual_volumes is not None:
            if self.api_version < 9.0:
                raise ApiParameterVersionError("list_volume_stats_by_account", 9.0,
                    [("include_virtual_volumes", include_virtual_volumes, 9.0, False)])
            else:
                params["includeVirtualVolumes"] = include_virtual_volumes
        
        # There is no adaptor.
        return self.send_request(
            'ListVolumeStatsByAccount',
            ListVolumeStatsByAccountResult,
            params,
            since=1.0
        )

    def list_volume_stats_by_volume(
            self,
            include_virtual_volumes=OPTIONAL,):
        """
        ListVolumeStatsByVolume returns high-level activity measurements for every volume, by volume. Values are cumulative from the
        creation of the volume.
        :param includeVirtualVolumes:  Specifies that virtual volumes are included in the response by default. To exclude virtual volumes, set to false. 
        :type includeVirtualVolumes: bool
        """

        self._check_connection_type("list_volume_stats_by_volume", "Cluster")

        params = { 
        }
        if include_virtual_volumes is not None:
            if self.api_version < 9.0:
                raise ApiParameterVersionError("list_volume_stats_by_volume", 9.0,
                    [("include_virtual_volumes", include_virtual_volumes, 9.0, False)])
            else:
                params["includeVirtualVolumes"] = include_virtual_volumes
        
        # There is no adaptor.
        return self.send_request(
            'ListVolumeStatsByVolume',
            ListVolumeStatsByVolumeResult,
            params,
            since=1.0
        )

    def list_volume_stats_by_volume_access_group(
            self,
            volume_access_groups=OPTIONAL,
            include_virtual_volumes=OPTIONAL,):
        """
        ListVolumeStatsByVolumeAccessGroup enables you to get total activity measurements for all of the volumes that are a member of the
        specified volume access group(s).
        :param volumeAccessGroups:  An array of VolumeAccessGroupIDs for which volume activity is returned. If omitted, statistics for all volume access groups are returned. 
        :type volumeAccessGroups: int

        :param includeVirtualVolumes:  Specifies that virtual volumes are included in the response by default. To exclude virtual volumes, set to false. 
        :type includeVirtualVolumes: bool
        """

        self._check_connection_type("list_volume_stats_by_volume_access_group", "Cluster")

        params = { 
        }
        if volume_access_groups is not None:
            params["volumeAccessGroups"] = volume_access_groups
        if include_virtual_volumes is not None:
            if self.api_version < 9.0:
                raise ApiParameterVersionError("list_volume_stats_by_volume_access_group", 9.0,
                    [("include_virtual_volumes", include_virtual_volumes, 9.0, False)])
            else:
                params["includeVirtualVolumes"] = include_virtual_volumes
        
        # There is no adaptor.
        return self.send_request(
            'ListVolumeStatsByVolumeAccessGroup',
            ListVolumeStatsByVolumeAccessGroupResult,
            params,
            since=5.0
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
        ModifyVolume enables you to modify settings on an existing volume. You can make modifications to one volume at a time and
        changes take place immediately. If you do not specify QoS values when you modify a volume, they remain the same as before the modification. You can retrieve
        default QoS values for a newly created volume by running the GetDefaultQoS method.
        When you need to increase the size of a volume that is being replicated, do so in the following order to prevent replication errors:
        1. Increase the size of the "Replication Target" volume.
        2. Increase the size of the source or "Read / Write" volume.
        NetApp recommends that both the target and source volumes are the same size.
        Note: If you change the "access" status to locked or target, all existing iSCSI connections are terminated.
        :param volumeID: [required] VolumeID for the volume to be modified. 
        :type volumeID: int

        :param accountID:  AccountID to which the volume is reassigned. If unspecified, the previous account name is used. 
        :type accountID: int

        :param access:  Specifies the access allowed for the volume. Possible values are: readOnly: Only read operations are allowed. readWrite: Reads and writes are allowed. locked: No reads or writes are allowed. If not specified, the access value does not change. replicationTarget: Identify a volume as the target volume for a paired set of volumes. If the volume is not paired, the access status is locked. If a value is not specified, the access value does not change. 
        :type access: str

        :param qos:  New QoS settings for this volume. If not specified, the QoS settings are not changed. 
        :type qos: QoS

        :param totalSize:  New size of the volume in bytes. 1000000000 is equal to 1GB. Size is rounded up to the nearest 1MB. This parameter can only be used to increase the size of a volume. 
        :type totalSize: int

        :param attributes:  List of name-value pairs in JSON object format. 
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
            since=1.0
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
        ModifyVolumes allows you to configure up to 500 existing volumes at one time. Changes take place immediately.
        If ModifyVolumes fails to modify any of the specified volumes, none of the specified volumes are changed.
        If you do not specify QoS values when you modify volumes, the QoS values for each volume remain unchanged.
        You can retrieve default QoS values for a newly created volume by running the GetDefaultQoS method.
        When you need to increase the size of volumes that are being replicated, do so in the following order
        to prevent replication errors:
           Increase the size of the "Replication Target" volume.
           Increase the size of the source or "Read / Write" volume.
        Recommend that both the target and source volumes be the same size.
        NOTE: If you change access status to locked or replicationTarget all existing iSCSI connections are terminated.
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

        :param attributes:  List of name/value pairs in JSON object format. 
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
            since=9.0
        )

    def purge_deleted_volume(
            self,
            volume_id,):
        """
        PurgeDeletedVolume immediately and permanently purges a volume that has been deleted. You must delete a volume using
        DeleteVolume before it can be purged. Volumes are purged automatically after a period of time, so usage of this method is not
        typically required.
        :param volumeID: [required] The ID of the volume to be purged. 
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
            since=1.0
        )

    def purge_deleted_volumes(
            self,
            volume_ids=OPTIONAL,
            account_ids=OPTIONAL,
            volume_access_group_ids=OPTIONAL,):
        """
        PurgeDeletedVolumes immediately and permanently purges volumes that have been deleted.
        You can use this method to purge up to 500 volumes at one time.
        You must delete volumes using DeleteVolumes before they can be purged.
        Volumes are purged by the system automatically after a period of time, so usage of this method is not typically required.
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
            since=9.0
        )

    def remove_volumes_from_volume_access_group(
            self,
            volume_access_group_id,
            volumes,):
        """
        The RemoveVolumeFromVolumeAccessGroup method enables you to remove volumes from a volume access group.
        :param volumeAccessGroupID: [required] The ID of the volume access group to remove volumes from. 
        :type volumeAccessGroupID: int

        :param volumes: [required] The ID of the volume access group to remove volumes from. 
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
            since=5.0
        )

    def restore_deleted_volume(
            self,
            volume_id,):
        """
        RestoreDeletedVolume marks a deleted volume as active again. This action makes the volume immediately available for iSCSI connection.
        :param volumeID: [required] VolumeID of the deleted volume to be restored. 
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
            since=1.0
        )

    def set_default_qos(
            self,
            min_iops=OPTIONAL,
            max_iops=OPTIONAL,
            burst_iops=OPTIONAL,):
        """
        SetDefaultQoS enables you to configure the default Quality of Service (QoS) values (measured in inputs and outputs per second, or
        IOPS) for a volume. For more information about QoS in a SolidFire cluster, see the User Guide.
        :param minIOPS:  The minimum number of sustained IOPS provided by the cluster to a volume. 
        :type minIOPS: int

        :param maxIOPS:  The maximum number of sustained IOPS provided by the cluster to a volume. 
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
            since=9.0
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
        StartBulkVolumeRead enables you to initialize a bulk volume read session on a specified volume. Only two bulk volume processes
        can run simultaneously on a volume. When you initialize the session, data is read from a SolidFire storage volume for the purposes
        of storing the data on an external backup source. The external data is accessed by a web server running on an SF-series node.
        Communications and server interaction information for external data access is passed by a script running on the storage system.
        At the start of a bulk volume read operation, a snapshot of the volume is made and the snapshot is deleted when the read is complete. You can also read a snapshot of the volume by entering the ID of the snapshot as a parameter. When you read a
        previous snapshot, the system does not create a new snapshot of the volume or delete the previous snapshot when the
        read completes.
        Note: This process creates a new snapshot if the ID of an existing snapshot is not provided. Snapshots can be created if cluster fullness is at stage 2 or 3. Snapshots are not created when cluster fullness is at stage 4 or 5.
        :param volumeID: [required] The ID of the volume to be read. 
        :type volumeID: int

        :param format: [required] The format of the volume data. It can be either of the following formats: uncompressed: Every byte of the volume is returned without any compression. native: Opaque data is returned that is smaller and more efficiently stored and written on a subsequent bulk volume write. 
        :type format: str

        :param snapshotID:  The ID of a previously created snapshot used for bulk volume reads. If no ID is entered, a snapshot of the current active volume image is made. 
        :type snapshotID: int

        :param script:  The executable name of a script. If unspecified, the key and URL is necessary to access SF-series nodes. The script is run on the primary node and the key and URL is returned to the script so the local web server can be contacted. 
        :type script: str

        :param scriptParameters:  JSON parameters to pass to the script. 
        :type scriptParameters: dict

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
            since=6.0
        )

    def start_bulk_volume_write(
            self,
            volume_id,
            format,
            script=OPTIONAL,
            script_parameters=OPTIONAL,
            attributes=OPTIONAL,):
        """
        StartBulkVolumeWrite enables you to initialize a bulk volume write session on a specified volume. Only two bulk volume processes can run simultaneously on a volume. When you initialize the write session, data is written to a SolidFire storage volume from an external backup source. The external data is accessed by a web server running on an SF-series node. Communications and server
        interaction information for external data access is passed by a script running on the storage system.
        :param volumeID: [required] The ID of the volume to be written to. 
        :type volumeID: int

        :param format: [required] The format of the volume data. It can be either of the following formats: uncompressed: Every byte of the volume is returned without any compression. native: Opaque data is returned that is smaller and more efficiently stored and written on a subsequent bulk volume write. 
        :type format: str

        :param script:  The executable name of a script. If unspecified, the key and URL are necessary to access SF-series nodes. The script runs on the primary node and the key and URL is returned to the script, so the local web server can be contacted. 
        :type script: str

        :param scriptParameters:  JSON parameters to pass to the script. 
        :type scriptParameters: dict

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
            since=6.0
        )

    def update_bulk_volume_status(
            self,
            key,
            status,
            percent_complete=OPTIONAL,
            message=OPTIONAL,
            attributes=OPTIONAL,):
        """
        You can use UpdateBulkVolumeStatus in a script to update the status of a bulk volume job that you started with the
        StartBulkVolumeRead or StartBulkVolumeWrite methods.
        :param key: [required] The key assigned during initialization of a StartBulkVolumeRead or StartBulkVolumeWrite session. 
        :type key: str

        :param status: [required] The status of the given bulk volume job. The system sets the status. Possible values are:  running: Jobs that are still active. complete: Jobs that are done. failed: Jobs that failed. 
        :type status: str

        :param percentComplete:  The completed progress of the bulk volume job as a percentage value. 
        :type percentComplete: str

        :param message:  The message returned indicating the status of the bulk volume job after the job is complete. 
        :type message: str

        :param attributes:  JSON attributes; updates what is on the bulk volume job. 
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
            since=6.0
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
        You can use CreateVolumeAccessGroup to create a new volume access group. When you create the volume access group, you need to give it a name, and you can optionally enter initiators and volumes. After you create the group, you can add volumes and initiator IQNs. Any initiator IQN that you add to the volume access group is able to access any volume in the group without CHAP authentication.
        :param name: [required] The name for this volume access group. Not required to be unique, but recommended. 
        :type name: str

        :param initiators:  List of initiators to include in the volume access group. If unspecified, the access group's configured initiators are not modified. 
        :type initiators: str

        :param volumes:  List of volumes to initially include in the volume access group. If unspecified, the access group's volumes are not modified. 
        :type volumes: int

        :param virtualNetworkID:  The ID of the SolidFire virtual network to associate the volume access group with. 
        :type virtualNetworkID: int

        :param virtualNetworkTags:  The ID of the SolidFire virtual network to associate the volume access group with. 
        :type virtualNetworkTags: int

        :param attributes:  List of name-value pairs in JSON object format. 
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
            since=5.0
        )

    def delete_volume_access_group(
            self,
            volume_access_group_id,):
        """
        DeleteVolumeAccessGroup enables you to delete a
        volume access group.
        :param volumeAccessGroupID: [required] The ID of the volume access group to be deleted. 
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
            since=5.0
        )

    def get_volume_access_group_efficiency(
            self,
            volume_access_group_id,):
        """
        GetVolumeAccessGroupEfficiency enables you to
        retrieve efficiency information about a volume access
        group. Only the volume access group you provide as the
        parameter in this API method is used to compute the
        capacity.
        :param volumeAccessGroupID: [required] The volume access group for which capacity is computed. 
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
            since=6.0
        )

    def get_volume_access_group_lun_assignments(
            self,
            volume_access_group_id,):
        """
        The GetVolumeAccessGroupLunAssignments
        method enables you to retrieve details on LUN mappings
        of a specified volume access group.
        :param volumeAccessGroupID: [required] The unique volume access group ID used to return information. 
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
            since=7.0
        )

    def list_volume_access_groups(
            self,
            start_volume_access_group_id=OPTIONAL,
            limit=OPTIONAL,
            volume_access_groups=OPTIONAL,):
        """
        ListVolumeAccessGroups enables you to return
        information about the volume access groups that are
        currently in the system.
        :param startVolumeAccessGroupID:  The volume access group ID at which to begin the listing. If unspecified, there is no lower limit (implicitly 0). 
        :type startVolumeAccessGroupID: int

        :param limit:  The maximum number of results to return. This can be useful for paging. 
        :type limit: int

        :param volumeAccessGroups:  The list of ids of the volume access groups you wish to list 
        :type volumeAccessGroups: int
        """

        self._check_connection_type("list_volume_access_groups", "Cluster")

        params = { 
        }
        if start_volume_access_group_id is not None:
            params["startVolumeAccessGroupID"] = start_volume_access_group_id
        if limit is not None:
            params["limit"] = limit
        if volume_access_groups is not None:
            params["volumeAccessGroups"] = volume_access_groups
        
        # There is no adaptor.
        return self.send_request(
            'ListVolumeAccessGroups',
            ListVolumeAccessGroupsResult,
            params,
            since=5.0
        )

    def modify_volume_access_group(
            self,
            volume_access_group_id,
            virtual_network_id=OPTIONAL,
            virtual_network_tags=OPTIONAL,
            name=OPTIONAL,
            initiators=OPTIONAL,
            volumes=OPTIONAL,
            delete_orphan_initiators=OPTIONAL,
            attributes=OPTIONAL,):
        """
        You can use ModifyVolumeAccessGroup to update initiators and add or remove volumes from a volume access group. If a specified initiator or volume is a duplicate of what currently exists, the volume access group is left as-is. If you do not specify a value for volumes or initiators, the current list of initiators and volumes is not changed.
        :param volumeAccessGroupID: [required] The ID of the volume access group to modify. 
        :type volumeAccessGroupID: int

        :param virtualNetworkID:  The ID of the SolidFire virtual network to associate the volume access group with. 
        :type virtualNetworkID: int

        :param virtualNetworkTags:  The ID of the SolidFire virtual network to associate the volume access group with. 
        :type virtualNetworkTags: int

        :param name:  The new name for this volume access group. Not required to be unique, but recommended. 
        :type name: str

        :param initiators:  List of initiators to include in the volume access group. If unspecified, the access group's configured initiators are not modified. 
        :type initiators: str

        :param volumes:  List of volumes to initially include in the volume access group. If unspecified, the access group's volumes are not modified. 
        :type volumes: int

        :param deleteOrphanInitiators:  true: Delete initiator objects after they are removed from a volume access group. false: Do not delete initiator objects after they are removed from a volume access group. 
        :type deleteOrphanInitiators: bool

        :param attributes:  List of name-value pairs in JSON object format. 
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
        if delete_orphan_initiators is not None:
            if self.api_version < 9.0:
                raise ApiParameterVersionError("modify_volume_access_group", 9.0,
                    [("delete_orphan_initiators", delete_orphan_initiators, 9.0, False)])
            else:
                params["deleteOrphanInitiators"] = delete_orphan_initiators
        if attributes is not None:
            params["attributes"] = attributes
        
        # There is no adaptor.
        return self.send_request(
            'ModifyVolumeAccessGroup',
            ModifyVolumeAccessGroupResult,
            params,
            since=5.0
        )

    def modify_volume_access_group_lun_assignments(
            self,
            volume_access_group_id,
            lun_assignments,):
        """
        The ModifyVolumeAccessGroupLunAssignments
        method enables you to define custom LUN assignments
        for specific volumes. This method changes only LUN
        values set on the lunAssignments parameter in the
        volume access group. All other LUN assignments remain
        unchanged. LUN assignment values must be unique for volumes in a volume access group. You cannot define duplicate LUN values within a volume access group. However, you can use the same LUN values again in different volume access groups. 
        Note: Correct LUN values are 0 through 16383. The system generates an exception if you pass a LUN value outside of this range. None of the specified LUN assignments are modified if there is an exception. 
        Caution: If you change a LUN assignment for a volume with active I/O, the I/O can be disrupted. You might need to change the server configuration before changing volume LUN assignments.
        :param volumeAccessGroupID: [required] The ID of the volume access group for which the LUN assignments will be modified. 
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
            since=7.0
        )

