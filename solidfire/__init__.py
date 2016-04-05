#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2014-2016 NetApp, Inc. All Rights Reserved.
#
# DO NOT EDIT THIS CODE BY HAND! It has been generated with jsvcgen.
#
from __future__ import unicode_literals
from __future__ import absolute_import

import logging
from logging import Logger
from solidfire import common
from solidfire.common import ServiceBase, ApiVersionExceededError, \
    ApiVersionUnsupportedError
from solidfire.results import AddAccountResult
from solidfire.results import CloneVolumeResult
from solidfire.results import CreateGroupSnapshotResult
from solidfire.results import CreateSnapshotResult
from solidfire.results import CreateVolumeAccessGroupResult
from solidfire.results import CreateVolumeResult
from solidfire.results import DeleteGroupSnapshotResult
from solidfire.results import DeleteSnapshotResult
from solidfire.results import DeleteVolumeAccessGroupResult
from solidfire.results import DeleteVolumeResult
from solidfire.results import GetAPIResult
from solidfire.results import GetAccountResult
from solidfire.results import GetAsyncResultResult
from solidfire.results import GetVolumeEfficiencyResult
from solidfire.results import GetVolumeStatsResult
from solidfire.results import ListAccountsResult
from solidfire.results import ListActiveVolumesResult
from solidfire.results import ListDeletedVolumesResult
from solidfire.results import ListGroupSnapshotsResult
from solidfire.results import ListSnapshotsResult
from solidfire.results import ListVolumeAccessGroupsResult
from solidfire.results import ListVolumeStatsByAccountResult
from solidfire.results import ListVolumeStatsByVolumeAccessGroupResult
from solidfire.results import ListVolumeStatsByVolumeResult
from solidfire.results import ListVolumesForAccountResult
from solidfire.results import ListVolumesResult
from solidfire.results import ModifyAccountResult
from solidfire.results import ModifyGroupSnapshotResult
from solidfire.results import ModifySnapshotResult
from solidfire.results import ModifyVolumeAccessGroupResult
from solidfire.results import ModifyVolumeResult
from solidfire.results import PurgeDeletedVolumeResult
from solidfire.results import RemoveAccountResult
from solidfire.results import RestoreDeletedVolumeResult

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
        :raises:
            ApiVersionExceededError: api_version is greater than connected
                Element OS.
            ApiVersionUnsupportedError: api_version is not supported by
                instance of Element OS.
        """

        logLevel = Logger.getEffectiveLevel(common.log)
        Logger.setLevel(common.log, logging.ERROR)
        ServiceBase.__init__(self, mvip, username, password,
                             0.0, verify_ssl, dispatcher)

        api = self.get_api()
        if float(api_version) > float(api.current_version):
            raise ApiVersionExceededError(api_version, api.current_version)
        elif str(api_version) not in api.supported_versions:
            raise ApiVersionUnsupportedError(api_version,
                                             api.supported_versions)

        ServiceBase.__init__(self, mvip, username, password, api_version,
                             verify_ssl, dispatcher)
        common.setLogLevel(logLevel)

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

        :type initiator_secret: str

        :param target_secret: (optional) CHAP secret to use for the target
            (mutual CHAP authentication). Should be 12-16 characters long and
            impenetrable. The CHAP target secrets must be unique and cannot be
            the same as the initiator CHAP secret.

            If not specified, a random secret is created.

        :type target_secret: str

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

        return self._send_request(
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

        return self._send_request(
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

        return self._send_request(
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

        return self._send_request(
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
        :type initiator_secret: str

        :param target_secret: (optional) CHAP secret to use for the target
            (mutual CHAP authentication). Should be 12-16 characters long and
            impenetrable.
        :type target_secret: str

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

        return self._send_request(
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

        return self._send_request(
            'RemoveAccount',
            RemoveAccountResult,
            params,
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

        return self._send_request(
            'GetAPI',
            GetAPIResult,
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

        return self._send_request(
            'GetAsyncResult',
            GetAsyncResultResult,
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
            is created from the volume's active branch.
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

        return self._send_request(
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

        return self._send_request(
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

        return self._send_request(
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

        return self._send_request(
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

        return self._send_request(
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
        :type volumes: int

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

        return self._send_request(
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

        return self._send_request(
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

        return self._send_request(
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

        return self._send_request(
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

        return self._send_request(
            'RollbackToGroupSnapshot',
            CreateGroupSnapshotResult,
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

        return self._send_request(
            'CloneVolume',
            CloneVolumeResult,
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

        return self._send_request(
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

        return self._send_request(
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

        return self._send_request(
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

        return self._send_request(
            'GetVolumeEfficiency',
            GetVolumeEfficiencyResult,
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

        return self._send_request(
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

        return self._send_request(
            'ListDeletedVolumes',
            ListDeletedVolumesResult,
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
        :type accounts: int

        :param is_paired: (optional) If specified, only fetch volumes which are
            paired (if true) or non-paired (if false). By default, list all
            volumes regardless of their pairing status.
        :type is_paired: bool

        :param volume_ids: (optional) If specified, only fetch volumes
            specified in this list. This option cannot be specified if
            *start_volume_id,* limit, or accounts option is specified.
        :type volume_ids: int

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

        return self._send_request(
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

        return self._send_request(
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

        return self._send_request(
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

        return self._send_request(
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
        :type volume_access_groups: int

        :returns: a response
        :rtype: ListVolumeStatsByVolumeAccessGroupResult
        """

        params = {}
        if volume_access_groups is not None:
            params["volumeAccessGroups"] = volume_access_groups

        return self._send_request(
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

        return self._send_request(
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

        return self._send_request(
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

        :param volume_id: [required] *restore_deleted_volume*
        :type volume_id: int

        :returns: a response
        :rtype: RestoreDeletedVolumeResult
        """

        params = {
            "volumeID": volume_id,
        }

        return self._send_request(
            'RestoreDeletedVolume',
            RestoreDeletedVolumeResult,
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
        :type initiators: str

        :param volumes: (optional) List of volumes to initially include in the
            volume access group. If unspecified, the access group will start
            without any volumes.
        :type volumes: int

        :param virtual_network_id: (optional) The ID of the SolidFire Virtual
            Network ID to associate the volume access group with.
        :type virtual_network_id: int

        :param virtual_network_tags: (optional) The ID of the VLAN Virtual
            Network Tag to associate the volume access group with.
        :type virtual_network_tags: int

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

        return self._send_request(
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

        return self._send_request(
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

        return self._send_request(
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
        :type virtual_network_id: int

        :param virtual_network_tags: (optional) The ID of the VLAN Virtual
            Network Tag to associate the volume access group with.
        :type virtual_network_tags: int

        :param name: (optional) Name of the volume access group. It is not
            required to be unique, but recommended.
        :type name: str

        :param initiators: (optional) List of initiators to include in the
            volume access group. If unspecified, the access group&#39;s
            configured initiators will not be modified.
        :type initiators: str

        :param volumes: (optional) List of volumes to initially include in the
            volume access group. If unspecified, the access group&#39;s volumes
            will not be modified.
        :type volumes: int

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

        return self._send_request(
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
        :type initiators: str

        :returns: a response
        :rtype: ModifyVolumeAccessGroupResult
        """

        params = {
            "volumeAccessGroupID": volume_access_group_id,
            "initiators": initiators,
        }

        return self._send_request(
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
        :type initiators: str

        :returns: a response
        :rtype: ModifyVolumeAccessGroupResult
        """

        params = {
            "volumeAccessGroupID": volume_access_group_id,
            "initiators": initiators,
        }

        return self._send_request(
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
        :type volumes: int

        :returns: a response
        :rtype: ModifyVolumeAccessGroupResult
        """

        params = {
            "volumeAccessGroupID": volume_access_group_id,
            "volumes": volumes,
        }

        return self._send_request(
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
        :type volumes: int

        :returns: a response
        :rtype: ModifyVolumeAccessGroupResult
        """

        params = {
            "volumeAccessGroupID": volume_access_group_id,
            "volumes": volumes,
        }

        return self._send_request(
            'RemoveVolumesFromVolumeAccessGroup',
            ModifyVolumeAccessGroupResult,
            params,
        )
