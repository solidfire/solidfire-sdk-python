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
        Used to add a new account to the system.
        New volumes can be created under the new account.
        The CHAP settings specified for the account applies to all volumes owned by the account.
        :param username: [required] [&#x27;Unique username for this account.&#x27;, &#x27;(May be 1 to 64 characters in length).&#x27;][&#x27;Unique username for this account.&#x27;, &#x27;(May be 1 to 64 characters in length).&#x27;]
        :type username: str
        
        :param initiatorSecret:  [&#x27;CHAP secret to use for the initiator.&#x27;, &#x27;Should be 12-16 characters long and impenetrable.&#x27;, &#x27;The CHAP initiator secrets must be unique and cannot be the same as the target CHAP secret.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;If not specified, a random secret is created.&#x27;][&#x27;CHAP secret to use for the initiator.&#x27;, &#x27;Should be 12-16 characters long and impenetrable.&#x27;, &#x27;The CHAP initiator secrets must be unique and cannot be the same as the target CHAP secret.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;If not specified, a random secret is created.&#x27;][&#x27;CHAP secret to use for the initiator.&#x27;, &#x27;Should be 12-16 characters long and impenetrable.&#x27;, &#x27;The CHAP initiator secrets must be unique and cannot be the same as the target CHAP secret.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;If not specified, a random secret is created.&#x27;][&#x27;CHAP secret to use for the initiator.&#x27;, &#x27;Should be 12-16 characters long and impenetrable.&#x27;, &#x27;The CHAP initiator secrets must be unique and cannot be the same as the target CHAP secret.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;If not specified, a random secret is created.&#x27;][&#x27;CHAP secret to use for the initiator.&#x27;, &#x27;Should be 12-16 characters long and impenetrable.&#x27;, &#x27;The CHAP initiator secrets must be unique and cannot be the same as the target CHAP secret.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;If not specified, a random secret is created.&#x27;]
        :type initiatorSecret: CHAPSecret
        
        :param targetSecret:  [&#x27;CHAP secret to use for the target (mutual CHAP authentication).&#x27;, &#x27;Should be 12-16 characters long and impenetrable.&#x27;, &#x27;The CHAP target secrets must be unique and cannot be the same as the initiator CHAP secret.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;If not specified, a random secret is created.&#x27;][&#x27;CHAP secret to use for the target (mutual CHAP authentication).&#x27;, &#x27;Should be 12-16 characters long and impenetrable.&#x27;, &#x27;The CHAP target secrets must be unique and cannot be the same as the initiator CHAP secret.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;If not specified, a random secret is created.&#x27;][&#x27;CHAP secret to use for the target (mutual CHAP authentication).&#x27;, &#x27;Should be 12-16 characters long and impenetrable.&#x27;, &#x27;The CHAP target secrets must be unique and cannot be the same as the initiator CHAP secret.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;If not specified, a random secret is created.&#x27;][&#x27;CHAP secret to use for the target (mutual CHAP authentication).&#x27;, &#x27;Should be 12-16 characters long and impenetrable.&#x27;, &#x27;The CHAP target secrets must be unique and cannot be the same as the initiator CHAP secret.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;If not specified, a random secret is created.&#x27;][&#x27;CHAP secret to use for the target (mutual CHAP authentication).&#x27;, &#x27;Should be 12-16 characters long and impenetrable.&#x27;, &#x27;The CHAP target secrets must be unique and cannot be the same as the initiator CHAP secret.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;If not specified, a random secret is created.&#x27;]
        :type targetSecret: CHAPSecret
        
        :param attributes:  List of Name/Value pairs in JSON object format.
        :type attributes: dict
        """

        connection_type = "Cluster"
        self._check_connection_type(connection_type)

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
            params
        )

    def get_account_by_id(
            self,
            account_id,):
        """
        Returns details about an account, given its AccountID.
        :param accountID: [required] Specifies the account for which details are gathered.
        :type accountID: int
        """

        connection_type = "Cluster"
        self._check_connection_type(connection_type)

        params = { 
            "accountID": account_id,
        }
        
        # There is no adaptor.
        return self.send_request(
            'GetAccountByID',
            GetAccountResult,
            params
        )

    def get_account_by_name(
            self,
            username,):
        """
        Returns details about an account, given its Username.
        :param username: [required] Username for the account.
        :type username: str
        """

        connection_type = "Cluster"
        self._check_connection_type(connection_type)

        params = { 
            "username": username,
        }
        
        # There is no adaptor.
        return self.send_request(
            'GetAccountByName',
            GetAccountResult,
            params
        )

    def list_accounts(
            self,
            start_account_id=OPTIONAL,
            limit=OPTIONAL,):
        """
        Returns the entire list of accounts, with optional paging support.
        :param startAccountID:  [&#x27;Starting AccountID to return.&#x27;, &#x27;If no Account exists with this AccountID,&#x27;, &#x27;the next Account by AccountID order is used as the start of the list.&#x27;, &#x27;To page through the list, pass the AccountID of the last Account in the previous response + 1&#x27;][&#x27;Starting AccountID to return.&#x27;, &#x27;If no Account exists with this AccountID,&#x27;, &#x27;the next Account by AccountID order is used as the start of the list.&#x27;, &#x27;To page through the list, pass the AccountID of the last Account in the previous response + 1&#x27;][&#x27;Starting AccountID to return.&#x27;, &#x27;If no Account exists with this AccountID,&#x27;, &#x27;the next Account by AccountID order is used as the start of the list.&#x27;, &#x27;To page through the list, pass the AccountID of the last Account in the previous response + 1&#x27;][&#x27;Starting AccountID to return.&#x27;, &#x27;If no Account exists with this AccountID,&#x27;, &#x27;the next Account by AccountID order is used as the start of the list.&#x27;, &#x27;To page through the list, pass the AccountID of the last Account in the previous response + 1&#x27;]
        :type startAccountID: int
        
        :param limit:  Maximum number of AccountInfo objects to return.
        :type limit: int
        """

        connection_type = "Cluster"
        self._check_connection_type(connection_type)

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
            params
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
        
        :param initiatorSecret:  [&#x27;CHAP secret to use for the initiator.&#x27;, &#x27;Should be 12-16 characters long and impenetrable.&#x27;][&#x27;CHAP secret to use for the initiator.&#x27;, &#x27;Should be 12-16 characters long and impenetrable.&#x27;]
        :type initiatorSecret: CHAPSecret
        
        :param targetSecret:  [&#x27;CHAP secret to use for the target (mutual CHAP authentication).&#x27;, &#x27;Should be 12-16 characters long and impenetrable.&#x27;][&#x27;CHAP secret to use for the target (mutual CHAP authentication).&#x27;, &#x27;Should be 12-16 characters long and impenetrable.&#x27;]
        :type targetSecret: CHAPSecret
        
        :param attributes:  List of Name/Value pairs in JSON object format.
        :type attributes: dict
        """

        connection_type = "Cluster"
        self._check_connection_type(connection_type)

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
            params
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

        connection_type = "Cluster"
        self._check_connection_type(connection_type)

        params = { 
            "accountID": account_id,
        }
        
        # There is no adaptor.
        return self.send_request(
            'RemoveAccount',
            RemoveAccountResult,
            params
        )

    def get_account_efficiency(
            self,
            account_id,
            force=OPTIONAL,):
        """
        GetAccountEfficiency is used to retrieve information about a volume account. Only the account given as a parameter in this API method is used to compute the capacity.
        :param accountID: [required] Specifies the volume account for which capacity is computed.
        :type accountID: int
        
        :param force:  
        :type force: bool
        """

        connection_type = "Cluster"
        self._check_connection_type(connection_type)

        params = { 
            "accountID": account_id,
        }
        if force is not None:
            params["force"] = force
        
        # There is no adaptor.
        return self.send_request(
            'GetAccountEfficiency',
            GetEfficiencyResult,
            params
        )

    def create_backup_target(
            self,
            name,
            attributes=OPTIONAL,):
        """
        CreateBackupTarget allows you to create and store backup target information so that you do not need to re-enter it each time a backup is created.
        :param name: [required] [&#x27;Name for the backup target.&#x27;]
        :type name: str
        
        :param attributes:  List of Name/Value pairs in JSON object format.
        :type attributes: dict
        """

        connection_type = "Cluster"
        self._check_connection_type(connection_type)

        params = { 
            "name": name,
        }
        if attributes is not None:
            params["attributes"] = attributes
        
        # There is no adaptor.
        return self.send_request(
            'CreateBackupTarget',
            CreateBackupTargetResult,
            params
        )

    def get_backup_target(
            self,
            backup_target_id,):
        """
        GetBackupTarget allows you to return information about a specific backup target that has been created.
        :param backupTargetID: [required] [&#x27;Unique identifier assigned to the backup target.&#x27;]
        :type backupTargetID: int
        """

        connection_type = "Cluster"
        self._check_connection_type(connection_type)

        params = { 
            "backupTargetID": backup_target_id,
        }
        
        # There is no adaptor.
        return self.send_request(
            'GetBackupTarget',
            GetBackupTargetResult,
            params
        )

    def list_backup_targets(
            self,):
        """
        You can use ListBackupTargets to retrieve information about all backup targets that have been created."""

        connection_type = "Cluster"
        self._check_connection_type(connection_type)

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'ListBackupTargets',
            ListBackupTargetsResult,
            params
        )

    def modify_backup_target(
            self,
            backup_target_id,
            name=OPTIONAL,
            attributes=OPTIONAL,):
        """
        ModifyBackupTarget is used to change attributes of a backup target.
        :param backupTargetID: [required] [&#x27;Unique identifier assigned to the backup target.&#x27;]
        :type backupTargetID: int
        
        :param name:  [&#x27;Name for the backup target.&#x27;]
        :type name: str
        
        :param attributes:  List of Name/Value pairs in JSON object format.
        :type attributes: dict
        """

        connection_type = "Cluster"
        self._check_connection_type(connection_type)

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
            params
        )

    def remove_backup_target(
            self,
            backup_target_id,):
        """
        RemoveBackupTarget allows you to delete backup targets.
        :param backupTargetID: [required] [&#x27;Unique target ID of the target to remove.&#x27;]
        :type backupTargetID: int
        """

        connection_type = "Cluster"
        self._check_connection_type(connection_type)

        params = { 
            "backupTargetID": backup_target_id,
        }
        
        # There is no adaptor.
        return self.send_request(
            'RemoveBackupTarget',
            RemoveBackupTargetResult,
            params
        )

    def get_cluster_capacity(
            self,):
        """
        Return the high-level capacity measurements for an entire cluster.
        The fields returned from this method can be used to calculate the efficiency rates that are displayed in the Element User Interface."""

        connection_type = "Cluster"
        self._check_connection_type(connection_type)

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'GetClusterCapacity',
            GetClusterCapacityResult,
            params
        )

    def get_cluster_info(
            self,):
        """
        Return configuration information about the cluster."""

        connection_type = "Cluster"
        self._check_connection_type(connection_type)

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'GetClusterInfo',
            GetClusterInfoResult,
            params
        )

    def get_cluster_version_info(
            self,):
        """
        Return information about the Element software version running on each node in the cluster.
        Information about the nodes that are currently in the process of upgrading software is also returned."""

        connection_type = "Cluster"
        self._check_connection_type(connection_type)

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'GetClusterVersionInfo',
            GetClusterVersionInfoResult,
            params
        )

    def get_limits(
            self,):
        """
        Retrieves the limit values set by the API"""

        connection_type = "Cluster"
        self._check_connection_type(connection_type)

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'GetLimits',
            GetLimitsResult,
            params
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

        connection_type = "Cluster"
        self._check_connection_type(connection_type)

        params = { 
        }
        if max_events is not None:
            params["maxEvents"] = max_events
        if start_event_id is not None:
            params["startEventID"] = start_event_id
        if end_event_id is not None:
            params["endEventID"] = end_event_id
        if event_queue_type is not None:
            params["eventQueueType"] = event_queue_type
        
        # There is no adaptor.
        return self.send_request(
            'ListEvents',
            ListEventsResult,
            params
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
        
        :param bestPractices:  [&#x27;Include faults triggered by sub-optimal system configuration.&#x27;, &#x27;Possible values: true, false&#x27;][&#x27;Include faults triggered by sub-optimal system configuration.&#x27;, &#x27;Possible values: true, false&#x27;]
        :type bestPractices: bool
        
        :param update:  
        :type update: bool
        
        :param faultTypes:  [&#x27;Determines the types of faults returned: current: List active, unresolved faults.&#x27;, &#x27;&lt;b&gt;resolved&lt;/b&gt;: List faults that were previously detected and resolved.&#x27;, &quot;&lt;b&gt;all&lt;/b&gt;: (Default) List both current and resolved faults. You can see the fault status in the &#x27;resolved&#x27; field of the Cluster Fault object.&quot;][&#x27;Determines the types of faults returned: current: List active, unresolved faults.&#x27;, &#x27;&lt;b&gt;resolved&lt;/b&gt;: List faults that were previously detected and resolved.&#x27;, &quot;&lt;b&gt;all&lt;/b&gt;: (Default) List both current and resolved faults. You can see the fault status in the &#x27;resolved&#x27; field of the Cluster Fault object.&quot;][&#x27;Determines the types of faults returned: current: List active, unresolved faults.&#x27;, &#x27;&lt;b&gt;resolved&lt;/b&gt;: List faults that were previously detected and resolved.&#x27;, &quot;&lt;b&gt;all&lt;/b&gt;: (Default) List both current and resolved faults. You can see the fault status in the &#x27;resolved&#x27; field of the Cluster Fault object.&quot;]
        :type faultTypes: str
        """

        connection_type = "Cluster"
        self._check_connection_type(connection_type)

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
            params
        )

    def clear_cluster_faults(
            self,
            fault_types=OPTIONAL,):
        """
        ClearClusterFaults is used to clear information about both current faults that are resolved as well as faults that were previously detected and resolved can be cleared.
        :param faultTypes:  [&#x27;Determines the types of faults cleared:&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;current&lt;/b&gt;: Faults that are currently detected and have not been resolved.&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;resolved&lt;/b&gt;: Faults that were previously detected and resolved.&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;all&lt;/b&gt;: Both current and resolved faults are cleared. The fault status can be determined by the &quot;resolved&quot; field of the fault object.&#x27;][&#x27;Determines the types of faults cleared:&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;current&lt;/b&gt;: Faults that are currently detected and have not been resolved.&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;resolved&lt;/b&gt;: Faults that were previously detected and resolved.&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;all&lt;/b&gt;: Both current and resolved faults are cleared. The fault status can be determined by the &quot;resolved&quot; field of the fault object.&#x27;][&#x27;Determines the types of faults cleared:&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;current&lt;/b&gt;: Faults that are currently detected and have not been resolved.&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;resolved&lt;/b&gt;: Faults that were previously detected and resolved.&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;all&lt;/b&gt;: Both current and resolved faults are cleared. The fault status can be determined by the &quot;resolved&quot; field of the fault object.&#x27;][&#x27;Determines the types of faults cleared:&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;current&lt;/b&gt;: Faults that are currently detected and have not been resolved.&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;resolved&lt;/b&gt;: Faults that were previously detected and resolved.&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;all&lt;/b&gt;: Both current and resolved faults are cleared. The fault status can be determined by the &quot;resolved&quot; field of the fault object.&#x27;]
        :type faultTypes: str
        """

        connection_type = "Cluster"
        self._check_connection_type(connection_type)

        params = { 
        }
        if fault_types is not None:
            params["faultTypes"] = fault_types
        
        # There is no adaptor.
        return self.send_request(
            'ClearClusterFaults',
            ClearClusterFaultsResult,
            params
        )

    def get_cluster_config(
            self,):
        """
        The GetClusterConfig API method is used to return information about the cluster configuration this node uses to communicate with the cluster it is a part of.
        <br/><br/>
        <b>Note</b>: This method is available only through the per-node API endpoint 5.0 or later."""

        connection_type = "Node"
        self._check_connection_type(connection_type)

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'GetClusterConfig',
            GetClusterConfigResult,
            params
        )

    def get_cluster_full_threshold(
            self,):
        """
        GetClusterFullThreshold is used to view the stages set for cluster fullness levels. All levels are returned when this method is entered."""

        connection_type = "Cluster"
        self._check_connection_type(connection_type)

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'GetClusterFullThreshold',
            GetClusterFullThresholdResult,
            params
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
        
        :param stage3BlockThresholdPercent:  Percent below &quot;Error&quot; state to raise a cluster &quot;Warning&quot; alert.
        :type stage3BlockThresholdPercent: int
        
        :param maxMetadataOverProvisionFactor:  A value representative of the number of times metadata space can be over provisioned relative to the amount of space available. For example, if there was enough metadata space to store 100 TiB of volumes and this number was set to 5, then 500 TiB worth of volumes could be created.
        :type maxMetadataOverProvisionFactor: int
        """

        connection_type = "Cluster"
        self._check_connection_type(connection_type)

        params = { 
        }
        if stage2_aware_threshold is not None:
            params["stage2AwareThreshold"] = stage2_aware_threshold
        if stage3_block_threshold_percent is not None:
            params["stage3BlockThresholdPercent"] = stage3_block_threshold_percent
        if max_metadata_over_provision_factor is not None:
            params["maxMetadataOverProvisionFactor"] = max_metadata_over_provision_factor
        
        # There is no adaptor.
        return self.send_request(
            'ModifyClusterFullThreshold',
            ModifyClusterFullThresholdResult,
            params
        )

    def get_cluster_stats(
            self,):
        """
        GetClusterStats is used to return high-level activity measurements for the cluster. Values returned are cumulative from the creation of the cluster."""

        connection_type = "Cluster"
        self._check_connection_type(connection_type)

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'GetClusterStats',
            GetClusterStatsResult,
            params
        )

    def list_cluster_admins(
            self,):
        """
        ListClusterAdmins returns the list of all cluster administrators for the cluster. There can be several cluster administrators that have different levels of permissions. There can be only one primary cluster administrator in the system. The primary Cluster Admin is the administrator that was created when the cluster was created. LDAP administrators can also be created when setting up an LDAP system on the cluster."""

        connection_type = "Cluster"
        self._check_connection_type(connection_type)

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'ListClusterAdmins',
            ListClusterAdminsResult,
            params
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
        <br/><br/>
        Each Cluster Admin can be restricted to a sub-set of the API. SolidFire recommends using multiple Cluster Admins for different users and applications. Each Cluster Admin should be given the minimal permissions necessary to reduce the potential impact of credential compromise.
        :param username: [required] Unique username for this Cluster Admin.
        :type username: str
        
        :param password: [required] Password used to authenticate this Cluster Admin.
        :type password: str
        
        :param access: [required] Controls which methods this Cluster Admin can use. For more details on the levels of access, see &quot;Access Control&quot; in the Element API Guide.
        :type access: str
        
        :param acceptEula:  Indicate your acceptance of the End User License Agreement when creating this cluster admin. To accept the EULA, set this parameter to true.
        :type acceptEula: bool
        
        :param attributes:  List of Name/Value pairs in JSON object format.
        :type attributes: dict
        """

        connection_type = "Cluster"
        self._check_connection_type(connection_type)

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
            params
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
        
        :param access:  Controls which methods this Cluster Admin can use. For more details on the levels of access, see &quot;Access Control&quot; in the Element API Guide.
        :type access: str
        
        :param attributes:  List of Name/Value pairs in JSON object format.
        :type attributes: dict
        """

        connection_type = "Cluster"
        self._check_connection_type(connection_type)

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
            params
        )

    def remove_cluster_admin(
            self,
            cluster_admin_id,):
        """
        RemoveClusterAdmin is used to remove a Cluster Admin. The "admin" Cluster Admin cannot be removed.
        :param clusterAdminID: [required] ClusterAdminID for the Cluster Admin to remove.
        :type clusterAdminID: int
        """

        connection_type = "Cluster"
        self._check_connection_type(connection_type)

        params = { 
            "clusterAdminID": cluster_admin_id,
        }
        
        # There is no adaptor.
        return self.send_request(
            'RemoveClusterAdmin',
            RemoveClusterAdminResult,
            params
        )

    def set_cluster_config(
            self,
            cluster,):
        """
        The SetClusterConfig API method is used to set the configuration this node uses to communicate with the cluster it is associated with. To see the states in which these objects can be modified see Cluster Object on page 109. To display the current cluster interface settings for a node, run the GetClusterConfig API method.
        <br/><br/>
        <b>Note</b>: This method is available only through the per-node API endpoint 5.0 or later.
        :param cluster: [required] Objects that are changed for the cluster interface settings. Only the fields you want changed need to be added to this method as objects in the &quot;cluster&quot; parameter.
        :type cluster: ClusterConfig
        """

        connection_type = "Node"
        self._check_connection_type(connection_type)

        params = { 
            "cluster": cluster,
        }
        
        # There is no adaptor.
        return self.send_request(
            'SetClusterConfig',
            SetClusterConfigResult,
            params
        )

    def get_snmp_acl(
            self,):
        """
        GetSnmpACL is used to return the current SNMP access permissions on the cluster nodes."""

        connection_type = "Cluster"
        self._check_connection_type(connection_type)

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'GetSnmpACL',
            GetSnmpACLResult,
            params,
            since=8.0
        )

    def set_snmp_acl(
            self,
            networks,
            usm_users,):
        """
        SetSnmpACL is used to configure SNMP access permissions on the cluster nodes. The values set with this interface apply to all nodes in the cluster, and the values that are passed replace, in whole, all values set in any previous call to SetSnmpACL. Also note that the values set with this interface replace all "network" or "usmUsers" values set with the older SetSnmpInfo.
        :param networks: [required] List of networks and what type of access they have to the SNMP servers running on the cluster nodes. See SNMP Network Object for possible &quot;networks&quot; values. REQUIRED if SNMP v# is disabled.
        :type networks: SnmpNetwork
        
        :param usmUsers: [required] List of users and the type of access they have to the SNMP servers running on the cluster nodes. REQUIRED if SNMP v3 is enabled.
        :type usmUsers: SnmpV3UsmUser
        """

        connection_type = "Cluster"
        self._check_connection_type(connection_type)

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

    def get_snmp_trap_info(
            self,):
        """
        GetSnmpTrapInfo is used to return current SNMP trap configuration information."""

        connection_type = "Cluster"
        self._check_connection_type(connection_type)

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'GetSnmpTrapInfo',
            GetSnmpTrapInfoResult,
            params
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
        
        :param clusterFaultTrapsEnabled: [required] If &quot;true&quot;, when a cluster fault is logged a corresponding solidFireClusterFaultNotification is sent to the configured list of trap recipients.
        :type clusterFaultTrapsEnabled: bool
        
        :param clusterFaultResolvedTrapsEnabled: [required] If &quot;true&quot;, when a cluster fault is logged a corresponding solidFireClusterFaultResolvedNotification is sent to the configured list of trap recipients.
        :type clusterFaultResolvedTrapsEnabled: bool
        
        :param clusterEventTrapsEnabled: [required] If &quot;true&quot;, when a cluster fault is logged a corresponding solidFireClusterEventNotification is sent to the configured list of trap recipients.
        :type clusterEventTrapsEnabled: bool
        """

        connection_type = "Cluster"
        self._check_connection_type(connection_type)

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
            params
        )

    def enable_snmp(
            self,
            snmp_v3_enabled,):
        """
        EnableSnmp is used to enable SNMP on the cluster nodes. The values set with this interface apply to all nodes in the cluster, and the values that are passed replace, in whole, all values set in any previous call to EnableSnmp.
        :param snmpV3Enabled: [required] If set to &quot;true&quot;, then SNMP v3 is enabled on each node in the cluster. If set to &quot;false&quot;, then SNMP v2 is enabled.
        :type snmpV3Enabled: bool
        """

        connection_type = "Cluster"
        self._check_connection_type(connection_type)

        params = { 
            "snmpV3Enabled": snmp_v3_enabled,
        }
        
        # There is no adaptor.
        return self.send_request(
            'EnableSnmp',
            EnableSnmpResult,
            params
        )

    def disable_snmp(
            self,):
        """
        DisableSnmp is used to disable SNMP on the cluster nodes."""

        connection_type = "Cluster"
        self._check_connection_type(connection_type)

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'DisableSnmp',
            DisableSnmpResult,
            params
        )

    def get_snmp_info(
            self,):
        """
        GetSnmpInfo is used to return the current simple network management protocol (SNMP) configuration information.
        <br/><br/>
        <b>Note</b>: GetSnmpInfo will be available for Element OS 8 and prior releases. It will be deprecated after Element OS 8. There are two new SNMP API methods that you should migrate over to. They are GetSnmpState and GetSnmpACL. Please see details in this document for their descriptions and usage."""

        connection_type = "Cluster"
        self._check_connection_type(connection_type)

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'GetSnmpInfo',
            GetSnmpInfoResult,
            params
        )

    def set_snmp_info(
            self,
            networks=OPTIONAL,
            enabled=OPTIONAL,
            snmp_v3_enabled=OPTIONAL,
            usm_users=OPTIONAL,):
        """
        SetSnmpInfo is used to configure SNMP v2 and v3 on the cluster nodes. The values set with this interface apply to all nodes in the cluster, and the values that are passed replace, in whole, all values set in any previous call to SetSnmpInfo.
        <br/><br/>
        <b>Note</b>: EnableSnmp and SetSnmpACL methods can be used to accomplish the same results as SetSnmpInfo. SetSnmpInfo will no longer be available after the Element 8 release. Please use EnableSnmp and SetSnmpACL in the future.
        :param networks:  List of networks and what type of access they have to the SNMP servers running on the cluster nodes. See SNMP Network Object for possible &quot;networks&quot; values. SNMP v2 only.
        :type networks: SnmpNetwork
        
        :param enabled:  If set to &quot;true&quot;, then SNMP is enabled on each node in the cluster.
        :type enabled: bool
        
        :param snmpV3Enabled:  If set to &quot;true&quot;, then SNMP v3 is enabled on each node in the cluster.
        :type snmpV3Enabled: bool
        
        :param usmUsers:  If SNMP v3 is enabled, this value must be passed in place of the &quot;networks&quot; parameter. SNMP v3 only.
        :type usmUsers: SnmpV3UsmUser
        """

        connection_type = "Cluster"
        self._check_connection_type(connection_type)

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
            params
        )

    def get_snmp_state(
            self,):
        """
        GetSnmpState is used to return the current state of the SNMP feature.
        <br/><br/>
        <b>Note</b>: GetSnmpState is new for Element OS 8. Please use this method and SetSnmpACL to migrate your SNMP functionality in the future."""

        connection_type = "Cluster"
        self._check_connection_type(connection_type)

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'GetSnmpState',
            GetSnmpStateResult,
            params,
            since=8.0
        )

    def get_api(
            self,):
        """
        Retrieves the current version of the API and a list of all supported versions."""

        connection_type = "Both"
        self._check_connection_type(connection_type)

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'GetAPI',
            GetAPIResult,
            params
        )

    def get_ntp_info(
            self,):
        """
        GetNtpInfo is used to return the current network time protocol (NTP) configuration information."""

        connection_type = "Cluster"
        self._check_connection_type(connection_type)

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'GetNtpInfo',
            GetNtpInfoResult,
            params
        )

    def get_current_cluster_admin(
            self,):
        """
        GetCurrentClusterAdmin returns information for the current primary cluster administrator. The primary Cluster Admin was ncreated when the cluster was created."""

        connection_type = "Cluster"
        self._check_connection_type(connection_type)

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'GetCurrentClusterAdmin',
            GetCurrentClusterAdminResult,
            params
        )

    def enable_encryption_at_rest(
            self,):
        """
        The EnableEncryptionAtRest method is used to enable the Advanced Encryption Standard (AES) 256-bit encryption at rest on the cluster so that the cluster can manage the encryption key used for the drives on each node. This feature is not enabled by default. Enabling this operation allows the cluster to automatically manage encryption keys internally for the drives on each node in the cluster. Nodes do not store the keys to unlock drives and the keys are never passed over the network. Two nodes participating in a cluster are required to access the key to disable encryption on a drive. The encryption management does not affect performance or efficiency on the cluster. If an encryption-enabled drive or node is removed from the cluster with the API, all data is secure erased and any data left on the drive cannot be read or accessed.
        Enabling or disabling encryption should be performed when the cluster is running and in a healthy state. Encryption can be enabled or disabled at your discretion and can be performed as often as you need.
        <br/><b>Note</b>: This process is asynchronous and returns a response before encryption is enabled. The GetClusterInfo method can be used to poll the system to see when the process has completed."""

        connection_type = "Cluster"
        self._check_connection_type(connection_type)

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'EnableEncryptionAtRest',
            EnableEncryptionAtRestResult,
            params
        )

    def disable_encryption_at_rest(
            self,):
        """
        The DisableEncryptionAtRest method enables you to remove the encryption that was previously applied to the cluster using the EnableEncryptionAtRest method.
        This disable method is asynchronous and returns a response before encryption is disabled.
        You can use the GetClusterInfo method to poll the system to see when the process has completed."""

        connection_type = "Cluster"
        self._check_connection_type(connection_type)

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'DisableEncryptionAtRest',
            DisableEncryptionAtRestResult,
            params
        )

    def snmp_send_test_traps(
            self,):
        """
        SnmpSendTestTraps enables you to test SNMP functionality for a cluster. This method instructs the cluster to send test SNMP traps to the currently configured SNMP manager."""

        connection_type = "Cluster"
        self._check_connection_type(connection_type)

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'SnmpSendTestTraps',
            SnmpSendTestTrapsResult,
            params
        )

    def get_async_result(
            self,
            async_handle,):
        """
        Used to retrieve the result of asynchronous method calls.
        Some method calls are long running and do not complete when the initial response is sent.
        To obtain the result of the method call, polling with GetAsyncResult is required.
        <br/><br/>
        GetAsyncResult returns the overall status of the operation (in progress, completed, or error) in a standard fashion,
        but the actual data returned for the operation depends on the original method call and the return data is documented with each method.
        <br/><br/>
        The result for a completed asynchronous method call can only be retrieved once.
        Once the final result has been returned, later attempts returns an error.
        :param asyncHandle: [required] A value that was returned from the original asynchronous method call.
        :type asyncHandle: int
        """

        connection_type = "Cluster"
        self._check_connection_type(connection_type)

        params = { 
            "asyncHandle": async_handle,
        }
        
        # There is no adaptor.
        return self.send_request(
            'GetAsyncResult',
            GetAsyncResultResult,
            params
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
        <br/><br/>
        When you add a drive, the system automatically determines the "type" of drive it should be.
        <br/><br/>
        The method returns immediately. However, it may take some time for the data in the cluster to be rebalanced using the newly added drives.
        As the new drive(s) are syncing on the system, you can use the "ListSyncJobs" method to see how the drive(s) are being rebalanced and the progress of adding the new drive.
        :param drives: [required] List of drives to add to the cluster.
        :type drives: NewDrive
        """

        connection_type = "Cluster"
        self._check_connection_type(connection_type)

        params = { 
            "drives": drives,
        }
        
        # There is no adaptor.
        return self.send_request(
            'AddDrives',
            AddDrivesResult,
            params
        )

    def list_drives(
            self,):
        """
        ListDrives allows you to retrieve the list of the drives that exist in the cluster's active nodes.
        This method returns drives that have been added as volume metadata or block drives as well as drives that have not been added and are available."""

        connection_type = "Cluster"
        self._check_connection_type(connection_type)

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'ListDrives',
            ListDrivesResult,
            params
        )

    def get_drive_hardware_info(
            self,
            drive_id,):
        """
        GetDriveHardwareInfo returns all the hardware info for the given drive. This generally includes manufacturers, vendors, versions, and other associated hardware identification information.
        :param driveID: [required] DriveID for the drive information requested. DriveIDs can be obtained via the &quot;ListDrives&quot; method.
        :type driveID: int
        """

        connection_type = "Cluster"
        self._check_connection_type(connection_type)

        params = { 
            "driveID": drive_id,
        }
        
        # There is no adaptor.
        return self.send_request(
            'GetDriveHardwareInfo',
            GetDriveHardwareInfoResult,
            params
        )

    def list_drive_hardware(
            self,
            force,):
        """
        ListDriveHardware returns all the drives connected to a node. Use this method on the cluster to return drive hardware information for all the drives on all nodes.
        :param force: [required] This must be set to true in order to retrieve the drive hardware stats from the cluster.
        :type force: bool
        """

        connection_type = "Node"
        self._check_connection_type(connection_type)

        params = { 
            "force": force,
        }
        
        # There is no adaptor.
        return self.send_request(
            'ListDriveHardware',
            ListDriveHardwareResult,
            params
        )

    def reset_drives(
            self,
            drives,
            force,):
        """
        ResetDrives is used to pro-actively initialize drives and remove all data currently residing on the drive. The drive can then be reused in an existing node or used in an upgraded SolidFire node. This method requires the force=true parameter to be included in the method call.
        <br/><br/>
        <b>Note</b>: This method is available only through the per-node API endpoint 5.0 or later.
        :param drives: [required] List of device names (not driveIDs) to reset.
        :type drives: str
        
        :param force: [required] The &quot;force&quot; parameter must be included on this method to successfully reset a drive.
        :type force: bool
        """

        connection_type = "Node"
        self._check_connection_type(connection_type)

        params = { 
            "drives": drives,
            "force": force,
        }
        
        # There is no adaptor.
        return self.send_request(
            'ResetDrives',
            ResetDrivesResult,
            params
        )

    def test_drives(
            self,
            force,
            minutes=OPTIONAL,):
        """
        The TestDrives API method is used to run a hardware validation on all the drives on the node. Hardware failures on the drives are detected if present and they are reported in the results of the validation tests.
        <br/><br/>
        <b>Note</b>: This test takes approximately 10 minutes.
        <br/><br/>
        <b>Note</b>: This method is available only through the per-node API endpoint 5.0 or later.
        :param minutes:  The number of minutes to run the test can be specified.
        :type minutes: int
        
        :param force: [required] The &quot;force&quot; parameter must be included on this method to successfully test the drives on the node.
        :type force: bool
        """

        connection_type = "Node"
        self._check_connection_type(connection_type)

        params = { 
            "force": force,
        }
        if minutes is not None:
            params["minutes"] = minutes
        
        # There is no adaptor.
        return self.send_request(
            'TestDrives',
            TestDrivesResult,
            params
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

        connection_type = "Cluster"
        self._check_connection_type(connection_type)

        params = { 
            "driveID": drive_id,
        }
        
        # There is no adaptor.
        return self.send_request(
            'GetDriveStats',
            GetDriveStatsResult,
            params
        )

    def secure_erase_drives(
            self,
            drives,):
        """
        SecureEraseDrives is used to remove any residual data from drives that have a status of "available." For example, when replacing a drive at its end-of-life that contained sensitive data.
        It uses a Security Erase Unit command to write a predetermined pattern to the drive and resets the encryption key on the drive. The method may take up to two minutes to complete, so it is an asynchronous method.
        The GetAsyncResult method can be used to check on the status of the secure erase operation.
        <br/><br/>
        Use the "ListDrives" method to obtain the driveIDs for the drives you want to secure erase.
        :param drives: [required] List of driveIDs to secure erase.
        :type drives: int
        """

        connection_type = "Cluster"
        self._check_connection_type(connection_type)

        params = { 
            "drives": drives,
        }
        
        # There is no adaptor.
        return self.send_request(
            'SecureEraseDrives',
            AsyncHandleResult,
            params
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
        <br/><br/>
        When removing multiple drives, use a single "RemoveDrives" method call rather than multiple individual methods with a single drive each.
        This reduces the amount of data balancing that must occur to even stabilize the storage load on the cluster.
        <br/><br/>
        You can also remove drives with a "failed" status using "RemoveDrives".
        When you remove a drive with a "failed" status it is not returned to an "available" or "active" status.
        The drive is unavailable for use in the cluster.
        <br/><br/>
        Use the "ListDrives" method to obtain the driveIDs for the drives you want to remove.
        :param drives: [required] List of driveIDs to remove from the cluster.
        :type drives: int
        """

        connection_type = "Cluster"
        self._check_connection_type(connection_type)

        params = { 
            "drives": drives,
        }
        
        # There is no adaptor.
        return self.send_request(
            'RemoveDrives',
            AsyncHandleResult,
            params
        )

    def get_feature_status(
            self,
            feature=OPTIONAL,):
        """
        GetFeatureStatus allows you to retrieve the status of a cluster feature.
        :param feature:  [&#x27;Valid values: vvols: Find the status of the Virtual Volumes (VVOLs) cluster feature.&#x27;]
        :type feature: str
        """

        connection_type = "Cluster"
        self._check_connection_type(connection_type)

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

    def enable_feature(
            self,
            feature,):
        """
        EnableFeature allows you to enable cluster features that are disabled by default.
        :param feature: [required] [&#x27;Valid values: vvols: Enable the Virtual Volumes (VVOLs) cluster feature.&#x27;]
        :type feature: str
        """

        connection_type = "Cluster"
        self._check_connection_type(connection_type)

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

    def list_fibre_channel_port_info(
            self,):
        """
        The ListFibreChannelPortInfo is used to return information about the Fibre Channel ports. The API method is intended for use on individual nodes; userid and password is required for access to individual Fibre Channel nodes. However, this method can be used on the cluster if the force=true parameter is included in the method call. When used on the cluster, all Fibre Channel interfaces are listed."""

        connection_type = "Cluster"
        self._check_connection_type(connection_type)

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'ListFibreChannelPortInfo',
            ListFibreChannelPortInfoResult,
            params,
            since=8.0
        )

    def list_node_fibre_channel_port_info(
            self,
            force=OPTIONAL,):
        """
        The ListNodeFibreChannelPortInfo is used to return information about the Fibre Channel ports. The API method is intended for use on individual nodes; userid and password is required for access to individual Fibre Channel nodes. However, this method can be used on the cluster if the force=true parameter is included in the method call. When used on the cluster, all Fibre Channel interfaces are listed.
        :param force:  Specify force=true to call method on all member nodes of the cluster.
        :type force: bool
        """

        connection_type = "Node"
        self._check_connection_type(connection_type)

        params = { 
        }
        if force is not None:
            params["force"] = force
        
        # There is no adaptor.
        return self.send_request(
            'ListNodeFibreChannelPortInfo',
            ListNodeFibreChannelPortInfoResult,
            params,
            since=7.0
        )

    def list_fibre_channel_sessions(
            self,):
        """
        The ListFibreChannelSessions is used to return information about the active Fibre Channel sessions on a cluster."""

        connection_type = "Cluster"
        self._check_connection_type(connection_type)

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'ListFibreChannelSessions',
            ListFibreChannelSessionsResult,
            params,
            since=7.0
        )

    def get_cluster_hardware_info(
            self,
            type=OPTIONAL,):
        """
        You can use the GetClusterHardwareInfo method to retrieve the hardware status and information for all Fibre Channel nodes, iSCSI nodes and drives in the cluster. This generally includes manufacturers, vendors, versions, and other associated hardware identification information.
        :param type:  Include only a certain type of hardware information in the response. Can be one of the following:drives: List only drive information in the response.nodes: List only node information in the response.all: Include both drive and node information in the response.If this parameter is omitted, a type of &quot;all&quot; is assumed.
        :type type: str
        """

        connection_type = "Cluster"
        self._check_connection_type(connection_type)

        params = { 
        }
        if type is not None:
            params["type"] = type
        
        # There is no adaptor.
        return self.send_request(
            'GetClusterHardwareInfo',
            GetClusterHardwareInfoResult,
            params
        )

    def get_hardware_config(
            self,):
        """
        GetHardwareConfig enables you to display the hardware configuration information for a node. NOTE: This method is available only through the per-node API endpoint 5.0 or later."""

        connection_type = "Node"
        self._check_connection_type(connection_type)

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'GetHardwareConfig',
            GetHardwareConfigResult,
            params
        )

    def get_node_hardware_info(
            self,
            node_id,):
        """
        GetNodeHardwareInfo is used to return all the hardware info and status for the node specified. This generally includes manufacturers, vendors, versions, and other associated hardware identification information.
        :param nodeID: [required] The ID of the node for which hardware information is being requested.  Information about a  node is returned if a   node is specified.
        :type nodeID: int
        """

        connection_type = "Cluster"
        self._check_connection_type(connection_type)

        params = { 
            "nodeID": node_id,
        }
        
        # There is no adaptor.
        return self.send_request(
            'GetNodeHardwareInfo',
            GetNodeHardwareInfoResult,
            params
        )

    def get_nvram_info(
            self,):
        """
        GetNvramInfo allows you to retrieve information from each node about the NVRAM card.  """

        connection_type = "Node"
        self._check_connection_type(connection_type)

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'GetNvramInfo',
            GetNvramInfoResult,
            params
        )

    def create_initiators(
            self,
            initiators,):
        """
        CreateInitiators enables you to create multiple new initiator IQNs or World Wide Port Names (WWPNs) and optionally assign them aliases and attributes. When you use CreateInitiators to create new initiators, you can also add them to volume access groups.
        If CreateInitiators fails to create one of the initiators provided in the parameter, the method returns an error and does not create any initiators (no partial completion is possible).
        :param initiators: [required] [&#x27;A list of Initiator objects containing characteristics of each new initiator&#x27;]
        :type initiators: CreateInitiator
        """

        connection_type = "Cluster"
        self._check_connection_type(connection_type)

        params = { 
            "initiators": initiators,
        }
        
        # There is no adaptor.
        return self.send_request(
            'CreateInitiators',
            CreateInitiatorsResult,
            params
        )

    def modify_initiators(
            self,
            initiators,):
        """
        ModifyInitiators enables you to change the attributes of an existing initiator. You cannot change the name of an existing initiator. If you need to change the name of an initiator, delete the existing initiator with DeleteInitiators and create a new one with CreateInitiators.
        If ModifyInitiators fails to change one of the initiators provided in the parameter, the method returns an error and does not create any initiators (no partial completion is possible).
        :param initiators: [required] [&#x27;A list of Initiator objects containing characteristics of each initiator to modify.&#x27;]
        :type initiators: ModifyInitiator
        """

        connection_type = "Cluster"
        self._check_connection_type(connection_type)

        params = { 
            "initiators": initiators,
        }
        
        # There is no adaptor.
        return self.send_request(
            'ModifyInitiators',
            ModifyInitiatorsResult,
            params
        )

    def delete_initiators(
            self,
            initiators,):
        """
        DeleteInitiators enables you to delete one or more initiators from the system (and from any associated volumes or volume access groups).
        If DeleteInitiators fails to delete one of the initiators provided in the parameter, the system returns an error and does not delete any initiators (no partial completion is possible).
        :param initiators: [required] [&#x27;An array of IDs of initiators to delete.&#x27;]
        :type initiators: int
        """

        connection_type = "Cluster"
        self._check_connection_type(connection_type)

        params = { 
            "initiators": initiators,
        }
        
        # There is no adaptor.
        return self.send_request(
            'DeleteInitiators',
            DeleteInitiatorsResult,
            params
        )

    def list_initiators(
            self,
            start_initiator_id=OPTIONAL,
            limit=OPTIONAL,
            initiators=OPTIONAL,):
        """
        ListInitiators enables you to list initiator IQNs or World Wide Port Names (WWPNs).
        :param startInitiatorID:  The initiator ID at which to begin the listing. You can supply this parameter or the &quot;initiators&quot; parameter, but not both.
        :type startInitiatorID: int
        
        :param limit:  The maximum number of initiator objects to return.
        :type limit: int
        
        :param initiators:  A list of initiator IDs to retrieve. You can supply this parameter or the &quot;startInitiatorID&quot; parameter, but not both.
        :type initiators: int
        """

        connection_type = "Cluster"
        self._check_connection_type(connection_type)

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
            params
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
        
        :param parameters:  [&#x27;An object, normally a dictionary or hashtable of the key/value pairs, to be passed as the params for the method being invoked.&#x27;]
        :type parameters: dict
        """

        connection_type = "Both"
        self._check_connection_type(connection_type)

        params = { 
            "method": method,
        }
        if parameters is not None:
            params["parameters"] = parameters
        
        # There is an adaptor!
        since = None
        deprecated = None

        return ElementServiceAdaptor.invoke_sfapi(self, params,
                                                  since, deprecated)

    def add_ldap_cluster_admin(
            self,
            username,
            access,
            accept_eula=OPTIONAL,
            attributes=OPTIONAL,):
        """
        AddLdapClusterAdmin is used to add a new LDAP Cluster Admin. An LDAP Cluster Admin can be used to manage the cluster via the API and management tools. LDAP Cluster Admins are completely separate and unrelated to standard tenant accounts.
        <br/><br/>
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

        connection_type = "Cluster"
        self._check_connection_type(connection_type)

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

        connection_type = "Cluster"
        self._check_connection_type(connection_type)

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
            since=8.0
        )

    def get_ldap_configuration(
            self,):
        """
        The GetLdapConfiguration is used to get the LDAP configuration currently active on the cluster."""

        connection_type = "Cluster"
        self._check_connection_type(connection_type)

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'GetLdapConfiguration',
            GetLdapConfigurationResult,
            params,
            since=8.0
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
        :param authType:  [&#x27;Identifies which user authentcation method will be used. &lt;br/&gt;&#x27;, &#x27;Must be one of the following:&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;DirectBind&lt;/b&gt;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;SearchAndBind&lt;/b&gt; (default)&#x27;][&#x27;Identifies which user authentcation method will be used. &lt;br/&gt;&#x27;, &#x27;Must be one of the following:&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;DirectBind&lt;/b&gt;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;SearchAndBind&lt;/b&gt; (default)&#x27;][&#x27;Identifies which user authentcation method will be used. &lt;br/&gt;&#x27;, &#x27;Must be one of the following:&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;DirectBind&lt;/b&gt;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;SearchAndBind&lt;/b&gt; (default)&#x27;][&#x27;Identifies which user authentcation method will be used. &lt;br/&gt;&#x27;, &#x27;Must be one of the following:&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;DirectBind&lt;/b&gt;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;SearchAndBind&lt;/b&gt; (default)&#x27;]
        :type authType: str
        
        :param groupSearchBaseDN:  [&#x27;The base DN of the tree to start the group search (will do a subtree search from here).&#x27;]
        :type groupSearchBaseDN: str
        
        :param groupSearchCustomFilter:  [&#x27;REQUIRED for CustomFilter&lt;br/&gt;&#x27;, &quot;For use with the CustomFilter search type, an LDAP filter to use to return the DNs of a user&#x27;s groups.&lt;br/&gt;&quot;, &#x27;The string can have placeholder text of %USERNAME% and %USERDN% to be replaced with their username and full userDN as needed.&#x27;][&#x27;REQUIRED for CustomFilter&lt;br/&gt;&#x27;, &quot;For use with the CustomFilter search type, an LDAP filter to use to return the DNs of a user&#x27;s groups.&lt;br/&gt;&quot;, &#x27;The string can have placeholder text of %USERNAME% and %USERDN% to be replaced with their username and full userDN as needed.&#x27;][&#x27;REQUIRED for CustomFilter&lt;br/&gt;&#x27;, &quot;For use with the CustomFilter search type, an LDAP filter to use to return the DNs of a user&#x27;s groups.&lt;br/&gt;&quot;, &#x27;The string can have placeholder text of %USERNAME% and %USERDN% to be replaced with their username and full userDN as needed.&#x27;]
        :type groupSearchCustomFilter: str
        
        :param groupSearchType:  [&#x27;Controls the default group search filter used, can be one of the following:&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;NoGroups&lt;/b&gt;: No group support.&lt;br/&gt;&#x27;, &quot;&lt;b&gt;ActiveDirectory&lt;/b&gt;: (default) Nested membership of all of a user&#x27;s AD groups.&lt;br/&gt;&quot;, &#x27;&lt;b&gt;MemberDN&lt;/b&gt;: MemberDN style groups (single-level).&#x27;][&#x27;Controls the default group search filter used, can be one of the following:&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;NoGroups&lt;/b&gt;: No group support.&lt;br/&gt;&#x27;, &quot;&lt;b&gt;ActiveDirectory&lt;/b&gt;: (default) Nested membership of all of a user&#x27;s AD groups.&lt;br/&gt;&quot;, &#x27;&lt;b&gt;MemberDN&lt;/b&gt;: MemberDN style groups (single-level).&#x27;][&#x27;Controls the default group search filter used, can be one of the following:&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;NoGroups&lt;/b&gt;: No group support.&lt;br/&gt;&#x27;, &quot;&lt;b&gt;ActiveDirectory&lt;/b&gt;: (default) Nested membership of all of a user&#x27;s AD groups.&lt;br/&gt;&quot;, &#x27;&lt;b&gt;MemberDN&lt;/b&gt;: MemberDN style groups (single-level).&#x27;][&#x27;Controls the default group search filter used, can be one of the following:&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;NoGroups&lt;/b&gt;: No group support.&lt;br/&gt;&#x27;, &quot;&lt;b&gt;ActiveDirectory&lt;/b&gt;: (default) Nested membership of all of a user&#x27;s AD groups.&lt;br/&gt;&quot;, &#x27;&lt;b&gt;MemberDN&lt;/b&gt;: MemberDN style groups (single-level).&#x27;]
        :type groupSearchType: str
        
        :param searchBindDN:  [&#x27;REQUIRED for SearchAndBind&lt;br/&gt;&#x27;, &#x27;A fully qualified DN to log in with to perform an LDAP search for the user (needs read access to the LDAP directory).&#x27;][&#x27;REQUIRED for SearchAndBind&lt;br/&gt;&#x27;, &#x27;A fully qualified DN to log in with to perform an LDAP search for the user (needs read access to the LDAP directory).&#x27;]
        :type searchBindDN: str
        
        :param searchBindPassword:  [&#x27;REQUIRED for SearchAndBind&lt;br/&gt;&#x27;, &#x27;The password for the searchBindDN account used for searching.&#x27;][&#x27;REQUIRED for SearchAndBind&lt;br/&gt;&#x27;, &#x27;The password for the searchBindDN account used for searching.&#x27;]
        :type searchBindPassword: str
        
        :param serverURIs: [required] [&#x27;A list of LDAP server URIs (examples: &quot;ldap://1.2.3.4&quot; and ldaps://1.2.3.4:123&quot;)&#x27;]
        :type serverURIs: str
        
        :param userDNTemplate:  [&#x27;REQUIRED for DirectBind&lt;br/&gt;&#x27;, &#x27;A string that is used to form a fully qualified user DN.&lt;br/&gt;&#x27;, &#x27;The string should have the placeholder text &quot;%USERNAME%&quot; which will be replaced with the username of the authenticating user.&#x27;][&#x27;REQUIRED for DirectBind&lt;br/&gt;&#x27;, &#x27;A string that is used to form a fully qualified user DN.&lt;br/&gt;&#x27;, &#x27;The string should have the placeholder text &quot;%USERNAME%&quot; which will be replaced with the username of the authenticating user.&#x27;][&#x27;REQUIRED for DirectBind&lt;br/&gt;&#x27;, &#x27;A string that is used to form a fully qualified user DN.&lt;br/&gt;&#x27;, &#x27;The string should have the placeholder text &quot;%USERNAME%&quot; which will be replaced with the username of the authenticating user.&#x27;]
        :type userDNTemplate: str
        
        :param userSearchBaseDN:  [&#x27;REQUIRED for SearchAndBind&#x27;, &#x27;The base DN of the tree used to start the search (will do a subtree search from here).&#x27;][&#x27;REQUIRED for SearchAndBind&#x27;, &#x27;The base DN of the tree used to start the search (will do a subtree search from here).&#x27;]
        :type userSearchBaseDN: str
        
        :param userSearchFilter:  [&#x27;REQUIRED for SearchAndBind.&lt;br/&gt;&#x27;, &#x27;The LDAP filter to use.&lt;br/&gt;&#x27;, &#x27;The string should have the placeholder text &quot;%USERNAME%&quot; which will be replaced with the username of the authenticating user.&lt;br/&gt;&#x27;, &#x27;Example: (&amp;(objectClass=person) (sAMAccountName=%USERNAME%)) will use the sAMAccountName field in Active Directory to match the nusername entered at cluster login.&#x27;][&#x27;REQUIRED for SearchAndBind.&lt;br/&gt;&#x27;, &#x27;The LDAP filter to use.&lt;br/&gt;&#x27;, &#x27;The string should have the placeholder text &quot;%USERNAME%&quot; which will be replaced with the username of the authenticating user.&lt;br/&gt;&#x27;, &#x27;Example: (&amp;(objectClass=person) (sAMAccountName=%USERNAME%)) will use the sAMAccountName field in Active Directory to match the nusername entered at cluster login.&#x27;][&#x27;REQUIRED for SearchAndBind.&lt;br/&gt;&#x27;, &#x27;The LDAP filter to use.&lt;br/&gt;&#x27;, &#x27;The string should have the placeholder text &quot;%USERNAME%&quot; which will be replaced with the username of the authenticating user.&lt;br/&gt;&#x27;, &#x27;Example: (&amp;(objectClass=person) (sAMAccountName=%USERNAME%)) will use the sAMAccountName field in Active Directory to match the nusername entered at cluster login.&#x27;][&#x27;REQUIRED for SearchAndBind.&lt;br/&gt;&#x27;, &#x27;The LDAP filter to use.&lt;br/&gt;&#x27;, &#x27;The string should have the placeholder text &quot;%USERNAME%&quot; which will be replaced with the username of the authenticating user.&lt;br/&gt;&#x27;, &#x27;Example: (&amp;(objectClass=person) (sAMAccountName=%USERNAME%)) will use the sAMAccountName field in Active Directory to match the nusername entered at cluster login.&#x27;]
        :type userSearchFilter: str
        """

        connection_type = "Cluster"
        self._check_connection_type(connection_type)

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
            since=8.0
        )

    def disable_ldap_authentication(
            self,):
        """
        The DisableLdapAuthentication method is used disable LDAP authentication and remove all LDAP configuration settings. This call will not remove any configured cluster admin accounts (user or group). However, those cluster admin accounts will no longer be able to log in."""

        connection_type = "Cluster"
        self._check_connection_type(connection_type)

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'DisableLdapAuthentication',
            DisableLdapAuthenticationResult,
            params,
            since=8.0
        )

    def list_active_nodes(
            self,):
        """
        ListActiveNodes returns the list of currently active nodes that are in the cluster."""

        connection_type = "Cluster"
        self._check_connection_type(connection_type)

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'ListActiveNodes',
            ListActiveNodesResult,
            params
        )

    def list_all_nodes(
            self,):
        """
        ListAllNodes enables you to retrieve a list of active and pending nodes in the cluster."""

        connection_type = "Cluster"
        self._check_connection_type(connection_type)

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'ListAllNodes',
            ListAllNodesResult,
            params
        )

    def list_pending_nodes(
            self,):
        """
        Gets the list of pending nodes.
        Pending nodes are running and configured to join the cluster, but have not been added via the AddNodes method."""

        connection_type = "Cluster"
        self._check_connection_type(connection_type)

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'ListPendingNodes',
            ListPendingNodesResult,
            params
        )

    def add_nodes(
            self,
            pending_nodes,):
        """
        AddNodes is used to add one or more new nodes to the cluster. When a node is not configured and starts up for the first time you are prompted to configure the node. Once a node is configured it is registered as a "pending node" with the cluster.
        <br/><br/>
        Adding a node to a cluster that has been set up for virtual networking will require a sufficient number of virtual storage IP addresses to allocate a virtual IP to the new node. If there are no virtual IP addresses available for the new node, the AddNode operation will not complete successfully. Use the "ModifyVirtualNetwork" method to add more storage IP addresses to your virtual network.
        <br/><br/>
        The software version on each node in a cluster must be compatible. Run the "ListAllNodes" API to see what versions of software are currently running on the cluster nodes. For an explanation of software version compatibility, see "Node Versioning and Compatibility" in the Element API guide.
        <br/><br/>
        Once a node has been added, the drives on the node are made available and can then be added via the "AddDrives" method to increase the storage capacity of the cluster.
        <br/><br/>
        <b>Note</b>: It may take several seconds after adding a new Node for it to start up and register the drives as being available.
        :param pendingNodes: [required] List of PendingNodeIDs for the Nodes to be added. You can obtain the list of Pending Nodes via the ListPendingNodes method.
        :type pendingNodes: int
        """

        connection_type = "Cluster"
        self._check_connection_type(connection_type)

        params = { 
            "pendingNodes": pending_nodes,
        }
        
        # There is no adaptor.
        return self.send_request(
            'AddNodes',
            AddNodesResult,
            params
        )

    def remove_nodes(
            self,
            nodes,):
        """
        RemoveNodes is used to remove one or more nodes that should no longer participate in the cluster. Before removing a node, all drives it contains must first be removed with "RemoveDrives" method. A node cannot be removed until the RemoveDrives process has completed and all data has been migrated away from the node.
        <br/><br/>
        Once removed, a node registers itself as a pending node and can be added again, or shut down which removes it from the "Pending Node" list.
        :param nodes: [required] List of NodeIDs for the nodes to be removed.
        :type nodes: int
        """

        connection_type = "Cluster"
        self._check_connection_type(connection_type)

        params = { 
            "nodes": nodes,
        }
        
        # There is no adaptor.
        return self.send_request(
            'RemoveNodes',
            RemoveNodesResult,
            params
        )

    def get_network_config(
            self,):
        """
        The GetNetworkConfig API method is used to display the network configuration information for a node.
        <br/><br/>
        <b>Note</b>: This method is available only through the per-node API endpoint 5.0 or later."""

        connection_type = "Node"
        self._check_connection_type(connection_type)

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'GetNetworkConfig',
            GetNetworkConfigResult,
            params
        )

    def set_config(
            self,
            config,):
        """
        The SetConfig API method is used to set all the configuration information for the node. This includes the same information available via calls to SetClusterConfig and SetNetworkConfig in one API method.
        <br/><br/>
        <b>Warning!</b> Changing the 'bond-mode' on a node can cause a temporary loss of network connectivity. Caution should be taken when using this method.
        <br/><br/>
        <b>Note</b>: This method is available only through the per-node API endpoint 5.0 or later.
        :param config: [required] Objects that you want changed for the cluster interface settings.
        :type config: Config
        """

        connection_type = "Node"
        self._check_connection_type(connection_type)

        params = { 
            "config": config,
        }
        
        # There is no adaptor.
        return self.send_request(
            'SetConfig',
            SetConfigResult,
            params
        )

    def set_network_config(
            self,
            network,):
        """
        The "SetNetworkConfig" method is used to set the network configuration for a node. To see the states in which these objects can be modified, see "Network Object for 1G and 10G Interfaces" on page 109 of the Element API. To display the current network settings for a node, run the "GetNetworkConfig" method.
        <br/><br/>
        <b>WARNING!</b> Changing the "bond-mode" on a node can cause a temporary loss of network connectivity. Caution should be taken when using this method.
        <br/><br/>
        <b>Note</b>: This method is available only through the per-node API endpoint 5.0 or later.
        :param network: [required] Objects that will be changed for the node network settings.
        :type network: Network
        """

        connection_type = "Node"
        self._check_connection_type(connection_type)

        params = { 
            "network": network,
        }
        
        # There is no adaptor.
        return self.send_request(
            'SetNetworkConfig',
            SetNetworkConfigResult,
            params
        )

    def get_config(
            self,):
        """
        The GetConfig API method is used to retrieve all the configuration information for the node. This one API method includes the same information available in both "GetClusterConfig" and "GetNetworkConfig" methods.
        <br/><br/>
        <b>Note</b>: This method is available only through the per-node API endpoint 5.0 or later."""

        connection_type = "Both"
        self._check_connection_type(connection_type)

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'GetConfig',
            GetConfigResult,
            params
        )

    def get_node_stats(
            self,
            node_id,):
        """
        GetNodeStats is used to return the high-level activity measurements for a single node.
        :param nodeID: [required] Specifies the node for which statistics are gathered.
        :type nodeID: int
        """

        connection_type = "Cluster"
        self._check_connection_type(connection_type)

        params = { 
            "nodeID": node_id,
        }
        
        # There is an adaptor!
        since = None
        deprecated = None

        return ElementServiceAdaptor.get_node_stats(self, params,
                                                  since, deprecated)

    def list_node_stats(
            self,):
        """
        ListNodeStats is used to return the high-level activity measurements for all nodes in a cluster."""

        connection_type = "Cluster"
        self._check_connection_type(connection_type)

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'ListNodeStats',
            ListNodeStatsResult,
            params
        )

    def list_cluster_pairs(
            self,):
        """
        ListClusterPairs is used to list all of the clusters a cluster is paired with.
        This method returns information about active and pending cluster pairings, such as statistics about the current pairing as well as the connectivity and latency (in milliseconds) of the cluster pairing."""

        connection_type = "Cluster"
        self._check_connection_type(connection_type)

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'ListClusterPairs',
            ListClusterPairsResult,
            params
        )

    def list_active_paired_volumes(
            self,):
        """
        ListActivePairedVolumes is used to list all of the active volumes paired with a volume.
        Volumes listed in the return for this method include volumes with active and pending pairings."""

        connection_type = "Cluster"
        self._check_connection_type(connection_type)

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'ListActivePairedVolumes',
            ListActivePairedVolumesResult,
            params
        )

    def start_cluster_pairing(
            self,):
        """
        StartClusterPairing is used to create an encoded key from a cluster that is used to pair with another cluster.
        The key created from this API method is used in the "CompleteClusterPairing" API method to establish a cluster pairing.
        You can pair a cluster with a maximum of four other SolidFire clusters."""

        connection_type = "Cluster"
        self._check_connection_type(connection_type)

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'StartClusterPairing',
            StartClusterPairingResult,
            params
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
        
        :param mode:  [&#x27;The mode of the volume on which to start the pairing process. The mode can only be set if the volume is the source volume.&lt;br/&gt;&#x27;, &#x27;Possible values:&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Async&lt;/b&gt;: (default if no mode parameter specified) Writes are acknowledged when they complete locally. The cluster does not wait for writes to be replicated to the target cluster.&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Sync&lt;/b&gt;: Source acknowledges write when the data is stored locally and on the remote cluster.&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;SnapshotsOnly&lt;/b&gt;: Only snapshots created on the source cluster will be replicated. Active writes from the source volume will not be replicated.&lt;br/&gt;&#x27;][&#x27;The mode of the volume on which to start the pairing process. The mode can only be set if the volume is the source volume.&lt;br/&gt;&#x27;, &#x27;Possible values:&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Async&lt;/b&gt;: (default if no mode parameter specified) Writes are acknowledged when they complete locally. The cluster does not wait for writes to be replicated to the target cluster.&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Sync&lt;/b&gt;: Source acknowledges write when the data is stored locally and on the remote cluster.&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;SnapshotsOnly&lt;/b&gt;: Only snapshots created on the source cluster will be replicated. Active writes from the source volume will not be replicated.&lt;br/&gt;&#x27;][&#x27;The mode of the volume on which to start the pairing process. The mode can only be set if the volume is the source volume.&lt;br/&gt;&#x27;, &#x27;Possible values:&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Async&lt;/b&gt;: (default if no mode parameter specified) Writes are acknowledged when they complete locally. The cluster does not wait for writes to be replicated to the target cluster.&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Sync&lt;/b&gt;: Source acknowledges write when the data is stored locally and on the remote cluster.&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;SnapshotsOnly&lt;/b&gt;: Only snapshots created on the source cluster will be replicated. Active writes from the source volume will not be replicated.&lt;br/&gt;&#x27;][&#x27;The mode of the volume on which to start the pairing process. The mode can only be set if the volume is the source volume.&lt;br/&gt;&#x27;, &#x27;Possible values:&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Async&lt;/b&gt;: (default if no mode parameter specified) Writes are acknowledged when they complete locally. The cluster does not wait for writes to be replicated to the target cluster.&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Sync&lt;/b&gt;: Source acknowledges write when the data is stored locally and on the remote cluster.&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;SnapshotsOnly&lt;/b&gt;: Only snapshots created on the source cluster will be replicated. Active writes from the source volume will not be replicated.&lt;br/&gt;&#x27;][&#x27;The mode of the volume on which to start the pairing process. The mode can only be set if the volume is the source volume.&lt;br/&gt;&#x27;, &#x27;Possible values:&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Async&lt;/b&gt;: (default if no mode parameter specified) Writes are acknowledged when they complete locally. The cluster does not wait for writes to be replicated to the target cluster.&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Sync&lt;/b&gt;: Source acknowledges write when the data is stored locally and on the remote cluster.&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;SnapshotsOnly&lt;/b&gt;: Only snapshots created on the source cluster will be replicated. Active writes from the source volume will not be replicated.&lt;br/&gt;&#x27;]
        :type mode: str
        """

        connection_type = "Cluster"
        self._check_connection_type(connection_type)

        params = { 
            "volumeID": volume_id,
        }
        if mode is not None:
            params["mode"] = mode
        
        # There is no adaptor.
        return self.send_request(
            'StartVolumePairing',
            StartVolumePairingResult,
            params
        )

    def complete_cluster_pairing(
            self,
            cluster_pairing_key,):
        """
        The CompleteClusterPairing method is the second step in the cluster pairing process.
        Use this method with the encoded key received from the "StartClusterPairing" API method to complete the cluster pairing process.
        :param clusterPairingKey: [required] A string of characters that is returned from the &quot;StartClusterPairing&quot; API method.
        :type clusterPairingKey: str
        """

        connection_type = "Cluster"
        self._check_connection_type(connection_type)

        params = { 
            "clusterPairingKey": cluster_pairing_key,
        }
        
        # There is no adaptor.
        return self.send_request(
            'CompleteClusterPairing',
            CompleteClusterPairingResult,
            params
        )

    def complete_volume_pairing(
            self,
            volume_pairing_key,
            volume_id,):
        """
        CompleteVolumePairing is used to complete the pairing of two volumes.
        :param volumePairingKey: [required] The key returned from the &quot;StartVolumePairing&quot; API method.
        :type volumePairingKey: str
        
        :param volumeID: [required] The ID of volume on which to complete the pairing process.
        :type volumeID: int
        """

        connection_type = "Cluster"
        self._check_connection_type(connection_type)

        params = { 
            "volumePairingKey": volume_pairing_key,
            "volumeID": volume_id,
        }
        
        # There is no adaptor.
        return self.send_request(
            'CompleteVolumePairing',
            CompleteVolumePairingResult,
            params
        )

    def remove_cluster_pair(
            self,
            cluster_pair_id,):
        """
        You can use the RemoveClusterPair method to close the open connections between two paired clusters.<br/>
        <b>Note</b>: Before you remove a cluster pair, you must first remove all volume pairing to the clusters with the "RemoveVolumePair" API method.
        :param clusterPairID: [required] Unique identifier used to pair two clusters.
        :type clusterPairID: int
        """

        connection_type = "Cluster"
        self._check_connection_type(connection_type)

        params = { 
            "clusterPairID": cluster_pair_id,
        }
        
        # There is no adaptor.
        return self.send_request(
            'RemoveClusterPair',
            RemoveClusterPairResult,
            params
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

        connection_type = "Cluster"
        self._check_connection_type(connection_type)

        params = { 
            "volumeID": volume_id,
        }
        
        # There is no adaptor.
        return self.send_request(
            'RemoveVolumePair',
            RemoveVolumePairResult,
            params
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
        
        :param pausedManual:  [&#x27;Valid values that can be entered:&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;true&lt;/b&gt;: to pause volume replication.&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;false&lt;/b&gt;: to restart volume replication.&lt;br/&gt;&#x27;, &#x27;If no value is specified, no change in replication is performed.&#x27;][&#x27;Valid values that can be entered:&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;true&lt;/b&gt;: to pause volume replication.&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;false&lt;/b&gt;: to restart volume replication.&lt;br/&gt;&#x27;, &#x27;If no value is specified, no change in replication is performed.&#x27;][&#x27;Valid values that can be entered:&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;true&lt;/b&gt;: to pause volume replication.&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;false&lt;/b&gt;: to restart volume replication.&lt;br/&gt;&#x27;, &#x27;If no value is specified, no change in replication is performed.&#x27;][&#x27;Valid values that can be entered:&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;true&lt;/b&gt;: to pause volume replication.&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;false&lt;/b&gt;: to restart volume replication.&lt;br/&gt;&#x27;, &#x27;If no value is specified, no change in replication is performed.&#x27;]
        :type pausedManual: bool
        
        :param mode:  [&#x27;Volume replication mode.&lt;br/&gt;&#x27;, &#x27;Possible values:&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Async&lt;/b&gt;: Writes are acknowledged when they complete locally. The cluster does not wait for writes to be replicated to the target cluster.&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Sync&lt;/b&gt;: The source acknowledges the write when the data is stored locally and on the remote cluster.&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;SnapshotsOnly&lt;/b&gt;: Only snapshots created on the source cluster will be replicated. Active writes from the source volume are not replicated.&lt;br/&gt;&#x27;][&#x27;Volume replication mode.&lt;br/&gt;&#x27;, &#x27;Possible values:&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Async&lt;/b&gt;: Writes are acknowledged when they complete locally. The cluster does not wait for writes to be replicated to the target cluster.&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Sync&lt;/b&gt;: The source acknowledges the write when the data is stored locally and on the remote cluster.&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;SnapshotsOnly&lt;/b&gt;: Only snapshots created on the source cluster will be replicated. Active writes from the source volume are not replicated.&lt;br/&gt;&#x27;][&#x27;Volume replication mode.&lt;br/&gt;&#x27;, &#x27;Possible values:&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Async&lt;/b&gt;: Writes are acknowledged when they complete locally. The cluster does not wait for writes to be replicated to the target cluster.&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Sync&lt;/b&gt;: The source acknowledges the write when the data is stored locally and on the remote cluster.&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;SnapshotsOnly&lt;/b&gt;: Only snapshots created on the source cluster will be replicated. Active writes from the source volume are not replicated.&lt;br/&gt;&#x27;][&#x27;Volume replication mode.&lt;br/&gt;&#x27;, &#x27;Possible values:&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Async&lt;/b&gt;: Writes are acknowledged when they complete locally. The cluster does not wait for writes to be replicated to the target cluster.&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Sync&lt;/b&gt;: The source acknowledges the write when the data is stored locally and on the remote cluster.&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;SnapshotsOnly&lt;/b&gt;: Only snapshots created on the source cluster will be replicated. Active writes from the source volume are not replicated.&lt;br/&gt;&#x27;][&#x27;Volume replication mode.&lt;br/&gt;&#x27;, &#x27;Possible values:&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Async&lt;/b&gt;: Writes are acknowledged when they complete locally. The cluster does not wait for writes to be replicated to the target cluster.&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Sync&lt;/b&gt;: The source acknowledges the write when the data is stored locally and on the remote cluster.&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;SnapshotsOnly&lt;/b&gt;: Only snapshots created on the source cluster will be replicated. Active writes from the source volume are not replicated.&lt;br/&gt;&#x27;]
        :type mode: str
        """

        connection_type = "Cluster"
        self._check_connection_type(connection_type)

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
            params
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
        CreateSnapshot is used to create a point-in-time copy of a volume.
        A snapshot can be created from any volume or from an existing snapshot.
        <br/><br/>
        <b>Note</b>: Creating a snapshot is allowed if cluster fullness is at stage 2 or 3.
        Snapshots are not created when cluster fullness is at stage 4 or 5.
        :param volumeID: [required] ID of the volume image from which to copy.
        :type volumeID: int
        
        :param snapshotID:  [&#x27;Unique ID of a snapshot from which the new snapshot is made.&#x27;, &#x27;The snapshotID passed must be a snapshot on the given volume.&#x27;, &quot;If a SnapshotID is not provided, a snapshot is created from the volume&#x27;s active branch.&quot;][&#x27;Unique ID of a snapshot from which the new snapshot is made.&#x27;, &#x27;The snapshotID passed must be a snapshot on the given volume.&#x27;, &quot;If a SnapshotID is not provided, a snapshot is created from the volume&#x27;s active branch.&quot;][&#x27;Unique ID of a snapshot from which the new snapshot is made.&#x27;, &#x27;The snapshotID passed must be a snapshot on the given volume.&#x27;, &quot;If a SnapshotID is not provided, a snapshot is created from the volume&#x27;s active branch.&quot;]
        :type snapshotID: int
        
        :param name:  [&#x27;A name for the snapshot.&#x27;, &#x27;If no name is provided, the date and time the snapshot was taken is used.&#x27;][&#x27;A name for the snapshot.&#x27;, &#x27;If no name is provided, the date and time the snapshot was taken is used.&#x27;]
        :type name: str
        
        :param enableRemoteReplication:  Identifies if snapshot is enabled for remote replication.
        :type enableRemoteReplication: bool
        
        :param retention:  [&#x27;The amount of time the snapshot will be retained. Enter in HH:mm:ss&#x27;]
        :type retention: str
        
        :param attributes:  List of Name/Value pairs in JSON object format.
        :type attributes: dict
        """

        connection_type = "Cluster"
        self._check_connection_type(connection_type)

        params = { 
            "volumeID": volume_id,
        }
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
        
        # There is no adaptor.
        return self.send_request(
            'CreateSnapshot',
            CreateSnapshotResult,
            params
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

        connection_type = "Cluster"
        self._check_connection_type(connection_type)

        params = { 
            "snapshotID": snapshot_id,
        }
        
        # There is no adaptor.
        return self.send_request(
            'DeleteSnapshot',
            DeleteSnapshotResult,
            params
        )

    def list_snapshots(
            self,
            volume_id=OPTIONAL,):
        """
        ListSnapshots is used to return the attributes of each snapshot taken on the volume.
        :param volumeID:  [&#x27;The volume to list snapshots for.&#x27;, &#x27;If not provided, all snapshots for all volumes are returned.&#x27;][&#x27;The volume to list snapshots for.&#x27;, &#x27;If not provided, all snapshots for all volumes are returned.&#x27;]
        :type volumeID: int
        """

        connection_type = "Cluster"
        self._check_connection_type(connection_type)

        params = { 
        }
        if volume_id is not None:
            params["volumeID"] = volume_id
        
        # There is no adaptor.
        return self.send_request(
            'ListSnapshots',
            ListSnapshotsResult,
            params
        )

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
        
        :param enableRemoteReplication:  [&#x27;Use to enable the snapshot created to be replicated to a remote SolidFire cluster.&#x27;, &#x27;Possible values:&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;true&lt;/b&gt;: the snapshot will be replicated to remote storage.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;false&lt;/b&gt;: Default. No replication.&#x27;][&#x27;Use to enable the snapshot created to be replicated to a remote SolidFire cluster.&#x27;, &#x27;Possible values:&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;true&lt;/b&gt;: the snapshot will be replicated to remote storage.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;false&lt;/b&gt;: Default. No replication.&#x27;][&#x27;Use to enable the snapshot created to be replicated to a remote SolidFire cluster.&#x27;, &#x27;Possible values:&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;true&lt;/b&gt;: the snapshot will be replicated to remote storage.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;false&lt;/b&gt;: Default. No replication.&#x27;][&#x27;Use to enable the snapshot created to be replicated to a remote SolidFire cluster.&#x27;, &#x27;Possible values:&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;true&lt;/b&gt;: the snapshot will be replicated to remote storage.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;false&lt;/b&gt;: Default. No replication.&#x27;]
        :type enableRemoteReplication: bool
        """

        connection_type = "Cluster"
        self._check_connection_type(connection_type)

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
        <b>Note</b>: Creating a snapshot is allowed if cluster fullness is at stage 2 or 3.
        Snapshots are not created when cluster fullness is at stage 4 or 5.
        :param volumeID: [required] [&#x27;VolumeID for the volume.&#x27;]
        :type volumeID: int
        
        :param snapshotID: [required] [&#x27;ID of a previously created snapshot on the given volume.&#x27;]
        :type snapshotID: int
        
        :param saveCurrentState: [required] [&#x27;&lt;br/&gt;&lt;b&gt;true&lt;/b&gt;: The previous active volume image is kept.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;false&lt;/b&gt;: (default) The previous active volume image is deleted.&#x27;][&#x27;&lt;br/&gt;&lt;b&gt;true&lt;/b&gt;: The previous active volume image is kept.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;false&lt;/b&gt;: (default) The previous active volume image is deleted.&#x27;]
        :type saveCurrentState: bool
        
        :param name:  [&#x27;Name for the snapshot. If no name is given, then the name of the snapshot being rolled back to is used with &#x27;, &#x27;&quot;-copy&quot; appended to the end of the name.&#x27;][&#x27;Name for the snapshot. If no name is given, then the name of the snapshot being rolled back to is used with &#x27;, &#x27;&quot;-copy&quot; appended to the end of the name.&#x27;]
        :type name: str
        
        :param attributes:  [&#x27;List of Name/Value pairs in JSON object format&#x27;]
        :type attributes: dict
        """

        connection_type = "Cluster"
        self._check_connection_type(connection_type)

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
            params
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
        <br/><br/>
        <b>Note</b>: Creating a group snapshot is allowed if cluster fullness is at stage 2 or 3.
        Snapshots are not created when cluster fullness is at stage 4 or 5.
        :param volumes: [required] Unique ID of the volume image from which to copy.
        :type volumes: int
        
        :param name:  [&#x27;A name for the snapshot.&#x27;, &#x27;If no name is provided, the date and time the snapshot was taken is used.&#x27;][&#x27;A name for the snapshot.&#x27;, &#x27;If no name is provided, the date and time the snapshot was taken is used.&#x27;]
        :type name: str
        
        :param enableRemoteReplication:  Identifies if snapshot is enabled for remote replication.
        :type enableRemoteReplication: bool
        
        :param retention:  [&#x27;The amount of time the snapshot will be retained. Enter in HH:mm:ss&#x27;]
        :type retention: str
        
        :param attributes:  List of Name/Value pairs in JSON object format.
        :type attributes: dict
        """

        connection_type = "Cluster"
        self._check_connection_type(connection_type)

        params = { 
            "volumes": volumes,
        }
        if name is not None:
            params["name"] = name
        if enable_remote_replication is not None:
            params["enableRemoteReplication"] = enable_remote_replication
        if retention is not None:
            params["retention"] = retention
        if attributes is not None:
            params["attributes"] = attributes
        
        # There is no adaptor.
        return self.send_request(
            'CreateGroupSnapshot',
            CreateGroupSnapshotResult,
            params
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
        
        :param saveMembers: [required] [&#x27;&lt;br/&gt;&lt;b&gt;true&lt;/b&gt;: Snapshots are kept, but group association is removed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;false&lt;/b&gt;: The group and snapshots are deleted.&#x27;][&#x27;&lt;br/&gt;&lt;b&gt;true&lt;/b&gt;: Snapshots are kept, but group association is removed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;false&lt;/b&gt;: The group and snapshots are deleted.&#x27;]
        :type saveMembers: bool
        """

        connection_type = "Cluster"
        self._check_connection_type(connection_type)

        params = { 
            "groupSnapshotID": group_snapshot_id,
            "saveMembers": save_members,
        }
        
        # There is no adaptor.
        return self.send_request(
            'DeleteGroupSnapshot',
            DeleteGroupSnapshotResult,
            params
        )

    def list_group_snapshots(
            self,
            volume_id=OPTIONAL,):
        """
        ListGroupSnapshots is used to return information about all group snapshots that have been created.
        :param volumeID:  [&#x27;An array of unique volume IDs to query.&#x27;, &#x27;If this parameter is not specified, all group snapshots on the cluster will be included.&#x27;][&#x27;An array of unique volume IDs to query.&#x27;, &#x27;If this parameter is not specified, all group snapshots on the cluster will be included.&#x27;]
        :type volumeID: int
        """

        connection_type = "Cluster"
        self._check_connection_type(connection_type)

        params = { 
        }
        if volume_id is not None:
            params["volumeID"] = volume_id
        
        # There is no adaptor.
        return self.send_request(
            'ListGroupSnapshots',
            ListGroupSnapshotsResult,
            params
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
        
        :param enableRemoteReplication:  [&#x27;Use to enable the snapshot created to be replicated to a remote SolidFire cluster.&#x27;, &#x27;Possible values:&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;true&lt;/b&gt;: the snapshot will be replicated to remote storage.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;false&lt;/b&gt;: Default. No replication.&#x27;][&#x27;Use to enable the snapshot created to be replicated to a remote SolidFire cluster.&#x27;, &#x27;Possible values:&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;true&lt;/b&gt;: the snapshot will be replicated to remote storage.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;false&lt;/b&gt;: Default. No replication.&#x27;][&#x27;Use to enable the snapshot created to be replicated to a remote SolidFire cluster.&#x27;, &#x27;Possible values:&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;true&lt;/b&gt;: the snapshot will be replicated to remote storage.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;false&lt;/b&gt;: Default. No replication.&#x27;][&#x27;Use to enable the snapshot created to be replicated to a remote SolidFire cluster.&#x27;, &#x27;Possible values:&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;true&lt;/b&gt;: the snapshot will be replicated to remote storage.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;false&lt;/b&gt;: Default. No replication.&#x27;]
        :type enableRemoteReplication: bool
        """

        connection_type = "Cluster"
        self._check_connection_type(connection_type)

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

    def rollback_to_group_snapshot(
            self,
            group_snapshot_id,
            save_current_state,
            name=OPTIONAL,
            attributes=OPTIONAL,):
        """
        RollbackToGroupSnapshot is used to roll back each individual volume in a snapshot group to a copy of their individual snapshots.
        <br/><br/>
        <b>Note</b>: Creating a snapshot is allowed if cluster fullness is at stage 2 or 3.
        Snapshots are not created when cluster fullness is at stage 4 or 5.
        :param groupSnapshotID: [required] [&#x27;Unique ID of the group snapshot.&#x27;]
        :type groupSnapshotID: int
        
        :param saveCurrentState: [required] [&#x27;&lt;br/&gt;&lt;b&gt;true&lt;/b&gt;: The previous active volume image is kept.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;false&lt;/b&gt;: (default) The previous active volume image is deleted.&#x27;][&#x27;&lt;br/&gt;&lt;b&gt;true&lt;/b&gt;: The previous active volume image is kept.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;false&lt;/b&gt;: (default) The previous active volume image is deleted.&#x27;]
        :type saveCurrentState: bool
        
        :param name:  [&#x27;Name for the snapshot. If no name is given, then the name of the snapshot being rolled back to is used with &#x27;, &#x27;&quot;-copy&quot; appended to the end of the name.&#x27;][&#x27;Name for the snapshot. If no name is given, then the name of the snapshot being rolled back to is used with &#x27;, &#x27;&quot;-copy&quot; appended to the end of the name.&#x27;]
        :type name: str
        
        :param attributes:  [&#x27;List of Name/Value pairs in JSON object format&#x27;]
        :type attributes: dict
        """

        connection_type = "Cluster"
        self._check_connection_type(connection_type)

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
            since=7.0
        )

    def get_schedule(
            self,
            schedule_id,):
        """
        GetSchedule is used to return information about a scheduled snapshot that has been created. You can see information about a specified schedule if there are many snapshot schedules in the system. You can include more than one schedule with this method by specifying additional scheduleIDs to the parameter.
        :param scheduleID: [required] [&#x27;Unique ID of the schedule or multiple schedules to display&#x27;]
        :type scheduleID: int
        """

        connection_type = "Cluster"
        self._check_connection_type(connection_type)

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
        ListSchedule is used to return information about all scheduled snapshots that have been created."""

        connection_type = "Cluster"
        self._check_connection_type(connection_type)

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'ListSchedules',
            ListSchedulesResult,
            params,
            since=8.0
        )

    def create_schedule(
            self,
            schedule,):
        """
        CreateSchedule is used to create a schedule that will autonomously make a snapshot of a volume at a defined interval.<br/>
        <br/>
        The snapshot created can be used later as a backup or rollback to ensure the data on a volume or group of volumes is consistent for the point in time in which the snapshot was created. <br/>
        <br/>
        <b>Note</b>: Creating a snapshot is allowed if cluster fullness is at stage 2 or 3. Snapshots are not created when cluster fullness is at stage 4 or 5.
        :param schedule: [required] [&#x27;The &quot;Schedule&quot; object will be used to create a new schedule.&lt;br/&gt;&#x27;, &#x27;Do not set ScheduleID property, it will be ignored.&lt;br/&gt;&#x27;, &#x27;Frequency property must be of type that inherits from Frequency. Valid types are:&lt;br/&gt;&#x27;, &#x27;DaysOfMonthFrequency&lt;br/&gt;&#x27;, &#x27;DaysOrWeekFrequency&lt;br/&gt;&#x27;, &#x27;TimeIntervalFrequency&#x27;][&#x27;The &quot;Schedule&quot; object will be used to create a new schedule.&lt;br/&gt;&#x27;, &#x27;Do not set ScheduleID property, it will be ignored.&lt;br/&gt;&#x27;, &#x27;Frequency property must be of type that inherits from Frequency. Valid types are:&lt;br/&gt;&#x27;, &#x27;DaysOfMonthFrequency&lt;br/&gt;&#x27;, &#x27;DaysOrWeekFrequency&lt;br/&gt;&#x27;, &#x27;TimeIntervalFrequency&#x27;][&#x27;The &quot;Schedule&quot; object will be used to create a new schedule.&lt;br/&gt;&#x27;, &#x27;Do not set ScheduleID property, it will be ignored.&lt;br/&gt;&#x27;, &#x27;Frequency property must be of type that inherits from Frequency. Valid types are:&lt;br/&gt;&#x27;, &#x27;DaysOfMonthFrequency&lt;br/&gt;&#x27;, &#x27;DaysOrWeekFrequency&lt;br/&gt;&#x27;, &#x27;TimeIntervalFrequency&#x27;][&#x27;The &quot;Schedule&quot; object will be used to create a new schedule.&lt;br/&gt;&#x27;, &#x27;Do not set ScheduleID property, it will be ignored.&lt;br/&gt;&#x27;, &#x27;Frequency property must be of type that inherits from Frequency. Valid types are:&lt;br/&gt;&#x27;, &#x27;DaysOfMonthFrequency&lt;br/&gt;&#x27;, &#x27;DaysOrWeekFrequency&lt;br/&gt;&#x27;, &#x27;TimeIntervalFrequency&#x27;][&#x27;The &quot;Schedule&quot; object will be used to create a new schedule.&lt;br/&gt;&#x27;, &#x27;Do not set ScheduleID property, it will be ignored.&lt;br/&gt;&#x27;, &#x27;Frequency property must be of type that inherits from Frequency. Valid types are:&lt;br/&gt;&#x27;, &#x27;DaysOfMonthFrequency&lt;br/&gt;&#x27;, &#x27;DaysOrWeekFrequency&lt;br/&gt;&#x27;, &#x27;TimeIntervalFrequency&#x27;][&#x27;The &quot;Schedule&quot; object will be used to create a new schedule.&lt;br/&gt;&#x27;, &#x27;Do not set ScheduleID property, it will be ignored.&lt;br/&gt;&#x27;, &#x27;Frequency property must be of type that inherits from Frequency. Valid types are:&lt;br/&gt;&#x27;, &#x27;DaysOfMonthFrequency&lt;br/&gt;&#x27;, &#x27;DaysOrWeekFrequency&lt;br/&gt;&#x27;, &#x27;TimeIntervalFrequency&#x27;]
        :type schedule: Schedule
        """

        connection_type = "Cluster"
        self._check_connection_type(connection_type)

        params = { 
            "schedule": schedule,
        }
        
        # There is an adaptor!
        since = 8.0
        deprecated = None

        return ElementServiceAdaptor.create_schedule(self, params,
                                                  since, deprecated)

    def modify_schedule(
            self,
            schedule,):
        """
        ModifySchedule is used to change the intervals at which a scheduled snapshot occurs. This allows for adjustment to the snapshot frequency and retention.<br/>
        :param schedule: [required] [&#x27;The &quot;Schedule&quot; object will be used to modify an existing schedule.&lt;br/&gt;&#x27;, &#x27;The ScheduleID property is required.&lt;br/&gt;&#x27;, &#x27;Frequency property must be of type that inherits from Frequency. Valid types are:&lt;br/&gt;&#x27;, &#x27;DaysOfMonthFrequency&lt;br/&gt;&#x27;, &#x27;DaysOrWeekFrequency&lt;br/&gt;&#x27;, &#x27;TimeIntervalFrequency&#x27;][&#x27;The &quot;Schedule&quot; object will be used to modify an existing schedule.&lt;br/&gt;&#x27;, &#x27;The ScheduleID property is required.&lt;br/&gt;&#x27;, &#x27;Frequency property must be of type that inherits from Frequency. Valid types are:&lt;br/&gt;&#x27;, &#x27;DaysOfMonthFrequency&lt;br/&gt;&#x27;, &#x27;DaysOrWeekFrequency&lt;br/&gt;&#x27;, &#x27;TimeIntervalFrequency&#x27;][&#x27;The &quot;Schedule&quot; object will be used to modify an existing schedule.&lt;br/&gt;&#x27;, &#x27;The ScheduleID property is required.&lt;br/&gt;&#x27;, &#x27;Frequency property must be of type that inherits from Frequency. Valid types are:&lt;br/&gt;&#x27;, &#x27;DaysOfMonthFrequency&lt;br/&gt;&#x27;, &#x27;DaysOrWeekFrequency&lt;br/&gt;&#x27;, &#x27;TimeIntervalFrequency&#x27;][&#x27;The &quot;Schedule&quot; object will be used to modify an existing schedule.&lt;br/&gt;&#x27;, &#x27;The ScheduleID property is required.&lt;br/&gt;&#x27;, &#x27;Frequency property must be of type that inherits from Frequency. Valid types are:&lt;br/&gt;&#x27;, &#x27;DaysOfMonthFrequency&lt;br/&gt;&#x27;, &#x27;DaysOrWeekFrequency&lt;br/&gt;&#x27;, &#x27;TimeIntervalFrequency&#x27;][&#x27;The &quot;Schedule&quot; object will be used to modify an existing schedule.&lt;br/&gt;&#x27;, &#x27;The ScheduleID property is required.&lt;br/&gt;&#x27;, &#x27;Frequency property must be of type that inherits from Frequency. Valid types are:&lt;br/&gt;&#x27;, &#x27;DaysOfMonthFrequency&lt;br/&gt;&#x27;, &#x27;DaysOrWeekFrequency&lt;br/&gt;&#x27;, &#x27;TimeIntervalFrequency&#x27;][&#x27;The &quot;Schedule&quot; object will be used to modify an existing schedule.&lt;br/&gt;&#x27;, &#x27;The ScheduleID property is required.&lt;br/&gt;&#x27;, &#x27;Frequency property must be of type that inherits from Frequency. Valid types are:&lt;br/&gt;&#x27;, &#x27;DaysOfMonthFrequency&lt;br/&gt;&#x27;, &#x27;DaysOrWeekFrequency&lt;br/&gt;&#x27;, &#x27;TimeIntervalFrequency&#x27;]
        :type schedule: Schedule
        """

        connection_type = "Cluster"
        self._check_connection_type(connection_type)

        params = { 
            "schedule": schedule,
        }
        
        # There is an adaptor!
        since = 8.0
        deprecated = None

        return ElementServiceAdaptor.modify_schedule(self, params,
                                                  since, deprecated)

    def get_raw_stats(
            self,):
        """
        The GetRawStats call is used by SolidFire engineering to troubleshoot new features. The data returned from GetRawStats is not documented, it changes frequently, and is not guaranteed to be accurate. It is not recommended to ever use GetRawStats for collecting performance data or any other management integration with a SolidFire cluster.
        The data returned from GetRawStats changes frequently, and is not guaranteed to accurately show performance from the system. It is not recommended to ever use GetRawStats for collecting performance data or any other management integration with a SolidFire cluster."""

        connection_type = "Cluster"
        self._check_connection_type(connection_type)

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'GetRawStats',
            str,
            params
        )

    def get_complete_stats(
            self,):
        """
        The GetCompleteStats API method is used by SolidFire engineering to troubleshoot new features. The data returned from GetCompleteStats is not documented, changes frequently, and is not guaranteed to be accurate. It is not recommended to ever use GetCompleteStats for collecting performance data or any other management integration with a SolidFire cluster.
        The data returned from GetCompleteStats changes frequently, and is not guaranteed to accurately show performance from the system. It is not recommended to ever use GetCompleteStats for collecting performance data or any other management integration with a SolidFire cluster."""

        connection_type = "Cluster"
        self._check_connection_type(connection_type)

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'GetCompleteStats',
            str,
            params
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

        connection_type = "Cluster"
        self._check_connection_type(connection_type)

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
            since=9.0
        )

    def delete_storage_containers(
            self,
            storage_container_ids,):
        """
        Deletes a storage container from the system.
        :param storageContainerIDs: [required] list of storageContainerID of the storage container to delete.
        :type storageContainerIDs: UUID
        """

        connection_type = "Cluster"
        self._check_connection_type(connection_type)

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

        connection_type = "Cluster"
        self._check_connection_type(connection_type)

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
            CreateStorageContainerResult,
            params,
            since=9.0
        )

    def list_storage_containers(
            self,
            storage_container_ids=OPTIONAL,):
        """
        Gets information for all storage containers currently in the system.
        :param storageContainerIDs:  List of storage containers to get
        :type storageContainerIDs: UUID
        """

        connection_type = "Cluster"
        self._check_connection_type(connection_type)

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

    def get_storage_container_efficiency(
            self,
            storage_container_id,):
        """
        GetStorageContainerEfficiency enables you to retrieve efficiency information about a virtual volume storage container.
        :param storageContainerID: [required] The ID of the storage container for which to retrieve efficiency information.
        :type storageContainerID: UUID
        """

        connection_type = "Cluster"
        self._check_connection_type(connection_type)

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

    def list_tests(
            self,):
        """
        The ListTests API method is used to return the tests that are available to run on a node.
        <br/><b>Note</b>: This method is available only through the per-node API endpoint 5.0 or later."""

        connection_type = "Node"
        self._check_connection_type(connection_type)

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'ListTests',
            ListTestsResult,
            params
        )

    def list_utilities(
            self,):
        """
        The ListUtilities API method is used to return the tests that are available to run on a node.
        <br/><b>Note</b>: This method is available only through the per-node API endpoint 5.0 or later."""

        connection_type = "Node"
        self._check_connection_type(connection_type)

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'ListUtilities',
            ListUtilitiesResult,
            params
        )

    def test_connect_ensemble(
            self,
            ensemble=OPTIONAL,):
        """
        The TestConnectEnsemble API method is used to verify connectivity with a sepcified database ensemble. By default it uses the ensemble for the cluster the node is associated with. Alternatively you can provide a different ensemble to test connectivity with.
        <br/><b>Note</b>: This method is available only through the per-node API endpoint 5.0 or later.
        :param ensemble:  A comma-separated list of ensemble node CIPs for connectivity testing
        :type ensemble: str
        """

        connection_type = "Node"
        self._check_connection_type(connection_type)

        params = { 
        }
        if ensemble is not None:
            params["ensemble"] = ensemble
        
        # There is no adaptor.
        return self.send_request(
            'TestConnectEnsemble',
            TestConnectEnsembleResult,
            params
        )

    def test_connect_mvip(
            self,
            mvip=OPTIONAL,):
        """
        The TestConnectMvip API method is used to test the management connection to the cluster. The test pings the MVIP and executes a simple API method to verify connectivity.
        <br/><b>Note</b>: This method is available only through the per-node API endpoint 5.0 or later.
        :param mvip:  Optionally, use to test the management connection of a different MVIP. This is not needed to test the connection to the target cluster.
        :type mvip: str
        """

        connection_type = "Node"
        self._check_connection_type(connection_type)

        params = { 
        }
        if mvip is not None:
            params["mvip"] = mvip
        
        # There is no adaptor.
        return self.send_request(
            'TestConnectMvip',
            TestConnectMvipResult,
            params
        )

    def test_connect_svip(
            self,
            svip=OPTIONAL,):
        """
        The TestConnectSvip API method is used to test the storage connection to the cluster. The test pings the SVIP using ICMP packets and when successful connects as an iSCSI initiator.
        <br/><b>Note</b>: This method is available only through the per-node API endpoint 5.0 or later.
        :param svip:  Optionally, use to test the storage connection of a different SVIP. This is not needed to test the connection to the target cluster.
        :type svip: str
        """

        connection_type = "Node"
        self._check_connection_type(connection_type)

        params = { 
        }
        if svip is not None:
            params["svip"] = svip
        
        # There is no adaptor.
        return self.send_request(
            'TestConnectSvip',
            TestConnectSvipResult,
            params
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
        <br/><b>Note</b>: This method is available only through the per-node API endpoint 5.0 or later.
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

        connection_type = "Node"
        self._check_connection_type(connection_type)

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
            params
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

        connection_type = "Cluster"
        self._check_connection_type(connection_type)

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
        <br/><br/>
        <b>Note:</b> The AddVirtualNetwork method is used only to create a new virtual network. If you want to make changes to a virtual network, please use the ModifyVirtualNetwork method.
        :param virtualNetworkTag: [required] A unique virtual network (VLAN) tag. Supported values are 1 to 4095 (the number zero (0) is not supported).
        :type virtualNetworkTag: int
        
        :param name: [required] User defined name for the new virtual network.
        :type name: str
        
        :param addressBlocks: [required] [&#x27;Unique Range of IP addresses to include in the virtual network.&#x27;, &#x27;Attributes for this parameter are:&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;start:&lt;/b&gt; start of the IP address range. (String)&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;size:&lt;/b&gt; numbre of IP addresses to include in the block. (Integer)&#x27;][&#x27;Unique Range of IP addresses to include in the virtual network.&#x27;, &#x27;Attributes for this parameter are:&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;start:&lt;/b&gt; start of the IP address range. (String)&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;size:&lt;/b&gt; numbre of IP addresses to include in the block. (Integer)&#x27;][&#x27;Unique Range of IP addresses to include in the virtual network.&#x27;, &#x27;Attributes for this parameter are:&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;start:&lt;/b&gt; start of the IP address range. (String)&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;size:&lt;/b&gt; numbre of IP addresses to include in the block. (Integer)&#x27;][&#x27;Unique Range of IP addresses to include in the virtual network.&#x27;, &#x27;Attributes for this parameter are:&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;start:&lt;/b&gt; start of the IP address range. (String)&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;size:&lt;/b&gt; numbre of IP addresses to include in the block. (Integer)&#x27;]
        :type addressBlocks: AddressBlock
        
        :param netmask: [required] [&#x27;Unique netmask for the virtual network being created.&#x27;]
        :type netmask: str
        
        :param svip: [required] [&#x27;Unique storage IP address for the virtual network being created.&#x27;]
        :type svip: str
        
        :param gateway:  [&#x27;&#x27;]
        :type gateway: str
        
        :param namespace:  [&#x27;&#x27;]
        :type namespace: bool
        
        :param attributes:  [&#x27;List of Name/Value pairs in JSON object format.&#x27;]
        :type attributes: dict
        """

        connection_type = "Cluster"
        self._check_connection_type(connection_type)

        params = { 
            "virtualNetworkTag": virtual_network_tag,
            "name": name,
            "addressBlocks": address_blocks,
            "netmask": netmask,
            "svip": svip,
        }
        if gateway is not None:
            params["gateway"] = gateway
        if namespace is not None:
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
        <br/><br/>
        <b>Note:</b> This method requires either the VirtualNetworkID or the VirtualNetworkTag as a parameter, but not both.
        :param virtualNetworkID:  Unique identifier of the virtual network to modify. This is the virtual network ID assigned by the SolidFire cluster.
        :type virtualNetworkID: int
        
        :param virtualNetworkTag:  Network Tag that identifies the virtual network to modify.
        :type virtualNetworkTag: int
        
        :param name:  New name for the virtual network.
        :type name: str
        
        :param addressBlocks:  [&#x27;New addressBlock to set for this Virtual Network object. This may contain new address blocks to add to the existing object or it may omit unused address blocks that need to be removed. Alternatively, existing address blocks may be extended or reduced in size. The size of the starting addressBlocks for a Virtual Network object can only be increased, and can never be decreased.&#x27;, &#x27;Attributes for this parameter are:&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;start:&lt;/b&gt; start of the IP address range. (String)&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;size:&lt;/b&gt; numbre of IP addresses to include in the block. (Integer)&#x27;][&#x27;New addressBlock to set for this Virtual Network object. This may contain new address blocks to add to the existing object or it may omit unused address blocks that need to be removed. Alternatively, existing address blocks may be extended or reduced in size. The size of the starting addressBlocks for a Virtual Network object can only be increased, and can never be decreased.&#x27;, &#x27;Attributes for this parameter are:&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;start:&lt;/b&gt; start of the IP address range. (String)&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;size:&lt;/b&gt; numbre of IP addresses to include in the block. (Integer)&#x27;][&#x27;New addressBlock to set for this Virtual Network object. This may contain new address blocks to add to the existing object or it may omit unused address blocks that need to be removed. Alternatively, existing address blocks may be extended or reduced in size. The size of the starting addressBlocks for a Virtual Network object can only be increased, and can never be decreased.&#x27;, &#x27;Attributes for this parameter are:&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;start:&lt;/b&gt; start of the IP address range. (String)&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;size:&lt;/b&gt; numbre of IP addresses to include in the block. (Integer)&#x27;][&#x27;New addressBlock to set for this Virtual Network object. This may contain new address blocks to add to the existing object or it may omit unused address blocks that need to be removed. Alternatively, existing address blocks may be extended or reduced in size. The size of the starting addressBlocks for a Virtual Network object can only be increased, and can never be decreased.&#x27;, &#x27;Attributes for this parameter are:&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;start:&lt;/b&gt; start of the IP address range. (String)&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;size:&lt;/b&gt; numbre of IP addresses to include in the block. (Integer)&#x27;]
        :type addressBlocks: AddressBlock
        
        :param netmask:  [&#x27;New netmask for this virtual network.&#x27;]
        :type netmask: str
        
        :param svip:  [&#x27;The storage virtual IP address for this virtual network. The svip for Virtual Network cannot be changed. A new Virtual Network must be created in order to use a different svip address.&#x27;]
        :type svip: str
        
        :param gateway:  [&#x27;&#x27;]
        :type gateway: str
        
        :param namespace:  [&#x27;&#x27;]
        :type namespace: bool
        
        :param attributes:  [&#x27;A new list of Name/Value pairs in JSON object format.&#x27;]
        :type attributes: dict
        """

        connection_type = "Cluster"
        self._check_connection_type(connection_type)

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
            params["gateway"] = gateway
        if namespace is not None:
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
        RemoveVirtualNetwork is used to remove a previously added virtual network.
        <br/><br/>
        <b>Note:</b> This method requires either the VirtualNetworkID of the VirtualNetworkTag as a parameter, but not both.
        :param virtualNetworkID:  Network ID that identifies the virtual network to remove.
        :type virtualNetworkID: int
        
        :param virtualNetworkTag:  Network Tag that identifies the virtual network to remove.
        :type virtualNetworkTag: int
        """

        connection_type = "Cluster"
        self._check_connection_type(connection_type)

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

    def prepare_virtual_snapshot(
            self,
            virtual_volume_id,
            name=OPTIONAL,
            writable_snapshot=OPTIONAL,
            calling_virtual_volume_host_id=OPTIONAL,):
        """
        PrepareVirtualSnapshot is used to set up VMware Virtual Volume snapshot.
        :param virtualVolumeID: [required] The ID of the Virtual Volume to clone.
        :type virtualVolumeID: UUID
        
        :param name:  The name for the newly-created volume.
        :type name: str
        
        :param writableSnapshot:  Will the snapshot be writable?
        :type writableSnapshot: bool
        
        :param callingVirtualVolumeHostID:  
        :type callingVirtualVolumeHostID: UUID
        """

        connection_type = "Cluster"
        self._check_connection_type(connection_type)

        params = { 
            "virtualVolumeID": virtual_volume_id,
        }
        if name is not None:
            params["name"] = name
        if writable_snapshot is not None:
            params["writableSnapshot"] = writable_snapshot
        if calling_virtual_volume_host_id is not None:
            params["callingVirtualVolumeHostID"] = calling_virtual_volume_host_id
        
        # There is no adaptor.
        return self.send_request(
            'PrepareVirtualSnapshot',
            PrepareVirtualSnapshotResult,
            params,
            since=9.0
        )

    def get_virtual_volume_unshared_chunks(
            self,
            virtual_volume_id,
            base_virtual_volume_id,
            segment_start,
            segment_length,
            chunk_size,
            calling_virtual_volume_host_id=OPTIONAL,):
        """
        GetVirtualVolumeAllocatedBitmap scans a VVol segment and returns the number of 
        chunks not shared between two volumes. This call will return results in less 
        than 30 seconds. If the specified VVol and the base VVil are not related, an 
        error is thrown. If the offset/length combination is invalid or out fo range 
        an error is thrown.
        :param virtualVolumeID: [required] The ID of the Virtual Volume.
        :type virtualVolumeID: UUID
        
        :param baseVirtualVolumeID: [required] The ID of the Virtual Volume to compare against.
        :type baseVirtualVolumeID: UUID
        
        :param segmentStart: [required] Start Byte offset.
        :type segmentStart: int
        
        :param segmentLength: [required] Length of the scan segment in bytes.
        :type segmentLength: int
        
        :param chunkSize: [required] Number of bytes represented by one bit in the bitmap.
        :type chunkSize: int
        
        :param callingVirtualVolumeHostID:  
        :type callingVirtualVolumeHostID: UUID
        """

        connection_type = "Cluster"
        self._check_connection_type(connection_type)

        params = { 
            "virtualVolumeID": virtual_volume_id,
            "baseVirtualVolumeID": base_virtual_volume_id,
            "segmentStart": segment_start,
            "segmentLength": segment_length,
            "chunkSize": chunk_size,
        }
        if calling_virtual_volume_host_id is not None:
            params["callingVirtualVolumeHostID"] = calling_virtual_volume_host_id
        
        # There is no adaptor.
        return self.send_request(
            'GetVirtualVolumeUnsharedChunks',
            VirtualVolumeUnsharedChunkResult,
            params,
            since=9.0
        )

    def create_virtual_volume_host(
            self,
            virtual_volume_host_id,
            cluster_id,
            initiator_names=OPTIONAL,
            visible_protocol_endpoint_ids=OPTIONAL,
            host_address=OPTIONAL,
            calling_virtual_volume_host_id=OPTIONAL,):
        """
        CreateVirtualVolumeHost creates a new ESX host.
        :param virtualVolumeHostID: [required] The GUID of the ESX host.
        :type virtualVolumeHostID: UUID
        
        :param clusterID: [required] The GUID of the ESX Cluster.
        :type clusterID: UUID
        
        :param initiatorNames:  
        :type initiatorNames: str
        
        :param visibleProtocolEndpointIDs:  A list of PEs the host is aware of.
        :type visibleProtocolEndpointIDs: UUID
        
        :param hostAddress:  IP or DNS name for the host.
        :type hostAddress: str
        
        :param callingVirtualVolumeHostID:  
        :type callingVirtualVolumeHostID: UUID
        """

        connection_type = "Cluster"
        self._check_connection_type(connection_type)

        params = { 
            "virtualVolumeHostID": virtual_volume_host_id,
            "clusterID": cluster_id,
        }
        if initiator_names is not None:
            params["initiatorNames"] = initiator_names
        if visible_protocol_endpoint_ids is not None:
            params["visibleProtocolEndpointIDs"] = visible_protocol_endpoint_ids
        if host_address is not None:
            params["hostAddress"] = host_address
        if calling_virtual_volume_host_id is not None:
            params["callingVirtualVolumeHostID"] = calling_virtual_volume_host_id
        
        # There is no adaptor.
        return self.send_request(
            'CreateVirtualVolumeHost',
            VirtualVolumeNullResult,
            params,
            since=9.0
        )

    def list_virtual_volume_hosts(
            self,
            virtual_volume_host_ids=OPTIONAL,
            calling_virtual_volume_host_id=OPTIONAL,):
        """
        ListVirtualVolumeHosts returns a list of known ESX hosts.
        :param virtualVolumeHostIDs:  
        :type virtualVolumeHostIDs: UUID
        
        :param callingVirtualVolumeHostID:  
        :type callingVirtualVolumeHostID: UUID
        """

        connection_type = "Cluster"
        self._check_connection_type(connection_type)

        params = { 
        }
        if virtual_volume_host_ids is not None:
            params["virtualVolumeHostIDs"] = virtual_volume_host_ids
        if calling_virtual_volume_host_id is not None:
            params["callingVirtualVolumeHostID"] = calling_virtual_volume_host_id
        
        # There is no adaptor.
        return self.send_request(
            'ListVirtualVolumeHosts',
            ListVirtualVolumeHostsResult,
            params,
            since=9.0
        )

    def get_virtual_volume_task_update(
            self,
            virtual_volume_task_id,
            calling_virtual_volume_host_id=OPTIONAL,):
        """
        GetVirtualVolumeTaskUpdate checks the status of a VVol Async Task.
        :param virtualVolumeTaskID: [required] The UUID of the VVol Task.
        :type virtualVolumeTaskID: UUID
        
        :param callingVirtualVolumeHostID:  
        :type callingVirtualVolumeHostID: UUID
        """

        connection_type = "Cluster"
        self._check_connection_type(connection_type)

        params = { 
            "virtualVolumeTaskID": virtual_volume_task_id,
        }
        if calling_virtual_volume_host_id is not None:
            params["callingVirtualVolumeHostID"] = calling_virtual_volume_host_id
        
        # There is no adaptor.
        return self.send_request(
            'GetVirtualVolumeTaskUpdate',
            VirtualVolumeTaskResult,
            params,
            since=9.0
        )

    def list_virtual_volume_tasks(
            self,
            virtual_volume_task_ids=OPTIONAL,
            calling_virtual_volume_host_id=OPTIONAL,):
        """
        ListVirtualVolumeTasks returns a list of VVol Async Tasks.
        :param virtualVolumeTaskIDs:  
        :type virtualVolumeTaskIDs: UUID
        
        :param callingVirtualVolumeHostID:  
        :type callingVirtualVolumeHostID: UUID
        """

        connection_type = "Cluster"
        self._check_connection_type(connection_type)

        params = { 
        }
        if virtual_volume_task_ids is not None:
            params["virtualVolumeTaskIDs"] = virtual_volume_task_ids
        if calling_virtual_volume_host_id is not None:
            params["callingVirtualVolumeHostID"] = calling_virtual_volume_host_id
        
        # There is no adaptor.
        return self.send_request(
            'ListVirtualVolumeTasks',
            ListVirtualVolumeTasksResult,
            params,
            since=9.0
        )

    def list_virtual_volume_bindings(
            self,
            virtual_volume_binding_ids=OPTIONAL,
            calling_virtual_volume_host_id=OPTIONAL,):
        """
        ListVirtualVolumeBindings returns a list of VVol bindings.
        :param virtualVolumeBindingIDs:  
        :type virtualVolumeBindingIDs: int
        
        :param callingVirtualVolumeHostID:  
        :type callingVirtualVolumeHostID: UUID
        """

        connection_type = "Cluster"
        self._check_connection_type(connection_type)

        params = { 
        }
        if virtual_volume_binding_ids is not None:
            params["virtualVolumeBindingIDs"] = virtual_volume_binding_ids
        if calling_virtual_volume_host_id is not None:
            params["callingVirtualVolumeHostID"] = calling_virtual_volume_host_id
        
        # There is no adaptor.
        return self.send_request(
            'ListVirtualVolumeBindings',
            ListVirtualVolumeBindingsResult,
            params,
            since=9.0
        )

    def get_virtual_volume_count(
            self,):
        """
        Enables retrieval of the number of virtual volumes currently in the system."""

        connection_type = "Cluster"
        self._check_connection_type(connection_type)

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'GetVirtualVolumeCount',
            GetVirtualVolumeCountResult,
            params,
            since=9.0
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
        <br/><br/>
        <b>Note</b>: The initial attributes and quality of service settings for the volume are inherited from the volume being cloned.
        If different settings are required, they can be changed via ModifyVolume.
        <br/><br/>
        <b>Note</b>: Cloned volumes do not inherit volume access group memberships from the source volume.
        :param volumeID: [required] The ID of the volume to clone.
        :type volumeID: int
        
        :param name: [required] The name for the newly-created volume.
        :type name: str
        
        :param newAccountID:  [&#x27;AccountID for the owner of the new volume.&#x27;, &#x27;If unspecified, the AccountID of the owner of the volume being cloned is used.&#x27;][&#x27;AccountID for the owner of the new volume.&#x27;, &#x27;If unspecified, the AccountID of the owner of the volume being cloned is used.&#x27;]
        :type newAccountID: int
        
        :param newSize:  [&#x27;New size of the volume, in bytes.&#x27;, &#x27;May be greater or less than the size of the volume being cloned.&#x27;, &quot;If unspecified, the clone&#x27;s volume size will be the same as the source volume.&quot;, &#x27;Size is rounded up to the nearest 1 MiB.&#x27;][&#x27;New size of the volume, in bytes.&#x27;, &#x27;May be greater or less than the size of the volume being cloned.&#x27;, &quot;If unspecified, the clone&#x27;s volume size will be the same as the source volume.&quot;, &#x27;Size is rounded up to the nearest 1 MiB.&#x27;][&#x27;New size of the volume, in bytes.&#x27;, &#x27;May be greater or less than the size of the volume being cloned.&#x27;, &quot;If unspecified, the clone&#x27;s volume size will be the same as the source volume.&quot;, &#x27;Size is rounded up to the nearest 1 MiB.&#x27;][&#x27;New size of the volume, in bytes.&#x27;, &#x27;May be greater or less than the size of the volume being cloned.&#x27;, &quot;If unspecified, the clone&#x27;s volume size will be the same as the source volume.&quot;, &#x27;Size is rounded up to the nearest 1 MiB.&#x27;]
        :type newSize: int
        
        :param access:  [&#x27;Access settings for the new volume.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;readOnly&lt;/b&gt;: Only read operations are allowed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;readWrite&lt;/b&gt;: Reads and writes are allowed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;locked&lt;/b&gt;: No reads or writes are allowed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;replicationTarget&lt;/b&gt;: Identify a volume as the target volume for a paired set of volumes. If the volume is not paired, the access status is locked.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;If unspecified, the access settings of the clone will be the same as the source.&#x27;][&#x27;Access settings for the new volume.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;readOnly&lt;/b&gt;: Only read operations are allowed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;readWrite&lt;/b&gt;: Reads and writes are allowed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;locked&lt;/b&gt;: No reads or writes are allowed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;replicationTarget&lt;/b&gt;: Identify a volume as the target volume for a paired set of volumes. If the volume is not paired, the access status is locked.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;If unspecified, the access settings of the clone will be the same as the source.&#x27;][&#x27;Access settings for the new volume.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;readOnly&lt;/b&gt;: Only read operations are allowed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;readWrite&lt;/b&gt;: Reads and writes are allowed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;locked&lt;/b&gt;: No reads or writes are allowed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;replicationTarget&lt;/b&gt;: Identify a volume as the target volume for a paired set of volumes. If the volume is not paired, the access status is locked.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;If unspecified, the access settings of the clone will be the same as the source.&#x27;][&#x27;Access settings for the new volume.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;readOnly&lt;/b&gt;: Only read operations are allowed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;readWrite&lt;/b&gt;: Reads and writes are allowed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;locked&lt;/b&gt;: No reads or writes are allowed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;replicationTarget&lt;/b&gt;: Identify a volume as the target volume for a paired set of volumes. If the volume is not paired, the access status is locked.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;If unspecified, the access settings of the clone will be the same as the source.&#x27;][&#x27;Access settings for the new volume.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;readOnly&lt;/b&gt;: Only read operations are allowed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;readWrite&lt;/b&gt;: Reads and writes are allowed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;locked&lt;/b&gt;: No reads or writes are allowed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;replicationTarget&lt;/b&gt;: Identify a volume as the target volume for a paired set of volumes. If the volume is not paired, the access status is locked.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;If unspecified, the access settings of the clone will be the same as the source.&#x27;][&#x27;Access settings for the new volume.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;readOnly&lt;/b&gt;: Only read operations are allowed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;readWrite&lt;/b&gt;: Reads and writes are allowed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;locked&lt;/b&gt;: No reads or writes are allowed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;replicationTarget&lt;/b&gt;: Identify a volume as the target volume for a paired set of volumes. If the volume is not paired, the access status is locked.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;If unspecified, the access settings of the clone will be the same as the source.&#x27;][&#x27;Access settings for the new volume.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;readOnly&lt;/b&gt;: Only read operations are allowed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;readWrite&lt;/b&gt;: Reads and writes are allowed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;locked&lt;/b&gt;: No reads or writes are allowed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;replicationTarget&lt;/b&gt;: Identify a volume as the target volume for a paired set of volumes. If the volume is not paired, the access status is locked.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;If unspecified, the access settings of the clone will be the same as the source.&#x27;]
        :type access: str
        
        :param snapshotID:  [&#x27;ID of the snapshot to use as the source of the clone.&#x27;, &#x27;If unspecified, the clone will be created with a snapshot of the active volume.&#x27;][&#x27;ID of the snapshot to use as the source of the clone.&#x27;, &#x27;If unspecified, the clone will be created with a snapshot of the active volume.&#x27;]
        :type snapshotID: int
        
        :param attributes:  List of Name/Value pairs in JSON object format.
        :type attributes: dict
        """

        connection_type = "Cluster"
        self._check_connection_type(connection_type)

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
            params
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
        <br/><br/>
        <b>Note</b>: Cloning multiple volumes is allowed if cluster fullness is at stage 2 or 3. Clones are not created when cluster fullness is at stage 4 or 5.
        :param volumes: [required] Array of Unique ID for each volume to include in the clone with optional parameters. If optional parameters are not specified, the values will be inherited from the source volumes.
        :type volumes: CloneMultipleVolumeParams
        
        :param access:  [&#x27;New default access method for the new volumes if not overridden by information passed in the volumes array.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;readOnly&lt;/b&gt;: Only read operations are allowed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;readWrite&lt;/b&gt;: Reads and writes are allowed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;locked&lt;/b&gt;: No reads or writes are allowed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;replicationTarget&lt;/b&gt;: Identify a volume as the target volume for a paired set of volumes. If the volume is not paired, the access status is locked.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;If unspecified, the access settings of the clone will be the same as the source.&#x27;][&#x27;New default access method for the new volumes if not overridden by information passed in the volumes array.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;readOnly&lt;/b&gt;: Only read operations are allowed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;readWrite&lt;/b&gt;: Reads and writes are allowed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;locked&lt;/b&gt;: No reads or writes are allowed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;replicationTarget&lt;/b&gt;: Identify a volume as the target volume for a paired set of volumes. If the volume is not paired, the access status is locked.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;If unspecified, the access settings of the clone will be the same as the source.&#x27;][&#x27;New default access method for the new volumes if not overridden by information passed in the volumes array.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;readOnly&lt;/b&gt;: Only read operations are allowed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;readWrite&lt;/b&gt;: Reads and writes are allowed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;locked&lt;/b&gt;: No reads or writes are allowed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;replicationTarget&lt;/b&gt;: Identify a volume as the target volume for a paired set of volumes. If the volume is not paired, the access status is locked.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;If unspecified, the access settings of the clone will be the same as the source.&#x27;][&#x27;New default access method for the new volumes if not overridden by information passed in the volumes array.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;readOnly&lt;/b&gt;: Only read operations are allowed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;readWrite&lt;/b&gt;: Reads and writes are allowed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;locked&lt;/b&gt;: No reads or writes are allowed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;replicationTarget&lt;/b&gt;: Identify a volume as the target volume for a paired set of volumes. If the volume is not paired, the access status is locked.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;If unspecified, the access settings of the clone will be the same as the source.&#x27;][&#x27;New default access method for the new volumes if not overridden by information passed in the volumes array.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;readOnly&lt;/b&gt;: Only read operations are allowed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;readWrite&lt;/b&gt;: Reads and writes are allowed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;locked&lt;/b&gt;: No reads or writes are allowed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;replicationTarget&lt;/b&gt;: Identify a volume as the target volume for a paired set of volumes. If the volume is not paired, the access status is locked.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;If unspecified, the access settings of the clone will be the same as the source.&#x27;][&#x27;New default access method for the new volumes if not overridden by information passed in the volumes array.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;readOnly&lt;/b&gt;: Only read operations are allowed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;readWrite&lt;/b&gt;: Reads and writes are allowed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;locked&lt;/b&gt;: No reads or writes are allowed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;replicationTarget&lt;/b&gt;: Identify a volume as the target volume for a paired set of volumes. If the volume is not paired, the access status is locked.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;If unspecified, the access settings of the clone will be the same as the source.&#x27;][&#x27;New default access method for the new volumes if not overridden by information passed in the volumes array.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;readOnly&lt;/b&gt;: Only read operations are allowed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;readWrite&lt;/b&gt;: Reads and writes are allowed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;locked&lt;/b&gt;: No reads or writes are allowed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;replicationTarget&lt;/b&gt;: Identify a volume as the target volume for a paired set of volumes. If the volume is not paired, the access status is locked.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;If unspecified, the access settings of the clone will be the same as the source.&#x27;]
        :type access: str
        
        :param groupSnapshotID:  ID of the group snapshot to use as a basis for the clone.
        :type groupSnapshotID: int
        
        :param newAccountID:  New account ID for the volumes if not overridden by information passed in the volumes array.
        :type newAccountID: int
        """

        connection_type = "Cluster"
        self._check_connection_type(connection_type)

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
            params
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
        :param name: [required] [&#x27;Name of the volume.&#x27;, &#x27;Not required to be unique, but it is recommended.&#x27;, &#x27;May be 1 to 64 characters in length.&#x27;][&#x27;Name of the volume.&#x27;, &#x27;Not required to be unique, but it is recommended.&#x27;, &#x27;May be 1 to 64 characters in length.&#x27;][&#x27;Name of the volume.&#x27;, &#x27;Not required to be unique, but it is recommended.&#x27;, &#x27;May be 1 to 64 characters in length.&#x27;]
        :type name: str
        
        :param accountID: [required] AccountID for the owner of this volume.
        :type accountID: int
        
        :param totalSize: [required] Total size of the volume, in bytes. Size is rounded up to the nearest 1MB size.
        :type totalSize: int
        
        :param enable512e: [required] Should the volume provides 512-byte sector emulation?
        :type enable512e: bool
        
        :param qos:  [&#x27;Initial quality of service settings for this volume.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;Volumes created without specified QoS values are created with the default values for QoS.&#x27;, &#x27;Default values for a volume can be found by running the GetDefaultQoS method.&#x27;][&#x27;Initial quality of service settings for this volume.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;Volumes created without specified QoS values are created with the default values for QoS.&#x27;, &#x27;Default values for a volume can be found by running the GetDefaultQoS method.&#x27;][&#x27;Initial quality of service settings for this volume.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;Volumes created without specified QoS values are created with the default values for QoS.&#x27;, &#x27;Default values for a volume can be found by running the GetDefaultQoS method.&#x27;][&#x27;Initial quality of service settings for this volume.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;Volumes created without specified QoS values are created with the default values for QoS.&#x27;, &#x27;Default values for a volume can be found by running the GetDefaultQoS method.&#x27;]
        :type qos: QoS
        
        :param attributes:  List of Name/Value pairs in JSON object format.
        :type attributes: dict
        """

        connection_type = "Cluster"
        self._check_connection_type(connection_type)

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
            params
        )

    def delete_volume(
            self,
            volume_id,):
        """
        DeleteVolume marks an active volume for deletion.
        It is purged (permanently deleted) after the cleanup interval elapses.
        After making a request to delete a volume, any active iSCSI connections to the volume is immediately terminated and no further connections are allowed while the volume is in this state.
        It is not returned in target discovery requests.
        <br/><br/>
        Any snapshots of a volume that has been marked to delete are not affected.
        Snapshots are kept until the volume is purged from the system.
        <br/><br/>
        If a volume is marked for deletion, and it has a bulk volume read or bulk volume write operation in progress, the bulk volume operation is stopped.
        <br/><br/>
        If the volume you delete is paired with a volume, replication between the paired volumes is suspended and no data is transferred to it or from it while in a deleted state.
        The remote volume the deleted volume was paired with enters into a PausedMisconfigured state and data is no longer sent to it or from the deleted volume.
        Until the deleted volume is purged, it can be restored and data transfers resumes.
        If the deleted volume gets purged from the system, the volume it was paired with enters into a StoppedMisconfigured state and the volume pairing status is removed.
        The purged volume becomes permanently unavailable.
        :param volumeID: [required] The ID of the volume to delete.
        :type volumeID: int
        """

        connection_type = "Cluster"
        self._check_connection_type(connection_type)

        params = { 
            "volumeID": volume_id,
        }
        
        # There is no adaptor.
        return self.send_request(
            'DeleteVolume',
            DeleteVolumeResult,
            params
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

        connection_type = "Cluster"
        self._check_connection_type(connection_type)

        params = { 
            "volumeID": volume_id,
        }
        
        # There is no adaptor.
        return self.send_request(
            'GetVolumeStats',
            GetVolumeStatsResult,
            params
        )

    def get_volume_efficiency(
            self,
            volume_id,
            force=OPTIONAL,):
        """
        GetVolumeEfficiency is used to retrieve information about a volume.
        Only the volume given as a parameter in this API method is used to compute the capacity.
        :param volumeID: [required] Specifies the volume for which capacity is computed.
        :type volumeID: int
        
        :param force:  
        :type force: bool
        """

        connection_type = "Cluster"
        self._check_connection_type(connection_type)

        params = { 
            "volumeID": volume_id,
        }
        if force is not None:
            params["force"] = force
        
        # There is no adaptor.
        return self.send_request(
            'GetVolumeEfficiency',
            GetVolumeEfficiencyResult,
            params
        )

    def list_bulk_volume_jobs(
            self,):
        """
        ListBulkVolumeJobs is used to return information about each bulk volume read or write operation that is occurring in the system."""

        connection_type = "Cluster"
        self._check_connection_type(connection_type)

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'ListBulkVolumeJobs',
            ListBulkVolumeJobsResult,
            params
        )

    def list_active_volumes(
            self,
            start_volume_id=OPTIONAL,
            limit=OPTIONAL,):
        """
        ListActiveVolumes is used to return the list of active volumes currently in the system.
        The list of volumes is returned sorted in VolumeID order and can be returned in multiple parts (pages).
        :param startVolumeID:  [&#x27;The ID of the first volume to list.&#x27;, &#x27;This can be useful for paging results.&#x27;, &#x27;By default, this starts at the lowest VolumeID.&#x27;][&#x27;The ID of the first volume to list.&#x27;, &#x27;This can be useful for paging results.&#x27;, &#x27;By default, this starts at the lowest VolumeID.&#x27;][&#x27;The ID of the first volume to list.&#x27;, &#x27;This can be useful for paging results.&#x27;, &#x27;By default, this starts at the lowest VolumeID.&#x27;]
        :type startVolumeID: int
        
        :param limit:  [&#x27;The maximum number of volumes to return from the API.&#x27;]
        :type limit: int
        """

        connection_type = "Cluster"
        self._check_connection_type(connection_type)

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
            params
        )

    def list_deleted_volumes(
            self,):
        """
        ListDeletedVolumes is used to return the entire list of volumes that have been marked for deletion and is purged from the system."""

        connection_type = "Cluster"
        self._check_connection_type(connection_type)

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'ListDeletedVolumes',
            ListDeletedVolumesResult,
            params
        )

    def list_iscsisessions(
            self,):
        """
        ListISCSISessions is used to return iSCSI connection information for volumes in the cluster."""

        connection_type = "Cluster"
        self._check_connection_type(connection_type)

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'ListISCSISessions',
            ListISCSISessionsResult,
            params
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
        :param startVolumeID:  [&#x27;The ID of the first volume to list.&#x27;, &#x27;This can be useful for paging results.&#x27;, &#x27;By default, this starts at the lowest VolumeID.&#x27;][&#x27;The ID of the first volume to list.&#x27;, &#x27;This can be useful for paging results.&#x27;, &#x27;By default, this starts at the lowest VolumeID.&#x27;][&#x27;The ID of the first volume to list.&#x27;, &#x27;This can be useful for paging results.&#x27;, &#x27;By default, this starts at the lowest VolumeID.&#x27;]
        :type startVolumeID: int
        
        :param limit:  [&#x27;The maximum number of volumes to return from the API.&#x27;]
        :type limit: int
        
        :param volumeStatus:  [&#x27;If specified, filter to only volumes with the provided status.&#x27;, &#x27;By default, list all volumes.&#x27;][&#x27;If specified, filter to only volumes with the provided status.&#x27;, &#x27;By default, list all volumes.&#x27;]
        :type volumeStatus: str
        
        :param accounts:  [&#x27;If specified, only fetch volumes which belong to the provided accounts.&#x27;, &#x27;By default, list volumes for all accounts.&#x27;][&#x27;If specified, only fetch volumes which belong to the provided accounts.&#x27;, &#x27;By default, list volumes for all accounts.&#x27;]
        :type accounts: int
        
        :param isPaired:  [&#x27;If specified, only fetch volumes which are paired (if true) or non-paired (if false).&#x27;, &#x27;By default, list all volumes regardless of their pairing status.&#x27;][&#x27;If specified, only fetch volumes which are paired (if true) or non-paired (if false).&#x27;, &#x27;By default, list all volumes regardless of their pairing status.&#x27;]
        :type isPaired: bool
        
        :param volumeIDs:  [&#x27;If specified, only fetch volumes specified in this list.&#x27;, &#x27;This option cannot be specified if startVolumeID, limit, or accounts option is specified.&#x27;][&#x27;If specified, only fetch volumes specified in this list.&#x27;, &#x27;This option cannot be specified if startVolumeID, limit, or accounts option is specified.&#x27;]
        :type volumeIDs: int
        """

        connection_type = "Cluster"
        self._check_connection_type(connection_type)

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
            params["volumeIDs"] = volume_ids
        
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
            limit=OPTIONAL,):
        """
        ListVolumesForAccount returns the list of active AND (pending) deleted volumes for an account.
        :param accountID: [required] The ID of the account to list the volumes for.
        :type accountID: int
        
        :param startVolumeID:  [&#x27;The ID of the first volume to list.&#x27;, &#x27;This can be useful for paging results.&#x27;, &#x27;By default, this starts at the lowest VolumeID.&#x27;][&#x27;The ID of the first volume to list.&#x27;, &#x27;This can be useful for paging results.&#x27;, &#x27;By default, this starts at the lowest VolumeID.&#x27;][&#x27;The ID of the first volume to list.&#x27;, &#x27;This can be useful for paging results.&#x27;, &#x27;By default, this starts at the lowest VolumeID.&#x27;]
        :type startVolumeID: int
        
        :param limit:  [&#x27;The maximum number of volumes to return from the API.&#x27;]
        :type limit: int
        """

        connection_type = "Cluster"
        self._check_connection_type(connection_type)

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
            params
        )

    def list_volume_stats_by_account(
            self,):
        """
        ListVolumeStatsByAccount returns high-level activity measurements for every account.
        Values are summed from all the volumes owned by the account."""

        connection_type = "Cluster"
        self._check_connection_type(connection_type)

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'ListVolumeStatsByAccount',
            ListVolumeStatsByAccountResult,
            params
        )

    def list_volume_stats_by_volume(
            self,):
        """
        ListVolumeStatsByVolume returns high-level activity measurements for every volume, by volume.
        Values are cumulative from the creation of the volume."""

        connection_type = "Cluster"
        self._check_connection_type(connection_type)

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'ListVolumeStatsByVolume',
            ListVolumeStatsByVolumeResult,
            params
        )

    def list_volume_stats_by_volume_access_group(
            self,
            volume_access_groups=OPTIONAL,):
        """
        ListVolumeStatsByVolumeAccessGroup is used to get total activity measurements for all of the volumes that are a member of the specified volume access group(s).
        :param volumeAccessGroups:  [&#x27;An array of VolumeAccessGroupIDs for which volume activity is returned.&#x27;, &#x27;If no VolumeAccessGroupID is specified, stats for all volume access groups is returned.&#x27;][&#x27;An array of VolumeAccessGroupIDs for which volume activity is returned.&#x27;, &#x27;If no VolumeAccessGroupID is specified, stats for all volume access groups is returned.&#x27;]
        :type volumeAccessGroups: int
        """

        connection_type = "Cluster"
        self._check_connection_type(connection_type)

        params = { 
        }
        if volume_access_groups is not None:
            params["volumeAccessGroups"] = volume_access_groups
        
        # There is no adaptor.
        return self.send_request(
            'ListVolumeStatsByVolumeAccessGroup',
            ListVolumeStatsByVolumeAccessGroupResult,
            params
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
        <br/><br/>
        Extending the size of a volume that is being replicated should be done in an order.
        The target (Replication Target) volume should first be increased in size, then the source (Read/Write) volume can be resized.
        It is recommended that both the target and the source volumes be the same size.
        <br/><br/>
        <b>Note</b>: If you change access status to locked or target all existing iSCSI connections are terminated.
        :param volumeID: [required] VolumeID for the volume to be modified.
        :type volumeID: int
        
        :param accountID:  [&#x27;AccountID to which the volume is reassigned.&#x27;, &#x27;If none is specified, the previous account name is used.&#x27;][&#x27;AccountID to which the volume is reassigned.&#x27;, &#x27;If none is specified, the previous account name is used.&#x27;]
        :type accountID: int
        
        :param access:  [&#x27;Access allowed for the volume.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;readOnly&lt;/b&gt;: Only read operations are allowed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;readWrite&lt;/b&gt;: Reads and writes are allowed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;locked&lt;/b&gt;: No reads or writes are allowed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;replicationTarget&lt;/b&gt;: Identify a volume as the target volume for a paired set of volumes. If the volume is not paired, the access status is locked.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;If unspecified, the access settings of the clone will be the same as the source.&#x27;][&#x27;Access allowed for the volume.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;readOnly&lt;/b&gt;: Only read operations are allowed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;readWrite&lt;/b&gt;: Reads and writes are allowed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;locked&lt;/b&gt;: No reads or writes are allowed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;replicationTarget&lt;/b&gt;: Identify a volume as the target volume for a paired set of volumes. If the volume is not paired, the access status is locked.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;If unspecified, the access settings of the clone will be the same as the source.&#x27;][&#x27;Access allowed for the volume.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;readOnly&lt;/b&gt;: Only read operations are allowed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;readWrite&lt;/b&gt;: Reads and writes are allowed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;locked&lt;/b&gt;: No reads or writes are allowed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;replicationTarget&lt;/b&gt;: Identify a volume as the target volume for a paired set of volumes. If the volume is not paired, the access status is locked.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;If unspecified, the access settings of the clone will be the same as the source.&#x27;][&#x27;Access allowed for the volume.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;readOnly&lt;/b&gt;: Only read operations are allowed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;readWrite&lt;/b&gt;: Reads and writes are allowed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;locked&lt;/b&gt;: No reads or writes are allowed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;replicationTarget&lt;/b&gt;: Identify a volume as the target volume for a paired set of volumes. If the volume is not paired, the access status is locked.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;If unspecified, the access settings of the clone will be the same as the source.&#x27;][&#x27;Access allowed for the volume.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;readOnly&lt;/b&gt;: Only read operations are allowed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;readWrite&lt;/b&gt;: Reads and writes are allowed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;locked&lt;/b&gt;: No reads or writes are allowed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;replicationTarget&lt;/b&gt;: Identify a volume as the target volume for a paired set of volumes. If the volume is not paired, the access status is locked.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;If unspecified, the access settings of the clone will be the same as the source.&#x27;][&#x27;Access allowed for the volume.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;readOnly&lt;/b&gt;: Only read operations are allowed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;readWrite&lt;/b&gt;: Reads and writes are allowed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;locked&lt;/b&gt;: No reads or writes are allowed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;replicationTarget&lt;/b&gt;: Identify a volume as the target volume for a paired set of volumes. If the volume is not paired, the access status is locked.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;If unspecified, the access settings of the clone will be the same as the source.&#x27;][&#x27;Access allowed for the volume.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;readOnly&lt;/b&gt;: Only read operations are allowed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;readWrite&lt;/b&gt;: Reads and writes are allowed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;locked&lt;/b&gt;: No reads or writes are allowed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;replicationTarget&lt;/b&gt;: Identify a volume as the target volume for a paired set of volumes. If the volume is not paired, the access status is locked.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;If unspecified, the access settings of the clone will be the same as the source.&#x27;]
        :type access: str
        
        :param qos:  New quality of service settings for this volume.
        :type qos: QoS
        
        :param totalSize:  [&#x27;New size of the volume in bytes.&#x27;, &#x27;Size is rounded up to the nearest 1MiB size.&#x27;, &#x27;This parameter can only be used to *increase* the size of a volume.&#x27;][&#x27;New size of the volume in bytes.&#x27;, &#x27;Size is rounded up to the nearest 1MiB size.&#x27;, &#x27;This parameter can only be used to *increase* the size of a volume.&#x27;][&#x27;New size of the volume in bytes.&#x27;, &#x27;Size is rounded up to the nearest 1MiB size.&#x27;, &#x27;This parameter can only be used to *increase* the size of a volume.&#x27;]
        :type totalSize: int
        
        :param attributes:  List of Name/Value pairs in JSON object format.
        :type attributes: dict
        """

        connection_type = "Cluster"
        self._check_connection_type(connection_type)

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
            params
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

        connection_type = "Cluster"
        self._check_connection_type(connection_type)

        params = { 
            "volumeID": volume_id,
        }
        
        # There is no adaptor.
        return self.send_request(
            'PurgeDeletedVolume',
            PurgeDeletedVolumeResult,
            params
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

        connection_type = "Cluster"
        self._check_connection_type(connection_type)

        params = { 
            "volumeID": volume_id,
        }
        
        # There is no adaptor.
        return self.send_request(
            'RestoreDeletedVolume',
            RestoreDeletedVolumeResult,
            params
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
        Communications and server interaction information for external data access is passed by a script running on the SolidFire storage system.<br/>
        <br/>
        At the start of a bulk volume read operation, a snapshot of the volume is made and the snapshot is deleted when the read has completed.
        You can also read a snapshot of the volume by entering the ID of the snapshot as a parameter.
        Reading a previous snapshot does not create a new snapshot of the volume, nor does the previous snapshot be deleted when the read completes.<br/>
        <br/>
        <b>Note</b>: This process creates a new snapshot if the ID of an existing snapshot is not provided.
        Snapshots can be created if cluster fullness is at stage 2 or 3.
        Snapshots are not created when cluster fullness is at stage 4 or 5.
        :param volumeID: [required] ID of the volume to be read.
        :type volumeID: int
        
        :param format: [required] [&#x27;The format of the volume data. Can be either:&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;uncompressed&lt;/b&gt;: every byte of the volume is returned without any compression.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;native&lt;/b&gt;: opaque data is returned that is smaller and more efficiently stored and written on a subsequent bulk volume write.&#x27;][&#x27;The format of the volume data. Can be either:&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;uncompressed&lt;/b&gt;: every byte of the volume is returned without any compression.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;native&lt;/b&gt;: opaque data is returned that is smaller and more efficiently stored and written on a subsequent bulk volume write.&#x27;][&#x27;The format of the volume data. Can be either:&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;uncompressed&lt;/b&gt;: every byte of the volume is returned without any compression.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;native&lt;/b&gt;: opaque data is returned that is smaller and more efficiently stored and written on a subsequent bulk volume write.&#x27;]
        :type format: str
        
        :param snapshotID:  [&#x27;ID of a previously created snapshot used for bulk volume reads.&#x27;, &#x27;If no ID is entered, a snapshot of the current active volume image is made.&#x27;][&#x27;ID of a previously created snapshot used for bulk volume reads.&#x27;, &#x27;If no ID is entered, a snapshot of the current active volume image is made.&#x27;]
        :type snapshotID: int
        
        :param script:  [&#x27;Executable name of a script.&#x27;, &#x27;If no script name is given then the key and URL is necessary to access SolidFire nodes.&#x27;, &#x27;The script is run on the primary node and the key and URL is returned to the script so the local web server can be contacted.&#x27;][&#x27;Executable name of a script.&#x27;, &#x27;If no script name is given then the key and URL is necessary to access SolidFire nodes.&#x27;, &#x27;The script is run on the primary node and the key and URL is returned to the script so the local web server can be contacted.&#x27;][&#x27;Executable name of a script.&#x27;, &#x27;If no script name is given then the key and URL is necessary to access SolidFire nodes.&#x27;, &#x27;The script is run on the primary node and the key and URL is returned to the script so the local web server can be contacted.&#x27;]
        :type script: str
        
        :param scriptParameters:  [&#x27;JSON parameters to pass to the script.&#x27;]
        :type scriptParameters: str
        
        :param attributes:  [&#x27;JSON attributes for the bulk volume job.&#x27;]
        :type attributes: dict
        """

        connection_type = "Cluster"
        self._check_connection_type(connection_type)

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
            params
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
        
        :param format: [required] [&#x27;The format of the volume data. Can be either:&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;uncompressed&lt;/b&gt;: every byte of the volume is returned without any compression.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;native&lt;/b&gt;: opaque data is returned that is smaller and more efficiently stored and written on a subsequent bulk volume write&#x27;][&#x27;The format of the volume data. Can be either:&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;uncompressed&lt;/b&gt;: every byte of the volume is returned without any compression.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;native&lt;/b&gt;: opaque data is returned that is smaller and more efficiently stored and written on a subsequent bulk volume write&#x27;][&#x27;The format of the volume data. Can be either:&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;uncompressed&lt;/b&gt;: every byte of the volume is returned without any compression.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;native&lt;/b&gt;: opaque data is returned that is smaller and more efficiently stored and written on a subsequent bulk volume write&#x27;]
        :type format: str
        
        :param script:  [&#x27;Executable name of a script.&#x27;, &#x27;If no script name is given then the key and URL are necessary to access SolidFire nodes.&#x27;, &#x27;The script runs on the primary node and the key and URL is returned to the script so the local web server can be contacted.&#x27;][&#x27;Executable name of a script.&#x27;, &#x27;If no script name is given then the key and URL are necessary to access SolidFire nodes.&#x27;, &#x27;The script runs on the primary node and the key and URL is returned to the script so the local web server can be contacted.&#x27;][&#x27;Executable name of a script.&#x27;, &#x27;If no script name is given then the key and URL are necessary to access SolidFire nodes.&#x27;, &#x27;The script runs on the primary node and the key and URL is returned to the script so the local web server can be contacted.&#x27;]
        :type script: str
        
        :param scriptParameters:  [&#x27;JSON parameters to pass to the script.&#x27;]
        :type scriptParameters: str
        
        :param attributes:  [&#x27;JSON attributes for the bulk volume job.&#x27;]
        :type attributes: dict
        """

        connection_type = "Cluster"
        self._check_connection_type(connection_type)

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
            params
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
        :param key: [required] The key assigned during initialization of a &quot;StartBulkVolumeRead&quot; or &quot;StartBulkVolumeWrite&quot; session.
        :type key: str
        
        :param status: [required] [&#x27;The SolidFire system sets the status of the given bulk volume job.&lt;br/&gt;&#x27;, &#x27;Possible values:&lt;br/&gt;&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;running&lt;/b&gt;: jobs that are still active.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;complete&lt;/b&gt;: jobs that are done. failed - jobs that have failed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;failed&lt;/b&gt;: jobs that have failed.&#x27;][&#x27;The SolidFire system sets the status of the given bulk volume job.&lt;br/&gt;&#x27;, &#x27;Possible values:&lt;br/&gt;&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;running&lt;/b&gt;: jobs that are still active.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;complete&lt;/b&gt;: jobs that are done. failed - jobs that have failed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;failed&lt;/b&gt;: jobs that have failed.&#x27;][&#x27;The SolidFire system sets the status of the given bulk volume job.&lt;br/&gt;&#x27;, &#x27;Possible values:&lt;br/&gt;&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;running&lt;/b&gt;: jobs that are still active.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;complete&lt;/b&gt;: jobs that are done. failed - jobs that have failed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;failed&lt;/b&gt;: jobs that have failed.&#x27;][&#x27;The SolidFire system sets the status of the given bulk volume job.&lt;br/&gt;&#x27;, &#x27;Possible values:&lt;br/&gt;&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;running&lt;/b&gt;: jobs that are still active.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;complete&lt;/b&gt;: jobs that are done. failed - jobs that have failed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;failed&lt;/b&gt;: jobs that have failed.&#x27;][&#x27;The SolidFire system sets the status of the given bulk volume job.&lt;br/&gt;&#x27;, &#x27;Possible values:&lt;br/&gt;&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;running&lt;/b&gt;: jobs that are still active.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;complete&lt;/b&gt;: jobs that are done. failed - jobs that have failed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;failed&lt;/b&gt;: jobs that have failed.&#x27;]
        :type status: str
        
        :param percentComplete:  [&#x27;The completed progress of the bulk volume job as a percentage.&#x27;]
        :type percentComplete: str
        
        :param message:  [&#x27;Returns the status of the bulk volume job when the job has completed.&#x27;]
        :type message: str
        
        :param attributes:  [&#x27;JSON attributes  updates what is on the bulk volume job.&#x27;]
        :type attributes: dict
        """

        connection_type = "Cluster"
        self._check_connection_type(connection_type)

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
            params
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
        :param name: [required] [&#x27;Name of the volume access group.&#x27;, &#x27;It is not required to be unique, but recommended.&#x27;][&#x27;Name of the volume access group.&#x27;, &#x27;It is not required to be unique, but recommended.&#x27;]
        :type name: str
        
        :param initiators:  [&#x27;List of initiators to include in the volume access group.&#x27;, &#x27;If unspecified, the access group will start out without configured initiators.&#x27;][&#x27;List of initiators to include in the volume access group.&#x27;, &#x27;If unspecified, the access group will start out without configured initiators.&#x27;]
        :type initiators: str
        
        :param volumes:  [&#x27;List of volumes to initially include in the volume access group.&#x27;, &#x27;If unspecified, the access group will start without any volumes.&#x27;][&#x27;List of volumes to initially include in the volume access group.&#x27;, &#x27;If unspecified, the access group will start without any volumes.&#x27;]
        :type volumes: int
        
        :param virtualNetworkID:  The ID of the SolidFire Virtual Network ID to associate the volume access group with.
        :type virtualNetworkID: int
        
        :param virtualNetworkTags:  The ID of the VLAN Virtual Network Tag to associate the volume access group with.
        :type virtualNetworkTags: int
        
        :param attributes:  List of Name/Value pairs in JSON object format.
        :type attributes: dict
        """

        connection_type = "Cluster"
        self._check_connection_type(connection_type)

        params = { 
            "name": name,
        }
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
        
        # There is no adaptor.
        return self.send_request(
            'CreateVolumeAccessGroup',
            CreateVolumeAccessGroupResult,
            params
        )

    def list_volume_access_groups(
            self,
            start_volume_access_group_id=OPTIONAL,
            limit=OPTIONAL,):
        """
        ListVolumeAccessGroups is used to return information about the volume access groups that are currently in the system.
        :param startVolumeAccessGroupID:  [&#x27;The lowest VolumeAccessGroupID to return.&#x27;, &#x27;This can be useful for paging.&#x27;, &#x27;If unspecified, there is no lower limit (implicitly 0).&#x27;][&#x27;The lowest VolumeAccessGroupID to return.&#x27;, &#x27;This can be useful for paging.&#x27;, &#x27;If unspecified, there is no lower limit (implicitly 0).&#x27;][&#x27;The lowest VolumeAccessGroupID to return.&#x27;, &#x27;This can be useful for paging.&#x27;, &#x27;If unspecified, there is no lower limit (implicitly 0).&#x27;]
        :type startVolumeAccessGroupID: int
        
        :param limit:  [&#x27;The maximum number of results to return.&#x27;, &#x27;This can be useful for paging.&#x27;][&#x27;The maximum number of results to return.&#x27;, &#x27;This can be useful for paging.&#x27;]
        :type limit: int
        """

        connection_type = "Cluster"
        self._check_connection_type(connection_type)

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
            params
        )

    def delete_volume_access_group(
            self,
            volume_access_group_id,):
        """
        Delete a volume access group from the system.
        :param volumeAccessGroupID: [required] [&#x27;The ID of the volume access group to delete.&#x27;]
        :type volumeAccessGroupID: int
        """

        connection_type = "Cluster"
        self._check_connection_type(connection_type)

        params = { 
            "volumeAccessGroupID": volume_access_group_id,
        }
        
        # There is no adaptor.
        return self.send_request(
            'DeleteVolumeAccessGroup',
            DeleteVolumeAccessGroupResult,
            params
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
        <br/><br/>
        Often, it is easier to use the convenience functions to modify initiators and volumes independently:
        <br/><br/>
        AddInitiatorsToVolumeAccessGroup<br/>
        RemoveInitiatorsFromVolumeAccessGroup<br/>
        AddVolumesToVolumeAccessGroup<br/>
        RemoveVolumesFromVolumeAccessGroup<br/>
        :param volumeAccessGroupID: [required] The ID of the volume access group to modify.
        :type volumeAccessGroupID: int
        
        :param virtualNetworkID:  The ID of the SolidFire Virtual Network ID to associate the volume access group with.
        :type virtualNetworkID: int
        
        :param virtualNetworkTags:  The ID of the VLAN Virtual Network Tag to associate the volume access group with.
        :type virtualNetworkTags: int
        
        :param name:  [&#x27;Name of the volume access group.&#x27;, &#x27;It is not required to be unique, but recommended.&#x27;][&#x27;Name of the volume access group.&#x27;, &#x27;It is not required to be unique, but recommended.&#x27;]
        :type name: str
        
        :param initiators:  [&#x27;List of initiators to include in the volume access group.&#x27;, &quot;If unspecified, the access group&#x27;s configured initiators will not be modified.&quot;][&#x27;List of initiators to include in the volume access group.&#x27;, &quot;If unspecified, the access group&#x27;s configured initiators will not be modified.&quot;]
        :type initiators: str
        
        :param volumes:  [&#x27;List of volumes to initially include in the volume access group.&#x27;, &quot;If unspecified, the access group&#x27;s volumes will not be modified.&quot;][&#x27;List of volumes to initially include in the volume access group.&#x27;, &quot;If unspecified, the access group&#x27;s volumes will not be modified.&quot;]
        :type volumes: int
        
        :param attributes:  List of Name/Value pairs in JSON object format.
        :type attributes: dict
        """

        connection_type = "Cluster"
        self._check_connection_type(connection_type)

        params = { 
            "volumeAccessGroupID": volume_access_group_id,
        }
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
        
        # There is no adaptor.
        return self.send_request(
            'ModifyVolumeAccessGroup',
            ModifyVolumeAccessGroupResult,
            params
        )

    def add_initiators_to_volume_access_group(
            self,
            volume_access_group_id,
            initiators,):
        """
        Add initiators to a volume access group.
        :param volumeAccessGroupID: [required] The ID of the volume access group to modify.
        :type volumeAccessGroupID: int
        
        :param initiators: [required] [&#x27;List of initiators to add to the volume access group.&#x27;]
        :type initiators: str
        """

        connection_type = "Cluster"
        self._check_connection_type(connection_type)

        params = { 
            "volumeAccessGroupID": volume_access_group_id,
            "initiators": initiators,
        }
        
        # There is no adaptor.
        return self.send_request(
            'AddInitiatorsToVolumeAccessGroup',
            ModifyVolumeAccessGroupResult,
            params
        )

    def remove_initiators_from_volume_access_group(
            self,
            volume_access_group_id,
            initiators,):
        """
        Remove initiators from a volume access group.
        :param volumeAccessGroupID: [required] The ID of the volume access group to modify.
        :type volumeAccessGroupID: int
        
        :param initiators: [required] [&#x27;List of initiators to remove from the volume access group.&#x27;]
        :type initiators: str
        """

        connection_type = "Cluster"
        self._check_connection_type(connection_type)

        params = { 
            "volumeAccessGroupID": volume_access_group_id,
            "initiators": initiators,
        }
        
        # There is no adaptor.
        return self.send_request(
            'RemoveInitiatorsFromVolumeAccessGroup',
            ModifyVolumeAccessGroupResult,
            params
        )

    def add_volumes_to_volume_access_group(
            self,
            volume_access_group_id,
            volumes,):
        """
        Add volumes to a volume access group.
        :param volumeAccessGroupID: [required] The ID of the volume access group to modify.
        :type volumeAccessGroupID: int
        
        :param volumes: [required] [&#x27;List of volumes to add to this volume access group.&#x27;]
        :type volumes: int
        """

        connection_type = "Cluster"
        self._check_connection_type(connection_type)

        params = { 
            "volumeAccessGroupID": volume_access_group_id,
            "volumes": volumes,
        }
        
        # There is no adaptor.
        return self.send_request(
            'AddVolumesToVolumeAccessGroup',
            ModifyVolumeAccessGroupResult,
            params
        )

    def remove_volumes_from_volume_access_group(
            self,
            volume_access_group_id,
            volumes,):
        """
        Remove volumes from a volume access group.
        :param volumeAccessGroupID: [required] The ID of the volume access group to modify.
        :type volumeAccessGroupID: int
        
        :param volumes: [required] [&#x27;List of volumes to remove from this volume access group.&#x27;]
        :type volumes: int
        """

        connection_type = "Cluster"
        self._check_connection_type(connection_type)

        params = { 
            "volumeAccessGroupID": volume_access_group_id,
            "volumes": volumes,
        }
        
        # There is no adaptor.
        return self.send_request(
            'RemoveVolumesFromVolumeAccessGroup',
            ModifyVolumeAccessGroupResult,
            params
        )

    def get_volume_access_group_efficiency(
            self,
            volume_access_group_id,):
        """
        GetVolumeAccessGroupEfficiency is used to retrieve efficiency information about a volume access group. Only the volume access group provided as parameters in this API method is used to compute the capacity.
        :param volumeAccessGroupID: [required] Specifies the volume access group for which capacity is computed.
        :type volumeAccessGroupID: int
        """

        connection_type = "Cluster"
        self._check_connection_type(connection_type)

        params = { 
            "volumeAccessGroupID": volume_access_group_id,
        }
        
        # There is no adaptor.
        return self.send_request(
            'GetVolumeAccessGroupEfficiency',
            GetEfficiencyResult,
            params
        )

    def get_volume_access_group_lun_assignments(
            self,
            volume_access_group_id,):
        """
        The GetVolumeAccessGroupLunAssignments is used to return information LUN mappings of a specified volume access group.
        :param volumeAccessGroupID: [required] Unique volume access group ID used to return information.
        :type volumeAccessGroupID: int
        """

        connection_type = "Cluster"
        self._check_connection_type(connection_type)

        params = { 
            "volumeAccessGroupID": volume_access_group_id,
        }
        
        # There is no adaptor.
        return self.send_request(
            'GetVolumeAccessGroupLunAssignments',
            GetVolumeAccessGroupLunAssignmentsResult,
            params
        )

    def modify_volume_access_group_lun_assignments(
            self,
            volume_access_group_id,
            lun_assignments,):
        """
        The ModifytVolumeAccessGroupLunAssignments is used to define custom LUN assignments for specific volumes. Only LUN values set on the lunAssignments parameter will be changed in the volume access group. All other LUN assignments will remain unchanged.
        <br/><br/>
        LUN assignment values must be unique for volumes in a volume access group. An exception will be seen if LUN assignments are duplicated in a volume access group. However, the same LUN values can be used again in different volume access groups.
        <br/><br/>
        <b>Note:</b> Correct LUN values are 0 - 16383. An exception will be seen if an incorrect LUN value is passed. None of the specified LUN assignments will be modified if there is an exception.
        <br/><br/>
        <b>Caution:</b> If a LUN assignment is changed for a volume with active I/O, the I/O could be disrupted. Changes to the server configuration may be required in order to change volume LUN assignments.
        :param volumeAccessGroupID: [required] Unique volume access group ID for which the LUN assignments will be modified.
        :type volumeAccessGroupID: int
        
        :param lunAssignments: [required] The volume IDs with new assigned LUN values.
        :type lunAssignments: LunAssignment
        """

        connection_type = "Cluster"
        self._check_connection_type(connection_type)

        params = { 
            "volumeAccessGroupID": volume_access_group_id,
            "lunAssignments": lun_assignments,
        }
        
        # There is no adaptor.
        return self.send_request(
            'ModifyVolumeAccessGroupLunAssignments',
            ModifyVolumeAccessGroupLunAssignmentsResult,
            params
        )

