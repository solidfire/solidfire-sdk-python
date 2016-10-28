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
            initiatorSecret=OPTIONAL,
            targetSecret=OPTIONAL,
            attributes=OPTIONAL,):
        """
        [&#x27;Used to add a new account to the system.&#x27;, &#x27;New volumes can be created under the new account.&#x27;, &#x27;The CHAP settings specified for the account applies to all volumes owned by the account.&#x27;]
        [&#x27;Used to add a new account to the system.&#x27;, &#x27;New volumes can be created under the new account.&#x27;, &#x27;The CHAP settings specified for the account applies to all volumes owned by the account.&#x27;]
        [&#x27;Used to add a new account to the system.&#x27;, &#x27;New volumes can be created under the new account.&#x27;, &#x27;The CHAP settings specified for the account applies to all volumes owned by the account.&#x27;]
        :param username: [required] [&#x27;Unique username for this account.&#x27;, &#x27;(May be 1 to 64 characters in length).&#x27;][&#x27;Unique username for this account.&#x27;, &#x27;(May be 1 to 64 characters in length).&#x27;]
        :type username: 
        
        :param initiatorSecret:  [&#x27;CHAP secret to use for the initiator.&#x27;, &#x27;Should be 12-16 characters long and impenetrable.&#x27;, &#x27;The CHAP initiator secrets must be unique and cannot be the same as the target CHAP secret.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;If not specified, a random secret is created.&#x27;][&#x27;CHAP secret to use for the initiator.&#x27;, &#x27;Should be 12-16 characters long and impenetrable.&#x27;, &#x27;The CHAP initiator secrets must be unique and cannot be the same as the target CHAP secret.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;If not specified, a random secret is created.&#x27;][&#x27;CHAP secret to use for the initiator.&#x27;, &#x27;Should be 12-16 characters long and impenetrable.&#x27;, &#x27;The CHAP initiator secrets must be unique and cannot be the same as the target CHAP secret.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;If not specified, a random secret is created.&#x27;][&#x27;CHAP secret to use for the initiator.&#x27;, &#x27;Should be 12-16 characters long and impenetrable.&#x27;, &#x27;The CHAP initiator secrets must be unique and cannot be the same as the target CHAP secret.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;If not specified, a random secret is created.&#x27;][&#x27;CHAP secret to use for the initiator.&#x27;, &#x27;Should be 12-16 characters long and impenetrable.&#x27;, &#x27;The CHAP initiator secrets must be unique and cannot be the same as the target CHAP secret.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;If not specified, a random secret is created.&#x27;]
        :type initiatorSecret: 
        
        :param targetSecret:  [&#x27;CHAP secret to use for the target (mutual CHAP authentication).&#x27;, &#x27;Should be 12-16 characters long and impenetrable.&#x27;, &#x27;The CHAP target secrets must be unique and cannot be the same as the initiator CHAP secret.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;If not specified, a random secret is created.&#x27;][&#x27;CHAP secret to use for the target (mutual CHAP authentication).&#x27;, &#x27;Should be 12-16 characters long and impenetrable.&#x27;, &#x27;The CHAP target secrets must be unique and cannot be the same as the initiator CHAP secret.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;If not specified, a random secret is created.&#x27;][&#x27;CHAP secret to use for the target (mutual CHAP authentication).&#x27;, &#x27;Should be 12-16 characters long and impenetrable.&#x27;, &#x27;The CHAP target secrets must be unique and cannot be the same as the initiator CHAP secret.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;If not specified, a random secret is created.&#x27;][&#x27;CHAP secret to use for the target (mutual CHAP authentication).&#x27;, &#x27;Should be 12-16 characters long and impenetrable.&#x27;, &#x27;The CHAP target secrets must be unique and cannot be the same as the initiator CHAP secret.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;If not specified, a random secret is created.&#x27;][&#x27;CHAP secret to use for the target (mutual CHAP authentication).&#x27;, &#x27;Should be 12-16 characters long and impenetrable.&#x27;, &#x27;The CHAP target secrets must be unique and cannot be the same as the initiator CHAP secret.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;If not specified, a random secret is created.&#x27;]
        :type targetSecret: 
        
        :param attributes:  List of Name/Value pairs in JSON object format.
        :type attributes: 
        """

        params = { 
            "username": username,
        }
        if initiatorSecret is not None:
            params["initiatorSecret"] = initiatorSecret
        if targetSecret is not None:
            params["targetSecret"] = targetSecret
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
            accountID,):
        """
        Returns details about an account, given its AccountID.
        :param accountID: [required] Specifies the account for which details are gathered.
        :type accountID: 
        """

        params = { 
            "accountID": accountID,
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
        :type username: 
        """

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
            startAccountID=OPTIONAL,
            limit=OPTIONAL,):
        """
        Returns the entire list of accounts, with optional paging support.
        :param startAccountID:  [&#x27;Starting AccountID to return.&#x27;, &#x27;If no Account exists with this AccountID,&#x27;, &#x27;the next Account by AccountID order is used as the start of the list.&#x27;, &#x27;To page through the list, pass the AccountID of the last Account in the previous response + 1&#x27;][&#x27;Starting AccountID to return.&#x27;, &#x27;If no Account exists with this AccountID,&#x27;, &#x27;the next Account by AccountID order is used as the start of the list.&#x27;, &#x27;To page through the list, pass the AccountID of the last Account in the previous response + 1&#x27;][&#x27;Starting AccountID to return.&#x27;, &#x27;If no Account exists with this AccountID,&#x27;, &#x27;the next Account by AccountID order is used as the start of the list.&#x27;, &#x27;To page through the list, pass the AccountID of the last Account in the previous response + 1&#x27;][&#x27;Starting AccountID to return.&#x27;, &#x27;If no Account exists with this AccountID,&#x27;, &#x27;the next Account by AccountID order is used as the start of the list.&#x27;, &#x27;To page through the list, pass the AccountID of the last Account in the previous response + 1&#x27;]
        :type startAccountID: 
        
        :param limit:  Maximum number of AccountInfo objects to return.
        :type limit: 
        """

        params = { 
        }
        if startAccountID is not None:
            params["startAccountID"] = startAccountID
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
            accountID,
            username=OPTIONAL,
            status=OPTIONAL,
            initiatorSecret=OPTIONAL,
            targetSecret=OPTIONAL,
            attributes=OPTIONAL,):
        """
        [&#x27;Used to modify an existing account.&#x27;, &#x27;When locking an account, any existing connections from that account are immediately terminated.&#x27;, &#x27;When changing CHAP settings, any existing connections continue to be active,&#x27;, &#x27;and the new CHAP values are only used on subsequent connection or reconnection.&#x27;]
        [&#x27;Used to modify an existing account.&#x27;, &#x27;When locking an account, any existing connections from that account are immediately terminated.&#x27;, &#x27;When changing CHAP settings, any existing connections continue to be active,&#x27;, &#x27;and the new CHAP values are only used on subsequent connection or reconnection.&#x27;]
        [&#x27;Used to modify an existing account.&#x27;, &#x27;When locking an account, any existing connections from that account are immediately terminated.&#x27;, &#x27;When changing CHAP settings, any existing connections continue to be active,&#x27;, &#x27;and the new CHAP values are only used on subsequent connection or reconnection.&#x27;]
        [&#x27;Used to modify an existing account.&#x27;, &#x27;When locking an account, any existing connections from that account are immediately terminated.&#x27;, &#x27;When changing CHAP settings, any existing connections continue to be active,&#x27;, &#x27;and the new CHAP values are only used on subsequent connection or reconnection.&#x27;]
        :param accountID: [required] AccountID for the account to modify.
        :type accountID: 
        
        :param username:  Change the username of the account to this value.
        :type username: 
        
        :param status:  Status of the account.
        :type status: 
        
        :param initiatorSecret:  [&#x27;CHAP secret to use for the initiator.&#x27;, &#x27;Should be 12-16 characters long and impenetrable.&#x27;][&#x27;CHAP secret to use for the initiator.&#x27;, &#x27;Should be 12-16 characters long and impenetrable.&#x27;]
        :type initiatorSecret: 
        
        :param targetSecret:  [&#x27;CHAP secret to use for the target (mutual CHAP authentication).&#x27;, &#x27;Should be 12-16 characters long and impenetrable.&#x27;][&#x27;CHAP secret to use for the target (mutual CHAP authentication).&#x27;, &#x27;Should be 12-16 characters long and impenetrable.&#x27;]
        :type targetSecret: 
        
        :param attributes:  List of Name/Value pairs in JSON object format.
        :type attributes: 
        """

        params = { 
            "accountID": accountID,
        }
        if username is not None:
            params["username"] = username
        if status is not None:
            params["status"] = status
        if initiatorSecret is not None:
            params["initiatorSecret"] = initiatorSecret
        if targetSecret is not None:
            params["targetSecret"] = targetSecret
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
            accountID,):
        """
        [&#x27;Used to remove an existing account.&#x27;, &#x27;All Volumes must be deleted and purged on the account before it can be removed.&#x27;, &#x27;If volumes on the account are still pending deletion, RemoveAccount cannot be used until DeleteVolume to delete and purge the volumes.&#x27;]
        [&#x27;Used to remove an existing account.&#x27;, &#x27;All Volumes must be deleted and purged on the account before it can be removed.&#x27;, &#x27;If volumes on the account are still pending deletion, RemoveAccount cannot be used until DeleteVolume to delete and purge the volumes.&#x27;]
        [&#x27;Used to remove an existing account.&#x27;, &#x27;All Volumes must be deleted and purged on the account before it can be removed.&#x27;, &#x27;If volumes on the account are still pending deletion, RemoveAccount cannot be used until DeleteVolume to delete and purge the volumes.&#x27;]
        :param accountID: [required] AccountID for the account to remove.
        :type accountID: 
        """

        params = { 
            "accountID": accountID,
        }
        
        # There is no adaptor.
        return self.send_request(
            'RemoveAccount',
            RemoveAccountResult,
            params
        )

    def get_account_efficiency(
            self,
            accountID,
            force=OPTIONAL,):
        """
        GetAccountEfficiency is used to retrieve information about a volume account. Only the account given as a parameter in this API method is used to compute the capacity.
        :param accountID: [required] Specifies the volume account for which capacity is computed.
        :type accountID: 
        
        :param force:  
        :type force: 
        """

        params = { 
            "accountID": accountID,
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
        [&#x27;CreateBackupTarget allows you to create and store backup target information so that you do not need to re-enter it each time a backup is created.&#x27;]
        :param name: [required] [&#x27;Name for the backup target.&#x27;]
        :type name: 
        
        :param attributes:  List of Name/Value pairs in JSON object format.
        :type attributes: 
        """

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
            backupTargetID,):
        """
        GetBackupTarget allows you to return information about a specific backup target that has been created.
        :param backupTargetID: [required] [&#x27;Unique identifier assigned to the backup target.&#x27;]
        :type backupTargetID: 
        """

        params = { 
            "backupTargetID": backupTargetID,
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
            backupTargetID,
            name=OPTIONAL,
            attributes=OPTIONAL,):
        """
        ModifyBackupTarget is used to change attributes of a backup target.
        :param backupTargetID: [required] [&#x27;Unique identifier assigned to the backup target.&#x27;]
        :type backupTargetID: 
        
        :param name:  [&#x27;Name for the backup target.&#x27;]
        :type name: 
        
        :param attributes:  List of Name/Value pairs in JSON object format.
        :type attributes: 
        """

        params = { 
            "backupTargetID": backupTargetID,
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
            backupTargetID,):
        """
        [&#x27;RemoveBackupTarget allows you to delete backup targets.&#x27;]
        :param backupTargetID: [required] [&#x27;Unique target ID of the target to remove.&#x27;]
        :type backupTargetID: 
        """

        params = { 
            "backupTargetID": backupTargetID,
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
        [&#x27;Return the high-level capacity measurements for an entire cluster.&#x27;, &#x27;The fields returned from this method can be used to calculate the efficiency rates that are displayed in the Element User Interface.&#x27;]
        [&#x27;Return the high-level capacity measurements for an entire cluster.&#x27;, &#x27;The fields returned from this method can be used to calculate the efficiency rates that are displayed in the Element User Interface.&#x27;]"""

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
        [&#x27;Return information about the Element software version running on each node in the cluster.&#x27;, &#x27;Information about the nodes that are currently in the process of upgrading software is also returned.&#x27;]
        [&#x27;Return information about the Element software version running on each node in the cluster.&#x27;, &#x27;Information about the nodes that are currently in the process of upgrading software is also returned.&#x27;]"""

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
            maxEvents=OPTIONAL,
            startEventID=OPTIONAL,
            endEventID=OPTIONAL,
            eventQueueType=OPTIONAL,):
        """
        ListEvents returns events detected on the cluster, sorted from oldest to newest.
        :param maxEvents:  Specifies the maximum number of events to return.
        :type maxEvents: 
        
        :param startEventID:  Identifies the beginning of a range of events to return.
        :type startEventID: 
        
        :param endEventID:  Identifies the end of a range of events to return.
        :type endEventID: 
        
        :param eventQueueType:  
        :type eventQueueType: 
        """

        params = { 
        }
        if maxEvents is not None:
            params["maxEvents"] = maxEvents
        if startEventID is not None:
            params["startEventID"] = startEventID
        if endEventID is not None:
            params["endEventID"] = endEventID
        if eventQueueType is not None:
            params["eventQueueType"] = eventQueueType
        
        # There is no adaptor.
        return self.send_request(
            'ListEvents',
            ListEventsResult,
            params
        )

    def list_cluster_faults(
            self,
            exceptions=OPTIONAL,
            bestPractices=OPTIONAL,
            update=OPTIONAL,
            faultTypes=OPTIONAL,):
        """
        [&#x27;ListClusterFaults is used to retrieve information about any faults detected on the cluster.&#x27;, &#x27;With this method, both current and resolved faults can be retrieved. The system caches faults every 30 seconds.&#x27;]
        [&#x27;ListClusterFaults is used to retrieve information about any faults detected on the cluster.&#x27;, &#x27;With this method, both current and resolved faults can be retrieved. The system caches faults every 30 seconds.&#x27;]
        :param exceptions:  
        :type exceptions: 
        
        :param bestPractices:  [&#x27;Include faults triggered by sub-optimal system configuration.&#x27;, &#x27;Possible values: true, false&#x27;][&#x27;Include faults triggered by sub-optimal system configuration.&#x27;, &#x27;Possible values: true, false&#x27;]
        :type bestPractices: 
        
        :param update:  
        :type update: 
        
        :param faultTypes:  [&#x27;Determines the types of faults returned: current: List active, unresolved faults.&#x27;, &#x27;&lt;b&gt;resolved&lt;/b&gt;: List faults that were previously detected and resolved.&#x27;, &quot;&lt;b&gt;all&lt;/b&gt;: (Default) List both current and resolved faults. You can see the fault status in the &#x27;resolved&#x27; field of the Cluster Fault object.&quot;][&#x27;Determines the types of faults returned: current: List active, unresolved faults.&#x27;, &#x27;&lt;b&gt;resolved&lt;/b&gt;: List faults that were previously detected and resolved.&#x27;, &quot;&lt;b&gt;all&lt;/b&gt;: (Default) List both current and resolved faults. You can see the fault status in the &#x27;resolved&#x27; field of the Cluster Fault object.&quot;][&#x27;Determines the types of faults returned: current: List active, unresolved faults.&#x27;, &#x27;&lt;b&gt;resolved&lt;/b&gt;: List faults that were previously detected and resolved.&#x27;, &quot;&lt;b&gt;all&lt;/b&gt;: (Default) List both current and resolved faults. You can see the fault status in the &#x27;resolved&#x27; field of the Cluster Fault object.&quot;]
        :type faultTypes: 
        """

        params = { 
        }
        if exceptions is not None:
            params["exceptions"] = exceptions
        if bestPractices is not None:
            params["bestPractices"] = bestPractices
        if update is not None:
            params["update"] = update
        if faultTypes is not None:
            params["faultTypes"] = faultTypes
        
        # There is no adaptor.
        return self.send_request(
            'ListClusterFaults',
            ListClusterFaultsResult,
            params
        )

    def clear_cluster_faults(
            self,
            faultTypes=OPTIONAL,):
        """
        ClearClusterFaults is used to clear information about both current faults that are resolved as well as faults that were previously detected and resolved can be cleared.
        :param faultTypes:  [&#x27;Determines the types of faults cleared:&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;current&lt;/b&gt;: Faults that are currently detected and have not been resolved.&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;resolved&lt;/b&gt;: Faults that were previously detected and resolved.&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;all&lt;/b&gt;: Both current and resolved faults are cleared. The fault status can be determined by the &quot;resolved&quot; field of the fault object.&#x27;][&#x27;Determines the types of faults cleared:&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;current&lt;/b&gt;: Faults that are currently detected and have not been resolved.&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;resolved&lt;/b&gt;: Faults that were previously detected and resolved.&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;all&lt;/b&gt;: Both current and resolved faults are cleared. The fault status can be determined by the &quot;resolved&quot; field of the fault object.&#x27;][&#x27;Determines the types of faults cleared:&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;current&lt;/b&gt;: Faults that are currently detected and have not been resolved.&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;resolved&lt;/b&gt;: Faults that were previously detected and resolved.&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;all&lt;/b&gt;: Both current and resolved faults are cleared. The fault status can be determined by the &quot;resolved&quot; field of the fault object.&#x27;][&#x27;Determines the types of faults cleared:&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;current&lt;/b&gt;: Faults that are currently detected and have not been resolved.&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;resolved&lt;/b&gt;: Faults that were previously detected and resolved.&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;all&lt;/b&gt;: Both current and resolved faults are cleared. The fault status can be determined by the &quot;resolved&quot; field of the fault object.&#x27;]
        :type faultTypes: 
        """

        params = { 
        }
        if faultTypes is not None:
            params["faultTypes"] = faultTypes
        
        # There is no adaptor.
        return self.send_request(
            'ClearClusterFaults',
            ClearClusterFaultsResult,
            params
        )

    def get_cluster_config(
            self,):
        """
        [&#x27;The GetClusterConfig API method is used to return information about the cluster configuration this node uses to communicate with the cluster it is a part of.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Note&lt;/b&gt;: This method is available only through the per-node API endpoint 5.0 or later.&#x27;]
        [&#x27;The GetClusterConfig API method is used to return information about the cluster configuration this node uses to communicate with the cluster it is a part of.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Note&lt;/b&gt;: This method is available only through the per-node API endpoint 5.0 or later.&#x27;]
        [&#x27;The GetClusterConfig API method is used to return information about the cluster configuration this node uses to communicate with the cluster it is a part of.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Note&lt;/b&gt;: This method is available only through the per-node API endpoint 5.0 or later.&#x27;]"""

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
        [&#x27;GetClusterFullThreshold is used to view the stages set for cluster fullness levels. All levels are returned when this method is entered.&#x27;]"""

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
            stage2AwareThreshold=OPTIONAL,
            stage3BlockThresholdPercent=OPTIONAL,
            maxMetadataOverProvisionFactor=OPTIONAL,):
        """
        [&#x27;ModifyClusterFullThreshold is used to change the level at which an event is generated when the storage cluster approaches the capacity utilization requested. The number entered in this setting is used to indicate the number of node failures the system is required to recover from. For example, on a 10 node cluster, if you want to be alerted when the system cannot recover from 3 nodes failures, enter the value of &quot;3&quot;. When this number is reached, a message alert is sent to the Event Log in the Cluster Management Console.&#x27;]
        :param stage2AwareThreshold:  Number of nodes worth of capacity remaining on the cluster that triggers a notification.
        :type stage2AwareThreshold: 
        
        :param stage3BlockThresholdPercent:  Percent below &quot;Error&quot; state to raise a cluster &quot;Warning&quot; alert.
        :type stage3BlockThresholdPercent: 
        
        :param maxMetadataOverProvisionFactor:  A value representative of the number of times metadata space can be over provisioned relative to the amount of space available. For example, if there was enough metadata space to store 100 TiB of volumes and this number was set to 5, then 500 TiB worth of volumes could be created.
        :type maxMetadataOverProvisionFactor: 
        """

        params = { 
        }
        if stage2AwareThreshold is not None:
            params["stage2AwareThreshold"] = stage2AwareThreshold
        if stage3BlockThresholdPercent is not None:
            params["stage3BlockThresholdPercent"] = stage3BlockThresholdPercent
        if maxMetadataOverProvisionFactor is not None:
            params["maxMetadataOverProvisionFactor"] = maxMetadataOverProvisionFactor
        
        # There is no adaptor.
        return self.send_request(
            'ModifyClusterFullThreshold',
            ModifyClusterFullThresholdResult,
            params
        )

    def get_cluster_master_node_id(
            self,):
        """
        [&#x27;GetClusterMasterNodeID is used to return the ID of the node that can perform cluster-wide administration tasks and holds the storage virtual IP (SVIP) and management virtual IP (MVIP).&#x27;]"""

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'GetClusterMasterNodeID',
            GetClusterMasterNodeIDResult,
            params
        )

    def get_cluster_stats(
            self,):
        """
        [&#x27;GetClusterStats is used to return high-level activity measurements for the cluster. Values returned are cumulative from the creation of the cluster.&#x27;]"""

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'GetClusterStats',
            GetClusterStatsResult,
            params
        )

    def create_cluster(
            self,
            mvip,
            svip,
            repCount,
            username,
            password,
            nodes,
            acceptEula=OPTIONAL,
            attributes=OPTIONAL,):
        """
        [&#x27;The CreateCluster method is used to initialize the node in a cluster that has ownership of the &quot;mvip&quot; and &quot;svip&quot; addresses. Each new cluster is initialized using the MIP of the first node in the cluster. This method also automatically adds all the nodes being configured into the cluster. The method is used only once each time a new cluster is initialized.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Note&lt;/b&gt;: You need to log into the node that is used as the master node for the cluster. Once logged in, run the GetBootstrapConfig method on the node to get the IP addresses for the rest of the nodes that you want to include in the cluster. Then run the CreateCluster method.&#x27;]
        [&#x27;The CreateCluster method is used to initialize the node in a cluster that has ownership of the &quot;mvip&quot; and &quot;svip&quot; addresses. Each new cluster is initialized using the MIP of the first node in the cluster. This method also automatically adds all the nodes being configured into the cluster. The method is used only once each time a new cluster is initialized.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Note&lt;/b&gt;: You need to log into the node that is used as the master node for the cluster. Once logged in, run the GetBootstrapConfig method on the node to get the IP addresses for the rest of the nodes that you want to include in the cluster. Then run the CreateCluster method.&#x27;]
        [&#x27;The CreateCluster method is used to initialize the node in a cluster that has ownership of the &quot;mvip&quot; and &quot;svip&quot; addresses. Each new cluster is initialized using the MIP of the first node in the cluster. This method also automatically adds all the nodes being configured into the cluster. The method is used only once each time a new cluster is initialized.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Note&lt;/b&gt;: You need to log into the node that is used as the master node for the cluster. Once logged in, run the GetBootstrapConfig method on the node to get the IP addresses for the rest of the nodes that you want to include in the cluster. Then run the CreateCluster method.&#x27;]
        :param acceptEula:  Indicate your acceptance of the End User License Agreement when creating this cluster. To accept the EULA, set this parameter to true.
        :type acceptEula: 
        
        :param mvip: [required] Floating (virtual) IP address for the cluster on the management network.
        :type mvip: 
        
        :param svip: [required] Floating (virtual) IP address for the cluster on the storage (iSCSI) network.
        :type svip: 
        
        :param repCount: [required] Number of replicas of each piece of data to store in the cluster. Valid value is &quot;2&quot;.
        :type repCount: 
        
        :param username: [required] User name for the cluster admin.
        :type username: 
        
        :param password: [required] Initial password for the cluster admin account.
        :type password: 
        
        :param nodes: [required] CIP/SIP addresses of the initial set of nodes making up the cluster. This node&#x27;s IP must be in the list.
        :type nodes: 
        
        :param attributes:  List of Name/Value pairs in JSON object format.
        :type attributes: 
        """

        params = { 
            "mvip": mvip,
            "svip": svip,
            "repCount": repCount,
            "username": username,
            "password": password,
            "nodes": nodes,
        }
        if acceptEula is not None:
            params["acceptEula"] = acceptEula
        if attributes is not None:
            params["attributes"] = attributes
        
        # There is no adaptor.
        return self.send_request(
            'CreateCluster',
            CreateClusterResult,
            params
        )

    def list_cluster_admins(
            self,):
        """
        [&#x27;ListClusterAdmins returns the list of all cluster administrators for the cluster. There can be several cluster administrators that have different levels of permissions. There can be only one primary cluster administrator in the system. The primary Cluster Admin is the administrator that was created when the cluster was created. LDAP administrators can also be created when setting up an LDAP system on the cluster.&#x27;]"""

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
            acceptEula=OPTIONAL,
            attributes=OPTIONAL,):
        """
        [&#x27;AddClusterAdmin adds a new Cluster Admin. A Cluster Admin can be used to manage the cluster via the API and management tools. Cluster Admins are completely separate and unrelated to standard tenant accounts.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;Each Cluster Admin can be restricted to a sub-set of the API. SolidFire recommends using multiple Cluster Admins for different users and applications. Each Cluster Admin should be given the minimal permissions necessary to reduce the potential impact of credential compromise.&#x27;]
        [&#x27;AddClusterAdmin adds a new Cluster Admin. A Cluster Admin can be used to manage the cluster via the API and management tools. Cluster Admins are completely separate and unrelated to standard tenant accounts.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;Each Cluster Admin can be restricted to a sub-set of the API. SolidFire recommends using multiple Cluster Admins for different users and applications. Each Cluster Admin should be given the minimal permissions necessary to reduce the potential impact of credential compromise.&#x27;]
        [&#x27;AddClusterAdmin adds a new Cluster Admin. A Cluster Admin can be used to manage the cluster via the API and management tools. Cluster Admins are completely separate and unrelated to standard tenant accounts.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;Each Cluster Admin can be restricted to a sub-set of the API. SolidFire recommends using multiple Cluster Admins for different users and applications. Each Cluster Admin should be given the minimal permissions necessary to reduce the potential impact of credential compromise.&#x27;]
        :param username: [required] Unique username for this Cluster Admin.
        :type username: 
        
        :param password: [required] Password used to authenticate this Cluster Admin.
        :type password: 
        
        :param access: [required] Controls which methods this Cluster Admin can use. For more details on the levels of access, see &quot;Access Control&quot; in the Element API Guide.
        :type access: 
        
        :param acceptEula:  Indicate your acceptance of the End User License Agreement when creating this cluster admin. To accept the EULA, set this parameter to true.
        :type acceptEula: 
        
        :param attributes:  List of Name/Value pairs in JSON object format.
        :type attributes: 
        """

        params = { 
            "username": username,
            "password": password,
            "access": access,
        }
        if acceptEula is not None:
            params["acceptEula"] = acceptEula
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
            clusterAdminID,
            password=OPTIONAL,
            access=OPTIONAL,
            attributes=OPTIONAL,):
        """
        [&#x27;ModifyClusterAdmin is used to change the settings for a Cluster Admin or LDAP Cluster Admin. Access for the administrator Cluster Admin account cannot be changed.&#x27;]
        :param clusterAdminID: [required] ClusterAdminID for the Cluster Admin or LDAP Cluster Admin to modify.
        :type clusterAdminID: 
        
        :param password:  Password used to authenticate this Cluster Admin.
        :type password: 
        
        :param access:  Controls which methods this Cluster Admin can use. For more details on the levels of access, see &quot;Access Control&quot; in the Element API Guide.
        :type access: 
        
        :param attributes:  List of Name/Value pairs in JSON object format.
        :type attributes: 
        """

        params = { 
            "clusterAdminID": clusterAdminID,
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
            clusterAdminID,):
        """
        [&#x27;RemoveClusterAdmin is used to remove a Cluster Admin. The &quot;admin&quot; Cluster Admin cannot be removed.&#x27;]
        :param clusterAdminID: [required] ClusterAdminID for the Cluster Admin to remove.
        :type clusterAdminID: 
        """

        params = { 
            "clusterAdminID": clusterAdminID,
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
        [&#x27;The SetClusterConfig API method is used to set the configuration this node uses to communicate with the cluster it is associated with. To see the states in which these objects can be modified see Cluster Object on page 109. To display the current cluster interface settings for a node, run the GetClusterConfig API method.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Note&lt;/b&gt;: This method is available only through the per-node API endpoint 5.0 or later.&#x27;]
        [&#x27;The SetClusterConfig API method is used to set the configuration this node uses to communicate with the cluster it is associated with. To see the states in which these objects can be modified see Cluster Object on page 109. To display the current cluster interface settings for a node, run the GetClusterConfig API method.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Note&lt;/b&gt;: This method is available only through the per-node API endpoint 5.0 or later.&#x27;]
        [&#x27;The SetClusterConfig API method is used to set the configuration this node uses to communicate with the cluster it is associated with. To see the states in which these objects can be modified see Cluster Object on page 109. To display the current cluster interface settings for a node, run the GetClusterConfig API method.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Note&lt;/b&gt;: This method is available only through the per-node API endpoint 5.0 or later.&#x27;]
        :param cluster: [required] Objects that are changed for the cluster interface settings. Only the fields you want changed need to be added to this method as objects in the &quot;cluster&quot; parameter.
        :type cluster: 
        """

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
        [&#x27;GetSnmpACL is used to return the current SNMP access permissions on the cluster nodes.&#x27;]"""

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
            usmUsers,):
        """
        [&#x27;SetSnmpACL is used to configure SNMP access permissions on the cluster nodes. The values set with this interface apply to all nodes in the cluster, and the values that are passed replace, in whole, all values set in any previous call to SetSnmpACL. Also note that the values set with this interface replace all &quot;network&quot; or &quot;usmUsers&quot; values set with the older SetSnmpInfo.&#x27;]
        :param networks: [required] List of networks and what type of access they have to the SNMP servers running on the cluster nodes. See SNMP Network Object for possible &quot;networks&quot; values. REQUIRED if SNMP v# is disabled.
        :type networks: 
        
        :param usmUsers: [required] List of users and the type of access they have to the SNMP servers running on the cluster nodes. REQUIRED if SNMP v3 is enabled.
        :type usmUsers: 
        """

        params = { 
            "networks": networks,
            "usmUsers": usmUsers,
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
        [&#x27;GetSnmpTrapInfo is used to return current SNMP trap configuration information.&#x27;]"""

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
            trapRecipients,
            clusterFaultTrapsEnabled,
            clusterFaultResolvedTrapsEnabled,
            clusterEventTrapsEnabled,):
        """
        [&#x27;SetSnmpTrapInfo is used to enable and disable the generation of SolidFire SNMP notifications (traps) and to specify the set of network host computers that are to receive the notifications. The values passed with each SetSnmpTrapInfo method replaces all values set in any previous method to SetSnmpTrapInfo.&#x27;]
        :param trapRecipients: [required] List of hosts that are to receive the traps generated by the Cluster Master. At least one object is required if any one of the trap types is enabled.
        :type trapRecipients: 
        
        :param clusterFaultTrapsEnabled: [required] If &quot;true&quot;, when a cluster fault is logged a corresponding solidFireClusterFaultNotification is sent to the configured list of trap recipients.
        :type clusterFaultTrapsEnabled: 
        
        :param clusterFaultResolvedTrapsEnabled: [required] If &quot;true&quot;, when a cluster fault is logged a corresponding solidFireClusterFaultResolvedNotification is sent to the configured list of trap recipients.
        :type clusterFaultResolvedTrapsEnabled: 
        
        :param clusterEventTrapsEnabled: [required] If &quot;true&quot;, when a cluster fault is logged a corresponding solidFireClusterEventNotification is sent to the configured list of trap recipients.
        :type clusterEventTrapsEnabled: 
        """

        params = { 
            "trapRecipients": trapRecipients,
            "clusterFaultTrapsEnabled": clusterFaultTrapsEnabled,
            "clusterFaultResolvedTrapsEnabled": clusterFaultResolvedTrapsEnabled,
            "clusterEventTrapsEnabled": clusterEventTrapsEnabled,
        }
        
        # There is no adaptor.
        return self.send_request(
            'SetSnmpTrapInfo',
            SetSnmpTrapInfoResult,
            params
        )

    def enable_snmp(
            self,
            snmpV3Enabled,):
        """
        [&#x27;EnableSnmp is used to enable SNMP on the cluster nodes. The values set with this interface apply to all nodes in the cluster, and the values that are passed replace, in whole, all values set in any previous call to EnableSnmp.&#x27;]
        :param snmpV3Enabled: [required] If set to &quot;true&quot;, then SNMP v3 is enabled on each node in the cluster. If set to &quot;false&quot;, then SNMP v2 is enabled.
        :type snmpV3Enabled: 
        """

        params = { 
            "snmpV3Enabled": snmpV3Enabled,
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
        [&#x27;DisableSnmp is used to disable SNMP on the cluster nodes.&#x27;]"""

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
        [&#x27;GetSnmpInfo is used to return the current simple network management protocol (SNMP) configuration information.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Note&lt;/b&gt;: GetSnmpInfo will be available for Element OS 8 and prior releases. It will be deprecated after Element OS 8. There are two new SNMP API methods that you should migrate over to. They are GetSnmpState and GetSnmpACL. Please see details in this document for their descriptions and usage.&#x27;]
        [&#x27;GetSnmpInfo is used to return the current simple network management protocol (SNMP) configuration information.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Note&lt;/b&gt;: GetSnmpInfo will be available for Element OS 8 and prior releases. It will be deprecated after Element OS 8. There are two new SNMP API methods that you should migrate over to. They are GetSnmpState and GetSnmpACL. Please see details in this document for their descriptions and usage.&#x27;]
        [&#x27;GetSnmpInfo is used to return the current simple network management protocol (SNMP) configuration information.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Note&lt;/b&gt;: GetSnmpInfo will be available for Element OS 8 and prior releases. It will be deprecated after Element OS 8. There are two new SNMP API methods that you should migrate over to. They are GetSnmpState and GetSnmpACL. Please see details in this document for their descriptions and usage.&#x27;]"""

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
            snmpV3Enabled=OPTIONAL,
            usmUsers=OPTIONAL,):
        """
        [&#x27;SetSnmpInfo is used to configure SNMP v2 and v3 on the cluster nodes. The values set with this interface apply to all nodes in the cluster, and the values that are passed replace, in whole, all values set in any previous call to SetSnmpInfo.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Note&lt;/b&gt;: EnableSnmp and SetSnmpACL methods can be used to accomplish the same results as SetSnmpInfo. SetSnmpInfo will no longer be available after the Element 8 release. Please use EnableSnmp and SetSnmpACL in the future.&#x27;]
        [&#x27;SetSnmpInfo is used to configure SNMP v2 and v3 on the cluster nodes. The values set with this interface apply to all nodes in the cluster, and the values that are passed replace, in whole, all values set in any previous call to SetSnmpInfo.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Note&lt;/b&gt;: EnableSnmp and SetSnmpACL methods can be used to accomplish the same results as SetSnmpInfo. SetSnmpInfo will no longer be available after the Element 8 release. Please use EnableSnmp and SetSnmpACL in the future.&#x27;]
        [&#x27;SetSnmpInfo is used to configure SNMP v2 and v3 on the cluster nodes. The values set with this interface apply to all nodes in the cluster, and the values that are passed replace, in whole, all values set in any previous call to SetSnmpInfo.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Note&lt;/b&gt;: EnableSnmp and SetSnmpACL methods can be used to accomplish the same results as SetSnmpInfo. SetSnmpInfo will no longer be available after the Element 8 release. Please use EnableSnmp and SetSnmpACL in the future.&#x27;]
        :param networks:  List of networks and what type of access they have to the SNMP servers running on the cluster nodes. See SNMP Network Object for possible &quot;networks&quot; values. SNMP v2 only.
        :type networks: 
        
        :param enabled:  If set to &quot;true&quot;, then SNMP is enabled on each node in the cluster.
        :type enabled: 
        
        :param snmpV3Enabled:  If set to &quot;true&quot;, then SNMP v3 is enabled on each node in the cluster.
        :type snmpV3Enabled: 
        
        :param usmUsers:  If SNMP v3 is enabled, this value must be passed in place of the &quot;networks&quot; parameter. SNMP v3 only.
        :type usmUsers: 
        """

        params = { 
        }
        if networks is not None:
            params["networks"] = networks
        if enabled is not None:
            params["enabled"] = enabled
        if snmpV3Enabled is not None:
            params["snmpV3Enabled"] = snmpV3Enabled
        if usmUsers is not None:
            params["usmUsers"] = usmUsers
        
        # There is no adaptor.
        return self.send_request(
            'SetSnmpInfo',
            SetSnmpInfoResult,
            params
        )

    def get_snmp_state(
            self,):
        """
        [&#x27;GetSnmpState is used to return the current state of the SNMP feature.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Note&lt;/b&gt;: GetSnmpState is new for Element OS 8. Please use this method and SetSnmpACL to migrate your SNMP functionality in the future.&#x27;]
        [&#x27;GetSnmpState is used to return the current state of the SNMP feature.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Note&lt;/b&gt;: GetSnmpState is new for Element OS 8. Please use this method and SetSnmpACL to migrate your SNMP functionality in the future.&#x27;]
        [&#x27;GetSnmpState is used to return the current state of the SNMP feature.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Note&lt;/b&gt;: GetSnmpState is new for Element OS 8. Please use this method and SetSnmpACL to migrate your SNMP functionality in the future.&#x27;]"""

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'GetSnmpState',
            GetSnmpStateResult,
            params,
            since=8.0
        )

    def list_sync_jobs(
            self,):
        """
        [&#x27;ListSyncJobs is used to return information about synchronization jobs that are running on a SolidFire cluster. Synchronization jobs that are returned with this method are, &quot;slice,&quot; &quot;clone&quot; and &quot;remote.&quot;&#x27;]"""

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'ListSyncJobs',
            ListSyncJobsResult,
            params
        )

    def get_api(
            self,):
        """
        [&#x27;Retrieves the current version of the API and a list of all supported versions.&#x27;]"""

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
        [&#x27;GetNtpInfo is used to return the current network time protocol (NTP) configuration information.&#x27;]"""

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'GetNtpInfo',
            GetNtpInfoResult,
            params
        )

    def set_ntp_info(
            self,
            servers,
            broadcastclient=OPTIONAL,):
        """
        [&#x27;SetNtpInfo is used to configure the NTP on cluster nodes. The values set with this interface apply to all nodes in the cluster. The nodes can only be configured as a server where a host is selected to administrate the networking and/or a broadcast client where each host sends each message to each peer.&#x27;]
        :param servers: [required] List of NTP servers to add to each node&#x27;s NTP configuration.
        :type servers: 
        
        :param broadcastclient:  Enable every node in the cluster as a broadcase client.
        :type broadcastclient: 
        """

        params = { 
            "servers": servers,
        }
        if broadcastclient is not None:
            params["broadcastclient"] = broadcastclient
        
        # There is no adaptor.
        return self.send_request(
            'SetNtpInfo',
            SetNtpInfoResult,
            params
        )

    def get_cluster_state(
            self,):
        """
        [&#x27;The GetClusterState method is used to indicate if a node is part of a cluster or not. The three states are: &lt;br&gt;&lt;strong&gt;Available:&lt;/strong&gt; Node has not been configured with a cluster name.&lt;br&gt;&lt;strong&gt;Pending:&lt;/strong&gt; Node is pending for a specific named cluster and can be added.&lt;br&gt;&lt;strong&gt;Active:&lt;/strong&gt; Node is active and a member of a cluster and may not be added to another cluster.&#x27;]"""

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'GetClusterState',
            GetClusterStateResult,
            params
        )

    def get_current_cluster_admin(
            self,):
        """
        [&#x27;GetCurrentClusterAdmin returns information for the current primary cluster administrator. The primary Cluster Admin was ncreated when the cluster was created.&#x27;]"""

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'GetCurrentClusterAdmin',
            GetCurrentClusterAdminResult,
            params
        )

    def create_cluster_support_bundle(
            self,
            password,
            username,
            allowIncomplete=OPTIONAL,
            bundleName=OPTIONAL,
            extraArgs=OPTIONAL,
            mvip=OPTIONAL,
            nodes=OPTIONAL,):
        """
        [&#x27;CreateClusterSupportBundle is used to gather support bundles from all the nodes in a cluster. When the bundle has been successfully created, the bundle is stored on the node as a tar.gz file.&#x27;]
        :param allowIncomplete:  Allows the script to continue to run if bundles cannot be gathered from one or more of the nodes.
        :type allowIncomplete: 
        
        :param bundleName:  Unique name for each support bundle created. If no name is provided, then &#x27;supportbundle&#x27; and the node name is used as a file name.
        :type bundleName: 
        
        :param extraArgs:  This parameter is fed to the sf_make_support_bundle script. Should be used only at the request of SolidFire Support.
        :type extraArgs: 
        
        :param mvip:  [&#x27;The mvip of the cluster. Bundles will be gathered from all nodes in the cluster.&#x27;, &quot;REQUIRED if &#x27;nodes&#x27; are not specified.&quot;][&#x27;The mvip of the cluster. Bundles will be gathered from all nodes in the cluster.&#x27;, &quot;REQUIRED if &#x27;nodes&#x27; are not specified.&quot;]
        :type mvip: 
        
        :param nodes:  [&quot;The IP addresses of the nodes from which to gather bundles. Use either &#x27;nodes&#x27; or &#x27;mvip&#x27;, but not both to specify which nodes to gather from.&quot;, &quot;REQUIRED if &#x27;nodes&#x27; are not specified.&quot;][&quot;The IP addresses of the nodes from which to gather bundles. Use either &#x27;nodes&#x27; or &#x27;mvip&#x27;, but not both to specify which nodes to gather from.&quot;, &quot;REQUIRED if &#x27;nodes&#x27; are not specified.&quot;]
        :type nodes: 
        
        :param password: [required] [&#x27;The cluster password. Note: This password will be visible as text when entered.&#x27;]
        :type password: 
        
        :param username: [required] [&quot;The admin user name. Any level of &#x27;admin&#x27; can be used.&quot;]
        :type username: 
        """

        params = { 
            "password": password,
            "username": username,
        }
        if allowIncomplete is not None:
            params["allowIncomplete"] = allowIncomplete
        if bundleName is not None:
            params["bundleName"] = bundleName
        if extraArgs is not None:
            params["extraArgs"] = extraArgs
        if mvip is not None:
            params["mvip"] = mvip
        if nodes is not None:
            params["nodes"] = nodes
        
        # There is no adaptor.
        return self.send_request(
            'CreateClusterSupportBundle',
            CreateClusterSupportBundleResult,
            params,
            since=8.0
        )

    def create_support_bundle(
            self,
            bundleName=OPTIONAL,
            extraArgs=OPTIONAL,
            timeoutSec=OPTIONAL,):
        """
        [&quot;CreateSupportBundle is used to create a support bundle file under the node&#x27;s directory. When the bundle has been successfully created, the bundle is stored on the node as a tar.gz file.&quot;]
        :param bundleName:  Unique name for each support bundle created. If no name is provided, then &#x27;supportbundle&#x27; and the node name is used as a file name.
        :type bundleName: 
        
        :param extraArgs:  This parameter is fed to the sf_make_support_bundle script. Should be used only at the request of SolidFire Support.
        :type extraArgs: 
        
        :param timeoutSec:  [&#x27;The number of seconds to let the support bundle script run before timing out and stopping. Default is 1500 seconds.&#x27;]
        :type timeoutSec: 
        """

        params = { 
        }
        if bundleName is not None:
            params["bundleName"] = bundleName
        if extraArgs is not None:
            params["extraArgs"] = extraArgs
        if timeoutSec is not None:
            params["timeoutSec"] = timeoutSec
        
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
        [&#x27;DeleteAllSupportBundles is used to delete all support bundles generated with the CreateSupportBundle API method.&#x27;]"""

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'DeleteAllSupportBundles',
            DeleteAllSupportBundlesResult,
            params,
            since=8.0
        )

    def enable_encryption_at_rest(
            self,):
        """
        [&#x27;The EnableEncryptionAtRest method is used to enable the Advanced Encryption Standard (AES) 256-bit encryption at rest on the cluster so that the cluster can manage the encryption key used for the drives on each node. This feature is not enabled by default. Enabling this operation allows the cluster to automatically manage encryption keys internally for the drives on each node in the cluster. Nodes do not store the keys to unlock drives and the keys are never passed over the network. Two nodes participating in a cluster are required to access the key to disable encryption on a drive. The encryption management does not affect performance or efficiency on the cluster. If an encryption-enabled drive or node is removed from the cluster with the API, all data is secure erased and any data left on the drive cannot be read or accessed.&#x27;, &#x27;Enabling or disabling encryption should be performed when the cluster is running and in a healthy state. Encryption can be enabled or disabled at your discretion and can be performed as often as you need.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;Note&lt;/b&gt;: This process is asynchronous and returns a response before encryption is enabled. The GetClusterInfo method can be used to poll the system to see when the process has completed.&#x27;]
        [&#x27;The EnableEncryptionAtRest method is used to enable the Advanced Encryption Standard (AES) 256-bit encryption at rest on the cluster so that the cluster can manage the encryption key used for the drives on each node. This feature is not enabled by default. Enabling this operation allows the cluster to automatically manage encryption keys internally for the drives on each node in the cluster. Nodes do not store the keys to unlock drives and the keys are never passed over the network. Two nodes participating in a cluster are required to access the key to disable encryption on a drive. The encryption management does not affect performance or efficiency on the cluster. If an encryption-enabled drive or node is removed from the cluster with the API, all data is secure erased and any data left on the drive cannot be read or accessed.&#x27;, &#x27;Enabling or disabling encryption should be performed when the cluster is running and in a healthy state. Encryption can be enabled or disabled at your discretion and can be performed as often as you need.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;Note&lt;/b&gt;: This process is asynchronous and returns a response before encryption is enabled. The GetClusterInfo method can be used to poll the system to see when the process has completed.&#x27;]
        [&#x27;The EnableEncryptionAtRest method is used to enable the Advanced Encryption Standard (AES) 256-bit encryption at rest on the cluster so that the cluster can manage the encryption key used for the drives on each node. This feature is not enabled by default. Enabling this operation allows the cluster to automatically manage encryption keys internally for the drives on each node in the cluster. Nodes do not store the keys to unlock drives and the keys are never passed over the network. Two nodes participating in a cluster are required to access the key to disable encryption on a drive. The encryption management does not affect performance or efficiency on the cluster. If an encryption-enabled drive or node is removed from the cluster with the API, all data is secure erased and any data left on the drive cannot be read or accessed.&#x27;, &#x27;Enabling or disabling encryption should be performed when the cluster is running and in a healthy state. Encryption can be enabled or disabled at your discretion and can be performed as often as you need.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;Note&lt;/b&gt;: This process is asynchronous and returns a response before encryption is enabled. The GetClusterInfo method can be used to poll the system to see when the process has completed.&#x27;]"""

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
        [&#x27;The DisableEncryptionAtRest method enables you to remove the encryption that was previously applied to the cluster using the EnableEncryptionAtRest method.&#x27;, &#x27;This disable method is asynchronous and returns a response before encryption is disabled.&#x27;, &#x27;You can use the GetClusterInfo method to poll the system to see when the process has completed.&#x27;]
        [&#x27;The DisableEncryptionAtRest method enables you to remove the encryption that was previously applied to the cluster using the EnableEncryptionAtRest method.&#x27;, &#x27;This disable method is asynchronous and returns a response before encryption is disabled.&#x27;, &#x27;You can use the GetClusterInfo method to poll the system to see when the process has completed.&#x27;]
        [&#x27;The DisableEncryptionAtRest method enables you to remove the encryption that was previously applied to the cluster using the EnableEncryptionAtRest method.&#x27;, &#x27;This disable method is asynchronous and returns a response before encryption is disabled.&#x27;, &#x27;You can use the GetClusterInfo method to poll the system to see when the process has completed.&#x27;]"""

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'DisableEncryptionAtRest',
            DisableEncryptionAtRestResult,
            params
        )

    def get_system_status(
            self,
            force,):
        """
        :param force: [required] Force must always be true when called on a cluster connection.
        :type force: 
        """

        params = { 
            "force": force,
        }
        
        # There is no adaptor.
        return self.send_request(
            'GetSystemStatus',
            GetSystemStatusResult,
            params
        )

    def snmp_send_test_traps(
            self,):
        """
        [&#x27;SnmpSendTestTraps enables you to test SNMP functionality for a cluster. This method instructs the cluster to send test SNMP traps to the currently configured SNMP manager.&#x27;]"""

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
            asyncHandle,):
        """
        [&#x27;Used to retrieve the result of asynchronous method calls.&#x27;, &#x27;Some method calls are long running and do not complete when the initial response is sent.&#x27;, &#x27;To obtain the result of the method call, polling with GetAsyncResult is required.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;GetAsyncResult returns the overall status of the operation (in progress, completed, or error) in a standard fashion,&#x27;, &#x27;but the actual data returned for the operation depends on the original method call and the return data is documented with each method.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;The result for a completed asynchronous method call can only be retrieved once.&#x27;, &#x27;Once the final result has been returned, later attempts returns an error.&#x27;]
        [&#x27;Used to retrieve the result of asynchronous method calls.&#x27;, &#x27;Some method calls are long running and do not complete when the initial response is sent.&#x27;, &#x27;To obtain the result of the method call, polling with GetAsyncResult is required.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;GetAsyncResult returns the overall status of the operation (in progress, completed, or error) in a standard fashion,&#x27;, &#x27;but the actual data returned for the operation depends on the original method call and the return data is documented with each method.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;The result for a completed asynchronous method call can only be retrieved once.&#x27;, &#x27;Once the final result has been returned, later attempts returns an error.&#x27;]
        [&#x27;Used to retrieve the result of asynchronous method calls.&#x27;, &#x27;Some method calls are long running and do not complete when the initial response is sent.&#x27;, &#x27;To obtain the result of the method call, polling with GetAsyncResult is required.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;GetAsyncResult returns the overall status of the operation (in progress, completed, or error) in a standard fashion,&#x27;, &#x27;but the actual data returned for the operation depends on the original method call and the return data is documented with each method.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;The result for a completed asynchronous method call can only be retrieved once.&#x27;, &#x27;Once the final result has been returned, later attempts returns an error.&#x27;]
        [&#x27;Used to retrieve the result of asynchronous method calls.&#x27;, &#x27;Some method calls are long running and do not complete when the initial response is sent.&#x27;, &#x27;To obtain the result of the method call, polling with GetAsyncResult is required.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;GetAsyncResult returns the overall status of the operation (in progress, completed, or error) in a standard fashion,&#x27;, &#x27;but the actual data returned for the operation depends on the original method call and the return data is documented with each method.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;The result for a completed asynchronous method call can only be retrieved once.&#x27;, &#x27;Once the final result has been returned, later attempts returns an error.&#x27;]
        [&#x27;Used to retrieve the result of asynchronous method calls.&#x27;, &#x27;Some method calls are long running and do not complete when the initial response is sent.&#x27;, &#x27;To obtain the result of the method call, polling with GetAsyncResult is required.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;GetAsyncResult returns the overall status of the operation (in progress, completed, or error) in a standard fashion,&#x27;, &#x27;but the actual data returned for the operation depends on the original method call and the return data is documented with each method.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;The result for a completed asynchronous method call can only be retrieved once.&#x27;, &#x27;Once the final result has been returned, later attempts returns an error.&#x27;]
        [&#x27;Used to retrieve the result of asynchronous method calls.&#x27;, &#x27;Some method calls are long running and do not complete when the initial response is sent.&#x27;, &#x27;To obtain the result of the method call, polling with GetAsyncResult is required.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;GetAsyncResult returns the overall status of the operation (in progress, completed, or error) in a standard fashion,&#x27;, &#x27;but the actual data returned for the operation depends on the original method call and the return data is documented with each method.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;The result for a completed asynchronous method call can only be retrieved once.&#x27;, &#x27;Once the final result has been returned, later attempts returns an error.&#x27;]
        [&#x27;Used to retrieve the result of asynchronous method calls.&#x27;, &#x27;Some method calls are long running and do not complete when the initial response is sent.&#x27;, &#x27;To obtain the result of the method call, polling with GetAsyncResult is required.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;GetAsyncResult returns the overall status of the operation (in progress, completed, or error) in a standard fashion,&#x27;, &#x27;but the actual data returned for the operation depends on the original method call and the return data is documented with each method.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;The result for a completed asynchronous method call can only be retrieved once.&#x27;, &#x27;Once the final result has been returned, later attempts returns an error.&#x27;]
        [&#x27;Used to retrieve the result of asynchronous method calls.&#x27;, &#x27;Some method calls are long running and do not complete when the initial response is sent.&#x27;, &#x27;To obtain the result of the method call, polling with GetAsyncResult is required.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;GetAsyncResult returns the overall status of the operation (in progress, completed, or error) in a standard fashion,&#x27;, &#x27;but the actual data returned for the operation depends on the original method call and the return data is documented with each method.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;The result for a completed asynchronous method call can only be retrieved once.&#x27;, &#x27;Once the final result has been returned, later attempts returns an error.&#x27;]
        [&#x27;Used to retrieve the result of asynchronous method calls.&#x27;, &#x27;Some method calls are long running and do not complete when the initial response is sent.&#x27;, &#x27;To obtain the result of the method call, polling with GetAsyncResult is required.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;GetAsyncResult returns the overall status of the operation (in progress, completed, or error) in a standard fashion,&#x27;, &#x27;but the actual data returned for the operation depends on the original method call and the return data is documented with each method.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;The result for a completed asynchronous method call can only be retrieved once.&#x27;, &#x27;Once the final result has been returned, later attempts returns an error.&#x27;]
        :param asyncHandle: [required] A value that was returned from the original asynchronous method call.
        :type asyncHandle: 
        """

        params = { 
            "asyncHandle": asyncHandle,
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
        [&quot;AddDrives is used to add one or more available drives to the cluster enabling the drives to host a portion of the cluster&#x27;s data.&quot;, &#x27;When you add a node to the cluster or install new drives in an existing node, the new drives are marked as &quot;available&quot; and must be added via AddDrives before they can be utilized.&#x27;, &#x27;Use the &quot;ListDrives&quot; method to display drives that are &quot;available&quot; to be added.&#x27;, &#x27;When you add multiple drives, it is more efficient to add them in a single &quot;AddDrives&quot; method call rather than multiple individual methods with a single drive each.&#x27;, &#x27;This reduces the amount of data balancing that must occur to stabilize the storage load on the cluster.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;When you add a drive, the system automatically determines the &quot;type&quot; of drive it should be.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;The method returns immediately. However, it may take some time for the data in the cluster to be rebalanced using the newly added drives.&#x27;, &#x27;As the new drive(s) are syncing on the system, you can use the &quot;ListSyncJobs&quot; method to see how the drive(s) are being rebalanced and the progress of adding the new drive.&#x27;]
        [&quot;AddDrives is used to add one or more available drives to the cluster enabling the drives to host a portion of the cluster&#x27;s data.&quot;, &#x27;When you add a node to the cluster or install new drives in an existing node, the new drives are marked as &quot;available&quot; and must be added via AddDrives before they can be utilized.&#x27;, &#x27;Use the &quot;ListDrives&quot; method to display drives that are &quot;available&quot; to be added.&#x27;, &#x27;When you add multiple drives, it is more efficient to add them in a single &quot;AddDrives&quot; method call rather than multiple individual methods with a single drive each.&#x27;, &#x27;This reduces the amount of data balancing that must occur to stabilize the storage load on the cluster.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;When you add a drive, the system automatically determines the &quot;type&quot; of drive it should be.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;The method returns immediately. However, it may take some time for the data in the cluster to be rebalanced using the newly added drives.&#x27;, &#x27;As the new drive(s) are syncing on the system, you can use the &quot;ListSyncJobs&quot; method to see how the drive(s) are being rebalanced and the progress of adding the new drive.&#x27;]
        [&quot;AddDrives is used to add one or more available drives to the cluster enabling the drives to host a portion of the cluster&#x27;s data.&quot;, &#x27;When you add a node to the cluster or install new drives in an existing node, the new drives are marked as &quot;available&quot; and must be added via AddDrives before they can be utilized.&#x27;, &#x27;Use the &quot;ListDrives&quot; method to display drives that are &quot;available&quot; to be added.&#x27;, &#x27;When you add multiple drives, it is more efficient to add them in a single &quot;AddDrives&quot; method call rather than multiple individual methods with a single drive each.&#x27;, &#x27;This reduces the amount of data balancing that must occur to stabilize the storage load on the cluster.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;When you add a drive, the system automatically determines the &quot;type&quot; of drive it should be.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;The method returns immediately. However, it may take some time for the data in the cluster to be rebalanced using the newly added drives.&#x27;, &#x27;As the new drive(s) are syncing on the system, you can use the &quot;ListSyncJobs&quot; method to see how the drive(s) are being rebalanced and the progress of adding the new drive.&#x27;]
        [&quot;AddDrives is used to add one or more available drives to the cluster enabling the drives to host a portion of the cluster&#x27;s data.&quot;, &#x27;When you add a node to the cluster or install new drives in an existing node, the new drives are marked as &quot;available&quot; and must be added via AddDrives before they can be utilized.&#x27;, &#x27;Use the &quot;ListDrives&quot; method to display drives that are &quot;available&quot; to be added.&#x27;, &#x27;When you add multiple drives, it is more efficient to add them in a single &quot;AddDrives&quot; method call rather than multiple individual methods with a single drive each.&#x27;, &#x27;This reduces the amount of data balancing that must occur to stabilize the storage load on the cluster.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;When you add a drive, the system automatically determines the &quot;type&quot; of drive it should be.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;The method returns immediately. However, it may take some time for the data in the cluster to be rebalanced using the newly added drives.&#x27;, &#x27;As the new drive(s) are syncing on the system, you can use the &quot;ListSyncJobs&quot; method to see how the drive(s) are being rebalanced and the progress of adding the new drive.&#x27;]
        [&quot;AddDrives is used to add one or more available drives to the cluster enabling the drives to host a portion of the cluster&#x27;s data.&quot;, &#x27;When you add a node to the cluster or install new drives in an existing node, the new drives are marked as &quot;available&quot; and must be added via AddDrives before they can be utilized.&#x27;, &#x27;Use the &quot;ListDrives&quot; method to display drives that are &quot;available&quot; to be added.&#x27;, &#x27;When you add multiple drives, it is more efficient to add them in a single &quot;AddDrives&quot; method call rather than multiple individual methods with a single drive each.&#x27;, &#x27;This reduces the amount of data balancing that must occur to stabilize the storage load on the cluster.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;When you add a drive, the system automatically determines the &quot;type&quot; of drive it should be.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;The method returns immediately. However, it may take some time for the data in the cluster to be rebalanced using the newly added drives.&#x27;, &#x27;As the new drive(s) are syncing on the system, you can use the &quot;ListSyncJobs&quot; method to see how the drive(s) are being rebalanced and the progress of adding the new drive.&#x27;]
        [&quot;AddDrives is used to add one or more available drives to the cluster enabling the drives to host a portion of the cluster&#x27;s data.&quot;, &#x27;When you add a node to the cluster or install new drives in an existing node, the new drives are marked as &quot;available&quot; and must be added via AddDrives before they can be utilized.&#x27;, &#x27;Use the &quot;ListDrives&quot; method to display drives that are &quot;available&quot; to be added.&#x27;, &#x27;When you add multiple drives, it is more efficient to add them in a single &quot;AddDrives&quot; method call rather than multiple individual methods with a single drive each.&#x27;, &#x27;This reduces the amount of data balancing that must occur to stabilize the storage load on the cluster.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;When you add a drive, the system automatically determines the &quot;type&quot; of drive it should be.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;The method returns immediately. However, it may take some time for the data in the cluster to be rebalanced using the newly added drives.&#x27;, &#x27;As the new drive(s) are syncing on the system, you can use the &quot;ListSyncJobs&quot; method to see how the drive(s) are being rebalanced and the progress of adding the new drive.&#x27;]
        [&quot;AddDrives is used to add one or more available drives to the cluster enabling the drives to host a portion of the cluster&#x27;s data.&quot;, &#x27;When you add a node to the cluster or install new drives in an existing node, the new drives are marked as &quot;available&quot; and must be added via AddDrives before they can be utilized.&#x27;, &#x27;Use the &quot;ListDrives&quot; method to display drives that are &quot;available&quot; to be added.&#x27;, &#x27;When you add multiple drives, it is more efficient to add them in a single &quot;AddDrives&quot; method call rather than multiple individual methods with a single drive each.&#x27;, &#x27;This reduces the amount of data balancing that must occur to stabilize the storage load on the cluster.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;When you add a drive, the system automatically determines the &quot;type&quot; of drive it should be.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;The method returns immediately. However, it may take some time for the data in the cluster to be rebalanced using the newly added drives.&#x27;, &#x27;As the new drive(s) are syncing on the system, you can use the &quot;ListSyncJobs&quot; method to see how the drive(s) are being rebalanced and the progress of adding the new drive.&#x27;]
        [&quot;AddDrives is used to add one or more available drives to the cluster enabling the drives to host a portion of the cluster&#x27;s data.&quot;, &#x27;When you add a node to the cluster or install new drives in an existing node, the new drives are marked as &quot;available&quot; and must be added via AddDrives before they can be utilized.&#x27;, &#x27;Use the &quot;ListDrives&quot; method to display drives that are &quot;available&quot; to be added.&#x27;, &#x27;When you add multiple drives, it is more efficient to add them in a single &quot;AddDrives&quot; method call rather than multiple individual methods with a single drive each.&#x27;, &#x27;This reduces the amount of data balancing that must occur to stabilize the storage load on the cluster.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;When you add a drive, the system automatically determines the &quot;type&quot; of drive it should be.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;The method returns immediately. However, it may take some time for the data in the cluster to be rebalanced using the newly added drives.&#x27;, &#x27;As the new drive(s) are syncing on the system, you can use the &quot;ListSyncJobs&quot; method to see how the drive(s) are being rebalanced and the progress of adding the new drive.&#x27;]
        [&quot;AddDrives is used to add one or more available drives to the cluster enabling the drives to host a portion of the cluster&#x27;s data.&quot;, &#x27;When you add a node to the cluster or install new drives in an existing node, the new drives are marked as &quot;available&quot; and must be added via AddDrives before they can be utilized.&#x27;, &#x27;Use the &quot;ListDrives&quot; method to display drives that are &quot;available&quot; to be added.&#x27;, &#x27;When you add multiple drives, it is more efficient to add them in a single &quot;AddDrives&quot; method call rather than multiple individual methods with a single drive each.&#x27;, &#x27;This reduces the amount of data balancing that must occur to stabilize the storage load on the cluster.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;When you add a drive, the system automatically determines the &quot;type&quot; of drive it should be.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;The method returns immediately. However, it may take some time for the data in the cluster to be rebalanced using the newly added drives.&#x27;, &#x27;As the new drive(s) are syncing on the system, you can use the &quot;ListSyncJobs&quot; method to see how the drive(s) are being rebalanced and the progress of adding the new drive.&#x27;]
        [&quot;AddDrives is used to add one or more available drives to the cluster enabling the drives to host a portion of the cluster&#x27;s data.&quot;, &#x27;When you add a node to the cluster or install new drives in an existing node, the new drives are marked as &quot;available&quot; and must be added via AddDrives before they can be utilized.&#x27;, &#x27;Use the &quot;ListDrives&quot; method to display drives that are &quot;available&quot; to be added.&#x27;, &#x27;When you add multiple drives, it is more efficient to add them in a single &quot;AddDrives&quot; method call rather than multiple individual methods with a single drive each.&#x27;, &#x27;This reduces the amount of data balancing that must occur to stabilize the storage load on the cluster.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;When you add a drive, the system automatically determines the &quot;type&quot; of drive it should be.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;The method returns immediately. However, it may take some time for the data in the cluster to be rebalanced using the newly added drives.&#x27;, &#x27;As the new drive(s) are syncing on the system, you can use the &quot;ListSyncJobs&quot; method to see how the drive(s) are being rebalanced and the progress of adding the new drive.&#x27;]
        :param drives: [required] List of drives to add to the cluster.
        :type drives: 
        """

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
        [&quot;ListDrives allows you to retrieve the list of the drives that exist in the cluster&#x27;s active nodes.&quot;, &#x27;This method returns drives that have been added as volume metadata or block drives as well as drives that have not been added and are available.&#x27;]
        [&quot;ListDrives allows you to retrieve the list of the drives that exist in the cluster&#x27;s active nodes.&quot;, &#x27;This method returns drives that have been added as volume metadata or block drives as well as drives that have not been added and are available.&#x27;]"""

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'ListDrives',
            ListDrivesResult,
            params
        )

    def get_drive_config(
            self,):
        """
        [&#x27;GetDriveConfig is used to display drive information for expected slice and block drive counts as well as the number of slices and block drives that are currently connected to the node.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Note&lt;/b&gt;: This method is available only through the per-node API endpoint 5.0 or later.&#x27;]
        [&#x27;GetDriveConfig is used to display drive information for expected slice and block drive counts as well as the number of slices and block drives that are currently connected to the node.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Note&lt;/b&gt;: This method is available only through the per-node API endpoint 5.0 or later.&#x27;]
        [&#x27;GetDriveConfig is used to display drive information for expected slice and block drive counts as well as the number of slices and block drives that are currently connected to the node.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Note&lt;/b&gt;: This method is available only through the per-node API endpoint 5.0 or later.&#x27;]"""

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'GetDriveConfig',
            GetDriveConfigResult,
            params
        )

    def get_drive_hardware_info(
            self,
            driveID,):
        """
        GetDriveHardwareInfo returns all the hardware info for the given drive. This generally includes manufacturers, vendors, versions, and other associated hardware identification information.
        :param driveID: [required] DriveID for the drive information requested. DriveIDs can be obtained via the &quot;ListDrives&quot; method.
        :type driveID: 
        """

        params = { 
            "driveID": driveID,
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
        :type force: 
        """

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
        [&#x27;ResetDrives is used to pro-actively initialize drives and remove all data currently residing on the drive. The drive can then be reused in an existing node or used in an upgraded SolidFire node. This method requires the force=true parameter to be included in the method call.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Note&lt;/b&gt;: This method is available only through the per-node API endpoint 5.0 or later.&#x27;]
        [&#x27;ResetDrives is used to pro-actively initialize drives and remove all data currently residing on the drive. The drive can then be reused in an existing node or used in an upgraded SolidFire node. This method requires the force=true parameter to be included in the method call.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Note&lt;/b&gt;: This method is available only through the per-node API endpoint 5.0 or later.&#x27;]
        [&#x27;ResetDrives is used to pro-actively initialize drives and remove all data currently residing on the drive. The drive can then be reused in an existing node or used in an upgraded SolidFire node. This method requires the force=true parameter to be included in the method call.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Note&lt;/b&gt;: This method is available only through the per-node API endpoint 5.0 or later.&#x27;]
        :param drives: [required] List of device names (not driveIDs) to reset.
        :type drives: 
        
        :param force: [required] The &quot;force&quot; parameter must be included on this method to successfully reset a drive.
        :type force: 
        """

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
        [&#x27;The TestDrives API method is used to run a hardware validation on all the drives on the node. Hardware failures on the drives are detected if present and they are reported in the results of the validation tests.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Note&lt;/b&gt;: This test takes approximately 10 minutes.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Note&lt;/b&gt;: This method is available only through the per-node API endpoint 5.0 or later.&#x27;]
        [&#x27;The TestDrives API method is used to run a hardware validation on all the drives on the node. Hardware failures on the drives are detected if present and they are reported in the results of the validation tests.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Note&lt;/b&gt;: This test takes approximately 10 minutes.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Note&lt;/b&gt;: This method is available only through the per-node API endpoint 5.0 or later.&#x27;]
        [&#x27;The TestDrives API method is used to run a hardware validation on all the drives on the node. Hardware failures on the drives are detected if present and they are reported in the results of the validation tests.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Note&lt;/b&gt;: This test takes approximately 10 minutes.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Note&lt;/b&gt;: This method is available only through the per-node API endpoint 5.0 or later.&#x27;]
        [&#x27;The TestDrives API method is used to run a hardware validation on all the drives on the node. Hardware failures on the drives are detected if present and they are reported in the results of the validation tests.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Note&lt;/b&gt;: This test takes approximately 10 minutes.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Note&lt;/b&gt;: This method is available only through the per-node API endpoint 5.0 or later.&#x27;]
        [&#x27;The TestDrives API method is used to run a hardware validation on all the drives on the node. Hardware failures on the drives are detected if present and they are reported in the results of the validation tests.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Note&lt;/b&gt;: This test takes approximately 10 minutes.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Note&lt;/b&gt;: This method is available only through the per-node API endpoint 5.0 or later.&#x27;]
        :param minutes:  The number of minutes to run the test can be specified.
        :type minutes: 
        
        :param force: [required] The &quot;force&quot; parameter must be included on this method to successfully test the drives on the node.
        :type force: 
        """

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
            driveID,):
        """
        [&#x27;GetDriveStats return high-level activity measurements for a single drive. Values are cumulative from the addition of the drive to the cluster. Some values are specific to Block Drives. Statistical data may not be returned for both block and metadata drives when running this method.&#x27;, &#x27;For more information on which drive type returns which data, see Response Example (Block Drive) and Response Example (Volume Metadata Drive) in the SolidFire API guide.&#x27;]
        [&#x27;GetDriveStats return high-level activity measurements for a single drive. Values are cumulative from the addition of the drive to the cluster. Some values are specific to Block Drives. Statistical data may not be returned for both block and metadata drives when running this method.&#x27;, &#x27;For more information on which drive type returns which data, see Response Example (Block Drive) and Response Example (Volume Metadata Drive) in the SolidFire API guide.&#x27;]
        :param driveID: [required] Specifies the drive for which statistics are gathered.
        :type driveID: 
        """

        params = { 
            "driveID": driveID,
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
        [&#x27;SecureEraseDrives is used to remove any residual data from drives that have a status of &quot;available.&quot; For example, when replacing a drive at its end-of-life that contained sensitive data.&#x27;, &#x27;It uses a Security Erase Unit command to write a predetermined pattern to the drive and resets the encryption key on the drive. The method may take up to two minutes to complete, so it is an asynchronous method.&#x27;, &#x27;The GetAsyncResult method can be used to check on the status of the secure erase operation.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;Use the &quot;ListDrives&quot; method to obtain the driveIDs for the drives you want to secure erase.&#x27;]
        [&#x27;SecureEraseDrives is used to remove any residual data from drives that have a status of &quot;available.&quot; For example, when replacing a drive at its end-of-life that contained sensitive data.&#x27;, &#x27;It uses a Security Erase Unit command to write a predetermined pattern to the drive and resets the encryption key on the drive. The method may take up to two minutes to complete, so it is an asynchronous method.&#x27;, &#x27;The GetAsyncResult method can be used to check on the status of the secure erase operation.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;Use the &quot;ListDrives&quot; method to obtain the driveIDs for the drives you want to secure erase.&#x27;]
        [&#x27;SecureEraseDrives is used to remove any residual data from drives that have a status of &quot;available.&quot; For example, when replacing a drive at its end-of-life that contained sensitive data.&#x27;, &#x27;It uses a Security Erase Unit command to write a predetermined pattern to the drive and resets the encryption key on the drive. The method may take up to two minutes to complete, so it is an asynchronous method.&#x27;, &#x27;The GetAsyncResult method can be used to check on the status of the secure erase operation.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;Use the &quot;ListDrives&quot; method to obtain the driveIDs for the drives you want to secure erase.&#x27;]
        [&#x27;SecureEraseDrives is used to remove any residual data from drives that have a status of &quot;available.&quot; For example, when replacing a drive at its end-of-life that contained sensitive data.&#x27;, &#x27;It uses a Security Erase Unit command to write a predetermined pattern to the drive and resets the encryption key on the drive. The method may take up to two minutes to complete, so it is an asynchronous method.&#x27;, &#x27;The GetAsyncResult method can be used to check on the status of the secure erase operation.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;Use the &quot;ListDrives&quot; method to obtain the driveIDs for the drives you want to secure erase.&#x27;]
        [&#x27;SecureEraseDrives is used to remove any residual data from drives that have a status of &quot;available.&quot; For example, when replacing a drive at its end-of-life that contained sensitive data.&#x27;, &#x27;It uses a Security Erase Unit command to write a predetermined pattern to the drive and resets the encryption key on the drive. The method may take up to two minutes to complete, so it is an asynchronous method.&#x27;, &#x27;The GetAsyncResult method can be used to check on the status of the secure erase operation.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;Use the &quot;ListDrives&quot; method to obtain the driveIDs for the drives you want to secure erase.&#x27;]
        :param drives: [required] List of driveIDs to secure erase.
        :type drives: 
        """

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
        [&#x27;You can use RemoveDrives to proactively remove drives that are part of the cluster.&#x27;, &#x27;You may want to use this method when reducing cluster capacity or preparing to replace drives nearing the end of their service life.&#x27;, &#x27;Any data on the drives is removed and migrated to other drives in the cluster before the drive is removed from the cluster. This is an asynchronous method.&#x27;, &#x27;Depending on the total capacity of the drives being removed, it may take several minutes to migrate all of the data.&#x27;, &#x27;Use the &quot;GetAsyncResult&quot; method to check the status of the remove operation.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;When removing multiple drives, use a single &quot;RemoveDrives&quot; method call rather than multiple individual methods with a single drive each.&#x27;, &#x27;This reduces the amount of data balancing that must occur to even stabilize the storage load on the cluster.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;You can also remove drives with a &quot;failed&quot; status using &quot;RemoveDrives&quot;.&#x27;, &#x27;When you remove a drive with a &quot;failed&quot; status it is not returned to an &quot;available&quot; or &quot;active&quot; status.&#x27;, &#x27;The drive is unavailable for use in the cluster.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;Use the &quot;ListDrives&quot; method to obtain the driveIDs for the drives you want to remove.&#x27;]
        [&#x27;You can use RemoveDrives to proactively remove drives that are part of the cluster.&#x27;, &#x27;You may want to use this method when reducing cluster capacity or preparing to replace drives nearing the end of their service life.&#x27;, &#x27;Any data on the drives is removed and migrated to other drives in the cluster before the drive is removed from the cluster. This is an asynchronous method.&#x27;, &#x27;Depending on the total capacity of the drives being removed, it may take several minutes to migrate all of the data.&#x27;, &#x27;Use the &quot;GetAsyncResult&quot; method to check the status of the remove operation.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;When removing multiple drives, use a single &quot;RemoveDrives&quot; method call rather than multiple individual methods with a single drive each.&#x27;, &#x27;This reduces the amount of data balancing that must occur to even stabilize the storage load on the cluster.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;You can also remove drives with a &quot;failed&quot; status using &quot;RemoveDrives&quot;.&#x27;, &#x27;When you remove a drive with a &quot;failed&quot; status it is not returned to an &quot;available&quot; or &quot;active&quot; status.&#x27;, &#x27;The drive is unavailable for use in the cluster.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;Use the &quot;ListDrives&quot; method to obtain the driveIDs for the drives you want to remove.&#x27;]
        [&#x27;You can use RemoveDrives to proactively remove drives that are part of the cluster.&#x27;, &#x27;You may want to use this method when reducing cluster capacity or preparing to replace drives nearing the end of their service life.&#x27;, &#x27;Any data on the drives is removed and migrated to other drives in the cluster before the drive is removed from the cluster. This is an asynchronous method.&#x27;, &#x27;Depending on the total capacity of the drives being removed, it may take several minutes to migrate all of the data.&#x27;, &#x27;Use the &quot;GetAsyncResult&quot; method to check the status of the remove operation.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;When removing multiple drives, use a single &quot;RemoveDrives&quot; method call rather than multiple individual methods with a single drive each.&#x27;, &#x27;This reduces the amount of data balancing that must occur to even stabilize the storage load on the cluster.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;You can also remove drives with a &quot;failed&quot; status using &quot;RemoveDrives&quot;.&#x27;, &#x27;When you remove a drive with a &quot;failed&quot; status it is not returned to an &quot;available&quot; or &quot;active&quot; status.&#x27;, &#x27;The drive is unavailable for use in the cluster.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;Use the &quot;ListDrives&quot; method to obtain the driveIDs for the drives you want to remove.&#x27;]
        [&#x27;You can use RemoveDrives to proactively remove drives that are part of the cluster.&#x27;, &#x27;You may want to use this method when reducing cluster capacity or preparing to replace drives nearing the end of their service life.&#x27;, &#x27;Any data on the drives is removed and migrated to other drives in the cluster before the drive is removed from the cluster. This is an asynchronous method.&#x27;, &#x27;Depending on the total capacity of the drives being removed, it may take several minutes to migrate all of the data.&#x27;, &#x27;Use the &quot;GetAsyncResult&quot; method to check the status of the remove operation.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;When removing multiple drives, use a single &quot;RemoveDrives&quot; method call rather than multiple individual methods with a single drive each.&#x27;, &#x27;This reduces the amount of data balancing that must occur to even stabilize the storage load on the cluster.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;You can also remove drives with a &quot;failed&quot; status using &quot;RemoveDrives&quot;.&#x27;, &#x27;When you remove a drive with a &quot;failed&quot; status it is not returned to an &quot;available&quot; or &quot;active&quot; status.&#x27;, &#x27;The drive is unavailable for use in the cluster.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;Use the &quot;ListDrives&quot; method to obtain the driveIDs for the drives you want to remove.&#x27;]
        [&#x27;You can use RemoveDrives to proactively remove drives that are part of the cluster.&#x27;, &#x27;You may want to use this method when reducing cluster capacity or preparing to replace drives nearing the end of their service life.&#x27;, &#x27;Any data on the drives is removed and migrated to other drives in the cluster before the drive is removed from the cluster. This is an asynchronous method.&#x27;, &#x27;Depending on the total capacity of the drives being removed, it may take several minutes to migrate all of the data.&#x27;, &#x27;Use the &quot;GetAsyncResult&quot; method to check the status of the remove operation.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;When removing multiple drives, use a single &quot;RemoveDrives&quot; method call rather than multiple individual methods with a single drive each.&#x27;, &#x27;This reduces the amount of data balancing that must occur to even stabilize the storage load on the cluster.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;You can also remove drives with a &quot;failed&quot; status using &quot;RemoveDrives&quot;.&#x27;, &#x27;When you remove a drive with a &quot;failed&quot; status it is not returned to an &quot;available&quot; or &quot;active&quot; status.&#x27;, &#x27;The drive is unavailable for use in the cluster.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;Use the &quot;ListDrives&quot; method to obtain the driveIDs for the drives you want to remove.&#x27;]
        [&#x27;You can use RemoveDrives to proactively remove drives that are part of the cluster.&#x27;, &#x27;You may want to use this method when reducing cluster capacity or preparing to replace drives nearing the end of their service life.&#x27;, &#x27;Any data on the drives is removed and migrated to other drives in the cluster before the drive is removed from the cluster. This is an asynchronous method.&#x27;, &#x27;Depending on the total capacity of the drives being removed, it may take several minutes to migrate all of the data.&#x27;, &#x27;Use the &quot;GetAsyncResult&quot; method to check the status of the remove operation.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;When removing multiple drives, use a single &quot;RemoveDrives&quot; method call rather than multiple individual methods with a single drive each.&#x27;, &#x27;This reduces the amount of data balancing that must occur to even stabilize the storage load on the cluster.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;You can also remove drives with a &quot;failed&quot; status using &quot;RemoveDrives&quot;.&#x27;, &#x27;When you remove a drive with a &quot;failed&quot; status it is not returned to an &quot;available&quot; or &quot;active&quot; status.&#x27;, &#x27;The drive is unavailable for use in the cluster.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;Use the &quot;ListDrives&quot; method to obtain the driveIDs for the drives you want to remove.&#x27;]
        [&#x27;You can use RemoveDrives to proactively remove drives that are part of the cluster.&#x27;, &#x27;You may want to use this method when reducing cluster capacity or preparing to replace drives nearing the end of their service life.&#x27;, &#x27;Any data on the drives is removed and migrated to other drives in the cluster before the drive is removed from the cluster. This is an asynchronous method.&#x27;, &#x27;Depending on the total capacity of the drives being removed, it may take several minutes to migrate all of the data.&#x27;, &#x27;Use the &quot;GetAsyncResult&quot; method to check the status of the remove operation.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;When removing multiple drives, use a single &quot;RemoveDrives&quot; method call rather than multiple individual methods with a single drive each.&#x27;, &#x27;This reduces the amount of data balancing that must occur to even stabilize the storage load on the cluster.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;You can also remove drives with a &quot;failed&quot; status using &quot;RemoveDrives&quot;.&#x27;, &#x27;When you remove a drive with a &quot;failed&quot; status it is not returned to an &quot;available&quot; or &quot;active&quot; status.&#x27;, &#x27;The drive is unavailable for use in the cluster.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;Use the &quot;ListDrives&quot; method to obtain the driveIDs for the drives you want to remove.&#x27;]
        [&#x27;You can use RemoveDrives to proactively remove drives that are part of the cluster.&#x27;, &#x27;You may want to use this method when reducing cluster capacity or preparing to replace drives nearing the end of their service life.&#x27;, &#x27;Any data on the drives is removed and migrated to other drives in the cluster before the drive is removed from the cluster. This is an asynchronous method.&#x27;, &#x27;Depending on the total capacity of the drives being removed, it may take several minutes to migrate all of the data.&#x27;, &#x27;Use the &quot;GetAsyncResult&quot; method to check the status of the remove operation.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;When removing multiple drives, use a single &quot;RemoveDrives&quot; method call rather than multiple individual methods with a single drive each.&#x27;, &#x27;This reduces the amount of data balancing that must occur to even stabilize the storage load on the cluster.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;You can also remove drives with a &quot;failed&quot; status using &quot;RemoveDrives&quot;.&#x27;, &#x27;When you remove a drive with a &quot;failed&quot; status it is not returned to an &quot;available&quot; or &quot;active&quot; status.&#x27;, &#x27;The drive is unavailable for use in the cluster.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;Use the &quot;ListDrives&quot; method to obtain the driveIDs for the drives you want to remove.&#x27;]
        [&#x27;You can use RemoveDrives to proactively remove drives that are part of the cluster.&#x27;, &#x27;You may want to use this method when reducing cluster capacity or preparing to replace drives nearing the end of their service life.&#x27;, &#x27;Any data on the drives is removed and migrated to other drives in the cluster before the drive is removed from the cluster. This is an asynchronous method.&#x27;, &#x27;Depending on the total capacity of the drives being removed, it may take several minutes to migrate all of the data.&#x27;, &#x27;Use the &quot;GetAsyncResult&quot; method to check the status of the remove operation.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;When removing multiple drives, use a single &quot;RemoveDrives&quot; method call rather than multiple individual methods with a single drive each.&#x27;, &#x27;This reduces the amount of data balancing that must occur to even stabilize the storage load on the cluster.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;You can also remove drives with a &quot;failed&quot; status using &quot;RemoveDrives&quot;.&#x27;, &#x27;When you remove a drive with a &quot;failed&quot; status it is not returned to an &quot;available&quot; or &quot;active&quot; status.&#x27;, &#x27;The drive is unavailable for use in the cluster.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;Use the &quot;ListDrives&quot; method to obtain the driveIDs for the drives you want to remove.&#x27;]
        [&#x27;You can use RemoveDrives to proactively remove drives that are part of the cluster.&#x27;, &#x27;You may want to use this method when reducing cluster capacity or preparing to replace drives nearing the end of their service life.&#x27;, &#x27;Any data on the drives is removed and migrated to other drives in the cluster before the drive is removed from the cluster. This is an asynchronous method.&#x27;, &#x27;Depending on the total capacity of the drives being removed, it may take several minutes to migrate all of the data.&#x27;, &#x27;Use the &quot;GetAsyncResult&quot; method to check the status of the remove operation.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;When removing multiple drives, use a single &quot;RemoveDrives&quot; method call rather than multiple individual methods with a single drive each.&#x27;, &#x27;This reduces the amount of data balancing that must occur to even stabilize the storage load on the cluster.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;You can also remove drives with a &quot;failed&quot; status using &quot;RemoveDrives&quot;.&#x27;, &#x27;When you remove a drive with a &quot;failed&quot; status it is not returned to an &quot;available&quot; or &quot;active&quot; status.&#x27;, &#x27;The drive is unavailable for use in the cluster.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;Use the &quot;ListDrives&quot; method to obtain the driveIDs for the drives you want to remove.&#x27;]
        [&#x27;You can use RemoveDrives to proactively remove drives that are part of the cluster.&#x27;, &#x27;You may want to use this method when reducing cluster capacity or preparing to replace drives nearing the end of their service life.&#x27;, &#x27;Any data on the drives is removed and migrated to other drives in the cluster before the drive is removed from the cluster. This is an asynchronous method.&#x27;, &#x27;Depending on the total capacity of the drives being removed, it may take several minutes to migrate all of the data.&#x27;, &#x27;Use the &quot;GetAsyncResult&quot; method to check the status of the remove operation.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;When removing multiple drives, use a single &quot;RemoveDrives&quot; method call rather than multiple individual methods with a single drive each.&#x27;, &#x27;This reduces the amount of data balancing that must occur to even stabilize the storage load on the cluster.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;You can also remove drives with a &quot;failed&quot; status using &quot;RemoveDrives&quot;.&#x27;, &#x27;When you remove a drive with a &quot;failed&quot; status it is not returned to an &quot;available&quot; or &quot;active&quot; status.&#x27;, &#x27;The drive is unavailable for use in the cluster.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;Use the &quot;ListDrives&quot; method to obtain the driveIDs for the drives you want to remove.&#x27;]
        [&#x27;You can use RemoveDrives to proactively remove drives that are part of the cluster.&#x27;, &#x27;You may want to use this method when reducing cluster capacity or preparing to replace drives nearing the end of their service life.&#x27;, &#x27;Any data on the drives is removed and migrated to other drives in the cluster before the drive is removed from the cluster. This is an asynchronous method.&#x27;, &#x27;Depending on the total capacity of the drives being removed, it may take several minutes to migrate all of the data.&#x27;, &#x27;Use the &quot;GetAsyncResult&quot; method to check the status of the remove operation.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;When removing multiple drives, use a single &quot;RemoveDrives&quot; method call rather than multiple individual methods with a single drive each.&#x27;, &#x27;This reduces the amount of data balancing that must occur to even stabilize the storage load on the cluster.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;You can also remove drives with a &quot;failed&quot; status using &quot;RemoveDrives&quot;.&#x27;, &#x27;When you remove a drive with a &quot;failed&quot; status it is not returned to an &quot;available&quot; or &quot;active&quot; status.&#x27;, &#x27;The drive is unavailable for use in the cluster.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;Use the &quot;ListDrives&quot; method to obtain the driveIDs for the drives you want to remove.&#x27;]
        [&#x27;You can use RemoveDrives to proactively remove drives that are part of the cluster.&#x27;, &#x27;You may want to use this method when reducing cluster capacity or preparing to replace drives nearing the end of their service life.&#x27;, &#x27;Any data on the drives is removed and migrated to other drives in the cluster before the drive is removed from the cluster. This is an asynchronous method.&#x27;, &#x27;Depending on the total capacity of the drives being removed, it may take several minutes to migrate all of the data.&#x27;, &#x27;Use the &quot;GetAsyncResult&quot; method to check the status of the remove operation.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;When removing multiple drives, use a single &quot;RemoveDrives&quot; method call rather than multiple individual methods with a single drive each.&#x27;, &#x27;This reduces the amount of data balancing that must occur to even stabilize the storage load on the cluster.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;You can also remove drives with a &quot;failed&quot; status using &quot;RemoveDrives&quot;.&#x27;, &#x27;When you remove a drive with a &quot;failed&quot; status it is not returned to an &quot;available&quot; or &quot;active&quot; status.&#x27;, &#x27;The drive is unavailable for use in the cluster.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;Use the &quot;ListDrives&quot; method to obtain the driveIDs for the drives you want to remove.&#x27;]
        [&#x27;You can use RemoveDrives to proactively remove drives that are part of the cluster.&#x27;, &#x27;You may want to use this method when reducing cluster capacity or preparing to replace drives nearing the end of their service life.&#x27;, &#x27;Any data on the drives is removed and migrated to other drives in the cluster before the drive is removed from the cluster. This is an asynchronous method.&#x27;, &#x27;Depending on the total capacity of the drives being removed, it may take several minutes to migrate all of the data.&#x27;, &#x27;Use the &quot;GetAsyncResult&quot; method to check the status of the remove operation.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;When removing multiple drives, use a single &quot;RemoveDrives&quot; method call rather than multiple individual methods with a single drive each.&#x27;, &#x27;This reduces the amount of data balancing that must occur to even stabilize the storage load on the cluster.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;You can also remove drives with a &quot;failed&quot; status using &quot;RemoveDrives&quot;.&#x27;, &#x27;When you remove a drive with a &quot;failed&quot; status it is not returned to an &quot;available&quot; or &quot;active&quot; status.&#x27;, &#x27;The drive is unavailable for use in the cluster.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;Use the &quot;ListDrives&quot; method to obtain the driveIDs for the drives you want to remove.&#x27;]
        :param drives: [required] List of driveIDs to remove from the cluster.
        :type drives: 
        """

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
        [&#x27;GetFeatureStatus allows you to retrieve the status of a cluster feature.&#x27;]
        :param feature:  [&#x27;Valid values: vvols: Find the status of the Virtual Volumes (VVOLs) cluster feature.&#x27;]
        :type feature: 
        """

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
        [&#x27;EnableFeature allows you to enable cluster features that are disabled by default.&#x27;]
        :param feature: [required] [&#x27;Valid values: vvols: Enable the Virtual Volumes (VVOLs) cluster feature.&#x27;]
        :type feature: 
        """

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
        [&#x27;The ListFibreChannelPortInfo is used to return information about the Fibre Channel ports. The API method is intended for use on individual nodes; userid and password is required for access to individual Fibre Channel nodes. However, this method can be used on the cluster if the force=true parameter is included in the method call. When used on the cluster, all Fibre Channel interfaces are listed.&#x27;]"""

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
        [&#x27;The ListNodeFibreChannelPortInfo is used to return information about the Fibre Channel ports. The API method is intended for use on individual nodes; userid and password is required for access to individual Fibre Channel nodes. However, this method can be used on the cluster if the force=true parameter is included in the method call. When used on the cluster, all Fibre Channel interfaces are listed.&#x27;]
        :param force:  Specify force=true to call method on all member nodes of the cluster.
        :type force: 
        """

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
        [&#x27;The ListFibreChannelSessions is used to return information about the active Fibre Channel sessions on a cluster.&#x27;]"""

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
        :type type: 
        """

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
            nodeID,):
        """
        GetNodeHardwareInfo is used to return all the hardware info and status for the node specified. This generally includes manufacturers, vendors, versions, and other associated hardware identification information.
        :param nodeID: [required] The ID of the node for which hardware information is being requested.  Information about a  node is returned if a   node is specified.
        :type nodeID: 
        """

        params = { 
            "nodeID": nodeID,
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

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'GetNvramInfo',
            GetNvramInfoResult,
            params
        )

    def invoke_sfapi(
            self,
            method,
            parameters=OPTIONAL,):
        """
        [&#x27;This will invoke any API method supported by the SolidFire API for the version and port the connection is using.&#x27;, &#x27;Returns a nested hashtable of key/value pairs that contain the result of the invoked method.&#x27;]
        [&#x27;This will invoke any API method supported by the SolidFire API for the version and port the connection is using.&#x27;, &#x27;Returns a nested hashtable of key/value pairs that contain the result of the invoked method.&#x27;]
        :param method: [required] The name of the method to invoke. This is case sensitive.
        :type method: 
        
        :param parameters:  [&#x27;An object, normally a dictionary or hashtable of the key/value pairs, to be passed as the params for the method being invoked.&#x27;]
        :type parameters: 
        """

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
            acceptEula=OPTIONAL,
            attributes=OPTIONAL,):
        """
        [&#x27;AddLdapClusterAdmin is used to add a new LDAP Cluster Admin. An LDAP Cluster Admin can be used to manage the cluster via the API and management tools. LDAP Cluster Admins are completely separate and unrelated to standard tenant accounts.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;An LDAP group that has been defined in Active Directory can also be added using this API method. The access level that is given to the group will be passed to the individual users in the LDAP group.&#x27;]
        [&#x27;AddLdapClusterAdmin is used to add a new LDAP Cluster Admin. An LDAP Cluster Admin can be used to manage the cluster via the API and management tools. LDAP Cluster Admins are completely separate and unrelated to standard tenant accounts.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;An LDAP group that has been defined in Active Directory can also be added using this API method. The access level that is given to the group will be passed to the individual users in the LDAP group.&#x27;]
        [&#x27;AddLdapClusterAdmin is used to add a new LDAP Cluster Admin. An LDAP Cluster Admin can be used to manage the cluster via the API and management tools. LDAP Cluster Admins are completely separate and unrelated to standard tenant accounts.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;An LDAP group that has been defined in Active Directory can also be added using this API method. The access level that is given to the group will be passed to the individual users in the LDAP group.&#x27;]
        :param username: [required] The distinguished user name for the new LDAP cluster admin.
        :type username: 
        
        :param access: [required] Controls which methods this Cluster Admin can use. For more details on the levels of access, see the Access Control appendix in the SolidFire API Reference.
        :type access: 
        
        :param acceptEula:  Indicate your acceptance of the End User License Agreement when creating this cluster admin. To accept the EULA, set this parameter to true.
        :type acceptEula: 
        
        :param attributes:  List of Name/Value pairs in JSON object format.
        :type attributes: 
        """

        params = { 
            "username": username,
            "access": access,
        }
        if acceptEula is not None:
            params["acceptEula"] = acceptEula
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
            ldapConfiguration=OPTIONAL,):
        """
        [&#x27;The TestLdapAuthentication is used to verify the currently enabled LDAP authentication configuration settings are correct. If the configuration settings are correct, the API call returns a list of the groups the tested user is a member of.&#x27;]
        :param username: [required] The username to be tested.
        :type username: 
        
        :param password: [required] The password for the username to be tester.
        :type password: 
        
        :param ldapConfiguration:  An ldapConfiguration object to be tested. If this parameter is provided, the API call will test the provided configuration even if LDAP authentication is currently disabled.
        :type ldapConfiguration: 
        """

        params = { 
            "username": username,
            "password": password,
        }
        if ldapConfiguration is not None:
            params["ldapConfiguration"] = ldapConfiguration
        
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
        [&#x27;The GetLdapConfiguration is used to get the LDAP configuration currently active on the cluster.&#x27;]"""

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
            serverURIs,
            authType=OPTIONAL,
            groupSearchBaseDN=OPTIONAL,
            groupSearchCustomFilter=OPTIONAL,
            groupSearchType=OPTIONAL,
            searchBindDN=OPTIONAL,
            searchBindPassword=OPTIONAL,
            userDNTemplate=OPTIONAL,
            userSearchBaseDN=OPTIONAL,
            userSearchFilter=OPTIONAL,):
        """
        [&#x27;The EnableLdapAuthentication method is used to configure an LDAP server connection to use for LDAP authentication to a SolidFire cluster. Users that are members on the LDAP server can then log in to a SolidFire storage system using their LDAP authentication userid and password.&#x27;]
        :param authType:  [&#x27;Identifies which user authentcation method will be used. &lt;br/&gt;&#x27;, &#x27;Must be one of the following:&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;DirectBind&lt;/b&gt;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;SearchAndBind&lt;/b&gt; (default)&#x27;][&#x27;Identifies which user authentcation method will be used. &lt;br/&gt;&#x27;, &#x27;Must be one of the following:&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;DirectBind&lt;/b&gt;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;SearchAndBind&lt;/b&gt; (default)&#x27;][&#x27;Identifies which user authentcation method will be used. &lt;br/&gt;&#x27;, &#x27;Must be one of the following:&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;DirectBind&lt;/b&gt;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;SearchAndBind&lt;/b&gt; (default)&#x27;][&#x27;Identifies which user authentcation method will be used. &lt;br/&gt;&#x27;, &#x27;Must be one of the following:&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;DirectBind&lt;/b&gt;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;SearchAndBind&lt;/b&gt; (default)&#x27;]
        :type authType: 
        
        :param groupSearchBaseDN:  [&#x27;The base DN of the tree to start the group search (will do a subtree search from here).&#x27;]
        :type groupSearchBaseDN: 
        
        :param groupSearchCustomFilter:  [&#x27;REQUIRED for CustomFilter&lt;br/&gt;&#x27;, &quot;For use with the CustomFilter search type, an LDAP filter to use to return the DNs of a user&#x27;s groups.&lt;br/&gt;&quot;, &#x27;The string can have placeholder text of %USERNAME% and %USERDN% to be replaced with their username and full userDN as needed.&#x27;][&#x27;REQUIRED for CustomFilter&lt;br/&gt;&#x27;, &quot;For use with the CustomFilter search type, an LDAP filter to use to return the DNs of a user&#x27;s groups.&lt;br/&gt;&quot;, &#x27;The string can have placeholder text of %USERNAME% and %USERDN% to be replaced with their username and full userDN as needed.&#x27;][&#x27;REQUIRED for CustomFilter&lt;br/&gt;&#x27;, &quot;For use with the CustomFilter search type, an LDAP filter to use to return the DNs of a user&#x27;s groups.&lt;br/&gt;&quot;, &#x27;The string can have placeholder text of %USERNAME% and %USERDN% to be replaced with their username and full userDN as needed.&#x27;]
        :type groupSearchCustomFilter: 
        
        :param groupSearchType:  [&#x27;Controls the default group search filter used, can be one of the following:&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;NoGroups&lt;/b&gt;: No group support.&lt;br/&gt;&#x27;, &quot;&lt;b&gt;ActiveDirectory&lt;/b&gt;: (default) Nested membership of all of a user&#x27;s AD groups.&lt;br/&gt;&quot;, &#x27;&lt;b&gt;MemberDN&lt;/b&gt;: MemberDN style groups (single-level).&#x27;][&#x27;Controls the default group search filter used, can be one of the following:&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;NoGroups&lt;/b&gt;: No group support.&lt;br/&gt;&#x27;, &quot;&lt;b&gt;ActiveDirectory&lt;/b&gt;: (default) Nested membership of all of a user&#x27;s AD groups.&lt;br/&gt;&quot;, &#x27;&lt;b&gt;MemberDN&lt;/b&gt;: MemberDN style groups (single-level).&#x27;][&#x27;Controls the default group search filter used, can be one of the following:&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;NoGroups&lt;/b&gt;: No group support.&lt;br/&gt;&#x27;, &quot;&lt;b&gt;ActiveDirectory&lt;/b&gt;: (default) Nested membership of all of a user&#x27;s AD groups.&lt;br/&gt;&quot;, &#x27;&lt;b&gt;MemberDN&lt;/b&gt;: MemberDN style groups (single-level).&#x27;][&#x27;Controls the default group search filter used, can be one of the following:&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;NoGroups&lt;/b&gt;: No group support.&lt;br/&gt;&#x27;, &quot;&lt;b&gt;ActiveDirectory&lt;/b&gt;: (default) Nested membership of all of a user&#x27;s AD groups.&lt;br/&gt;&quot;, &#x27;&lt;b&gt;MemberDN&lt;/b&gt;: MemberDN style groups (single-level).&#x27;]
        :type groupSearchType: 
        
        :param searchBindDN:  [&#x27;REQUIRED for SearchAndBind&lt;br/&gt;&#x27;, &#x27;A fully qualified DN to log in with to perform an LDAP search for the user (needs read access to the LDAP directory).&#x27;][&#x27;REQUIRED for SearchAndBind&lt;br/&gt;&#x27;, &#x27;A fully qualified DN to log in with to perform an LDAP search for the user (needs read access to the LDAP directory).&#x27;]
        :type searchBindDN: 
        
        :param searchBindPassword:  [&#x27;REQUIRED for SearchAndBind&lt;br/&gt;&#x27;, &#x27;The password for the searchBindDN account used for searching.&#x27;][&#x27;REQUIRED for SearchAndBind&lt;br/&gt;&#x27;, &#x27;The password for the searchBindDN account used for searching.&#x27;]
        :type searchBindPassword: 
        
        :param serverURIs: [required] [&#x27;A list of LDAP server URIs (examples: &quot;ldap://1.2.3.4&quot; and ldaps://1.2.3.4:123&quot;)&#x27;]
        :type serverURIs: 
        
        :param userDNTemplate:  [&#x27;REQUIRED for DirectBind&lt;br/&gt;&#x27;, &#x27;A string that is used to form a fully qualified user DN.&lt;br/&gt;&#x27;, &#x27;The string should have the placeholder text &quot;%USERNAME%&quot; which will be replaced with the username of the authenticating user.&#x27;][&#x27;REQUIRED for DirectBind&lt;br/&gt;&#x27;, &#x27;A string that is used to form a fully qualified user DN.&lt;br/&gt;&#x27;, &#x27;The string should have the placeholder text &quot;%USERNAME%&quot; which will be replaced with the username of the authenticating user.&#x27;][&#x27;REQUIRED for DirectBind&lt;br/&gt;&#x27;, &#x27;A string that is used to form a fully qualified user DN.&lt;br/&gt;&#x27;, &#x27;The string should have the placeholder text &quot;%USERNAME%&quot; which will be replaced with the username of the authenticating user.&#x27;]
        :type userDNTemplate: 
        
        :param userSearchBaseDN:  [&#x27;REQUIRED for SearchAndBind&#x27;, &#x27;The base DN of the tree used to start the search (will do a subtree search from here).&#x27;][&#x27;REQUIRED for SearchAndBind&#x27;, &#x27;The base DN of the tree used to start the search (will do a subtree search from here).&#x27;]
        :type userSearchBaseDN: 
        
        :param userSearchFilter:  [&#x27;REQUIRED for SearchAndBind.&lt;br/&gt;&#x27;, &#x27;The LDAP filter to use.&lt;br/&gt;&#x27;, &#x27;The string should have the placeholder text &quot;%USERNAME%&quot; which will be replaced with the username of the authenticating user.&lt;br/&gt;&#x27;, &#x27;Example: (&amp;(objectClass=person) (sAMAccountName=%USERNAME%)) will use the sAMAccountName field in Active Directory to match the nusername entered at cluster login.&#x27;][&#x27;REQUIRED for SearchAndBind.&lt;br/&gt;&#x27;, &#x27;The LDAP filter to use.&lt;br/&gt;&#x27;, &#x27;The string should have the placeholder text &quot;%USERNAME%&quot; which will be replaced with the username of the authenticating user.&lt;br/&gt;&#x27;, &#x27;Example: (&amp;(objectClass=person) (sAMAccountName=%USERNAME%)) will use the sAMAccountName field in Active Directory to match the nusername entered at cluster login.&#x27;][&#x27;REQUIRED for SearchAndBind.&lt;br/&gt;&#x27;, &#x27;The LDAP filter to use.&lt;br/&gt;&#x27;, &#x27;The string should have the placeholder text &quot;%USERNAME%&quot; which will be replaced with the username of the authenticating user.&lt;br/&gt;&#x27;, &#x27;Example: (&amp;(objectClass=person) (sAMAccountName=%USERNAME%)) will use the sAMAccountName field in Active Directory to match the nusername entered at cluster login.&#x27;][&#x27;REQUIRED for SearchAndBind.&lt;br/&gt;&#x27;, &#x27;The LDAP filter to use.&lt;br/&gt;&#x27;, &#x27;The string should have the placeholder text &quot;%USERNAME%&quot; which will be replaced with the username of the authenticating user.&lt;br/&gt;&#x27;, &#x27;Example: (&amp;(objectClass=person) (sAMAccountName=%USERNAME%)) will use the sAMAccountName field in Active Directory to match the nusername entered at cluster login.&#x27;]
        :type userSearchFilter: 
        """

        params = { 
            "serverURIs": serverURIs,
        }
        if authType is not None:
            params["authType"] = authType
        if groupSearchBaseDN is not None:
            params["groupSearchBaseDN"] = groupSearchBaseDN
        if groupSearchCustomFilter is not None:
            params["groupSearchCustomFilter"] = groupSearchCustomFilter
        if groupSearchType is not None:
            params["groupSearchType"] = groupSearchType
        if searchBindDN is not None:
            params["searchBindDN"] = searchBindDN
        if searchBindPassword is not None:
            params["searchBindPassword"] = searchBindPassword
        if userDNTemplate is not None:
            params["userDNTemplate"] = userDNTemplate
        if userSearchBaseDN is not None:
            params["userSearchBaseDN"] = userSearchBaseDN
        if userSearchFilter is not None:
            params["userSearchFilter"] = userSearchFilter
        
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
        [&#x27;The DisableLdapAuthentication method is used disable LDAP authentication and remove all LDAP configuration settings. This call will not remove any configured cluster admin accounts (user or group). However, those cluster admin accounts will no longer be able to log in.&#x27;]"""

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'DisableLdapAuthentication',
            DisableLdapAuthenticationResult,
            params,
            since=8.0
        )

    def get_login_session_info(
            self,):
        """
        [&#x27;GetLoginSessionInfo is used to return the period of time a log in authentication is valid for both log in shells and the TUI.&#x27;]"""

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'GetLoginSessionInfo',
            GetLoginSessionInfoResult,
            params
        )

    def set_login_session_info(
            self,
            timeout,):
        """
        [&#x27;SetLoginSessionInfo is used to set the period of time a log in authentication is valid. After the log in period elapses without activity on the system the authentication will expire. New log in credentials will be required for continued access to the cluster once the timeout period has elapsed.&#x27;]
        :param timeout: [required] Cluster authentication expiration period. Formatted in HH:mm:ss. For example: 01:30:00, 00:90:00, and 00:00:5400 can all be used to equal a 90 minute timeout period. Default is 30 minutes.
        :type timeout: 
        """

        params = { 
            "timeout": timeout,
        }
        
        # There is no adaptor.
        return self.send_request(
            'SetLoginSessionInfo',
            SetLoginSessionInfoResult,
            params
        )

    def get_remote_logging_hosts(
            self,):
        """
        [&#x27;GetRemoteLoggingHosts is used to retrieve the current list of log servers.&#x27;]"""

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'GetRemoteLoggingHosts',
            GetRemoteLoggingHostsResult,
            params,
            since=8.0
        )

    def set_remote_logging_hosts(
            self,
            remoteHosts,):
        """
        [&#x27;RemoteLoggingHosts is used to configure remote logging from the nodes in the storage cluster to a centralized log server or servers. Remote logging is performed over TCP using the default port 514. This API does not add to the existing logging hosts. Rather, it replaces what currently exists with new values specified by this API method. You can use the GetRemoteLoggingHosts to determine what the current logging hosts are and then use the SetRemoteLoggingHosts to set the desired list of current and new logging hosts.&#x27;]
        :param remoteHosts: [required] List of hosts to send log messages to.
        :type remoteHosts: 
        """

        params = { 
            "remoteHosts": remoteHosts,
        }
        
        # There is no adaptor.
        return self.send_request(
            'SetRemoteLoggingHosts',
            SetRemoteLoggingHostsResult,
            params,
            since=8.0
        )

    def list_network_interfaces(
            self,
            force,):
        """
        [&#x27;The ListNetworkInterfaces API method is used to return information about each network interface on a node. The API method is intended for use on individual nodes. &#x27;]
        :param force: [required] [&#x27;This parameter is necessary when calling this API method against a cluster connection.&#x27;, &#x27;Possible values:&#x27;, &#x27;&lt;strong&gt;true:&lt;/strong&gt; information about all network interfaces in the cluster will be returned.&#x27;, &#x27;&lt;strong&gt;false:&lt;/strong&gt; no information will be returned.&#x27;][&#x27;This parameter is necessary when calling this API method against a cluster connection.&#x27;, &#x27;Possible values:&#x27;, &#x27;&lt;strong&gt;true:&lt;/strong&gt; information about all network interfaces in the cluster will be returned.&#x27;, &#x27;&lt;strong&gt;false:&lt;/strong&gt; no information will be returned.&#x27;][&#x27;This parameter is necessary when calling this API method against a cluster connection.&#x27;, &#x27;Possible values:&#x27;, &#x27;&lt;strong&gt;true:&lt;/strong&gt; information about all network interfaces in the cluster will be returned.&#x27;, &#x27;&lt;strong&gt;false:&lt;/strong&gt; no information will be returned.&#x27;][&#x27;This parameter is necessary when calling this API method against a cluster connection.&#x27;, &#x27;Possible values:&#x27;, &#x27;&lt;strong&gt;true:&lt;/strong&gt; information about all network interfaces in the cluster will be returned.&#x27;, &#x27;&lt;strong&gt;false:&lt;/strong&gt; no information will be returned.&#x27;]
        :type force: 
        """

        params = { 
            "force": force,
        }
        
        # There is no adaptor.
        return self.send_request(
            'ListNetworkInterfaces',
            ListNetworkInterfacesResult,
            params,
            since=7.0
        )

    def list_cluster_network_interfaces(
            self,
            force,):
        """
        [&#x27;The ListClusterNetworkInterfaces API method is used to return information about each network interface on the nodes in a cluster. You must pass the force=true parameter when this method is called against a cluster. When used on the cluster, all interfaces on all nodes are listed.&#x27;]
        :param force: [required] [&#x27;This parameter is necessary when calling this API method against a cluster connection.&#x27;, &#x27;Possible values:&#x27;, &#x27;&lt;strong&gt;true:&lt;/strong&gt; information about all network interfaces in the cluster will be returned.&#x27;, &#x27;&lt;strong&gt;false:&lt;/strong&gt; no information will be returned.&#x27;][&#x27;This parameter is necessary when calling this API method against a cluster connection.&#x27;, &#x27;Possible values:&#x27;, &#x27;&lt;strong&gt;true:&lt;/strong&gt; information about all network interfaces in the cluster will be returned.&#x27;, &#x27;&lt;strong&gt;false:&lt;/strong&gt; no information will be returned.&#x27;][&#x27;This parameter is necessary when calling this API method against a cluster connection.&#x27;, &#x27;Possible values:&#x27;, &#x27;&lt;strong&gt;true:&lt;/strong&gt; information about all network interfaces in the cluster will be returned.&#x27;, &#x27;&lt;strong&gt;false:&lt;/strong&gt; no information will be returned.&#x27;][&#x27;This parameter is necessary when calling this API method against a cluster connection.&#x27;, &#x27;Possible values:&#x27;, &#x27;&lt;strong&gt;true:&lt;/strong&gt; information about all network interfaces in the cluster will be returned.&#x27;, &#x27;&lt;strong&gt;false:&lt;/strong&gt; no information will be returned.&#x27;]
        :type force: 
        """

        params = { 
            "force": force,
        }
        
        # There is no adaptor.
        return self.send_request(
            'ListClusterNetworkInterfaces',
            ListClusterNetworkInterfacesResult,
            params,
            since=7.0
        )

    def list_active_nodes(
            self,):
        """
        ListActiveNodes returns the list of currently active nodes that are in the cluster."""

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
        [&#x27;Gets the list of pending nodes.&#x27;, &#x27;Pending nodes are running and configured to join the cluster, but have not been added via the AddNodes method.&#x27;]
        [&#x27;Gets the list of pending nodes.&#x27;, &#x27;Pending nodes are running and configured to join the cluster, but have not been added via the AddNodes method.&#x27;]"""

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
            pendingNodes,):
        """
        [&#x27;AddNodes is used to add one or more new nodes to the cluster. When a node is not configured and starts up for the first time you are prompted to configure the node. Once a node is configured it is registered as a &quot;pending node&quot; with the cluster.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;Adding a node to a cluster that has been set up for virtual networking will require a sufficient number of virtual storage IP addresses to allocate a virtual IP to the new node. If there are no virtual IP addresses available for the new node, the AddNode operation will not complete successfully. Use the &quot;ModifyVirtualNetwork&quot; method to add more storage IP addresses to your virtual network.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;The software version on each node in a cluster must be compatible. Run the &quot;ListAllNodes&quot; API to see what versions of software are currently running on the cluster nodes. For an explanation of software version compatibility, see &quot;Node Versioning and Compatibility&quot; in the Element API guide.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;Once a node has been added, the drives on the node are made available and can then be added via the &quot;AddDrives&quot; method to increase the storage capacity of the cluster.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Note&lt;/b&gt;: It may take several seconds after adding a new Node for it to start up and register the drives as being available.&#x27;]
        [&#x27;AddNodes is used to add one or more new nodes to the cluster. When a node is not configured and starts up for the first time you are prompted to configure the node. Once a node is configured it is registered as a &quot;pending node&quot; with the cluster.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;Adding a node to a cluster that has been set up for virtual networking will require a sufficient number of virtual storage IP addresses to allocate a virtual IP to the new node. If there are no virtual IP addresses available for the new node, the AddNode operation will not complete successfully. Use the &quot;ModifyVirtualNetwork&quot; method to add more storage IP addresses to your virtual network.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;The software version on each node in a cluster must be compatible. Run the &quot;ListAllNodes&quot; API to see what versions of software are currently running on the cluster nodes. For an explanation of software version compatibility, see &quot;Node Versioning and Compatibility&quot; in the Element API guide.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;Once a node has been added, the drives on the node are made available and can then be added via the &quot;AddDrives&quot; method to increase the storage capacity of the cluster.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Note&lt;/b&gt;: It may take several seconds after adding a new Node for it to start up and register the drives as being available.&#x27;]
        [&#x27;AddNodes is used to add one or more new nodes to the cluster. When a node is not configured and starts up for the first time you are prompted to configure the node. Once a node is configured it is registered as a &quot;pending node&quot; with the cluster.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;Adding a node to a cluster that has been set up for virtual networking will require a sufficient number of virtual storage IP addresses to allocate a virtual IP to the new node. If there are no virtual IP addresses available for the new node, the AddNode operation will not complete successfully. Use the &quot;ModifyVirtualNetwork&quot; method to add more storage IP addresses to your virtual network.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;The software version on each node in a cluster must be compatible. Run the &quot;ListAllNodes&quot; API to see what versions of software are currently running on the cluster nodes. For an explanation of software version compatibility, see &quot;Node Versioning and Compatibility&quot; in the Element API guide.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;Once a node has been added, the drives on the node are made available and can then be added via the &quot;AddDrives&quot; method to increase the storage capacity of the cluster.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Note&lt;/b&gt;: It may take several seconds after adding a new Node for it to start up and register the drives as being available.&#x27;]
        [&#x27;AddNodes is used to add one or more new nodes to the cluster. When a node is not configured and starts up for the first time you are prompted to configure the node. Once a node is configured it is registered as a &quot;pending node&quot; with the cluster.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;Adding a node to a cluster that has been set up for virtual networking will require a sufficient number of virtual storage IP addresses to allocate a virtual IP to the new node. If there are no virtual IP addresses available for the new node, the AddNode operation will not complete successfully. Use the &quot;ModifyVirtualNetwork&quot; method to add more storage IP addresses to your virtual network.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;The software version on each node in a cluster must be compatible. Run the &quot;ListAllNodes&quot; API to see what versions of software are currently running on the cluster nodes. For an explanation of software version compatibility, see &quot;Node Versioning and Compatibility&quot; in the Element API guide.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;Once a node has been added, the drives on the node are made available and can then be added via the &quot;AddDrives&quot; method to increase the storage capacity of the cluster.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Note&lt;/b&gt;: It may take several seconds after adding a new Node for it to start up and register the drives as being available.&#x27;]
        [&#x27;AddNodes is used to add one or more new nodes to the cluster. When a node is not configured and starts up for the first time you are prompted to configure the node. Once a node is configured it is registered as a &quot;pending node&quot; with the cluster.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;Adding a node to a cluster that has been set up for virtual networking will require a sufficient number of virtual storage IP addresses to allocate a virtual IP to the new node. If there are no virtual IP addresses available for the new node, the AddNode operation will not complete successfully. Use the &quot;ModifyVirtualNetwork&quot; method to add more storage IP addresses to your virtual network.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;The software version on each node in a cluster must be compatible. Run the &quot;ListAllNodes&quot; API to see what versions of software are currently running on the cluster nodes. For an explanation of software version compatibility, see &quot;Node Versioning and Compatibility&quot; in the Element API guide.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;Once a node has been added, the drives on the node are made available and can then be added via the &quot;AddDrives&quot; method to increase the storage capacity of the cluster.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Note&lt;/b&gt;: It may take several seconds after adding a new Node for it to start up and register the drives as being available.&#x27;]
        [&#x27;AddNodes is used to add one or more new nodes to the cluster. When a node is not configured and starts up for the first time you are prompted to configure the node. Once a node is configured it is registered as a &quot;pending node&quot; with the cluster.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;Adding a node to a cluster that has been set up for virtual networking will require a sufficient number of virtual storage IP addresses to allocate a virtual IP to the new node. If there are no virtual IP addresses available for the new node, the AddNode operation will not complete successfully. Use the &quot;ModifyVirtualNetwork&quot; method to add more storage IP addresses to your virtual network.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;The software version on each node in a cluster must be compatible. Run the &quot;ListAllNodes&quot; API to see what versions of software are currently running on the cluster nodes. For an explanation of software version compatibility, see &quot;Node Versioning and Compatibility&quot; in the Element API guide.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;Once a node has been added, the drives on the node are made available and can then be added via the &quot;AddDrives&quot; method to increase the storage capacity of the cluster.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Note&lt;/b&gt;: It may take several seconds after adding a new Node for it to start up and register the drives as being available.&#x27;]
        [&#x27;AddNodes is used to add one or more new nodes to the cluster. When a node is not configured and starts up for the first time you are prompted to configure the node. Once a node is configured it is registered as a &quot;pending node&quot; with the cluster.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;Adding a node to a cluster that has been set up for virtual networking will require a sufficient number of virtual storage IP addresses to allocate a virtual IP to the new node. If there are no virtual IP addresses available for the new node, the AddNode operation will not complete successfully. Use the &quot;ModifyVirtualNetwork&quot; method to add more storage IP addresses to your virtual network.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;The software version on each node in a cluster must be compatible. Run the &quot;ListAllNodes&quot; API to see what versions of software are currently running on the cluster nodes. For an explanation of software version compatibility, see &quot;Node Versioning and Compatibility&quot; in the Element API guide.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;Once a node has been added, the drives on the node are made available and can then be added via the &quot;AddDrives&quot; method to increase the storage capacity of the cluster.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Note&lt;/b&gt;: It may take several seconds after adding a new Node for it to start up and register the drives as being available.&#x27;]
        [&#x27;AddNodes is used to add one or more new nodes to the cluster. When a node is not configured and starts up for the first time you are prompted to configure the node. Once a node is configured it is registered as a &quot;pending node&quot; with the cluster.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;Adding a node to a cluster that has been set up for virtual networking will require a sufficient number of virtual storage IP addresses to allocate a virtual IP to the new node. If there are no virtual IP addresses available for the new node, the AddNode operation will not complete successfully. Use the &quot;ModifyVirtualNetwork&quot; method to add more storage IP addresses to your virtual network.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;The software version on each node in a cluster must be compatible. Run the &quot;ListAllNodes&quot; API to see what versions of software are currently running on the cluster nodes. For an explanation of software version compatibility, see &quot;Node Versioning and Compatibility&quot; in the Element API guide.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;Once a node has been added, the drives on the node are made available and can then be added via the &quot;AddDrives&quot; method to increase the storage capacity of the cluster.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Note&lt;/b&gt;: It may take several seconds after adding a new Node for it to start up and register the drives as being available.&#x27;]
        [&#x27;AddNodes is used to add one or more new nodes to the cluster. When a node is not configured and starts up for the first time you are prompted to configure the node. Once a node is configured it is registered as a &quot;pending node&quot; with the cluster.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;Adding a node to a cluster that has been set up for virtual networking will require a sufficient number of virtual storage IP addresses to allocate a virtual IP to the new node. If there are no virtual IP addresses available for the new node, the AddNode operation will not complete successfully. Use the &quot;ModifyVirtualNetwork&quot; method to add more storage IP addresses to your virtual network.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;The software version on each node in a cluster must be compatible. Run the &quot;ListAllNodes&quot; API to see what versions of software are currently running on the cluster nodes. For an explanation of software version compatibility, see &quot;Node Versioning and Compatibility&quot; in the Element API guide.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;Once a node has been added, the drives on the node are made available and can then be added via the &quot;AddDrives&quot; method to increase the storage capacity of the cluster.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Note&lt;/b&gt;: It may take several seconds after adding a new Node for it to start up and register the drives as being available.&#x27;]
        :param pendingNodes: [required] List of PendingNodeIDs for the Nodes to be added. You can obtain the list of Pending Nodes via the ListPendingNodes method.
        :type pendingNodes: 
        """

        params = { 
            "pendingNodes": pendingNodes,
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
        [&#x27;RemoveNodes is used to remove one or more nodes that should no longer participate in the cluster. Before removing a node, all drives it contains must first be removed with &quot;RemoveDrives&quot; method. A node cannot be removed until the RemoveDrives process has completed and all data has been migrated away from the node.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;Once removed, a node registers itself as a pending node and can be added again, or shut down which removes it from the &quot;Pending Node&quot; list.&#x27;]
        [&#x27;RemoveNodes is used to remove one or more nodes that should no longer participate in the cluster. Before removing a node, all drives it contains must first be removed with &quot;RemoveDrives&quot; method. A node cannot be removed until the RemoveDrives process has completed and all data has been migrated away from the node.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;Once removed, a node registers itself as a pending node and can be added again, or shut down which removes it from the &quot;Pending Node&quot; list.&#x27;]
        [&#x27;RemoveNodes is used to remove one or more nodes that should no longer participate in the cluster. Before removing a node, all drives it contains must first be removed with &quot;RemoveDrives&quot; method. A node cannot be removed until the RemoveDrives process has completed and all data has been migrated away from the node.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;Once removed, a node registers itself as a pending node and can be added again, or shut down which removes it from the &quot;Pending Node&quot; list.&#x27;]
        :param nodes: [required] List of NodeIDs for the nodes to be removed.
        :type nodes: 
        """

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
        [&#x27;The GetNetworkConfig API method is used to display the network configuration information for a node.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Note&lt;/b&gt;: This method is available only through the per-node API endpoint 5.0 or later.&#x27;]
        [&#x27;The GetNetworkConfig API method is used to display the network configuration information for a node.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Note&lt;/b&gt;: This method is available only through the per-node API endpoint 5.0 or later.&#x27;]
        [&#x27;The GetNetworkConfig API method is used to display the network configuration information for a node.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Note&lt;/b&gt;: This method is available only through the per-node API endpoint 5.0 or later.&#x27;]"""

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
        [&#x27;The SetConfig API method is used to set all the configuration information for the node. This includes the same information available via calls to SetClusterConfig and SetNetworkConfig in one API method.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &quot;&lt;b&gt;Warning!&lt;/b&gt; Changing the &#x27;bond-mode&#x27; on a node can cause a temporary loss of network connectivity. Caution should be taken when using this method.&quot;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Note&lt;/b&gt;: This method is available only through the per-node API endpoint 5.0 or later.&#x27;]
        [&#x27;The SetConfig API method is used to set all the configuration information for the node. This includes the same information available via calls to SetClusterConfig and SetNetworkConfig in one API method.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &quot;&lt;b&gt;Warning!&lt;/b&gt; Changing the &#x27;bond-mode&#x27; on a node can cause a temporary loss of network connectivity. Caution should be taken when using this method.&quot;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Note&lt;/b&gt;: This method is available only through the per-node API endpoint 5.0 or later.&#x27;]
        [&#x27;The SetConfig API method is used to set all the configuration information for the node. This includes the same information available via calls to SetClusterConfig and SetNetworkConfig in one API method.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &quot;&lt;b&gt;Warning!&lt;/b&gt; Changing the &#x27;bond-mode&#x27; on a node can cause a temporary loss of network connectivity. Caution should be taken when using this method.&quot;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Note&lt;/b&gt;: This method is available only through the per-node API endpoint 5.0 or later.&#x27;]
        [&#x27;The SetConfig API method is used to set all the configuration information for the node. This includes the same information available via calls to SetClusterConfig and SetNetworkConfig in one API method.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &quot;&lt;b&gt;Warning!&lt;/b&gt; Changing the &#x27;bond-mode&#x27; on a node can cause a temporary loss of network connectivity. Caution should be taken when using this method.&quot;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Note&lt;/b&gt;: This method is available only through the per-node API endpoint 5.0 or later.&#x27;]
        [&#x27;The SetConfig API method is used to set all the configuration information for the node. This includes the same information available via calls to SetClusterConfig and SetNetworkConfig in one API method.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &quot;&lt;b&gt;Warning!&lt;/b&gt; Changing the &#x27;bond-mode&#x27; on a node can cause a temporary loss of network connectivity. Caution should be taken when using this method.&quot;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Note&lt;/b&gt;: This method is available only through the per-node API endpoint 5.0 or later.&#x27;]
        :param config: [required] Objects that you want changed for the cluster interface settings.
        :type config: 
        """

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
        [&#x27;The &quot;SetNetworkConfig&quot; method is used to set the network configuration for a node. To see the states in which these objects can be modified, see &quot;Network Object for 1G and 10G Interfaces&quot; on page 109 of the Element API. To display the current network settings for a node, run the &quot;GetNetworkConfig&quot; method.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;WARNING!&lt;/b&gt; Changing the &quot;bond-mode&quot; on a node can cause a temporary loss of network connectivity. Caution should be taken when using this method.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Note&lt;/b&gt;: This method is available only through the per-node API endpoint 5.0 or later.&#x27;]
        [&#x27;The &quot;SetNetworkConfig&quot; method is used to set the network configuration for a node. To see the states in which these objects can be modified, see &quot;Network Object for 1G and 10G Interfaces&quot; on page 109 of the Element API. To display the current network settings for a node, run the &quot;GetNetworkConfig&quot; method.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;WARNING!&lt;/b&gt; Changing the &quot;bond-mode&quot; on a node can cause a temporary loss of network connectivity. Caution should be taken when using this method.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Note&lt;/b&gt;: This method is available only through the per-node API endpoint 5.0 or later.&#x27;]
        [&#x27;The &quot;SetNetworkConfig&quot; method is used to set the network configuration for a node. To see the states in which these objects can be modified, see &quot;Network Object for 1G and 10G Interfaces&quot; on page 109 of the Element API. To display the current network settings for a node, run the &quot;GetNetworkConfig&quot; method.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;WARNING!&lt;/b&gt; Changing the &quot;bond-mode&quot; on a node can cause a temporary loss of network connectivity. Caution should be taken when using this method.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Note&lt;/b&gt;: This method is available only through the per-node API endpoint 5.0 or later.&#x27;]
        [&#x27;The &quot;SetNetworkConfig&quot; method is used to set the network configuration for a node. To see the states in which these objects can be modified, see &quot;Network Object for 1G and 10G Interfaces&quot; on page 109 of the Element API. To display the current network settings for a node, run the &quot;GetNetworkConfig&quot; method.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;WARNING!&lt;/b&gt; Changing the &quot;bond-mode&quot; on a node can cause a temporary loss of network connectivity. Caution should be taken when using this method.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Note&lt;/b&gt;: This method is available only through the per-node API endpoint 5.0 or later.&#x27;]
        [&#x27;The &quot;SetNetworkConfig&quot; method is used to set the network configuration for a node. To see the states in which these objects can be modified, see &quot;Network Object for 1G and 10G Interfaces&quot; on page 109 of the Element API. To display the current network settings for a node, run the &quot;GetNetworkConfig&quot; method.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;WARNING!&lt;/b&gt; Changing the &quot;bond-mode&quot; on a node can cause a temporary loss of network connectivity. Caution should be taken when using this method.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Note&lt;/b&gt;: This method is available only through the per-node API endpoint 5.0 or later.&#x27;]
        :param network: [required] Objects that will be changed for the node network settings.
        :type network: 
        """

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
        [&#x27;The GetConfig API method is used to retrieve all the configuration information for the node. This one API method includes the same information available in both &quot;GetClusterConfig&quot; and &quot;GetNetworkConfig&quot; methods.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Note&lt;/b&gt;: This method is available only through the per-node API endpoint 5.0 or later.&#x27;]
        [&#x27;The GetConfig API method is used to retrieve all the configuration information for the node. This one API method includes the same information available in both &quot;GetClusterConfig&quot; and &quot;GetNetworkConfig&quot; methods.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Note&lt;/b&gt;: This method is available only through the per-node API endpoint 5.0 or later.&#x27;]
        [&#x27;The GetConfig API method is used to retrieve all the configuration information for the node. This one API method includes the same information available in both &quot;GetClusterConfig&quot; and &quot;GetNetworkConfig&quot; methods.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Note&lt;/b&gt;: This method is available only through the per-node API endpoint 5.0 or later.&#x27;]"""

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'GetConfig',
            GetConfigResult,
            params
        )

    def get_bootstrap_config(
            self,):
        """
        [&#x27;GetBootstrapConfig returns the cluster name and node name from the bootstrap configuration file. This API method should be performed on an individual node before it has been configured into a cluster. The resulting information from this method is used in the Cluster Configuration UI when the cluster is eventually created.&#x27;]"""

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'GetBootstrapConfig',
            GetBootstrapConfigResult,
            params
        )

    def get_node_stats(
            self,
            nodeID,):
        """
        [&#x27;GetNodeStats is used to return the high-level activity measurements for a single node.&#x27;]
        :param nodeID: [required] Specifies the node for which statistics are gathered.
        :type nodeID: 
        """

        params = { 
            "nodeID": nodeID,
        }
        
        # There is an adaptor!
        since = None
        deprecated = None

        return ElementServiceAdaptor.get_node_stats(self, params,
                                                  since, deprecated)

    def list_node_stats(
            self,):
        """
        [&#x27;ListNodeStats is used to return the high-level activity measurements for all nodes in a cluster.&#x27;]"""

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'ListNodeStats',
            ListNodeStatsResult,
            params
        )

    def get_pending_operation(
            self,):
        """
        [&#x27;GetPendingOperation is used to detect an operation on a node that is currently in progress. This method can also be used to report back when an operation has completed.&lt;br/&gt;&#x27;, &#x27;&lt;br/&gt;&#x27;, &#x27;Note: This method is available only through the per-node API endpoint 5.0 or later.&#x27;]
        [&#x27;GetPendingOperation is used to detect an operation on a node that is currently in progress. This method can also be used to report back when an operation has completed.&lt;br/&gt;&#x27;, &#x27;&lt;br/&gt;&#x27;, &#x27;Note: This method is available only through the per-node API endpoint 5.0 or later.&#x27;]
        [&#x27;GetPendingOperation is used to detect an operation on a node that is currently in progress. This method can also be used to report back when an operation has completed.&lt;br/&gt;&#x27;, &#x27;&lt;br/&gt;&#x27;, &#x27;Note: This method is available only through the per-node API endpoint 5.0 or later.&#x27;]"""

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'GetPendingOperation',
            GetPendingOperationResult,
            params
        )

    def list_cluster_pairs(
            self,):
        """
        [&#x27;ListClusterPairs is used to list all of the clusters a cluster is paired with.&#x27;, &#x27;This method returns information about active and pending cluster pairings, such as statistics about the current pairing as well as the connectivity and latency (in milliseconds) of the cluster pairing.&#x27;]
        [&#x27;ListClusterPairs is used to list all of the clusters a cluster is paired with.&#x27;, &#x27;This method returns information about active and pending cluster pairings, such as statistics about the current pairing as well as the connectivity and latency (in milliseconds) of the cluster pairing.&#x27;]"""

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
        [&#x27;ListActivePairedVolumes is used to list all of the active volumes paired with a volume.&#x27;, &#x27;Volumes listed in the return for this method include volumes with active and pending pairings.&#x27;]
        [&#x27;ListActivePairedVolumes is used to list all of the active volumes paired with a volume.&#x27;, &#x27;Volumes listed in the return for this method include volumes with active and pending pairings.&#x27;]"""

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
        [&#x27;StartClusterPairing is used to create an encoded key from a cluster that is used to pair with another cluster.&#x27;, &#x27;The key created from this API method is used in the &quot;CompleteClusterPairing&quot; API method to establish a cluster pairing.&#x27;, &#x27;You can pair a cluster with a maximum of four other SolidFire clusters.&#x27;]
        [&#x27;StartClusterPairing is used to create an encoded key from a cluster that is used to pair with another cluster.&#x27;, &#x27;The key created from this API method is used in the &quot;CompleteClusterPairing&quot; API method to establish a cluster pairing.&#x27;, &#x27;You can pair a cluster with a maximum of four other SolidFire clusters.&#x27;]
        [&#x27;StartClusterPairing is used to create an encoded key from a cluster that is used to pair with another cluster.&#x27;, &#x27;The key created from this API method is used in the &quot;CompleteClusterPairing&quot; API method to establish a cluster pairing.&#x27;, &#x27;You can pair a cluster with a maximum of four other SolidFire clusters.&#x27;]"""

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
            volumeID,
            mode=OPTIONAL,):
        """
        [&#x27;StartVolumePairing is used to create an encoded key from a volume that is used to pair with another volume.&#x27;, &#x27;The key that this method creates is used in the &quot;CompleteVolumePairing&quot; API method to establish a volume pairing.&#x27;]
        [&#x27;StartVolumePairing is used to create an encoded key from a volume that is used to pair with another volume.&#x27;, &#x27;The key that this method creates is used in the &quot;CompleteVolumePairing&quot; API method to establish a volume pairing.&#x27;]
        :param volumeID: [required] The ID of the volume on which to start the pairing process.
        :type volumeID: 
        
        :param mode:  [&#x27;The mode of the volume on which to start the pairing process. The mode can only be set if the volume is the source volume.&lt;br/&gt;&#x27;, &#x27;Possible values:&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Async&lt;/b&gt;: (default if no mode parameter specified) Writes are acknowledged when they complete locally. The cluster does not wait for writes to be replicated to the target cluster.&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Sync&lt;/b&gt;: Source acknowledges write when the data is stored locally and on the remote cluster.&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;SnapshotsOnly&lt;/b&gt;: Only snapshots created on the source cluster will be replicated. Active writes from the source volume will not be replicated.&lt;br/&gt;&#x27;][&#x27;The mode of the volume on which to start the pairing process. The mode can only be set if the volume is the source volume.&lt;br/&gt;&#x27;, &#x27;Possible values:&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Async&lt;/b&gt;: (default if no mode parameter specified) Writes are acknowledged when they complete locally. The cluster does not wait for writes to be replicated to the target cluster.&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Sync&lt;/b&gt;: Source acknowledges write when the data is stored locally and on the remote cluster.&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;SnapshotsOnly&lt;/b&gt;: Only snapshots created on the source cluster will be replicated. Active writes from the source volume will not be replicated.&lt;br/&gt;&#x27;][&#x27;The mode of the volume on which to start the pairing process. The mode can only be set if the volume is the source volume.&lt;br/&gt;&#x27;, &#x27;Possible values:&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Async&lt;/b&gt;: (default if no mode parameter specified) Writes are acknowledged when they complete locally. The cluster does not wait for writes to be replicated to the target cluster.&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Sync&lt;/b&gt;: Source acknowledges write when the data is stored locally and on the remote cluster.&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;SnapshotsOnly&lt;/b&gt;: Only snapshots created on the source cluster will be replicated. Active writes from the source volume will not be replicated.&lt;br/&gt;&#x27;][&#x27;The mode of the volume on which to start the pairing process. The mode can only be set if the volume is the source volume.&lt;br/&gt;&#x27;, &#x27;Possible values:&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Async&lt;/b&gt;: (default if no mode parameter specified) Writes are acknowledged when they complete locally. The cluster does not wait for writes to be replicated to the target cluster.&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Sync&lt;/b&gt;: Source acknowledges write when the data is stored locally and on the remote cluster.&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;SnapshotsOnly&lt;/b&gt;: Only snapshots created on the source cluster will be replicated. Active writes from the source volume will not be replicated.&lt;br/&gt;&#x27;][&#x27;The mode of the volume on which to start the pairing process. The mode can only be set if the volume is the source volume.&lt;br/&gt;&#x27;, &#x27;Possible values:&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Async&lt;/b&gt;: (default if no mode parameter specified) Writes are acknowledged when they complete locally. The cluster does not wait for writes to be replicated to the target cluster.&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Sync&lt;/b&gt;: Source acknowledges write when the data is stored locally and on the remote cluster.&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;SnapshotsOnly&lt;/b&gt;: Only snapshots created on the source cluster will be replicated. Active writes from the source volume will not be replicated.&lt;br/&gt;&#x27;]
        :type mode: 
        """

        params = { 
            "volumeID": volumeID,
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
            clusterPairingKey,):
        """
        [&#x27;The CompleteClusterPairing method is the second step in the cluster pairing process.&#x27;, &#x27;Use this method with the encoded key received from the &quot;StartClusterPairing&quot; API method to complete the cluster pairing process.&#x27;]
        [&#x27;The CompleteClusterPairing method is the second step in the cluster pairing process.&#x27;, &#x27;Use this method with the encoded key received from the &quot;StartClusterPairing&quot; API method to complete the cluster pairing process.&#x27;]
        :param clusterPairingKey: [required] A string of characters that is returned from the &quot;StartClusterPairing&quot; API method.
        :type clusterPairingKey: 
        """

        params = { 
            "clusterPairingKey": clusterPairingKey,
        }
        
        # There is no adaptor.
        return self.send_request(
            'CompleteClusterPairing',
            CompleteClusterPairingResult,
            params
        )

    def complete_volume_pairing(
            self,
            volumePairingKey,
            volumeID,):
        """
        [&#x27;CompleteVolumePairing is used to complete the pairing of two volumes.&#x27;]
        :param volumePairingKey: [required] The key returned from the &quot;StartVolumePairing&quot; API method.
        :type volumePairingKey: 
        
        :param volumeID: [required] The ID of volume on which to complete the pairing process.
        :type volumeID: 
        """

        params = { 
            "volumePairingKey": volumePairingKey,
            "volumeID": volumeID,
        }
        
        # There is no adaptor.
        return self.send_request(
            'CompleteVolumePairing',
            CompleteVolumePairingResult,
            params
        )

    def remove_cluster_pair(
            self,
            clusterPairID,):
        """
        [&#x27;You can use the RemoveClusterPair method to close the open connections between two paired clusters.&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Note&lt;/b&gt;: Before you remove a cluster pair, you must first remove all volume pairing to the clusters with the &quot;RemoveVolumePair&quot; API method.&#x27;]
        [&#x27;You can use the RemoveClusterPair method to close the open connections between two paired clusters.&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Note&lt;/b&gt;: Before you remove a cluster pair, you must first remove all volume pairing to the clusters with the &quot;RemoveVolumePair&quot; API method.&#x27;]
        :param clusterPairID: [required] Unique identifier used to pair two clusters.
        :type clusterPairID: 
        """

        params = { 
            "clusterPairID": clusterPairID,
        }
        
        # There is no adaptor.
        return self.send_request(
            'RemoveClusterPair',
            RemoveClusterPairResult,
            params
        )

    def remove_volume_pair(
            self,
            volumeID,):
        """
        [&#x27;RemoveVolumePair is used to remove the remote pairing between two volumes.&#x27;, &#x27;When the volume pairing information is removed, data is no longer replicated to or from the volume.&#x27;, &#x27;This method should be run on both the source and target volumes that are paired together.&#x27;]
        [&#x27;RemoveVolumePair is used to remove the remote pairing between two volumes.&#x27;, &#x27;When the volume pairing information is removed, data is no longer replicated to or from the volume.&#x27;, &#x27;This method should be run on both the source and target volumes that are paired together.&#x27;]
        [&#x27;RemoveVolumePair is used to remove the remote pairing between two volumes.&#x27;, &#x27;When the volume pairing information is removed, data is no longer replicated to or from the volume.&#x27;, &#x27;This method should be run on both the source and target volumes that are paired together.&#x27;]
        :param volumeID: [required] ID of the volume on which to stop the replication process.
        :type volumeID: 
        """

        params = { 
            "volumeID": volumeID,
        }
        
        # There is no adaptor.
        return self.send_request(
            'RemoveVolumePair',
            RemoveVolumePairResult,
            params
        )

    def modify_volume_pair(
            self,
            volumeID,
            pausedManual=OPTIONAL,
            mode=OPTIONAL,):
        """
        [&#x27;ModifyVolumePair is used to pause or restart replication between a pair of volumes.&#x27;]
        :param volumeID: [required] Identification number of the volume to be modified.
        :type volumeID: 
        
        :param pausedManual:  [&#x27;Valid values that can be entered:&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;true&lt;/b&gt;: to pause volume replication.&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;false&lt;/b&gt;: to restart volume replication.&lt;br/&gt;&#x27;, &#x27;If no value is specified, no change in replication is performed.&#x27;][&#x27;Valid values that can be entered:&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;true&lt;/b&gt;: to pause volume replication.&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;false&lt;/b&gt;: to restart volume replication.&lt;br/&gt;&#x27;, &#x27;If no value is specified, no change in replication is performed.&#x27;][&#x27;Valid values that can be entered:&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;true&lt;/b&gt;: to pause volume replication.&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;false&lt;/b&gt;: to restart volume replication.&lt;br/&gt;&#x27;, &#x27;If no value is specified, no change in replication is performed.&#x27;][&#x27;Valid values that can be entered:&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;true&lt;/b&gt;: to pause volume replication.&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;false&lt;/b&gt;: to restart volume replication.&lt;br/&gt;&#x27;, &#x27;If no value is specified, no change in replication is performed.&#x27;]
        :type pausedManual: 
        
        :param mode:  [&#x27;Volume replication mode.&lt;br/&gt;&#x27;, &#x27;Possible values:&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Async&lt;/b&gt;: Writes are acknowledged when they complete locally. The cluster does not wait for writes to be replicated to the target cluster.&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Sync&lt;/b&gt;: The source acknowledges the write when the data is stored locally and on the remote cluster.&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;SnapshotsOnly&lt;/b&gt;: Only snapshots created on the source cluster will be replicated. Active writes from the source volume are not replicated.&lt;br/&gt;&#x27;][&#x27;Volume replication mode.&lt;br/&gt;&#x27;, &#x27;Possible values:&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Async&lt;/b&gt;: Writes are acknowledged when they complete locally. The cluster does not wait for writes to be replicated to the target cluster.&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Sync&lt;/b&gt;: The source acknowledges the write when the data is stored locally and on the remote cluster.&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;SnapshotsOnly&lt;/b&gt;: Only snapshots created on the source cluster will be replicated. Active writes from the source volume are not replicated.&lt;br/&gt;&#x27;][&#x27;Volume replication mode.&lt;br/&gt;&#x27;, &#x27;Possible values:&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Async&lt;/b&gt;: Writes are acknowledged when they complete locally. The cluster does not wait for writes to be replicated to the target cluster.&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Sync&lt;/b&gt;: The source acknowledges the write when the data is stored locally and on the remote cluster.&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;SnapshotsOnly&lt;/b&gt;: Only snapshots created on the source cluster will be replicated. Active writes from the source volume are not replicated.&lt;br/&gt;&#x27;][&#x27;Volume replication mode.&lt;br/&gt;&#x27;, &#x27;Possible values:&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Async&lt;/b&gt;: Writes are acknowledged when they complete locally. The cluster does not wait for writes to be replicated to the target cluster.&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Sync&lt;/b&gt;: The source acknowledges the write when the data is stored locally and on the remote cluster.&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;SnapshotsOnly&lt;/b&gt;: Only snapshots created on the source cluster will be replicated. Active writes from the source volume are not replicated.&lt;br/&gt;&#x27;][&#x27;Volume replication mode.&lt;br/&gt;&#x27;, &#x27;Possible values:&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Async&lt;/b&gt;: Writes are acknowledged when they complete locally. The cluster does not wait for writes to be replicated to the target cluster.&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Sync&lt;/b&gt;: The source acknowledges the write when the data is stored locally and on the remote cluster.&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;SnapshotsOnly&lt;/b&gt;: Only snapshots created on the source cluster will be replicated. Active writes from the source volume are not replicated.&lt;br/&gt;&#x27;]
        :type mode: 
        """

        params = { 
            "volumeID": volumeID,
        }
        if pausedManual is not None:
            params["pausedManual"] = pausedManual
        if mode is not None:
            params["mode"] = mode
        
        # There is no adaptor.
        return self.send_request(
            'ModifyVolumePair',
            ModifyVolumePairResult,
            params
        )

    def list_protocol_endpoints(
            self,
            protocolEndpointIDs=OPTIONAL,):
        """
        [&#x27;Gets protocol endpoints in the system&#x27;, &quot;If protocolEndpointIDs isn&#x27;t specified all protocol endpoints&quot;, &#x27;are returned. Else the supplied protocolEndpointIDs are.&#x27;]
        [&#x27;Gets protocol endpoints in the system&#x27;, &quot;If protocolEndpointIDs isn&#x27;t specified all protocol endpoints&quot;, &#x27;are returned. Else the supplied protocolEndpointIDs are.&#x27;]
        [&#x27;Gets protocol endpoints in the system&#x27;, &quot;If protocolEndpointIDs isn&#x27;t specified all protocol endpoints&quot;, &#x27;are returned. Else the supplied protocolEndpointIDs are.&#x27;]
        :param protocolEndpointIDs:  
        :type protocolEndpointIDs: 
        """

        params = { 
        }
        if protocolEndpointIDs is not None:
            params["protocolEndpointIDs"] = protocolEndpointIDs
        
        # There is no adaptor.
        return self.send_request(
            'ListProtocolEndpoints',
            ListProtocolEndpointsResult,
            params
        )

    def list_services(
            self,):
        """
        [&#x27;List the services in the cluster.&#x27;]"""

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'ListServices',
            ListServicesResult,
            params
        )

    def create_snapshot(
            self,
            volumeID,
            snapshotID=OPTIONAL,
            name=OPTIONAL,
            enableRemoteReplication=OPTIONAL,
            retention=OPTIONAL,
            attributes=OPTIONAL,):
        """
        [&#x27;CreateSnapshot is used to create a point-in-time copy of a volume.&#x27;, &#x27;A snapshot can be created from any volume or from an existing snapshot.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Note&lt;/b&gt;: Creating a snapshot is allowed if cluster fullness is at stage 2 or 3.&#x27;, &#x27;Snapshots are not created when cluster fullness is at stage 4 or 5.&#x27;]
        [&#x27;CreateSnapshot is used to create a point-in-time copy of a volume.&#x27;, &#x27;A snapshot can be created from any volume or from an existing snapshot.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Note&lt;/b&gt;: Creating a snapshot is allowed if cluster fullness is at stage 2 or 3.&#x27;, &#x27;Snapshots are not created when cluster fullness is at stage 4 or 5.&#x27;]
        [&#x27;CreateSnapshot is used to create a point-in-time copy of a volume.&#x27;, &#x27;A snapshot can be created from any volume or from an existing snapshot.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Note&lt;/b&gt;: Creating a snapshot is allowed if cluster fullness is at stage 2 or 3.&#x27;, &#x27;Snapshots are not created when cluster fullness is at stage 4 or 5.&#x27;]
        [&#x27;CreateSnapshot is used to create a point-in-time copy of a volume.&#x27;, &#x27;A snapshot can be created from any volume or from an existing snapshot.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Note&lt;/b&gt;: Creating a snapshot is allowed if cluster fullness is at stage 2 or 3.&#x27;, &#x27;Snapshots are not created when cluster fullness is at stage 4 or 5.&#x27;]
        [&#x27;CreateSnapshot is used to create a point-in-time copy of a volume.&#x27;, &#x27;A snapshot can be created from any volume or from an existing snapshot.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Note&lt;/b&gt;: Creating a snapshot is allowed if cluster fullness is at stage 2 or 3.&#x27;, &#x27;Snapshots are not created when cluster fullness is at stage 4 or 5.&#x27;]
        :param volumeID: [required] ID of the volume image from which to copy.
        :type volumeID: 
        
        :param snapshotID:  [&#x27;Unique ID of a snapshot from which the new snapshot is made.&#x27;, &#x27;The snapshotID passed must be a snapshot on the given volume.&#x27;, &quot;If a SnapshotID is not provided, a snapshot is created from the volume&#x27;s active branch.&quot;][&#x27;Unique ID of a snapshot from which the new snapshot is made.&#x27;, &#x27;The snapshotID passed must be a snapshot on the given volume.&#x27;, &quot;If a SnapshotID is not provided, a snapshot is created from the volume&#x27;s active branch.&quot;][&#x27;Unique ID of a snapshot from which the new snapshot is made.&#x27;, &#x27;The snapshotID passed must be a snapshot on the given volume.&#x27;, &quot;If a SnapshotID is not provided, a snapshot is created from the volume&#x27;s active branch.&quot;]
        :type snapshotID: 
        
        :param name:  [&#x27;A name for the snapshot.&#x27;, &#x27;If no name is provided, the date and time the snapshot was taken is used.&#x27;][&#x27;A name for the snapshot.&#x27;, &#x27;If no name is provided, the date and time the snapshot was taken is used.&#x27;]
        :type name: 
        
        :param enableRemoteReplication:  Identifies if snapshot is enabled for remote replication.
        :type enableRemoteReplication: 
        
        :param retention:  [&#x27;The amount of time the snapshot will be retained. Enter in HH:mm:ss&#x27;]
        :type retention: 
        
        :param attributes:  List of Name/Value pairs in JSON object format.
        :type attributes: 
        """

        params = { 
            "volumeID": volumeID,
        }
        if snapshotID is not None:
            params["snapshotID"] = snapshotID
        if name is not None:
            params["name"] = name
        if enableRemoteReplication is not None:
            params["enableRemoteReplication"] = enableRemoteReplication
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
            snapshotID,):
        """
        [&#x27;DeleteSnapshot is used to delete a snapshot.&#x27;, &#x27;A snapshot that is currently the &quot;active&quot; snapshot cannot be deleted.&#x27;, &#x27;You must rollback and make another snapshot &quot;active&quot; before the current snapshot can be deleted.&#x27;, &#x27;To rollback a snapshot, use RollbackToSnapshot.&#x27;]
        [&#x27;DeleteSnapshot is used to delete a snapshot.&#x27;, &#x27;A snapshot that is currently the &quot;active&quot; snapshot cannot be deleted.&#x27;, &#x27;You must rollback and make another snapshot &quot;active&quot; before the current snapshot can be deleted.&#x27;, &#x27;To rollback a snapshot, use RollbackToSnapshot.&#x27;]
        [&#x27;DeleteSnapshot is used to delete a snapshot.&#x27;, &#x27;A snapshot that is currently the &quot;active&quot; snapshot cannot be deleted.&#x27;, &#x27;You must rollback and make another snapshot &quot;active&quot; before the current snapshot can be deleted.&#x27;, &#x27;To rollback a snapshot, use RollbackToSnapshot.&#x27;]
        [&#x27;DeleteSnapshot is used to delete a snapshot.&#x27;, &#x27;A snapshot that is currently the &quot;active&quot; snapshot cannot be deleted.&#x27;, &#x27;You must rollback and make another snapshot &quot;active&quot; before the current snapshot can be deleted.&#x27;, &#x27;To rollback a snapshot, use RollbackToSnapshot.&#x27;]
        :param snapshotID: [required] The ID of the snapshot to delete.
        :type snapshotID: 
        """

        params = { 
            "snapshotID": snapshotID,
        }
        
        # There is no adaptor.
        return self.send_request(
            'DeleteSnapshot',
            DeleteSnapshotResult,
            params
        )

    def list_snapshots(
            self,
            volumeID=OPTIONAL,):
        """
        [&#x27;ListSnapshots is used to return the attributes of each snapshot taken on the volume.&#x27;]
        :param volumeID:  [&#x27;The volume to list snapshots for.&#x27;, &#x27;If not provided, all snapshots for all volumes are returned.&#x27;][&#x27;The volume to list snapshots for.&#x27;, &#x27;If not provided, all snapshots for all volumes are returned.&#x27;]
        :type volumeID: 
        """

        params = { 
        }
        if volumeID is not None:
            params["volumeID"] = volumeID
        
        # There is no adaptor.
        return self.send_request(
            'ListSnapshots',
            ListSnapshotsResult,
            params
        )

    def modify_snapshot(
            self,
            snapshotID,
            expirationTime=OPTIONAL,
            enableRemoteReplication=OPTIONAL,):
        """
        [&#x27;ModifySnapshot is used to change the attributes currently assigned to a snapshot.&#x27;, &#x27;Use this API method to enable the snapshots created on the Read/Write (source) volume to be remotely replicated to a target SolidFire storage system.&#x27;]
        [&#x27;ModifySnapshot is used to change the attributes currently assigned to a snapshot.&#x27;, &#x27;Use this API method to enable the snapshots created on the Read/Write (source) volume to be remotely replicated to a target SolidFire storage system.&#x27;]
        :param snapshotID: [required] ID of the snapshot.
        :type snapshotID: 
        
        :param expirationTime:  Use to set the time when the snapshot should be removed.
        :type expirationTime: 
        
        :param enableRemoteReplication:  [&#x27;Use to enable the snapshot created to be replicated to a remote SolidFire cluster.&#x27;, &#x27;Possible values:&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;true&lt;/b&gt;: the snapshot will be replicated to remote storage.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;false&lt;/b&gt;: Default. No replication.&#x27;][&#x27;Use to enable the snapshot created to be replicated to a remote SolidFire cluster.&#x27;, &#x27;Possible values:&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;true&lt;/b&gt;: the snapshot will be replicated to remote storage.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;false&lt;/b&gt;: Default. No replication.&#x27;][&#x27;Use to enable the snapshot created to be replicated to a remote SolidFire cluster.&#x27;, &#x27;Possible values:&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;true&lt;/b&gt;: the snapshot will be replicated to remote storage.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;false&lt;/b&gt;: Default. No replication.&#x27;][&#x27;Use to enable the snapshot created to be replicated to a remote SolidFire cluster.&#x27;, &#x27;Possible values:&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;true&lt;/b&gt;: the snapshot will be replicated to remote storage.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;false&lt;/b&gt;: Default. No replication.&#x27;]
        :type enableRemoteReplication: 
        """

        params = { 
            "snapshotID": snapshotID,
        }
        if expirationTime is not None:
            params["expirationTime"] = expirationTime
        if enableRemoteReplication is not None:
            params["enableRemoteReplication"] = enableRemoteReplication
        
        # There is no adaptor.
        return self.send_request(
            'ModifySnapshot',
            ModifySnapshotResult,
            params,
            since=8.0
        )

    def rollback_to_snapshot(
            self,
            volumeID,
            snapshotID,
            saveCurrentState,
            name=OPTIONAL,
            attributes=OPTIONAL,):
        """
        [&#x27;RollbackToSnapshot is used to make an existing snapshot the &quot;active&quot; volume image. This method creates a new &#x27;, &#x27;snapshot from an existing snapshot. The new snapshot becomes &quot;active&quot; and the existing snapshot is preserved until &#x27;, &#x27;it is manually deleted. The previously &quot;active&quot; snapshot is deleted unless the parameter saveCurrentState is set with &#x27;, &#x27;a value of &quot;true.&quot;&#x27;, &#x27;&lt;b&gt;Note&lt;/b&gt;: Creating a snapshot is allowed if cluster fullness is at stage 2 or 3.&#x27;, &#x27;Snapshots are not created when cluster fullness is at stage 4 or 5.&#x27;]
        [&#x27;RollbackToSnapshot is used to make an existing snapshot the &quot;active&quot; volume image. This method creates a new &#x27;, &#x27;snapshot from an existing snapshot. The new snapshot becomes &quot;active&quot; and the existing snapshot is preserved until &#x27;, &#x27;it is manually deleted. The previously &quot;active&quot; snapshot is deleted unless the parameter saveCurrentState is set with &#x27;, &#x27;a value of &quot;true.&quot;&#x27;, &#x27;&lt;b&gt;Note&lt;/b&gt;: Creating a snapshot is allowed if cluster fullness is at stage 2 or 3.&#x27;, &#x27;Snapshots are not created when cluster fullness is at stage 4 or 5.&#x27;]
        [&#x27;RollbackToSnapshot is used to make an existing snapshot the &quot;active&quot; volume image. This method creates a new &#x27;, &#x27;snapshot from an existing snapshot. The new snapshot becomes &quot;active&quot; and the existing snapshot is preserved until &#x27;, &#x27;it is manually deleted. The previously &quot;active&quot; snapshot is deleted unless the parameter saveCurrentState is set with &#x27;, &#x27;a value of &quot;true.&quot;&#x27;, &#x27;&lt;b&gt;Note&lt;/b&gt;: Creating a snapshot is allowed if cluster fullness is at stage 2 or 3.&#x27;, &#x27;Snapshots are not created when cluster fullness is at stage 4 or 5.&#x27;]
        [&#x27;RollbackToSnapshot is used to make an existing snapshot the &quot;active&quot; volume image. This method creates a new &#x27;, &#x27;snapshot from an existing snapshot. The new snapshot becomes &quot;active&quot; and the existing snapshot is preserved until &#x27;, &#x27;it is manually deleted. The previously &quot;active&quot; snapshot is deleted unless the parameter saveCurrentState is set with &#x27;, &#x27;a value of &quot;true.&quot;&#x27;, &#x27;&lt;b&gt;Note&lt;/b&gt;: Creating a snapshot is allowed if cluster fullness is at stage 2 or 3.&#x27;, &#x27;Snapshots are not created when cluster fullness is at stage 4 or 5.&#x27;]
        [&#x27;RollbackToSnapshot is used to make an existing snapshot the &quot;active&quot; volume image. This method creates a new &#x27;, &#x27;snapshot from an existing snapshot. The new snapshot becomes &quot;active&quot; and the existing snapshot is preserved until &#x27;, &#x27;it is manually deleted. The previously &quot;active&quot; snapshot is deleted unless the parameter saveCurrentState is set with &#x27;, &#x27;a value of &quot;true.&quot;&#x27;, &#x27;&lt;b&gt;Note&lt;/b&gt;: Creating a snapshot is allowed if cluster fullness is at stage 2 or 3.&#x27;, &#x27;Snapshots are not created when cluster fullness is at stage 4 or 5.&#x27;]
        [&#x27;RollbackToSnapshot is used to make an existing snapshot the &quot;active&quot; volume image. This method creates a new &#x27;, &#x27;snapshot from an existing snapshot. The new snapshot becomes &quot;active&quot; and the existing snapshot is preserved until &#x27;, &#x27;it is manually deleted. The previously &quot;active&quot; snapshot is deleted unless the parameter saveCurrentState is set with &#x27;, &#x27;a value of &quot;true.&quot;&#x27;, &#x27;&lt;b&gt;Note&lt;/b&gt;: Creating a snapshot is allowed if cluster fullness is at stage 2 or 3.&#x27;, &#x27;Snapshots are not created when cluster fullness is at stage 4 or 5.&#x27;]
        :param volumeID: [required] [&#x27;VolumeID for the volume.&#x27;]
        :type volumeID: 
        
        :param snapshotID: [required] [&#x27;ID of a previously created snapshot on the given volume.&#x27;]
        :type snapshotID: 
        
        :param saveCurrentState: [required] [&#x27;&lt;br/&gt;&lt;b&gt;true&lt;/b&gt;: The previous active volume image is kept.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;false&lt;/b&gt;: (default) The previous active volume image is deleted.&#x27;][&#x27;&lt;br/&gt;&lt;b&gt;true&lt;/b&gt;: The previous active volume image is kept.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;false&lt;/b&gt;: (default) The previous active volume image is deleted.&#x27;]
        :type saveCurrentState: 
        
        :param name:  [&#x27;Name for the snapshot. If no name is given, then the name of the snapshot being rolled back to is used with &#x27;, &#x27;&quot;-copy&quot; appended to the end of the name.&#x27;][&#x27;Name for the snapshot. If no name is given, then the name of the snapshot being rolled back to is used with &#x27;, &#x27;&quot;-copy&quot; appended to the end of the name.&#x27;]
        :type name: 
        
        :param attributes:  [&#x27;List of Name/Value pairs in JSON object format&#x27;]
        :type attributes: 
        """

        params = { 
            "volumeID": volumeID,
            "snapshotID": snapshotID,
            "saveCurrentState": saveCurrentState,
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
            enableRemoteReplication=OPTIONAL,
            retention=OPTIONAL,
            attributes=OPTIONAL,):
        """
        [&#x27;CreateGroupSnapshot is used to create a point-in-time copy of a group of volumes.&#x27;, &#x27;The snapshot created can then be used later as a backup or rollback to ensure the data on the group of volumes is consistent for the point in time in which the snapshot was created.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Note&lt;/b&gt;: Creating a group snapshot is allowed if cluster fullness is at stage 2 or 3.&#x27;, &#x27;Snapshots are not created when cluster fullness is at stage 4 or 5.&#x27;]
        [&#x27;CreateGroupSnapshot is used to create a point-in-time copy of a group of volumes.&#x27;, &#x27;The snapshot created can then be used later as a backup or rollback to ensure the data on the group of volumes is consistent for the point in time in which the snapshot was created.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Note&lt;/b&gt;: Creating a group snapshot is allowed if cluster fullness is at stage 2 or 3.&#x27;, &#x27;Snapshots are not created when cluster fullness is at stage 4 or 5.&#x27;]
        [&#x27;CreateGroupSnapshot is used to create a point-in-time copy of a group of volumes.&#x27;, &#x27;The snapshot created can then be used later as a backup or rollback to ensure the data on the group of volumes is consistent for the point in time in which the snapshot was created.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Note&lt;/b&gt;: Creating a group snapshot is allowed if cluster fullness is at stage 2 or 3.&#x27;, &#x27;Snapshots are not created when cluster fullness is at stage 4 or 5.&#x27;]
        [&#x27;CreateGroupSnapshot is used to create a point-in-time copy of a group of volumes.&#x27;, &#x27;The snapshot created can then be used later as a backup or rollback to ensure the data on the group of volumes is consistent for the point in time in which the snapshot was created.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Note&lt;/b&gt;: Creating a group snapshot is allowed if cluster fullness is at stage 2 or 3.&#x27;, &#x27;Snapshots are not created when cluster fullness is at stage 4 or 5.&#x27;]
        [&#x27;CreateGroupSnapshot is used to create a point-in-time copy of a group of volumes.&#x27;, &#x27;The snapshot created can then be used later as a backup or rollback to ensure the data on the group of volumes is consistent for the point in time in which the snapshot was created.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Note&lt;/b&gt;: Creating a group snapshot is allowed if cluster fullness is at stage 2 or 3.&#x27;, &#x27;Snapshots are not created when cluster fullness is at stage 4 or 5.&#x27;]
        :param volumes: [required] Unique ID of the volume image from which to copy.
        :type volumes: 
        
        :param name:  [&#x27;A name for the snapshot.&#x27;, &#x27;If no name is provided, the date and time the snapshot was taken is used.&#x27;][&#x27;A name for the snapshot.&#x27;, &#x27;If no name is provided, the date and time the snapshot was taken is used.&#x27;]
        :type name: 
        
        :param enableRemoteReplication:  Identifies if snapshot is enabled for remote replication.
        :type enableRemoteReplication: 
        
        :param retention:  [&#x27;The amount of time the snapshot will be retained. Enter in HH:mm:ss&#x27;]
        :type retention: 
        
        :param attributes:  List of Name/Value pairs in JSON object format.
        :type attributes: 
        """

        params = { 
            "volumes": volumes,
        }
        if name is not None:
            params["name"] = name
        if enableRemoteReplication is not None:
            params["enableRemoteReplication"] = enableRemoteReplication
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
            groupSnapshotID,
            saveMembers,):
        """
        [&#x27;DeleteGroupSnapshot is used to delete a group snapshot.&#x27;, &#x27;The saveMembers parameter can be used to preserve all the snapshots that&#x27;, &#x27;were made for the volumes in the group but the group association will be removed.&#x27;]
        [&#x27;DeleteGroupSnapshot is used to delete a group snapshot.&#x27;, &#x27;The saveMembers parameter can be used to preserve all the snapshots that&#x27;, &#x27;were made for the volumes in the group but the group association will be removed.&#x27;]
        [&#x27;DeleteGroupSnapshot is used to delete a group snapshot.&#x27;, &#x27;The saveMembers parameter can be used to preserve all the snapshots that&#x27;, &#x27;were made for the volumes in the group but the group association will be removed.&#x27;]
        :param groupSnapshotID: [required] Unique ID of the group snapshot.
        :type groupSnapshotID: 
        
        :param saveMembers: [required] [&#x27;&lt;br/&gt;&lt;b&gt;true&lt;/b&gt;: Snapshots are kept, but group association is removed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;false&lt;/b&gt;: The group and snapshots are deleted.&#x27;][&#x27;&lt;br/&gt;&lt;b&gt;true&lt;/b&gt;: Snapshots are kept, but group association is removed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;false&lt;/b&gt;: The group and snapshots are deleted.&#x27;]
        :type saveMembers: 
        """

        params = { 
            "groupSnapshotID": groupSnapshotID,
            "saveMembers": saveMembers,
        }
        
        # There is no adaptor.
        return self.send_request(
            'DeleteGroupSnapshot',
            DeleteGroupSnapshotResult,
            params
        )

    def list_group_snapshots(
            self,
            volumeID=OPTIONAL,):
        """
        [&#x27;ListGroupSnapshots is used to return information about all group snapshots that have been created.&#x27;]
        :param volumeID:  [&#x27;An array of unique volume IDs to query.&#x27;, &#x27;If this parameter is not specified, all group snapshots on the cluster will be included.&#x27;][&#x27;An array of unique volume IDs to query.&#x27;, &#x27;If this parameter is not specified, all group snapshots on the cluster will be included.&#x27;]
        :type volumeID: 
        """

        params = { 
        }
        if volumeID is not None:
            params["volumeID"] = volumeID
        
        # There is no adaptor.
        return self.send_request(
            'ListGroupSnapshots',
            ListGroupSnapshotsResult,
            params
        )

    def modify_group_snapshot(
            self,
            groupSnapshotID,
            expirationTime=OPTIONAL,
            enableRemoteReplication=OPTIONAL,):
        """
        [&#x27;ModifyGroupSnapshot is used to change the attributes currently assigned to a group snapshot.&#x27;]
        :param groupSnapshotID: [required] ID of the snapshot.
        :type groupSnapshotID: 
        
        :param expirationTime:  Use to set the time when the snapshot should be removed.
        :type expirationTime: 
        
        :param enableRemoteReplication:  [&#x27;Use to enable the snapshot created to be replicated to a remote SolidFire cluster.&#x27;, &#x27;Possible values:&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;true&lt;/b&gt;: the snapshot will be replicated to remote storage.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;false&lt;/b&gt;: Default. No replication.&#x27;][&#x27;Use to enable the snapshot created to be replicated to a remote SolidFire cluster.&#x27;, &#x27;Possible values:&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;true&lt;/b&gt;: the snapshot will be replicated to remote storage.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;false&lt;/b&gt;: Default. No replication.&#x27;][&#x27;Use to enable the snapshot created to be replicated to a remote SolidFire cluster.&#x27;, &#x27;Possible values:&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;true&lt;/b&gt;: the snapshot will be replicated to remote storage.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;false&lt;/b&gt;: Default. No replication.&#x27;][&#x27;Use to enable the snapshot created to be replicated to a remote SolidFire cluster.&#x27;, &#x27;Possible values:&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;true&lt;/b&gt;: the snapshot will be replicated to remote storage.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;false&lt;/b&gt;: Default. No replication.&#x27;]
        :type enableRemoteReplication: 
        """

        params = { 
            "groupSnapshotID": groupSnapshotID,
        }
        if expirationTime is not None:
            params["expirationTime"] = expirationTime
        if enableRemoteReplication is not None:
            params["enableRemoteReplication"] = enableRemoteReplication
        
        # There is no adaptor.
        return self.send_request(
            'ModifyGroupSnapshot',
            ModifyGroupSnapshotResult,
            params,
            since=8.0
        )

    def rollback_to_group_snapshot(
            self,
            groupSnapshotID,
            saveCurrentState,
            name=OPTIONAL,
            attributes=OPTIONAL,):
        """
        [&#x27;RollbackToGroupSnapshot is used to roll back each individual volume in a snapshot group to a copy of their individual snapshots.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Note&lt;/b&gt;: Creating a snapshot is allowed if cluster fullness is at stage 2 or 3.&#x27;, &#x27;Snapshots are not created when cluster fullness is at stage 4 or 5.&#x27;]
        [&#x27;RollbackToGroupSnapshot is used to roll back each individual volume in a snapshot group to a copy of their individual snapshots.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Note&lt;/b&gt;: Creating a snapshot is allowed if cluster fullness is at stage 2 or 3.&#x27;, &#x27;Snapshots are not created when cluster fullness is at stage 4 or 5.&#x27;]
        [&#x27;RollbackToGroupSnapshot is used to roll back each individual volume in a snapshot group to a copy of their individual snapshots.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Note&lt;/b&gt;: Creating a snapshot is allowed if cluster fullness is at stage 2 or 3.&#x27;, &#x27;Snapshots are not created when cluster fullness is at stage 4 or 5.&#x27;]
        [&#x27;RollbackToGroupSnapshot is used to roll back each individual volume in a snapshot group to a copy of their individual snapshots.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Note&lt;/b&gt;: Creating a snapshot is allowed if cluster fullness is at stage 2 or 3.&#x27;, &#x27;Snapshots are not created when cluster fullness is at stage 4 or 5.&#x27;]
        :param groupSnapshotID: [required] [&#x27;Unique ID of the group snapshot.&#x27;]
        :type groupSnapshotID: 
        
        :param saveCurrentState: [required] [&#x27;&lt;br/&gt;&lt;b&gt;true&lt;/b&gt;: The previous active volume image is kept.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;false&lt;/b&gt;: (default) The previous active volume image is deleted.&#x27;][&#x27;&lt;br/&gt;&lt;b&gt;true&lt;/b&gt;: The previous active volume image is kept.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;false&lt;/b&gt;: (default) The previous active volume image is deleted.&#x27;]
        :type saveCurrentState: 
        
        :param name:  [&#x27;Name for the snapshot. If no name is given, then the name of the snapshot being rolled back to is used with &#x27;, &#x27;&quot;-copy&quot; appended to the end of the name.&#x27;][&#x27;Name for the snapshot. If no name is given, then the name of the snapshot being rolled back to is used with &#x27;, &#x27;&quot;-copy&quot; appended to the end of the name.&#x27;]
        :type name: 
        
        :param attributes:  [&#x27;List of Name/Value pairs in JSON object format&#x27;]
        :type attributes: 
        """

        params = { 
            "groupSnapshotID": groupSnapshotID,
            "saveCurrentState": saveCurrentState,
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
            scheduleID,):
        """
        [&#x27;GetSchedule is used to return information about a scheduled snapshot that has been created. You can see information about a specified schedule if there are many snapshot schedules in the system. You can include more than one schedule with this method by specifying additional scheduleIDs to the parameter.&#x27;]
        :param scheduleID: [required] [&#x27;Unique ID of the schedule or multiple schedules to display&#x27;]
        :type scheduleID: 
        """

        params = { 
            "scheduleID": scheduleID,
        }
        
        # There is an adaptor!
        since = 8.0
        deprecated = None

        return ElementServiceAdaptor.get_schedule(self, params,
                                                  since, deprecated)

    def list_schedules(
            self,):
        """
        [&#x27;ListSchedule is used to return information about all scheduled snapshots that have been created.&#x27;]"""

        params = { 
        }
        
        # There is an adaptor!
        since = 8.0
        deprecated = None

        return ElementServiceAdaptor.list_schedules(self, params,
                                                  since, deprecated)

    def create_schedule(
            self,
            schedule,):
        """
        [&#x27;CreateSchedule is used to create a schedule that will autonomously make a snapshot of a volume at a defined interval.&lt;br/&gt;&#x27;, &#x27;&lt;br/&gt;&#x27;, &#x27;The snapshot created can be used later as a backup or rollback to ensure the data on a volume or group of volumes is consistent for the point in time in which the snapshot was created. &lt;br/&gt;&#x27;, &#x27;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Note&lt;/b&gt;: Creating a snapshot is allowed if cluster fullness is at stage 2 or 3. Snapshots are not created when cluster fullness is at stage 4 or 5.&#x27;]
        [&#x27;CreateSchedule is used to create a schedule that will autonomously make a snapshot of a volume at a defined interval.&lt;br/&gt;&#x27;, &#x27;&lt;br/&gt;&#x27;, &#x27;The snapshot created can be used later as a backup or rollback to ensure the data on a volume or group of volumes is consistent for the point in time in which the snapshot was created. &lt;br/&gt;&#x27;, &#x27;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Note&lt;/b&gt;: Creating a snapshot is allowed if cluster fullness is at stage 2 or 3. Snapshots are not created when cluster fullness is at stage 4 or 5.&#x27;]
        [&#x27;CreateSchedule is used to create a schedule that will autonomously make a snapshot of a volume at a defined interval.&lt;br/&gt;&#x27;, &#x27;&lt;br/&gt;&#x27;, &#x27;The snapshot created can be used later as a backup or rollback to ensure the data on a volume or group of volumes is consistent for the point in time in which the snapshot was created. &lt;br/&gt;&#x27;, &#x27;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Note&lt;/b&gt;: Creating a snapshot is allowed if cluster fullness is at stage 2 or 3. Snapshots are not created when cluster fullness is at stage 4 or 5.&#x27;]
        [&#x27;CreateSchedule is used to create a schedule that will autonomously make a snapshot of a volume at a defined interval.&lt;br/&gt;&#x27;, &#x27;&lt;br/&gt;&#x27;, &#x27;The snapshot created can be used later as a backup or rollback to ensure the data on a volume or group of volumes is consistent for the point in time in which the snapshot was created. &lt;br/&gt;&#x27;, &#x27;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Note&lt;/b&gt;: Creating a snapshot is allowed if cluster fullness is at stage 2 or 3. Snapshots are not created when cluster fullness is at stage 4 or 5.&#x27;]
        [&#x27;CreateSchedule is used to create a schedule that will autonomously make a snapshot of a volume at a defined interval.&lt;br/&gt;&#x27;, &#x27;&lt;br/&gt;&#x27;, &#x27;The snapshot created can be used later as a backup or rollback to ensure the data on a volume or group of volumes is consistent for the point in time in which the snapshot was created. &lt;br/&gt;&#x27;, &#x27;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Note&lt;/b&gt;: Creating a snapshot is allowed if cluster fullness is at stage 2 or 3. Snapshots are not created when cluster fullness is at stage 4 or 5.&#x27;]
        :param schedule: [required] [&#x27;The &quot;Schedule&quot; object will be used to create a new schedule.&lt;br/&gt;&#x27;, &#x27;Do not set ScheduleID property, it will be ignored.&lt;br/&gt;&#x27;, &#x27;Frequency property must be of type that inherits from Frequency. Valid types are:&lt;br/&gt;&#x27;, &#x27;DaysOfMonthFrequency&lt;br/&gt;&#x27;, &#x27;DaysOrWeekFrequency&lt;br/&gt;&#x27;, &#x27;TimeIntervalFrequency&#x27;][&#x27;The &quot;Schedule&quot; object will be used to create a new schedule.&lt;br/&gt;&#x27;, &#x27;Do not set ScheduleID property, it will be ignored.&lt;br/&gt;&#x27;, &#x27;Frequency property must be of type that inherits from Frequency. Valid types are:&lt;br/&gt;&#x27;, &#x27;DaysOfMonthFrequency&lt;br/&gt;&#x27;, &#x27;DaysOrWeekFrequency&lt;br/&gt;&#x27;, &#x27;TimeIntervalFrequency&#x27;][&#x27;The &quot;Schedule&quot; object will be used to create a new schedule.&lt;br/&gt;&#x27;, &#x27;Do not set ScheduleID property, it will be ignored.&lt;br/&gt;&#x27;, &#x27;Frequency property must be of type that inherits from Frequency. Valid types are:&lt;br/&gt;&#x27;, &#x27;DaysOfMonthFrequency&lt;br/&gt;&#x27;, &#x27;DaysOrWeekFrequency&lt;br/&gt;&#x27;, &#x27;TimeIntervalFrequency&#x27;][&#x27;The &quot;Schedule&quot; object will be used to create a new schedule.&lt;br/&gt;&#x27;, &#x27;Do not set ScheduleID property, it will be ignored.&lt;br/&gt;&#x27;, &#x27;Frequency property must be of type that inherits from Frequency. Valid types are:&lt;br/&gt;&#x27;, &#x27;DaysOfMonthFrequency&lt;br/&gt;&#x27;, &#x27;DaysOrWeekFrequency&lt;br/&gt;&#x27;, &#x27;TimeIntervalFrequency&#x27;][&#x27;The &quot;Schedule&quot; object will be used to create a new schedule.&lt;br/&gt;&#x27;, &#x27;Do not set ScheduleID property, it will be ignored.&lt;br/&gt;&#x27;, &#x27;Frequency property must be of type that inherits from Frequency. Valid types are:&lt;br/&gt;&#x27;, &#x27;DaysOfMonthFrequency&lt;br/&gt;&#x27;, &#x27;DaysOrWeekFrequency&lt;br/&gt;&#x27;, &#x27;TimeIntervalFrequency&#x27;][&#x27;The &quot;Schedule&quot; object will be used to create a new schedule.&lt;br/&gt;&#x27;, &#x27;Do not set ScheduleID property, it will be ignored.&lt;br/&gt;&#x27;, &#x27;Frequency property must be of type that inherits from Frequency. Valid types are:&lt;br/&gt;&#x27;, &#x27;DaysOfMonthFrequency&lt;br/&gt;&#x27;, &#x27;DaysOrWeekFrequency&lt;br/&gt;&#x27;, &#x27;TimeIntervalFrequency&#x27;]
        :type schedule: 
        """

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
        [&#x27;ModifySchedule is used to change the intervals at which a scheduled snapshot occurs. This allows for adjustment to the snapshot frequency and retention.&lt;br/&gt;&#x27;]
        :param schedule: [required] [&#x27;The &quot;Schedule&quot; object will be used to modify an existing schedule.&lt;br/&gt;&#x27;, &#x27;The ScheduleID property is required.&lt;br/&gt;&#x27;, &#x27;Frequency property must be of type that inherits from Frequency. Valid types are:&lt;br/&gt;&#x27;, &#x27;DaysOfMonthFrequency&lt;br/&gt;&#x27;, &#x27;DaysOrWeekFrequency&lt;br/&gt;&#x27;, &#x27;TimeIntervalFrequency&#x27;][&#x27;The &quot;Schedule&quot; object will be used to modify an existing schedule.&lt;br/&gt;&#x27;, &#x27;The ScheduleID property is required.&lt;br/&gt;&#x27;, &#x27;Frequency property must be of type that inherits from Frequency. Valid types are:&lt;br/&gt;&#x27;, &#x27;DaysOfMonthFrequency&lt;br/&gt;&#x27;, &#x27;DaysOrWeekFrequency&lt;br/&gt;&#x27;, &#x27;TimeIntervalFrequency&#x27;][&#x27;The &quot;Schedule&quot; object will be used to modify an existing schedule.&lt;br/&gt;&#x27;, &#x27;The ScheduleID property is required.&lt;br/&gt;&#x27;, &#x27;Frequency property must be of type that inherits from Frequency. Valid types are:&lt;br/&gt;&#x27;, &#x27;DaysOfMonthFrequency&lt;br/&gt;&#x27;, &#x27;DaysOrWeekFrequency&lt;br/&gt;&#x27;, &#x27;TimeIntervalFrequency&#x27;][&#x27;The &quot;Schedule&quot; object will be used to modify an existing schedule.&lt;br/&gt;&#x27;, &#x27;The ScheduleID property is required.&lt;br/&gt;&#x27;, &#x27;Frequency property must be of type that inherits from Frequency. Valid types are:&lt;br/&gt;&#x27;, &#x27;DaysOfMonthFrequency&lt;br/&gt;&#x27;, &#x27;DaysOrWeekFrequency&lt;br/&gt;&#x27;, &#x27;TimeIntervalFrequency&#x27;][&#x27;The &quot;Schedule&quot; object will be used to modify an existing schedule.&lt;br/&gt;&#x27;, &#x27;The ScheduleID property is required.&lt;br/&gt;&#x27;, &#x27;Frequency property must be of type that inherits from Frequency. Valid types are:&lt;br/&gt;&#x27;, &#x27;DaysOfMonthFrequency&lt;br/&gt;&#x27;, &#x27;DaysOrWeekFrequency&lt;br/&gt;&#x27;, &#x27;TimeIntervalFrequency&#x27;][&#x27;The &quot;Schedule&quot; object will be used to modify an existing schedule.&lt;br/&gt;&#x27;, &#x27;The ScheduleID property is required.&lt;br/&gt;&#x27;, &#x27;Frequency property must be of type that inherits from Frequency. Valid types are:&lt;br/&gt;&#x27;, &#x27;DaysOfMonthFrequency&lt;br/&gt;&#x27;, &#x27;DaysOrWeekFrequency&lt;br/&gt;&#x27;, &#x27;TimeIntervalFrequency&#x27;]
        :type schedule: 
        """

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
        [&#x27;The GetRawStats call is used by SolidFire engineering to troubleshoot new features. The data returned from GetRawStats is not documented, it changes frequently, and is not guaranteed to be accurate. It is not recommended to ever use GetRawStats for collecting performance data or any other management integration with a SolidFire cluster.&#x27;, &#x27;The data returned from GetRawStats changes frequently, and is not guaranteed to accurately show performance from the system. It is not recommended to ever use GetRawStats for collecting performance data or any other management integration with a SolidFire cluster.&#x27;]
        [&#x27;The GetRawStats call is used by SolidFire engineering to troubleshoot new features. The data returned from GetRawStats is not documented, it changes frequently, and is not guaranteed to be accurate. It is not recommended to ever use GetRawStats for collecting performance data or any other management integration with a SolidFire cluster.&#x27;, &#x27;The data returned from GetRawStats changes frequently, and is not guaranteed to accurately show performance from the system. It is not recommended to ever use GetRawStats for collecting performance data or any other management integration with a SolidFire cluster.&#x27;]"""

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
        [&#x27;The GetCompleteStats API method is used by SolidFire engineering to troubleshoot new features. The data returned from GetCompleteStats is not documented, changes frequently, and is not guaranteed to be accurate. It is not recommended to ever use GetCompleteStats for collecting performance data or any other management integration with a SolidFire cluster.&#x27;, &#x27;The data returned from GetCompleteStats changes frequently, and is not guaranteed to accurately show performance from the system. It is not recommended to ever use GetCompleteStats for collecting performance data or any other management integration with a SolidFire cluster.&#x27;]
        [&#x27;The GetCompleteStats API method is used by SolidFire engineering to troubleshoot new features. The data returned from GetCompleteStats is not documented, changes frequently, and is not guaranteed to be accurate. It is not recommended to ever use GetCompleteStats for collecting performance data or any other management integration with a SolidFire cluster.&#x27;, &#x27;The data returned from GetCompleteStats changes frequently, and is not guaranteed to accurately show performance from the system. It is not recommended to ever use GetCompleteStats for collecting performance data or any other management integration with a SolidFire cluster.&#x27;]"""

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
            callingHostID=OPTIONAL,
            initiatorSecret=OPTIONAL,
            targetSecret=OPTIONAL,):
        """
        Creates a new VVols storage container.
        :param name: [required] Name of the storage container.
        :type name: 
        
        :param callingHostID:  Non-storagecontainer account that will become a storage container.
        :type callingHostID: 
        
        :param initiatorSecret:  The secret for CHAP authentication for the initiator
        :type initiatorSecret: 
        
        :param targetSecret:  The secret for CHAP authentication for the target
        :type targetSecret: 
        """

        params = { 
            "name": name,
        }
        if callingHostID is not None:
            params["callingHostID"] = callingHostID
        if initiatorSecret is not None:
            params["initiatorSecret"] = initiatorSecret
        if targetSecret is not None:
            params["targetSecret"] = targetSecret
        
        # There is no adaptor.
        return self.send_request(
            'CreateStorageContainer',
            CreateStorageContainerResult,
            params,
            since=9.0
        )

    def delete_storage_containers(
            self,
            storageContainerIDs,
            callingHostID=OPTIONAL,):
        """
        Deletes a storage container from the system.
        :param storageContainerIDs: [required] list of storageContainerID of the storage container to delete.
        :type storageContainerIDs: 
        
        :param callingHostID:  
        :type callingHostID: 
        """

        params = { 
            "storageContainerIDs": storageContainerIDs,
        }
        if callingHostID is not None:
            params["callingHostID"] = callingHostID
        
        # There is no adaptor.
        return self.send_request(
            'DeleteStorageContainers',
            DeleteStorageContainerResult,
            params,
            since=9.0
        )

    def modify_storage_container(
            self,
            storageContainerID,
            initiatorSecret=OPTIONAL,
            targetSecret=OPTIONAL,
            callingHostID=OPTIONAL,):
        """
        Modifies an existing storage container.
        :param storageContainerID: [required] 
        :type storageContainerID: 
        
        :param initiatorSecret:  
        :type initiatorSecret: 
        
        :param targetSecret:  
        :type targetSecret: 
        
        :param callingHostID:  
        :type callingHostID: 
        """

        params = { 
            "storageContainerID": storageContainerID,
        }
        if initiatorSecret is not None:
            params["initiatorSecret"] = initiatorSecret
        if targetSecret is not None:
            params["targetSecret"] = targetSecret
        if callingHostID is not None:
            params["callingHostID"] = callingHostID
        
        # There is no adaptor.
        return self.send_request(
            'ModifyStorageContainer',
            CreateStorageContainerResult,
            params,
            since=9.0
        )

    def list_storage_containers(
            self,
            storageContainerIDs=OPTIONAL,
            callingHostID=OPTIONAL,):
        """
        Gets information for all storage containers currently in the system.
        :param storageContainerIDs:  List of storage containers to get
        :type storageContainerIDs: 
        
        :param callingHostID:  
        :type callingHostID: 
        """

        params = { 
        }
        if storageContainerIDs is not None:
            params["storageContainerIDs"] = storageContainerIDs
        if callingHostID is not None:
            params["callingHostID"] = callingHostID
        
        # There is no adaptor.
        return self.send_request(
            'ListStorageContainers',
            ListStorageContainersResult,
            params,
            since=9.0
        )

    def get_storage_container_efficiency(
            self,
            storageContainerID,):
        """
        GetStorageContainerEfficiency enables you to retrieve efficiency information about a virtual volume storage container.
        :param storageContainerID: [required] The ID of the storage container for which to retrieve efficiency information.
        :type storageContainerID: 
        """

        params = { 
            "storageContainerID": storageContainerID,
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
        [&#x27;The ListTests API method is used to return the tests that are available to run on a node.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;Note&lt;/b&gt;: This method is available only through the per-node API endpoint 5.0 or later.&#x27;]
        [&#x27;The ListTests API method is used to return the tests that are available to run on a node.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;Note&lt;/b&gt;: This method is available only through the per-node API endpoint 5.0 or later.&#x27;]"""

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
        [&#x27;The ListUtilities API method is used to return the tests that are available to run on a node.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;Note&lt;/b&gt;: This method is available only through the per-node API endpoint 5.0 or later.&#x27;]
        [&#x27;The ListUtilities API method is used to return the tests that are available to run on a node.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;Note&lt;/b&gt;: This method is available only through the per-node API endpoint 5.0 or later.&#x27;]"""

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
        [&#x27;The TestConnectEnsemble API method is used to verify connectivity with a sepcified database ensemble. By default it uses the ensemble for the cluster the node is associated with. Alternatively you can provide a different ensemble to test connectivity with.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;Note&lt;/b&gt;: This method is available only through the per-node API endpoint 5.0 or later.&#x27;]
        [&#x27;The TestConnectEnsemble API method is used to verify connectivity with a sepcified database ensemble. By default it uses the ensemble for the cluster the node is associated with. Alternatively you can provide a different ensemble to test connectivity with.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;Note&lt;/b&gt;: This method is available only through the per-node API endpoint 5.0 or later.&#x27;]
        :param ensemble:  A comma-separated list of ensemble node CIPs for connectivity testing
        :type ensemble: 
        """

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
        [&#x27;The TestConnectMvip API method is used to test the management connection to the cluster. The test pings the MVIP and executes a simple API method to verify connectivity.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;Note&lt;/b&gt;: This method is available only through the per-node API endpoint 5.0 or later.&#x27;]
        [&#x27;The TestConnectMvip API method is used to test the management connection to the cluster. The test pings the MVIP and executes a simple API method to verify connectivity.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;Note&lt;/b&gt;: This method is available only through the per-node API endpoint 5.0 or later.&#x27;]
        :param mvip:  Optionally, use to test the management connection of a different MVIP. This is not needed to test the connection to the target cluster.
        :type mvip: 
        """

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
        [&#x27;The TestConnectSvip API method is used to test the storage connection to the cluster. The test pings the SVIP using ICMP packets and when successful connects as an iSCSI initiator.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;Note&lt;/b&gt;: This method is available only through the per-node API endpoint 5.0 or later.&#x27;]
        [&#x27;The TestConnectSvip API method is used to test the storage connection to the cluster. The test pings the SVIP using ICMP packets and when successful connects as an iSCSI initiator.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;Note&lt;/b&gt;: This method is available only through the per-node API endpoint 5.0 or later.&#x27;]
        :param svip:  Optionally, use to test the storage connection of a different SVIP. This is not needed to test the connection to the target cluster.
        :type svip: 
        """

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
            totalTimeoutSec=OPTIONAL,
            packetSize=OPTIONAL,
            pingTimeoutMsec=OPTIONAL,):
        """
        [&#x27;The TestPing API method is used to validate the connection to all nodes in the cluster on both 1G and 10G interfaces using ICMP packets. The test uses the appropriate MTU sizes for each packet based on the MTU settings in the network configuration.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;Note&lt;/b&gt;: This method is available only through the per-node API endpoint 5.0 or later.&#x27;]
        [&#x27;The TestPing API method is used to validate the connection to all nodes in the cluster on both 1G and 10G interfaces using ICMP packets. The test uses the appropriate MTU sizes for each packet based on the MTU settings in the network configuration.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;Note&lt;/b&gt;: This method is available only through the per-node API endpoint 5.0 or later.&#x27;]
        :param attempts:  Specifies the number of times the system should repeat the test ping. Default is 5.
        :type attempts: 
        
        :param hosts:  Specify address or hostnames of devices to ping.
        :type hosts: 
        
        :param totalTimeoutSec:  Specifies the length of time the ping should wait for a system response before issuing the next ping attempt or ending the process.
        :type totalTimeoutSec: 
        
        :param packetSize:  Specify the number of bytes to send in the ICMP packet sent to each IP. Number be less than the maximum MTU specified in the network configuration.
        :type packetSize: 
        
        :param pingTimeoutMsec:  Specify the number of milliseconds to wait for each individual ping response. Default is 500ms.
        :type pingTimeoutMsec: 
        """

        params = { 
        }
        if attempts is not None:
            params["attempts"] = attempts
        if hosts is not None:
            params["hosts"] = hosts
        if totalTimeoutSec is not None:
            params["totalTimeoutSec"] = totalTimeoutSec
        if packetSize is not None:
            params["packetSize"] = packetSize
        if pingTimeoutMsec is not None:
            params["pingTimeoutMsec"] = pingTimeoutMsec
        
        # There is no adaptor.
        return self.send_request(
            'TestPing',
            TestPingResult,
            params
        )

    def list_virtual_networks(
            self,
            virtualNetworkID=OPTIONAL,
            virtualNetworkTag=OPTIONAL,
            virtualNetworkIDs=OPTIONAL,
            virtualNetworkTags=OPTIONAL,):
        """
        [&#x27;ListVirtualNetworks is used to get a list of all the configured virtual networks for the cluster. This method can be used to verify the virtual network settings in the cluster.&#x27;, &#x27;&#x27;, &#x27;This method does not require any parameters to be passed. But, one or more VirtualNetworkIDs or VirtualNetworkTags can be passed in order to filter the results.&#x27;]
        [&#x27;ListVirtualNetworks is used to get a list of all the configured virtual networks for the cluster. This method can be used to verify the virtual network settings in the cluster.&#x27;, &#x27;&#x27;, &#x27;This method does not require any parameters to be passed. But, one or more VirtualNetworkIDs or VirtualNetworkTags can be passed in order to filter the results.&#x27;]
        [&#x27;ListVirtualNetworks is used to get a list of all the configured virtual networks for the cluster. This method can be used to verify the virtual network settings in the cluster.&#x27;, &#x27;&#x27;, &#x27;This method does not require any parameters to be passed. But, one or more VirtualNetworkIDs or VirtualNetworkTags can be passed in order to filter the results.&#x27;]
        :param virtualNetworkID:  Network ID to filter the list for a single virtual network
        :type virtualNetworkID: 
        
        :param virtualNetworkTag:  Network Tag to filter the list for a single virtual network
        :type virtualNetworkTag: 
        
        :param virtualNetworkIDs:  NetworkIDs to include in the list.
        :type virtualNetworkIDs: 
        
        :param virtualNetworkTags:  Network Tags to include in the list.
        :type virtualNetworkTags: 
        """

        params = { 
        }
        if virtualNetworkID is not None:
            params["virtualNetworkID"] = virtualNetworkID
        if virtualNetworkTag is not None:
            params["virtualNetworkTag"] = virtualNetworkTag
        if virtualNetworkIDs is not None:
            params["virtualNetworkIDs"] = virtualNetworkIDs
        if virtualNetworkTags is not None:
            params["virtualNetworkTags"] = virtualNetworkTags
        
        # There is no adaptor.
        return self.send_request(
            'ListVirtualNetworks',
            ListVirtualNetworksResult,
            params,
            since=7.0
        )

    def add_virtual_network(
            self,
            virtualNetworkTag,
            name,
            addressBlocks,
            netmask,
            svip,
            gateway=OPTIONAL,
            namespace=OPTIONAL,
            attributes=OPTIONAL,):
        """
        [&#x27;AddVirtualNetwork is used to add a new virtual network to a cluster configuration. When a virtual network is added, an interface for each node is created and each will require a virtual network IP address. The number of IP addresses specified as a parameter for this API method must be equal to or greater than the number of nodes in the cluster. Virtual network addresses are bulk provisioned by SolidFire and assigned to individual nodes automatically. Virtual network addresses do not need to be assigned to nodes manually.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Note:&lt;/b&gt; The AddVirtualNetwork method is used only to create a new virtual network. If you want to make changes to a virtual network, please use the ModifyVirtualNetwork method.&#x27;]
        [&#x27;AddVirtualNetwork is used to add a new virtual network to a cluster configuration. When a virtual network is added, an interface for each node is created and each will require a virtual network IP address. The number of IP addresses specified as a parameter for this API method must be equal to or greater than the number of nodes in the cluster. Virtual network addresses are bulk provisioned by SolidFire and assigned to individual nodes automatically. Virtual network addresses do not need to be assigned to nodes manually.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Note:&lt;/b&gt; The AddVirtualNetwork method is used only to create a new virtual network. If you want to make changes to a virtual network, please use the ModifyVirtualNetwork method.&#x27;]
        [&#x27;AddVirtualNetwork is used to add a new virtual network to a cluster configuration. When a virtual network is added, an interface for each node is created and each will require a virtual network IP address. The number of IP addresses specified as a parameter for this API method must be equal to or greater than the number of nodes in the cluster. Virtual network addresses are bulk provisioned by SolidFire and assigned to individual nodes automatically. Virtual network addresses do not need to be assigned to nodes manually.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Note:&lt;/b&gt; The AddVirtualNetwork method is used only to create a new virtual network. If you want to make changes to a virtual network, please use the ModifyVirtualNetwork method.&#x27;]
        :param virtualNetworkTag: [required] A unique virtual network (VLAN) tag. Supported values are 1 to 4095 (the number zero (0) is not supported).
        :type virtualNetworkTag: 
        
        :param name: [required] User defined name for the new virtual network.
        :type name: 
        
        :param addressBlocks: [required] [&#x27;Unique Range of IP addresses to include in the virtual network.&#x27;, &#x27;Attributes for this parameter are:&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;start:&lt;/b&gt; start of the IP address range. (String)&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;size:&lt;/b&gt; numbre of IP addresses to include in the block. (Integer)&#x27;][&#x27;Unique Range of IP addresses to include in the virtual network.&#x27;, &#x27;Attributes for this parameter are:&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;start:&lt;/b&gt; start of the IP address range. (String)&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;size:&lt;/b&gt; numbre of IP addresses to include in the block. (Integer)&#x27;][&#x27;Unique Range of IP addresses to include in the virtual network.&#x27;, &#x27;Attributes for this parameter are:&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;start:&lt;/b&gt; start of the IP address range. (String)&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;size:&lt;/b&gt; numbre of IP addresses to include in the block. (Integer)&#x27;][&#x27;Unique Range of IP addresses to include in the virtual network.&#x27;, &#x27;Attributes for this parameter are:&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;start:&lt;/b&gt; start of the IP address range. (String)&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;size:&lt;/b&gt; numbre of IP addresses to include in the block. (Integer)&#x27;]
        :type addressBlocks: 
        
        :param netmask: [required] [&#x27;Unique netmask for the virtual network being created.&#x27;]
        :type netmask: 
        
        :param svip: [required] [&#x27;Unique storage IP address for the virtual network being created.&#x27;]
        :type svip: 
        
        :param gateway:  [&#x27;&#x27;]
        :type gateway: 
        
        :param namespace:  [&#x27;&#x27;]
        :type namespace: 
        
        :param attributes:  [&#x27;List of Name/Value pairs in JSON object format.&#x27;]
        :type attributes: 
        """

        params = { 
            "virtualNetworkTag": virtualNetworkTag,
            "name": name,
            "addressBlocks": addressBlocks,
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
            virtualNetworkID=OPTIONAL,
            virtualNetworkTag=OPTIONAL,
            name=OPTIONAL,
            addressBlocks=OPTIONAL,
            netmask=OPTIONAL,
            svip=OPTIONAL,
            gateway=OPTIONAL,
            namespace=OPTIONAL,
            attributes=OPTIONAL,):
        """
        [&#x27;ModifyVirtualNetwork is used to change various attributes of a VirtualNetwork object. This method can be used to add or remove address blocks, change the netmask IP, or modify the name or description of the virtual network.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Note:&lt;/b&gt; This method requires either the VirtualNetworkID or the VirtualNetworkTag as a parameter, but not both.&#x27;]
        [&#x27;ModifyVirtualNetwork is used to change various attributes of a VirtualNetwork object. This method can be used to add or remove address blocks, change the netmask IP, or modify the name or description of the virtual network.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Note:&lt;/b&gt; This method requires either the VirtualNetworkID or the VirtualNetworkTag as a parameter, but not both.&#x27;]
        [&#x27;ModifyVirtualNetwork is used to change various attributes of a VirtualNetwork object. This method can be used to add or remove address blocks, change the netmask IP, or modify the name or description of the virtual network.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Note:&lt;/b&gt; This method requires either the VirtualNetworkID or the VirtualNetworkTag as a parameter, but not both.&#x27;]
        :param virtualNetworkID:  Unique identifier of the virtual network to modify. This is the virtual network ID assigned by the SolidFire cluster.
        :type virtualNetworkID: 
        
        :param virtualNetworkTag:  Network Tag that identifies the virtual network to modify.
        :type virtualNetworkTag: 
        
        :param name:  New name for the virtual network.
        :type name: 
        
        :param addressBlocks:  [&#x27;New addressBlock to set for this Virtual Network object. This may contain new address blocks to add to the existing object or it may omit unused address blocks that need to be removed. Alternatively, existing address blocks may be extended or reduced in size. The size of the starting addressBlocks for a Virtual Network object can only be increased, and can never be decreased.&#x27;, &#x27;Attributes for this parameter are:&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;start:&lt;/b&gt; start of the IP address range. (String)&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;size:&lt;/b&gt; numbre of IP addresses to include in the block. (Integer)&#x27;][&#x27;New addressBlock to set for this Virtual Network object. This may contain new address blocks to add to the existing object or it may omit unused address blocks that need to be removed. Alternatively, existing address blocks may be extended or reduced in size. The size of the starting addressBlocks for a Virtual Network object can only be increased, and can never be decreased.&#x27;, &#x27;Attributes for this parameter are:&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;start:&lt;/b&gt; start of the IP address range. (String)&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;size:&lt;/b&gt; numbre of IP addresses to include in the block. (Integer)&#x27;][&#x27;New addressBlock to set for this Virtual Network object. This may contain new address blocks to add to the existing object or it may omit unused address blocks that need to be removed. Alternatively, existing address blocks may be extended or reduced in size. The size of the starting addressBlocks for a Virtual Network object can only be increased, and can never be decreased.&#x27;, &#x27;Attributes for this parameter are:&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;start:&lt;/b&gt; start of the IP address range. (String)&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;size:&lt;/b&gt; numbre of IP addresses to include in the block. (Integer)&#x27;][&#x27;New addressBlock to set for this Virtual Network object. This may contain new address blocks to add to the existing object or it may omit unused address blocks that need to be removed. Alternatively, existing address blocks may be extended or reduced in size. The size of the starting addressBlocks for a Virtual Network object can only be increased, and can never be decreased.&#x27;, &#x27;Attributes for this parameter are:&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;start:&lt;/b&gt; start of the IP address range. (String)&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;size:&lt;/b&gt; numbre of IP addresses to include in the block. (Integer)&#x27;]
        :type addressBlocks: 
        
        :param netmask:  [&#x27;New netmask for this virtual network.&#x27;]
        :type netmask: 
        
        :param svip:  [&#x27;The storage virtual IP address for this virtual network. The svip for Virtual Network cannot be changed. A new Virtual Network must be created in order to use a different svip address.&#x27;]
        :type svip: 
        
        :param gateway:  [&#x27;&#x27;]
        :type gateway: 
        
        :param namespace:  [&#x27;&#x27;]
        :type namespace: 
        
        :param attributes:  [&#x27;A new list of Name/Value pairs in JSON object format.&#x27;]
        :type attributes: 
        """

        params = { 
        }
        if virtualNetworkID is not None:
            params["virtualNetworkID"] = virtualNetworkID
        if virtualNetworkTag is not None:
            params["virtualNetworkTag"] = virtualNetworkTag
        if name is not None:
            params["name"] = name
        if addressBlocks is not None:
            params["addressBlocks"] = addressBlocks
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
            virtualNetworkID=OPTIONAL,
            virtualNetworkTag=OPTIONAL,):
        """
        [&#x27;RemoveVirtualNetwork is used to remove a previously added virtual network.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Note:&lt;/b&gt; This method requires either the VirtualNetworkID of the VirtualNetworkTag as a parameter, but not both.&#x27;]
        [&#x27;RemoveVirtualNetwork is used to remove a previously added virtual network.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Note:&lt;/b&gt; This method requires either the VirtualNetworkID of the VirtualNetworkTag as a parameter, but not both.&#x27;]
        [&#x27;RemoveVirtualNetwork is used to remove a previously added virtual network.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Note:&lt;/b&gt; This method requires either the VirtualNetworkID of the VirtualNetworkTag as a parameter, but not both.&#x27;]
        :param virtualNetworkID:  Network ID that identifies the virtual network to remove.
        :type virtualNetworkID: 
        
        :param virtualNetworkTag:  Network Tag that identifies the virtual network to remove.
        :type virtualNetworkTag: 
        """

        params = { 
        }
        if virtualNetworkID is not None:
            params["virtualNetworkID"] = virtualNetworkID
        if virtualNetworkTag is not None:
            params["virtualNetworkTag"] = virtualNetworkTag
        
        # There is no adaptor.
        return self.send_request(
            'RemoveVirtualNetwork',
            RemoveVirtualNetworkResult,
            params,
            since=7.0
        )

    def create_virtual_volume(
            self,
            name,
            storageContainerID,
            virtualVolumeType,
            totalSize,
            qos=OPTIONAL,
            metadata=OPTIONAL,
            callingVirtualVolumeHostID=OPTIONAL,):
        """
        [&#x27;CreateVirtualVolume is used to create a new (empty) Virtual Volume on the cluster.&#x27;, &#x27;When the volume is created successfully it is available for connection via PE.&#x27;]
        [&#x27;CreateVirtualVolume is used to create a new (empty) Virtual Volume on the cluster.&#x27;, &#x27;When the volume is created successfully it is available for connection via PE.&#x27;]
        :param name: [required] [&#x27;Name of the Virtual Volume.&#x27;, &#x27;Not required to be unique, but it is recommended.&#x27;, &#x27;May be 1 to 64 characters in length.&#x27;][&#x27;Name of the Virtual Volume.&#x27;, &#x27;Not required to be unique, but it is recommended.&#x27;, &#x27;May be 1 to 64 characters in length.&#x27;][&#x27;Name of the Virtual Volume.&#x27;, &#x27;Not required to be unique, but it is recommended.&#x27;, &#x27;May be 1 to 64 characters in length.&#x27;]
        :type name: 
        
        :param storageContainerID: [required] UUID for the Storage Container of this volume.
        :type storageContainerID: 
        
        :param virtualVolumeType: [required] VMW_TYPE value for this volume.
        :type virtualVolumeType: 
        
        :param totalSize: [required] Total size of the volume, in bytes. Size is rounded up to the nearest 1MB size.
        :type totalSize: 
        
        :param qos:  [&#x27;Initial quality of service settings for this volume.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;Volumes created without specified QoS values are created with the default values for QoS.&#x27;, &#x27;Default values for a volume can be found by running the GetDefaultQoS method.&#x27;][&#x27;Initial quality of service settings for this volume.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;Volumes created without specified QoS values are created with the default values for QoS.&#x27;, &#x27;Default values for a volume can be found by running the GetDefaultQoS method.&#x27;][&#x27;Initial quality of service settings for this volume.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;Volumes created without specified QoS values are created with the default values for QoS.&#x27;, &#x27;Default values for a volume can be found by running the GetDefaultQoS method.&#x27;][&#x27;Initial quality of service settings for this volume.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;Volumes created without specified QoS values are created with the default values for QoS.&#x27;, &#x27;Default values for a volume can be found by running the GetDefaultQoS method.&#x27;]
        :type qos: 
        
        :param metadata:  [&quot;List of name/value pairs to save in the volume&#x27;s metadata.&quot;]
        :type metadata: 
        
        :param callingVirtualVolumeHostID:  
        :type callingVirtualVolumeHostID: 
        """

        params = { 
            "name": name,
            "storageContainerID": storageContainerID,
            "virtualVolumeType": virtualVolumeType,
            "totalSize": totalSize,
        }
        if qos is not None:
            params["qos"] = qos
        if metadata is not None:
            params["metadata"] = metadata
        if callingVirtualVolumeHostID is not None:
            params["callingVirtualVolumeHostID"] = callingVirtualVolumeHostID
        
        # There is no adaptor.
        return self.send_request(
            'CreateVirtualVolume',
            VirtualVolumeSyncResult,
            params,
            since=9.0
        )

    def delete_virtual_volumes(
            self,
            virtualVolumes,
            callingVirtualVolumeHostID=OPTIONAL,):
        """
        [&#x27;DeleteVirtualVolume marks an active volume for deletion.&#x27;, &#x27;It is purged (permanently deleted) after the cleanup interval elapses.&#x27;, &#x27;After making a request to delete a volume, any active iSCSI connections to the volume is immediately terminated and no further connections are allowed while the volume is in this state.&#x27;, &#x27;It is not returned in target discovery requests.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;Any snapshots of a volume that has been marked to delete are not affected.&#x27;, &#x27;Snapshots are kept until the volume is purged from the system.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;If a volume is marked for deletion, and it has a bulk volume read or bulk volume write operation in progress, the bulk volume operation is stopped.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;If the volume you delete is paired with a volume, replication between the paired volumes is suspended and no data is transferred to it or from it while in a deleted state.&#x27;, &#x27;The remote volume the deleted volume was paired with enters into a PausedMisconfigured state and data is no longer sent to it or from the deleted volume.&#x27;, &#x27;Until the deleted volume is purged, it can be restored and data transfers resumes.&#x27;, &#x27;If the deleted volume gets purged from the system, the volume it was paired with enters into a StoppedMisconfigured state and the volume pairing status is removed.&#x27;, &#x27;The purged volume becomes permanently unavailable.&#x27;]
        [&#x27;DeleteVirtualVolume marks an active volume for deletion.&#x27;, &#x27;It is purged (permanently deleted) after the cleanup interval elapses.&#x27;, &#x27;After making a request to delete a volume, any active iSCSI connections to the volume is immediately terminated and no further connections are allowed while the volume is in this state.&#x27;, &#x27;It is not returned in target discovery requests.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;Any snapshots of a volume that has been marked to delete are not affected.&#x27;, &#x27;Snapshots are kept until the volume is purged from the system.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;If a volume is marked for deletion, and it has a bulk volume read or bulk volume write operation in progress, the bulk volume operation is stopped.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;If the volume you delete is paired with a volume, replication between the paired volumes is suspended and no data is transferred to it or from it while in a deleted state.&#x27;, &#x27;The remote volume the deleted volume was paired with enters into a PausedMisconfigured state and data is no longer sent to it or from the deleted volume.&#x27;, &#x27;Until the deleted volume is purged, it can be restored and data transfers resumes.&#x27;, &#x27;If the deleted volume gets purged from the system, the volume it was paired with enters into a StoppedMisconfigured state and the volume pairing status is removed.&#x27;, &#x27;The purged volume becomes permanently unavailable.&#x27;]
        [&#x27;DeleteVirtualVolume marks an active volume for deletion.&#x27;, &#x27;It is purged (permanently deleted) after the cleanup interval elapses.&#x27;, &#x27;After making a request to delete a volume, any active iSCSI connections to the volume is immediately terminated and no further connections are allowed while the volume is in this state.&#x27;, &#x27;It is not returned in target discovery requests.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;Any snapshots of a volume that has been marked to delete are not affected.&#x27;, &#x27;Snapshots are kept until the volume is purged from the system.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;If a volume is marked for deletion, and it has a bulk volume read or bulk volume write operation in progress, the bulk volume operation is stopped.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;If the volume you delete is paired with a volume, replication between the paired volumes is suspended and no data is transferred to it or from it while in a deleted state.&#x27;, &#x27;The remote volume the deleted volume was paired with enters into a PausedMisconfigured state and data is no longer sent to it or from the deleted volume.&#x27;, &#x27;Until the deleted volume is purged, it can be restored and data transfers resumes.&#x27;, &#x27;If the deleted volume gets purged from the system, the volume it was paired with enters into a StoppedMisconfigured state and the volume pairing status is removed.&#x27;, &#x27;The purged volume becomes permanently unavailable.&#x27;]
        [&#x27;DeleteVirtualVolume marks an active volume for deletion.&#x27;, &#x27;It is purged (permanently deleted) after the cleanup interval elapses.&#x27;, &#x27;After making a request to delete a volume, any active iSCSI connections to the volume is immediately terminated and no further connections are allowed while the volume is in this state.&#x27;, &#x27;It is not returned in target discovery requests.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;Any snapshots of a volume that has been marked to delete are not affected.&#x27;, &#x27;Snapshots are kept until the volume is purged from the system.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;If a volume is marked for deletion, and it has a bulk volume read or bulk volume write operation in progress, the bulk volume operation is stopped.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;If the volume you delete is paired with a volume, replication between the paired volumes is suspended and no data is transferred to it or from it while in a deleted state.&#x27;, &#x27;The remote volume the deleted volume was paired with enters into a PausedMisconfigured state and data is no longer sent to it or from the deleted volume.&#x27;, &#x27;Until the deleted volume is purged, it can be restored and data transfers resumes.&#x27;, &#x27;If the deleted volume gets purged from the system, the volume it was paired with enters into a StoppedMisconfigured state and the volume pairing status is removed.&#x27;, &#x27;The purged volume becomes permanently unavailable.&#x27;]
        [&#x27;DeleteVirtualVolume marks an active volume for deletion.&#x27;, &#x27;It is purged (permanently deleted) after the cleanup interval elapses.&#x27;, &#x27;After making a request to delete a volume, any active iSCSI connections to the volume is immediately terminated and no further connections are allowed while the volume is in this state.&#x27;, &#x27;It is not returned in target discovery requests.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;Any snapshots of a volume that has been marked to delete are not affected.&#x27;, &#x27;Snapshots are kept until the volume is purged from the system.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;If a volume is marked for deletion, and it has a bulk volume read or bulk volume write operation in progress, the bulk volume operation is stopped.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;If the volume you delete is paired with a volume, replication between the paired volumes is suspended and no data is transferred to it or from it while in a deleted state.&#x27;, &#x27;The remote volume the deleted volume was paired with enters into a PausedMisconfigured state and data is no longer sent to it or from the deleted volume.&#x27;, &#x27;Until the deleted volume is purged, it can be restored and data transfers resumes.&#x27;, &#x27;If the deleted volume gets purged from the system, the volume it was paired with enters into a StoppedMisconfigured state and the volume pairing status is removed.&#x27;, &#x27;The purged volume becomes permanently unavailable.&#x27;]
        [&#x27;DeleteVirtualVolume marks an active volume for deletion.&#x27;, &#x27;It is purged (permanently deleted) after the cleanup interval elapses.&#x27;, &#x27;After making a request to delete a volume, any active iSCSI connections to the volume is immediately terminated and no further connections are allowed while the volume is in this state.&#x27;, &#x27;It is not returned in target discovery requests.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;Any snapshots of a volume that has been marked to delete are not affected.&#x27;, &#x27;Snapshots are kept until the volume is purged from the system.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;If a volume is marked for deletion, and it has a bulk volume read or bulk volume write operation in progress, the bulk volume operation is stopped.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;If the volume you delete is paired with a volume, replication between the paired volumes is suspended and no data is transferred to it or from it while in a deleted state.&#x27;, &#x27;The remote volume the deleted volume was paired with enters into a PausedMisconfigured state and data is no longer sent to it or from the deleted volume.&#x27;, &#x27;Until the deleted volume is purged, it can be restored and data transfers resumes.&#x27;, &#x27;If the deleted volume gets purged from the system, the volume it was paired with enters into a StoppedMisconfigured state and the volume pairing status is removed.&#x27;, &#x27;The purged volume becomes permanently unavailable.&#x27;]
        [&#x27;DeleteVirtualVolume marks an active volume for deletion.&#x27;, &#x27;It is purged (permanently deleted) after the cleanup interval elapses.&#x27;, &#x27;After making a request to delete a volume, any active iSCSI connections to the volume is immediately terminated and no further connections are allowed while the volume is in this state.&#x27;, &#x27;It is not returned in target discovery requests.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;Any snapshots of a volume that has been marked to delete are not affected.&#x27;, &#x27;Snapshots are kept until the volume is purged from the system.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;If a volume is marked for deletion, and it has a bulk volume read or bulk volume write operation in progress, the bulk volume operation is stopped.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;If the volume you delete is paired with a volume, replication between the paired volumes is suspended and no data is transferred to it or from it while in a deleted state.&#x27;, &#x27;The remote volume the deleted volume was paired with enters into a PausedMisconfigured state and data is no longer sent to it or from the deleted volume.&#x27;, &#x27;Until the deleted volume is purged, it can be restored and data transfers resumes.&#x27;, &#x27;If the deleted volume gets purged from the system, the volume it was paired with enters into a StoppedMisconfigured state and the volume pairing status is removed.&#x27;, &#x27;The purged volume becomes permanently unavailable.&#x27;]
        [&#x27;DeleteVirtualVolume marks an active volume for deletion.&#x27;, &#x27;It is purged (permanently deleted) after the cleanup interval elapses.&#x27;, &#x27;After making a request to delete a volume, any active iSCSI connections to the volume is immediately terminated and no further connections are allowed while the volume is in this state.&#x27;, &#x27;It is not returned in target discovery requests.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;Any snapshots of a volume that has been marked to delete are not affected.&#x27;, &#x27;Snapshots are kept until the volume is purged from the system.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;If a volume is marked for deletion, and it has a bulk volume read or bulk volume write operation in progress, the bulk volume operation is stopped.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;If the volume you delete is paired with a volume, replication between the paired volumes is suspended and no data is transferred to it or from it while in a deleted state.&#x27;, &#x27;The remote volume the deleted volume was paired with enters into a PausedMisconfigured state and data is no longer sent to it or from the deleted volume.&#x27;, &#x27;Until the deleted volume is purged, it can be restored and data transfers resumes.&#x27;, &#x27;If the deleted volume gets purged from the system, the volume it was paired with enters into a StoppedMisconfigured state and the volume pairing status is removed.&#x27;, &#x27;The purged volume becomes permanently unavailable.&#x27;]
        [&#x27;DeleteVirtualVolume marks an active volume for deletion.&#x27;, &#x27;It is purged (permanently deleted) after the cleanup interval elapses.&#x27;, &#x27;After making a request to delete a volume, any active iSCSI connections to the volume is immediately terminated and no further connections are allowed while the volume is in this state.&#x27;, &#x27;It is not returned in target discovery requests.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;Any snapshots of a volume that has been marked to delete are not affected.&#x27;, &#x27;Snapshots are kept until the volume is purged from the system.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;If a volume is marked for deletion, and it has a bulk volume read or bulk volume write operation in progress, the bulk volume operation is stopped.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;If the volume you delete is paired with a volume, replication between the paired volumes is suspended and no data is transferred to it or from it while in a deleted state.&#x27;, &#x27;The remote volume the deleted volume was paired with enters into a PausedMisconfigured state and data is no longer sent to it or from the deleted volume.&#x27;, &#x27;Until the deleted volume is purged, it can be restored and data transfers resumes.&#x27;, &#x27;If the deleted volume gets purged from the system, the volume it was paired with enters into a StoppedMisconfigured state and the volume pairing status is removed.&#x27;, &#x27;The purged volume becomes permanently unavailable.&#x27;]
        [&#x27;DeleteVirtualVolume marks an active volume for deletion.&#x27;, &#x27;It is purged (permanently deleted) after the cleanup interval elapses.&#x27;, &#x27;After making a request to delete a volume, any active iSCSI connections to the volume is immediately terminated and no further connections are allowed while the volume is in this state.&#x27;, &#x27;It is not returned in target discovery requests.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;Any snapshots of a volume that has been marked to delete are not affected.&#x27;, &#x27;Snapshots are kept until the volume is purged from the system.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;If a volume is marked for deletion, and it has a bulk volume read or bulk volume write operation in progress, the bulk volume operation is stopped.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;If the volume you delete is paired with a volume, replication between the paired volumes is suspended and no data is transferred to it or from it while in a deleted state.&#x27;, &#x27;The remote volume the deleted volume was paired with enters into a PausedMisconfigured state and data is no longer sent to it or from the deleted volume.&#x27;, &#x27;Until the deleted volume is purged, it can be restored and data transfers resumes.&#x27;, &#x27;If the deleted volume gets purged from the system, the volume it was paired with enters into a StoppedMisconfigured state and the volume pairing status is removed.&#x27;, &#x27;The purged volume becomes permanently unavailable.&#x27;]
        [&#x27;DeleteVirtualVolume marks an active volume for deletion.&#x27;, &#x27;It is purged (permanently deleted) after the cleanup interval elapses.&#x27;, &#x27;After making a request to delete a volume, any active iSCSI connections to the volume is immediately terminated and no further connections are allowed while the volume is in this state.&#x27;, &#x27;It is not returned in target discovery requests.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;Any snapshots of a volume that has been marked to delete are not affected.&#x27;, &#x27;Snapshots are kept until the volume is purged from the system.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;If a volume is marked for deletion, and it has a bulk volume read or bulk volume write operation in progress, the bulk volume operation is stopped.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;If the volume you delete is paired with a volume, replication between the paired volumes is suspended and no data is transferred to it or from it while in a deleted state.&#x27;, &#x27;The remote volume the deleted volume was paired with enters into a PausedMisconfigured state and data is no longer sent to it or from the deleted volume.&#x27;, &#x27;Until the deleted volume is purged, it can be restored and data transfers resumes.&#x27;, &#x27;If the deleted volume gets purged from the system, the volume it was paired with enters into a StoppedMisconfigured state and the volume pairing status is removed.&#x27;, &#x27;The purged volume becomes permanently unavailable.&#x27;]
        [&#x27;DeleteVirtualVolume marks an active volume for deletion.&#x27;, &#x27;It is purged (permanently deleted) after the cleanup interval elapses.&#x27;, &#x27;After making a request to delete a volume, any active iSCSI connections to the volume is immediately terminated and no further connections are allowed while the volume is in this state.&#x27;, &#x27;It is not returned in target discovery requests.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;Any snapshots of a volume that has been marked to delete are not affected.&#x27;, &#x27;Snapshots are kept until the volume is purged from the system.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;If a volume is marked for deletion, and it has a bulk volume read or bulk volume write operation in progress, the bulk volume operation is stopped.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;If the volume you delete is paired with a volume, replication between the paired volumes is suspended and no data is transferred to it or from it while in a deleted state.&#x27;, &#x27;The remote volume the deleted volume was paired with enters into a PausedMisconfigured state and data is no longer sent to it or from the deleted volume.&#x27;, &#x27;Until the deleted volume is purged, it can be restored and data transfers resumes.&#x27;, &#x27;If the deleted volume gets purged from the system, the volume it was paired with enters into a StoppedMisconfigured state and the volume pairing status is removed.&#x27;, &#x27;The purged volume becomes permanently unavailable.&#x27;]
        [&#x27;DeleteVirtualVolume marks an active volume for deletion.&#x27;, &#x27;It is purged (permanently deleted) after the cleanup interval elapses.&#x27;, &#x27;After making a request to delete a volume, any active iSCSI connections to the volume is immediately terminated and no further connections are allowed while the volume is in this state.&#x27;, &#x27;It is not returned in target discovery requests.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;Any snapshots of a volume that has been marked to delete are not affected.&#x27;, &#x27;Snapshots are kept until the volume is purged from the system.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;If a volume is marked for deletion, and it has a bulk volume read or bulk volume write operation in progress, the bulk volume operation is stopped.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;If the volume you delete is paired with a volume, replication between the paired volumes is suspended and no data is transferred to it or from it while in a deleted state.&#x27;, &#x27;The remote volume the deleted volume was paired with enters into a PausedMisconfigured state and data is no longer sent to it or from the deleted volume.&#x27;, &#x27;Until the deleted volume is purged, it can be restored and data transfers resumes.&#x27;, &#x27;If the deleted volume gets purged from the system, the volume it was paired with enters into a StoppedMisconfigured state and the volume pairing status is removed.&#x27;, &#x27;The purged volume becomes permanently unavailable.&#x27;]
        [&#x27;DeleteVirtualVolume marks an active volume for deletion.&#x27;, &#x27;It is purged (permanently deleted) after the cleanup interval elapses.&#x27;, &#x27;After making a request to delete a volume, any active iSCSI connections to the volume is immediately terminated and no further connections are allowed while the volume is in this state.&#x27;, &#x27;It is not returned in target discovery requests.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;Any snapshots of a volume that has been marked to delete are not affected.&#x27;, &#x27;Snapshots are kept until the volume is purged from the system.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;If a volume is marked for deletion, and it has a bulk volume read or bulk volume write operation in progress, the bulk volume operation is stopped.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;If the volume you delete is paired with a volume, replication between the paired volumes is suspended and no data is transferred to it or from it while in a deleted state.&#x27;, &#x27;The remote volume the deleted volume was paired with enters into a PausedMisconfigured state and data is no longer sent to it or from the deleted volume.&#x27;, &#x27;Until the deleted volume is purged, it can be restored and data transfers resumes.&#x27;, &#x27;If the deleted volume gets purged from the system, the volume it was paired with enters into a StoppedMisconfigured state and the volume pairing status is removed.&#x27;, &#x27;The purged volume becomes permanently unavailable.&#x27;]
        [&#x27;DeleteVirtualVolume marks an active volume for deletion.&#x27;, &#x27;It is purged (permanently deleted) after the cleanup interval elapses.&#x27;, &#x27;After making a request to delete a volume, any active iSCSI connections to the volume is immediately terminated and no further connections are allowed while the volume is in this state.&#x27;, &#x27;It is not returned in target discovery requests.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;Any snapshots of a volume that has been marked to delete are not affected.&#x27;, &#x27;Snapshots are kept until the volume is purged from the system.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;If a volume is marked for deletion, and it has a bulk volume read or bulk volume write operation in progress, the bulk volume operation is stopped.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;If the volume you delete is paired with a volume, replication between the paired volumes is suspended and no data is transferred to it or from it while in a deleted state.&#x27;, &#x27;The remote volume the deleted volume was paired with enters into a PausedMisconfigured state and data is no longer sent to it or from the deleted volume.&#x27;, &#x27;Until the deleted volume is purged, it can be restored and data transfers resumes.&#x27;, &#x27;If the deleted volume gets purged from the system, the volume it was paired with enters into a StoppedMisconfigured state and the volume pairing status is removed.&#x27;, &#x27;The purged volume becomes permanently unavailable.&#x27;]
        :param virtualVolumes: [required] The UUID of the volume to delete.
        :type virtualVolumes: 
        
        :param callingVirtualVolumeHostID:  
        :type callingVirtualVolumeHostID: 
        """

        params = { 
            "virtualVolumes": virtualVolumes,
        }
        if callingVirtualVolumeHostID is not None:
            params["callingVirtualVolumeHostID"] = callingVirtualVolumeHostID
        
        # There is no adaptor.
        return self.send_request(
            'DeleteVirtualVolumes',
            VirtualVolumeNullResult,
            params,
            since=9.0
        )

    def list_virtual_volumes(
            self,
            startVirtualVolumeID=OPTIONAL,
            limit=OPTIONAL,
            virtualVolumeIDs=OPTIONAL,
            callingVirtualVolumeHostID=OPTIONAL,):
        """
        :param startVirtualVolumeID:  [&#x27;The ID of the first Virtual Volume to list.&#x27;, &#x27;This can be useful for paging results.&#x27;, &#x27;By default, this lists all Virtual Volumes.&#x27;][&#x27;The ID of the first Virtual Volume to list.&#x27;, &#x27;This can be useful for paging results.&#x27;, &#x27;By default, this lists all Virtual Volumes.&#x27;][&#x27;The ID of the first Virtual Volume to list.&#x27;, &#x27;This can be useful for paging results.&#x27;, &#x27;By default, this lists all Virtual Volumes.&#x27;]
        :type startVirtualVolumeID: 
        
        :param limit:  [&#x27;The maximum number of volumes to return from the API.&#x27;]
        :type limit: 
        
        :param virtualVolumeIDs:  [&#x27;List of Virtual Volume IDs to get.&#x27;]
        :type virtualVolumeIDs: 
        
        :param callingVirtualVolumeHostID:  
        :type callingVirtualVolumeHostID: 
        """

        params = { 
        }
        if startVirtualVolumeID is not None:
            params["startVirtualVolumeID"] = startVirtualVolumeID
        if limit is not None:
            params["limit"] = limit
        if virtualVolumeIDs is not None:
            params["virtualVolumeIDs"] = virtualVolumeIDs
        if callingVirtualVolumeHostID is not None:
            params["callingVirtualVolumeHostID"] = callingVirtualVolumeHostID
        
        # There is no adaptor.
        return self.send_request(
            'ListVirtualVolumes',
            ListVirtualVolumesResult,
            params
        )

    def modify_virtual_volume(
            self,
            virtualVolumeID,
            qos=OPTIONAL,
            totalSize=OPTIONAL,
            callingVirtualVolumeHostID=OPTIONAL,):
        """
        [&#x27;ModifyVirtualVolume is used to modify settings on an existing virtual volume.&#x27;]
        :param virtualVolumeID: [required] VvolVolumeID for the volume to be modified.
        :type virtualVolumeID: 
        
        :param qos:  New quality of service settings for this volume.
        :type qos: 
        
        :param totalSize:  [&#x27;New size of the volume in bytes.&#x27;, &#x27;Size is rounded up to the nearest 1MiB size.&#x27;, &#x27;This parameter can only be used to *increase* the size of a volume.&#x27;][&#x27;New size of the volume in bytes.&#x27;, &#x27;Size is rounded up to the nearest 1MiB size.&#x27;, &#x27;This parameter can only be used to *increase* the size of a volume.&#x27;][&#x27;New size of the volume in bytes.&#x27;, &#x27;Size is rounded up to the nearest 1MiB size.&#x27;, &#x27;This parameter can only be used to *increase* the size of a volume.&#x27;]
        :type totalSize: 
        
        :param callingVirtualVolumeHostID:  
        :type callingVirtualVolumeHostID: 
        """

        params = { 
            "virtualVolumeID": virtualVolumeID,
        }
        if qos is not None:
            params["qos"] = qos
        if totalSize is not None:
            params["totalSize"] = totalSize
        if callingVirtualVolumeHostID is not None:
            params["callingVirtualVolumeHostID"] = callingVirtualVolumeHostID
        
        # There is no adaptor.
        return self.send_request(
            'ModifyVirtualVolume',
            VirtualVolumeNullResult,
            params,
            since=9.0
        )

    def modify_virtual_volume_metadata(
            self,
            virtualVolumeID,
            metadata,
            removeKeys,
            callingVirtualVolumeHostID=OPTIONAL,):
        """
        [&#x27;ModifyVirtualVolumeMetadata is used to selectively modify the VVol metadata.&#x27;]
        :param virtualVolumeID: [required] VvolVolumeID for the volume to be modified.
        :type virtualVolumeID: 
        
        :param metadata: [required] 
        :type metadata: 
        
        :param removeKeys: [required] 
        :type removeKeys: 
        
        :param callingVirtualVolumeHostID:  
        :type callingVirtualVolumeHostID: 
        """

        params = { 
            "virtualVolumeID": virtualVolumeID,
            "metadata": metadata,
            "removeKeys": removeKeys,
        }
        if callingVirtualVolumeHostID is not None:
            params["callingVirtualVolumeHostID"] = callingVirtualVolumeHostID
        
        # There is no adaptor.
        return self.send_request(
            'ModifyVirtualVolumeMetadata',
            VirtualVolumeNullResult,
            params,
            since=9.0
        )

    def query_virtual_volume_metadata(
            self,
            queryConstraints=OPTIONAL,
            wildcardConstraints=OPTIONAL,
            callingVirtualVolumeHostID=OPTIONAL,):
        """
        [&#x27;QueryVirtualVolumeMetadata returns a list of VVols matching a metadata query.&#x27;]
        :param queryConstraints:  
        :type queryConstraints: 
        
        :param wildcardConstraints:  
        :type wildcardConstraints: 
        
        :param callingVirtualVolumeHostID:  
        :type callingVirtualVolumeHostID: 
        """

        params = { 
        }
        if queryConstraints is not None:
            params["queryConstraints"] = queryConstraints
        if wildcardConstraints is not None:
            params["wildcardConstraints"] = wildcardConstraints
        if callingVirtualVolumeHostID is not None:
            params["callingVirtualVolumeHostID"] = callingVirtualVolumeHostID
        
        # There is no adaptor.
        return self.send_request(
            'QueryVirtualVolumeMetadata',
            QueryVirtualVolumeMetadataResult,
            params,
            since=9.0
        )

    def clone_virtual_volume(
            self,
            virtualVolumeID,
            name=OPTIONAL,
            qos=OPTIONAL,
            metadata=OPTIONAL,
            newContainerID=OPTIONAL,
            callingVirtualVolumeHostID=OPTIONAL,):
        """
        [&#x27;CloneVirtualVolume is used to execute a VMware Virtual Volume clone.&#x27;]
        :param virtualVolumeID: [required] The ID of the Virtual Volume to clone.
        :type virtualVolumeID: 
        
        :param name:  The name for the newly-created volume.
        :type name: 
        
        :param qos:  New quality of service settings for this volume.
        :type qos: 
        
        :param metadata:  
        :type metadata: 
        
        :param newContainerID:  
        :type newContainerID: 
        
        :param callingVirtualVolumeHostID:  
        :type callingVirtualVolumeHostID: 
        """

        params = { 
            "virtualVolumeID": virtualVolumeID,
        }
        if name is not None:
            params["name"] = name
        if qos is not None:
            params["qos"] = qos
        if metadata is not None:
            params["metadata"] = metadata
        if newContainerID is not None:
            params["newContainerID"] = newContainerID
        if callingVirtualVolumeHostID is not None:
            params["callingVirtualVolumeHostID"] = callingVirtualVolumeHostID
        
        # There is no adaptor.
        return self.send_request(
            'CloneVirtualVolume',
            VirtualVolumeAsyncResult,
            params,
            since=9.0
        )

    def fast_clone_virtual_volume(
            self,
            virtualVolumeID,
            name=OPTIONAL,
            qos=OPTIONAL,
            metadata=OPTIONAL,
            callingVirtualVolumeHostID=OPTIONAL,):
        """
        [&#x27;FastCloneVirtualVolume is used to execute a VMware Virtual Volume fast clone.&#x27;]
        :param virtualVolumeID: [required] The ID of the Virtual Volume to clone.
        :type virtualVolumeID: 
        
        :param name:  The name for the newly-created volume.
        :type name: 
        
        :param qos:  New quality of service settings for this volume.
        :type qos: 
        
        :param metadata:  
        :type metadata: 
        
        :param callingVirtualVolumeHostID:  
        :type callingVirtualVolumeHostID: 
        """

        params = { 
            "virtualVolumeID": virtualVolumeID,
        }
        if name is not None:
            params["name"] = name
        if qos is not None:
            params["qos"] = qos
        if metadata is not None:
            params["metadata"] = metadata
        if callingVirtualVolumeHostID is not None:
            params["callingVirtualVolumeHostID"] = callingVirtualVolumeHostID
        
        # There is no adaptor.
        return self.send_request(
            'FastCloneVirtualVolume',
            VirtualVolumeAsyncResult,
            params,
            since=9.0
        )

    def prepare_virtual_snapshot(
            self,
            virtualVolumeID,
            name=OPTIONAL,
            writableSnapshot=OPTIONAL,
            callingVirtualVolumeHostID=OPTIONAL,):
        """
        [&#x27;PrepareVirtualSnapshot is used to set up VMware Virtual Volume snapshot.&#x27;]
        :param virtualVolumeID: [required] The ID of the Virtual Volume to clone.
        :type virtualVolumeID: 
        
        :param name:  The name for the newly-created volume.
        :type name: 
        
        :param writableSnapshot:  Will the snapshot be writable?
        :type writableSnapshot: 
        
        :param callingVirtualVolumeHostID:  
        :type callingVirtualVolumeHostID: 
        """

        params = { 
            "virtualVolumeID": virtualVolumeID,
        }
        if name is not None:
            params["name"] = name
        if writableSnapshot is not None:
            params["writableSnapshot"] = writableSnapshot
        if callingVirtualVolumeHostID is not None:
            params["callingVirtualVolumeHostID"] = callingVirtualVolumeHostID
        
        # There is no adaptor.
        return self.send_request(
            'PrepareVirtualSnapshot',
            PrepareVirtualSnapshotResult,
            params,
            since=9.0
        )

    def snapshot_virtual_volume(
            self,
            virtualVolumeID,
            timeout,
            metadata=OPTIONAL,
            callingVirtualVolumeHostID=OPTIONAL,):
        """
        [&#x27;SnapshotVirtualVolume is used to take a VMware Virtual Volume snapshot.&#x27;]
        :param virtualVolumeID: [required] The ID of the Virtual Volume to clone.
        :type virtualVolumeID: 
        
        :param timeout: [required] Number of seconds to complete or fail.
        :type timeout: 
        
        :param metadata:  
        :type metadata: 
        
        :param callingVirtualVolumeHostID:  
        :type callingVirtualVolumeHostID: 
        """

        params = { 
            "virtualVolumeID": virtualVolumeID,
            "timeout": timeout,
        }
        if metadata is not None:
            params["metadata"] = metadata
        if callingVirtualVolumeHostID is not None:
            params["callingVirtualVolumeHostID"] = callingVirtualVolumeHostID
        
        # There is no adaptor.
        return self.send_request(
            'SnapshotVirtualVolume',
            SnapshotVirtualVolumeResult,
            params,
            since=9.0
        )

    def rollback_virtual_volume(
            self,
            srcVirtualVolumeID,
            dstVirtualVolumeID,
            callingVirtualVolumeHostID=OPTIONAL,):
        """
        [&#x27;RollbackVirtualVolume is used to restore a VMware Virtual Volume snapshot.&#x27;]
        :param srcVirtualVolumeID: [required] The ID of the Virtual Volume snapshot.
        :type srcVirtualVolumeID: 
        
        :param dstVirtualVolumeID: [required] The ID of the Virtual Volume to restore to.
        :type dstVirtualVolumeID: 
        
        :param callingVirtualVolumeHostID:  
        :type callingVirtualVolumeHostID: 
        """

        params = { 
            "srcVirtualVolumeID": srcVirtualVolumeID,
            "dstVirtualVolumeID": dstVirtualVolumeID,
        }
        if callingVirtualVolumeHostID is not None:
            params["callingVirtualVolumeHostID"] = callingVirtualVolumeHostID
        
        # There is no adaptor.
        return self.send_request(
            'RollbackVirtualVolume',
            VirtualVolumeAsyncResult,
            params,
            since=9.0
        )

    def get_virtual_volume_allocated_bitmap(
            self,
            virtualVolumeID,
            segmentStart,
            segmentLength,
            chunkSize,
            callingVirtualVolumeHostID=OPTIONAL,):
        """
        [&#x27;GetVirtualVolumeAllocatedBitmap returns a b64-encoded block of data &#x27;, &#x27;representing a bitmap where non-zero bits indicate the allocation of a &#x27;, &#x27;segment (LBA range) of the volume.&#x27;]
        [&#x27;GetVirtualVolumeAllocatedBitmap returns a b64-encoded block of data &#x27;, &#x27;representing a bitmap where non-zero bits indicate the allocation of a &#x27;, &#x27;segment (LBA range) of the volume.&#x27;]
        [&#x27;GetVirtualVolumeAllocatedBitmap returns a b64-encoded block of data &#x27;, &#x27;representing a bitmap where non-zero bits indicate the allocation of a &#x27;, &#x27;segment (LBA range) of the volume.&#x27;]
        :param virtualVolumeID: [required] The ID of the Virtual Volume.
        :type virtualVolumeID: 
        
        :param segmentStart: [required] Byte offset.
        :type segmentStart: 
        
        :param segmentLength: [required] Byte length adjusted to end on a chunk boundary.
        :type segmentLength: 
        
        :param chunkSize: [required] Number of bytes represented by one bit in the bitmap.
        :type chunkSize: 
        
        :param callingVirtualVolumeHostID:  
        :type callingVirtualVolumeHostID: 
        """

        params = { 
            "virtualVolumeID": virtualVolumeID,
            "segmentStart": segmentStart,
            "segmentLength": segmentLength,
            "chunkSize": chunkSize,
        }
        if callingVirtualVolumeHostID is not None:
            params["callingVirtualVolumeHostID"] = callingVirtualVolumeHostID
        
        # There is no adaptor.
        return self.send_request(
            'GetVirtualVolumeAllocatedBitmap',
            VirtualVolumeBitmapResult,
            params,
            since=9.0
        )

    def get_virtual_volume_unshared_bitmap(
            self,
            virtualVolumeID,
            baseVirtualVolumeID,
            segmentStart,
            segmentLength,
            chunkSize,
            callingVirtualVolumeHostID=OPTIONAL,):
        """
        [&#x27;GetVirtualVolumeAllocatedBitmap returns a b64-encoded block of data &#x27;, &#x27;representing a bitmap where non-zero bits indicate that data is not the same &#x27;, &#x27;between two volumes for a common segment (LBA range) of the volumes.&#x27;]
        [&#x27;GetVirtualVolumeAllocatedBitmap returns a b64-encoded block of data &#x27;, &#x27;representing a bitmap where non-zero bits indicate that data is not the same &#x27;, &#x27;between two volumes for a common segment (LBA range) of the volumes.&#x27;]
        [&#x27;GetVirtualVolumeAllocatedBitmap returns a b64-encoded block of data &#x27;, &#x27;representing a bitmap where non-zero bits indicate that data is not the same &#x27;, &#x27;between two volumes for a common segment (LBA range) of the volumes.&#x27;]
        :param virtualVolumeID: [required] The ID of the Virtual Volume.
        :type virtualVolumeID: 
        
        :param baseVirtualVolumeID: [required] The ID of the Virtual Volume to compare against.
        :type baseVirtualVolumeID: 
        
        :param segmentStart: [required] Byte offset.
        :type segmentStart: 
        
        :param segmentLength: [required] Byte length adjusted to end on a chunk boundary.
        :type segmentLength: 
        
        :param chunkSize: [required] Number of bytes represented by one bit in the bitmap.
        :type chunkSize: 
        
        :param callingVirtualVolumeHostID:  
        :type callingVirtualVolumeHostID: 
        """

        params = { 
            "virtualVolumeID": virtualVolumeID,
            "baseVirtualVolumeID": baseVirtualVolumeID,
            "segmentStart": segmentStart,
            "segmentLength": segmentLength,
            "chunkSize": chunkSize,
        }
        if callingVirtualVolumeHostID is not None:
            params["callingVirtualVolumeHostID"] = callingVirtualVolumeHostID
        
        # There is no adaptor.
        return self.send_request(
            'GetVirtualVolumeUnsharedBitmap',
            VirtualVolumeBitmapResult,
            params,
            since=9.0
        )

    def get_virtual_volume_unshared_chunks(
            self,
            virtualVolumeID,
            baseVirtualVolumeID,
            segmentStart,
            segmentLength,
            chunkSize,
            callingVirtualVolumeHostID=OPTIONAL,):
        """
        [&#x27;GetVirtualVolumeAllocatedBitmap scans a VVol segment and returns the number of &#x27;, &#x27;chunks not shared between two volumes. This call will return results in less &#x27;, &#x27;than 30 seconds. If the specified VVol and the base VVil are not related, an &#x27;, &#x27;error is thrown. If the offset/length combination is invalid or out fo range &#x27;, &#x27;an error is thrown.&#x27;]
        [&#x27;GetVirtualVolumeAllocatedBitmap scans a VVol segment and returns the number of &#x27;, &#x27;chunks not shared between two volumes. This call will return results in less &#x27;, &#x27;than 30 seconds. If the specified VVol and the base VVil are not related, an &#x27;, &#x27;error is thrown. If the offset/length combination is invalid or out fo range &#x27;, &#x27;an error is thrown.&#x27;]
        [&#x27;GetVirtualVolumeAllocatedBitmap scans a VVol segment and returns the number of &#x27;, &#x27;chunks not shared between two volumes. This call will return results in less &#x27;, &#x27;than 30 seconds. If the specified VVol and the base VVil are not related, an &#x27;, &#x27;error is thrown. If the offset/length combination is invalid or out fo range &#x27;, &#x27;an error is thrown.&#x27;]
        [&#x27;GetVirtualVolumeAllocatedBitmap scans a VVol segment and returns the number of &#x27;, &#x27;chunks not shared between two volumes. This call will return results in less &#x27;, &#x27;than 30 seconds. If the specified VVol and the base VVil are not related, an &#x27;, &#x27;error is thrown. If the offset/length combination is invalid or out fo range &#x27;, &#x27;an error is thrown.&#x27;]
        [&#x27;GetVirtualVolumeAllocatedBitmap scans a VVol segment and returns the number of &#x27;, &#x27;chunks not shared between two volumes. This call will return results in less &#x27;, &#x27;than 30 seconds. If the specified VVol and the base VVil are not related, an &#x27;, &#x27;error is thrown. If the offset/length combination is invalid or out fo range &#x27;, &#x27;an error is thrown.&#x27;]
        :param virtualVolumeID: [required] The ID of the Virtual Volume.
        :type virtualVolumeID: 
        
        :param baseVirtualVolumeID: [required] The ID of the Virtual Volume to compare against.
        :type baseVirtualVolumeID: 
        
        :param segmentStart: [required] Start Byte offset.
        :type segmentStart: 
        
        :param segmentLength: [required] Length of the scan segment in bytes.
        :type segmentLength: 
        
        :param chunkSize: [required] Number of bytes represented by one bit in the bitmap.
        :type chunkSize: 
        
        :param callingVirtualVolumeHostID:  
        :type callingVirtualVolumeHostID: 
        """

        params = { 
            "virtualVolumeID": virtualVolumeID,
            "baseVirtualVolumeID": baseVirtualVolumeID,
            "segmentStart": segmentStart,
            "segmentLength": segmentLength,
            "chunkSize": chunkSize,
        }
        if callingVirtualVolumeHostID is not None:
            params["callingVirtualVolumeHostID"] = callingVirtualVolumeHostID
        
        # There is no adaptor.
        return self.send_request(
            'GetVirtualVolumeUnsharedChunks',
            VirtualVolumeUnsharedChunkResult,
            params,
            since=9.0
        )

    def copy_diffs_to_virtual_volume(
            self,
            virtualVolumeID,
            baseVirtualVolumeID,
            dstVirtualVolumeID,
            callingVirtualVolumeHostID=OPTIONAL,):
        """
        [&#x27;CopyDiffsToVirtualVolume is a three-way merge function.&#x27;]
        :param virtualVolumeID: [required] The ID of the snapshot Virtual Volume.
        :type virtualVolumeID: 
        
        :param baseVirtualVolumeID: [required] The ID of the base Virtual Volume.
        :type baseVirtualVolumeID: 
        
        :param dstVirtualVolumeID: [required] The ID of the Virtual Volume to be overwritten.
        :type dstVirtualVolumeID: 
        
        :param callingVirtualVolumeHostID:  
        :type callingVirtualVolumeHostID: 
        """

        params = { 
            "virtualVolumeID": virtualVolumeID,
            "baseVirtualVolumeID": baseVirtualVolumeID,
            "dstVirtualVolumeID": dstVirtualVolumeID,
        }
        if callingVirtualVolumeHostID is not None:
            params["callingVirtualVolumeHostID"] = callingVirtualVolumeHostID
        
        # There is no adaptor.
        return self.send_request(
            'CopyDiffsToVirtualVolume',
            VirtualVolumeAsyncResult,
            params,
            since=9.0
        )

    def create_virtual_volume_host(
            self,
            virtualVolumeHostID,
            clusterID,
            initiatorNames=OPTIONAL,
            visibleProtocolEndpointIDs=OPTIONAL,
            hostAddress=OPTIONAL,
            callingVirtualVolumeHostID=OPTIONAL,):
        """
        [&#x27;CreateVirtualVolumeHost creates a new ESX host.&#x27;]
        :param virtualVolumeHostID: [required] The GUID of the ESX host.
        :type virtualVolumeHostID: 
        
        :param clusterID: [required] The GUID of the ESX Cluster.
        :type clusterID: 
        
        :param initiatorNames:  
        :type initiatorNames: 
        
        :param visibleProtocolEndpointIDs:  A list of PEs the host is aware of.
        :type visibleProtocolEndpointIDs: 
        
        :param hostAddress:  IP or DNS name for the host.
        :type hostAddress: 
        
        :param callingVirtualVolumeHostID:  
        :type callingVirtualVolumeHostID: 
        """

        params = { 
            "virtualVolumeHostID": virtualVolumeHostID,
            "clusterID": clusterID,
        }
        if initiatorNames is not None:
            params["initiatorNames"] = initiatorNames
        if visibleProtocolEndpointIDs is not None:
            params["visibleProtocolEndpointIDs"] = visibleProtocolEndpointIDs
        if hostAddress is not None:
            params["hostAddress"] = hostAddress
        if callingVirtualVolumeHostID is not None:
            params["callingVirtualVolumeHostID"] = callingVirtualVolumeHostID
        
        # There is no adaptor.
        return self.send_request(
            'CreateVirtualVolumeHost',
            VirtualVolumeNullResult,
            params,
            since=9.0
        )

    def list_virtual_volume_hosts(
            self,
            virtualVolumeHostIDs=OPTIONAL,
            callingVirtualVolumeHostID=OPTIONAL,):
        """
        [&#x27;ListVirtualVolumeHosts returns a list of known ESX hosts.&#x27;]
        :param virtualVolumeHostIDs:  
        :type virtualVolumeHostIDs: 
        
        :param callingVirtualVolumeHostID:  
        :type callingVirtualVolumeHostID: 
        """

        params = { 
        }
        if virtualVolumeHostIDs is not None:
            params["virtualVolumeHostIDs"] = virtualVolumeHostIDs
        if callingVirtualVolumeHostID is not None:
            params["callingVirtualVolumeHostID"] = callingVirtualVolumeHostID
        
        # There is no adaptor.
        return self.send_request(
            'ListVirtualVolumeHosts',
            ListVirtualVolumeHostsResult,
            params,
            since=9.0
        )

    def modify_virtual_volume_host(
            self,
            virtualVolumeHostID,
            clusterID=OPTIONAL,
            visibleProtocolEndpointIDs=OPTIONAL,
            initiatorNames=OPTIONAL,
            hostAddress=OPTIONAL,
            callingVirtualVolumeHostID=OPTIONAL,):
        """
        [&#x27;ModifyVirtualVolumeHost changes an existing ESX host.&#x27;]
        :param virtualVolumeHostID: [required] The GUID of the ESX host.
        :type virtualVolumeHostID: 
        
        :param clusterID:  The GUID of the ESX Cluster.
        :type clusterID: 
        
        :param visibleProtocolEndpointIDs:  A list of PEs the host is aware of.
        :type visibleProtocolEndpointIDs: 
        
        :param initiatorNames:  List of iSCSI initiator IQNs for the host.
        :type initiatorNames: 
        
        :param hostAddress:  IP or DNS name for the host.
        :type hostAddress: 
        
        :param callingVirtualVolumeHostID:  
        :type callingVirtualVolumeHostID: 
        """

        params = { 
            "virtualVolumeHostID": virtualVolumeHostID,
        }
        if clusterID is not None:
            params["clusterID"] = clusterID
        if visibleProtocolEndpointIDs is not None:
            params["visibleProtocolEndpointIDs"] = visibleProtocolEndpointIDs
        if initiatorNames is not None:
            params["initiatorNames"] = initiatorNames
        if hostAddress is not None:
            params["hostAddress"] = hostAddress
        if callingVirtualVolumeHostID is not None:
            params["callingVirtualVolumeHostID"] = callingVirtualVolumeHostID
        
        # There is no adaptor.
        return self.send_request(
            'ModifyVirtualVolumeHost',
            VirtualVolumeNullResult,
            params
        )

    def get_virtual_volume_task_update(
            self,
            virtualVolumeTaskID,
            callingVirtualVolumeHostID=OPTIONAL,):
        """
        [&#x27;GetVirtualVolumeTaskUpdate checks the status of a VVol Async Task.&#x27;]
        :param virtualVolumeTaskID: [required] The UUID of the VVol Task.
        :type virtualVolumeTaskID: 
        
        :param callingVirtualVolumeHostID:  
        :type callingVirtualVolumeHostID: 
        """

        params = { 
            "virtualVolumeTaskID": virtualVolumeTaskID,
        }
        if callingVirtualVolumeHostID is not None:
            params["callingVirtualVolumeHostID"] = callingVirtualVolumeHostID
        
        # There is no adaptor.
        return self.send_request(
            'GetVirtualVolumeTaskUpdate',
            VirtualVolumeTaskResult,
            params,
            since=9.0
        )

    def list_virtual_volume_tasks(
            self,
            virtualVolumeTaskIDs=OPTIONAL,
            callingVirtualVolumeHostID=OPTIONAL,):
        """
        [&#x27;ListVirtualVolumeTasks returns a list of VVol Async Tasks.&#x27;]
        :param virtualVolumeTaskIDs:  
        :type virtualVolumeTaskIDs: 
        
        :param callingVirtualVolumeHostID:  
        :type callingVirtualVolumeHostID: 
        """

        params = { 
        }
        if virtualVolumeTaskIDs is not None:
            params["virtualVolumeTaskIDs"] = virtualVolumeTaskIDs
        if callingVirtualVolumeHostID is not None:
            params["callingVirtualVolumeHostID"] = callingVirtualVolumeHostID
        
        # There is no adaptor.
        return self.send_request(
            'ListVirtualVolumeTasks',
            ListVirtualVolumeTasksResult,
            params,
            since=9.0
        )

    def cancel_virtual_volume_task(
            self,
            virtualVolumeTaskID,
            callingVirtualVolumeHostID=OPTIONAL,):
        """
        [&#x27;CancelVirtualVolumeTask attempts to cancel the VVol Async Task.&#x27;]
        :param virtualVolumeTaskID: [required] The UUID of the VVol Task to cancel.
        :type virtualVolumeTaskID: 
        
        :param callingVirtualVolumeHostID:  
        :type callingVirtualVolumeHostID: 
        """

        params = { 
            "virtualVolumeTaskID": virtualVolumeTaskID,
        }
        if callingVirtualVolumeHostID is not None:
            params["callingVirtualVolumeHostID"] = callingVirtualVolumeHostID
        
        # There is no adaptor.
        return self.send_request(
            'CancelVirtualVolumeTask',
            VirtualVolumeNullResult,
            params,
            since=9.0
        )

    def bind_virtual_volumes(
            self,
            virtualVolumeIDs,
            virtualVolumeHostID,
            bindContext,):
        """
        [&#x27;BindVirtualVolume binds a VVol with a Host.&#x27;]
        :param virtualVolumeIDs: [required] The UUID of the VVol to bind.
        :type virtualVolumeIDs: 
        
        :param virtualVolumeHostID: [required] The UUID of the ESX host.
        :type virtualVolumeHostID: 
        
        :param bindContext: [required] Normal or Start?
        :type bindContext: 
        """

        params = { 
            "virtualVolumeIDs": virtualVolumeIDs,
            "virtualVolumeHostID": virtualVolumeHostID,
            "bindContext": bindContext,
        }
        
        # There is no adaptor.
        return self.send_request(
            'BindVirtualVolumes',
            ListVirtualVolumeBindingsResult,
            params
        )

    def list_virtual_volume_bindings(
            self,
            virtualVolumeBindingIDs=OPTIONAL,
            callingVirtualVolumeHostID=OPTIONAL,):
        """
        [&#x27;ListVirtualVolumeBindings returns a list of VVol bindings.&#x27;]
        :param virtualVolumeBindingIDs:  
        :type virtualVolumeBindingIDs: 
        
        :param callingVirtualVolumeHostID:  
        :type callingVirtualVolumeHostID: 
        """

        params = { 
        }
        if virtualVolumeBindingIDs is not None:
            params["virtualVolumeBindingIDs"] = virtualVolumeBindingIDs
        if callingVirtualVolumeHostID is not None:
            params["callingVirtualVolumeHostID"] = callingVirtualVolumeHostID
        
        # There is no adaptor.
        return self.send_request(
            'ListVirtualVolumeBindings',
            ListVirtualVolumeBindingsResult,
            params,
            since=9.0
        )

    def unbind_virtual_volumes(
            self,
            unbindContext,
            virtualVolumeHostID,
            unbindArgs,):
        """
        [&#x27;UnbindGetVirtualVolume removes the VVol &lt;-&gt; Host binding.&#x27;]
        :param unbindContext: [required] Normal, Start, or End?
        :type unbindContext: 
        
        :param virtualVolumeHostID: [required] 
        :type virtualVolumeHostID: 
        
        :param unbindArgs: [required] 
        :type unbindArgs: 
        """

        params = { 
            "unbindContext": unbindContext,
            "virtualVolumeHostID": virtualVolumeHostID,
            "unbindArgs": unbindArgs,
        }
        
        # There is no adaptor.
        return self.send_request(
            'UnbindVirtualVolumes',
            VirtualVolumeUnbindResult,
            params
        )

    def modify_vasa_provider_info(
            self,
            keystore=OPTIONAL,
            vasaProviderID=OPTIONAL,
            options=OPTIONAL,):
        """
        [&#x27;Update the Vasa Provider info&#x27;]
        :param keystore:  Signed SSL certificate for the Vasa Provider
        :type keystore: 
        
        :param vasaProviderID:  UUID identifying the vasa provider
        :type vasaProviderID: 
        
        :param options:  
        :type options: 
        """

        params = { 
        }
        if keystore is not None:
            params["keystore"] = keystore
        if vasaProviderID is not None:
            params["vasaProviderID"] = vasaProviderID
        if options is not None:
            params["options"] = options
        
        # There is no adaptor.
        return self.send_request(
            'ModifyVasaProviderInfo',
            VirtualVolumeNullResult,
            params,
            since=9.0
        )

    def get_vasa_provider_info(
            self,):
        """
        [&#x27;Gets the Vasa Provider info&#x27;]"""

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'GetVasaProviderInfo',
            VasaProviderInfoResult,
            params,
            since=9.0
        )

    def get_virtual_volume_count(
            self,):
        """
        [&#x27;Enables retrieval of the number of virtual volumes currently in the system.&#x27;]"""

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
            volumeID,
            name,
            newAccountID=OPTIONAL,
            newSize=OPTIONAL,
            access=OPTIONAL,
            snapshotID=OPTIONAL,
            attributes=OPTIONAL,):
        """
        [&#x27;CloneVolume is used to create a copy of the volume.&#x27;, &#x27;This method is asynchronous and may take a variable amount of time to complete.&#x27;, &#x27;The cloning process begins immediately when the CloneVolume request is made and is representative of the state of the volume when the API method is issued.&#x27;, &#x27;GetAsyncResults can be used to determine when the cloning process is complete and the new volume is available for connections.&#x27;, &#x27;ListSyncJobs can be used to see the progress of creating the clone.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Note&lt;/b&gt;: The initial attributes and quality of service settings for the volume are inherited from the volume being cloned.&#x27;, &#x27;If different settings are required, they can be changed via ModifyVolume.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Note&lt;/b&gt;: Cloned volumes do not inherit volume access group memberships from the source volume.&#x27;]
        [&#x27;CloneVolume is used to create a copy of the volume.&#x27;, &#x27;This method is asynchronous and may take a variable amount of time to complete.&#x27;, &#x27;The cloning process begins immediately when the CloneVolume request is made and is representative of the state of the volume when the API method is issued.&#x27;, &#x27;GetAsyncResults can be used to determine when the cloning process is complete and the new volume is available for connections.&#x27;, &#x27;ListSyncJobs can be used to see the progress of creating the clone.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Note&lt;/b&gt;: The initial attributes and quality of service settings for the volume are inherited from the volume being cloned.&#x27;, &#x27;If different settings are required, they can be changed via ModifyVolume.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Note&lt;/b&gt;: Cloned volumes do not inherit volume access group memberships from the source volume.&#x27;]
        [&#x27;CloneVolume is used to create a copy of the volume.&#x27;, &#x27;This method is asynchronous and may take a variable amount of time to complete.&#x27;, &#x27;The cloning process begins immediately when the CloneVolume request is made and is representative of the state of the volume when the API method is issued.&#x27;, &#x27;GetAsyncResults can be used to determine when the cloning process is complete and the new volume is available for connections.&#x27;, &#x27;ListSyncJobs can be used to see the progress of creating the clone.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Note&lt;/b&gt;: The initial attributes and quality of service settings for the volume are inherited from the volume being cloned.&#x27;, &#x27;If different settings are required, they can be changed via ModifyVolume.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Note&lt;/b&gt;: Cloned volumes do not inherit volume access group memberships from the source volume.&#x27;]
        [&#x27;CloneVolume is used to create a copy of the volume.&#x27;, &#x27;This method is asynchronous and may take a variable amount of time to complete.&#x27;, &#x27;The cloning process begins immediately when the CloneVolume request is made and is representative of the state of the volume when the API method is issued.&#x27;, &#x27;GetAsyncResults can be used to determine when the cloning process is complete and the new volume is available for connections.&#x27;, &#x27;ListSyncJobs can be used to see the progress of creating the clone.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Note&lt;/b&gt;: The initial attributes and quality of service settings for the volume are inherited from the volume being cloned.&#x27;, &#x27;If different settings are required, they can be changed via ModifyVolume.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Note&lt;/b&gt;: Cloned volumes do not inherit volume access group memberships from the source volume.&#x27;]
        [&#x27;CloneVolume is used to create a copy of the volume.&#x27;, &#x27;This method is asynchronous and may take a variable amount of time to complete.&#x27;, &#x27;The cloning process begins immediately when the CloneVolume request is made and is representative of the state of the volume when the API method is issued.&#x27;, &#x27;GetAsyncResults can be used to determine when the cloning process is complete and the new volume is available for connections.&#x27;, &#x27;ListSyncJobs can be used to see the progress of creating the clone.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Note&lt;/b&gt;: The initial attributes and quality of service settings for the volume are inherited from the volume being cloned.&#x27;, &#x27;If different settings are required, they can be changed via ModifyVolume.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Note&lt;/b&gt;: Cloned volumes do not inherit volume access group memberships from the source volume.&#x27;]
        [&#x27;CloneVolume is used to create a copy of the volume.&#x27;, &#x27;This method is asynchronous and may take a variable amount of time to complete.&#x27;, &#x27;The cloning process begins immediately when the CloneVolume request is made and is representative of the state of the volume when the API method is issued.&#x27;, &#x27;GetAsyncResults can be used to determine when the cloning process is complete and the new volume is available for connections.&#x27;, &#x27;ListSyncJobs can be used to see the progress of creating the clone.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Note&lt;/b&gt;: The initial attributes and quality of service settings for the volume are inherited from the volume being cloned.&#x27;, &#x27;If different settings are required, they can be changed via ModifyVolume.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Note&lt;/b&gt;: Cloned volumes do not inherit volume access group memberships from the source volume.&#x27;]
        [&#x27;CloneVolume is used to create a copy of the volume.&#x27;, &#x27;This method is asynchronous and may take a variable amount of time to complete.&#x27;, &#x27;The cloning process begins immediately when the CloneVolume request is made and is representative of the state of the volume when the API method is issued.&#x27;, &#x27;GetAsyncResults can be used to determine when the cloning process is complete and the new volume is available for connections.&#x27;, &#x27;ListSyncJobs can be used to see the progress of creating the clone.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Note&lt;/b&gt;: The initial attributes and quality of service settings for the volume are inherited from the volume being cloned.&#x27;, &#x27;If different settings are required, they can be changed via ModifyVolume.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Note&lt;/b&gt;: Cloned volumes do not inherit volume access group memberships from the source volume.&#x27;]
        [&#x27;CloneVolume is used to create a copy of the volume.&#x27;, &#x27;This method is asynchronous and may take a variable amount of time to complete.&#x27;, &#x27;The cloning process begins immediately when the CloneVolume request is made and is representative of the state of the volume when the API method is issued.&#x27;, &#x27;GetAsyncResults can be used to determine when the cloning process is complete and the new volume is available for connections.&#x27;, &#x27;ListSyncJobs can be used to see the progress of creating the clone.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Note&lt;/b&gt;: The initial attributes and quality of service settings for the volume are inherited from the volume being cloned.&#x27;, &#x27;If different settings are required, they can be changed via ModifyVolume.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Note&lt;/b&gt;: Cloned volumes do not inherit volume access group memberships from the source volume.&#x27;]
        [&#x27;CloneVolume is used to create a copy of the volume.&#x27;, &#x27;This method is asynchronous and may take a variable amount of time to complete.&#x27;, &#x27;The cloning process begins immediately when the CloneVolume request is made and is representative of the state of the volume when the API method is issued.&#x27;, &#x27;GetAsyncResults can be used to determine when the cloning process is complete and the new volume is available for connections.&#x27;, &#x27;ListSyncJobs can be used to see the progress of creating the clone.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Note&lt;/b&gt;: The initial attributes and quality of service settings for the volume are inherited from the volume being cloned.&#x27;, &#x27;If different settings are required, they can be changed via ModifyVolume.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Note&lt;/b&gt;: Cloned volumes do not inherit volume access group memberships from the source volume.&#x27;]
        [&#x27;CloneVolume is used to create a copy of the volume.&#x27;, &#x27;This method is asynchronous and may take a variable amount of time to complete.&#x27;, &#x27;The cloning process begins immediately when the CloneVolume request is made and is representative of the state of the volume when the API method is issued.&#x27;, &#x27;GetAsyncResults can be used to determine when the cloning process is complete and the new volume is available for connections.&#x27;, &#x27;ListSyncJobs can be used to see the progress of creating the clone.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Note&lt;/b&gt;: The initial attributes and quality of service settings for the volume are inherited from the volume being cloned.&#x27;, &#x27;If different settings are required, they can be changed via ModifyVolume.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Note&lt;/b&gt;: Cloned volumes do not inherit volume access group memberships from the source volume.&#x27;]
        :param volumeID: [required] The ID of the volume to clone.
        :type volumeID: 
        
        :param name: [required] The name for the newly-created volume.
        :type name: 
        
        :param newAccountID:  [&#x27;AccountID for the owner of the new volume.&#x27;, &#x27;If unspecified, the AccountID of the owner of the volume being cloned is used.&#x27;][&#x27;AccountID for the owner of the new volume.&#x27;, &#x27;If unspecified, the AccountID of the owner of the volume being cloned is used.&#x27;]
        :type newAccountID: 
        
        :param newSize:  [&#x27;New size of the volume, in bytes.&#x27;, &#x27;May be greater or less than the size of the volume being cloned.&#x27;, &quot;If unspecified, the clone&#x27;s volume size will be the same as the source volume.&quot;, &#x27;Size is rounded up to the nearest 1 MiB.&#x27;][&#x27;New size of the volume, in bytes.&#x27;, &#x27;May be greater or less than the size of the volume being cloned.&#x27;, &quot;If unspecified, the clone&#x27;s volume size will be the same as the source volume.&quot;, &#x27;Size is rounded up to the nearest 1 MiB.&#x27;][&#x27;New size of the volume, in bytes.&#x27;, &#x27;May be greater or less than the size of the volume being cloned.&#x27;, &quot;If unspecified, the clone&#x27;s volume size will be the same as the source volume.&quot;, &#x27;Size is rounded up to the nearest 1 MiB.&#x27;][&#x27;New size of the volume, in bytes.&#x27;, &#x27;May be greater or less than the size of the volume being cloned.&#x27;, &quot;If unspecified, the clone&#x27;s volume size will be the same as the source volume.&quot;, &#x27;Size is rounded up to the nearest 1 MiB.&#x27;]
        :type newSize: 
        
        :param access:  [&#x27;Access settings for the new volume.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;readOnly&lt;/b&gt;: Only read operations are allowed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;readWrite&lt;/b&gt;: Reads and writes are allowed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;locked&lt;/b&gt;: No reads or writes are allowed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;replicationTarget&lt;/b&gt;: Identify a volume as the target volume for a paired set of volumes. If the volume is not paired, the access status is locked.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;If unspecified, the access settings of the clone will be the same as the source.&#x27;][&#x27;Access settings for the new volume.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;readOnly&lt;/b&gt;: Only read operations are allowed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;readWrite&lt;/b&gt;: Reads and writes are allowed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;locked&lt;/b&gt;: No reads or writes are allowed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;replicationTarget&lt;/b&gt;: Identify a volume as the target volume for a paired set of volumes. If the volume is not paired, the access status is locked.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;If unspecified, the access settings of the clone will be the same as the source.&#x27;][&#x27;Access settings for the new volume.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;readOnly&lt;/b&gt;: Only read operations are allowed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;readWrite&lt;/b&gt;: Reads and writes are allowed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;locked&lt;/b&gt;: No reads or writes are allowed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;replicationTarget&lt;/b&gt;: Identify a volume as the target volume for a paired set of volumes. If the volume is not paired, the access status is locked.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;If unspecified, the access settings of the clone will be the same as the source.&#x27;][&#x27;Access settings for the new volume.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;readOnly&lt;/b&gt;: Only read operations are allowed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;readWrite&lt;/b&gt;: Reads and writes are allowed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;locked&lt;/b&gt;: No reads or writes are allowed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;replicationTarget&lt;/b&gt;: Identify a volume as the target volume for a paired set of volumes. If the volume is not paired, the access status is locked.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;If unspecified, the access settings of the clone will be the same as the source.&#x27;][&#x27;Access settings for the new volume.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;readOnly&lt;/b&gt;: Only read operations are allowed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;readWrite&lt;/b&gt;: Reads and writes are allowed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;locked&lt;/b&gt;: No reads or writes are allowed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;replicationTarget&lt;/b&gt;: Identify a volume as the target volume for a paired set of volumes. If the volume is not paired, the access status is locked.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;If unspecified, the access settings of the clone will be the same as the source.&#x27;][&#x27;Access settings for the new volume.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;readOnly&lt;/b&gt;: Only read operations are allowed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;readWrite&lt;/b&gt;: Reads and writes are allowed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;locked&lt;/b&gt;: No reads or writes are allowed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;replicationTarget&lt;/b&gt;: Identify a volume as the target volume for a paired set of volumes. If the volume is not paired, the access status is locked.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;If unspecified, the access settings of the clone will be the same as the source.&#x27;][&#x27;Access settings for the new volume.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;readOnly&lt;/b&gt;: Only read operations are allowed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;readWrite&lt;/b&gt;: Reads and writes are allowed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;locked&lt;/b&gt;: No reads or writes are allowed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;replicationTarget&lt;/b&gt;: Identify a volume as the target volume for a paired set of volumes. If the volume is not paired, the access status is locked.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;If unspecified, the access settings of the clone will be the same as the source.&#x27;]
        :type access: 
        
        :param snapshotID:  [&#x27;ID of the snapshot to use as the source of the clone.&#x27;, &#x27;If unspecified, the clone will be created with a snapshot of the active volume.&#x27;][&#x27;ID of the snapshot to use as the source of the clone.&#x27;, &#x27;If unspecified, the clone will be created with a snapshot of the active volume.&#x27;]
        :type snapshotID: 
        
        :param attributes:  List of Name/Value pairs in JSON object format.
        :type attributes: 
        """

        params = { 
            "volumeID": volumeID,
            "name": name,
        }
        if newAccountID is not None:
            params["newAccountID"] = newAccountID
        if newSize is not None:
            params["newSize"] = newSize
        if access is not None:
            params["access"] = access
        if snapshotID is not None:
            params["snapshotID"] = snapshotID
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
            groupSnapshotID=OPTIONAL,
            newAccountID=OPTIONAL,):
        """
        [&#x27;CloneMultipleVolumes is used to create a clone of a group of specified volumes. A consistent set of characteristics can be assigned to a group of multiple volume when they are cloned together.&#x27;, &#x27;If groupSnapshotID is going to be used to clone the volumes in a group snapshot, the group snapshot must be created first using the CreateGroupSnapshot API method or the SolidFire Element WebUI. Using groupSnapshotID is optional when cloning multiple volumes.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Note&lt;/b&gt;: Cloning multiple volumes is allowed if cluster fullness is at stage 2 or 3. Clones are not created when cluster fullness is at stage 4 or 5.&#x27;]
        [&#x27;CloneMultipleVolumes is used to create a clone of a group of specified volumes. A consistent set of characteristics can be assigned to a group of multiple volume when they are cloned together.&#x27;, &#x27;If groupSnapshotID is going to be used to clone the volumes in a group snapshot, the group snapshot must be created first using the CreateGroupSnapshot API method or the SolidFire Element WebUI. Using groupSnapshotID is optional when cloning multiple volumes.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Note&lt;/b&gt;: Cloning multiple volumes is allowed if cluster fullness is at stage 2 or 3. Clones are not created when cluster fullness is at stage 4 or 5.&#x27;]
        [&#x27;CloneMultipleVolumes is used to create a clone of a group of specified volumes. A consistent set of characteristics can be assigned to a group of multiple volume when they are cloned together.&#x27;, &#x27;If groupSnapshotID is going to be used to clone the volumes in a group snapshot, the group snapshot must be created first using the CreateGroupSnapshot API method or the SolidFire Element WebUI. Using groupSnapshotID is optional when cloning multiple volumes.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Note&lt;/b&gt;: Cloning multiple volumes is allowed if cluster fullness is at stage 2 or 3. Clones are not created when cluster fullness is at stage 4 or 5.&#x27;]
        [&#x27;CloneMultipleVolumes is used to create a clone of a group of specified volumes. A consistent set of characteristics can be assigned to a group of multiple volume when they are cloned together.&#x27;, &#x27;If groupSnapshotID is going to be used to clone the volumes in a group snapshot, the group snapshot must be created first using the CreateGroupSnapshot API method or the SolidFire Element WebUI. Using groupSnapshotID is optional when cloning multiple volumes.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Note&lt;/b&gt;: Cloning multiple volumes is allowed if cluster fullness is at stage 2 or 3. Clones are not created when cluster fullness is at stage 4 or 5.&#x27;]
        :param volumes: [required] Array of Unique ID for each volume to include in the clone with optional parameters. If optional parameters are not specified, the values will be inherited from the source volumes.
        :type volumes: 
        
        :param access:  [&#x27;New default access method for the new volumes if not overridden by information passed in the volumes array.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;readOnly&lt;/b&gt;: Only read operations are allowed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;readWrite&lt;/b&gt;: Reads and writes are allowed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;locked&lt;/b&gt;: No reads or writes are allowed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;replicationTarget&lt;/b&gt;: Identify a volume as the target volume for a paired set of volumes. If the volume is not paired, the access status is locked.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;If unspecified, the access settings of the clone will be the same as the source.&#x27;][&#x27;New default access method for the new volumes if not overridden by information passed in the volumes array.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;readOnly&lt;/b&gt;: Only read operations are allowed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;readWrite&lt;/b&gt;: Reads and writes are allowed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;locked&lt;/b&gt;: No reads or writes are allowed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;replicationTarget&lt;/b&gt;: Identify a volume as the target volume for a paired set of volumes. If the volume is not paired, the access status is locked.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;If unspecified, the access settings of the clone will be the same as the source.&#x27;][&#x27;New default access method for the new volumes if not overridden by information passed in the volumes array.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;readOnly&lt;/b&gt;: Only read operations are allowed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;readWrite&lt;/b&gt;: Reads and writes are allowed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;locked&lt;/b&gt;: No reads or writes are allowed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;replicationTarget&lt;/b&gt;: Identify a volume as the target volume for a paired set of volumes. If the volume is not paired, the access status is locked.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;If unspecified, the access settings of the clone will be the same as the source.&#x27;][&#x27;New default access method for the new volumes if not overridden by information passed in the volumes array.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;readOnly&lt;/b&gt;: Only read operations are allowed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;readWrite&lt;/b&gt;: Reads and writes are allowed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;locked&lt;/b&gt;: No reads or writes are allowed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;replicationTarget&lt;/b&gt;: Identify a volume as the target volume for a paired set of volumes. If the volume is not paired, the access status is locked.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;If unspecified, the access settings of the clone will be the same as the source.&#x27;][&#x27;New default access method for the new volumes if not overridden by information passed in the volumes array.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;readOnly&lt;/b&gt;: Only read operations are allowed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;readWrite&lt;/b&gt;: Reads and writes are allowed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;locked&lt;/b&gt;: No reads or writes are allowed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;replicationTarget&lt;/b&gt;: Identify a volume as the target volume for a paired set of volumes. If the volume is not paired, the access status is locked.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;If unspecified, the access settings of the clone will be the same as the source.&#x27;][&#x27;New default access method for the new volumes if not overridden by information passed in the volumes array.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;readOnly&lt;/b&gt;: Only read operations are allowed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;readWrite&lt;/b&gt;: Reads and writes are allowed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;locked&lt;/b&gt;: No reads or writes are allowed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;replicationTarget&lt;/b&gt;: Identify a volume as the target volume for a paired set of volumes. If the volume is not paired, the access status is locked.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;If unspecified, the access settings of the clone will be the same as the source.&#x27;][&#x27;New default access method for the new volumes if not overridden by information passed in the volumes array.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;readOnly&lt;/b&gt;: Only read operations are allowed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;readWrite&lt;/b&gt;: Reads and writes are allowed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;locked&lt;/b&gt;: No reads or writes are allowed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;replicationTarget&lt;/b&gt;: Identify a volume as the target volume for a paired set of volumes. If the volume is not paired, the access status is locked.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;If unspecified, the access settings of the clone will be the same as the source.&#x27;]
        :type access: 
        
        :param groupSnapshotID:  ID of the group snapshot to use as a basis for the clone.
        :type groupSnapshotID: 
        
        :param newAccountID:  New account ID for the volumes if not overridden by information passed in the volumes array.
        :type newAccountID: 
        """

        params = { 
            "volumes": volumes,
        }
        if access is not None:
            params["access"] = access
        if groupSnapshotID is not None:
            params["groupSnapshotID"] = groupSnapshotID
        if newAccountID is not None:
            params["newAccountID"] = newAccountID
        
        # There is no adaptor.
        return self.send_request(
            'CloneMultipleVolumes',
            CloneMultipleVolumesResult,
            params
        )

    def copy_volume(
            self,
            volumeID,
            dstVolumeID,
            snapshotID=OPTIONAL,):
        """
        Copies one volume to another.
        :param volumeID: [required] Source volume to copy.
        :type volumeID: 
        
        :param dstVolumeID: [required] Destination volume for the copy.
        :type dstVolumeID: 
        
        :param snapshotID:  Snapshot ID of the source volume to create the copy from.
        :type snapshotID: 
        """

        params = { 
            "volumeID": volumeID,
            "dstVolumeID": dstVolumeID,
        }
        if snapshotID is not None:
            params["snapshotID"] = snapshotID
        
        # There is no adaptor.
        return self.send_request(
            'CopyVolume',
            CopyVolumeResult,
            params,
            since=9.0
        )

    def cancel_clone(
            self,
            cloneID,):
        """
        Cancels a currently running clone operation.
        :param cloneID: [required] 
        :type cloneID: 
        """

        params = { 
            "cloneID": cloneID,
        }
        
        # There is no adaptor.
        return self.send_request(
            'CancelClone',
            CancelCloneResult,
            params,
            since=9.0
        )

    def create_volume(
            self,
            name,
            accountID,
            totalSize,
            enable512e,
            qos=OPTIONAL,
            attributes=OPTIONAL,):
        """
        [&#x27;CreateVolume is used to create a new (empty) volume on the cluster.&#x27;, &#x27;When the volume is created successfully it is available for connection via iSCSI.&#x27;]
        [&#x27;CreateVolume is used to create a new (empty) volume on the cluster.&#x27;, &#x27;When the volume is created successfully it is available for connection via iSCSI.&#x27;]
        :param name: [required] [&#x27;Name of the volume.&#x27;, &#x27;Not required to be unique, but it is recommended.&#x27;, &#x27;May be 1 to 64 characters in length.&#x27;][&#x27;Name of the volume.&#x27;, &#x27;Not required to be unique, but it is recommended.&#x27;, &#x27;May be 1 to 64 characters in length.&#x27;][&#x27;Name of the volume.&#x27;, &#x27;Not required to be unique, but it is recommended.&#x27;, &#x27;May be 1 to 64 characters in length.&#x27;]
        :type name: 
        
        :param accountID: [required] AccountID for the owner of this volume.
        :type accountID: 
        
        :param totalSize: [required] Total size of the volume, in bytes. Size is rounded up to the nearest 1MB size.
        :type totalSize: 
        
        :param enable512e: [required] Should the volume provides 512-byte sector emulation?
        :type enable512e: 
        
        :param qos:  [&#x27;Initial quality of service settings for this volume.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;Volumes created without specified QoS values are created with the default values for QoS.&#x27;, &#x27;Default values for a volume can be found by running the GetDefaultQoS method.&#x27;][&#x27;Initial quality of service settings for this volume.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;Volumes created without specified QoS values are created with the default values for QoS.&#x27;, &#x27;Default values for a volume can be found by running the GetDefaultQoS method.&#x27;][&#x27;Initial quality of service settings for this volume.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;Volumes created without specified QoS values are created with the default values for QoS.&#x27;, &#x27;Default values for a volume can be found by running the GetDefaultQoS method.&#x27;][&#x27;Initial quality of service settings for this volume.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;Volumes created without specified QoS values are created with the default values for QoS.&#x27;, &#x27;Default values for a volume can be found by running the GetDefaultQoS method.&#x27;]
        :type qos: 
        
        :param attributes:  List of Name/Value pairs in JSON object format.
        :type attributes: 
        """

        params = { 
            "name": name,
            "accountID": accountID,
            "totalSize": totalSize,
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
            volumeID,):
        """
        [&#x27;DeleteVolume marks an active volume for deletion.&#x27;, &#x27;It is purged (permanently deleted) after the cleanup interval elapses.&#x27;, &#x27;After making a request to delete a volume, any active iSCSI connections to the volume is immediately terminated and no further connections are allowed while the volume is in this state.&#x27;, &#x27;It is not returned in target discovery requests.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;Any snapshots of a volume that has been marked to delete are not affected.&#x27;, &#x27;Snapshots are kept until the volume is purged from the system.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;If a volume is marked for deletion, and it has a bulk volume read or bulk volume write operation in progress, the bulk volume operation is stopped.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;If the volume you delete is paired with a volume, replication between the paired volumes is suspended and no data is transferred to it or from it while in a deleted state.&#x27;, &#x27;The remote volume the deleted volume was paired with enters into a PausedMisconfigured state and data is no longer sent to it or from the deleted volume.&#x27;, &#x27;Until the deleted volume is purged, it can be restored and data transfers resumes.&#x27;, &#x27;If the deleted volume gets purged from the system, the volume it was paired with enters into a StoppedMisconfigured state and the volume pairing status is removed.&#x27;, &#x27;The purged volume becomes permanently unavailable.&#x27;]
        [&#x27;DeleteVolume marks an active volume for deletion.&#x27;, &#x27;It is purged (permanently deleted) after the cleanup interval elapses.&#x27;, &#x27;After making a request to delete a volume, any active iSCSI connections to the volume is immediately terminated and no further connections are allowed while the volume is in this state.&#x27;, &#x27;It is not returned in target discovery requests.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;Any snapshots of a volume that has been marked to delete are not affected.&#x27;, &#x27;Snapshots are kept until the volume is purged from the system.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;If a volume is marked for deletion, and it has a bulk volume read or bulk volume write operation in progress, the bulk volume operation is stopped.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;If the volume you delete is paired with a volume, replication between the paired volumes is suspended and no data is transferred to it or from it while in a deleted state.&#x27;, &#x27;The remote volume the deleted volume was paired with enters into a PausedMisconfigured state and data is no longer sent to it or from the deleted volume.&#x27;, &#x27;Until the deleted volume is purged, it can be restored and data transfers resumes.&#x27;, &#x27;If the deleted volume gets purged from the system, the volume it was paired with enters into a StoppedMisconfigured state and the volume pairing status is removed.&#x27;, &#x27;The purged volume becomes permanently unavailable.&#x27;]
        [&#x27;DeleteVolume marks an active volume for deletion.&#x27;, &#x27;It is purged (permanently deleted) after the cleanup interval elapses.&#x27;, &#x27;After making a request to delete a volume, any active iSCSI connections to the volume is immediately terminated and no further connections are allowed while the volume is in this state.&#x27;, &#x27;It is not returned in target discovery requests.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;Any snapshots of a volume that has been marked to delete are not affected.&#x27;, &#x27;Snapshots are kept until the volume is purged from the system.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;If a volume is marked for deletion, and it has a bulk volume read or bulk volume write operation in progress, the bulk volume operation is stopped.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;If the volume you delete is paired with a volume, replication between the paired volumes is suspended and no data is transferred to it or from it while in a deleted state.&#x27;, &#x27;The remote volume the deleted volume was paired with enters into a PausedMisconfigured state and data is no longer sent to it or from the deleted volume.&#x27;, &#x27;Until the deleted volume is purged, it can be restored and data transfers resumes.&#x27;, &#x27;If the deleted volume gets purged from the system, the volume it was paired with enters into a StoppedMisconfigured state and the volume pairing status is removed.&#x27;, &#x27;The purged volume becomes permanently unavailable.&#x27;]
        [&#x27;DeleteVolume marks an active volume for deletion.&#x27;, &#x27;It is purged (permanently deleted) after the cleanup interval elapses.&#x27;, &#x27;After making a request to delete a volume, any active iSCSI connections to the volume is immediately terminated and no further connections are allowed while the volume is in this state.&#x27;, &#x27;It is not returned in target discovery requests.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;Any snapshots of a volume that has been marked to delete are not affected.&#x27;, &#x27;Snapshots are kept until the volume is purged from the system.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;If a volume is marked for deletion, and it has a bulk volume read or bulk volume write operation in progress, the bulk volume operation is stopped.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;If the volume you delete is paired with a volume, replication between the paired volumes is suspended and no data is transferred to it or from it while in a deleted state.&#x27;, &#x27;The remote volume the deleted volume was paired with enters into a PausedMisconfigured state and data is no longer sent to it or from the deleted volume.&#x27;, &#x27;Until the deleted volume is purged, it can be restored and data transfers resumes.&#x27;, &#x27;If the deleted volume gets purged from the system, the volume it was paired with enters into a StoppedMisconfigured state and the volume pairing status is removed.&#x27;, &#x27;The purged volume becomes permanently unavailable.&#x27;]
        [&#x27;DeleteVolume marks an active volume for deletion.&#x27;, &#x27;It is purged (permanently deleted) after the cleanup interval elapses.&#x27;, &#x27;After making a request to delete a volume, any active iSCSI connections to the volume is immediately terminated and no further connections are allowed while the volume is in this state.&#x27;, &#x27;It is not returned in target discovery requests.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;Any snapshots of a volume that has been marked to delete are not affected.&#x27;, &#x27;Snapshots are kept until the volume is purged from the system.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;If a volume is marked for deletion, and it has a bulk volume read or bulk volume write operation in progress, the bulk volume operation is stopped.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;If the volume you delete is paired with a volume, replication between the paired volumes is suspended and no data is transferred to it or from it while in a deleted state.&#x27;, &#x27;The remote volume the deleted volume was paired with enters into a PausedMisconfigured state and data is no longer sent to it or from the deleted volume.&#x27;, &#x27;Until the deleted volume is purged, it can be restored and data transfers resumes.&#x27;, &#x27;If the deleted volume gets purged from the system, the volume it was paired with enters into a StoppedMisconfigured state and the volume pairing status is removed.&#x27;, &#x27;The purged volume becomes permanently unavailable.&#x27;]
        [&#x27;DeleteVolume marks an active volume for deletion.&#x27;, &#x27;It is purged (permanently deleted) after the cleanup interval elapses.&#x27;, &#x27;After making a request to delete a volume, any active iSCSI connections to the volume is immediately terminated and no further connections are allowed while the volume is in this state.&#x27;, &#x27;It is not returned in target discovery requests.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;Any snapshots of a volume that has been marked to delete are not affected.&#x27;, &#x27;Snapshots are kept until the volume is purged from the system.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;If a volume is marked for deletion, and it has a bulk volume read or bulk volume write operation in progress, the bulk volume operation is stopped.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;If the volume you delete is paired with a volume, replication between the paired volumes is suspended and no data is transferred to it or from it while in a deleted state.&#x27;, &#x27;The remote volume the deleted volume was paired with enters into a PausedMisconfigured state and data is no longer sent to it or from the deleted volume.&#x27;, &#x27;Until the deleted volume is purged, it can be restored and data transfers resumes.&#x27;, &#x27;If the deleted volume gets purged from the system, the volume it was paired with enters into a StoppedMisconfigured state and the volume pairing status is removed.&#x27;, &#x27;The purged volume becomes permanently unavailable.&#x27;]
        [&#x27;DeleteVolume marks an active volume for deletion.&#x27;, &#x27;It is purged (permanently deleted) after the cleanup interval elapses.&#x27;, &#x27;After making a request to delete a volume, any active iSCSI connections to the volume is immediately terminated and no further connections are allowed while the volume is in this state.&#x27;, &#x27;It is not returned in target discovery requests.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;Any snapshots of a volume that has been marked to delete are not affected.&#x27;, &#x27;Snapshots are kept until the volume is purged from the system.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;If a volume is marked for deletion, and it has a bulk volume read or bulk volume write operation in progress, the bulk volume operation is stopped.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;If the volume you delete is paired with a volume, replication between the paired volumes is suspended and no data is transferred to it or from it while in a deleted state.&#x27;, &#x27;The remote volume the deleted volume was paired with enters into a PausedMisconfigured state and data is no longer sent to it or from the deleted volume.&#x27;, &#x27;Until the deleted volume is purged, it can be restored and data transfers resumes.&#x27;, &#x27;If the deleted volume gets purged from the system, the volume it was paired with enters into a StoppedMisconfigured state and the volume pairing status is removed.&#x27;, &#x27;The purged volume becomes permanently unavailable.&#x27;]
        [&#x27;DeleteVolume marks an active volume for deletion.&#x27;, &#x27;It is purged (permanently deleted) after the cleanup interval elapses.&#x27;, &#x27;After making a request to delete a volume, any active iSCSI connections to the volume is immediately terminated and no further connections are allowed while the volume is in this state.&#x27;, &#x27;It is not returned in target discovery requests.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;Any snapshots of a volume that has been marked to delete are not affected.&#x27;, &#x27;Snapshots are kept until the volume is purged from the system.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;If a volume is marked for deletion, and it has a bulk volume read or bulk volume write operation in progress, the bulk volume operation is stopped.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;If the volume you delete is paired with a volume, replication between the paired volumes is suspended and no data is transferred to it or from it while in a deleted state.&#x27;, &#x27;The remote volume the deleted volume was paired with enters into a PausedMisconfigured state and data is no longer sent to it or from the deleted volume.&#x27;, &#x27;Until the deleted volume is purged, it can be restored and data transfers resumes.&#x27;, &#x27;If the deleted volume gets purged from the system, the volume it was paired with enters into a StoppedMisconfigured state and the volume pairing status is removed.&#x27;, &#x27;The purged volume becomes permanently unavailable.&#x27;]
        [&#x27;DeleteVolume marks an active volume for deletion.&#x27;, &#x27;It is purged (permanently deleted) after the cleanup interval elapses.&#x27;, &#x27;After making a request to delete a volume, any active iSCSI connections to the volume is immediately terminated and no further connections are allowed while the volume is in this state.&#x27;, &#x27;It is not returned in target discovery requests.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;Any snapshots of a volume that has been marked to delete are not affected.&#x27;, &#x27;Snapshots are kept until the volume is purged from the system.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;If a volume is marked for deletion, and it has a bulk volume read or bulk volume write operation in progress, the bulk volume operation is stopped.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;If the volume you delete is paired with a volume, replication between the paired volumes is suspended and no data is transferred to it or from it while in a deleted state.&#x27;, &#x27;The remote volume the deleted volume was paired with enters into a PausedMisconfigured state and data is no longer sent to it or from the deleted volume.&#x27;, &#x27;Until the deleted volume is purged, it can be restored and data transfers resumes.&#x27;, &#x27;If the deleted volume gets purged from the system, the volume it was paired with enters into a StoppedMisconfigured state and the volume pairing status is removed.&#x27;, &#x27;The purged volume becomes permanently unavailable.&#x27;]
        [&#x27;DeleteVolume marks an active volume for deletion.&#x27;, &#x27;It is purged (permanently deleted) after the cleanup interval elapses.&#x27;, &#x27;After making a request to delete a volume, any active iSCSI connections to the volume is immediately terminated and no further connections are allowed while the volume is in this state.&#x27;, &#x27;It is not returned in target discovery requests.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;Any snapshots of a volume that has been marked to delete are not affected.&#x27;, &#x27;Snapshots are kept until the volume is purged from the system.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;If a volume is marked for deletion, and it has a bulk volume read or bulk volume write operation in progress, the bulk volume operation is stopped.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;If the volume you delete is paired with a volume, replication between the paired volumes is suspended and no data is transferred to it or from it while in a deleted state.&#x27;, &#x27;The remote volume the deleted volume was paired with enters into a PausedMisconfigured state and data is no longer sent to it or from the deleted volume.&#x27;, &#x27;Until the deleted volume is purged, it can be restored and data transfers resumes.&#x27;, &#x27;If the deleted volume gets purged from the system, the volume it was paired with enters into a StoppedMisconfigured state and the volume pairing status is removed.&#x27;, &#x27;The purged volume becomes permanently unavailable.&#x27;]
        [&#x27;DeleteVolume marks an active volume for deletion.&#x27;, &#x27;It is purged (permanently deleted) after the cleanup interval elapses.&#x27;, &#x27;After making a request to delete a volume, any active iSCSI connections to the volume is immediately terminated and no further connections are allowed while the volume is in this state.&#x27;, &#x27;It is not returned in target discovery requests.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;Any snapshots of a volume that has been marked to delete are not affected.&#x27;, &#x27;Snapshots are kept until the volume is purged from the system.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;If a volume is marked for deletion, and it has a bulk volume read or bulk volume write operation in progress, the bulk volume operation is stopped.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;If the volume you delete is paired with a volume, replication between the paired volumes is suspended and no data is transferred to it or from it while in a deleted state.&#x27;, &#x27;The remote volume the deleted volume was paired with enters into a PausedMisconfigured state and data is no longer sent to it or from the deleted volume.&#x27;, &#x27;Until the deleted volume is purged, it can be restored and data transfers resumes.&#x27;, &#x27;If the deleted volume gets purged from the system, the volume it was paired with enters into a StoppedMisconfigured state and the volume pairing status is removed.&#x27;, &#x27;The purged volume becomes permanently unavailable.&#x27;]
        [&#x27;DeleteVolume marks an active volume for deletion.&#x27;, &#x27;It is purged (permanently deleted) after the cleanup interval elapses.&#x27;, &#x27;After making a request to delete a volume, any active iSCSI connections to the volume is immediately terminated and no further connections are allowed while the volume is in this state.&#x27;, &#x27;It is not returned in target discovery requests.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;Any snapshots of a volume that has been marked to delete are not affected.&#x27;, &#x27;Snapshots are kept until the volume is purged from the system.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;If a volume is marked for deletion, and it has a bulk volume read or bulk volume write operation in progress, the bulk volume operation is stopped.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;If the volume you delete is paired with a volume, replication between the paired volumes is suspended and no data is transferred to it or from it while in a deleted state.&#x27;, &#x27;The remote volume the deleted volume was paired with enters into a PausedMisconfigured state and data is no longer sent to it or from the deleted volume.&#x27;, &#x27;Until the deleted volume is purged, it can be restored and data transfers resumes.&#x27;, &#x27;If the deleted volume gets purged from the system, the volume it was paired with enters into a StoppedMisconfigured state and the volume pairing status is removed.&#x27;, &#x27;The purged volume becomes permanently unavailable.&#x27;]
        [&#x27;DeleteVolume marks an active volume for deletion.&#x27;, &#x27;It is purged (permanently deleted) after the cleanup interval elapses.&#x27;, &#x27;After making a request to delete a volume, any active iSCSI connections to the volume is immediately terminated and no further connections are allowed while the volume is in this state.&#x27;, &#x27;It is not returned in target discovery requests.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;Any snapshots of a volume that has been marked to delete are not affected.&#x27;, &#x27;Snapshots are kept until the volume is purged from the system.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;If a volume is marked for deletion, and it has a bulk volume read or bulk volume write operation in progress, the bulk volume operation is stopped.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;If the volume you delete is paired with a volume, replication between the paired volumes is suspended and no data is transferred to it or from it while in a deleted state.&#x27;, &#x27;The remote volume the deleted volume was paired with enters into a PausedMisconfigured state and data is no longer sent to it or from the deleted volume.&#x27;, &#x27;Until the deleted volume is purged, it can be restored and data transfers resumes.&#x27;, &#x27;If the deleted volume gets purged from the system, the volume it was paired with enters into a StoppedMisconfigured state and the volume pairing status is removed.&#x27;, &#x27;The purged volume becomes permanently unavailable.&#x27;]
        [&#x27;DeleteVolume marks an active volume for deletion.&#x27;, &#x27;It is purged (permanently deleted) after the cleanup interval elapses.&#x27;, &#x27;After making a request to delete a volume, any active iSCSI connections to the volume is immediately terminated and no further connections are allowed while the volume is in this state.&#x27;, &#x27;It is not returned in target discovery requests.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;Any snapshots of a volume that has been marked to delete are not affected.&#x27;, &#x27;Snapshots are kept until the volume is purged from the system.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;If a volume is marked for deletion, and it has a bulk volume read or bulk volume write operation in progress, the bulk volume operation is stopped.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;If the volume you delete is paired with a volume, replication between the paired volumes is suspended and no data is transferred to it or from it while in a deleted state.&#x27;, &#x27;The remote volume the deleted volume was paired with enters into a PausedMisconfigured state and data is no longer sent to it or from the deleted volume.&#x27;, &#x27;Until the deleted volume is purged, it can be restored and data transfers resumes.&#x27;, &#x27;If the deleted volume gets purged from the system, the volume it was paired with enters into a StoppedMisconfigured state and the volume pairing status is removed.&#x27;, &#x27;The purged volume becomes permanently unavailable.&#x27;]
        [&#x27;DeleteVolume marks an active volume for deletion.&#x27;, &#x27;It is purged (permanently deleted) after the cleanup interval elapses.&#x27;, &#x27;After making a request to delete a volume, any active iSCSI connections to the volume is immediately terminated and no further connections are allowed while the volume is in this state.&#x27;, &#x27;It is not returned in target discovery requests.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;Any snapshots of a volume that has been marked to delete are not affected.&#x27;, &#x27;Snapshots are kept until the volume is purged from the system.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;If a volume is marked for deletion, and it has a bulk volume read or bulk volume write operation in progress, the bulk volume operation is stopped.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;If the volume you delete is paired with a volume, replication between the paired volumes is suspended and no data is transferred to it or from it while in a deleted state.&#x27;, &#x27;The remote volume the deleted volume was paired with enters into a PausedMisconfigured state and data is no longer sent to it or from the deleted volume.&#x27;, &#x27;Until the deleted volume is purged, it can be restored and data transfers resumes.&#x27;, &#x27;If the deleted volume gets purged from the system, the volume it was paired with enters into a StoppedMisconfigured state and the volume pairing status is removed.&#x27;, &#x27;The purged volume becomes permanently unavailable.&#x27;]
        :param volumeID: [required] The ID of the volume to delete.
        :type volumeID: 
        """

        params = { 
            "volumeID": volumeID,
        }
        
        # There is no adaptor.
        return self.send_request(
            'DeleteVolume',
            DeleteVolumeResult,
            params
        )

    def get_default_qo_s(
            self,):
        """
        [&#x27;GetDefaultQoS is used to retrieve the default QoS values that are set for a volume if QoS is not supplied.&#x27;]"""

        params = { 
        }
        
        # There is no adaptor.
        return self.send_request(
            'GetDefaultQoS',
            VolumeQOS,
            params
        )

    def get_volume_stats(
            self,
            volumeID,):
        """
        [&#x27;GetVolumeStats is used to retrieve high-level activity measurements for a single volume.&#x27;, &#x27;Values are cumulative from the creation of the volume.&#x27;]
        [&#x27;GetVolumeStats is used to retrieve high-level activity measurements for a single volume.&#x27;, &#x27;Values are cumulative from the creation of the volume.&#x27;]
        :param volumeID: [required] Specifies the volume for which statistics is gathered.
        :type volumeID: 
        """

        params = { 
            "volumeID": volumeID,
        }
        
        # There is no adaptor.
        return self.send_request(
            'GetVolumeStats',
            GetVolumeStatsResult,
            params
        )

    def get_volume_efficiency(
            self,
            volumeID,
            force=OPTIONAL,):
        """
        [&#x27;GetVolumeEfficiency is used to retrieve information about a volume.&#x27;, &#x27;Only the volume given as a parameter in this API method is used to compute the capacity.&#x27;]
        [&#x27;GetVolumeEfficiency is used to retrieve information about a volume.&#x27;, &#x27;Only the volume given as a parameter in this API method is used to compute the capacity.&#x27;]
        :param volumeID: [required] Specifies the volume for which capacity is computed.
        :type volumeID: 
        
        :param force:  
        :type force: 
        """

        params = { 
            "volumeID": volumeID,
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
        [&#x27;ListBulkVolumeJobs is used to return information about each bulk volume read or write operation that is occurring in the system.&#x27;]"""

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
            startVolumeID=OPTIONAL,
            limit=OPTIONAL,):
        """
        [&#x27;ListActiveVolumes is used to return the list of active volumes currently in the system.&#x27;, &#x27;The list of volumes is returned sorted in VolumeID order and can be returned in multiple parts (pages).&#x27;]
        [&#x27;ListActiveVolumes is used to return the list of active volumes currently in the system.&#x27;, &#x27;The list of volumes is returned sorted in VolumeID order and can be returned in multiple parts (pages).&#x27;]
        :param startVolumeID:  [&#x27;The ID of the first volume to list.&#x27;, &#x27;This can be useful for paging results.&#x27;, &#x27;By default, this starts at the lowest VolumeID.&#x27;][&#x27;The ID of the first volume to list.&#x27;, &#x27;This can be useful for paging results.&#x27;, &#x27;By default, this starts at the lowest VolumeID.&#x27;][&#x27;The ID of the first volume to list.&#x27;, &#x27;This can be useful for paging results.&#x27;, &#x27;By default, this starts at the lowest VolumeID.&#x27;]
        :type startVolumeID: 
        
        :param limit:  [&#x27;The maximum number of volumes to return from the API.&#x27;]
        :type limit: 
        """

        params = { 
        }
        if startVolumeID is not None:
            params["startVolumeID"] = startVolumeID
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
        [&#x27;ListDeletedVolumes is used to return the entire list of volumes that have been marked for deletion and is purged from the system.&#x27;]"""

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
            startVolumeID=OPTIONAL,
            limit=OPTIONAL,
            volumeStatus=OPTIONAL,
            accounts=OPTIONAL,
            isPaired=OPTIONAL,
            volumeIDs=OPTIONAL,):
        """
        [&#x27;The ListVolumes method is used to return a list of volumes that are in a cluster.&#x27;, &#x27;You can specify the volumes you want to return in the list by using the available parameters.&#x27;]
        [&#x27;The ListVolumes method is used to return a list of volumes that are in a cluster.&#x27;, &#x27;You can specify the volumes you want to return in the list by using the available parameters.&#x27;]
        :param startVolumeID:  [&#x27;The ID of the first volume to list.&#x27;, &#x27;This can be useful for paging results.&#x27;, &#x27;By default, this starts at the lowest VolumeID.&#x27;][&#x27;The ID of the first volume to list.&#x27;, &#x27;This can be useful for paging results.&#x27;, &#x27;By default, this starts at the lowest VolumeID.&#x27;][&#x27;The ID of the first volume to list.&#x27;, &#x27;This can be useful for paging results.&#x27;, &#x27;By default, this starts at the lowest VolumeID.&#x27;]
        :type startVolumeID: 
        
        :param limit:  [&#x27;The maximum number of volumes to return from the API.&#x27;]
        :type limit: 
        
        :param volumeStatus:  [&#x27;If specified, filter to only volumes with the provided status.&#x27;, &#x27;By default, list all volumes.&#x27;][&#x27;If specified, filter to only volumes with the provided status.&#x27;, &#x27;By default, list all volumes.&#x27;]
        :type volumeStatus: 
        
        :param accounts:  [&#x27;If specified, only fetch volumes which belong to the provided accounts.&#x27;, &#x27;By default, list volumes for all accounts.&#x27;][&#x27;If specified, only fetch volumes which belong to the provided accounts.&#x27;, &#x27;By default, list volumes for all accounts.&#x27;]
        :type accounts: 
        
        :param isPaired:  [&#x27;If specified, only fetch volumes which are paired (if true) or non-paired (if false).&#x27;, &#x27;By default, list all volumes regardless of their pairing status.&#x27;][&#x27;If specified, only fetch volumes which are paired (if true) or non-paired (if false).&#x27;, &#x27;By default, list all volumes regardless of their pairing status.&#x27;]
        :type isPaired: 
        
        :param volumeIDs:  [&#x27;If specified, only fetch volumes specified in this list.&#x27;, &#x27;This option cannot be specified if startVolumeID, limit, or accounts option is specified.&#x27;][&#x27;If specified, only fetch volumes specified in this list.&#x27;, &#x27;This option cannot be specified if startVolumeID, limit, or accounts option is specified.&#x27;]
        :type volumeIDs: 
        """

        params = { 
        }
        if startVolumeID is not None:
            params["startVolumeID"] = startVolumeID
        if limit is not None:
            params["limit"] = limit
        if volumeStatus is not None:
            params["volumeStatus"] = volumeStatus
        if accounts is not None:
            params["accounts"] = accounts
        if isPaired is not None:
            params["isPaired"] = isPaired
        if volumeIDs is not None:
            params["volumeIDs"] = volumeIDs
        
        # There is no adaptor.
        return self.send_request(
            'ListVolumes',
            ListVolumesResult,
            params,
            since=8.0
        )

    def list_volumes_for_account(
            self,
            accountID,
            startVolumeID=OPTIONAL,
            limit=OPTIONAL,):
        """
        [&#x27;ListVolumesForAccount returns the list of active AND (pending) deleted volumes for an account.&#x27;]
        :param accountID: [required] The ID of the account to list the volumes for.
        :type accountID: 
        
        :param startVolumeID:  [&#x27;The ID of the first volume to list.&#x27;, &#x27;This can be useful for paging results.&#x27;, &#x27;By default, this starts at the lowest VolumeID.&#x27;][&#x27;The ID of the first volume to list.&#x27;, &#x27;This can be useful for paging results.&#x27;, &#x27;By default, this starts at the lowest VolumeID.&#x27;][&#x27;The ID of the first volume to list.&#x27;, &#x27;This can be useful for paging results.&#x27;, &#x27;By default, this starts at the lowest VolumeID.&#x27;]
        :type startVolumeID: 
        
        :param limit:  [&#x27;The maximum number of volumes to return from the API.&#x27;]
        :type limit: 
        """

        params = { 
            "accountID": accountID,
        }
        if startVolumeID is not None:
            params["startVolumeID"] = startVolumeID
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
        [&#x27;ListVolumeStatsByAccount returns high-level activity measurements for every account.&#x27;, &#x27;Values are summed from all the volumes owned by the account.&#x27;]
        [&#x27;ListVolumeStatsByAccount returns high-level activity measurements for every account.&#x27;, &#x27;Values are summed from all the volumes owned by the account.&#x27;]"""

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
        [&#x27;ListVolumeStatsByVolume returns high-level activity measurements for every volume, by volume.&#x27;, &#x27;Values are cumulative from the creation of the volume.&#x27;]
        [&#x27;ListVolumeStatsByVolume returns high-level activity measurements for every volume, by volume.&#x27;, &#x27;Values are cumulative from the creation of the volume.&#x27;]"""

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
            volumeAccessGroups=OPTIONAL,):
        """
        [&#x27;ListVolumeStatsByVolumeAccessGroup is used to get total activity measurements for all of the volumes that are a member of the specified volume access group(s).&#x27;]
        :param volumeAccessGroups:  [&#x27;An array of VolumeAccessGroupIDs for which volume activity is returned.&#x27;, &#x27;If no VolumeAccessGroupID is specified, stats for all volume access groups is returned.&#x27;][&#x27;An array of VolumeAccessGroupIDs for which volume activity is returned.&#x27;, &#x27;If no VolumeAccessGroupID is specified, stats for all volume access groups is returned.&#x27;]
        :type volumeAccessGroups: 
        """

        params = { 
        }
        if volumeAccessGroups is not None:
            params["volumeAccessGroups"] = volumeAccessGroups
        
        # There is no adaptor.
        return self.send_request(
            'ListVolumeStatsByVolumeAccessGroup',
            ListVolumeStatsByVolumeAccessGroupResult,
            params
        )

    def modify_volume(
            self,
            volumeID,
            accountID=OPTIONAL,
            access=OPTIONAL,
            qos=OPTIONAL,
            totalSize=OPTIONAL,
            attributes=OPTIONAL,):
        """
        [&#x27;ModifyVolume is used to modify settings on an existing volume.&#x27;, &#x27;Modifications can be made to one volume at a time and changes take place immediately.&#x27;, &#x27;If an optional parameter is left unspecified, the value will not be changed.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;Extending the size of a volume that is being replicated should be done in an order.&#x27;, &#x27;The target (Replication Target) volume should first be increased in size, then the source (Read/Write) volume can be resized.&#x27;, &#x27;It is recommended that both the target and the source volumes be the same size.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Note&lt;/b&gt;: If you change access status to locked or target all existing iSCSI connections are terminated.&#x27;]
        [&#x27;ModifyVolume is used to modify settings on an existing volume.&#x27;, &#x27;Modifications can be made to one volume at a time and changes take place immediately.&#x27;, &#x27;If an optional parameter is left unspecified, the value will not be changed.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;Extending the size of a volume that is being replicated should be done in an order.&#x27;, &#x27;The target (Replication Target) volume should first be increased in size, then the source (Read/Write) volume can be resized.&#x27;, &#x27;It is recommended that both the target and the source volumes be the same size.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Note&lt;/b&gt;: If you change access status to locked or target all existing iSCSI connections are terminated.&#x27;]
        [&#x27;ModifyVolume is used to modify settings on an existing volume.&#x27;, &#x27;Modifications can be made to one volume at a time and changes take place immediately.&#x27;, &#x27;If an optional parameter is left unspecified, the value will not be changed.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;Extending the size of a volume that is being replicated should be done in an order.&#x27;, &#x27;The target (Replication Target) volume should first be increased in size, then the source (Read/Write) volume can be resized.&#x27;, &#x27;It is recommended that both the target and the source volumes be the same size.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Note&lt;/b&gt;: If you change access status to locked or target all existing iSCSI connections are terminated.&#x27;]
        [&#x27;ModifyVolume is used to modify settings on an existing volume.&#x27;, &#x27;Modifications can be made to one volume at a time and changes take place immediately.&#x27;, &#x27;If an optional parameter is left unspecified, the value will not be changed.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;Extending the size of a volume that is being replicated should be done in an order.&#x27;, &#x27;The target (Replication Target) volume should first be increased in size, then the source (Read/Write) volume can be resized.&#x27;, &#x27;It is recommended that both the target and the source volumes be the same size.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Note&lt;/b&gt;: If you change access status to locked or target all existing iSCSI connections are terminated.&#x27;]
        [&#x27;ModifyVolume is used to modify settings on an existing volume.&#x27;, &#x27;Modifications can be made to one volume at a time and changes take place immediately.&#x27;, &#x27;If an optional parameter is left unspecified, the value will not be changed.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;Extending the size of a volume that is being replicated should be done in an order.&#x27;, &#x27;The target (Replication Target) volume should first be increased in size, then the source (Read/Write) volume can be resized.&#x27;, &#x27;It is recommended that both the target and the source volumes be the same size.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Note&lt;/b&gt;: If you change access status to locked or target all existing iSCSI connections are terminated.&#x27;]
        [&#x27;ModifyVolume is used to modify settings on an existing volume.&#x27;, &#x27;Modifications can be made to one volume at a time and changes take place immediately.&#x27;, &#x27;If an optional parameter is left unspecified, the value will not be changed.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;Extending the size of a volume that is being replicated should be done in an order.&#x27;, &#x27;The target (Replication Target) volume should first be increased in size, then the source (Read/Write) volume can be resized.&#x27;, &#x27;It is recommended that both the target and the source volumes be the same size.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Note&lt;/b&gt;: If you change access status to locked or target all existing iSCSI connections are terminated.&#x27;]
        [&#x27;ModifyVolume is used to modify settings on an existing volume.&#x27;, &#x27;Modifications can be made to one volume at a time and changes take place immediately.&#x27;, &#x27;If an optional parameter is left unspecified, the value will not be changed.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;Extending the size of a volume that is being replicated should be done in an order.&#x27;, &#x27;The target (Replication Target) volume should first be increased in size, then the source (Read/Write) volume can be resized.&#x27;, &#x27;It is recommended that both the target and the source volumes be the same size.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Note&lt;/b&gt;: If you change access status to locked or target all existing iSCSI connections are terminated.&#x27;]
        [&#x27;ModifyVolume is used to modify settings on an existing volume.&#x27;, &#x27;Modifications can be made to one volume at a time and changes take place immediately.&#x27;, &#x27;If an optional parameter is left unspecified, the value will not be changed.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;Extending the size of a volume that is being replicated should be done in an order.&#x27;, &#x27;The target (Replication Target) volume should first be increased in size, then the source (Read/Write) volume can be resized.&#x27;, &#x27;It is recommended that both the target and the source volumes be the same size.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Note&lt;/b&gt;: If you change access status to locked or target all existing iSCSI connections are terminated.&#x27;]
        [&#x27;ModifyVolume is used to modify settings on an existing volume.&#x27;, &#x27;Modifications can be made to one volume at a time and changes take place immediately.&#x27;, &#x27;If an optional parameter is left unspecified, the value will not be changed.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;Extending the size of a volume that is being replicated should be done in an order.&#x27;, &#x27;The target (Replication Target) volume should first be increased in size, then the source (Read/Write) volume can be resized.&#x27;, &#x27;It is recommended that both the target and the source volumes be the same size.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Note&lt;/b&gt;: If you change access status to locked or target all existing iSCSI connections are terminated.&#x27;]
        :param volumeID: [required] VolumeID for the volume to be modified.
        :type volumeID: 
        
        :param accountID:  [&#x27;AccountID to which the volume is reassigned.&#x27;, &#x27;If none is specified, the previous account name is used.&#x27;][&#x27;AccountID to which the volume is reassigned.&#x27;, &#x27;If none is specified, the previous account name is used.&#x27;]
        :type accountID: 
        
        :param access:  [&#x27;Access allowed for the volume.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;readOnly&lt;/b&gt;: Only read operations are allowed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;readWrite&lt;/b&gt;: Reads and writes are allowed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;locked&lt;/b&gt;: No reads or writes are allowed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;replicationTarget&lt;/b&gt;: Identify a volume as the target volume for a paired set of volumes. If the volume is not paired, the access status is locked.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;If unspecified, the access settings of the clone will be the same as the source.&#x27;][&#x27;Access allowed for the volume.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;readOnly&lt;/b&gt;: Only read operations are allowed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;readWrite&lt;/b&gt;: Reads and writes are allowed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;locked&lt;/b&gt;: No reads or writes are allowed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;replicationTarget&lt;/b&gt;: Identify a volume as the target volume for a paired set of volumes. If the volume is not paired, the access status is locked.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;If unspecified, the access settings of the clone will be the same as the source.&#x27;][&#x27;Access allowed for the volume.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;readOnly&lt;/b&gt;: Only read operations are allowed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;readWrite&lt;/b&gt;: Reads and writes are allowed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;locked&lt;/b&gt;: No reads or writes are allowed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;replicationTarget&lt;/b&gt;: Identify a volume as the target volume for a paired set of volumes. If the volume is not paired, the access status is locked.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;If unspecified, the access settings of the clone will be the same as the source.&#x27;][&#x27;Access allowed for the volume.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;readOnly&lt;/b&gt;: Only read operations are allowed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;readWrite&lt;/b&gt;: Reads and writes are allowed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;locked&lt;/b&gt;: No reads or writes are allowed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;replicationTarget&lt;/b&gt;: Identify a volume as the target volume for a paired set of volumes. If the volume is not paired, the access status is locked.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;If unspecified, the access settings of the clone will be the same as the source.&#x27;][&#x27;Access allowed for the volume.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;readOnly&lt;/b&gt;: Only read operations are allowed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;readWrite&lt;/b&gt;: Reads and writes are allowed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;locked&lt;/b&gt;: No reads or writes are allowed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;replicationTarget&lt;/b&gt;: Identify a volume as the target volume for a paired set of volumes. If the volume is not paired, the access status is locked.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;If unspecified, the access settings of the clone will be the same as the source.&#x27;][&#x27;Access allowed for the volume.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;readOnly&lt;/b&gt;: Only read operations are allowed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;readWrite&lt;/b&gt;: Reads and writes are allowed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;locked&lt;/b&gt;: No reads or writes are allowed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;replicationTarget&lt;/b&gt;: Identify a volume as the target volume for a paired set of volumes. If the volume is not paired, the access status is locked.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;If unspecified, the access settings of the clone will be the same as the source.&#x27;][&#x27;Access allowed for the volume.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;readOnly&lt;/b&gt;: Only read operations are allowed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;readWrite&lt;/b&gt;: Reads and writes are allowed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;locked&lt;/b&gt;: No reads or writes are allowed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;replicationTarget&lt;/b&gt;: Identify a volume as the target volume for a paired set of volumes. If the volume is not paired, the access status is locked.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;If unspecified, the access settings of the clone will be the same as the source.&#x27;]
        :type access: 
        
        :param qos:  New quality of service settings for this volume.
        :type qos: 
        
        :param totalSize:  [&#x27;New size of the volume in bytes.&#x27;, &#x27;Size is rounded up to the nearest 1MiB size.&#x27;, &#x27;This parameter can only be used to *increase* the size of a volume.&#x27;][&#x27;New size of the volume in bytes.&#x27;, &#x27;Size is rounded up to the nearest 1MiB size.&#x27;, &#x27;This parameter can only be used to *increase* the size of a volume.&#x27;][&#x27;New size of the volume in bytes.&#x27;, &#x27;Size is rounded up to the nearest 1MiB size.&#x27;, &#x27;This parameter can only be used to *increase* the size of a volume.&#x27;]
        :type totalSize: 
        
        :param attributes:  List of Name/Value pairs in JSON object format.
        :type attributes: 
        """

        params = { 
            "volumeID": volumeID,
        }
        if accountID is not None:
            params["accountID"] = accountID
        if access is not None:
            params["access"] = access
        if qos is not None:
            params["qos"] = qos
        if totalSize is not None:
            params["totalSize"] = totalSize
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
            volumeID,):
        """
        [&#x27;PurgeDeletedVolume immediately and permanently purges a volume which has been deleted.&#x27;, &#x27;A volume must be deleted using DeleteVolume before it can be purged.&#x27;, &#x27;Volumes are purged automatically after a period of time, so usage of this method is not typically required.&#x27;]
        [&#x27;PurgeDeletedVolume immediately and permanently purges a volume which has been deleted.&#x27;, &#x27;A volume must be deleted using DeleteVolume before it can be purged.&#x27;, &#x27;Volumes are purged automatically after a period of time, so usage of this method is not typically required.&#x27;]
        [&#x27;PurgeDeletedVolume immediately and permanently purges a volume which has been deleted.&#x27;, &#x27;A volume must be deleted using DeleteVolume before it can be purged.&#x27;, &#x27;Volumes are purged automatically after a period of time, so usage of this method is not typically required.&#x27;]
        :param volumeID: [required] The ID of the volume to purge.
        :type volumeID: 
        """

        params = { 
            "volumeID": volumeID,
        }
        
        # There is no adaptor.
        return self.send_request(
            'PurgeDeletedVolume',
            PurgeDeletedVolumeResult,
            params
        )

    def restore_deleted_volume(
            self,
            volumeID,):
        """
        [&#x27;RestoreDeletedVolume marks a deleted volume as active again.&#x27;, &#x27;This action makes the volume immediately available for iSCSI connection.&#x27;]
        [&#x27;RestoreDeletedVolume marks a deleted volume as active again.&#x27;, &#x27;This action makes the volume immediately available for iSCSI connection.&#x27;]
        :param volumeID: [required] VolumeID for the deleted volume to restore.
        :type volumeID: 
        """

        params = { 
            "volumeID": volumeID,
        }
        
        # There is no adaptor.
        return self.send_request(
            'RestoreDeletedVolume',
            RestoreDeletedVolumeResult,
            params
        )

    def start_bulk_volume_read(
            self,
            volumeID,
            format,
            snapshotID=OPTIONAL,
            script=OPTIONAL,
            scriptParameters=OPTIONAL,
            attributes=OPTIONAL,):
        """
        [&#x27;StartBulkVolumeRead allows you to initialize a bulk volume read session on a specified volume.&#x27;, &#x27;Only two bulk volume processes can run simultaneously on a volume.&#x27;, &#x27;When you initialize the session, data is read from a SolidFire storage volume for the purposes of storing the data on an external backup source.&#x27;, &#x27;The external data is accessed by a web server running on a SolidFire node.&#x27;, &#x27;Communications and server interaction information for external data access is passed by a script running on the SolidFire storage system.&lt;br/&gt;&#x27;, &#x27;&lt;br/&gt;&#x27;, &#x27;At the start of a bulk volume read operation, a snapshot of the volume is made and the snapshot is deleted when the read has completed.&#x27;, &#x27;You can also read a snapshot of the volume by entering the ID of the snapshot as a parameter.&#x27;, &#x27;Reading a previous snapshot does not create a new snapshot of the volume, nor does the previous snapshot be deleted when the read completes.&lt;br/&gt;&#x27;, &#x27;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Note&lt;/b&gt;: This process creates a new snapshot if the ID of an existing snapshot is not provided.&#x27;, &#x27;Snapshots can be created if cluster fullness is at stage 2 or 3.&#x27;, &#x27;Snapshots are not created when cluster fullness is at stage 4 or 5.&#x27;]
        [&#x27;StartBulkVolumeRead allows you to initialize a bulk volume read session on a specified volume.&#x27;, &#x27;Only two bulk volume processes can run simultaneously on a volume.&#x27;, &#x27;When you initialize the session, data is read from a SolidFire storage volume for the purposes of storing the data on an external backup source.&#x27;, &#x27;The external data is accessed by a web server running on a SolidFire node.&#x27;, &#x27;Communications and server interaction information for external data access is passed by a script running on the SolidFire storage system.&lt;br/&gt;&#x27;, &#x27;&lt;br/&gt;&#x27;, &#x27;At the start of a bulk volume read operation, a snapshot of the volume is made and the snapshot is deleted when the read has completed.&#x27;, &#x27;You can also read a snapshot of the volume by entering the ID of the snapshot as a parameter.&#x27;, &#x27;Reading a previous snapshot does not create a new snapshot of the volume, nor does the previous snapshot be deleted when the read completes.&lt;br/&gt;&#x27;, &#x27;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Note&lt;/b&gt;: This process creates a new snapshot if the ID of an existing snapshot is not provided.&#x27;, &#x27;Snapshots can be created if cluster fullness is at stage 2 or 3.&#x27;, &#x27;Snapshots are not created when cluster fullness is at stage 4 or 5.&#x27;]
        [&#x27;StartBulkVolumeRead allows you to initialize a bulk volume read session on a specified volume.&#x27;, &#x27;Only two bulk volume processes can run simultaneously on a volume.&#x27;, &#x27;When you initialize the session, data is read from a SolidFire storage volume for the purposes of storing the data on an external backup source.&#x27;, &#x27;The external data is accessed by a web server running on a SolidFire node.&#x27;, &#x27;Communications and server interaction information for external data access is passed by a script running on the SolidFire storage system.&lt;br/&gt;&#x27;, &#x27;&lt;br/&gt;&#x27;, &#x27;At the start of a bulk volume read operation, a snapshot of the volume is made and the snapshot is deleted when the read has completed.&#x27;, &#x27;You can also read a snapshot of the volume by entering the ID of the snapshot as a parameter.&#x27;, &#x27;Reading a previous snapshot does not create a new snapshot of the volume, nor does the previous snapshot be deleted when the read completes.&lt;br/&gt;&#x27;, &#x27;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Note&lt;/b&gt;: This process creates a new snapshot if the ID of an existing snapshot is not provided.&#x27;, &#x27;Snapshots can be created if cluster fullness is at stage 2 or 3.&#x27;, &#x27;Snapshots are not created when cluster fullness is at stage 4 or 5.&#x27;]
        [&#x27;StartBulkVolumeRead allows you to initialize a bulk volume read session on a specified volume.&#x27;, &#x27;Only two bulk volume processes can run simultaneously on a volume.&#x27;, &#x27;When you initialize the session, data is read from a SolidFire storage volume for the purposes of storing the data on an external backup source.&#x27;, &#x27;The external data is accessed by a web server running on a SolidFire node.&#x27;, &#x27;Communications and server interaction information for external data access is passed by a script running on the SolidFire storage system.&lt;br/&gt;&#x27;, &#x27;&lt;br/&gt;&#x27;, &#x27;At the start of a bulk volume read operation, a snapshot of the volume is made and the snapshot is deleted when the read has completed.&#x27;, &#x27;You can also read a snapshot of the volume by entering the ID of the snapshot as a parameter.&#x27;, &#x27;Reading a previous snapshot does not create a new snapshot of the volume, nor does the previous snapshot be deleted when the read completes.&lt;br/&gt;&#x27;, &#x27;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Note&lt;/b&gt;: This process creates a new snapshot if the ID of an existing snapshot is not provided.&#x27;, &#x27;Snapshots can be created if cluster fullness is at stage 2 or 3.&#x27;, &#x27;Snapshots are not created when cluster fullness is at stage 4 or 5.&#x27;]
        [&#x27;StartBulkVolumeRead allows you to initialize a bulk volume read session on a specified volume.&#x27;, &#x27;Only two bulk volume processes can run simultaneously on a volume.&#x27;, &#x27;When you initialize the session, data is read from a SolidFire storage volume for the purposes of storing the data on an external backup source.&#x27;, &#x27;The external data is accessed by a web server running on a SolidFire node.&#x27;, &#x27;Communications and server interaction information for external data access is passed by a script running on the SolidFire storage system.&lt;br/&gt;&#x27;, &#x27;&lt;br/&gt;&#x27;, &#x27;At the start of a bulk volume read operation, a snapshot of the volume is made and the snapshot is deleted when the read has completed.&#x27;, &#x27;You can also read a snapshot of the volume by entering the ID of the snapshot as a parameter.&#x27;, &#x27;Reading a previous snapshot does not create a new snapshot of the volume, nor does the previous snapshot be deleted when the read completes.&lt;br/&gt;&#x27;, &#x27;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Note&lt;/b&gt;: This process creates a new snapshot if the ID of an existing snapshot is not provided.&#x27;, &#x27;Snapshots can be created if cluster fullness is at stage 2 or 3.&#x27;, &#x27;Snapshots are not created when cluster fullness is at stage 4 or 5.&#x27;]
        [&#x27;StartBulkVolumeRead allows you to initialize a bulk volume read session on a specified volume.&#x27;, &#x27;Only two bulk volume processes can run simultaneously on a volume.&#x27;, &#x27;When you initialize the session, data is read from a SolidFire storage volume for the purposes of storing the data on an external backup source.&#x27;, &#x27;The external data is accessed by a web server running on a SolidFire node.&#x27;, &#x27;Communications and server interaction information for external data access is passed by a script running on the SolidFire storage system.&lt;br/&gt;&#x27;, &#x27;&lt;br/&gt;&#x27;, &#x27;At the start of a bulk volume read operation, a snapshot of the volume is made and the snapshot is deleted when the read has completed.&#x27;, &#x27;You can also read a snapshot of the volume by entering the ID of the snapshot as a parameter.&#x27;, &#x27;Reading a previous snapshot does not create a new snapshot of the volume, nor does the previous snapshot be deleted when the read completes.&lt;br/&gt;&#x27;, &#x27;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Note&lt;/b&gt;: This process creates a new snapshot if the ID of an existing snapshot is not provided.&#x27;, &#x27;Snapshots can be created if cluster fullness is at stage 2 or 3.&#x27;, &#x27;Snapshots are not created when cluster fullness is at stage 4 or 5.&#x27;]
        [&#x27;StartBulkVolumeRead allows you to initialize a bulk volume read session on a specified volume.&#x27;, &#x27;Only two bulk volume processes can run simultaneously on a volume.&#x27;, &#x27;When you initialize the session, data is read from a SolidFire storage volume for the purposes of storing the data on an external backup source.&#x27;, &#x27;The external data is accessed by a web server running on a SolidFire node.&#x27;, &#x27;Communications and server interaction information for external data access is passed by a script running on the SolidFire storage system.&lt;br/&gt;&#x27;, &#x27;&lt;br/&gt;&#x27;, &#x27;At the start of a bulk volume read operation, a snapshot of the volume is made and the snapshot is deleted when the read has completed.&#x27;, &#x27;You can also read a snapshot of the volume by entering the ID of the snapshot as a parameter.&#x27;, &#x27;Reading a previous snapshot does not create a new snapshot of the volume, nor does the previous snapshot be deleted when the read completes.&lt;br/&gt;&#x27;, &#x27;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Note&lt;/b&gt;: This process creates a new snapshot if the ID of an existing snapshot is not provided.&#x27;, &#x27;Snapshots can be created if cluster fullness is at stage 2 or 3.&#x27;, &#x27;Snapshots are not created when cluster fullness is at stage 4 or 5.&#x27;]
        [&#x27;StartBulkVolumeRead allows you to initialize a bulk volume read session on a specified volume.&#x27;, &#x27;Only two bulk volume processes can run simultaneously on a volume.&#x27;, &#x27;When you initialize the session, data is read from a SolidFire storage volume for the purposes of storing the data on an external backup source.&#x27;, &#x27;The external data is accessed by a web server running on a SolidFire node.&#x27;, &#x27;Communications and server interaction information for external data access is passed by a script running on the SolidFire storage system.&lt;br/&gt;&#x27;, &#x27;&lt;br/&gt;&#x27;, &#x27;At the start of a bulk volume read operation, a snapshot of the volume is made and the snapshot is deleted when the read has completed.&#x27;, &#x27;You can also read a snapshot of the volume by entering the ID of the snapshot as a parameter.&#x27;, &#x27;Reading a previous snapshot does not create a new snapshot of the volume, nor does the previous snapshot be deleted when the read completes.&lt;br/&gt;&#x27;, &#x27;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Note&lt;/b&gt;: This process creates a new snapshot if the ID of an existing snapshot is not provided.&#x27;, &#x27;Snapshots can be created if cluster fullness is at stage 2 or 3.&#x27;, &#x27;Snapshots are not created when cluster fullness is at stage 4 or 5.&#x27;]
        [&#x27;StartBulkVolumeRead allows you to initialize a bulk volume read session on a specified volume.&#x27;, &#x27;Only two bulk volume processes can run simultaneously on a volume.&#x27;, &#x27;When you initialize the session, data is read from a SolidFire storage volume for the purposes of storing the data on an external backup source.&#x27;, &#x27;The external data is accessed by a web server running on a SolidFire node.&#x27;, &#x27;Communications and server interaction information for external data access is passed by a script running on the SolidFire storage system.&lt;br/&gt;&#x27;, &#x27;&lt;br/&gt;&#x27;, &#x27;At the start of a bulk volume read operation, a snapshot of the volume is made and the snapshot is deleted when the read has completed.&#x27;, &#x27;You can also read a snapshot of the volume by entering the ID of the snapshot as a parameter.&#x27;, &#x27;Reading a previous snapshot does not create a new snapshot of the volume, nor does the previous snapshot be deleted when the read completes.&lt;br/&gt;&#x27;, &#x27;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Note&lt;/b&gt;: This process creates a new snapshot if the ID of an existing snapshot is not provided.&#x27;, &#x27;Snapshots can be created if cluster fullness is at stage 2 or 3.&#x27;, &#x27;Snapshots are not created when cluster fullness is at stage 4 or 5.&#x27;]
        [&#x27;StartBulkVolumeRead allows you to initialize a bulk volume read session on a specified volume.&#x27;, &#x27;Only two bulk volume processes can run simultaneously on a volume.&#x27;, &#x27;When you initialize the session, data is read from a SolidFire storage volume for the purposes of storing the data on an external backup source.&#x27;, &#x27;The external data is accessed by a web server running on a SolidFire node.&#x27;, &#x27;Communications and server interaction information for external data access is passed by a script running on the SolidFire storage system.&lt;br/&gt;&#x27;, &#x27;&lt;br/&gt;&#x27;, &#x27;At the start of a bulk volume read operation, a snapshot of the volume is made and the snapshot is deleted when the read has completed.&#x27;, &#x27;You can also read a snapshot of the volume by entering the ID of the snapshot as a parameter.&#x27;, &#x27;Reading a previous snapshot does not create a new snapshot of the volume, nor does the previous snapshot be deleted when the read completes.&lt;br/&gt;&#x27;, &#x27;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Note&lt;/b&gt;: This process creates a new snapshot if the ID of an existing snapshot is not provided.&#x27;, &#x27;Snapshots can be created if cluster fullness is at stage 2 or 3.&#x27;, &#x27;Snapshots are not created when cluster fullness is at stage 4 or 5.&#x27;]
        [&#x27;StartBulkVolumeRead allows you to initialize a bulk volume read session on a specified volume.&#x27;, &#x27;Only two bulk volume processes can run simultaneously on a volume.&#x27;, &#x27;When you initialize the session, data is read from a SolidFire storage volume for the purposes of storing the data on an external backup source.&#x27;, &#x27;The external data is accessed by a web server running on a SolidFire node.&#x27;, &#x27;Communications and server interaction information for external data access is passed by a script running on the SolidFire storage system.&lt;br/&gt;&#x27;, &#x27;&lt;br/&gt;&#x27;, &#x27;At the start of a bulk volume read operation, a snapshot of the volume is made and the snapshot is deleted when the read has completed.&#x27;, &#x27;You can also read a snapshot of the volume by entering the ID of the snapshot as a parameter.&#x27;, &#x27;Reading a previous snapshot does not create a new snapshot of the volume, nor does the previous snapshot be deleted when the read completes.&lt;br/&gt;&#x27;, &#x27;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Note&lt;/b&gt;: This process creates a new snapshot if the ID of an existing snapshot is not provided.&#x27;, &#x27;Snapshots can be created if cluster fullness is at stage 2 or 3.&#x27;, &#x27;Snapshots are not created when cluster fullness is at stage 4 or 5.&#x27;]
        [&#x27;StartBulkVolumeRead allows you to initialize a bulk volume read session on a specified volume.&#x27;, &#x27;Only two bulk volume processes can run simultaneously on a volume.&#x27;, &#x27;When you initialize the session, data is read from a SolidFire storage volume for the purposes of storing the data on an external backup source.&#x27;, &#x27;The external data is accessed by a web server running on a SolidFire node.&#x27;, &#x27;Communications and server interaction information for external data access is passed by a script running on the SolidFire storage system.&lt;br/&gt;&#x27;, &#x27;&lt;br/&gt;&#x27;, &#x27;At the start of a bulk volume read operation, a snapshot of the volume is made and the snapshot is deleted when the read has completed.&#x27;, &#x27;You can also read a snapshot of the volume by entering the ID of the snapshot as a parameter.&#x27;, &#x27;Reading a previous snapshot does not create a new snapshot of the volume, nor does the previous snapshot be deleted when the read completes.&lt;br/&gt;&#x27;, &#x27;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Note&lt;/b&gt;: This process creates a new snapshot if the ID of an existing snapshot is not provided.&#x27;, &#x27;Snapshots can be created if cluster fullness is at stage 2 or 3.&#x27;, &#x27;Snapshots are not created when cluster fullness is at stage 4 or 5.&#x27;]
        [&#x27;StartBulkVolumeRead allows you to initialize a bulk volume read session on a specified volume.&#x27;, &#x27;Only two bulk volume processes can run simultaneously on a volume.&#x27;, &#x27;When you initialize the session, data is read from a SolidFire storage volume for the purposes of storing the data on an external backup source.&#x27;, &#x27;The external data is accessed by a web server running on a SolidFire node.&#x27;, &#x27;Communications and server interaction information for external data access is passed by a script running on the SolidFire storage system.&lt;br/&gt;&#x27;, &#x27;&lt;br/&gt;&#x27;, &#x27;At the start of a bulk volume read operation, a snapshot of the volume is made and the snapshot is deleted when the read has completed.&#x27;, &#x27;You can also read a snapshot of the volume by entering the ID of the snapshot as a parameter.&#x27;, &#x27;Reading a previous snapshot does not create a new snapshot of the volume, nor does the previous snapshot be deleted when the read completes.&lt;br/&gt;&#x27;, &#x27;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Note&lt;/b&gt;: This process creates a new snapshot if the ID of an existing snapshot is not provided.&#x27;, &#x27;Snapshots can be created if cluster fullness is at stage 2 or 3.&#x27;, &#x27;Snapshots are not created when cluster fullness is at stage 4 or 5.&#x27;]
        :param volumeID: [required] ID of the volume to be read.
        :type volumeID: 
        
        :param format: [required] [&#x27;The format of the volume data. Can be either:&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;uncompressed&lt;/b&gt;: every byte of the volume is returned without any compression.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;native&lt;/b&gt;: opaque data is returned that is smaller and more efficiently stored and written on a subsequent bulk volume write.&#x27;][&#x27;The format of the volume data. Can be either:&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;uncompressed&lt;/b&gt;: every byte of the volume is returned without any compression.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;native&lt;/b&gt;: opaque data is returned that is smaller and more efficiently stored and written on a subsequent bulk volume write.&#x27;][&#x27;The format of the volume data. Can be either:&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;uncompressed&lt;/b&gt;: every byte of the volume is returned without any compression.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;native&lt;/b&gt;: opaque data is returned that is smaller and more efficiently stored and written on a subsequent bulk volume write.&#x27;]
        :type format: 
        
        :param snapshotID:  [&#x27;ID of a previously created snapshot used for bulk volume reads.&#x27;, &#x27;If no ID is entered, a snapshot of the current active volume image is made.&#x27;][&#x27;ID of a previously created snapshot used for bulk volume reads.&#x27;, &#x27;If no ID is entered, a snapshot of the current active volume image is made.&#x27;]
        :type snapshotID: 
        
        :param script:  [&#x27;Executable name of a script.&#x27;, &#x27;If no script name is given then the key and URL is necessary to access SolidFire nodes.&#x27;, &#x27;The script is run on the primary node and the key and URL is returned to the script so the local web server can be contacted.&#x27;][&#x27;Executable name of a script.&#x27;, &#x27;If no script name is given then the key and URL is necessary to access SolidFire nodes.&#x27;, &#x27;The script is run on the primary node and the key and URL is returned to the script so the local web server can be contacted.&#x27;][&#x27;Executable name of a script.&#x27;, &#x27;If no script name is given then the key and URL is necessary to access SolidFire nodes.&#x27;, &#x27;The script is run on the primary node and the key and URL is returned to the script so the local web server can be contacted.&#x27;]
        :type script: 
        
        :param scriptParameters:  [&#x27;JSON parameters to pass to the script.&#x27;]
        :type scriptParameters: 
        
        :param attributes:  [&#x27;JSON attributes for the bulk volume job.&#x27;]
        :type attributes: 
        """

        params = { 
            "volumeID": volumeID,
            "format": format,
        }
        if snapshotID is not None:
            params["snapshotID"] = snapshotID
        if script is not None:
            params["script"] = script
        if scriptParameters is not None:
            params["scriptParameters"] = scriptParameters
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
            volumeID,
            format,
            script=OPTIONAL,
            scriptParameters=OPTIONAL,
            attributes=OPTIONAL,):
        """
        [&#x27;StartBulkVolumeWrite allows you to initialize a bulk volume write session on a specified volume.&#x27;, &#x27;Only two bulk volume processes can run simultaneously on a volume.&#x27;, &#x27;When the session is initialized, data can be written to a SolidFire storage volume from an external backup source.&#x27;, &#x27;The external data is accessed by a web server running on a SolidFire node.&#x27;, &#x27;Communications and server interaction information for external data access is passed by a script running on the SolidFire storage system.&#x27;]
        [&#x27;StartBulkVolumeWrite allows you to initialize a bulk volume write session on a specified volume.&#x27;, &#x27;Only two bulk volume processes can run simultaneously on a volume.&#x27;, &#x27;When the session is initialized, data can be written to a SolidFire storage volume from an external backup source.&#x27;, &#x27;The external data is accessed by a web server running on a SolidFire node.&#x27;, &#x27;Communications and server interaction information for external data access is passed by a script running on the SolidFire storage system.&#x27;]
        [&#x27;StartBulkVolumeWrite allows you to initialize a bulk volume write session on a specified volume.&#x27;, &#x27;Only two bulk volume processes can run simultaneously on a volume.&#x27;, &#x27;When the session is initialized, data can be written to a SolidFire storage volume from an external backup source.&#x27;, &#x27;The external data is accessed by a web server running on a SolidFire node.&#x27;, &#x27;Communications and server interaction information for external data access is passed by a script running on the SolidFire storage system.&#x27;]
        [&#x27;StartBulkVolumeWrite allows you to initialize a bulk volume write session on a specified volume.&#x27;, &#x27;Only two bulk volume processes can run simultaneously on a volume.&#x27;, &#x27;When the session is initialized, data can be written to a SolidFire storage volume from an external backup source.&#x27;, &#x27;The external data is accessed by a web server running on a SolidFire node.&#x27;, &#x27;Communications and server interaction information for external data access is passed by a script running on the SolidFire storage system.&#x27;]
        [&#x27;StartBulkVolumeWrite allows you to initialize a bulk volume write session on a specified volume.&#x27;, &#x27;Only two bulk volume processes can run simultaneously on a volume.&#x27;, &#x27;When the session is initialized, data can be written to a SolidFire storage volume from an external backup source.&#x27;, &#x27;The external data is accessed by a web server running on a SolidFire node.&#x27;, &#x27;Communications and server interaction information for external data access is passed by a script running on the SolidFire storage system.&#x27;]
        :param volumeID: [required] ID of the volume to be written to.
        :type volumeID: 
        
        :param format: [required] [&#x27;The format of the volume data. Can be either:&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;uncompressed&lt;/b&gt;: every byte of the volume is returned without any compression.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;native&lt;/b&gt;: opaque data is returned that is smaller and more efficiently stored and written on a subsequent bulk volume write&#x27;][&#x27;The format of the volume data. Can be either:&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;uncompressed&lt;/b&gt;: every byte of the volume is returned without any compression.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;native&lt;/b&gt;: opaque data is returned that is smaller and more efficiently stored and written on a subsequent bulk volume write&#x27;][&#x27;The format of the volume data. Can be either:&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;uncompressed&lt;/b&gt;: every byte of the volume is returned without any compression.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;native&lt;/b&gt;: opaque data is returned that is smaller and more efficiently stored and written on a subsequent bulk volume write&#x27;]
        :type format: 
        
        :param script:  [&#x27;Executable name of a script.&#x27;, &#x27;If no script name is given then the key and URL are necessary to access SolidFire nodes.&#x27;, &#x27;The script runs on the primary node and the key and URL is returned to the script so the local web server can be contacted.&#x27;][&#x27;Executable name of a script.&#x27;, &#x27;If no script name is given then the key and URL are necessary to access SolidFire nodes.&#x27;, &#x27;The script runs on the primary node and the key and URL is returned to the script so the local web server can be contacted.&#x27;][&#x27;Executable name of a script.&#x27;, &#x27;If no script name is given then the key and URL are necessary to access SolidFire nodes.&#x27;, &#x27;The script runs on the primary node and the key and URL is returned to the script so the local web server can be contacted.&#x27;]
        :type script: 
        
        :param scriptParameters:  [&#x27;JSON parameters to pass to the script.&#x27;]
        :type scriptParameters: 
        
        :param attributes:  [&#x27;JSON attributes for the bulk volume job.&#x27;]
        :type attributes: 
        """

        params = { 
            "volumeID": volumeID,
            "format": format,
        }
        if script is not None:
            params["script"] = script
        if scriptParameters is not None:
            params["scriptParameters"] = scriptParameters
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
            percentComplete=OPTIONAL,
            message=OPTIONAL,
            attributes=OPTIONAL,):
        """
        [&#x27;You can use UpdateBulkVolumeStatus in a script to return to the SolidFire system the status of a bulk volume job that you have started with the &quot;StartBulkVolumeRead&quot; or &quot;StartBulkVolumeWrite&quot; methods.&#x27;]
        :param key: [required] The key assigned during initialization of a &quot;StartBulkVolumeRead&quot; or &quot;StartBulkVolumeWrite&quot; session.
        :type key: 
        
        :param status: [required] [&#x27;The SolidFire system sets the status of the given bulk volume job.&lt;br/&gt;&#x27;, &#x27;Possible values:&lt;br/&gt;&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;running&lt;/b&gt;: jobs that are still active.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;complete&lt;/b&gt;: jobs that are done. failed - jobs that have failed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;failed&lt;/b&gt;: jobs that have failed.&#x27;][&#x27;The SolidFire system sets the status of the given bulk volume job.&lt;br/&gt;&#x27;, &#x27;Possible values:&lt;br/&gt;&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;running&lt;/b&gt;: jobs that are still active.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;complete&lt;/b&gt;: jobs that are done. failed - jobs that have failed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;failed&lt;/b&gt;: jobs that have failed.&#x27;][&#x27;The SolidFire system sets the status of the given bulk volume job.&lt;br/&gt;&#x27;, &#x27;Possible values:&lt;br/&gt;&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;running&lt;/b&gt;: jobs that are still active.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;complete&lt;/b&gt;: jobs that are done. failed - jobs that have failed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;failed&lt;/b&gt;: jobs that have failed.&#x27;][&#x27;The SolidFire system sets the status of the given bulk volume job.&lt;br/&gt;&#x27;, &#x27;Possible values:&lt;br/&gt;&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;running&lt;/b&gt;: jobs that are still active.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;complete&lt;/b&gt;: jobs that are done. failed - jobs that have failed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;failed&lt;/b&gt;: jobs that have failed.&#x27;][&#x27;The SolidFire system sets the status of the given bulk volume job.&lt;br/&gt;&#x27;, &#x27;Possible values:&lt;br/&gt;&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;running&lt;/b&gt;: jobs that are still active.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;complete&lt;/b&gt;: jobs that are done. failed - jobs that have failed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;failed&lt;/b&gt;: jobs that have failed.&#x27;]
        :type status: 
        
        :param percentComplete:  [&#x27;The completed progress of the bulk volume job as a percentage.&#x27;]
        :type percentComplete: 
        
        :param message:  [&#x27;Returns the status of the bulk volume job when the job has completed.&#x27;]
        :type message: 
        
        :param attributes:  [&#x27;JSON attributes  updates what is on the bulk volume job.&#x27;]
        :type attributes: 
        """

        params = { 
            "key": key,
            "status": status,
        }
        if percentComplete is not None:
            params["percentComplete"] = percentComplete
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
            virtualNetworkID=OPTIONAL,
            virtualNetworkTags=OPTIONAL,
            attributes=OPTIONAL,):
        """
        [&#x27;Creates a new volume access group.&#x27;, &#x27;The new volume access group must be given a name when it is created.&#x27;, &#x27;Entering initiators and volumes are optional when creating a volume access group.&#x27;, &#x27;Once the group is created volumes and initiator IQNs can be added.&#x27;, &#x27;Any initiator IQN that is successfully added to the volume access group is able to access any volume in the group without CHAP authentication.&#x27;]
        [&#x27;Creates a new volume access group.&#x27;, &#x27;The new volume access group must be given a name when it is created.&#x27;, &#x27;Entering initiators and volumes are optional when creating a volume access group.&#x27;, &#x27;Once the group is created volumes and initiator IQNs can be added.&#x27;, &#x27;Any initiator IQN that is successfully added to the volume access group is able to access any volume in the group without CHAP authentication.&#x27;]
        [&#x27;Creates a new volume access group.&#x27;, &#x27;The new volume access group must be given a name when it is created.&#x27;, &#x27;Entering initiators and volumes are optional when creating a volume access group.&#x27;, &#x27;Once the group is created volumes and initiator IQNs can be added.&#x27;, &#x27;Any initiator IQN that is successfully added to the volume access group is able to access any volume in the group without CHAP authentication.&#x27;]
        [&#x27;Creates a new volume access group.&#x27;, &#x27;The new volume access group must be given a name when it is created.&#x27;, &#x27;Entering initiators and volumes are optional when creating a volume access group.&#x27;, &#x27;Once the group is created volumes and initiator IQNs can be added.&#x27;, &#x27;Any initiator IQN that is successfully added to the volume access group is able to access any volume in the group without CHAP authentication.&#x27;]
        [&#x27;Creates a new volume access group.&#x27;, &#x27;The new volume access group must be given a name when it is created.&#x27;, &#x27;Entering initiators and volumes are optional when creating a volume access group.&#x27;, &#x27;Once the group is created volumes and initiator IQNs can be added.&#x27;, &#x27;Any initiator IQN that is successfully added to the volume access group is able to access any volume in the group without CHAP authentication.&#x27;]
        :param name: [required] [&#x27;Name of the volume access group.&#x27;, &#x27;It is not required to be unique, but recommended.&#x27;][&#x27;Name of the volume access group.&#x27;, &#x27;It is not required to be unique, but recommended.&#x27;]
        :type name: 
        
        :param initiators:  [&#x27;List of initiators to include in the volume access group.&#x27;, &#x27;If unspecified, the access group will start out without configured initiators.&#x27;][&#x27;List of initiators to include in the volume access group.&#x27;, &#x27;If unspecified, the access group will start out without configured initiators.&#x27;]
        :type initiators: 
        
        :param volumes:  [&#x27;List of volumes to initially include in the volume access group.&#x27;, &#x27;If unspecified, the access group will start without any volumes.&#x27;][&#x27;List of volumes to initially include in the volume access group.&#x27;, &#x27;If unspecified, the access group will start without any volumes.&#x27;]
        :type volumes: 
        
        :param virtualNetworkID:  The ID of the SolidFire Virtual Network ID to associate the volume access group with.
        :type virtualNetworkID: 
        
        :param virtualNetworkTags:  The ID of the VLAN Virtual Network Tag to associate the volume access group with.
        :type virtualNetworkTags: 
        
        :param attributes:  List of Name/Value pairs in JSON object format.
        :type attributes: 
        """

        params = { 
            "name": name,
        }
        if initiators is not None:
            params["initiators"] = initiators
        if volumes is not None:
            params["volumes"] = volumes
        if virtualNetworkID is not None:
            params["virtualNetworkID"] = virtualNetworkID
        if virtualNetworkTags is not None:
            params["virtualNetworkTags"] = virtualNetworkTags
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
            startVolumeAccessGroupID=OPTIONAL,
            limit=OPTIONAL,):
        """
        [&#x27;ListVolumeAccessGroups is used to return information about the volume access groups that are currently in the system.&#x27;]
        :param startVolumeAccessGroupID:  [&#x27;The lowest VolumeAccessGroupID to return.&#x27;, &#x27;This can be useful for paging.&#x27;, &#x27;If unspecified, there is no lower limit (implicitly 0).&#x27;][&#x27;The lowest VolumeAccessGroupID to return.&#x27;, &#x27;This can be useful for paging.&#x27;, &#x27;If unspecified, there is no lower limit (implicitly 0).&#x27;][&#x27;The lowest VolumeAccessGroupID to return.&#x27;, &#x27;This can be useful for paging.&#x27;, &#x27;If unspecified, there is no lower limit (implicitly 0).&#x27;]
        :type startVolumeAccessGroupID: 
        
        :param limit:  [&#x27;The maximum number of results to return.&#x27;, &#x27;This can be useful for paging.&#x27;][&#x27;The maximum number of results to return.&#x27;, &#x27;This can be useful for paging.&#x27;]
        :type limit: 
        """

        params = { 
        }
        if startVolumeAccessGroupID is not None:
            params["startVolumeAccessGroupID"] = startVolumeAccessGroupID
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
            volumeAccessGroupID,):
        """
        Delete a volume access group from the system.
        :param volumeAccessGroupID: [required] [&#x27;The ID of the volume access group to delete.&#x27;]
        :type volumeAccessGroupID: 
        """

        params = { 
            "volumeAccessGroupID": volumeAccessGroupID,
        }
        
        # There is no adaptor.
        return self.send_request(
            'DeleteVolumeAccessGroup',
            DeleteVolumeAccessGroupResult,
            params
        )

    def modify_volume_access_group(
            self,
            volumeAccessGroupID,
            virtualNetworkID=OPTIONAL,
            virtualNetworkTags=OPTIONAL,
            name=OPTIONAL,
            initiators=OPTIONAL,
            volumes=OPTIONAL,
            attributes=OPTIONAL,):
        """
        [&#x27;Update initiators and add or remove volumes from a volume access group.&#x27;, &#x27;A specified initiator or volume that duplicates an existing volume or initiator in a volume access group is left as-is.&#x27;, &#x27;If a value is not specified for volumes or initiators, the current list of initiators and volumes are not changed.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;Often, it is easier to use the convenience functions to modify initiators and volumes independently:&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;AddInitiatorsToVolumeAccessGroup&lt;br/&gt;&#x27;, &#x27;RemoveInitiatorsFromVolumeAccessGroup&lt;br/&gt;&#x27;, &#x27;AddVolumesToVolumeAccessGroup&lt;br/&gt;&#x27;, &#x27;RemoveVolumesFromVolumeAccessGroup&lt;br/&gt;&#x27;]
        [&#x27;Update initiators and add or remove volumes from a volume access group.&#x27;, &#x27;A specified initiator or volume that duplicates an existing volume or initiator in a volume access group is left as-is.&#x27;, &#x27;If a value is not specified for volumes or initiators, the current list of initiators and volumes are not changed.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;Often, it is easier to use the convenience functions to modify initiators and volumes independently:&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;AddInitiatorsToVolumeAccessGroup&lt;br/&gt;&#x27;, &#x27;RemoveInitiatorsFromVolumeAccessGroup&lt;br/&gt;&#x27;, &#x27;AddVolumesToVolumeAccessGroup&lt;br/&gt;&#x27;, &#x27;RemoveVolumesFromVolumeAccessGroup&lt;br/&gt;&#x27;]
        [&#x27;Update initiators and add or remove volumes from a volume access group.&#x27;, &#x27;A specified initiator or volume that duplicates an existing volume or initiator in a volume access group is left as-is.&#x27;, &#x27;If a value is not specified for volumes or initiators, the current list of initiators and volumes are not changed.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;Often, it is easier to use the convenience functions to modify initiators and volumes independently:&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;AddInitiatorsToVolumeAccessGroup&lt;br/&gt;&#x27;, &#x27;RemoveInitiatorsFromVolumeAccessGroup&lt;br/&gt;&#x27;, &#x27;AddVolumesToVolumeAccessGroup&lt;br/&gt;&#x27;, &#x27;RemoveVolumesFromVolumeAccessGroup&lt;br/&gt;&#x27;]
        [&#x27;Update initiators and add or remove volumes from a volume access group.&#x27;, &#x27;A specified initiator or volume that duplicates an existing volume or initiator in a volume access group is left as-is.&#x27;, &#x27;If a value is not specified for volumes or initiators, the current list of initiators and volumes are not changed.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;Often, it is easier to use the convenience functions to modify initiators and volumes independently:&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;AddInitiatorsToVolumeAccessGroup&lt;br/&gt;&#x27;, &#x27;RemoveInitiatorsFromVolumeAccessGroup&lt;br/&gt;&#x27;, &#x27;AddVolumesToVolumeAccessGroup&lt;br/&gt;&#x27;, &#x27;RemoveVolumesFromVolumeAccessGroup&lt;br/&gt;&#x27;]
        [&#x27;Update initiators and add or remove volumes from a volume access group.&#x27;, &#x27;A specified initiator or volume that duplicates an existing volume or initiator in a volume access group is left as-is.&#x27;, &#x27;If a value is not specified for volumes or initiators, the current list of initiators and volumes are not changed.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;Often, it is easier to use the convenience functions to modify initiators and volumes independently:&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;AddInitiatorsToVolumeAccessGroup&lt;br/&gt;&#x27;, &#x27;RemoveInitiatorsFromVolumeAccessGroup&lt;br/&gt;&#x27;, &#x27;AddVolumesToVolumeAccessGroup&lt;br/&gt;&#x27;, &#x27;RemoveVolumesFromVolumeAccessGroup&lt;br/&gt;&#x27;]
        [&#x27;Update initiators and add or remove volumes from a volume access group.&#x27;, &#x27;A specified initiator or volume that duplicates an existing volume or initiator in a volume access group is left as-is.&#x27;, &#x27;If a value is not specified for volumes or initiators, the current list of initiators and volumes are not changed.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;Often, it is easier to use the convenience functions to modify initiators and volumes independently:&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;AddInitiatorsToVolumeAccessGroup&lt;br/&gt;&#x27;, &#x27;RemoveInitiatorsFromVolumeAccessGroup&lt;br/&gt;&#x27;, &#x27;AddVolumesToVolumeAccessGroup&lt;br/&gt;&#x27;, &#x27;RemoveVolumesFromVolumeAccessGroup&lt;br/&gt;&#x27;]
        [&#x27;Update initiators and add or remove volumes from a volume access group.&#x27;, &#x27;A specified initiator or volume that duplicates an existing volume or initiator in a volume access group is left as-is.&#x27;, &#x27;If a value is not specified for volumes or initiators, the current list of initiators and volumes are not changed.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;Often, it is easier to use the convenience functions to modify initiators and volumes independently:&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;AddInitiatorsToVolumeAccessGroup&lt;br/&gt;&#x27;, &#x27;RemoveInitiatorsFromVolumeAccessGroup&lt;br/&gt;&#x27;, &#x27;AddVolumesToVolumeAccessGroup&lt;br/&gt;&#x27;, &#x27;RemoveVolumesFromVolumeAccessGroup&lt;br/&gt;&#x27;]
        [&#x27;Update initiators and add or remove volumes from a volume access group.&#x27;, &#x27;A specified initiator or volume that duplicates an existing volume or initiator in a volume access group is left as-is.&#x27;, &#x27;If a value is not specified for volumes or initiators, the current list of initiators and volumes are not changed.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;Often, it is easier to use the convenience functions to modify initiators and volumes independently:&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;AddInitiatorsToVolumeAccessGroup&lt;br/&gt;&#x27;, &#x27;RemoveInitiatorsFromVolumeAccessGroup&lt;br/&gt;&#x27;, &#x27;AddVolumesToVolumeAccessGroup&lt;br/&gt;&#x27;, &#x27;RemoveVolumesFromVolumeAccessGroup&lt;br/&gt;&#x27;]
        [&#x27;Update initiators and add or remove volumes from a volume access group.&#x27;, &#x27;A specified initiator or volume that duplicates an existing volume or initiator in a volume access group is left as-is.&#x27;, &#x27;If a value is not specified for volumes or initiators, the current list of initiators and volumes are not changed.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;Often, it is easier to use the convenience functions to modify initiators and volumes independently:&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;AddInitiatorsToVolumeAccessGroup&lt;br/&gt;&#x27;, &#x27;RemoveInitiatorsFromVolumeAccessGroup&lt;br/&gt;&#x27;, &#x27;AddVolumesToVolumeAccessGroup&lt;br/&gt;&#x27;, &#x27;RemoveVolumesFromVolumeAccessGroup&lt;br/&gt;&#x27;]
        [&#x27;Update initiators and add or remove volumes from a volume access group.&#x27;, &#x27;A specified initiator or volume that duplicates an existing volume or initiator in a volume access group is left as-is.&#x27;, &#x27;If a value is not specified for volumes or initiators, the current list of initiators and volumes are not changed.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;Often, it is easier to use the convenience functions to modify initiators and volumes independently:&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;AddInitiatorsToVolumeAccessGroup&lt;br/&gt;&#x27;, &#x27;RemoveInitiatorsFromVolumeAccessGroup&lt;br/&gt;&#x27;, &#x27;AddVolumesToVolumeAccessGroup&lt;br/&gt;&#x27;, &#x27;RemoveVolumesFromVolumeAccessGroup&lt;br/&gt;&#x27;]
        :param volumeAccessGroupID: [required] The ID of the volume access group to modify.
        :type volumeAccessGroupID: 
        
        :param virtualNetworkID:  The ID of the SolidFire Virtual Network ID to associate the volume access group with.
        :type virtualNetworkID: 
        
        :param virtualNetworkTags:  The ID of the VLAN Virtual Network Tag to associate the volume access group with.
        :type virtualNetworkTags: 
        
        :param name:  [&#x27;Name of the volume access group.&#x27;, &#x27;It is not required to be unique, but recommended.&#x27;][&#x27;Name of the volume access group.&#x27;, &#x27;It is not required to be unique, but recommended.&#x27;]
        :type name: 
        
        :param initiators:  [&#x27;List of initiators to include in the volume access group.&#x27;, &quot;If unspecified, the access group&#x27;s configured initiators will not be modified.&quot;][&#x27;List of initiators to include in the volume access group.&#x27;, &quot;If unspecified, the access group&#x27;s configured initiators will not be modified.&quot;]
        :type initiators: 
        
        :param volumes:  [&#x27;List of volumes to initially include in the volume access group.&#x27;, &quot;If unspecified, the access group&#x27;s volumes will not be modified.&quot;][&#x27;List of volumes to initially include in the volume access group.&#x27;, &quot;If unspecified, the access group&#x27;s volumes will not be modified.&quot;]
        :type volumes: 
        
        :param attributes:  List of Name/Value pairs in JSON object format.
        :type attributes: 
        """

        params = { 
            "volumeAccessGroupID": volumeAccessGroupID,
        }
        if virtualNetworkID is not None:
            params["virtualNetworkID"] = virtualNetworkID
        if virtualNetworkTags is not None:
            params["virtualNetworkTags"] = virtualNetworkTags
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
            volumeAccessGroupID,
            initiators,):
        """
        Add initiators to a volume access group.
        :param volumeAccessGroupID: [required] The ID of the volume access group to modify.
        :type volumeAccessGroupID: 
        
        :param initiators: [required] [&#x27;List of initiators to add to the volume access group.&#x27;]
        :type initiators: 
        """

        params = { 
            "volumeAccessGroupID": volumeAccessGroupID,
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
            volumeAccessGroupID,
            initiators,):
        """
        Remove initiators from a volume access group.
        :param volumeAccessGroupID: [required] The ID of the volume access group to modify.
        :type volumeAccessGroupID: 
        
        :param initiators: [required] [&#x27;List of initiators to remove from the volume access group.&#x27;]
        :type initiators: 
        """

        params = { 
            "volumeAccessGroupID": volumeAccessGroupID,
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
            volumeAccessGroupID,
            volumes,):
        """
        Add volumes to a volume access group.
        :param volumeAccessGroupID: [required] The ID of the volume access group to modify.
        :type volumeAccessGroupID: 
        
        :param volumes: [required] [&#x27;List of volumes to add to this volume access group.&#x27;]
        :type volumes: 
        """

        params = { 
            "volumeAccessGroupID": volumeAccessGroupID,
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
            volumeAccessGroupID,
            volumes,):
        """
        Remove volumes from a volume access group.
        :param volumeAccessGroupID: [required] The ID of the volume access group to modify.
        :type volumeAccessGroupID: 
        
        :param volumes: [required] [&#x27;List of volumes to remove from this volume access group.&#x27;]
        :type volumes: 
        """

        params = { 
            "volumeAccessGroupID": volumeAccessGroupID,
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
            volumeAccessGroupID,):
        """
        GetVolumeAccessGroupEfficiency is used to retrieve efficiency information about a volume access group. Only the volume access group provided as parameters in this API method is used to compute the capacity.
        :param volumeAccessGroupID: [required] Specifies the volume access group for which capacity is computed.
        :type volumeAccessGroupID: 
        """

        params = { 
            "volumeAccessGroupID": volumeAccessGroupID,
        }
        
        # There is no adaptor.
        return self.send_request(
            'GetVolumeAccessGroupEfficiency',
            GetEfficiencyResult,
            params
        )

    def get_volume_access_group_lun_assignments(
            self,
            volumeAccessGroupID,):
        """
        The GetVolumeAccessGroupLunAssignments is used to return information LUN mappings of a specified volume access group.
        :param volumeAccessGroupID: [required] Unique volume access group ID used to return information.
        :type volumeAccessGroupID: 
        """

        params = { 
            "volumeAccessGroupID": volumeAccessGroupID,
        }
        
        # There is no adaptor.
        return self.send_request(
            'GetVolumeAccessGroupLunAssignments',
            GetVolumeAccessGroupLunAssignmentsResult,
            params
        )

    def modify_volume_access_group_lun_assignments(
            self,
            volumeAccessGroupID,
            lunAssignments,):
        """
        [&#x27;The ModifytVolumeAccessGroupLunAssignments is used to define custom LUN assignments for specific volumes. Only LUN values set on the lunAssignments parameter will be changed in the volume access group. All other LUN assignments will remain unchanged.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;LUN assignment values must be unique for volumes in a volume access group. An exception will be seen if LUN assignments are duplicated in a volume access group. However, the same LUN values can be used again in different volume access groups.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Note:&lt;/b&gt; Correct LUN values are 0 - 16383. An exception will be seen if an incorrect LUN value is passed. None of the specified LUN assignments will be modified if there is an exception.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Caution:&lt;/b&gt; If a LUN assignment is changed for a volume with active I/O, the I/O could be disrupted. Changes to the server configuration may be required in order to change volume LUN assignments.&#x27;]
        [&#x27;The ModifytVolumeAccessGroupLunAssignments is used to define custom LUN assignments for specific volumes. Only LUN values set on the lunAssignments parameter will be changed in the volume access group. All other LUN assignments will remain unchanged.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;LUN assignment values must be unique for volumes in a volume access group. An exception will be seen if LUN assignments are duplicated in a volume access group. However, the same LUN values can be used again in different volume access groups.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Note:&lt;/b&gt; Correct LUN values are 0 - 16383. An exception will be seen if an incorrect LUN value is passed. None of the specified LUN assignments will be modified if there is an exception.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Caution:&lt;/b&gt; If a LUN assignment is changed for a volume with active I/O, the I/O could be disrupted. Changes to the server configuration may be required in order to change volume LUN assignments.&#x27;]
        [&#x27;The ModifytVolumeAccessGroupLunAssignments is used to define custom LUN assignments for specific volumes. Only LUN values set on the lunAssignments parameter will be changed in the volume access group. All other LUN assignments will remain unchanged.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;LUN assignment values must be unique for volumes in a volume access group. An exception will be seen if LUN assignments are duplicated in a volume access group. However, the same LUN values can be used again in different volume access groups.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Note:&lt;/b&gt; Correct LUN values are 0 - 16383. An exception will be seen if an incorrect LUN value is passed. None of the specified LUN assignments will be modified if there is an exception.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Caution:&lt;/b&gt; If a LUN assignment is changed for a volume with active I/O, the I/O could be disrupted. Changes to the server configuration may be required in order to change volume LUN assignments.&#x27;]
        [&#x27;The ModifytVolumeAccessGroupLunAssignments is used to define custom LUN assignments for specific volumes. Only LUN values set on the lunAssignments parameter will be changed in the volume access group. All other LUN assignments will remain unchanged.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;LUN assignment values must be unique for volumes in a volume access group. An exception will be seen if LUN assignments are duplicated in a volume access group. However, the same LUN values can be used again in different volume access groups.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Note:&lt;/b&gt; Correct LUN values are 0 - 16383. An exception will be seen if an incorrect LUN value is passed. None of the specified LUN assignments will be modified if there is an exception.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Caution:&lt;/b&gt; If a LUN assignment is changed for a volume with active I/O, the I/O could be disrupted. Changes to the server configuration may be required in order to change volume LUN assignments.&#x27;]
        [&#x27;The ModifytVolumeAccessGroupLunAssignments is used to define custom LUN assignments for specific volumes. Only LUN values set on the lunAssignments parameter will be changed in the volume access group. All other LUN assignments will remain unchanged.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;LUN assignment values must be unique for volumes in a volume access group. An exception will be seen if LUN assignments are duplicated in a volume access group. However, the same LUN values can be used again in different volume access groups.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Note:&lt;/b&gt; Correct LUN values are 0 - 16383. An exception will be seen if an incorrect LUN value is passed. None of the specified LUN assignments will be modified if there is an exception.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Caution:&lt;/b&gt; If a LUN assignment is changed for a volume with active I/O, the I/O could be disrupted. Changes to the server configuration may be required in order to change volume LUN assignments.&#x27;]
        [&#x27;The ModifytVolumeAccessGroupLunAssignments is used to define custom LUN assignments for specific volumes. Only LUN values set on the lunAssignments parameter will be changed in the volume access group. All other LUN assignments will remain unchanged.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;LUN assignment values must be unique for volumes in a volume access group. An exception will be seen if LUN assignments are duplicated in a volume access group. However, the same LUN values can be used again in different volume access groups.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Note:&lt;/b&gt; Correct LUN values are 0 - 16383. An exception will be seen if an incorrect LUN value is passed. None of the specified LUN assignments will be modified if there is an exception.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Caution:&lt;/b&gt; If a LUN assignment is changed for a volume with active I/O, the I/O could be disrupted. Changes to the server configuration may be required in order to change volume LUN assignments.&#x27;]
        [&#x27;The ModifytVolumeAccessGroupLunAssignments is used to define custom LUN assignments for specific volumes. Only LUN values set on the lunAssignments parameter will be changed in the volume access group. All other LUN assignments will remain unchanged.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;LUN assignment values must be unique for volumes in a volume access group. An exception will be seen if LUN assignments are duplicated in a volume access group. However, the same LUN values can be used again in different volume access groups.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Note:&lt;/b&gt; Correct LUN values are 0 - 16383. An exception will be seen if an incorrect LUN value is passed. None of the specified LUN assignments will be modified if there is an exception.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Caution:&lt;/b&gt; If a LUN assignment is changed for a volume with active I/O, the I/O could be disrupted. Changes to the server configuration may be required in order to change volume LUN assignments.&#x27;]
        :param volumeAccessGroupID: [required] Unique volume access group ID for which the LUN assignments will be modified.
        :type volumeAccessGroupID: 
        
        :param lunAssignments: [required] The volume IDs with new assigned LUN values.
        :type lunAssignments: 
        """

        params = { 
            "volumeAccessGroupID": volumeAccessGroupID,
            "lunAssignments": lunAssignments,
        }
        
        # There is no adaptor.
        return self.send_request(
            'ModifyVolumeAccessGroupLunAssignments',
            ModifyVolumeAccessGroupLunAssignmentsResult,
            params
        )

    def create_database_entry(
            self,
            path,
            data=OPTIONAL,):
        """
        Creates a new database entry
        :param path: [required] The path of the new entry
        :type path: 
        
        :param data:  Initial data of the entry
        :type data: 
        """

        params = { 
            "path": path,
        }
        if data is not None:
            params["data"] = data
        
        # There is no adaptor.
        return self.send_request(
            'CreateDatabaseEntry',
            CreateDatabaseEntryResult,
            params
        )

    def delete_database_entry(
            self,
            path,
            dataVersion,):
        """
        Deletes an existing database entry
        :param path: [required] 
        :type path: 
        
        :param dataVersion: [required] 
        :type dataVersion: 
        """

        params = { 
            "path": path,
            "dataVersion": dataVersion,
        }
        
        # There is no adaptor.
        return self.send_request(
            'DeleteDatabaseEntry',
            DeleteDatabaseEntryResult,
            params
        )

    def get_database_entry(
            self,
            path,):
        """
        Gets an entry from the database
        :param path: [required] The path of the database entry
        :type path: 
        """

        params = { 
            "path": path,
        }
        
        # There is no adaptor.
        return self.send_request(
            'GetDatabaseEntry',
            DatabaseEntryResult,
            params
        )

    def set_database_entry(
            self,
            path,
            dataVersion,
            data,):
        """
        Sets the contents of an existing database entry
        :param path: [required] 
        :type path: 
        
        :param dataVersion: [required] 
        :type dataVersion: 
        
        :param data: [required] 
        :type data: 
        """

        params = { 
            "path": path,
            "dataVersion": dataVersion,
            "data": data,
        }
        
        # There is no adaptor.
        return self.send_request(
            'SetDatabaseEntry',
            DatabaseEntryResult,
            params
        )

    def list_database_children(
            self,
            path,):
        """
        Returns a list of the names of the children for a database path
        :param path: [required] 
        :type path: 
        """

        params = { 
            "path": path,
        }
        
        # There is no adaptor.
        return self.send_request(
            'ListDatabaseChildren',
            ListDatabaseChildrenResult,
            params
        )

    def list_database_children_data(
            self,
            path,):
        """
        Returns the data for all children in a database path
        :param path: [required] 
        :type path: 
        """

        params = { 
            "path": path,
        }
        
        # There is no adaptor.
        return self.send_request(
            'ListDatabaseChildrenData',
            ListDatabaseChildrenDataResult,
            params
        )

