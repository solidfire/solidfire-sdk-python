#!/usr/bin/python
#
# Copyright &copy; 2014-2016 NetApp, Inc. All Rights Reserved.
#
# DO NOT EDIT THIS CODE BY HAND! It has been generated with jsvcgen.

from __future__ import unicode_literals
from __future__ import absolute_import
from solidfire.common import model as data_model
from uuid import UUID
from solidfire.custom.models import CHAPSecret as UserDefinedCHAPSecret
from solidfire.custom.models import Frequency as UserDefinedFrequency

class Frequency(UserDefinedFrequency):
    def __init__(self, **kwargs):
        self = UserDefinedFrequency()
        data_model.DataObject.__init__(self, **kwargs)

class CHAPSecret(UserDefinedCHAPSecret):
    def __init__(self, **kwargs):
        self = UserDefinedCHAPSecret()
        data_model.DataObject.__init__(self, **kwargs)

class CreateInitiator(data_model.DataObject):
    """CreateInitiator  
    Object containing characteristics of each new initiator.

    :param name: [required] (Required) The name of the initiator (IQN or WWPN) to create. (String) 
    :type name: str

    :param alias:  (Optional) The friendly name to assign to this initiator. (String) 
    :type alias: str

    :param volume_access_group_id:  (Optional) The ID of the volume access group into to which this newly created initiator will be added. (Integer) 
    :type volume_access_group_id: int

    :param attributes:  (Optional) A set of JSON attributes assigned to this initiator. (JSON Object) 
    :type attributes: dict

    """
    name = data_model.property(
        "name", str,
        array=False, optional=False,
        documentation="(Required) The name of the initiator (IQN or WWPN) to create. (String)",
        dictionaryType=None
    )
    alias = data_model.property(
        "alias", str,
        array=False, optional=True,
        documentation="[&#x27;(Optional) The friendly name to assign to this initiator. (String)&#x27;]",
        dictionaryType=None
    )
    volume_access_group_id = data_model.property(
        "volumeAccessGroupID", int,
        array=False, optional=True,
        documentation="(Optional) The ID of the volume access group into to which this newly created initiator will be added. (Integer)",
        dictionaryType=None
    )
    attributes = data_model.property(
        "attributes", dict,
        array=False, optional=True,
        documentation="(Optional) A set of JSON attributes assigned to this initiator. (JSON Object)",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ListStorageContainersRequest(data_model.DataObject):
    """ListStorageContainersRequest  

    :param storage_container_ids:  List of storage containers to get 
    :type storage_container_ids: UUID

    """
    storage_container_ids = data_model.property(
        "storageContainerIDs", UUID,
        array=True, optional=True,
        documentation="List of storage containers to get",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class RemoveClusterAdminRequest(data_model.DataObject):
    """RemoveClusterAdminRequest  

    :param cluster_admin_id: [required] ClusterAdminID for the Cluster Admin to remove. 
    :type cluster_admin_id: int

    """
    cluster_admin_id = data_model.property(
        "clusterAdminID", int,
        array=False, optional=False,
        documentation="ClusterAdminID for the Cluster Admin to remove.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class TestDrivesResult(data_model.DataObject):
    """TestDrivesResult  

    :param details: [required] 
    :type details: str

    """
    details = data_model.property(
        "details", str,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class CloneVolumeResult(data_model.DataObject):
    """CloneVolumeResult  

    :param clone_id: [required] The ID of the newly-created clone. 
    :type clone_id: int

    :param volume_id: [required] The volume ID of the newly-created clone. 
    :type volume_id: int

    :param async_handle: [required] Handle value used to track the progress of the clone. 
    :type async_handle: int

    """
    clone_id = data_model.property(
        "cloneID", int,
        array=False, optional=False,
        documentation="The ID of the newly-created clone.",
        dictionaryType=None
    )
    volume_id = data_model.property(
        "volumeID", int,
        array=False, optional=False,
        documentation="The volume ID of the newly-created clone.",
        dictionaryType=None
    )
    async_handle = data_model.property(
        "asyncHandle", int,
        array=False, optional=False,
        documentation="Handle value used to track the progress of the clone.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class GetHardwareInfoResult(data_model.DataObject):
    """GetHardwareInfoResult  

    :param hardware_info: [required] Hardware information for this node.  
    :type hardware_info: dict

    """
    hardware_info = data_model.property(
        "hardwareInfo", dict,
        array=False, optional=False,
        documentation="Hardware information for this node. ",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class GetOriginRequest(data_model.DataObject):
    """GetOriginRequest  

    :param force: [required] 
    :type force: bool

    """
    force = data_model.property(
        "force", bool,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class DriveStats(data_model.DataObject):
    """DriveStats  

    :param active_sessions:  
    :type active_sessions: int

    :param drive_id:  
    :type drive_id: int

    :param failed_die_count: [required] 
    :type failed_die_count: int

    :param life_remaining_percent: [required] 
    :type life_remaining_percent: int

    :param lifetime_read_bytes: [required] 
    :type lifetime_read_bytes: int

    :param lifetime_write_bytes: [required] 
    :type lifetime_write_bytes: int

    :param power_on_hours: [required] 
    :type power_on_hours: int

    :param read_bytes: [required] 
    :type read_bytes: int

    :param read_ops: [required] 
    :type read_ops: int

    :param reallocated_sectors: [required] 
    :type reallocated_sectors: int

    :param reserve_capacity_percent: [required] 
    :type reserve_capacity_percent: int

    :param timestamp: [required] 
    :type timestamp: str

    :param total_capacity: [required] 
    :type total_capacity: int

    :param used_capacity:  
    :type used_capacity: int

    :param used_memory: [required] 
    :type used_memory: int

    :param write_bytes: [required] 
    :type write_bytes: int

    :param write_ops: [required] 
    :type write_ops: int

    """
    active_sessions = data_model.property(
        "activeSessions", int,
        array=False, optional=True,
        documentation="",
        dictionaryType=None
    )
    drive_id = data_model.property(
        "driveID", int,
        array=False, optional=True,
        documentation="",
        dictionaryType=None
    )
    failed_die_count = data_model.property(
        "failedDieCount", int,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    life_remaining_percent = data_model.property(
        "lifeRemainingPercent", int,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    lifetime_read_bytes = data_model.property(
        "lifetimeReadBytes", int,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    lifetime_write_bytes = data_model.property(
        "lifetimeWriteBytes", int,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    power_on_hours = data_model.property(
        "powerOnHours", int,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    read_bytes = data_model.property(
        "readBytes", int,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    read_ops = data_model.property(
        "readOps", int,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    reallocated_sectors = data_model.property(
        "reallocatedSectors", int,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    reserve_capacity_percent = data_model.property(
        "reserveCapacityPercent", int,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    timestamp = data_model.property(
        "timestamp", str,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    total_capacity = data_model.property(
        "totalCapacity", int,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    used_capacity = data_model.property(
        "usedCapacity", int,
        array=False, optional=True,
        documentation="",
        dictionaryType=None
    )
    used_memory = data_model.property(
        "usedMemory", int,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    write_bytes = data_model.property(
        "writeBytes", int,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    write_ops = data_model.property(
        "writeOps", int,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ListDriveStatsResult(data_model.DataObject):
    """ListDriveStatsResult  

    :param drive_stats: [required] List of drive activity information for each drive. 
    :type drive_stats: DriveStats

    :param errors: [required] If there are errors retrieving information about a drive, this list contains the driveID and associated error message. Always present, and empty if there are no errors. 
    :type errors: dict

    """
    drive_stats = data_model.property(
        "driveStats", DriveStats,
        array=True, optional=False,
        documentation="List of drive activity information for each drive.",
        dictionaryType=None
    )
    errors = data_model.property(
        "errors", dict,
        array=True, optional=False,
        documentation="If there are errors retrieving information about a drive, this list contains the driveID and associated error message. Always present, and empty if there are no errors.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class VirtualVolumeHost(data_model.DataObject):
    """VirtualVolumeHost  

    :param virtual_volume_host_id: [required] 
    :type virtual_volume_host_id: UUID

    :param cluster_id: [required] 
    :type cluster_id: UUID

    :param visible_protocol_endpoint_ids: [required] 
    :type visible_protocol_endpoint_ids: UUID

    :param bindings: [required] 
    :type bindings: int

    :param initiator_names: [required] 
    :type initiator_names: str

    :param host_address: [required] 
    :type host_address: str

    """
    virtual_volume_host_id = data_model.property(
        "virtualVolumeHostID", UUID,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    cluster_id = data_model.property(
        "clusterID", UUID,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    visible_protocol_endpoint_ids = data_model.property(
        "visibleProtocolEndpointIDs", UUID,
        array=True, optional=False,
        documentation="",
        dictionaryType=None
    )
    bindings = data_model.property(
        "bindings", int,
        array=True, optional=False,
        documentation="",
        dictionaryType=None
    )
    initiator_names = data_model.property(
        "initiatorNames", str,
        array=True, optional=False,
        documentation="",
        dictionaryType=None
    )
    host_address = data_model.property(
        "hostAddress", str,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ListVirtualVolumeHostsResult(data_model.DataObject):
    """ListVirtualVolumeHostsResult  

    :param hosts: [required] List of known ESX hosts. 
    :type hosts: VirtualVolumeHost

    """
    hosts = data_model.property(
        "hosts", VirtualVolumeHost,
        array=True, optional=False,
        documentation="List of known ESX hosts.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class DeleteAllSupportBundlesResult(data_model.DataObject):
    """DeleteAllSupportBundlesResult  

    """

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class GetClusterHardwareInfoRequest(data_model.DataObject):
    """GetClusterHardwareInfoRequest  

    :param type:  Include only a certain type of hardware information in the response. Can be one of the following:drives: List only drive information in the response.nodes: List only node information in the response.all: Include both drive and node information in the response.If this parameter is omitted, a type of "all" is assumed. 
    :type type: str

    """
    type = data_model.property(
        "type", str,
        array=False, optional=True,
        documentation="Include only a certain type of hardware information in the response. Can be one of the following:drives: List only drive information in the response.nodes: List only node information in the response.all: Include both drive and node information in the response.If this parameter is omitted, a type of &quot;all&quot; is assumed.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class VolumeQOS(data_model.DataObject):
    """VolumeQOS  
    Quality of Service (QoS) Result values are used on SolidFire volumes to provision performance expectations.

    :param min_iops: [required] Desired minimum 4KB IOPS to guarantee. The allowed IOPS will only drop below this level if all volumes have been capped at their min IOPS value and there is still insufficient performance capacity. 
    :type min_iops: int

    :param max_iops: [required] Desired maximum 4KB IOPS allowed over an extended period of time. 
    :type max_iops: int

    :param burst_iops: [required] Maximum "peak" 4KB IOPS allowed for short periods of time. Allows for bursts of I/O activity over the normal max IOPS value. 
    :type burst_iops: int

    :param burst_time: [required] The length of time burst IOPS is allowed. The value returned is represented in time units of seconds. Note: this value is calculated by the system based on IOPS set for QoS. 
    :type burst_time: int

    :param curve: [required] The curve is a set of key-value pairs. The keys are I/O sizes in bytes. The values represent the cost performing an IOP at a specific I/O size. The curve is calculated relative to a 4096 byte operation set at 100 IOPS. 
    :type curve: dict

    """
    min_iops = data_model.property(
        "minIOPS", int,
        array=False, optional=False,
        documentation="[&#x27;Desired minimum 4KB IOPS to guarantee.&#x27;, &#x27;The allowed IOPS will only drop below this level if all volumes have been capped&#x27;, &#x27;at their min IOPS value and there is still insufficient performance capacity.&#x27;]",
        dictionaryType=None
    )
    max_iops = data_model.property(
        "maxIOPS", int,
        array=False, optional=False,
        documentation="[&#x27;Desired maximum 4KB IOPS allowed over an extended period of time.&#x27;]",
        dictionaryType=None
    )
    burst_iops = data_model.property(
        "burstIOPS", int,
        array=False, optional=False,
        documentation="[&#x27;Maximum &quot;peak&quot; 4KB IOPS allowed for short periods of time.&#x27;, &#x27;Allows for bursts of I/O activity over the normal max IOPS value.&#x27;]",
        dictionaryType=None
    )
    burst_time = data_model.property(
        "burstTime", int,
        array=False, optional=False,
        documentation="[&#x27;The length of time burst IOPS is allowed.&#x27;, &#x27;The value returned is represented in time units of seconds.&#x27;, &#x27;Note: this value is calculated by the system based on IOPS set for QoS.&#x27;]",
        dictionaryType=None
    )
    curve = data_model.property(
        "curve", dict,
        array=False, optional=False,
        documentation="[&#x27;The curve is a set of key-value pairs.&#x27;, &#x27;The keys are I/O sizes in bytes.&#x27;, &#x27;The values represent the cost performing an IOP at a specific I/O size.&#x27;, &#x27;The curve is calculated relative to a 4096 byte operation set at 100 IOPS.&#x27;]",
        dictionaryType=int
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class LoginSessionInfo(data_model.DataObject):
    """LoginSessionInfo  

    :param timeout: [required] 
    :type timeout: str

    """
    timeout = data_model.property(
        "timeout", str,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class GetLoginSessionInfoResult(data_model.DataObject):
    """GetLoginSessionInfoResult  

    :param login_session_info: [required] The authentication expiration period. Formatted in H:mm:ss. For example: 1:30:00, 20:00, 5:00. All leading zeros and colons are removed regardless of the format the timeout was entered. Objects returned are: timeout - The time, in minutes, when this session will timeout and expire. 
    :type login_session_info: LoginSessionInfo

    """
    login_session_info = data_model.property(
        "loginSessionInfo", LoginSessionInfo,
        array=False, optional=False,
        documentation="[&#x27;The authentication expiration period. Formatted in H:mm:ss. For example: 1:30:00, 20:00, 5:00. All leading zeros and colons are removed regardless of the format the timeout was entered.&#x27;, &#x27;Objects returned are:&#x27;, &#x27;timeout - The time, in minutes, when this session will timeout and expire.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class AddVolumesToVolumeAccessGroupRequest(data_model.DataObject):
    """AddVolumesToVolumeAccessGroupRequest  

    :param volume_access_group_id: [required] The ID of the volume access group to modify. 
    :type volume_access_group_id: int

    :param volumes: [required] List of volumes to add to this volume access group. 
    :type volumes: int

    """
    volume_access_group_id = data_model.property(
        "volumeAccessGroupID", int,
        array=False, optional=False,
        documentation="The ID of the volume access group to modify.",
        dictionaryType=None
    )
    volumes = data_model.property(
        "volumes", int,
        array=True, optional=False,
        documentation="[&#x27;List of volumes to add to this volume access group.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class SnapshotReplication(data_model.DataObject):
    """SnapshotReplication  

    :param state: [required] The state of the snapshot replication. 
    :type state: str

    :param state_details: [required] Reserved for future use. 
    :type state_details: str

    """
    state = data_model.property(
        "state", str,
        array=False, optional=False,
        documentation="The state of the snapshot replication.",
        dictionaryType=None
    )
    state_details = data_model.property(
        "stateDetails", str,
        array=False, optional=False,
        documentation="Reserved for future use.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class RemoteReplication(data_model.DataObject):
    """RemoteReplication  
    Details on the volume replication.

    :param mode: [required] Volume replication mode. Possible values: Async: Writes are acknowledged when they complete locally. The cluster does not wait for writes to be replicated to the target cluster. Sync: Source acknowledges write when the data is stored locally and on the remote cluster. SnapshotsOnly: Only snapshots created on the source cluster will be replicated. Active writes from the source volume will not be replicated. 
    :type mode: str

    :param pause_limit: [required] The number of occurring write ops before auto-pausing, on a per volume pair level. 
    :type pause_limit: int

    :param remote_service_id: [required] The remote slice service ID. 
    :type remote_service_id: int

    :param resume_details: [required] Reserved for future use. 
    :type resume_details: str

    :param snapshot_replication: [required] The details of snapshot replication. 
    :type snapshot_replication: SnapshotReplication

    :param state: [required] The state of the volume replication. 
    :type state: str

    :param state_details: [required] Reserved for future use. 
    :type state_details: str

    """
    mode = data_model.property(
        "mode", str,
        array=False, optional=False,
        documentation="[&#x27;Volume replication mode.&#x27;, &#x27;Possible values:&#x27;, &#x27;Async: Writes are acknowledged when they complete locally. The cluster does not wait for writes to be replicated to the target cluster.&#x27;, &#x27;Sync: Source acknowledges write when the data is stored locally and on the remote cluster.&#x27;, &#x27;SnapshotsOnly: Only snapshots created on the source cluster will be replicated. Active writes from the source volume will not be replicated.&#x27;]",
        dictionaryType=None
    )
    pause_limit = data_model.property(
        "pauseLimit", int,
        array=False, optional=False,
        documentation="The number of occurring write ops before auto-pausing, on a per volume pair level.",
        dictionaryType=None
    )
    remote_service_id = data_model.property(
        "remoteServiceID", int,
        array=False, optional=False,
        documentation="The remote slice service ID.",
        dictionaryType=None
    )
    resume_details = data_model.property(
        "resumeDetails", str,
        array=False, optional=False,
        documentation="Reserved for future use.",
        dictionaryType=None
    )
    snapshot_replication = data_model.property(
        "snapshotReplication", SnapshotReplication,
        array=False, optional=False,
        documentation="The details of snapshot replication.",
        dictionaryType=None
    )
    state = data_model.property(
        "state", str,
        array=False, optional=False,
        documentation="The state of the volume replication.",
        dictionaryType=None
    )
    state_details = data_model.property(
        "stateDetails", str,
        array=False, optional=False,
        documentation="Reserved for future use.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class VolumePair(data_model.DataObject):
    """VolumePair  
    The Volume Pair Info is an object containing information about a volume that is paired on a remote cluster.
    If the volume is not paired, this object is null.

    :param cluster_pair_id: [required] The remote cluster a volume is paired with. 
    :type cluster_pair_id: int

    :param remote_volume_id: [required] The VolumeID on the remote cluster a volume is paired with. 
    :type remote_volume_id: int

    :param remote_slice_id: [required] The SliceID on the remote cluster a volume is paired with. 
    :type remote_slice_id: int

    :param remote_volume_name: [required] The last-observed name of the volume on the remote cluster a volume is paired with. 
    :type remote_volume_name: str

    :param volume_pair_uuid: [required] A UUID in canonical form. 
    :type volume_pair_uuid: UUID

    :param remote_replication: [required] Details about the replication configuration for this volume pair. 
    :type remote_replication: RemoteReplication

    """
    cluster_pair_id = data_model.property(
        "clusterPairID", int,
        array=False, optional=False,
        documentation="The remote cluster a volume is paired with.",
        dictionaryType=None
    )
    remote_volume_id = data_model.property(
        "remoteVolumeID", int,
        array=False, optional=False,
        documentation="The VolumeID on the remote cluster a volume is paired with.",
        dictionaryType=None
    )
    remote_slice_id = data_model.property(
        "remoteSliceID", int,
        array=False, optional=False,
        documentation="The SliceID on the remote cluster a volume is paired with.",
        dictionaryType=None
    )
    remote_volume_name = data_model.property(
        "remoteVolumeName", str,
        array=False, optional=False,
        documentation="The last-observed name of the volume on the remote cluster a volume is paired with.",
        dictionaryType=None
    )
    volume_pair_uuid = data_model.property(
        "volumePairUUID", UUID,
        array=False, optional=False,
        documentation="A UUID in canonical form.",
        dictionaryType=None
    )
    remote_replication = data_model.property(
        "remoteReplication", RemoteReplication,
        array=False, optional=False,
        documentation="Details about the replication configuration for this volume pair.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class Volume(data_model.DataObject):
    """Volume  
    Volumes Info is an object containing information about a volume.
    The return objects only include "configured" information about the volume and not runtime or usage information.
    Information about paired volumes will also be returned.

    :param volume_id: [required] Unique VolumeID for the volume. 
    :type volume_id: int

    :param name: [required] Name of the volume as provided at creation time. 
    :type name: str

    :param account_id: [required] Unique AccountID for the account. 
    :type account_id: int

    :param create_time: [required] UTC formatted time the volume was created. 
    :type create_time: str

    :param status: [required] Current status of the volume init: A volume that is being initialized and is not ready for connections. active: An active volume ready for connections. 
    :type status: str

    :param access: [required] Access allowed for the volume readOnly: Only read operations are allowed. readWrite: Reads and writes are allowed. locked: No reads or writes are allowed. replicationTarget: Designated as a target volume in a replicated volume pair. 
    :type access: str

    :param enable512e: [required] If "true", the volume provides 512 byte sector emulation. 
    :type enable512e: bool

    :param iqn: [required] Volume iSCSI Qualified Name. 
    :type iqn: str

    :param scsi_euidevice_id: [required] Globally unique SCSI device identifier for the volume in EUI-64 based 16-byte format. 
    :type scsi_euidevice_id: str

    :param scsi_naadevice_id: [required] Globally unique SCSI device identifier for the volume in NAA IEEE Registered Extended format. 
    :type scsi_naadevice_id: str

    :param qos: [required] Quality of service settings for this volume. 
    :type qos: VolumeQOS

    :param volume_access_groups: [required] List of volume access groups to which a volume belongs. 
    :type volume_access_groups: int

    :param volume_pairs: [required] Information about a paired volume. Available only if a volume is paired. @see VolumePairs for return values. 
    :type volume_pairs: VolumePair

    :param delete_time:  The time this volume was deleted. If this has no value, the volume has not yet been deleted. 
    :type delete_time: str

    :param purge_time:  The time this volume will be purged from the system. If this has no value, the volume has not yet been deleted (and is not scheduled for purging). 
    :type purge_time: str

    :param slice_count: [required] The number of slices backing this volume. In the current software, this value will always be 1. 
    :type slice_count: int

    :param total_size: [required] Total size of this volume in bytes. 
    :type total_size: int

    :param block_size: [required] Size of the blocks on the volume. 
    :type block_size: int

    :param virtual_volume_id: [required] Virtual volume ID this volume backs. 
    :type virtual_volume_id: UUID

    :param attributes: [required] List of Name/Value pairs in JSON object format. 
    :type attributes: dict

    """
    volume_id = data_model.property(
        "volumeID", int,
        array=False, optional=False,
        documentation="Unique VolumeID for the volume.",
        dictionaryType=None
    )
    name = data_model.property(
        "name", str,
        array=False, optional=False,
        documentation="Name of the volume as provided at creation time.",
        dictionaryType=None
    )
    account_id = data_model.property(
        "accountID", int,
        array=False, optional=False,
        documentation="Unique AccountID for the account.",
        dictionaryType=None
    )
    create_time = data_model.property(
        "createTime", str,
        array=False, optional=False,
        documentation="UTC formatted time the volume was created.",
        dictionaryType=None
    )
    status = data_model.property(
        "status", str,
        array=False, optional=False,
        documentation="[&#x27;Current status of the volume&#x27;, &#x27;init: A volume that is being initialized and is not ready for connections.&#x27;, &#x27;active: An active volume ready for connections.&#x27;]",
        dictionaryType=None
    )
    access = data_model.property(
        "access", str,
        array=False, optional=False,
        documentation="[&#x27;Access allowed for the volume&#x27;, &#x27;readOnly: Only read operations are allowed.&#x27;, &#x27;readWrite: Reads and writes are allowed.&#x27;, &#x27;locked: No reads or writes are allowed.&#x27;, &#x27;replicationTarget: Designated as a target volume in a replicated volume pair.&#x27;]",
        dictionaryType=None
    )
    enable512e = data_model.property(
        "enable512e", bool,
        array=False, optional=False,
        documentation="If &quot;true&quot;, the volume provides 512 byte sector emulation.",
        dictionaryType=None
    )
    iqn = data_model.property(
        "iqn", str,
        array=False, optional=False,
        documentation="Volume iSCSI Qualified Name.",
        dictionaryType=None
    )
    scsi_euidevice_id = data_model.property(
        "scsiEUIDeviceID", str,
        array=False, optional=False,
        documentation="Globally unique SCSI device identifier for the volume in EUI-64 based 16-byte format.",
        dictionaryType=None
    )
    scsi_naadevice_id = data_model.property(
        "scsiNAADeviceID", str,
        array=False, optional=False,
        documentation="Globally unique SCSI device identifier for the volume in NAA IEEE Registered Extended format.",
        dictionaryType=None
    )
    qos = data_model.property(
        "qos", VolumeQOS,
        array=False, optional=False,
        documentation="Quality of service settings for this volume.",
        dictionaryType=None
    )
    volume_access_groups = data_model.property(
        "volumeAccessGroups", int,
        array=True, optional=False,
        documentation="List of volume access groups to which a volume belongs.",
        dictionaryType=None
    )
    volume_pairs = data_model.property(
        "volumePairs", VolumePair,
        array=True, optional=False,
        documentation="[&#x27;Information about a paired volume.&#x27;, &#x27;Available only if a volume is paired.&#x27;, &#x27;@see VolumePairs for return values.&#x27;]",
        dictionaryType=None
    )
    delete_time = data_model.property(
        "deleteTime", str,
        array=False, optional=True,
        documentation="[&#x27;The time this volume was deleted.&#x27;, &#x27;If this has no value, the volume has not yet been deleted.&#x27;]",
        dictionaryType=None
    )
    purge_time = data_model.property(
        "purgeTime", str,
        array=False, optional=True,
        documentation="[&#x27;The time this volume will be purged from the system.&#x27;, &#x27;If this has no value, the volume has not yet been deleted (and is not scheduled for purging).&#x27;]",
        dictionaryType=None
    )
    slice_count = data_model.property(
        "sliceCount", int,
        array=False, optional=False,
        documentation="[&#x27;The number of slices backing this volume.&#x27;, &#x27;In the current software, this value will always be 1.&#x27;]",
        dictionaryType=None
    )
    total_size = data_model.property(
        "totalSize", int,
        array=False, optional=False,
        documentation="[&#x27;Total size of this volume in bytes.&#x27;]",
        dictionaryType=None
    )
    block_size = data_model.property(
        "blockSize", int,
        array=False, optional=False,
        documentation="[&#x27;Size of the blocks on the volume.&#x27;]",
        dictionaryType=None
    )
    virtual_volume_id = data_model.property(
        "virtualVolumeID", UUID,
        array=False, optional=False,
        documentation="[&#x27;Virtual volume ID this volume backs.&#x27;]",
        dictionaryType=None
    )
    attributes = data_model.property(
        "attributes", dict,
        array=False, optional=False,
        documentation="List of Name/Value pairs in JSON object format.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ListVolumesForAccountResult(data_model.DataObject):
    """ListVolumesForAccountResult  

    :param volumes: [required] List of volumes. 
    :type volumes: Volume

    """
    volumes = data_model.property(
        "volumes", Volume,
        array=True, optional=False,
        documentation="List of volumes.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class MetadataHosts(data_model.DataObject):
    """MetadataHosts  
    The volume services on which the volume metadata resides.

    :param dead_secondaries: [required] Secondary metadata (slice) services that are in a dead state. 
    :type dead_secondaries: int

    :param live_secondaries: [required] Secondary metadata (slice) services that are currently in a "live" state. 
    :type live_secondaries: int

    :param primary: [required] The primary metadata (slice) services hosting the volume. 
    :type primary: int

    """
    dead_secondaries = data_model.property(
        "deadSecondaries", int,
        array=True, optional=False,
        documentation="Secondary metadata (slice) services that are in a dead state.",
        dictionaryType=None
    )
    live_secondaries = data_model.property(
        "liveSecondaries", int,
        array=True, optional=False,
        documentation="Secondary metadata (slice) services that are currently in a &quot;live&quot; state.",
        dictionaryType=None
    )
    primary = data_model.property(
        "primary", int,
        array=False, optional=False,
        documentation="The primary metadata (slice) services hosting the volume.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class VolumeStats(data_model.DataObject):
    """VolumeStats  
    Contains statistical data for an individual volume.

    :param account_id: [required] AccountID of the volume owner. 
    :type account_id: int

    :param actual_iops: [required] Current actual IOPS to the volume in the last 500 milliseconds. 
    :type actual_iops: int

    :param async_delay:  The length of time since the volume was last synced with the remote cluster. If the volume is not paired, this is null.  Note: A target volume in an active replication state always has an async delay of 0 (zero). Target volumes are system-aware during replication and assume async delay is accurate at all times. 
    :type async_delay: str

    :param average_iopsize: [required] Average size in bytes of recent I/O to the volume in the last 500 milliseconds. 
    :type average_iopsize: int

    :param burst_iopscredit: [required] The total number of IOP credits available to the user. When users are not using up to the max IOPS, credits are accrued. 
    :type burst_iopscredit: int

    :param client_queue_depth: [required] The number of outstanding read and write operations to the cluster. 
    :type client_queue_depth: int

    :param desired_metadata_hosts: [required] The volume services being migrated to if the volume metadata is getting migrated between volume services. A "null" value means the volume is not migrating. 
    :type desired_metadata_hosts: MetadataHosts

    :param latency_usec: [required] The observed latency time, in microseconds, to complete operations to a volume. A "0" (zero) value means there is no I/O to the volume. 
    :type latency_usec: int

    :param metadata_hosts: [required] The volume services on which the volume metadata resides. 
    :type metadata_hosts: MetadataHosts

    :param non_zero_blocks: [required] The number of 4KiB blocks with data after the last garbage collection operation has completed. 
    :type non_zero_blocks: int

    :param read_bytes: [required] Total bytes read by clients. 
    :type read_bytes: int

    :param read_latency_usec: [required] The average time, in microseconds, to complete read operations. 
    :type read_latency_usec: int

    :param read_ops: [required] Total read operations. 
    :type read_ops: int

    :param throttle: [required] A floating value between 0 and 1 that represents how much the system is throttling clients below their max IOPS because of re-replication of data, transient errors and snapshots taken. 
    :type throttle: float

    :param timestamp: [required] The current time in UTC. 
    :type timestamp: str

    :param total_latency_usec: [required] The average time, in microseconds, to complete read and write operations to a volume. 
    :type total_latency_usec: int

    :param unaligned_reads: [required] For 512e volumes, the number of read operations that were not on a 4k sector boundary. High numbers of unaligned reads may indicate improper partition alignment. 
    :type unaligned_reads: int

    :param unaligned_writes: [required] For 512e volumes, the number of write operations that were not on a 4k sector boundary. High numbers of unaligned writes may indicate improper partition alignment. 
    :type unaligned_writes: int

    :param volume_access_groups: [required] List of volume access group(s) to which a volume belongs. 
    :type volume_access_groups: int

    :param volume_id: [required] Volume ID of the volume. 
    :type volume_id: int

    :param volume_size: [required] Total provisioned capacity in bytes. 
    :type volume_size: int

    :param volume_utilization: [required] A floating value that describes how much the client is using the volume.  Values:  0 = Client is not using the volume 1 = Client is using their max >1 = Client is using their burst 
    :type volume_utilization: float

    :param write_bytes: [required] Total bytes written by clients. 
    :type write_bytes: int

    :param write_latency_usec: [required] The average time, in microseconds, to complete write operations. 
    :type write_latency_usec: int

    :param write_ops: [required] Total write operations occurring on the volume. 
    :type write_ops: int

    :param zero_blocks: [required] Total number of 4KiB blocks without data after the last round of garbage collection operation has completed. 
    :type zero_blocks: int

    :param write_bytes_last_sample: [required] The total number of bytes written to the volume during the last sample period. 
    :type write_bytes_last_sample: int

    :param sample_period_msec: [required] The length of the sample period in milliseconds. 
    :type sample_period_msec: int

    :param read_bytes_last_sample: [required] The total number of bytes read from the volume during the last sample period. 
    :type read_bytes_last_sample: int

    :param read_ops_last_sample: [required] The total number of read operations durin gth elast sample period. 
    :type read_ops_last_sample: int

    :param write_ops_last_sample: [required] The total number of write operations during the last sample period. 
    :type write_ops_last_sample: int

    :param virtual_volume_id: [required] If the volume of interest is associated with a virtual volume, this is the virtual volume ID. 
    :type virtual_volume_id: UUID

    """
    account_id = data_model.property(
        "accountID", int,
        array=False, optional=False,
        documentation="AccountID of the volume owner.",
        dictionaryType=None
    )
    actual_iops = data_model.property(
        "actualIOPS", int,
        array=False, optional=False,
        documentation="Current actual IOPS to the volume in the last 500 milliseconds.",
        dictionaryType=None
    )
    async_delay = data_model.property(
        "asyncDelay", str,
        array=False, optional=True,
        documentation="[&#x27;The length of time since the volume was last synced with the remote cluster.&#x27;, &#x27;If the volume is not paired, this is null.&#x27;, u&#x27;&#x27;, &#x27;Note: A target volume in an active replication state always has an async delay of 0 (zero).&#x27;, &#x27;Target volumes are system-aware during replication and assume async delay is accurate at all times.&#x27;]",
        dictionaryType=None
    )
    average_iopsize = data_model.property(
        "averageIOPSize", int,
        array=False, optional=False,
        documentation="Average size in bytes of recent I/O to the volume in the last 500 milliseconds.",
        dictionaryType=None
    )
    burst_iopscredit = data_model.property(
        "burstIOPSCredit", int,
        array=False, optional=False,
        documentation="[&#x27;The total number of IOP credits available to the user.&#x27;, &#x27;When users are not using up to the max IOPS, credits are accrued.&#x27;]",
        dictionaryType=None
    )
    client_queue_depth = data_model.property(
        "clientQueueDepth", int,
        array=False, optional=False,
        documentation="The number of outstanding read and write operations to the cluster.",
        dictionaryType=None
    )
    desired_metadata_hosts = data_model.property(
        "desiredMetadataHosts", MetadataHosts,
        array=False, optional=False,
        documentation="[&#x27;The volume services being migrated to if the volume metadata is getting migrated between volume services.&#x27;, &#x27;A &quot;null&quot; value means the volume is not migrating.&#x27;]",
        dictionaryType=None
    )
    latency_usec = data_model.property(
        "latencyUSec", int,
        array=False, optional=False,
        documentation="[&#x27;The observed latency time, in microseconds, to complete operations to a volume.&#x27;, &#x27;A &quot;0&quot; (zero) value means there is no I/O to the volume.&#x27;]",
        dictionaryType=None
    )
    metadata_hosts = data_model.property(
        "metadataHosts", MetadataHosts,
        array=False, optional=False,
        documentation="The volume services on which the volume metadata resides.",
        dictionaryType=None
    )
    non_zero_blocks = data_model.property(
        "nonZeroBlocks", int,
        array=False, optional=False,
        documentation="The number of 4KiB blocks with data after the last garbage collection operation has completed.",
        dictionaryType=None
    )
    read_bytes = data_model.property(
        "readBytes", int,
        array=False, optional=False,
        documentation="Total bytes read by clients.",
        dictionaryType=None
    )
    read_latency_usec = data_model.property(
        "readLatencyUSec", int,
        array=False, optional=False,
        documentation="The average time, in microseconds, to complete read operations.",
        dictionaryType=None
    )
    read_ops = data_model.property(
        "readOps", int,
        array=False, optional=False,
        documentation="Total read operations.",
        dictionaryType=None
    )
    throttle = data_model.property(
        "throttle", float,
        array=False, optional=False,
        documentation="[&#x27;A floating value between 0 and 1 that represents how much the system is throttling clients&#x27;, &#x27;below their max IOPS because of re-replication of data, transient errors and snapshots taken.&#x27;]",
        dictionaryType=None
    )
    timestamp = data_model.property(
        "timestamp", str,
        array=False, optional=False,
        documentation="The current time in UTC.",
        dictionaryType=None
    )
    total_latency_usec = data_model.property(
        "totalLatencyUSec", int,
        array=False, optional=False,
        documentation="The average time, in microseconds, to complete read and write operations to a volume.",
        dictionaryType=None
    )
    unaligned_reads = data_model.property(
        "unalignedReads", int,
        array=False, optional=False,
        documentation="[&#x27;For 512e volumes, the number of read operations that were not on a 4k sector boundary.&#x27;, &#x27;High numbers of unaligned reads may indicate improper partition alignment.&#x27;]",
        dictionaryType=None
    )
    unaligned_writes = data_model.property(
        "unalignedWrites", int,
        array=False, optional=False,
        documentation="[&#x27;For 512e volumes, the number of write operations that were not on a 4k sector boundary.&#x27;, &#x27;High numbers of unaligned writes may indicate improper partition alignment.&#x27;]",
        dictionaryType=None
    )
    volume_access_groups = data_model.property(
        "volumeAccessGroups", int,
        array=True, optional=False,
        documentation="List of volume access group(s) to which a volume belongs.",
        dictionaryType=None
    )
    volume_id = data_model.property(
        "volumeID", int,
        array=False, optional=False,
        documentation="Volume ID of the volume.",
        dictionaryType=None
    )
    volume_size = data_model.property(
        "volumeSize", int,
        array=False, optional=False,
        documentation="Total provisioned capacity in bytes.",
        dictionaryType=None
    )
    volume_utilization = data_model.property(
        "volumeUtilization", float,
        array=False, optional=False,
        documentation="[&#x27;A floating value that describes how much the client is using the volume.&#x27;, u&#x27;&#x27;, &#x27;Values:&#x27;, &#x27; 0 = Client is not using the volume&#x27;, &#x27;1 = Client is using their max&#x27;, &#x27;&gt;1 = Client is using their burst&#x27;]",
        dictionaryType=None
    )
    write_bytes = data_model.property(
        "writeBytes", int,
        array=False, optional=False,
        documentation="Total bytes written by clients.",
        dictionaryType=None
    )
    write_latency_usec = data_model.property(
        "writeLatencyUSec", int,
        array=False, optional=False,
        documentation="The average time, in microseconds, to complete write operations.",
        dictionaryType=None
    )
    write_ops = data_model.property(
        "writeOps", int,
        array=False, optional=False,
        documentation="Total write operations occurring on the volume.",
        dictionaryType=None
    )
    zero_blocks = data_model.property(
        "zeroBlocks", int,
        array=False, optional=False,
        documentation="Total number of 4KiB blocks without data after the last round of garbage collection operation has completed.",
        dictionaryType=None
    )
    write_bytes_last_sample = data_model.property(
        "writeBytesLastSample", int,
        array=False, optional=False,
        documentation="The total number of bytes written to the volume during the last sample period.",
        dictionaryType=None
    )
    sample_period_msec = data_model.property(
        "samplePeriodMSec", int,
        array=False, optional=False,
        documentation="The length of the sample period in milliseconds.",
        dictionaryType=None
    )
    read_bytes_last_sample = data_model.property(
        "readBytesLastSample", int,
        array=False, optional=False,
        documentation="The total number of bytes read from the volume during the last sample period.",
        dictionaryType=None
    )
    read_ops_last_sample = data_model.property(
        "readOpsLastSample", int,
        array=False, optional=False,
        documentation="The total number of read operations durin gth elast sample period.",
        dictionaryType=None
    )
    write_ops_last_sample = data_model.property(
        "writeOpsLastSample", int,
        array=False, optional=False,
        documentation="The total number of write operations during the last sample period.",
        dictionaryType=None
    )
    virtual_volume_id = data_model.property(
        "virtualVolumeID", UUID,
        array=False, optional=False,
        documentation="If the volume of interest is associated with a virtual volume, this is the virtual volume ID.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ListVolumeStatsByVolumeAccessGroupResult(data_model.DataObject):
    """ListVolumeStatsByVolumeAccessGroupResult  

    :param volume_stats: [required] List of account activity information. Note: The volumeID member is 0 for each entry, as the values represent the summation of all volumes owned by the account. 
    :type volume_stats: VolumeStats

    """
    volume_stats = data_model.property(
        "volumeStats", VolumeStats,
        array=True, optional=False,
        documentation="[&#x27;List of account activity information.&#x27;, &#x27;Note: The volumeID member is 0 for each entry, as the values represent the summation of all volumes owned by the account.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class CreateGroupSnapshotRequest(data_model.DataObject):
    """CreateGroupSnapshotRequest  

    :param volumes: [required] Unique ID of the volume image from which to copy. 
    :type volumes: int

    :param name:  A name for the snapshot. If no name is provided, the date and time the snapshot was taken is used. 
    :type name: str

    :param enable_remote_replication:  Identifies if snapshot is enabled for remote replication. 
    :type enable_remote_replication: bool

    :param retention:  The amount of time the snapshot will be retained. Enter in HH:mm:ss 
    :type retention: str

    :param attributes:  List of Name/Value pairs in JSON object format. 
    :type attributes: dict

    """
    volumes = data_model.property(
        "volumes", int,
        array=True, optional=False,
        documentation="Unique ID of the volume image from which to copy.",
        dictionaryType=None
    )
    name = data_model.property(
        "name", str,
        array=False, optional=True,
        documentation="[&#x27;A name for the snapshot.&#x27;, &#x27;If no name is provided, the date and time the snapshot was taken is used.&#x27;]",
        dictionaryType=None
    )
    enable_remote_replication = data_model.property(
        "enableRemoteReplication", bool,
        array=False, optional=True,
        documentation="Identifies if snapshot is enabled for remote replication.",
        dictionaryType=None
    )
    retention = data_model.property(
        "retention", str,
        array=False, optional=True,
        documentation="[&#x27;The amount of time the snapshot will be retained. Enter in HH:mm:ss&#x27;]",
        dictionaryType=None
    )
    attributes = data_model.property(
        "attributes", dict,
        array=False, optional=True,
        documentation="List of Name/Value pairs in JSON object format.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ModifyVolumeAccessGroupRequest(data_model.DataObject):
    """ModifyVolumeAccessGroupRequest  

    :param volume_access_group_id: [required] The ID of the volume access group to modify. 
    :type volume_access_group_id: int

    :param virtual_network_id:  The ID of the SolidFire Virtual Network ID to associate the volume access group with. 
    :type virtual_network_id: int

    :param virtual_network_tags:  The ID of the VLAN Virtual Network Tag to associate the volume access group with. 
    :type virtual_network_tags: int

    :param name:  Name of the volume access group. It is not required to be unique, but recommended. 
    :type name: str

    :param initiators:  List of initiators to include in the volume access group. If unspecified, the access group's configured initiators will not be modified. 
    :type initiators: str

    :param volumes:  List of volumes to initially include in the volume access group. If unspecified, the access group's volumes will not be modified. 
    :type volumes: int

    :param attributes:  List of Name/Value pairs in JSON object format. 
    :type attributes: dict

    """
    volume_access_group_id = data_model.property(
        "volumeAccessGroupID", int,
        array=False, optional=False,
        documentation="The ID of the volume access group to modify.",
        dictionaryType=None
    )
    virtual_network_id = data_model.property(
        "virtualNetworkID", int,
        array=True, optional=True,
        documentation="The ID of the SolidFire Virtual Network ID to associate the volume access group with.",
        dictionaryType=None
    )
    virtual_network_tags = data_model.property(
        "virtualNetworkTags", int,
        array=True, optional=True,
        documentation="The ID of the VLAN Virtual Network Tag to associate the volume access group with.",
        dictionaryType=None
    )
    name = data_model.property(
        "name", str,
        array=False, optional=True,
        documentation="[&#x27;Name of the volume access group.&#x27;, &#x27;It is not required to be unique, but recommended.&#x27;]",
        dictionaryType=None
    )
    initiators = data_model.property(
        "initiators", str,
        array=True, optional=True,
        documentation="[&#x27;List of initiators to include in the volume access group.&#x27;, &quot;If unspecified, the access group&#x27;s configured initiators will not be modified.&quot;]",
        dictionaryType=None
    )
    volumes = data_model.property(
        "volumes", int,
        array=True, optional=True,
        documentation="[&#x27;List of volumes to initially include in the volume access group.&#x27;, &quot;If unspecified, the access group&#x27;s volumes will not be modified.&quot;]",
        dictionaryType=None
    )
    attributes = data_model.property(
        "attributes", dict,
        array=False, optional=True,
        documentation="List of Name/Value pairs in JSON object format.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ModifySnapshotRequest(data_model.DataObject):
    """ModifySnapshotRequest  

    :param snapshot_id: [required] ID of the snapshot. 
    :type snapshot_id: int

    :param expiration_time:  Use to set the time when the snapshot should be removed. 
    :type expiration_time: str

    :param enable_remote_replication:  Use to enable the snapshot created to be replicated to a remote SolidFire cluster. Possible values: true: the snapshot will be replicated to remote storage. false: Default. No replication. 
    :type enable_remote_replication: bool

    """
    snapshot_id = data_model.property(
        "snapshotID", int,
        array=False, optional=False,
        documentation="ID of the snapshot.",
        dictionaryType=None
    )
    expiration_time = data_model.property(
        "expirationTime", str,
        array=False, optional=True,
        documentation="Use to set the time when the snapshot should be removed.",
        dictionaryType=None
    )
    enable_remote_replication = data_model.property(
        "enableRemoteReplication", bool,
        array=False, optional=True,
        documentation="[&#x27;Use to enable the snapshot created to be replicated to a remote SolidFire cluster.&#x27;, &#x27;Possible values:&#x27;, &#x27;true: the snapshot will be replicated to remote storage.&#x27;, &#x27;false: Default. No replication.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ClusterStats(data_model.DataObject):
    """ClusterStats  

    :param cluster_utilization: [required] The amount of cluster capacity being utilized. 
    :type cluster_utilization: float

    :param client_queue_depth: [required] 
    :type client_queue_depth: int

    :param read_bytes: [required] Total bytes read by clients. 
    :type read_bytes: int

    :param read_ops: [required] Total read operations. 
    :type read_ops: int

    :param timestamp: [required] Current time in UTC format. ISO 8601 date string. 
    :type timestamp: str

    :param write_bytes: [required] Total bytes written by clients. 
    :type write_bytes: int

    :param write_ops: [required] Total write operations. 
    :type write_ops: int

    """
    cluster_utilization = data_model.property(
        "clusterUtilization", float,
        array=False, optional=False,
        documentation="The amount of cluster capacity being utilized.",
        dictionaryType=None
    )
    client_queue_depth = data_model.property(
        "clientQueueDepth", int,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    read_bytes = data_model.property(
        "readBytes", int,
        array=False, optional=False,
        documentation="Total bytes read by clients.",
        dictionaryType=None
    )
    read_ops = data_model.property(
        "readOps", int,
        array=False, optional=False,
        documentation="Total read operations.",
        dictionaryType=None
    )
    timestamp = data_model.property(
        "timestamp", str,
        array=False, optional=False,
        documentation="Current time in UTC format. ISO 8601 date string.",
        dictionaryType=None
    )
    write_bytes = data_model.property(
        "writeBytes", int,
        array=False, optional=False,
        documentation="Total bytes written by clients.",
        dictionaryType=None
    )
    write_ops = data_model.property(
        "writeOps", int,
        array=False, optional=False,
        documentation="Total write operations.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class GetClusterStatsResult(data_model.DataObject):
    """GetClusterStatsResult  

    :param cluster_stats: [required] 
    :type cluster_stats: ClusterStats

    """
    cluster_stats = data_model.property(
        "clusterStats", ClusterStats,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class StartVolumePairingResult(data_model.DataObject):
    """StartVolumePairingResult  

    :param volume_pairing_key: [required] A string of characters that is used by the "CompleteVolumePairing" API method. 
    :type volume_pairing_key: str

    """
    volume_pairing_key = data_model.property(
        "volumePairingKey", str,
        array=False, optional=False,
        documentation="A string of characters that is used by the &quot;CompleteVolumePairing&quot; API method.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ScheduleInfo(data_model.DataObject):
    """ScheduleInfo  

    :param volume_ids:  A list of volume IDs to be included in the group snapshot. 
    :type volume_ids: int

    :param snapshot_name:  The snapshot name to be used.  
    :type snapshot_name: str

    :param enable_remote_replication:  Indicates if the snapshot should be included in remote replication. 
    :type enable_remote_replication: bool

    :param retention:  The amount of time the snapshot will be retained in HH:mm:ss. 
    :type retention: str

    """
    volume_ids = data_model.property(
        "volumeIDs", int,
        array=True, optional=True,
        documentation="A list of volume IDs to be included in the group snapshot.",
        dictionaryType=None
    )
    snapshot_name = data_model.property(
        "snapshotName", str,
        array=False, optional=True,
        documentation="The snapshot name to be used. ",
        dictionaryType=None
    )
    enable_remote_replication = data_model.property(
        "enableRemoteReplication", bool,
        array=False, optional=True,
        documentation="Indicates if the snapshot should be included in remote replication.",
        dictionaryType=None
    )
    retention = data_model.property(
        "retention", str,
        array=False, optional=True,
        documentation="The amount of time the snapshot will be retained in HH:mm:ss.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class Schedule(data_model.DataObject):
    """Schedule  
    Schedule is an object containing information about each schedule created to autonomously make a snapshot of a volume. The return object includes information for all schedules. If scheduleID is used to identify a specific schedule then only information for that scheduleID is returned. Schedules information is returned with the API method, see ListSchedules on the SolidFire API guide page 245.

    :param frequency: [required] Indicates the frequency of the schedule occurrence. Set this to a type that inherits from Frequency. Valid types are: DayOfWeekFrequency DayOfMonthFrequency TimeIntervalFrequency 
    :type frequency: Frequency

    :param has_error:  Indicates whether or not the schedule has errors. 
    :type has_error: bool

    :param last_run_status: [required] Indicates the status of the last scheduled snapshot. Valid values are: Success Failed 
    :type last_run_status: str

    :param last_run_time_started: [required] Indicates the last time the schedule started n ISO 8601 date string. Valid values are: Success Failed 
    :type last_run_time_started: str

    :param paused:  Indicates whether or not the schedule is paused. 
    :type paused: bool

    :param recurring:  Indicates whether or not the schedule is recurring. 
    :type recurring: bool

    :param run_next_interval:  Indicates whether or not the schedule will run the next time the scheduler is active. When set to "true", the schedule will run the next time the scheduler is active and then reset back to "false". 
    :type run_next_interval: bool

    :param schedule_id:  Unique ID of the schedule 
    :type schedule_id: int

    :param schedule_info: [required] Includes the unique name given to the schedule, the retention period for the snapshot that was created, and the volume ID of the volume from which the snapshot was created. 
    :type schedule_info: ScheduleInfo

    :param name: [required] Unique name assigned to the schedule. 
    :type name: str

    :param starting_date: [required] Indicates the date the first time the schedule began of will begin. Formatted in UTC time. 
    :type starting_date: str

    :param to_be_deleted:  Indicates if the schedule is marked for deletion. 
    :type to_be_deleted: bool

    """
    frequency = data_model.property(
        "frequency", Frequency,
        array=False, optional=False,
        documentation="[&#x27;Indicates the frequency of the schedule occurrence. Set this to a type that inherits from Frequency.&#x27;, &#x27;Valid types are:&#x27;, &#x27;DayOfWeekFrequency&#x27;, &#x27;DayOfMonthFrequency&#x27;, &#x27;TimeIntervalFrequency&#x27;]",
        dictionaryType=None
    )
    has_error = data_model.property(
        "hasError", bool,
        array=False, optional=True,
        documentation="[&#x27;Indicates whether or not the schedule has errors.&#x27;]",
        dictionaryType=None
    )
    last_run_status = data_model.property(
        "lastRunStatus", str,
        array=False, optional=False,
        documentation="[&#x27;Indicates the status of the last scheduled snapshot.&#x27;, &#x27;Valid values are:&#x27;, &#x27;Success&#x27;, &#x27;Failed&#x27;]",
        dictionaryType=None
    )
    last_run_time_started = data_model.property(
        "lastRunTimeStarted", str,
        array=False, optional=False,
        documentation="[&#x27;Indicates the last time the schedule started n ISO 8601 date string.&#x27;, &#x27;Valid values are:&#x27;, &#x27;Success&#x27;, &#x27;Failed&#x27;]",
        dictionaryType=None
    )
    paused = data_model.property(
        "paused", bool,
        array=False, optional=True,
        documentation="[&#x27;Indicates whether or not the schedule is paused.&#x27;]",
        dictionaryType=None
    )
    recurring = data_model.property(
        "recurring", bool,
        array=False, optional=True,
        documentation="[&#x27;Indicates whether or not the schedule is recurring.&#x27;]",
        dictionaryType=None
    )
    run_next_interval = data_model.property(
        "runNextInterval", bool,
        array=False, optional=True,
        documentation="[&#x27;Indicates whether or not the schedule will run the next time the scheduler is active. When set to &quot;true&quot;, the schedule will run the next time the scheduler is active and then reset back to &quot;false&quot;.&#x27;]",
        dictionaryType=None
    )
    schedule_id = data_model.property(
        "scheduleID", int,
        array=False, optional=True,
        documentation="[&#x27;Unique ID of the schedule&#x27;]",
        dictionaryType=None
    )
    schedule_info = data_model.property(
        "scheduleInfo", ScheduleInfo,
        array=False, optional=False,
        documentation="[&#x27;Includes the unique name given to the schedule, the retention period for the snapshot that was created, and the volume ID of the volume from which the snapshot was created.&#x27;]",
        dictionaryType=None
    )
    name = data_model.property(
        "name", str,
        array=False, optional=False,
        documentation="[&#x27;Unique name assigned to the schedule.&#x27;]",
        dictionaryType=None
    )
    starting_date = data_model.property(
        "startingDate", str,
        array=False, optional=False,
        documentation="[&#x27;Indicates the date the first time the schedule began of will begin. Formatted in UTC time.&#x27;]",
        dictionaryType=None
    )
    to_be_deleted = data_model.property(
        "toBeDeleted", bool,
        array=False, optional=True,
        documentation="[&#x27;Indicates if the schedule is marked for deletion.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class GetDriveHardwareInfoRequest(data_model.DataObject):
    """GetDriveHardwareInfoRequest  

    :param drive_id: [required] DriveID for the drive information requested. DriveIDs can be obtained via the "ListDrives" method. 
    :type drive_id: int

    """
    drive_id = data_model.property(
        "driveID", int,
        array=False, optional=False,
        documentation="DriveID for the drive information requested. DriveIDs can be obtained via the &quot;ListDrives&quot; method.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class StorageContainer(data_model.DataObject):
    """StorageContainer  

    :param name: [required] 
    :type name: str

    :param storage_container_id: [required] 
    :type storage_container_id: UUID

    :param account_id: [required] 
    :type account_id: int

    :param protocol_endpoint_type: [required] 
    :type protocol_endpoint_type: str

    :param initiator_secret: [required] 
    :type initiator_secret: str

    :param target_secret: [required] 
    :type target_secret: str

    :param status: [required] 
    :type status: str

    """
    name = data_model.property(
        "name", str,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    storage_container_id = data_model.property(
        "storageContainerID", UUID,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    account_id = data_model.property(
        "accountID", int,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    protocol_endpoint_type = data_model.property(
        "protocolEndpointType", str,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    initiator_secret = data_model.property(
        "initiatorSecret", str,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    target_secret = data_model.property(
        "targetSecret", str,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    status = data_model.property(
        "status", str,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ModifyStorageContainerResult(data_model.DataObject):
    """ModifyStorageContainerResult  

    :param storage_container: [required] 
    :type storage_container: StorageContainer

    """
    storage_container = data_model.property(
        "storageContainer", StorageContainer,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ClusterAdmin(data_model.DataObject):
    """ClusterAdmin  

    :param access: [required] 
    :type access: str

    :param cluster_admin_id: [required] 
    :type cluster_admin_id: int

    :param username: [required] 
    :type username: str

    :param attributes: [required] List of Name/Value pairs in JSON object format. 
    :type attributes: dict

    """
    access = data_model.property(
        "access", str,
        array=True, optional=False,
        documentation="",
        dictionaryType=None
    )
    cluster_admin_id = data_model.property(
        "clusterAdminID", int,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    username = data_model.property(
        "username", str,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    attributes = data_model.property(
        "attributes", dict,
        array=False, optional=False,
        documentation="List of Name/Value pairs in JSON object format.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ListClusterAdminsResult(data_model.DataObject):
    """ListClusterAdminsResult  

    :param cluster_admins: [required] Information about the cluster admin. 
    :type cluster_admins: ClusterAdmin

    """
    cluster_admins = data_model.property(
        "clusterAdmins", ClusterAdmin,
        array=True, optional=False,
        documentation="Information about the cluster admin.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class TestConnectSvipRequest(data_model.DataObject):
    """TestConnectSvipRequest  

    :param svip:  Optionally, use to test the storage connection of a different SVIP. This is not needed to test the connection to the target cluster. 
    :type svip: str

    """
    svip = data_model.property(
        "svip", str,
        array=False, optional=True,
        documentation="Optionally, use to test the storage connection of a different SVIP. This is not needed to test the connection to the target cluster.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ModifyVolumeResult(data_model.DataObject):
    """ModifyVolumeResult  

    :param volume: [required] Object containing information about the newly modified volume. 
    :type volume: Volume

    """
    volume = data_model.property(
        "volume", Volume,
        array=False, optional=False,
        documentation="Object containing information about the newly modified volume.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class CreateClusterResult(data_model.DataObject):
    """CreateClusterResult  

    """

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class TestConnectMvipDetails(data_model.DataObject):
    """TestConnectMvipDetails  

    :param ping_bytes: [required] Details of the ping tests with 56 Bytes and 1500 Bytes. 
    :type ping_bytes: str

    :param mvip: [required] The MVIP tested against. 
    :type mvip: str

    :param connected: [required] Whether the test could connect to the MVIP. 
    :type connected: bool

    """
    ping_bytes = data_model.property(
        "pingBytes", str,
        array=False, optional=False,
        documentation="Details of the ping tests with 56 Bytes and 1500 Bytes.",
        dictionaryType=None
    )
    mvip = data_model.property(
        "mvip", str,
        array=False, optional=False,
        documentation="The MVIP tested against.",
        dictionaryType=None
    )
    connected = data_model.property(
        "connected", bool,
        array=False, optional=False,
        documentation="Whether the test could connect to the MVIP.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class TestConnectMvipResult(data_model.DataObject):
    """TestConnectMvipResult  

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
        documentation="Information about the test operation",
        dictionaryType=None
    )
    duration = data_model.property(
        "duration", str,
        array=False, optional=False,
        documentation="The length of time required to run the test.",
        dictionaryType=None
    )
    result = data_model.property(
        "result", str,
        array=False, optional=False,
        documentation="The results of the entire test",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ClusterConfig(data_model.DataObject):
    """ClusterConfig  
    Cluster Config object returns information the node uses to communicate with the cluster.

    :param cipi:  Network interface used for cluster communication. 
    :type cipi: str

    :param cluster:  Unique cluster name. 
    :type cluster: str

    :param ensemble:  Nodes that are participating in the cluster. 
    :type ensemble: str

    :param mipi:  Network interface used for node management. 
    :type mipi: str

    :param name:  Unique cluster name. 
    :type name: str

    :param node_id:  
    :type node_id: int

    :param pending_node_id:  
    :type pending_node_id: int

    :param role:  Identifies the role of the node 
    :type role: str

    :param sipi:  Network interface used for storage. 
    :type sipi: str

    :param state:  
    :type state: str

    """
    cipi = data_model.property(
        "cipi", str,
        array=False, optional=True,
        documentation="Network interface used for cluster communication.",
        dictionaryType=None
    )
    cluster = data_model.property(
        "cluster", str,
        array=False, optional=True,
        documentation="Unique cluster name.",
        dictionaryType=None
    )
    ensemble = data_model.property(
        "ensemble", str,
        array=True, optional=True,
        documentation="Nodes that are participating in the cluster.",
        dictionaryType=None
    )
    mipi = data_model.property(
        "mipi", str,
        array=False, optional=True,
        documentation="Network interface used for node management.",
        dictionaryType=None
    )
    name = data_model.property(
        "name", str,
        array=False, optional=True,
        documentation="Unique cluster name.",
        dictionaryType=None
    )
    node_id = data_model.property(
        "nodeID", int,
        array=False, optional=True,
        documentation="",
        dictionaryType=None
    )
    pending_node_id = data_model.property(
        "pendingNodeID", int,
        array=False, optional=True,
        documentation="",
        dictionaryType=None
    )
    role = data_model.property(
        "role", str,
        array=False, optional=True,
        documentation="Identifies the role of the node",
        dictionaryType=None
    )
    sipi = data_model.property(
        "sipi", str,
        array=False, optional=True,
        documentation="Network interface used for storage.",
        dictionaryType=None
    )
    state = data_model.property(
        "state", str,
        array=False, optional=True,
        documentation="",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class PhysicalAdapter(data_model.DataObject):
    """PhysicalAdapter  

    :param address:  
    :type address: str

    :param mac_address:  
    :type mac_address: str

    :param mac_address_permanent:  
    :type mac_address_permanent: str

    :param mtu:  
    :type mtu: str

    :param netmask:  
    :type netmask: str

    :param network:  
    :type network: str

    :param up_and_running:  
    :type up_and_running: bool

    """
    address = data_model.property(
        "address", str,
        array=False, optional=True,
        documentation="",
        dictionaryType=None
    )
    mac_address = data_model.property(
        "macAddress", str,
        array=False, optional=True,
        documentation="",
        dictionaryType=None
    )
    mac_address_permanent = data_model.property(
        "macAddressPermanent", str,
        array=False, optional=True,
        documentation="",
        dictionaryType=None
    )
    mtu = data_model.property(
        "mtu", str,
        array=False, optional=True,
        documentation="",
        dictionaryType=None
    )
    netmask = data_model.property(
        "netmask", str,
        array=False, optional=True,
        documentation="",
        dictionaryType=None
    )
    network = data_model.property(
        "network", str,
        array=False, optional=True,
        documentation="",
        dictionaryType=None
    )
    up_and_running = data_model.property(
        "upAndRunning", bool,
        array=False, optional=True,
        documentation="",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class NetworkConfig(data_model.DataObject):
    """NetworkConfig  

    :param _default:  
    :type _default: bool

    :param bond_master: [required] 
    :type bond_master: str

    :param virtual_network_tag: [required] 
    :type virtual_network_tag: str

    :param address:  
    :type address: str

    :param auto:  
    :type auto: bool

    :param bond_downdelay:  
    :type bond_downdelay: str

    :param bond_fail_over_mac:  
    :type bond_fail_over_mac: str

    :param bond_primary_reselect:  
    :type bond_primary_reselect: str

    :param bond_lacp_rate:  
    :type bond_lacp_rate: str

    :param bond_miimon:  
    :type bond_miimon: str

    :param bond_mode:  
    :type bond_mode: str

    :param bond_slaves:  
    :type bond_slaves: str

    :param bond_updelay:  
    :type bond_updelay: str

    :param broadcast:  
    :type broadcast: str

    :param dns_nameservers:  
    :type dns_nameservers: str

    :param dns_search:  
    :type dns_search: str

    :param family:  
    :type family: str

    :param gateway:  
    :type gateway: str

    :param mac_address:  
    :type mac_address: str

    :param mac_address_permanent:  
    :type mac_address_permanent: str

    :param method:  
    :type method: str

    :param mtu:  
    :type mtu: str

    :param netmask:  
    :type netmask: str

    :param network:  
    :type network: str

    :param physical:  
    :type physical: PhysicalAdapter

    :param routes:  
    :type routes: str

    :param status:  
    :type status: str

    :param symmetric_route_rules:  
    :type symmetric_route_rules: str

    :param up_and_running:  
    :type up_and_running: bool

    """
    _default = data_model.property(
        "#default", bool,
        array=False, optional=True,
        documentation="",
        dictionaryType=None
    )
    bond_master = data_model.property(
        "bond-master", str,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    virtual_network_tag = data_model.property(
        "virtualNetworkTag", str,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    address = data_model.property(
        "address", str,
        array=False, optional=True,
        documentation="",
        dictionaryType=None
    )
    auto = data_model.property(
        "auto", bool,
        array=False, optional=True,
        documentation="",
        dictionaryType=None
    )
    bond_downdelay = data_model.property(
        "bond-downdelay", str,
        array=False, optional=True,
        documentation="",
        dictionaryType=None
    )
    bond_fail_over_mac = data_model.property(
        "bond-fail_over_mac", str,
        array=False, optional=True,
        documentation="",
        dictionaryType=None
    )
    bond_primary_reselect = data_model.property(
        "bond-primary_reselect", str,
        array=False, optional=True,
        documentation="",
        dictionaryType=None
    )
    bond_lacp_rate = data_model.property(
        "bond-lacp_rate", str,
        array=False, optional=True,
        documentation="",
        dictionaryType=None
    )
    bond_miimon = data_model.property(
        "bond-miimon", str,
        array=False, optional=True,
        documentation="",
        dictionaryType=None
    )
    bond_mode = data_model.property(
        "bond-mode", str,
        array=False, optional=True,
        documentation="",
        dictionaryType=None
    )
    bond_slaves = data_model.property(
        "bond-slaves", str,
        array=False, optional=True,
        documentation="",
        dictionaryType=None
    )
    bond_updelay = data_model.property(
        "bond-updelay", str,
        array=False, optional=True,
        documentation="",
        dictionaryType=None
    )
    broadcast = data_model.property(
        "broadcast", str,
        array=False, optional=True,
        documentation="",
        dictionaryType=None
    )
    dns_nameservers = data_model.property(
        "dns-nameservers", str,
        array=False, optional=True,
        documentation="",
        dictionaryType=None
    )
    dns_search = data_model.property(
        "dns-search", str,
        array=False, optional=True,
        documentation="",
        dictionaryType=None
    )
    family = data_model.property(
        "family", str,
        array=False, optional=True,
        documentation="",
        dictionaryType=None
    )
    gateway = data_model.property(
        "gateway", str,
        array=False, optional=True,
        documentation="",
        dictionaryType=None
    )
    mac_address = data_model.property(
        "macAddress", str,
        array=False, optional=True,
        documentation="",
        dictionaryType=None
    )
    mac_address_permanent = data_model.property(
        "macAddressPermanent", str,
        array=False, optional=True,
        documentation="",
        dictionaryType=None
    )
    method = data_model.property(
        "method", str,
        array=False, optional=True,
        documentation="",
        dictionaryType=None
    )
    mtu = data_model.property(
        "mtu", str,
        array=False, optional=True,
        documentation="",
        dictionaryType=None
    )
    netmask = data_model.property(
        "netmask", str,
        array=False, optional=True,
        documentation="",
        dictionaryType=None
    )
    network = data_model.property(
        "network", str,
        array=False, optional=True,
        documentation="",
        dictionaryType=None
    )
    physical = data_model.property(
        "physical", PhysicalAdapter,
        array=False, optional=True,
        documentation="",
        dictionaryType=None
    )
    routes = data_model.property(
        "routes", str,
        array=True, optional=True,
        documentation="",
        dictionaryType=None
    )
    status = data_model.property(
        "status", str,
        array=False, optional=True,
        documentation="",
        dictionaryType=None
    )
    symmetric_route_rules = data_model.property(
        "symmetricRouteRules", str,
        array=True, optional=True,
        documentation="",
        dictionaryType=None
    )
    up_and_running = data_model.property(
        "upAndRunning", bool,
        array=False, optional=True,
        documentation="",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class Network(data_model.DataObject):
    """Network  

    :param bond10_g:  
    :type bond10_g: NetworkConfig

    :param bond1_g:  
    :type bond1_g: NetworkConfig

    :param eth0:  
    :type eth0: NetworkConfig

    :param eth1:  
    :type eth1: NetworkConfig

    :param eth2:  
    :type eth2: NetworkConfig

    :param eth3:  
    :type eth3: NetworkConfig

    :param lo:  
    :type lo: NetworkConfig

    """
    bond10_g = data_model.property(
        "Bond10G", NetworkConfig,
        array=False, optional=True,
        documentation="",
        dictionaryType=None
    )
    bond1_g = data_model.property(
        "Bond1G", NetworkConfig,
        array=False, optional=True,
        documentation="",
        dictionaryType=None
    )
    eth0 = data_model.property(
        "eth0", NetworkConfig,
        array=False, optional=True,
        documentation="",
        dictionaryType=None
    )
    eth1 = data_model.property(
        "eth1", NetworkConfig,
        array=False, optional=True,
        documentation="",
        dictionaryType=None
    )
    eth2 = data_model.property(
        "eth2", NetworkConfig,
        array=False, optional=True,
        documentation="",
        dictionaryType=None
    )
    eth3 = data_model.property(
        "eth3", NetworkConfig,
        array=False, optional=True,
        documentation="",
        dictionaryType=None
    )
    lo = data_model.property(
        "lo", NetworkConfig,
        array=False, optional=True,
        documentation="",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class Config(data_model.DataObject):
    """Config  

    :param cluster: [required] 
    :type cluster: ClusterConfig

    :param network: [required] 
    :type network: Network

    """
    cluster = data_model.property(
        "cluster", ClusterConfig,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    network = data_model.property(
        "network", Network,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class SetConfigRequest(data_model.DataObject):
    """SetConfigRequest  

    :param config: [required] Objects that you want changed for the cluster interface settings. 
    :type config: Config

    """
    config = data_model.property(
        "config", Config,
        array=False, optional=False,
        documentation="Objects that you want changed for the cluster interface settings.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ListVolumeAccessGroupsRequest(data_model.DataObject):
    """ListVolumeAccessGroupsRequest  

    :param start_volume_access_group_id:  The lowest VolumeAccessGroupID to return. This can be useful for paging. If unspecified, there is no lower limit (implicitly 0). 
    :type start_volume_access_group_id: int

    :param limit:  The maximum number of results to return. This can be useful for paging. 
    :type limit: int

    """
    start_volume_access_group_id = data_model.property(
        "startVolumeAccessGroupID", int,
        array=False, optional=True,
        documentation="[&#x27;The lowest VolumeAccessGroupID to return.&#x27;, &#x27;This can be useful for paging.&#x27;, &#x27;If unspecified, there is no lower limit (implicitly 0).&#x27;]",
        dictionaryType=None
    )
    limit = data_model.property(
        "limit", int,
        array=False, optional=True,
        documentation="[&#x27;The maximum number of results to return.&#x27;, &#x27;This can be useful for paging.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class NodeStatsInfo(data_model.DataObject):
    """NodeStatsInfo  

    :param c_bytes_in: [required] Bytes in on the cluster interface. 
    :type c_bytes_in: int

    :param c_bytes_out: [required] Bytes out on the cluster interface. 
    :type c_bytes_out: int

    :param cpu: [required] CPU Usage % 
    :type cpu: int

    :param m_bytes_in: [required] Bytes in on the management interface. 
    :type m_bytes_in: int

    :param m_bytes_out: [required] Bytes out on the management interface. 
    :type m_bytes_out: int

    :param network_utilization_cluster: [required] Network interface utilization (in %) for the cluster network interface. 
    :type network_utilization_cluster: int

    :param network_utilization_storage: [required] Network interface utilization (in %) for the storage network interface. 
    :type network_utilization_storage: int

    :param node_id: [required] 
    :type node_id: int

    :param s_bytes_in: [required] Bytes in on the storage interface. 
    :type s_bytes_in: int

    :param s_bytes_out: [required] Bytes out on the storage interface. 
    :type s_bytes_out: int

    :param timestamp: [required] Current time in UTC format ISO 8691 date string. 
    :type timestamp: str

    :param used_memory: [required] Total memory usage in bytes. 
    :type used_memory: int

    """
    c_bytes_in = data_model.property(
        "cBytesIn", int,
        array=False, optional=False,
        documentation="Bytes in on the cluster interface.",
        dictionaryType=None
    )
    c_bytes_out = data_model.property(
        "cBytesOut", int,
        array=False, optional=False,
        documentation="Bytes out on the cluster interface.",
        dictionaryType=None
    )
    cpu = data_model.property(
        "cpu", int,
        array=False, optional=False,
        documentation="CPU Usage %",
        dictionaryType=None
    )
    m_bytes_in = data_model.property(
        "mBytesIn", int,
        array=False, optional=False,
        documentation="Bytes in on the management interface.",
        dictionaryType=None
    )
    m_bytes_out = data_model.property(
        "mBytesOut", int,
        array=False, optional=False,
        documentation="Bytes out on the management interface.",
        dictionaryType=None
    )
    network_utilization_cluster = data_model.property(
        "networkUtilizationCluster", int,
        array=False, optional=False,
        documentation="Network interface utilization (in %) for the cluster network interface.",
        dictionaryType=None
    )
    network_utilization_storage = data_model.property(
        "networkUtilizationStorage", int,
        array=False, optional=False,
        documentation="Network interface utilization (in %) for the storage network interface.",
        dictionaryType=None
    )
    node_id = data_model.property(
        "nodeID", int,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    s_bytes_in = data_model.property(
        "sBytesIn", int,
        array=False, optional=False,
        documentation="Bytes in on the storage interface.",
        dictionaryType=None
    )
    s_bytes_out = data_model.property(
        "sBytesOut", int,
        array=False, optional=False,
        documentation="Bytes out on the storage interface.",
        dictionaryType=None
    )
    timestamp = data_model.property(
        "timestamp", str,
        array=False, optional=False,
        documentation="Current time in UTC format ISO 8691 date string.",
        dictionaryType=None
    )
    used_memory = data_model.property(
        "usedMemory", int,
        array=False, optional=False,
        documentation="Total memory usage in bytes.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class GetNodeStatsResult(data_model.DataObject):
    """GetNodeStatsResult  

    :param node_stats: [required] Node activity information. 
    :type node_stats: NodeStatsInfo

    """
    node_stats = data_model.property(
        "nodeStats", NodeStatsInfo,
        array=False, optional=False,
        documentation="Node activity information.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class Initiator(data_model.DataObject):
    """Initiator  
    Object containing characteristics of each initiator

    :param alias: [required] The friendly name assigned to this initiator. (String) 
    :type alias: str

    :param initiator_id: [required] The numeric ID of the initiator that has been created. (Integer) 
    :type initiator_id: int

    :param initiator_name: [required] The name of the initiator that has been created. (String) 
    :type initiator_name: str

    :param volume_access_groups: [required] A list of volumeAccessGroupIDs to which this initiator belongs. (Array of Integers) 
    :type volume_access_groups: int

    :param attributes: [required] A set of JSON attributes assigned to this initiator. (JSON Object) 
    :type attributes: dict

    """
    alias = data_model.property(
        "alias", str,
        array=False, optional=False,
        documentation="[&#x27;The friendly name assigned to this initiator. (String)&#x27;]",
        dictionaryType=None
    )
    initiator_id = data_model.property(
        "initiatorID", int,
        array=False, optional=False,
        documentation="The numeric ID of the initiator that has been created. (Integer)",
        dictionaryType=None
    )
    initiator_name = data_model.property(
        "initiatorName", str,
        array=False, optional=False,
        documentation="The name of the initiator that has been created. (String)",
        dictionaryType=None
    )
    volume_access_groups = data_model.property(
        "volumeAccessGroups", int,
        array=True, optional=False,
        documentation="A list of volumeAccessGroupIDs to which this initiator belongs. (Array of Integers)",
        dictionaryType=None
    )
    attributes = data_model.property(
        "attributes", dict,
        array=False, optional=False,
        documentation="A set of JSON attributes assigned to this initiator. (JSON Object)",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class CreateInitiatorsResult(data_model.DataObject):
    """CreateInitiatorsResult  

    :param initiators: [required] List of objects containing details about the newly created initiators 
    :type initiators: Initiator

    """
    initiators = data_model.property(
        "initiators", Initiator,
        array=True, optional=False,
        documentation="List of objects containing details about the newly created initiators",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ListSnapshotsRequest(data_model.DataObject):
    """ListSnapshotsRequest  

    :param volume_id:  The volume to list snapshots for. If not provided, all snapshots for all volumes are returned. 
    :type volume_id: int

    """
    volume_id = data_model.property(
        "volumeID", int,
        array=False, optional=True,
        documentation="[&#x27;The volume to list snapshots for.&#x27;, &#x27;If not provided, all snapshots for all volumes are returned.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ShutdownRequest(data_model.DataObject):
    """ShutdownRequest  

    :param nodes: [required] List of NodeIDs for the nodes to be shutdown. 
    :type nodes: int

    :param option:  Action to take for the node shutdown:restart: Restarts the node.halt: Performs full power-off of the node. 
    :type option: str

    """
    nodes = data_model.property(
        "nodes", int,
        array=True, optional=False,
        documentation="List of NodeIDs for the nodes to be shutdown.",
        dictionaryType=None
    )
    option = data_model.property(
        "option", str,
        array=False, optional=True,
        documentation="Action to take for the node shutdown:restart: Restarts the node.halt: Performs full power-off of the node.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class RemoveNodesResult(data_model.DataObject):
    """RemoveNodesResult  

    """

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class QoS(data_model.DataObject):
    """QoS  
    Quality of Service (QoS) values are used on SolidFire volumes to provision performance expectations.
    Minimum, maximum and burst QoS values can be set within the ranges specified in the QoS table below.
    
    Volumes created without specified QoS values are created with the Default values listed below.
    Default values can be found by running the GetDefaultQoS method.
    
    minIOPS Min: 100/50 (v7.0/v8.0), Default: 100, Max: 15,000
    maxIOPS Min: 100/50 (v7.0/v8.0), Default: 15,000, Max: 100,000
    burstIOPS Min: 100/50 (v7.0/v8.0), Default: 15,000, Max: 100,000

    :param min_iops:  Desired minimum 4KB IOPS to guarantee. The allowed IOPS will only drop below this level if all volumes have been capped at their minimum IOPS value and there is still insufficient performance capacity. 
    :type min_iops: int

    :param max_iops:  Desired maximum 4KB IOPS allowed over an extended period of time. 
    :type max_iops: int

    :param burst_iops:  Maximum "peak" 4KB IOPS allowed for short periods of time. Allows for bursts of I/O activity over the normal max IOPS value. 
    :type burst_iops: int

    :param burst_time:  The length of time burst IOPS is allowed. The value returned is represented in time units of seconds. Note: this value is calculated by the system based on IOPS set for QoS. 
    :type burst_time: int

    """
    min_iops = data_model.property(
        "minIOPS", int,
        array=False, optional=True,
        documentation="[&#x27;Desired minimum 4KB IOPS to guarantee.&#x27;, &#x27;The allowed IOPS will only drop below this level if all volumes have been capped&#x27;, &#x27;at their minimum IOPS value and there is still insufficient performance capacity.&#x27;]",
        dictionaryType=None
    )
    max_iops = data_model.property(
        "maxIOPS", int,
        array=False, optional=True,
        documentation="[&#x27;Desired maximum 4KB IOPS allowed over an extended period of time.&#x27;]",
        dictionaryType=None
    )
    burst_iops = data_model.property(
        "burstIOPS", int,
        array=False, optional=True,
        documentation="[&#x27;Maximum &quot;peak&quot; 4KB IOPS allowed for short periods of time.&#x27;, &#x27;Allows for bursts of I/O activity over the normal max IOPS value.&#x27;]",
        dictionaryType=None
    )
    burst_time = data_model.property(
        "burstTime", int,
        array=False, optional=True,
        documentation="[&#x27;The length of time burst IOPS is allowed.&#x27;, &#x27;The value returned is represented in time units of seconds.&#x27;, &#x27;Note: this value is calculated by the system based on IOPS set for QoS.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ModifyVolumesRequest(data_model.DataObject):
    """ModifyVolumesRequest  

    :param volume_ids: [required] A list of volumeIDs for the volumes to be modified. 
    :type volume_ids: int

    :param account_id:  AccountID to which the volume is reassigned. If none is specified, the previous account name is used. 
    :type account_id: int

    :param access:  Access allowed for the volume. Possible values:readOnly: Only read operations are allowed.readWrite: Reads and writes are allowed.locked: No reads or writes are allowed.If not specified, the access value does not change.replicationTarget: Identify a volume as the target volume for a paired set of volumes. If the volume is not paired, the access status is locked.If a value is not specified, the access value does not change.  
    :type access: str

    :param qos:  New quality of service settings for this volume.If not specified, the QoS settings are not changed. 
    :type qos: QoS

    :param total_size:  New size of the volume in bytes. 1000000000 is equal to 1GB. Size is rounded up to the nearest 1MB in size. This parameter can only be used to increase the size of a volume. 
    :type total_size: int

    :param attributes:  
    :type attributes: dict

    """
    volume_ids = data_model.property(
        "volumeIDs", int,
        array=True, optional=False,
        documentation="A list of volumeIDs for the volumes to be modified.",
        dictionaryType=None
    )
    account_id = data_model.property(
        "accountID", int,
        array=False, optional=True,
        documentation="AccountID to which the volume is reassigned. If none is specified, the previous account name is used.",
        dictionaryType=None
    )
    access = data_model.property(
        "access", str,
        array=False, optional=True,
        documentation="Access allowed for the volume. Possible values:readOnly: Only read operations are allowed.readWrite: Reads and writes are allowed.locked: No reads or writes are allowed.If not specified, the access value does not change.replicationTarget: Identify a volume as the target volume for a paired set of volumes. If the volume is not paired, the access status is locked.If a value is not specified, the access value does not change. ",
        dictionaryType=None
    )
    qos = data_model.property(
        "qos", QoS,
        array=False, optional=True,
        documentation="New quality of service settings for this volume.If not specified, the QoS settings are not changed.",
        dictionaryType=None
    )
    total_size = data_model.property(
        "totalSize", int,
        array=False, optional=True,
        documentation="New size of the volume in bytes. 1000000000 is equal to 1GB. Size is rounded up to the nearest 1MB in size. This parameter can only be used to increase the size of a volume.",
        dictionaryType=None
    )
    attributes = data_model.property(
        "attributes", dict,
        array=False, optional=True,
        documentation="",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ListVolumesResult(data_model.DataObject):
    """ListVolumesResult  

    :param volumes: [required] List of volumes. 
    :type volumes: Volume

    """
    volumes = data_model.property(
        "volumes", Volume,
        array=True, optional=False,
        documentation="List of volumes.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class StartBulkVolumeWriteResult(data_model.DataObject):
    """StartBulkVolumeWriteResult  

    :param async_handle: [required] ID of the async process to be checked for completion. 
    :type async_handle: int

    :param key: [required] Opaque key uniquely identifying the session. 
    :type key: str

    :param url: [required] URL to access the node's web server 
    :type url: str

    """
    async_handle = data_model.property(
        "asyncHandle", int,
        array=False, optional=False,
        documentation="ID of the async process to be checked for completion.",
        dictionaryType=None
    )
    key = data_model.property(
        "key", str,
        array=False, optional=False,
        documentation="Opaque key uniquely identifying the session.",
        dictionaryType=None
    )
    url = data_model.property(
        "url", str,
        array=False, optional=False,
        documentation="URL to access the node&#x27;s web server",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class LoggingServer(data_model.DataObject):
    """LoggingServer  

    :param host: [required] Hostname or IP address of the log server. 
    :type host: str

    :param port: [required] Port number that the log server is listening on. 
    :type port: int

    """
    host = data_model.property(
        "host", str,
        array=False, optional=False,
        documentation="Hostname or IP address of the log server.",
        dictionaryType=None
    )
    port = data_model.property(
        "port", int,
        array=False, optional=False,
        documentation="Port number that the log server is listening on.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class GetRemoteLoggingHostsResult(data_model.DataObject):
    """GetRemoteLoggingHostsResult  

    :param remote_hosts: [required] List of hosts to forward logging information to. 
    :type remote_hosts: LoggingServer

    """
    remote_hosts = data_model.property(
        "remoteHosts", LoggingServer,
        array=True, optional=False,
        documentation="[&#x27;List of hosts to forward logging information to.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class LunAssignment(data_model.DataObject):
    """LunAssignment  
    VolumeID and Lun assignment.

    :param volume_id: [required] The volume ID assigned to the Lun. 
    :type volume_id: int

    :param lun: [required] Correct LUN values are 0 - 16383. An exception will be seen if an incorrect LUN value is passed. 
    :type lun: int

    """
    volume_id = data_model.property(
        "volumeID", int,
        array=False, optional=False,
        documentation="The volume ID assigned to the Lun.",
        dictionaryType=None
    )
    lun = data_model.property(
        "lun", int,
        array=False, optional=False,
        documentation="Correct LUN values are 0 - 16383. An exception will be seen if an incorrect LUN value is passed.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ModifyVolumeAccessGroupLunAssignmentsRequest(data_model.DataObject):
    """ModifyVolumeAccessGroupLunAssignmentsRequest  

    :param volume_access_group_id: [required] Unique volume access group ID for which the LUN assignments will be modified. 
    :type volume_access_group_id: int

    :param lun_assignments: [required] The volume IDs with new assigned LUN values. 
    :type lun_assignments: LunAssignment

    """
    volume_access_group_id = data_model.property(
        "volumeAccessGroupID", int,
        array=False, optional=False,
        documentation="Unique volume access group ID for which the LUN assignments will be modified.",
        dictionaryType=None
    )
    lun_assignments = data_model.property(
        "lunAssignments", LunAssignment,
        array=True, optional=False,
        documentation="The volume IDs with new assigned LUN values.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class Platform(data_model.DataObject):
    """Platform  

    :param node_type: [required] SolidFire's name for this platform. 
    :type node_type: str

    :param chassis_type: [required] Name of the chassis (example: "R620"). 
    :type chassis_type: str

    :param cpu_model: [required] The model of CPU used on this platform. 
    :type cpu_model: str

    :param node_memory_gb: [required] The amount of memory on this platform in GiB. 
    :type node_memory_gb: int

    """
    node_type = data_model.property(
        "nodeType", str,
        array=False, optional=False,
        documentation="SolidFire&#x27;s name for this platform.",
        dictionaryType=None
    )
    chassis_type = data_model.property(
        "chassisType", str,
        array=False, optional=False,
        documentation="Name of the chassis (example: &quot;R620&quot;).",
        dictionaryType=None
    )
    cpu_model = data_model.property(
        "cpuModel", str,
        array=False, optional=False,
        documentation="The model of CPU used on this platform.",
        dictionaryType=None
    )
    node_memory_gb = data_model.property(
        "nodeMemoryGB", int,
        array=False, optional=False,
        documentation="The amount of memory on this platform in GiB.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class PendingNode(data_model.DataObject):
    """PendingNode  
    A "pending node" is one that has not yet joined the cluster.
    It can be added to a cluster using the AddNode method.

    :param pending_node_id: [required] 
    :type pending_node_id: int

    :param assigned_node_id: [required] 
    :type assigned_node_id: int

    :param name: [required] The host name for this node. 
    :type name: str

    :param compatible: [required] 
    :type compatible: bool

    :param platform_info: [required] Information about the platform this node is. 
    :type platform_info: Platform

    :param cip: [required] IP address used for both intra- and inter-cluster communication. 
    :type cip: str

    :param cipi: [required] The machine's name for the "cip" interface. 
    :type cipi: str

    :param mip: [required] IP address used for cluster management (hosting the API and web site). 
    :type mip: str

    :param mipi: [required] The machine's name for the "mip" interface. 
    :type mipi: str

    :param sip: [required] IP address used for iSCSI traffic. 
    :type sip: str

    :param sipi: [required] The machine's name for the "sip" interface. 
    :type sipi: str

    :param software_version: [required] The version of SolidFire software this node is currently running. 
    :type software_version: str

    :param uuid: [required] UUID of node. 
    :type uuid: UUID

    """
    pending_node_id = data_model.property(
        "pendingNodeID", int,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    assigned_node_id = data_model.property(
        "AssignedNodeID", int,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    name = data_model.property(
        "name", str,
        array=False, optional=False,
        documentation="The host name for this node.",
        dictionaryType=None
    )
    compatible = data_model.property(
        "compatible", bool,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    platform_info = data_model.property(
        "platformInfo", Platform,
        array=False, optional=False,
        documentation="Information about the platform this node is.",
        dictionaryType=None
    )
    cip = data_model.property(
        "cip", str,
        array=False, optional=False,
        documentation="[&#x27;IP address used for both intra- and inter-cluster communication.&#x27;]",
        dictionaryType=None
    )
    cipi = data_model.property(
        "cipi", str,
        array=False, optional=False,
        documentation="The machine&#x27;s name for the &quot;cip&quot; interface.",
        dictionaryType=None
    )
    mip = data_model.property(
        "mip", str,
        array=False, optional=False,
        documentation="[&#x27;IP address used for cluster management (hosting the API and web site).&#x27;]",
        dictionaryType=None
    )
    mipi = data_model.property(
        "mipi", str,
        array=False, optional=False,
        documentation="The machine&#x27;s name for the &quot;mip&quot; interface.",
        dictionaryType=None
    )
    sip = data_model.property(
        "sip", str,
        array=False, optional=False,
        documentation="[&#x27;IP address used for iSCSI traffic.&#x27;]",
        dictionaryType=None
    )
    sipi = data_model.property(
        "sipi", str,
        array=False, optional=False,
        documentation="The machine&#x27;s name for the &quot;sip&quot; interface.",
        dictionaryType=None
    )
    software_version = data_model.property(
        "softwareVersion", str,
        array=False, optional=False,
        documentation="The version of SolidFire software this node is currently running.",
        dictionaryType=None
    )
    uuid = data_model.property(
        "uuid", UUID,
        array=False, optional=False,
        documentation="UUID of node.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ListPendingNodesResult(data_model.DataObject):
    """ListPendingNodesResult  

    :param pending_nodes: [required] 
    :type pending_nodes: PendingNode

    """
    pending_nodes = data_model.property(
        "pendingNodes", PendingNode,
        array=True, optional=False,
        documentation="",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class RemoveClusterPairResult(data_model.DataObject):
    """RemoveClusterPairResult  

    """

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class CancelGroupCloneResult(data_model.DataObject):
    """CancelGroupCloneResult  

    """

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class LdapConfiguration(data_model.DataObject):
    """LdapConfiguration  
    LDAP Configuration object returns information about the LDAP configuration on SolidFire storage. LDAP information is returned with the API method GetLdapConfiguration.

    :param auth_type: [required] Identifies which user authentcation method will be used.  Valid values: DirectBind SearchAndBind 
    :type auth_type: str

    :param enabled: [required] Identifies whether or not the system is enabled for LDAP.  Valid values: true false 
    :type enabled: bool

    :param group_search_base_dn: [required] The base DN of the tree to start the group search (will do a subtree search from here). 
    :type group_search_base_dn: str

    :param group_search_custom_filter: [required] The custom search filter used. 
    :type group_search_custom_filter: str

    :param group_search_type: [required] Controls the default group search filter used, can be one of the following: NoGroups: No group support. ActiveDirectory: Nested membership of all of a user's AD groups. MemberDN: MemberDN style groups (single-level). 
    :type group_search_type: str

    :param search_bind_dn: [required] A fully qualified DN to log in with to perform an LDAP search for the user (needs read access to the LDAP directory). 
    :type search_bind_dn: str

    :param server_uris: [required] A comma-separated list of LDAP server URIs (examples: "ldap://1.2.3.4" and ldaps://1.2.3.4:123") 
    :type server_uris: str

    :param user_dntemplate: [required] A string that is used to form a fully qualified user DN. 
    :type user_dntemplate: str

    :param user_search_base_dn: [required] The base DN of the tree used to start the search (will do a subtree search from here). 
    :type user_search_base_dn: str

    :param user_search_filter: [required] The LDAP filter used. 
    :type user_search_filter: str

    """
    auth_type = data_model.property(
        "authType", str,
        array=False, optional=False,
        documentation="[&#x27;Identifies which user authentcation method will be used. &#x27;, &#x27;Valid values:&#x27;, &#x27;DirectBind&#x27;, &#x27;SearchAndBind&#x27;]",
        dictionaryType=None
    )
    enabled = data_model.property(
        "enabled", bool,
        array=False, optional=False,
        documentation="[&#x27;Identifies whether or not the system is enabled for LDAP. &#x27;, &#x27;Valid values:&#x27;, &#x27;true&#x27;, &#x27;false&#x27;]",
        dictionaryType=None
    )
    group_search_base_dn = data_model.property(
        "groupSearchBaseDN", str,
        array=False, optional=False,
        documentation="[&#x27;The base DN of the tree to start the group search (will do a subtree search from here).&#x27;]",
        dictionaryType=None
    )
    group_search_custom_filter = data_model.property(
        "groupSearchCustomFilter", str,
        array=False, optional=False,
        documentation="[&#x27;The custom search filter used.&#x27;]",
        dictionaryType=None
    )
    group_search_type = data_model.property(
        "groupSearchType", str,
        array=False, optional=False,
        documentation="[&#x27;Controls the default group search filter used, can be one of the following:&#x27;, &#x27;NoGroups: No group support.&#x27;, &quot;ActiveDirectory: Nested membership of all of a user&#x27;s AD groups.&quot;, &#x27;MemberDN: MemberDN style groups (single-level).&#x27;]",
        dictionaryType=None
    )
    search_bind_dn = data_model.property(
        "searchBindDN", str,
        array=False, optional=False,
        documentation="[&#x27;A fully qualified DN to log in with to perform an LDAP search for the user (needs read access to the LDAP directory).&#x27;]",
        dictionaryType=None
    )
    server_uris = data_model.property(
        "serverURIs", str,
        array=True, optional=False,
        documentation="[&#x27;A comma-separated list of LDAP server URIs (examples: &quot;ldap://1.2.3.4&quot; and ldaps://1.2.3.4:123&quot;)&#x27;]",
        dictionaryType=None
    )
    user_dntemplate = data_model.property(
        "userDNTemplate", str,
        array=False, optional=False,
        documentation="[&#x27;A string that is used to form a fully qualified user DN.&#x27;]",
        dictionaryType=None
    )
    user_search_base_dn = data_model.property(
        "userSearchBaseDN", str,
        array=False, optional=False,
        documentation="[&#x27;The base DN of the tree used to start the search (will do a subtree search from here).&#x27;]",
        dictionaryType=None
    )
    user_search_filter = data_model.property(
        "userSearchFilter", str,
        array=False, optional=False,
        documentation="[&#x27;The LDAP filter used.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class RemoveAccountResult(data_model.DataObject):
    """RemoveAccountResult  

    """

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ModifyInitiator(data_model.DataObject):
    """ModifyInitiator  
    Object containing characteristics of each initiator to modify

    :param initiator_id: [required] (Required) The numeric ID of the initiator to modify. (Integer) 
    :type initiator_id: int

    :param alias:  (Optional) A new friendly name to assign to the initiator. (String) 
    :type alias: str

    :param volume_access_group_id:  (Optional) The ID of the volume access group into to which the newly created initiator should be added. If the initiator was previously in a different volume access group, it is removed from the old volume access group. If this key is present but null, the initiator is removed from its current volume access group, but not placed in any new volume access group. (Integer) 
    :type volume_access_group_id: int

    :param attributes:  (Optional) A new set of JSON attributes assigned to this initiator. (JSON Object) 
    :type attributes: dict

    """
    initiator_id = data_model.property(
        "initiatorID", int,
        array=False, optional=False,
        documentation="(Required) The numeric ID of the initiator to modify. (Integer)",
        dictionaryType=None
    )
    alias = data_model.property(
        "alias", str,
        array=False, optional=True,
        documentation="[&#x27;(Optional) A new friendly name to assign to the initiator. (String)&#x27;]",
        dictionaryType=None
    )
    volume_access_group_id = data_model.property(
        "volumeAccessGroupID", int,
        array=False, optional=True,
        documentation="(Optional) The ID of the volume access group into to which the newly created initiator should be added. If the initiator was previously in a different volume access group, it is removed from the old volume access group. If this key is present but null, the initiator is removed from its current volume access group, but not placed in any new volume access group. (Integer)",
        dictionaryType=None
    )
    attributes = data_model.property(
        "attributes", dict,
        array=False, optional=True,
        documentation="(Optional) A new set of JSON attributes assigned to this initiator. (JSON Object)",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class AddedNode(data_model.DataObject):
    """AddedNode  

    :param node_id: [required] 
    :type node_id: int

    :param pending_node_id: [required] 
    :type pending_node_id: int

    """
    node_id = data_model.property(
        "nodeID", int,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    pending_node_id = data_model.property(
        "pendingNodeID", int,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class AddNodesResult(data_model.DataObject):
    """AddNodesResult  

    :param nodes: [required] An array of objects mapping the previous "pendingNodeID" to the "nodeID". 
    :type nodes: AddedNode

    """
    nodes = data_model.property(
        "nodes", AddedNode,
        array=True, optional=False,
        documentation="An array of objects mapping the previous &quot;pendingNodeID&quot; to the &quot;nodeID&quot;.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class GetEfficiencyResult(data_model.DataObject):
    """GetEfficiencyResult  

    :param compression:  The amount of space being saved by compressing data on a single volume. Stated as a ratio where "1" means data has been stored without being compressed. 
    :type compression: float

    :param deduplication:  The amount of space being saved on a single volume by not duplicating data. Stated as a ratio. 
    :type deduplication: float

    :param thin_provisioning:  The ratio of space used to the amount of space allocated for storing data. Stated as a ratio. 
    :type thin_provisioning: float

    :param timestamp: [required] The last time efficiency data was collected after Garbage Collection (GC). ISO 8601 data string. 
    :type timestamp: str

    :param missing_volumes: [required] The volumes that could not be queried for efficiency data. Missing volumes can be caused by GC being less than hour old, temporary network loss or restarted services since the GC cycle. 
    :type missing_volumes: int

    """
    compression = data_model.property(
        "compression", float,
        array=False, optional=True,
        documentation="The amount of space being saved by compressing data on a single volume. Stated as a ratio where &quot;1&quot; means data has been stored without being compressed.",
        dictionaryType=None
    )
    deduplication = data_model.property(
        "deduplication", float,
        array=False, optional=True,
        documentation="The amount of space being saved on a single volume by not duplicating data. Stated as a ratio.",
        dictionaryType=None
    )
    thin_provisioning = data_model.property(
        "thinProvisioning", float,
        array=False, optional=True,
        documentation="The ratio of space used to the amount of space allocated for storing data. Stated as a ratio.",
        dictionaryType=None
    )
    timestamp = data_model.property(
        "timestamp", str,
        array=False, optional=False,
        documentation="The last time efficiency data was collected after Garbage Collection (GC). ISO 8601 data string.",
        dictionaryType=None
    )
    missing_volumes = data_model.property(
        "missingVolumes", int,
        array=True, optional=False,
        documentation="The volumes that could not be queried for efficiency data. Missing volumes can be caused by GC being less than hour old, temporary network loss or restarted services since the GC cycle.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class SetNtpInfoRequest(data_model.DataObject):
    """SetNtpInfoRequest  

    :param servers: [required] List of NTP servers to add to each node's NTP configuration. 
    :type servers: str

    :param broadcastclient:  Enable every node in the cluster as a broadcase client. 
    :type broadcastclient: bool

    """
    servers = data_model.property(
        "servers", str,
        array=True, optional=False,
        documentation="List of NTP servers to add to each node&#x27;s NTP configuration.",
        dictionaryType=None
    )
    broadcastclient = data_model.property(
        "broadcastclient", bool,
        array=False, optional=True,
        documentation="Enable every node in the cluster as a broadcase client.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class GetAPIResult(data_model.DataObject):
    """GetAPIResult  

    :param current_version: [required] 
    :type current_version: float

    :param supported_versions: [required] 
    :type supported_versions: float

    """
    current_version = data_model.property(
        "currentVersion", float,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    supported_versions = data_model.property(
        "supportedVersions", float,
        array=True, optional=False,
        documentation="",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class RollbackToGroupSnapshotRequest(data_model.DataObject):
    """RollbackToGroupSnapshotRequest  

    :param group_snapshot_id: [required] Unique ID of the group snapshot. 
    :type group_snapshot_id: int

    :param save_current_state: [required] true: The previous active volume image is kept. false: (default) The previous active volume image is deleted. 
    :type save_current_state: bool

    :param name:  Name for the snapshot. If no name is given, then the name of the snapshot being rolled back to is used with  "-copy" appended to the end of the name. 
    :type name: str

    :param attributes:  List of Name/Value pairs in JSON object format 
    :type attributes: dict

    """
    group_snapshot_id = data_model.property(
        "groupSnapshotID", int,
        array=False, optional=False,
        documentation="[&#x27;Unique ID of the group snapshot.&#x27;]",
        dictionaryType=None
    )
    save_current_state = data_model.property(
        "saveCurrentState", bool,
        array=False, optional=False,
        documentation="[&#x27;true: The previous active volume image is kept.&#x27;, &#x27;false: (default) The previous active volume image is deleted.&#x27;]",
        dictionaryType=None
    )
    name = data_model.property(
        "name", str,
        array=False, optional=True,
        documentation="[&#x27;Name for the snapshot. If no name is given, then the name of the snapshot being rolled back to is used with &#x27;, &#x27;&quot;-copy&quot; appended to the end of the name.&#x27;]",
        dictionaryType=None
    )
    attributes = data_model.property(
        "attributes", dict,
        array=False, optional=True,
        documentation="[&#x27;List of Name/Value pairs in JSON object format&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class FeatureObject(data_model.DataObject):
    """FeatureObject  

    :param enabled: [required] True if the feature is enabled, otherwise false. 
    :type enabled: bool

    :param feature: [required] The name of the feature. 
    :type feature: str

    """
    enabled = data_model.property(
        "enabled", bool,
        array=False, optional=False,
        documentation="True if the feature is enabled, otherwise false.",
        dictionaryType=None
    )
    feature = data_model.property(
        "feature", str,
        array=False, optional=False,
        documentation="The name of the feature.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class GetFeatureStatusResult(data_model.DataObject):
    """GetFeatureStatusResult  

    :param features: [required] An array of feature objects indicating the feature name and its status. 
    :type features: FeatureObject

    """
    features = data_model.property(
        "features", FeatureObject,
        array=True, optional=False,
        documentation="An array of feature objects indicating the feature name and its status.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class RemoveVolumePairResult(data_model.DataObject):
    """RemoveVolumePairResult  

    """

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class GetLimitsResult(data_model.DataObject):
    """GetLimitsResult  
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

    :param initiator_count_max: [required] 
    :type initiator_count_max: int

    :param initiators_per_volume_access_group_count_max: [required] 
    :type initiators_per_volume_access_group_count_max: int

    :param iscsi_sessions_from_fibre_channel_nodes_max: [required] 
    :type iscsi_sessions_from_fibre_channel_nodes_max: int

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

    :param initiator_alias_length_max: [required] 
    :type initiator_alias_length_max: int

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
        documentation="",
        dictionaryType=None
    )
    account_name_length_max = data_model.property(
        "accountNameLengthMax", int,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    account_name_length_min = data_model.property(
        "accountNameLengthMin", int,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    bulk_volume_jobs_per_node_max = data_model.property(
        "bulkVolumeJobsPerNodeMax", int,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    bulk_volume_jobs_per_volume_max = data_model.property(
        "bulkVolumeJobsPerVolumeMax", int,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    clone_jobs_per_volume_max = data_model.property(
        "cloneJobsPerVolumeMax", int,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    cluster_pairs_count_max = data_model.property(
        "clusterPairsCountMax", int,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    initiator_name_length_max = data_model.property(
        "initiatorNameLengthMax", int,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    initiator_count_max = data_model.property(
        "initiatorCountMax", int,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    initiators_per_volume_access_group_count_max = data_model.property(
        "initiatorsPerVolumeAccessGroupCountMax", int,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    iscsi_sessions_from_fibre_channel_nodes_max = data_model.property(
        "iscsiSessionsFromFibreChannelNodesMax", int,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    secret_length_max = data_model.property(
        "secretLengthMax", int,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    secret_length_min = data_model.property(
        "secretLengthMin", int,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    snapshot_name_length_max = data_model.property(
        "snapshotNameLengthMax", int,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    snapshots_per_volume_max = data_model.property(
        "snapshotsPerVolumeMax", int,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    volume_access_group_count_max = data_model.property(
        "volumeAccessGroupCountMax", int,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    volume_access_group_lun_max = data_model.property(
        "volumeAccessGroupLunMax", int,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    volume_access_group_name_length_max = data_model.property(
        "volumeAccessGroupNameLengthMax", int,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    volume_access_group_name_length_min = data_model.property(
        "volumeAccessGroupNameLengthMin", int,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    volume_access_groups_per_initiator_count_max = data_model.property(
        "volumeAccessGroupsPerInitiatorCountMax", int,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    volume_access_groups_per_volume_count_max = data_model.property(
        "volumeAccessGroupsPerVolumeCountMax", int,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    initiator_alias_length_max = data_model.property(
        "initiatorAliasLengthMax", int,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    volume_burst_iopsmax = data_model.property(
        "volumeBurstIOPSMax", int,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    volume_burst_iopsmin = data_model.property(
        "volumeBurstIOPSMin", int,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    volume_count_max = data_model.property(
        "volumeCountMax", int,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    volume_max_iopsmax = data_model.property(
        "volumeMaxIOPSMax", int,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    volume_max_iopsmin = data_model.property(
        "volumeMaxIOPSMin", int,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    volume_min_iopsmax = data_model.property(
        "volumeMinIOPSMax", int,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    volume_min_iopsmin = data_model.property(
        "volumeMinIOPSMin", int,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    volume_name_length_max = data_model.property(
        "volumeNameLengthMax", int,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    volume_name_length_min = data_model.property(
        "volumeNameLengthMin", int,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    volume_size_max = data_model.property(
        "volumeSizeMax", int,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    volume_size_min = data_model.property(
        "volumeSizeMin", int,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    volumes_per_account_count_max = data_model.property(
        "volumesPerAccountCountMax", int,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    volumes_per_group_snapshot_max = data_model.property(
        "volumesPerGroupSnapshotMax", int,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    volumes_per_volume_access_group_count_max = data_model.property(
        "volumesPerVolumeAccessGroupCountMax", int,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class RemoveNodesRequest(data_model.DataObject):
    """RemoveNodesRequest  

    :param nodes: [required] List of NodeIDs for the nodes to be removed. 
    :type nodes: int

    """
    nodes = data_model.property(
        "nodes", int,
        array=True, optional=False,
        documentation="List of NodeIDs for the nodes to be removed.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ListVirtualNetworksRequest(data_model.DataObject):
    """ListVirtualNetworksRequest  

    :param virtual_network_id:  Network ID to filter the list for a single virtual network 
    :type virtual_network_id: int

    :param virtual_network_tag:  Network Tag to filter the list for a single virtual network 
    :type virtual_network_tag: int

    :param virtual_network_ids:  NetworkIDs to include in the list. 
    :type virtual_network_ids: int

    :param virtual_network_tags:  Network Tags to include in the list. 
    :type virtual_network_tags: int

    """
    virtual_network_id = data_model.property(
        "virtualNetworkID", int,
        array=False, optional=True,
        documentation="Network ID to filter the list for a single virtual network",
        dictionaryType=None
    )
    virtual_network_tag = data_model.property(
        "virtualNetworkTag", int,
        array=False, optional=True,
        documentation="Network Tag to filter the list for a single virtual network",
        dictionaryType=None
    )
    virtual_network_ids = data_model.property(
        "virtualNetworkIDs", int,
        array=True, optional=True,
        documentation="NetworkIDs to include in the list.",
        dictionaryType=None
    )
    virtual_network_tags = data_model.property(
        "virtualNetworkTags", int,
        array=True, optional=True,
        documentation="Network Tags to include in the list.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class RemoveAccountRequest(data_model.DataObject):
    """RemoveAccountRequest  

    :param account_id: [required] AccountID for the account to remove. 
    :type account_id: int

    """
    account_id = data_model.property(
        "accountID", int,
        array=False, optional=False,
        documentation="AccountID for the account to remove.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class TestConnectEnsembleDetails(data_model.DataObject):
    """TestConnectEnsembleDetails  

    :param nodes: [required] A list of each ensemble node in the test and the results of the tests. 
    :type nodes: str

    """
    nodes = data_model.property(
        "nodes", str,
        array=False, optional=False,
        documentation="A list of each ensemble node in the test and the results of the tests.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class TestConnectEnsembleResult(data_model.DataObject):
    """TestConnectEnsembleResult  

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
        documentation="",
        dictionaryType=None
    )
    duration = data_model.property(
        "duration", str,
        array=False, optional=False,
        documentation="The length of time required to run the test.",
        dictionaryType=None
    )
    result = data_model.property(
        "result", str,
        array=False, optional=False,
        documentation="The results of the entire test",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class GetStorageContainerEfficiencyRequest(data_model.DataObject):
    """GetStorageContainerEfficiencyRequest  

    :param storage_container_id: [required] The ID of the storage container for which to retrieve efficiency information. 
    :type storage_container_id: UUID

    """
    storage_container_id = data_model.property(
        "storageContainerID", UUID,
        array=False, optional=False,
        documentation="The ID of the storage container for which to retrieve efficiency information.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class CreateStorageContainerResult(data_model.DataObject):
    """CreateStorageContainerResult  

    :param storage_container: [required] 
    :type storage_container: StorageContainer

    """
    storage_container = data_model.property(
        "storageContainer", StorageContainer,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ISCSISession(data_model.DataObject):
    """ISCSISession  

    :param account_id: [required] 
    :type account_id: int

    :param initiator: [required] 
    :type initiator: Initiator

    :param account_name: [required] 
    :type account_name: str

    :param drive_id: [required] 
    :type drive_id: int

    :param initiator_ip: [required] 
    :type initiator_ip: str

    :param initiator_port_name: [required] 
    :type initiator_port_name: str

    :param target_port_name: [required] 
    :type target_port_name: str

    :param initiator_name: [required] 
    :type initiator_name: str

    :param node_id: [required] 
    :type node_id: int

    :param service_id: [required] 
    :type service_id: int

    :param session_id: [required] 
    :type session_id: int

    :param target_name: [required] 
    :type target_name: str

    :param target_ip: [required] 
    :type target_ip: str

    :param virtual_network_id: [required] 
    :type virtual_network_id: int

    :param volume_id: [required] 
    :type volume_id: int

    :param create_time: [required] 
    :type create_time: str

    :param volume_instance: [required] 
    :type volume_instance: int

    :param initiator_session_id: [required] 
    :type initiator_session_id: int

    """
    account_id = data_model.property(
        "accountID", int,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    initiator = data_model.property(
        "initiator", Initiator,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    account_name = data_model.property(
        "accountName", str,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    drive_id = data_model.property(
        "driveID", int,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    initiator_ip = data_model.property(
        "initiatorIP", str,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    initiator_port_name = data_model.property(
        "initiatorPortName", str,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    target_port_name = data_model.property(
        "targetPortName", str,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    initiator_name = data_model.property(
        "initiatorName", str,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    node_id = data_model.property(
        "nodeID", int,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    service_id = data_model.property(
        "serviceID", int,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    session_id = data_model.property(
        "sessionID", int,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    target_name = data_model.property(
        "targetName", str,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    target_ip = data_model.property(
        "targetIP", str,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    virtual_network_id = data_model.property(
        "virtualNetworkID", int,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    volume_id = data_model.property(
        "volumeID", int,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    create_time = data_model.property(
        "createTime", str,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    volume_instance = data_model.property(
        "volumeInstance", int,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    initiator_session_id = data_model.property(
        "initiatorSessionID", int,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ListISCSISessionsResult(data_model.DataObject):
    """ListISCSISessionsResult  

    :param sessions: [required] 
    :type sessions: ISCSISession

    """
    sessions = data_model.property(
        "sessions", ISCSISession,
        array=True, optional=False,
        documentation="",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class GetBackupTargetRequest(data_model.DataObject):
    """GetBackupTargetRequest  

    :param backup_target_id: [required] Unique identifier assigned to the backup target. 
    :type backup_target_id: int

    """
    backup_target_id = data_model.property(
        "backupTargetID", int,
        array=False, optional=False,
        documentation="[&#x27;Unique identifier assigned to the backup target.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class GetIpmiConfigNodesResult(data_model.DataObject):
    """GetIpmiConfigNodesResult  

    :param node_id: [required] 
    :type node_id: int

    :param result: [required] 
    :type result: dict

    """
    node_id = data_model.property(
        "nodeID", int,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    result = data_model.property(
        "result", dict,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class GetIpmiConfigResult(data_model.DataObject):
    """GetIpmiConfigResult  

    :param nodes: [required] 
    :type nodes: GetIpmiConfigNodesResult

    """
    nodes = data_model.property(
        "nodes", GetIpmiConfigNodesResult,
        array=True, optional=False,
        documentation="",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class DeleteGroupSnapshotResult(data_model.DataObject):
    """DeleteGroupSnapshotResult  

    """

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ListVirtualVolumeBindingsRequest(data_model.DataObject):
    """ListVirtualVolumeBindingsRequest  

    :param virtual_volume_binding_ids:  
    :type virtual_volume_binding_ids: int

    """
    virtual_volume_binding_ids = data_model.property(
        "virtualVolumeBindingIDs", int,
        array=True, optional=True,
        documentation="",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class RemoveInitiatorsFromVolumeAccessGroupRequest(data_model.DataObject):
    """RemoveInitiatorsFromVolumeAccessGroupRequest  

    :param volume_access_group_id: [required] The ID of the volume access group to modify. 
    :type volume_access_group_id: int

    :param initiators: [required] List of initiators to remove from the volume access group. 
    :type initiators: str

    """
    volume_access_group_id = data_model.property(
        "volumeAccessGroupID", int,
        array=False, optional=False,
        documentation="The ID of the volume access group to modify.",
        dictionaryType=None
    )
    initiators = data_model.property(
        "initiators", str,
        array=True, optional=False,
        documentation="[&#x27;List of initiators to remove from the volume access group.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class Signature(data_model.DataObject):
    """Signature  

    :param data: [required] 
    :type data: str

    :param pubkey: [required] 
    :type pubkey: str

    :param version: [required] 
    :type version: int

    """
    data = data_model.property(
        "data", str,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    pubkey = data_model.property(
        "pubkey", str,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    version = data_model.property(
        "version", int,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class Origin(data_model.DataObject):
    """Origin  

    :param signature: [required] 
    :type signature: Signature

    :param contract_date: [required] 
    :type contract_date: str

    :param contract_name: [required] 
    :type contract_name: str

    :param contract_quantity: [required] 
    :type contract_quantity: int

    :param contract_type: [required] 
    :type contract_type: str

    :param integrator: [required] 
    :type integrator: str

    :param location: [required] 
    :type location: str

    :param organization: [required] 
    :type organization: str

    :param type: [required] 
    :type type: str

    """
    signature = data_model.property(
        "<signature>", Signature,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    contract_date = data_model.property(
        "contract-date", str,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    contract_name = data_model.property(
        "contract-name", str,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    contract_quantity = data_model.property(
        "contract-quantity", int,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    contract_type = data_model.property(
        "contract-type", str,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    integrator = data_model.property(
        "integrator", str,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    location = data_model.property(
        "location", str,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    organization = data_model.property(
        "organization", str,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    type = data_model.property(
        "type", str,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class GetOriginNodeResult(data_model.DataObject):
    """GetOriginNodeResult  

    :param origin: [required] 
    :type origin: Origin

    """
    origin = data_model.property(
        "origin", Origin,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class GetOriginNode(data_model.DataObject):
    """GetOriginNode  

    :param node_id: [required] 
    :type node_id: int

    :param result: [required] 
    :type result: GetOriginNodeResult

    """
    node_id = data_model.property(
        "nodeID", int,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    result = data_model.property(
        "result", GetOriginNodeResult,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class GetOriginResult(data_model.DataObject):
    """GetOriginResult  

    :param nodes: [required] 
    :type nodes: GetOriginNode

    """
    nodes = data_model.property(
        "nodes", GetOriginNode,
        array=True, optional=False,
        documentation="",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ModifyGroupSnapshotRequest(data_model.DataObject):
    """ModifyGroupSnapshotRequest  

    :param group_snapshot_id: [required] ID of the snapshot. 
    :type group_snapshot_id: int

    :param expiration_time:  Use to set the time when the snapshot should be removed. 
    :type expiration_time: str

    :param enable_remote_replication:  Use to enable the snapshot created to be replicated to a remote SolidFire cluster. Possible values: true: the snapshot will be replicated to remote storage. false: Default. No replication. 
    :type enable_remote_replication: bool

    """
    group_snapshot_id = data_model.property(
        "groupSnapshotID", int,
        array=False, optional=False,
        documentation="ID of the snapshot.",
        dictionaryType=None
    )
    expiration_time = data_model.property(
        "expirationTime", str,
        array=False, optional=True,
        documentation="Use to set the time when the snapshot should be removed.",
        dictionaryType=None
    )
    enable_remote_replication = data_model.property(
        "enableRemoteReplication", bool,
        array=False, optional=True,
        documentation="[&#x27;Use to enable the snapshot created to be replicated to a remote SolidFire cluster.&#x27;, &#x27;Possible values:&#x27;, &#x27;true: the snapshot will be replicated to remote storage.&#x27;, &#x27;false: Default. No replication.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class DeleteSnapshotRequest(data_model.DataObject):
    """DeleteSnapshotRequest  

    :param snapshot_id: [required] The ID of the snapshot to delete. 
    :type snapshot_id: int

    """
    snapshot_id = data_model.property(
        "snapshotID", int,
        array=False, optional=False,
        documentation="The ID of the snapshot to delete.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class SnmpV3UsmUser(data_model.DataObject):
    """SnmpV3UsmUser  
    The SNMP v3 usmUser object is used with the API method SetSnmpInfo to configure SNMP on the cluster.

    :param access: [required] rouser: read-only access.* rwuser: for read-write access. rosys: for read-only access to a restricted set of system information *SolidFire recommends that all USM users be set to "rouser" access, because all SolidFire MIB objects are read-only. 
    :type access: str

    :param name: [required] The name of the user. Must contain at least one character, but no more than 32 characters. Blank spaces are not allowed. 
    :type name: str

    :param password: [required] The password of the user. Must be between 8 and 255 characters long (inclusive). Blank spaces are not allowed. Required if "secLevel" is "auth" or "priv." 
    :type password: str

    :param passphrase: [required] The passphrase of the user. Must be between 8 and 255 characters long (inclusive). Blank spaces are not allowed. Required if "secLevel" is "priv." 
    :type passphrase: str

    :param sec_level: [required] noauth: No password or passphrase is required. auth: A password is required for user access. priv: A password and passphrase is required for user access. 
    :type sec_level: str

    """
    access = data_model.property(
        "access", str,
        array=False, optional=False,
        documentation="[&#x27;rouser: read-only access.*&#x27;, &#x27;rwuser: for read-write access.&#x27;, &#x27;rosys: for read-only access to a restricted set of system information&#x27;, &#x27;*SolidFire recommends that all USM users be set to &quot;rouser&quot; access, because all SolidFire MIB objects are read-only.&#x27;]",
        dictionaryType=None
    )
    name = data_model.property(
        "name", str,
        array=False, optional=False,
        documentation="[&#x27;The name of the user. Must contain at least one character, but no more than 32 characters. Blank spaces are not allowed.&#x27;]",
        dictionaryType=None
    )
    password = data_model.property(
        "password", str,
        array=False, optional=False,
        documentation="[&#x27;The password of the user. Must be between 8 and 255 characters long (inclusive). Blank spaces are not allowed. Required if &quot;secLevel&quot; is &quot;auth&quot; or &quot;priv.&quot;&#x27;]",
        dictionaryType=None
    )
    passphrase = data_model.property(
        "passphrase", str,
        array=False, optional=False,
        documentation="[&#x27;The passphrase of the user. Must be between 8 and 255 characters long (inclusive). Blank spaces are not allowed. Required if &quot;secLevel&quot; is &quot;priv.&quot;&#x27;]",
        dictionaryType=None
    )
    sec_level = data_model.property(
        "secLevel", str,
        array=False, optional=False,
        documentation="[&#x27;noauth: No password or passphrase is required.&#x27;, &#x27;auth: A password is required for user access.&#x27;, &#x27;priv: A password and passphrase is required for user access.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class AsyncResult(data_model.DataObject):
    """AsyncResult  
    The wrapped object returned by the "GetAsyncResult" API Service call.
    
    Note: The return value of GetAsyncResult is essentially a nested version of the standard JSON response with an additional status field.

    :param message: [required] The return value for the original method call if the call was completed successfully. 
    :type message: str

    """
    message = data_model.property(
        "message", str,
        array=False, optional=False,
        documentation="[&#x27;The return value for the original method call if the call was completed successfully.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class GetAsyncResultResult(data_model.DataObject):
    """GetAsyncResultResult  
    The object returned by the "GetAsyncResult" API Service call.
    
    Note: The return value of GetAsyncResult is essentially a nested version of the standard JSON response with an additional status field.

    :param result: [required] The resulting message for the original method call if the call was completed successfully. 
    :type result: AsyncResult

    :param status: [required] Status of the asynchronous method call running: The method is still running. complete: The method is complete and the result or error is available. 
    :type status: str

    """
    result = data_model.property(
        "result", AsyncResult,
        array=False, optional=False,
        documentation="[&#x27;The resulting message for the original method call if the call was completed successfully.&#x27;]",
        dictionaryType=None
    )
    status = data_model.property(
        "status", str,
        array=False, optional=False,
        documentation="[&#x27;Status of the asynchronous method call&#x27;, &#x27;running: The method is still running.&#x27;, &#x27;complete: The method is complete and the result or error is available.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class GetIpmiConfigRequest(data_model.DataObject):
    """GetIpmiConfigRequest  

    :param chassis_type:  Used to display information for each node chassis type. Valid values:all - returns sensor information for each chassis type. {chassis type} - returns sensor information for a specified chassis type. 
    :type chassis_type: str

    :param force: [required] 
    :type force: bool

    """
    chassis_type = data_model.property(
        "chassisType", str,
        array=False, optional=True,
        documentation="Used to display information for each node chassis type. Valid values:all - returns sensor information for each chassis type. {chassis type} - returns sensor information for a specified chassis type.",
        dictionaryType=None
    )
    force = data_model.property(
        "force", bool,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class GetScheduleResult(data_model.DataObject):
    """GetScheduleResult  

    :param schedule: [required] The schedule attributes. 
    :type schedule: Schedule

    """
    schedule = data_model.property(
        "schedule", Schedule,
        array=False, optional=False,
        documentation="The schedule attributes.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class DeleteSnapshotResult(data_model.DataObject):
    """DeleteSnapshotResult  

    """

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class IpmiInfo(data_model.DataObject):
    """IpmiInfo  

    :param sensors: [required] 
    :type sensors: dict

    """
    sensors = data_model.property(
        "sensors", dict,
        array=True, optional=False,
        documentation="",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class GetIpmiInfoNodesResultObject(data_model.DataObject):
    """GetIpmiInfoNodesResultObject  

    :param ipmi_info: [required] 
    :type ipmi_info: IpmiInfo

    """
    ipmi_info = data_model.property(
        "ipmiInfo", IpmiInfo,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class GetIpmiInfoNodesResult(data_model.DataObject):
    """GetIpmiInfoNodesResult  

    :param node_id: [required] 
    :type node_id: int

    :param result: [required] 
    :type result: GetIpmiInfoNodesResultObject

    """
    node_id = data_model.property(
        "nodeID", int,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    result = data_model.property(
        "result", GetIpmiInfoNodesResultObject,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class GetIpmiInfoResult(data_model.DataObject):
    """GetIpmiInfoResult  

    :param nodes: [required] Detailed information from each sensor within a node.  
    :type nodes: GetIpmiInfoNodesResult

    """
    nodes = data_model.property(
        "nodes", GetIpmiInfoNodesResult,
        array=True, optional=False,
        documentation="Detailed information from each sensor within a node. ",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class NewDrive(data_model.DataObject):
    """NewDrive  

    :param drive_id: [required] A unique identifier for this drive. 
    :type drive_id: int

    """
    drive_id = data_model.property(
        "driveID", int,
        array=False, optional=False,
        documentation="[&#x27;A unique identifier for this drive.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class DeleteVolumeAccessGroupResult(data_model.DataObject):
    """DeleteVolumeAccessGroupResult  

    """

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class DeleteStorageContainerResult(data_model.DataObject):
    """DeleteStorageContainerResult  

    """

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class UpdateBulkVolumeStatusResult(data_model.DataObject):
    """UpdateBulkVolumeStatusResult  

    :param status: [required] Status of the session requested. Returned status: preparing active done failed 
    :type status: str

    :param url: [required] The URL to access the node's web server provided only if the session is still active. 
    :type url: str

    :param attributes: [required] Returns attributes that were specified in the BulkVolumeStatusUpdate method. Values are returned if they have changed or not. 
    :type attributes: dict

    """
    status = data_model.property(
        "status", str,
        array=False, optional=False,
        documentation="[&#x27;Status of the session requested. Returned status:&#x27;, &#x27;preparing&#x27;, &#x27;active&#x27;, &#x27;done&#x27;, &#x27;failed&#x27;]",
        dictionaryType=None
    )
    url = data_model.property(
        "url", str,
        array=False, optional=False,
        documentation="The URL to access the node&#x27;s web server provided only if the session is still active.",
        dictionaryType=None
    )
    attributes = data_model.property(
        "attributes", dict,
        array=False, optional=False,
        documentation="Returns attributes that were specified in the BulkVolumeStatusUpdate method. Values are returned if they have changed or not.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ModifyScheduleResult(data_model.DataObject):
    """ModifyScheduleResult  

    """

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class GroupSnapshotMembers(data_model.DataObject):
    """GroupSnapshotMembers  
    List of checksum, volumeIDs and snapshotIDs for each member of the group.

    :param volume_id: [required] The source volume ID for the snapshot. 
    :type volume_id: int

    :param snapshot_id: [required] Unique ID of a snapshot from which the new snapshot is made. The snapshotID passed must be a snapshot on the given volume. 
    :type snapshot_id: int

    :param snapshot_uuid: [required] Universal Unique ID of an existing snapshot. 
    :type snapshot_uuid: str

    :param checksum: [required] A string that represents the correct digits in the stored snapshot. This checksum can be used later to compare other snapshots to detect errors in the data. 
    :type checksum: str

    """
    volume_id = data_model.property(
        "volumeID", int,
        array=False, optional=False,
        documentation="The source volume ID for the snapshot.",
        dictionaryType=None
    )
    snapshot_id = data_model.property(
        "snapshotID", int,
        array=False, optional=False,
        documentation="[&#x27;Unique ID of a snapshot from which the new snapshot is made.&#x27;, &#x27;The snapshotID passed must be a snapshot on the given volume.&#x27;]",
        dictionaryType=None
    )
    snapshot_uuid = data_model.property(
        "snapshotUUID", str,
        array=False, optional=False,
        documentation="Universal Unique ID of an existing snapshot.",
        dictionaryType=None
    )
    checksum = data_model.property(
        "checksum", str,
        array=False, optional=False,
        documentation="[&#x27;A string that represents the correct digits in the stored snapshot.&#x27;, &#x27;This checksum can be used later to compare other snapshots to detect errors in the data.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class GroupSnapshot(data_model.DataObject):
    """GroupSnapshot  
    Group Snapshot object represents a point-in-time copy of a group of volumes.

    :param group_snapshot_id: [required] Unique ID of the new group snapshot. 
    :type group_snapshot_id: int

    :param group_snapshot_uuid: [required] UUID of the group snapshot. 
    :type group_snapshot_uuid: UUID

    :param members: [required] List of volumeIDs and snapshotIDs for each member of the group. 
    :type members: GroupSnapshotMembers

    :param name: [required] Name of the group snapshot, or, if none was given, the UTC formatted day and time on which the snapshot was created. 
    :type name: str

    :param create_time: [required] The UTC formatted day and time on which the snapshot was created. 
    :type create_time: str

    :param status: [required] Status of the snapshot. Possible values: Preparing: A snapshot that is being prepared for use and is not yet writable. Done: A snapshot that has finished being prepared and is now usable 
    :type status: str

    :param attributes: [required] List of Name/Value pairs in JSON object format. 
    :type attributes: dict

    """
    group_snapshot_id = data_model.property(
        "groupSnapshotID", int,
        array=False, optional=False,
        documentation="Unique ID of the new group snapshot.",
        dictionaryType=None
    )
    group_snapshot_uuid = data_model.property(
        "groupSnapshotUUID", UUID,
        array=False, optional=False,
        documentation="UUID of the group snapshot.",
        dictionaryType=None
    )
    members = data_model.property(
        "members", GroupSnapshotMembers,
        array=True, optional=False,
        documentation="List of volumeIDs and snapshotIDs for each member of the group.",
        dictionaryType=None
    )
    name = data_model.property(
        "name", str,
        array=False, optional=False,
        documentation="Name of the group snapshot, or, if none was given, the UTC formatted day and time on which the snapshot was created.",
        dictionaryType=None
    )
    create_time = data_model.property(
        "createTime", str,
        array=False, optional=False,
        documentation="The UTC formatted day and time on which the snapshot was created.",
        dictionaryType=None
    )
    status = data_model.property(
        "status", str,
        array=False, optional=False,
        documentation="[&#x27;Status of the snapshot.&#x27;, &#x27;Possible values:&#x27;, &#x27;Preparing: A snapshot that is being prepared for use and is not yet writable.&#x27;, &#x27;Done: A snapshot that has finished being prepared and is now usable&#x27;]",
        dictionaryType=None
    )
    attributes = data_model.property(
        "attributes", dict,
        array=False, optional=False,
        documentation="List of Name/Value pairs in JSON object format.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ListGroupSnapshotsResult(data_model.DataObject):
    """ListGroupSnapshotsResult  

    :param group_snapshots: [required] List of Group Snapshots. 
    :type group_snapshots: GroupSnapshot

    """
    group_snapshots = data_model.property(
        "groupSnapshots", GroupSnapshot,
        array=True, optional=False,
        documentation="List of Group Snapshots.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ClearClusterFaultsRequest(data_model.DataObject):
    """ClearClusterFaultsRequest  

    :param fault_types:  Determines the types of faults cleared: current: Faults that are currently detected and have not been resolved. resolved: Faults that were previously detected and resolved. all: Both current and resolved faults are cleared. The fault status can be determined by the "resolved" field of the fault object. 
    :type fault_types: str

    """
    fault_types = data_model.property(
        "faultTypes", str,
        array=False, optional=True,
        documentation="[&#x27;Determines the types of faults cleared:&#x27;, &#x27;current: Faults that are currently detected and have not been resolved.&#x27;, &#x27;resolved: Faults that were previously detected and resolved.&#x27;, &#x27;all: Both current and resolved faults are cleared. The fault status can be determined by the &quot;resolved&quot; field of the fault object.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class GetVolumeAccessGroupEfficiencyRequest(data_model.DataObject):
    """GetVolumeAccessGroupEfficiencyRequest  

    :param volume_access_group_id: [required] Specifies the volume access group for which capacity is computed. 
    :type volume_access_group_id: int

    """
    volume_access_group_id = data_model.property(
        "volumeAccessGroupID", int,
        array=False, optional=False,
        documentation="Specifies the volume access group for which capacity is computed.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class GetVirtualVolumeCountResult(data_model.DataObject):
    """GetVirtualVolumeCountResult  

    :param count: [required] The number of virtual volumes currently in the system. 
    :type count: int

    """
    count = data_model.property(
        "count", int,
        array=False, optional=False,
        documentation="The number of virtual volumes currently in the system.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ListVirtualVolumeTasksRequest(data_model.DataObject):
    """ListVirtualVolumeTasksRequest  

    :param virtual_volume_task_ids:  
    :type virtual_volume_task_ids: UUID

    """
    virtual_volume_task_ids = data_model.property(
        "virtualVolumeTaskIDs", UUID,
        array=True, optional=True,
        documentation="",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class RemoveVirtualNetworkRequest(data_model.DataObject):
    """RemoveVirtualNetworkRequest  

    :param virtual_network_id:  Network ID that identifies the virtual network to remove. 
    :type virtual_network_id: int

    :param virtual_network_tag:  Network Tag that identifies the virtual network to remove. 
    :type virtual_network_tag: int

    """
    virtual_network_id = data_model.property(
        "virtualNetworkID", int,
        array=False, optional=True,
        documentation="Network ID that identifies the virtual network to remove.",
        dictionaryType=None
    )
    virtual_network_tag = data_model.property(
        "virtualNetworkTag", int,
        array=False, optional=True,
        documentation="Network Tag that identifies the virtual network to remove.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ListVolumeStatsByVolumeAccessGroupRequest(data_model.DataObject):
    """ListVolumeStatsByVolumeAccessGroupRequest  

    :param volume_access_groups:  An array of VolumeAccessGroupIDs for which volume activity is returned. If no VolumeAccessGroupID is specified, stats for all volume access groups is returned. 
    :type volume_access_groups: int

    """
    volume_access_groups = data_model.property(
        "volumeAccessGroups", int,
        array=True, optional=True,
        documentation="[&#x27;An array of VolumeAccessGroupIDs for which volume activity is returned.&#x27;, &#x27;If no VolumeAccessGroupID is specified, stats for all volume access groups is returned.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class TestDrivesRequest(data_model.DataObject):
    """TestDrivesRequest  

    :param minutes:  The number of minutes to run the test can be specified. 
    :type minutes: int

    """
    minutes = data_model.property(
        "minutes", int,
        array=False, optional=True,
        documentation="The number of minutes to run the test can be specified.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class RemoveClusterAdminResult(data_model.DataObject):
    """RemoveClusterAdminResult  

    """

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class GetLdapConfigurationResult(data_model.DataObject):
    """GetLdapConfigurationResult  

    :param ldap_configuration: [required] List of the current LDAP configuration settings. This API call will not return the plain text of the search account password.  Note: If LDAP authentication is currently disabled, all the returned settings will be empty with the exception of "authType", and "groupSearchType" which are set to "SearchAndBind" and "ActiveDirectory" respectively. 
    :type ldap_configuration: LdapConfiguration

    """
    ldap_configuration = data_model.property(
        "ldapConfiguration", LdapConfiguration,
        array=False, optional=False,
        documentation="[&#x27;List of the current LDAP configuration settings. This API call will not return the plain text of the search account password.&#x27;, u&#x27;&#x27;, &#x27;Note: If LDAP authentication is currently disabled, all the returned settings will be empty with the exception of &quot;authType&quot;, and &quot;groupSearchType&quot; which are set to &quot;SearchAndBind&quot; and &quot;ActiveDirectory&quot; respectively.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class VolumeAccessGroup(data_model.DataObject):
    """VolumeAccessGroup  
    A volume access group is a useful way of grouping volumes and initiators together for ease of management.
    
    Volume Access Group Limits:
    
    - A volume access group can contain up to sixty-four initiator IQNs.
    - An initiator can only belong to only one volume access group.
    - A volume access group can contain up to two thousand volumes.
    - Each volume access group can belong to a maximum of four other volume access groups.

    :param deleted_volumes: [required] A list of deleted volumes that have yet to be purged from the VAG. 
    :type deleted_volumes: int

    :param volume_access_group_id: [required] Unique ID for this volume access group. 
    :type volume_access_group_id: int

    :param name: [required] Name of the volume access group. 
    :type name: str

    :param initiator_ids: [required] A list of IDs of initiators that are mapped to the VAG. 
    :type initiator_ids: int

    :param initiators: [required] List of unique initiator names belonging to the volume access group. 
    :type initiators: str

    :param volumes: [required] List of volumes belonging to the volume access group. 
    :type volumes: int

    :param attributes: [required] List of name/value pairs 
    :type attributes: dict

    """
    deleted_volumes = data_model.property(
        "deletedVolumes", int,
        array=True, optional=False,
        documentation="A list of deleted volumes that have yet to be purged from the VAG.",
        dictionaryType=None
    )
    volume_access_group_id = data_model.property(
        "volumeAccessGroupID", int,
        array=False, optional=False,
        documentation="Unique ID for this volume access group.",
        dictionaryType=None
    )
    name = data_model.property(
        "name", str,
        array=False, optional=False,
        documentation="Name of the volume access group.",
        dictionaryType=None
    )
    initiator_ids = data_model.property(
        "initiatorIDs", int,
        array=True, optional=False,
        documentation="A list of IDs of initiators that are mapped to the VAG.",
        dictionaryType=None
    )
    initiators = data_model.property(
        "initiators", str,
        array=True, optional=False,
        documentation="List of unique initiator names belonging to the volume access group.",
        dictionaryType=None
    )
    volumes = data_model.property(
        "volumes", int,
        array=True, optional=False,
        documentation="List of volumes belonging to the volume access group.",
        dictionaryType=None
    )
    attributes = data_model.property(
        "attributes", dict,
        array=False, optional=False,
        documentation="List of name/value pairs",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class CreateVolumeAccessGroupResult(data_model.DataObject):
    """CreateVolumeAccessGroupResult  

    :param volume_access_group_id: [required] The ID for the newly-created volume access group. 
    :type volume_access_group_id: int

    :param volume_access_group: [required] 
    :type volume_access_group: VolumeAccessGroup

    """
    volume_access_group_id = data_model.property(
        "volumeAccessGroupID", int,
        array=False, optional=False,
        documentation="The ID for the newly-created volume access group.",
        dictionaryType=None
    )
    volume_access_group = data_model.property(
        "volumeAccessGroup", VolumeAccessGroup,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class DeleteVolumesResult(data_model.DataObject):
    """DeleteVolumesResult  

    :param volumes: [required] Information about the newly deleted volume. 
    :type volumes: Volume

    :param curve: [required] 
    :type curve: VolumeQOS

    """
    volumes = data_model.property(
        "volumes", Volume,
        array=True, optional=False,
        documentation="Information about the newly deleted volume.",
        dictionaryType=None
    )
    curve = data_model.property(
        "curve", VolumeQOS,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class PendingOperation(data_model.DataObject):
    """PendingOperation  

    :param pending: [required] true: operation is still in progress. false: operation is no longer in progress. 
    :type pending: bool

    :param operation: [required] Name of operation that is in progress or has completed. 
    :type operation: str

    """
    pending = data_model.property(
        "pending", bool,
        array=False, optional=False,
        documentation="[&#x27;true: operation is still in progress.&#x27;, &#x27;false: operation is no longer in progress.&#x27;]",
        dictionaryType=None
    )
    operation = data_model.property(
        "operation", str,
        array=False, optional=False,
        documentation="Name of operation that is in progress or has completed.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class GetPendingOperationResult(data_model.DataObject):
    """GetPendingOperationResult  

    :param pending_operation: [required] 
    :type pending_operation: PendingOperation

    """
    pending_operation = data_model.property(
        "pendingOperation", PendingOperation,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ModifyInitiatorsResult(data_model.DataObject):
    """ModifyInitiatorsResult  

    :param initiators: [required] List of objects containing details about the modified initiators 
    :type initiators: Initiator

    """
    initiators = data_model.property(
        "initiators", Initiator,
        array=True, optional=False,
        documentation="List of objects containing details about the modified initiators",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ModifyGroupSnapshotResult(data_model.DataObject):
    """ModifyGroupSnapshotResult  

    """

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class CloneMultipleVolumeParams(data_model.DataObject):
    """CloneMultipleVolumeParams  

    :param volume_id: [required] Required parameter for "volumes" array: volumeID. 
    :type volume_id: int

    :param access:  Access settings for the new volume. readOnly: Only read operations are allowed. readWrite: Reads and writes are allowed. locked: No reads or writes are allowed. replicationTarget: Identify a volume as the target volume for a paired set of volumes. If the volume is not paired, the access status is locked.  If unspecified, the access settings of the clone will be the same as the source. 
    :type access: str

    :param name:  New name for the clone. 
    :type name: str

    :param new_account_id:  Account ID for the new volume. 
    :type new_account_id: int

    :param new_size:  New size Total size of the volume, in bytes. Size is rounded up to the nearest 1MB size. 
    :type new_size: int

    :param attributes:  List of Name/Value pairs in JSON object format. 
    :type attributes: dict

    """
    volume_id = data_model.property(
        "volumeID", int,
        array=False, optional=False,
        documentation="Required parameter for &quot;volumes&quot; array: volumeID.",
        dictionaryType=None
    )
    access = data_model.property(
        "access", str,
        array=False, optional=True,
        documentation="[&#x27;Access settings for the new volume.&#x27;, &#x27;readOnly: Only read operations are allowed.&#x27;, &#x27;readWrite: Reads and writes are allowed.&#x27;, &#x27;locked: No reads or writes are allowed.&#x27;, &#x27;replicationTarget: Identify a volume as the target volume for a paired set of volumes. If the volume is not paired, the access status is locked.&#x27;, u&#x27;&#x27;, &#x27;If unspecified, the access settings of the clone will be the same as the source.&#x27;]",
        dictionaryType=None
    )
    name = data_model.property(
        "name", str,
        array=False, optional=True,
        documentation="New name for the clone.",
        dictionaryType=None
    )
    new_account_id = data_model.property(
        "newAccountID", int,
        array=False, optional=True,
        documentation="Account ID for the new volume.",
        dictionaryType=None
    )
    new_size = data_model.property(
        "newSize", int,
        array=False, optional=True,
        documentation="New size Total size of the volume, in bytes. Size is rounded up to the nearest 1MB size.",
        dictionaryType=None
    )
    attributes = data_model.property(
        "attributes", dict,
        array=False, optional=True,
        documentation="List of Name/Value pairs in JSON object format.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class UpdateBulkVolumeStatusRequest(data_model.DataObject):
    """UpdateBulkVolumeStatusRequest  

    :param key: [required] The key assigned during initialization of a "StartBulkVolumeRead" or "StartBulkVolumeWrite" session. 
    :type key: str

    :param status: [required] The SolidFire system sets the status of the given bulk volume job. Possible values: running: jobs that are still active. complete: jobs that are done. failed - jobs that have failed. failed: jobs that have failed. 
    :type status: str

    :param percent_complete:  The completed progress of the bulk volume job as a percentage. 
    :type percent_complete: str

    :param message:  Returns the status of the bulk volume job when the job has completed. 
    :type message: str

    :param attributes:  JSON attributes  updates what is on the bulk volume job. 
    :type attributes: dict

    """
    key = data_model.property(
        "key", str,
        array=False, optional=False,
        documentation="The key assigned during initialization of a &quot;StartBulkVolumeRead&quot; or &quot;StartBulkVolumeWrite&quot; session.",
        dictionaryType=None
    )
    status = data_model.property(
        "status", str,
        array=False, optional=False,
        documentation="[&#x27;The SolidFire system sets the status of the given bulk volume job.&#x27;, &#x27;Possible values:&#x27;, &#x27;running: jobs that are still active.&#x27;, &#x27;complete: jobs that are done. failed - jobs that have failed.&#x27;, &#x27;failed: jobs that have failed.&#x27;]",
        dictionaryType=None
    )
    percent_complete = data_model.property(
        "percentComplete", str,
        array=False, optional=True,
        documentation="[&#x27;The completed progress of the bulk volume job as a percentage.&#x27;]",
        dictionaryType=None
    )
    message = data_model.property(
        "message", str,
        array=False, optional=True,
        documentation="[&#x27;Returns the status of the bulk volume job when the job has completed.&#x27;]",
        dictionaryType=None
    )
    attributes = data_model.property(
        "attributes", dict,
        array=False, optional=True,
        documentation="[&#x27;JSON attributes  updates what is on the bulk volume job.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class SetNtpInfoResult(data_model.DataObject):
    """SetNtpInfoResult  

    """

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class AddressBlock(data_model.DataObject):
    """AddressBlock  
    Unique Range of IP addresses to include in the virtual network.

    :param start: [required] Start of the IP address range. 
    :type start: str

    :param size: [required] Number of IP addresses to include in the block. 
    :type size: int

    """
    start = data_model.property(
        "start", str,
        array=False, optional=False,
        documentation="Start of the IP address range.",
        dictionaryType=None
    )
    size = data_model.property(
        "size", int,
        array=False, optional=False,
        documentation="Number of IP addresses to include in the block.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ModifyVirtualNetworkRequest(data_model.DataObject):
    """ModifyVirtualNetworkRequest  

    :param virtual_network_id:  Unique identifier of the virtual network to modify. This is the virtual network ID assigned by the SolidFire cluster. 
    :type virtual_network_id: int

    :param virtual_network_tag:  Network Tag that identifies the virtual network to modify. 
    :type virtual_network_tag: int

    :param name:  New name for the virtual network. 
    :type name: str

    :param address_blocks:  New addressBlock to set for this Virtual Network object. This may contain new address blocks to add to the existing object or it may omit unused address blocks that need to be removed. Alternatively, existing address blocks may be extended or reduced in size. The size of the starting addressBlocks for a Virtual Network object can only be increased, and can never be decreased. Attributes for this parameter are: start: start of the IP address range. (String) size: numbre of IP addresses to include in the block. (Integer) 
    :type address_blocks: AddressBlock

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
    virtual_network_id = data_model.property(
        "virtualNetworkID", int,
        array=False, optional=True,
        documentation="Unique identifier of the virtual network to modify. This is the virtual network ID assigned by the SolidFire cluster.",
        dictionaryType=None
    )
    virtual_network_tag = data_model.property(
        "virtualNetworkTag", int,
        array=False, optional=True,
        documentation="Network Tag that identifies the virtual network to modify.",
        dictionaryType=None
    )
    name = data_model.property(
        "name", str,
        array=False, optional=True,
        documentation="New name for the virtual network.",
        dictionaryType=None
    )
    address_blocks = data_model.property(
        "addressBlocks", AddressBlock,
        array=True, optional=True,
        documentation="[&#x27;New addressBlock to set for this Virtual Network object. This may contain new address blocks to add to the existing object or it may omit unused address blocks that need to be removed. Alternatively, existing address blocks may be extended or reduced in size. The size of the starting addressBlocks for a Virtual Network object can only be increased, and can never be decreased.&#x27;, &#x27;Attributes for this parameter are:&#x27;, &#x27;start: start of the IP address range. (String)&#x27;, &#x27;size: numbre of IP addresses to include in the block. (Integer)&#x27;]",
        dictionaryType=None
    )
    netmask = data_model.property(
        "netmask", str,
        array=False, optional=True,
        documentation="[&#x27;New netmask for this virtual network.&#x27;]",
        dictionaryType=None
    )
    svip = data_model.property(
        "svip", str,
        array=False, optional=True,
        documentation="[&#x27;The storage virtual IP address for this virtual network. The svip for Virtual Network cannot be changed. A new Virtual Network must be created in order to use a different svip address.&#x27;]",
        dictionaryType=None
    )
    gateway = data_model.property(
        "gateway", str,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    namespace = data_model.property(
        "namespace", bool,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    attributes = data_model.property(
        "attributes", dict,
        array=False, optional=True,
        documentation="[&#x27;A new list of Name/Value pairs in JSON object format.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ListDriveStatsRequest(data_model.DataObject):
    """ListDriveStatsRequest  

    :param drives:  Optional list of DriveIDs for which to return drive statistics. If you omit this parameter, measurements for all drives are returned. 
    :type drives: int

    """
    drives = data_model.property(
        "drives", int,
        array=True, optional=True,
        documentation="Optional list of DriveIDs for which to return drive statistics. If you omit this parameter, measurements for all drives are returned.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class RemoveVolumesFromVolumeAccessGroupRequest(data_model.DataObject):
    """RemoveVolumesFromVolumeAccessGroupRequest  

    :param volume_access_group_id: [required] The ID of the volume access group to modify. 
    :type volume_access_group_id: int

    :param volumes: [required] List of volumes to remove from this volume access group. 
    :type volumes: int

    """
    volume_access_group_id = data_model.property(
        "volumeAccessGroupID", int,
        array=False, optional=False,
        documentation="The ID of the volume access group to modify.",
        dictionaryType=None
    )
    volumes = data_model.property(
        "volumes", int,
        array=True, optional=False,
        documentation="[&#x27;List of volumes to remove from this volume access group.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class DeleteVolumeAccessGroupRequest(data_model.DataObject):
    """DeleteVolumeAccessGroupRequest  

    :param volume_access_group_id: [required] The ID of the volume access group to delete. 
    :type volume_access_group_id: int

    """
    volume_access_group_id = data_model.property(
        "volumeAccessGroupID", int,
        array=False, optional=False,
        documentation="[&#x27;The ID of the volume access group to delete.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ListInitiatorsRequest(data_model.DataObject):
    """ListInitiatorsRequest  

    :param start_initiator_id:  The initiator ID at which to begin the listing. You can supply this parameter or the "initiators" parameter, but not both. 
    :type start_initiator_id: int

    :param limit:  The maximum number of initiator objects to return. 
    :type limit: int

    :param initiators:  A list of initiator IDs to retrieve. You can supply this parameter or the "startInitiatorID" parameter, but not both. 
    :type initiators: int

    """
    start_initiator_id = data_model.property(
        "startInitiatorID", int,
        array=False, optional=True,
        documentation="The initiator ID at which to begin the listing. You can supply this parameter or the &quot;initiators&quot; parameter, but not both.",
        dictionaryType=None
    )
    limit = data_model.property(
        "limit", int,
        array=False, optional=True,
        documentation="The maximum number of initiator objects to return.",
        dictionaryType=None
    )
    initiators = data_model.property(
        "initiators", int,
        array=True, optional=True,
        documentation="A list of initiator IDs to retrieve. You can supply this parameter or the &quot;startInitiatorID&quot; parameter, but not both.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class AddAccountResult(data_model.DataObject):
    """AddAccountResult  

    :param account_id: [required] AccountID for the newly created Account. 
    :type account_id: int

    """
    account_id = data_model.property(
        "accountID", int,
        array=False, optional=False,
        documentation="AccountID for the newly created Account.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class GetFeatureStatusRequest(data_model.DataObject):
    """GetFeatureStatusRequest  

    :param feature:  Valid values: vvols: Find the status of the Virtual Volumes (VVOLs) cluster feature. 
    :type feature: str

    """
    feature = data_model.property(
        "feature", str,
        array=False, optional=True,
        documentation="[&#x27;Valid values: vvols: Find the status of the Virtual Volumes (VVOLs) cluster feature.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ListInitiatorsResult(data_model.DataObject):
    """ListInitiatorsResult  

    :param initiators: [required] List of the initiator information. 
    :type initiators: Initiator

    """
    initiators = data_model.property(
        "initiators", Initiator,
        array=True, optional=False,
        documentation="List of the initiator information.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class CreateInitiatorsRequest(data_model.DataObject):
    """CreateInitiatorsRequest  

    :param initiators: [required] A list of Initiator objects containing characteristics of each new initiator 
    :type initiators: CreateInitiator

    """
    initiators = data_model.property(
        "initiators", CreateInitiator,
        array=True, optional=False,
        documentation="[&#x27;A list of Initiator objects containing characteristics of each new initiator&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class GetClusterFullThresholdResult(data_model.DataObject):
    """GetClusterFullThresholdResult  

    :param block_fullness: [required] Current computed level of block fullness of the cluster. Possible values: stage1Happy: No alerts or error conditions. stage2Aware: 3 nodes of capacity available. stage3Low: 2 nodes of capacity available. stage4Critical: 1 node of capacity available. No new volumes or clones can be created. stage5CompletelyConsumed: Completely consumed. Cluster is read-only, iSCSI connection is maintained but all writes are suspended. 
    :type block_fullness: str

    :param fullness: [required] Reflects the highest level of fullness between "blockFullness" and "metadataFullness". 
    :type fullness: str

    :param max_metadata_over_provision_factor: [required] A value representative of the number of times metadata space can be over provisioned relative to the amount of space available. For example, if there was enough metadata space to store 100 TiB of volumes and this number was set to 5, then 500 TiB worth of volumes could be created. 
    :type max_metadata_over_provision_factor: int

    :param metadata_fullness: [required] Current computed level of metadata fullness of the cluster. 
    :type metadata_fullness: str

    :param slice_reserve_used_threshold_pct: [required] Error condition; message sent to "Alerts" if the reserved slice utilization is greater than the sliceReserveUsedThresholdPct value returned. 
    :type slice_reserve_used_threshold_pct: int

    :param stage2_aware_threshold: [required] Awareness condition: Value that is set for "Stage 2" cluster threshold level. 
    :type stage2_aware_threshold: int

    :param stage2_block_threshold_bytes: [required] Number of bytes being used by the cluster at which a stage2 condition will exist. 
    :type stage2_block_threshold_bytes: int

    :param stage3_block_threshold_bytes: [required] Number of bytes being used by the cluster at which a stage3 condition will exist. 
    :type stage3_block_threshold_bytes: int

    :param stage3_block_threshold_percent: [required] The percent value set for stage3. At this percent full, a warning will be posted in the Alerts log. 
    :type stage3_block_threshold_percent: int

    :param stage3_low_threshold: [required] Error condition; message sent to "Alerts" that capacity on a cluster is getting low. 
    :type stage3_low_threshold: int

    :param stage4_critical_threshold: [required] Error condition; message sent to "Alerts" that capacity on a cluster is critically low. 
    :type stage4_critical_threshold: int

    :param stage4_block_threshold_bytes: [required] Number of bytes being used by the cluster at which a stage4 condition will exist. 
    :type stage4_block_threshold_bytes: int

    :param stage5_block_threshold_bytes: [required] Number of bytes being used by the cluster at which a stage5 condition will exist. 
    :type stage5_block_threshold_bytes: int

    :param sum_total_cluster_bytes: [required] Physical capacity of the cluster measured in bytes. 
    :type sum_total_cluster_bytes: int

    :param sum_total_metadata_cluster_bytes: [required] Total amount of space that can be used to store metadata. 
    :type sum_total_metadata_cluster_bytes: int

    :param sum_used_cluster_bytes: [required] Number of bytes used on the cluster. 
    :type sum_used_cluster_bytes: int

    :param sum_used_metadata_cluster_bytes: [required] Amount of space used on volume drives to store metadata. 
    :type sum_used_metadata_cluster_bytes: int

    """
    block_fullness = data_model.property(
        "blockFullness", str,
        array=False, optional=False,
        documentation="[&#x27;Current computed level of block fullness of the cluster.&#x27;, &#x27;Possible values: stage1Happy: No alerts or error conditions. stage2Aware: 3 nodes of capacity available. stage3Low: 2 nodes of capacity available. stage4Critical: 1 node of capacity available. No new volumes or clones can be created. stage5CompletelyConsumed: Completely consumed. Cluster is read-only, iSCSI connection is maintained but all writes are suspended.&#x27;]",
        dictionaryType=None
    )
    fullness = data_model.property(
        "fullness", str,
        array=False, optional=False,
        documentation="Reflects the highest level of fullness between &quot;blockFullness&quot; and &quot;metadataFullness&quot;.",
        dictionaryType=None
    )
    max_metadata_over_provision_factor = data_model.property(
        "maxMetadataOverProvisionFactor", int,
        array=False, optional=False,
        documentation="A value representative of the number of times metadata space can be over provisioned relative to the amount of space available. For example, if there was enough metadata space to store 100 TiB of volumes and this number was set to 5, then 500 TiB worth of volumes could be created.",
        dictionaryType=None
    )
    metadata_fullness = data_model.property(
        "metadataFullness", str,
        array=False, optional=False,
        documentation="Current computed level of metadata fullness of the cluster.",
        dictionaryType=None
    )
    slice_reserve_used_threshold_pct = data_model.property(
        "sliceReserveUsedThresholdPct", int,
        array=False, optional=False,
        documentation="Error condition; message sent to &quot;Alerts&quot; if the reserved slice utilization is greater than the sliceReserveUsedThresholdPct value returned.",
        dictionaryType=None
    )
    stage2_aware_threshold = data_model.property(
        "stage2AwareThreshold", int,
        array=False, optional=False,
        documentation="Awareness condition: Value that is set for &quot;Stage 2&quot; cluster threshold level.",
        dictionaryType=None
    )
    stage2_block_threshold_bytes = data_model.property(
        "stage2BlockThresholdBytes", int,
        array=False, optional=False,
        documentation="Number of bytes being used by the cluster at which a stage2 condition will exist.",
        dictionaryType=None
    )
    stage3_block_threshold_bytes = data_model.property(
        "stage3BlockThresholdBytes", int,
        array=False, optional=False,
        documentation="Number of bytes being used by the cluster at which a stage3 condition will exist.",
        dictionaryType=None
    )
    stage3_block_threshold_percent = data_model.property(
        "stage3BlockThresholdPercent", int,
        array=False, optional=False,
        documentation="The percent value set for stage3. At this percent full, a warning will be posted in the Alerts log.",
        dictionaryType=None
    )
    stage3_low_threshold = data_model.property(
        "stage3LowThreshold", int,
        array=False, optional=False,
        documentation="Error condition; message sent to &quot;Alerts&quot; that capacity on a cluster is getting low.",
        dictionaryType=None
    )
    stage4_critical_threshold = data_model.property(
        "stage4CriticalThreshold", int,
        array=False, optional=False,
        documentation="Error condition; message sent to &quot;Alerts&quot; that capacity on a cluster is critically low.",
        dictionaryType=None
    )
    stage4_block_threshold_bytes = data_model.property(
        "stage4BlockThresholdBytes", int,
        array=False, optional=False,
        documentation="Number of bytes being used by the cluster at which a stage4 condition will exist.",
        dictionaryType=None
    )
    stage5_block_threshold_bytes = data_model.property(
        "stage5BlockThresholdBytes", int,
        array=False, optional=False,
        documentation="Number of bytes being used by the cluster at which a stage5 condition will exist.",
        dictionaryType=None
    )
    sum_total_cluster_bytes = data_model.property(
        "sumTotalClusterBytes", int,
        array=False, optional=False,
        documentation="Physical capacity of the cluster measured in bytes.",
        dictionaryType=None
    )
    sum_total_metadata_cluster_bytes = data_model.property(
        "sumTotalMetadataClusterBytes", int,
        array=False, optional=False,
        documentation="Total amount of space that can be used to store metadata.",
        dictionaryType=None
    )
    sum_used_cluster_bytes = data_model.property(
        "sumUsedClusterBytes", int,
        array=False, optional=False,
        documentation="Number of bytes used on the cluster.",
        dictionaryType=None
    )
    sum_used_metadata_cluster_bytes = data_model.property(
        "sumUsedMetadataClusterBytes", int,
        array=False, optional=False,
        documentation="Amount of space used on volume drives to store metadata.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ListVolumesForAccountRequest(data_model.DataObject):
    """ListVolumesForAccountRequest  

    :param account_id: [required] The ID of the account to list the volumes for. 
    :type account_id: int

    :param start_volume_id:  The ID of the first volume to list. This can be useful for paging results. By default, this starts at the lowest VolumeID. 
    :type start_volume_id: int

    :param limit:  The maximum number of volumes to return from the API. 
    :type limit: int

    """
    account_id = data_model.property(
        "accountID", int,
        array=False, optional=False,
        documentation="The ID of the account to list the volumes for.",
        dictionaryType=None
    )
    start_volume_id = data_model.property(
        "startVolumeID", int,
        array=False, optional=True,
        documentation="[&#x27;The ID of the first volume to list.&#x27;, &#x27;This can be useful for paging results.&#x27;, &#x27;By default, this starts at the lowest VolumeID.&#x27;]",
        dictionaryType=None
    )
    limit = data_model.property(
        "limit", int,
        array=False, optional=True,
        documentation="[&#x27;The maximum number of volumes to return from the API.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class DisableEncryptionAtRestResult(data_model.DataObject):
    """DisableEncryptionAtRestResult  

    """

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ClusterInfo(data_model.DataObject):
    """ClusterInfo  
    Cluster Info object returns information the node uses to communicate with the cluster.

    :param encryption_at_rest_state: [required] Encryption at rest state. 
    :type encryption_at_rest_state: str

    :param ensemble: [required] Array of Node IP addresses that are participating in the cluster. 
    :type ensemble: str

    :param mvip: [required] Management network interface. 
    :type mvip: str

    :param mvip_node_id: [required] Node holding the master MVIP address 
    :type mvip_node_id: int

    :param name: [required] Unique cluster name. 
    :type name: str

    :param rep_count: [required] Number of replicas of each piece of data to store in the cluster. Valid value is 2 
    :type rep_count: int

    :param state: [required] 
    :type state: str

    :param svip: [required] Storage virtual IP 
    :type svip: str

    :param svip_node_id: [required] Node holding the master SVIP address. 
    :type svip_node_id: int

    :param unique_id: [required] Unique ID for the cluster. 
    :type unique_id: str

    :param uuid: [required] 
    :type uuid: UUID

    :param attributes: [required] List of Name/Value pairs in JSON object format. 
    :type attributes: dict

    """
    encryption_at_rest_state = data_model.property(
        "encryptionAtRestState", str,
        array=False, optional=False,
        documentation="Encryption at rest state.",
        dictionaryType=None
    )
    ensemble = data_model.property(
        "ensemble", str,
        array=True, optional=False,
        documentation="Array of Node IP addresses that are participating in the cluster.",
        dictionaryType=None
    )
    mvip = data_model.property(
        "mvip", str,
        array=False, optional=False,
        documentation="Management network interface.",
        dictionaryType=None
    )
    mvip_node_id = data_model.property(
        "mvipNodeID", int,
        array=False, optional=False,
        documentation="Node holding the master MVIP address",
        dictionaryType=None
    )
    name = data_model.property(
        "name", str,
        array=False, optional=False,
        documentation="Unique cluster name.",
        dictionaryType=None
    )
    rep_count = data_model.property(
        "repCount", int,
        array=False, optional=False,
        documentation="[&#x27;Number of replicas of each piece of data to store in the cluster.&#x27;, &#x27;Valid value is 2&#x27;]",
        dictionaryType=None
    )
    state = data_model.property(
        "state", str,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    svip = data_model.property(
        "svip", str,
        array=False, optional=False,
        documentation="Storage virtual IP",
        dictionaryType=None
    )
    svip_node_id = data_model.property(
        "svipNodeID", int,
        array=False, optional=False,
        documentation="Node holding the master SVIP address.",
        dictionaryType=None
    )
    unique_id = data_model.property(
        "uniqueID", str,
        array=False, optional=False,
        documentation="Unique ID for the cluster.",
        dictionaryType=None
    )
    uuid = data_model.property(
        "uuid", UUID,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    attributes = data_model.property(
        "attributes", dict,
        array=False, optional=False,
        documentation="List of Name/Value pairs in JSON object format.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class GetClusterInfoResult(data_model.DataObject):
    """GetClusterInfoResult  

    :param cluster_info: [required] 
    :type cluster_info: ClusterInfo

    """
    cluster_info = data_model.property(
        "clusterInfo", ClusterInfo,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class VirtualNetwork(data_model.DataObject):
    """VirtualNetwork  

    :param virtual_network_id: [required] SolidFire unique identifier for a virtual network. 
    :type virtual_network_id: int

    :param virtual_network_tag: [required] VLAN Tag identifier. 
    :type virtual_network_tag: int

    :param address_blocks: [required] Range of address blocks currently assigned to the virtual network. available: Binary string in "1"s and "0"s. 1 equals the IP is available and 0 equals the IP is not available. The string is read from right to left with the digit to the far right being the first IP address in the list of addressBlocks. size: the size of this block of addresses. start: first IP address in the block. 
    :type address_blocks: AddressBlock

    :param name: [required] The name assigned to the virtual network. 
    :type name: str

    :param netmask: [required] IP address of the netmask for the virtual network. 
    :type netmask: str

    :param svip: [required] Storage IP address for the virtual network. 
    :type svip: str

    :param gateway:   
    :type gateway: str

    :param namespace:   
    :type namespace: bool

    :param attributes: [required] List of Name/Value pairs in JSON object format. 
    :type attributes: dict

    """
    virtual_network_id = data_model.property(
        "virtualNetworkID", int,
        array=False, optional=False,
        documentation="SolidFire unique identifier for a virtual network.",
        dictionaryType=None
    )
    virtual_network_tag = data_model.property(
        "virtualNetworkTag", int,
        array=False, optional=False,
        documentation="VLAN Tag identifier.",
        dictionaryType=None
    )
    address_blocks = data_model.property(
        "addressBlocks", AddressBlock,
        array=True, optional=False,
        documentation="[&#x27;Range of address blocks currently assigned to the virtual network.&#x27;, &#x27;available: Binary string in &quot;1&quot;s and &quot;0&quot;s. 1 equals the IP is available and 0 equals the IP is not available. The string is read from right to left with the digit to the far right being the first IP address in the list of addressBlocks.&#x27;, &#x27;size: the size of this block of addresses.&#x27;, &#x27;start: first IP address in the block.&#x27;]",
        dictionaryType=None
    )
    name = data_model.property(
        "name", str,
        array=False, optional=False,
        documentation="[&#x27;The name assigned to the virtual network.&#x27;]",
        dictionaryType=None
    )
    netmask = data_model.property(
        "netmask", str,
        array=False, optional=False,
        documentation="[&#x27;IP address of the netmask for the virtual network.&#x27;]",
        dictionaryType=None
    )
    svip = data_model.property(
        "svip", str,
        array=False, optional=False,
        documentation="[&#x27;Storage IP address for the virtual network.&#x27;]",
        dictionaryType=None
    )
    gateway = data_model.property(
        "gateway", str,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    namespace = data_model.property(
        "namespace", bool,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    attributes = data_model.property(
        "attributes", dict,
        array=False, optional=False,
        documentation="[&#x27;List of Name/Value pairs in JSON object format.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ListVirtualNetworksResult(data_model.DataObject):
    """ListVirtualNetworksResult  

    :param virtual_networks: [required] Object containing virtual network IP addresses. 
    :type virtual_networks: VirtualNetwork

    """
    virtual_networks = data_model.property(
        "virtualNetworks", VirtualNetwork,
        array=True, optional=False,
        documentation="Object containing virtual network IP addresses.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ModifyClusterFullThresholdResult(data_model.DataObject):
    """ModifyClusterFullThresholdResult  

    :param block_fullness: [required] Current computed level of block fullness of the cluster. Possible values: stage1Happy: No alerts or error conditions. stage2Aware: 3 nodes of capacity available. stage3Low: 2 nodes of capacity available. stage4Critical: 1 node of capacity available. No new volumes or clones can be created. stage5CompletelyConsumed: Completely consumed. Cluster is read-only, iSCSI connection is maintained but all writes are suspended. 
    :type block_fullness: str

    :param fullness: [required] Reflects the highest level of fullness between "blockFullness" and "metadataFullness". 
    :type fullness: str

    :param max_metadata_over_provision_factor: [required] A value representative of the number of times metadata space can be over provisioned relative to the amount of space available. For example, if there was enough metadata space to store 100 TiB of volumes and this number was set to 5, then 500 TiB worth of volumes could be created. 
    :type max_metadata_over_provision_factor: int

    :param metadata_fullness: [required] Current computed level of metadata fullness of the cluster. 
    :type metadata_fullness: str

    :param slice_reserve_used_threshold_pct: [required] Error condition; message sent to "Alerts" if the reserved slice utilization is greater than the sliceReserveUsedThresholdPct value returned. 
    :type slice_reserve_used_threshold_pct: int

    :param stage2_aware_threshold: [required] Awareness condition: Value that is set for "Stage 2" cluster threshold level. 
    :type stage2_aware_threshold: int

    :param stage2_block_threshold_bytes: [required] Number of bytes being used by the cluster at which a stage2 condition will exist. 
    :type stage2_block_threshold_bytes: int

    :param stage3_block_threshold_bytes: [required] Number of bytes being used by the cluster at which a stage3 condition will exist. 
    :type stage3_block_threshold_bytes: int

    :param stage3_block_threshold_percent: [required] The percent value set for stage3. At this percent full, a warning will be posted in the Alerts log. 
    :type stage3_block_threshold_percent: int

    :param stage3_low_threshold: [required] Error condition; message sent to "Alerts" that capacity on a cluster is getting low. 
    :type stage3_low_threshold: int

    :param stage4_critical_threshold: [required] Error condition; message sent to "Alerts" that capacity on a cluster is critically low. 
    :type stage4_critical_threshold: int

    :param stage4_block_threshold_bytes: [required] Number of bytes being used by the cluster at which a stage4 condition will exist. 
    :type stage4_block_threshold_bytes: int

    :param stage5_block_threshold_bytes: [required] Number of bytes being used by the cluster at which a stage5 condition will exist. 
    :type stage5_block_threshold_bytes: int

    :param sum_total_cluster_bytes: [required] Physical capacity of the cluster measured in bytes. 
    :type sum_total_cluster_bytes: int

    :param sum_total_metadata_cluster_bytes: [required] Total amount of space that can be used to store metadata. 
    :type sum_total_metadata_cluster_bytes: int

    :param sum_used_cluster_bytes: [required] Number of bytes used on the cluster. 
    :type sum_used_cluster_bytes: int

    :param sum_used_metadata_cluster_bytes: [required] Amount of space used on volume drives to store metadata. 
    :type sum_used_metadata_cluster_bytes: int

    """
    block_fullness = data_model.property(
        "blockFullness", str,
        array=False, optional=False,
        documentation="[&#x27;Current computed level of block fullness of the cluster.&#x27;, &#x27;Possible values: stage1Happy: No alerts or error conditions. stage2Aware: 3 nodes of capacity available. stage3Low: 2 nodes of capacity available. stage4Critical: 1 node of capacity available. No new volumes or clones can be created. stage5CompletelyConsumed: Completely consumed. Cluster is read-only, iSCSI connection is maintained but all writes are suspended.&#x27;]",
        dictionaryType=None
    )
    fullness = data_model.property(
        "fullness", str,
        array=False, optional=False,
        documentation="Reflects the highest level of fullness between &quot;blockFullness&quot; and &quot;metadataFullness&quot;.",
        dictionaryType=None
    )
    max_metadata_over_provision_factor = data_model.property(
        "maxMetadataOverProvisionFactor", int,
        array=False, optional=False,
        documentation="A value representative of the number of times metadata space can be over provisioned relative to the amount of space available. For example, if there was enough metadata space to store 100 TiB of volumes and this number was set to 5, then 500 TiB worth of volumes could be created.",
        dictionaryType=None
    )
    metadata_fullness = data_model.property(
        "metadataFullness", str,
        array=False, optional=False,
        documentation="Current computed level of metadata fullness of the cluster.",
        dictionaryType=None
    )
    slice_reserve_used_threshold_pct = data_model.property(
        "sliceReserveUsedThresholdPct", int,
        array=False, optional=False,
        documentation="Error condition; message sent to &quot;Alerts&quot; if the reserved slice utilization is greater than the sliceReserveUsedThresholdPct value returned.",
        dictionaryType=None
    )
    stage2_aware_threshold = data_model.property(
        "stage2AwareThreshold", int,
        array=False, optional=False,
        documentation="Awareness condition: Value that is set for &quot;Stage 2&quot; cluster threshold level.",
        dictionaryType=None
    )
    stage2_block_threshold_bytes = data_model.property(
        "stage2BlockThresholdBytes", int,
        array=False, optional=False,
        documentation="Number of bytes being used by the cluster at which a stage2 condition will exist.",
        dictionaryType=None
    )
    stage3_block_threshold_bytes = data_model.property(
        "stage3BlockThresholdBytes", int,
        array=False, optional=False,
        documentation="Number of bytes being used by the cluster at which a stage3 condition will exist.",
        dictionaryType=None
    )
    stage3_block_threshold_percent = data_model.property(
        "stage3BlockThresholdPercent", int,
        array=False, optional=False,
        documentation="The percent value set for stage3. At this percent full, a warning will be posted in the Alerts log.",
        dictionaryType=None
    )
    stage3_low_threshold = data_model.property(
        "stage3LowThreshold", int,
        array=False, optional=False,
        documentation="Error condition; message sent to &quot;Alerts&quot; that capacity on a cluster is getting low.",
        dictionaryType=None
    )
    stage4_critical_threshold = data_model.property(
        "stage4CriticalThreshold", int,
        array=False, optional=False,
        documentation="Error condition; message sent to &quot;Alerts&quot; that capacity on a cluster is critically low.",
        dictionaryType=None
    )
    stage4_block_threshold_bytes = data_model.property(
        "stage4BlockThresholdBytes", int,
        array=False, optional=False,
        documentation="Number of bytes being used by the cluster at which a stage4 condition will exist.",
        dictionaryType=None
    )
    stage5_block_threshold_bytes = data_model.property(
        "stage5BlockThresholdBytes", int,
        array=False, optional=False,
        documentation="Number of bytes being used by the cluster at which a stage5 condition will exist.",
        dictionaryType=None
    )
    sum_total_cluster_bytes = data_model.property(
        "sumTotalClusterBytes", int,
        array=False, optional=False,
        documentation="Physical capacity of the cluster measured in bytes.",
        dictionaryType=None
    )
    sum_total_metadata_cluster_bytes = data_model.property(
        "sumTotalMetadataClusterBytes", int,
        array=False, optional=False,
        documentation="Total amount of space that can be used to store metadata.",
        dictionaryType=None
    )
    sum_used_cluster_bytes = data_model.property(
        "sumUsedClusterBytes", int,
        array=False, optional=False,
        documentation="Number of bytes used on the cluster.",
        dictionaryType=None
    )
    sum_used_metadata_cluster_bytes = data_model.property(
        "sumUsedMetadataClusterBytes", int,
        array=False, optional=False,
        documentation="Amount of space used on volume drives to store metadata.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class GetVolumeEfficiencyRequest(data_model.DataObject):
    """GetVolumeEfficiencyRequest  

    :param volume_id: [required] Specifies the volume for which capacity is computed. 
    :type volume_id: int

    """
    volume_id = data_model.property(
        "volumeID", int,
        array=False, optional=False,
        documentation="Specifies the volume for which capacity is computed.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class CancelCloneRequest(data_model.DataObject):
    """CancelCloneRequest  

    :param clone_id: [required] 
    :type clone_id: int

    """
    clone_id = data_model.property(
        "cloneID", int,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class Service(data_model.DataObject):
    """Service  

    :param service_id: [required] Unique identifier for this service. 
    :type service_id: int

    :param service_type: [required] 
    :type service_type: str

    :param node_id: [required] The node this service resides on. 
    :type node_id: int

    :param associated_bv:  This service's associated bulk volume service. This will only be set if the service type is a slice service. 
    :type associated_bv: int

    :param associated_ts:  This service's associated transport service. This will only be set if the service type is a slice service. 
    :type associated_ts: int

    :param associated_vs:  This service's associated volume service. This will only be set if the service type is a slice service. 
    :type associated_vs: int

    :param async_result_ids: [required] The list of asynchronous jobs currently running for this service. 
    :type async_result_ids: int

    :param drive_id:  If this service resides on a drive, the ID of that drive. 
    :type drive_id: int

    :param first_time_startup: [required] Has this service started successfully? When a new drive is added to the system, the created service will initially have a value of false here. After the service has started, this value will be set to true. This can be used to check if the service has ever started. 
    :type first_time_startup: bool

    :param ipc_port: [required] The port used for intra-cluster communication. This will be in the 4000-4100 range. 
    :type ipc_port: int

    :param iscsi_port: [required] The port used for iSCSI traffic. This will only be set if the service type is a transport service. 
    :type iscsi_port: int

    :param status: [required] 
    :type status: str

    :param started_drive_ids: [required] 
    :type started_drive_ids: int

    :param drive_ids: [required] 
    :type drive_ids: int

    """
    service_id = data_model.property(
        "serviceID", int,
        array=False, optional=False,
        documentation="Unique identifier for this service.",
        dictionaryType=None
    )
    service_type = data_model.property(
        "serviceType", str,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    node_id = data_model.property(
        "nodeID", int,
        array=False, optional=False,
        documentation="[&#x27;The node this service resides on.&#x27;]",
        dictionaryType=None
    )
    associated_bv = data_model.property(
        "associatedBV", int,
        array=False, optional=True,
        documentation="[&quot;This service&#x27;s associated bulk volume service.&quot;, &#x27;This will only be set if the service type is a slice service.&#x27;]",
        dictionaryType=None
    )
    associated_ts = data_model.property(
        "associatedTS", int,
        array=False, optional=True,
        documentation="[&quot;This service&#x27;s associated transport service.&quot;, &#x27;This will only be set if the service type is a slice service.&#x27;]",
        dictionaryType=None
    )
    associated_vs = data_model.property(
        "associatedVS", int,
        array=False, optional=True,
        documentation="[&quot;This service&#x27;s associated volume service.&quot;, &#x27;This will only be set if the service type is a slice service.&#x27;]",
        dictionaryType=None
    )
    async_result_ids = data_model.property(
        "asyncResultIDs", int,
        array=True, optional=False,
        documentation="[&#x27;The list of asynchronous jobs currently running for this service.&#x27;]",
        dictionaryType=None
    )
    drive_id = data_model.property(
        "driveID", int,
        array=False, optional=True,
        documentation="[&#x27;If this service resides on a drive, the ID of that drive.&#x27;]",
        dictionaryType=None
    )
    first_time_startup = data_model.property(
        "firstTimeStartup", bool,
        array=False, optional=False,
        documentation="[&#x27;Has this service started successfully?&#x27;, &#x27;When a new drive is added to the system, the created service will initially have a value of false here.&#x27;, &#x27;After the service has started, this value will be set to true.&#x27;, &#x27;This can be used to check if the service has ever started.&#x27;]",
        dictionaryType=None
    )
    ipc_port = data_model.property(
        "ipcPort", int,
        array=False, optional=False,
        documentation="[&#x27;The port used for intra-cluster communication.&#x27;, &#x27;This will be in the 4000-4100 range.&#x27;]",
        dictionaryType=None
    )
    iscsi_port = data_model.property(
        "iscsiPort", int,
        array=False, optional=False,
        documentation="[&#x27;The port used for iSCSI traffic.&#x27;, &#x27;This will only be set if the service type is a transport service.&#x27;]",
        dictionaryType=None
    )
    status = data_model.property(
        "status", str,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    started_drive_ids = data_model.property(
        "startedDriveIDs", int,
        array=True, optional=False,
        documentation="",
        dictionaryType=None
    )
    drive_ids = data_model.property(
        "driveIDs", int,
        array=True, optional=False,
        documentation="",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class VirtualNetworkAddress(data_model.DataObject):
    """VirtualNetworkAddress  

    :param virtual_network_id: [required] SolidFire unique identifier for a virtual network. 
    :type virtual_network_id: int

    :param address: [required] Virtual Network Address. 
    :type address: str

    """
    virtual_network_id = data_model.property(
        "virtualNetworkID", int,
        array=False, optional=False,
        documentation="SolidFire unique identifier for a virtual network.",
        dictionaryType=None
    )
    address = data_model.property(
        "address", str,
        array=False, optional=False,
        documentation="Virtual Network Address.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class Node(data_model.DataObject):
    """Node  
    A node refers to an individual machine in a cluster.
    Each active node hosts a master service, which is responsible for managing the drives and other services on its node.
    After a node is made active, its drives will become available for addition to the cluster.

    :param node_id: [required] The unique identifier for this node. 
    :type node_id: int

    :param associated_master_service_id: [required] The master service responsible for controlling other services on this node. 
    :type associated_master_service_id: int

    :param associated_fservice_id: [required] 
    :type associated_fservice_id: int

    :param fibre_channel_target_port_group: [required] 
    :type fibre_channel_target_port_group: str

    :param name: [required] 
    :type name: str

    :param platform_info: [required] Information about the platform this node is. 
    :type platform_info: Platform

    :param software_version: [required] The version of SolidFire software this node is currently running. 
    :type software_version: str

    :param cip: [required] IP address used for both intra- and inter-cluster communication. 
    :type cip: str

    :param cipi: [required] The machine's name for the "cip" interface. 
    :type cipi: str

    :param mip: [required] IP address used for cluster management (hosting the API and web site). 
    :type mip: str

    :param mipi: [required] The machine's name for the "mip" interface. 
    :type mipi: str

    :param sip: [required] IP address used for iSCSI traffic. 
    :type sip: str

    :param sipi: [required] The machine's name for the "sip" interface. 
    :type sipi: str

    :param uuid: [required] UUID of node. 
    :type uuid: UUID

    :param virtual_networks: [required] 
    :type virtual_networks: VirtualNetworkAddress

    :param attributes: [required] 
    :type attributes: dict

    """
    node_id = data_model.property(
        "nodeID", int,
        array=False, optional=False,
        documentation="[&#x27;The unique identifier for this node.&#x27;]",
        dictionaryType=None
    )
    associated_master_service_id = data_model.property(
        "associatedMasterServiceID", int,
        array=False, optional=False,
        documentation="[&#x27;The master service responsible for controlling other services on this node.&#x27;]",
        dictionaryType=None
    )
    associated_fservice_id = data_model.property(
        "associatedFServiceID", int,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    fibre_channel_target_port_group = data_model.property(
        "fibreChannelTargetPortGroup", str,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    name = data_model.property(
        "name", str,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    platform_info = data_model.property(
        "platformInfo", Platform,
        array=False, optional=False,
        documentation="Information about the platform this node is.",
        dictionaryType=None
    )
    software_version = data_model.property(
        "softwareVersion", str,
        array=False, optional=False,
        documentation="The version of SolidFire software this node is currently running.",
        dictionaryType=None
    )
    cip = data_model.property(
        "cip", str,
        array=False, optional=False,
        documentation="IP address used for both intra- and inter-cluster communication.",
        dictionaryType=None
    )
    cipi = data_model.property(
        "cipi", str,
        array=False, optional=False,
        documentation="The machine&#x27;s name for the &quot;cip&quot; interface.",
        dictionaryType=None
    )
    mip = data_model.property(
        "mip", str,
        array=False, optional=False,
        documentation="[&#x27;IP address used for cluster management (hosting the API and web site).&#x27;]",
        dictionaryType=None
    )
    mipi = data_model.property(
        "mipi", str,
        array=False, optional=False,
        documentation="The machine&#x27;s name for the &quot;mip&quot; interface.",
        dictionaryType=None
    )
    sip = data_model.property(
        "sip", str,
        array=False, optional=False,
        documentation="[&#x27;IP address used for iSCSI traffic.&#x27;]",
        dictionaryType=None
    )
    sipi = data_model.property(
        "sipi", str,
        array=False, optional=False,
        documentation="The machine&#x27;s name for the &quot;sip&quot; interface.",
        dictionaryType=None
    )
    uuid = data_model.property(
        "uuid", UUID,
        array=False, optional=False,
        documentation="UUID of node.",
        dictionaryType=None
    )
    virtual_networks = data_model.property(
        "virtualNetworks", VirtualNetworkAddress,
        array=True, optional=False,
        documentation="",
        dictionaryType=None
    )
    attributes = data_model.property(
        "attributes", dict,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class Drive(data_model.DataObject):
    """Drive  

    :param drive_id: [required] A unique identifier for this drive. 
    :type drive_id: int

    :param node_id: [required] The node this drive is located. If the drive has been physically removed from the node, this is where it was last seen. 
    :type node_id: int

    :param assigned_service:  If this drive is hosting a service, the identifier for that service. 
    :type assigned_service: int

    :param async_result_ids: [required] The list of asynchronous jobs currently running on the drive (for example: a secure erase job). 
    :type async_result_ids: int

    :param capacity: [required] The raw capacity of this drive in bytes. 
    :type capacity: int

    :param serial: [required] The manufacturer's serial number for this drive. 
    :type serial: str

    :param slot:  Slot number in the server chassis where this drive is located. If the drive has been physically removed from the node, this will not have a value. 
    :type slot: int

    :param drive_status: [required] The current status of this drive. 
    :type drive_status: str

    :param drive_type: [required] The type of this drive. 
    :type drive_type: str

    :param reserved_slice_file_capacity:  
    :type reserved_slice_file_capacity: int

    :param customer_slice_file_capacity:  
    :type customer_slice_file_capacity: int

    :param attributes: [required] List of Name/Value pairs in JSON object format. 
    :type attributes: dict

    """
    drive_id = data_model.property(
        "driveID", int,
        array=False, optional=False,
        documentation="[&#x27;A unique identifier for this drive.&#x27;]",
        dictionaryType=None
    )
    node_id = data_model.property(
        "nodeID", int,
        array=False, optional=False,
        documentation="[&#x27;The node this drive is located.&#x27;, &#x27;If the drive has been physically removed from the node, this is where it was last seen.&#x27;]",
        dictionaryType=None
    )
    assigned_service = data_model.property(
        "assignedService", int,
        array=False, optional=True,
        documentation="[&#x27;If this drive is hosting a service, the identifier for that service.&#x27;]",
        dictionaryType=None
    )
    async_result_ids = data_model.property(
        "asyncResultIDs", int,
        array=True, optional=False,
        documentation="[&#x27;The list of asynchronous jobs currently running on the drive (for example: a secure erase job).&#x27;]",
        dictionaryType=None
    )
    capacity = data_model.property(
        "capacity", int,
        array=False, optional=False,
        documentation="[&#x27;The raw capacity of this drive in bytes.&#x27;]",
        dictionaryType=None
    )
    serial = data_model.property(
        "serial", str,
        array=False, optional=False,
        documentation="The manufacturer&#x27;s serial number for this drive.",
        dictionaryType=None
    )
    slot = data_model.property(
        "slot", int,
        array=False, optional=True,
        documentation="[&#x27;Slot number in the server chassis where this drive is located.&#x27;, &#x27;If the drive has been physically removed from the node, this will not have a value.&#x27;]",
        dictionaryType=None
    )
    drive_status = data_model.property(
        "driveStatus", str,
        array=False, optional=False,
        documentation="The current status of this drive.",
        dictionaryType=None
    )
    drive_type = data_model.property(
        "driveType", str,
        array=False, optional=False,
        documentation="The type of this drive.",
        dictionaryType=None
    )
    reserved_slice_file_capacity = data_model.property(
        "reservedSliceFileCapacity", int,
        array=False, optional=True,
        documentation="",
        dictionaryType=None
    )
    customer_slice_file_capacity = data_model.property(
        "customerSliceFileCapacity", int,
        array=False, optional=True,
        documentation="",
        dictionaryType=None
    )
    attributes = data_model.property(
        "attributes", dict,
        array=False, optional=False,
        documentation="List of Name/Value pairs in JSON object format.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class DetailedService(data_model.DataObject):
    """DetailedService  

    :param service: [required] 
    :type service: Service

    :param node: [required] 
    :type node: Node

    :param drive:  
    :type drive: Drive

    :param drives: [required] 
    :type drives: Drive

    """
    service = data_model.property(
        "service", Service,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    node = data_model.property(
        "node", Node,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    drive = data_model.property(
        "drive", Drive,
        array=False, optional=True,
        documentation="",
        dictionaryType=None
    )
    drives = data_model.property(
        "drives", Drive,
        array=True, optional=False,
        documentation="",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ListServicesResult(data_model.DataObject):
    """ListServicesResult  

    :param services: [required] 
    :type services: DetailedService

    """
    services = data_model.property(
        "services", DetailedService,
        array=True, optional=False,
        documentation="",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class StartVolumePairingRequest(data_model.DataObject):
    """StartVolumePairingRequest  

    :param volume_id: [required] The ID of the volume on which to start the pairing process. 
    :type volume_id: int

    :param mode:  The mode of the volume on which to start the pairing process. The mode can only be set if the volume is the source volume. Possible values: Async: (default if no mode parameter specified) Writes are acknowledged when they complete locally. The cluster does not wait for writes to be replicated to the target cluster. Sync: Source acknowledges write when the data is stored locally and on the remote cluster. SnapshotsOnly: Only snapshots created on the source cluster will be replicated. Active writes from the source volume will not be replicated. 
    :type mode: str

    """
    volume_id = data_model.property(
        "volumeID", int,
        array=False, optional=False,
        documentation="The ID of the volume on which to start the pairing process.",
        dictionaryType=None
    )
    mode = data_model.property(
        "mode", str,
        array=False, optional=True,
        documentation="[&#x27;The mode of the volume on which to start the pairing process. The mode can only be set if the volume is the source volume.&#x27;, &#x27;Possible values:&#x27;, &#x27;Async: (default if no mode parameter specified) Writes are acknowledged when they complete locally. The cluster does not wait for writes to be replicated to the target cluster.&#x27;, &#x27;Sync: Source acknowledges write when the data is stored locally and on the remote cluster.&#x27;, &#x27;SnapshotsOnly: Only snapshots created on the source cluster will be replicated. Active writes from the source volume will not be replicated.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class DisableSnmpResult(data_model.DataObject):
    """DisableSnmpResult  

    """

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ListActiveNodesResult(data_model.DataObject):
    """ListActiveNodesResult  

    :param nodes: [required] 
    :type nodes: Node

    """
    nodes = data_model.property(
        "nodes", Node,
        array=True, optional=False,
        documentation="",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class BackupTarget(data_model.DataObject):
    """BackupTarget  
    The object containing information about a backup target.

    :param name: [required] Name for the backup target. 
    :type name: str

    :param backup_target_id: [required] Unique identifier assigned to the backup target. 
    :type backup_target_id: int

    :param attributes:  List of Name/Value pairs in JSON object format. 
    :type attributes: dict

    """
    name = data_model.property(
        "name", str,
        array=False, optional=False,
        documentation="[&#x27;Name for the backup target.&#x27;]",
        dictionaryType=None
    )
    backup_target_id = data_model.property(
        "backupTargetID", int,
        array=False, optional=False,
        documentation="[&#x27;Unique identifier assigned to the backup target.&#x27;]",
        dictionaryType=None
    )
    attributes = data_model.property(
        "attributes", dict,
        array=False, optional=True,
        documentation="List of Name/Value pairs in JSON object format.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ListBackupTargetsResult(data_model.DataObject):
    """ListBackupTargetsResult  

    :param backup_targets: [required] Objects returned for each backup target. 
    :type backup_targets: BackupTarget

    """
    backup_targets = data_model.property(
        "backupTargets", BackupTarget,
        array=True, optional=False,
        documentation="Objects returned for each backup target.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class FibreChannelSession(data_model.DataObject):
    """FibreChannelSession  
    FibreChannelSession contains information about each Fibre Channel session that is visible to the cluster and what target ports it is visible on.

    :param initiator_wwpn: [required] The WWPN of the initiator which is logged into the target port. 
    :type initiator_wwpn: str

    :param node_id: [required] The node owning the Fibre Channel session. 
    :type node_id: int

    :param service_id: [required] The service ID of the FService owning this Fibre Channel session 
    :type service_id: int

    :param target_wwpn: [required] The WWPN of the target port involved in this session. 
    :type target_wwpn: str

    :param volume_access_group_id:  The ID of the volume access group to which the initiatorWWPN belongs. If not in a volume access group, the value will be null. 
    :type volume_access_group_id: int

    """
    initiator_wwpn = data_model.property(
        "initiatorWWPN", str,
        array=False, optional=False,
        documentation="The WWPN of the initiator which is logged into the target port.",
        dictionaryType=None
    )
    node_id = data_model.property(
        "nodeID", int,
        array=False, optional=False,
        documentation="The node owning the Fibre Channel session.",
        dictionaryType=None
    )
    service_id = data_model.property(
        "serviceID", int,
        array=False, optional=False,
        documentation="The service ID of the FService owning this Fibre Channel session",
        dictionaryType=None
    )
    target_wwpn = data_model.property(
        "targetWWPN", str,
        array=False, optional=False,
        documentation="The WWPN of the target port involved in this session.",
        dictionaryType=None
    )
    volume_access_group_id = data_model.property(
        "volumeAccessGroupID", int,
        array=False, optional=True,
        documentation="The ID of the volume access group to which the initiatorWWPN belongs. If not in a volume access group, the value will be null.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ListFibreChannelSessionsResult(data_model.DataObject):
    """ListFibreChannelSessionsResult  
    Used to return information about the Fibre Channel sessions.

    :param sessions: [required] A list of FibreChannelSession objects with information about the Fibre Channel session. 
    :type sessions: FibreChannelSession

    """
    sessions = data_model.property(
        "sessions", FibreChannelSession,
        array=True, optional=False,
        documentation="A list of FibreChannelSession objects with information about the Fibre Channel session.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class SetNetworkConfigResult(data_model.DataObject):
    """SetNetworkConfigResult  

    :param network: [required] 
    :type network: Network

    """
    network = data_model.property(
        "network", Network,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class SnmpSendTestTrapsResult(data_model.DataObject):
    """SnmpSendTestTrapsResult  

    :param status: [required] 
    :type status: str

    """
    status = data_model.property(
        "status", str,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class RemoveBackupTargetRequest(data_model.DataObject):
    """RemoveBackupTargetRequest  

    :param backup_target_id: [required] Unique target ID of the target to remove. 
    :type backup_target_id: int

    """
    backup_target_id = data_model.property(
        "backupTargetID", int,
        array=False, optional=False,
        documentation="[&#x27;Unique target ID of the target to remove.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ListClusterFaultsRequest(data_model.DataObject):
    """ListClusterFaultsRequest  

    :param exceptions:  
    :type exceptions: bool

    :param best_practices:  Include faults triggered by sub-optimal system configuration. Possible values: true, false 
    :type best_practices: bool

    :param update:  
    :type update: bool

    :param fault_types:  Determines the types of faults returned: current: List active, unresolved faults. resolved: List faults that were previously detected and resolved. all: (Default) List both current and resolved faults. You can see the fault status in the 'resolved' field of the Cluster Fault object. 
    :type fault_types: str

    """
    exceptions = data_model.property(
        "exceptions", bool,
        array=False, optional=True,
        documentation="",
        dictionaryType=None
    )
    best_practices = data_model.property(
        "bestPractices", bool,
        array=False, optional=True,
        documentation="[&#x27;Include faults triggered by sub-optimal system configuration.&#x27;, &#x27;Possible values: true, false&#x27;]",
        dictionaryType=None
    )
    update = data_model.property(
        "update", bool,
        array=False, optional=True,
        documentation="",
        dictionaryType=None
    )
    fault_types = data_model.property(
        "faultTypes", str,
        array=False, optional=True,
        documentation="[&#x27;Determines the types of faults returned: current: List active, unresolved faults.&#x27;, &#x27;resolved: List faults that were previously detected and resolved.&#x27;, &quot;all: (Default) List both current and resolved faults. You can see the fault status in the &#x27;resolved&#x27; field of the Cluster Fault object.&quot;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class TestPingResult(data_model.DataObject):
    """TestPingResult  

    :param result: [required] Result of the ping test. 
    :type result: str

    :param duration: [required] The total duration of the ping test. 
    :type duration: str

    :param details: [required] List of each IP the node was able to communicate with. 
    :type details: str

    """
    result = data_model.property(
        "result", str,
        array=False, optional=False,
        documentation="Result of the ping test.",
        dictionaryType=None
    )
    duration = data_model.property(
        "duration", str,
        array=False, optional=False,
        documentation="The total duration of the ping test.",
        dictionaryType=None
    )
    details = data_model.property(
        "details", str,
        array=False, optional=False,
        documentation="List of each IP the node was able to communicate with.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class PurgeDeletedVolumeResult(data_model.DataObject):
    """PurgeDeletedVolumeResult  

    """

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class GetBackupTargetResult(data_model.DataObject):
    """GetBackupTargetResult  

    :param backup_target: [required] Object returned for backup target. 
    :type backup_target: BackupTarget

    """
    backup_target = data_model.property(
        "backupTarget", BackupTarget,
        array=False, optional=False,
        documentation="Object returned for backup target.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class GroupCloneVolumeMember(data_model.DataObject):
    """GroupCloneVolumeMember  
    Represents the relationship between the source Volume and cloned Volume IDs.

    :param volume_id: [required] The VolumeID of the cloned volume. 
    :type volume_id: int

    :param src_volume_id: [required] The VolumeID of the source volume. 
    :type src_volume_id: int

    """
    volume_id = data_model.property(
        "volumeID", int,
        array=False, optional=False,
        documentation="The VolumeID of the cloned volume.",
        dictionaryType=None
    )
    src_volume_id = data_model.property(
        "srcVolumeID", int,
        array=False, optional=False,
        documentation="The VolumeID of the source volume.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class CloneMultipleVolumesResult(data_model.DataObject):
    """CloneMultipleVolumesResult  

    :param async_handle: [required] A value returned from an asynchronous method call. 
    :type async_handle: int

    :param group_clone_id: [required] Unique ID of the new group clone. 
    :type group_clone_id: int

    :param members: [required] List of volumeIDs for the source and destination volume pairs. 
    :type members: GroupCloneVolumeMember

    """
    async_handle = data_model.property(
        "asyncHandle", int,
        array=False, optional=False,
        documentation="A value returned from an asynchronous method call.",
        dictionaryType=None
    )
    group_clone_id = data_model.property(
        "groupCloneID", int,
        array=False, optional=False,
        documentation="Unique ID of the new group clone.",
        dictionaryType=None
    )
    members = data_model.property(
        "members", GroupCloneVolumeMember,
        array=True, optional=False,
        documentation="List of volumeIDs for the source and destination volume pairs.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ListVolumeStatsByVirtualVolumeResult(data_model.DataObject):
    """ListVolumeStatsByVirtualVolumeResult  

    :param volume_stats: [required] 
    :type volume_stats: VolumeStats

    """
    volume_stats = data_model.property(
        "volumeStats", VolumeStats,
        array=True, optional=False,
        documentation="",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class SetDefaultQoSRequest(data_model.DataObject):
    """SetDefaultQoSRequest  

    :param min_iops:  The minimum number of sustained IOPS that are provided by the cluster to a volume. 
    :type min_iops: int

    :param max_iops:  The maximum number of sustained IOPS that are provided by the cluster to a volume. 
    :type max_iops: int

    :param burst_iops:  The maximum number of IOPS allowed in a short burst scenario. 
    :type burst_iops: int

    """
    min_iops = data_model.property(
        "minIOPS", int,
        array=False, optional=True,
        documentation="The minimum number of sustained IOPS that are provided by the cluster to a volume.",
        dictionaryType=None
    )
    max_iops = data_model.property(
        "maxIOPS", int,
        array=False, optional=True,
        documentation="The maximum number of sustained IOPS that are provided by the cluster to a volume.",
        dictionaryType=None
    )
    burst_iops = data_model.property(
        "burstIOPS", int,
        array=False, optional=True,
        documentation="The maximum number of IOPS allowed in a short burst scenario.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class AddDrivesResult(data_model.DataObject):
    """AddDrivesResult  

    """

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class GetVolumeStatsRequest(data_model.DataObject):
    """GetVolumeStatsRequest  

    :param volume_id: [required] Specifies the volume for which statistics is gathered. 
    :type volume_id: int

    """
    volume_id = data_model.property(
        "volumeID", int,
        array=False, optional=False,
        documentation="Specifies the volume for which statistics is gathered.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class GetDriveStatsRequest(data_model.DataObject):
    """GetDriveStatsRequest  

    :param drive_id: [required] Specifies the drive for which statistics are gathered. 
    :type drive_id: int

    """
    drive_id = data_model.property(
        "driveID", int,
        array=False, optional=False,
        documentation="Specifies the drive for which statistics are gathered.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class CompleteVolumePairingRequest(data_model.DataObject):
    """CompleteVolumePairingRequest  

    :param volume_pairing_key: [required] The key returned from the "StartVolumePairing" API method. 
    :type volume_pairing_key: str

    :param volume_id: [required] The ID of volume on which to complete the pairing process. 
    :type volume_id: int

    """
    volume_pairing_key = data_model.property(
        "volumePairingKey", str,
        array=False, optional=False,
        documentation="The key returned from the &quot;StartVolumePairing&quot; API method.",
        dictionaryType=None
    )
    volume_id = data_model.property(
        "volumeID", int,
        array=False, optional=False,
        documentation="The ID of volume on which to complete the pairing process.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ListVolumeStatsByVirtualVolumeRequest(data_model.DataObject):
    """ListVolumeStatsByVirtualVolumeRequest  

    :param virtual_volume_ids:  A list of virtual volume  IDs for which to retrieve information. If you specify this parameter, the method returns information about only these virtual volumes. 
    :type virtual_volume_ids: UUID

    """
    virtual_volume_ids = data_model.property(
        "virtualVolumeIDs", UUID,
        array=True, optional=True,
        documentation="A list of virtual volume  IDs for which to retrieve information. If you specify this parameter, the method returns information about only these virtual volumes.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class GetNodeHardwareInfoRequest(data_model.DataObject):
    """GetNodeHardwareInfoRequest  

    :param node_id: [required] The ID of the node for which hardware information is being requested.  Information about a  node is returned if a   node is specified. 
    :type node_id: int

    """
    node_id = data_model.property(
        "nodeID", int,
        array=False, optional=False,
        documentation="The ID of the node for which hardware information is being requested.  Information about a  node is returned if a   node is specified.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class GetVolumeAccessGroupLunAssignmentsRequest(data_model.DataObject):
    """GetVolumeAccessGroupLunAssignmentsRequest  

    :param volume_access_group_id: [required] Unique volume access group ID used to return information. 
    :type volume_access_group_id: int

    """
    volume_access_group_id = data_model.property(
        "volumeAccessGroupID", int,
        array=False, optional=False,
        documentation="Unique volume access group ID used to return information.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class AddInitiatorsToVolumeAccessGroupRequest(data_model.DataObject):
    """AddInitiatorsToVolumeAccessGroupRequest  

    :param volume_access_group_id: [required] The ID of the volume access group to modify. 
    :type volume_access_group_id: int

    :param initiators: [required] List of initiators to add to the volume access group. 
    :type initiators: str

    """
    volume_access_group_id = data_model.property(
        "volumeAccessGroupID", int,
        array=False, optional=False,
        documentation="The ID of the volume access group to modify.",
        dictionaryType=None
    )
    initiators = data_model.property(
        "initiators", str,
        array=True, optional=False,
        documentation="[&#x27;List of initiators to add to the volume access group.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class SetConfigResult(data_model.DataObject):
    """SetConfigResult  

    :param config: [required] The new and current configuration for the node. 
    :type config: Config

    """
    config = data_model.property(
        "config", Config,
        array=False, optional=False,
        documentation="The new and current configuration for the node.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class SecureEraseDrivesRequest(data_model.DataObject):
    """SecureEraseDrivesRequest  

    :param drives: [required] List of driveIDs to secure erase. 
    :type drives: int

    """
    drives = data_model.property(
        "drives", int,
        array=True, optional=False,
        documentation="List of driveIDs to secure erase.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class DriveInfo(data_model.DataObject):
    """DriveInfo  

    :param capacity: [required] Total capacity of the drive, in bytes. 
    :type capacity: int

    :param drive_id: [required] DriveID for this drive. 
    :type drive_id: int

    :param node_id: [required] NodeID where this drive is located. 
    :type node_id: int

    :param serial: [required] Drive serial number. 
    :type serial: str

    :param slot: [required] Slot number in the server chassis where this drive is located, or -1 if SATADimm used for internal metadata drive. 
    :type slot: int

    :param status: [required] 
    :type status: str

    :param type: [required] 
    :type type: str

    :param attributes: [required] List of Name/Value pairs in JSON object format. 
    :type attributes: dict

    """
    capacity = data_model.property(
        "capacity", int,
        array=False, optional=False,
        documentation="[&#x27;Total capacity of the drive, in bytes.&#x27;]",
        dictionaryType=None
    )
    drive_id = data_model.property(
        "driveID", int,
        array=False, optional=False,
        documentation="DriveID for this drive.",
        dictionaryType=None
    )
    node_id = data_model.property(
        "nodeID", int,
        array=False, optional=False,
        documentation="NodeID where this drive is located.",
        dictionaryType=None
    )
    serial = data_model.property(
        "serial", str,
        array=False, optional=False,
        documentation="Drive serial number.",
        dictionaryType=None
    )
    slot = data_model.property(
        "slot", int,
        array=False, optional=False,
        documentation="Slot number in the server chassis where this drive is located, or -1 if SATADimm used for internal metadata drive.",
        dictionaryType=None
    )
    status = data_model.property(
        "status", str,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    type = data_model.property(
        "type", str,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    attributes = data_model.property(
        "attributes", dict,
        array=False, optional=False,
        documentation="[&#x27;List of Name/Value pairs in JSON object format.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ListDrivesResult(data_model.DataObject):
    """ListDrivesResult  

    :param drives: [required] Information for the drives that are connected to the cluster. 
    :type drives: DriveInfo

    """
    drives = data_model.property(
        "drives", DriveInfo,
        array=True, optional=False,
        documentation="Information for the drives that are connected to the cluster.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ListVolumeStatsRequest(data_model.DataObject):
    """ListVolumeStatsRequest  

    :param volume_ids:  
    :type volume_ids: int

    """
    volume_ids = data_model.property(
        "volumeIDs", int,
        array=True, optional=True,
        documentation="",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class StartBulkVolumeWriteRequest(data_model.DataObject):
    """StartBulkVolumeWriteRequest  

    :param volume_id: [required] ID of the volume to be written to. 
    :type volume_id: int

    :param format: [required] The format of the volume data. Can be either: uncompressed: every byte of the volume is returned without any compression. native: opaque data is returned that is smaller and more efficiently stored and written on a subsequent bulk volume write 
    :type format: str

    :param script:  Executable name of a script. If no script name is given then the key and URL are necessary to access SolidFire nodes. The script runs on the primary node and the key and URL is returned to the script so the local web server can be contacted. 
    :type script: str

    :param script_parameters:  JSON parameters to pass to the script. 
    :type script_parameters: str

    :param attributes:  JSON attributes for the bulk volume job. 
    :type attributes: dict

    """
    volume_id = data_model.property(
        "volumeID", int,
        array=False, optional=False,
        documentation="ID of the volume to be written to.",
        dictionaryType=None
    )
    format = data_model.property(
        "format", str,
        array=False, optional=False,
        documentation="[&#x27;The format of the volume data. Can be either:&#x27;, &#x27;uncompressed: every byte of the volume is returned without any compression.&#x27;, &#x27;native: opaque data is returned that is smaller and more efficiently stored and written on a subsequent bulk volume write&#x27;]",
        dictionaryType=None
    )
    script = data_model.property(
        "script", str,
        array=False, optional=True,
        documentation="[&#x27;Executable name of a script.&#x27;, &#x27;If no script name is given then the key and URL are necessary to access SolidFire nodes.&#x27;, &#x27;The script runs on the primary node and the key and URL is returned to the script so the local web server can be contacted.&#x27;]",
        dictionaryType=None
    )
    script_parameters = data_model.property(
        "scriptParameters", str,
        array=False, optional=True,
        documentation="[&#x27;JSON parameters to pass to the script.&#x27;]",
        dictionaryType=None
    )
    attributes = data_model.property(
        "attributes", dict,
        array=False, optional=True,
        documentation="[&#x27;JSON attributes for the bulk volume job.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ModifyVolumePairRequest(data_model.DataObject):
    """ModifyVolumePairRequest  

    :param volume_id: [required] Identification number of the volume to be modified. 
    :type volume_id: int

    :param paused_manual:  Valid values that can be entered: true: to pause volume replication. false: to restart volume replication. If no value is specified, no change in replication is performed. 
    :type paused_manual: bool

    :param mode:  Volume replication mode. Possible values: Async: Writes are acknowledged when they complete locally. The cluster does not wait for writes to be replicated to the target cluster. Sync: The source acknowledges the write when the data is stored locally and on the remote cluster. SnapshotsOnly: Only snapshots created on the source cluster will be replicated. Active writes from the source volume are not replicated. 
    :type mode: str

    """
    volume_id = data_model.property(
        "volumeID", int,
        array=False, optional=False,
        documentation="Identification number of the volume to be modified.",
        dictionaryType=None
    )
    paused_manual = data_model.property(
        "pausedManual", bool,
        array=False, optional=True,
        documentation="[&#x27;Valid values that can be entered:&#x27;, &#x27;true: to pause volume replication.&#x27;, &#x27;false: to restart volume replication.&#x27;, &#x27;If no value is specified, no change in replication is performed.&#x27;]",
        dictionaryType=None
    )
    mode = data_model.property(
        "mode", str,
        array=False, optional=True,
        documentation="[&#x27;Volume replication mode.&#x27;, &#x27;Possible values:&#x27;, &#x27;Async: Writes are acknowledged when they complete locally. The cluster does not wait for writes to be replicated to the target cluster.&#x27;, &#x27;Sync: The source acknowledges the write when the data is stored locally and on the remote cluster.&#x27;, &#x27;SnapshotsOnly: Only snapshots created on the source cluster will be replicated. Active writes from the source volume are not replicated.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class SnapshotRemoteStatus(data_model.DataObject):
    """SnapshotRemoteStatus  

    :param remote_status: [required] 
    :type remote_status: str

    :param volume_pair_uuid: [required] The snapshot is done and is writable (the active branch of the slice). 
    :type volume_pair_uuid: UUID

    """
    remote_status = data_model.property(
        "remoteStatus", str,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    volume_pair_uuid = data_model.property(
        "volumePairUUID", UUID,
        array=False, optional=False,
        documentation="The snapshot is done and is writable (the active branch of the slice).",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class Snapshot(data_model.DataObject):
    """Snapshot  
    Snapshots is an object containing information about each snapshot made for a volume.
    The return object includes information for the active snapshot as well as each snapshot created for the volume.

    :param snapshot_id: [required] Unique ID for this snapshot. 
    :type snapshot_id: int

    :param volume_id: [required] The volume this snapshot was taken of. 
    :type volume_id: int

    :param name: [required] A name for this snapshot. It is not necessarily unique. 
    :type name: str

    :param checksum: [required] A string that represents the correct digits in the stored snapshot. This checksum can be used later to compare other snapshots to detect errors in the data. 
    :type checksum: str

    :param enable_remote_replication: [required] Identifies if snapshot is enabled for remote replication. 
    :type enable_remote_replication: bool

    :param expiration_reason: [required] Indicates how the snapshot expiration was set. Possible values: api: expiration time was set by using the API. none: there is no expiration time set. test: expiration time was set for testing. 
    :type expiration_reason: str

    :param expiration_time: [required] The time at which this snapshot will expire and be purged from the cluster. 
    :type expiration_time: str

    :param remote_statuses:  Current remote status of the snapshot remoteStatus: Possible values: Present: Snapshot exists on a remote cluster Not Present: Snapshot does not exist on remote cluster Syncing: This is a target cluster and it is currently replicating the snapshot Deleted: This is a target cluster, the snapshot has been deleted, and it still exists on the source. volumePairUUID: universal identifier of the volume pair 
    :type remote_statuses: SnapshotRemoteStatus

    :param status: [required] Current status of the snapshot Preparing: A snapshot that is being prepared for use and is not yet writable. Done: A snapshot that has finished being prepared and is now usable. Active: This snapshot is the active branch. 
    :type status: str

    :param snapshot_uuid: [required] Universal Unique ID of an existing snapshot. 
    :type snapshot_uuid: UUID

    :param total_size: [required] Total size of this snapshot in bytes. It is equivalent to totalSize of the volume when this snapshot was taken. 
    :type total_size: int

    :param group_id:  If present, the ID of the group this snapshot is a part of. If not present, this snapshot is not part of a group. 
    :type group_id: int

    :param group_snapshot_uuid: [required] The current "members" results contains information about each snapshot in the group. Each of these members will have a "uuid" parameter for the snapshot's UUID. 
    :type group_snapshot_uuid: UUID

    :param create_time: [required] The time this snapshot was taken. 
    :type create_time: str

    :param virtual_volume_id: [required] The ID of the virtual volume with which the snapshot is associated. 
    :type virtual_volume_id: UUID

    :param attributes: [required] List of Name/Value pairs in JSON object format. 
    :type attributes: dict

    """
    snapshot_id = data_model.property(
        "snapshotID", int,
        array=False, optional=False,
        documentation="Unique ID for this snapshot.",
        dictionaryType=None
    )
    volume_id = data_model.property(
        "volumeID", int,
        array=False, optional=False,
        documentation="The volume this snapshot was taken of.",
        dictionaryType=None
    )
    name = data_model.property(
        "name", str,
        array=False, optional=False,
        documentation="[&#x27;A name for this snapshot.&#x27;, &#x27;It is not necessarily unique.&#x27;]",
        dictionaryType=None
    )
    checksum = data_model.property(
        "checksum", str,
        array=False, optional=False,
        documentation="[&#x27;A string that represents the correct digits in the stored snapshot.&#x27;, &#x27;This checksum can be used later to compare other snapshots to detect errors in the data.&#x27;]",
        dictionaryType=None
    )
    enable_remote_replication = data_model.property(
        "enableRemoteReplication", bool,
        array=False, optional=False,
        documentation="Identifies if snapshot is enabled for remote replication.",
        dictionaryType=None
    )
    expiration_reason = data_model.property(
        "expirationReason", str,
        array=False, optional=False,
        documentation="[&#x27;Indicates how the snapshot expiration was set. Possible values:&#x27;, &#x27;api: expiration time was set by using the API.&#x27;, &#x27;none: there is no expiration time set.&#x27;, &#x27;test: expiration time was set for testing.&#x27;]",
        dictionaryType=None
    )
    expiration_time = data_model.property(
        "expirationTime", str,
        array=False, optional=False,
        documentation="The time at which this snapshot will expire and be purged from the cluster.",
        dictionaryType=None
    )
    remote_statuses = data_model.property(
        "remoteStatuses", SnapshotRemoteStatus,
        array=True, optional=True,
        documentation="[&#x27;Current remote status of the snapshot remoteStatus: Possible values:&#x27;, &#x27;Present: Snapshot exists on a remote cluster&#x27;, &#x27;Not Present: Snapshot does not exist on remote cluster&#x27;, &#x27;Syncing: This is a target cluster and it is currently replicating the snapshot&#x27;, &#x27;Deleted: This is a target cluster, the snapshot has been deleted, and it still exists on the source.&#x27;, &#x27;volumePairUUID: universal identifier of the volume pair&#x27;]",
        dictionaryType=None
    )
    status = data_model.property(
        "status", str,
        array=False, optional=False,
        documentation="[&#x27;Current status of the snapshot&#x27;, &#x27;Preparing: A snapshot that is being prepared for use and is not yet writable.&#x27;, &#x27;Done: A snapshot that has finished being prepared and is now usable.&#x27;, &#x27;Active: This snapshot is the active branch.&#x27;]",
        dictionaryType=None
    )
    snapshot_uuid = data_model.property(
        "snapshotUUID", UUID,
        array=False, optional=False,
        documentation="Universal Unique ID of an existing snapshot.",
        dictionaryType=None
    )
    total_size = data_model.property(
        "totalSize", int,
        array=False, optional=False,
        documentation="[&#x27;Total size of this snapshot in bytes.&#x27;, &#x27;It is equivalent to totalSize of the volume when this snapshot was taken.&#x27;]",
        dictionaryType=None
    )
    group_id = data_model.property(
        "groupID", int,
        array=False, optional=True,
        documentation="[&#x27;If present, the ID of the group this snapshot is a part of.&#x27;, &#x27;If not present, this snapshot is not part of a group.&#x27;]",
        dictionaryType=None
    )
    group_snapshot_uuid = data_model.property(
        "groupSnapshotUUID", UUID,
        array=False, optional=False,
        documentation="[&#x27;The current &quot;members&quot; results contains information about each snapshot in the group.&#x27;, &#x27;Each of these members will have a &quot;uuid&quot; parameter for the snapshot\&#x27;s UUID.&#x27;]",
        dictionaryType=None
    )
    create_time = data_model.property(
        "createTime", str,
        array=False, optional=False,
        documentation="The time this snapshot was taken.",
        dictionaryType=None
    )
    virtual_volume_id = data_model.property(
        "virtualVolumeID", UUID,
        array=False, optional=False,
        documentation="The ID of the virtual volume with which the snapshot is associated.",
        dictionaryType=None
    )
    attributes = data_model.property(
        "attributes", dict,
        array=False, optional=False,
        documentation="List of Name/Value pairs in JSON object format.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class VirtualVolumeInfo(data_model.DataObject):
    """VirtualVolumeInfo  

    :param virtual_volume_id: [required] 
    :type virtual_volume_id: UUID

    :param parent_virtual_volume_id: [required] 
    :type parent_virtual_volume_id: UUID

    :param storage_container_id: [required] 
    :type storage_container_id: UUID

    :param storage_container: [required] 
    :type storage_container: StorageContainer

    :param volume_id: [required] 
    :type volume_id: int

    :param snapshot_id: [required] 
    :type snapshot_id: int

    :param virtual_volume_type: [required] 
    :type virtual_volume_type: str

    :param status: [required] 
    :type status: str

    :param bindings: [required] 
    :type bindings: int

    :param children: [required] 
    :type children: UUID

    :param metadata: [required] 
    :type metadata: dict

    :param snapshot_info: [required] 
    :type snapshot_info: Snapshot

    :param volume_info: [required] 
    :type volume_info: Volume

    """
    virtual_volume_id = data_model.property(
        "virtualVolumeID", UUID,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    parent_virtual_volume_id = data_model.property(
        "parentVirtualVolumeID", UUID,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    storage_container_id = data_model.property(
        "storageContainerID", UUID,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    storage_container = data_model.property(
        "storageContainer", StorageContainer,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    volume_id = data_model.property(
        "volumeID", int,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    snapshot_id = data_model.property(
        "snapshotID", int,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    virtual_volume_type = data_model.property(
        "virtualVolumeType", str,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    status = data_model.property(
        "status", str,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    bindings = data_model.property(
        "bindings", int,
        array=True, optional=False,
        documentation="",
        dictionaryType=None
    )
    children = data_model.property(
        "children", UUID,
        array=True, optional=False,
        documentation="",
        dictionaryType=None
    )
    metadata = data_model.property(
        "metadata", dict,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    snapshot_info = data_model.property(
        "snapshotInfo", Snapshot,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    volume_info = data_model.property(
        "volumeInfo", Volume,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class VirtualVolumeBinding(data_model.DataObject):
    """VirtualVolumeBinding  

    :param protocol_endpoint_id: [required] The unique ID of the protocol endpoint. 
    :type protocol_endpoint_id: UUID

    :param protocol_endpoint_in_band_id: [required] The scsiNAADeviceID of the protocol endpoint. For more information, see protocolEndpoint. 
    :type protocol_endpoint_in_band_id: str

    :param protocol_endpoint_type: [required] The type of protocol endpoint. SCSI is the only value returned for the protocol endpoint type. 
    :type protocol_endpoint_type: str

    :param virtual_volume_binding_id: [required] The unique ID of the virtual volume binding object. 
    :type virtual_volume_binding_id: int

    :param virtual_volume_host_id: [required] The unique ID of the virtual volume host. 
    :type virtual_volume_host_id: UUID

    :param virtual_volume_id: [required] The unique ID of the virtual volume. 
    :type virtual_volume_id: UUID

    :param virtual_volume_secondary_id: [required] The secondary ID of the virtual volume. 
    :type virtual_volume_secondary_id: str

    :param virtual_volume: [required] An object describing the bound volume or snapshot. 
    :type virtual_volume: VirtualVolumeInfo

    :param protocol_endpoint: [required] An object describing the protocol endpoint to which the virtual volume is bound. 
    :type protocol_endpoint: UUID

    :param virtual_volume_host: [required] An object describing the host to which this binding corresponds. 
    :type virtual_volume_host: VirtualVolumeHost

    """
    protocol_endpoint_id = data_model.property(
        "protocolEndpointID", UUID,
        array=False, optional=False,
        documentation="The unique ID of the protocol endpoint.",
        dictionaryType=None
    )
    protocol_endpoint_in_band_id = data_model.property(
        "protocolEndpointInBandID", str,
        array=False, optional=False,
        documentation="The scsiNAADeviceID of the protocol endpoint. For more information, see protocolEndpoint.",
        dictionaryType=None
    )
    protocol_endpoint_type = data_model.property(
        "protocolEndpointType", str,
        array=False, optional=False,
        documentation="The type of protocol endpoint. SCSI is the only value returned for the protocol endpoint type.",
        dictionaryType=None
    )
    virtual_volume_binding_id = data_model.property(
        "virtualVolumeBindingID", int,
        array=False, optional=False,
        documentation="The unique ID of the virtual volume binding object.",
        dictionaryType=None
    )
    virtual_volume_host_id = data_model.property(
        "virtualVolumeHostID", UUID,
        array=False, optional=False,
        documentation="The unique ID of the virtual volume host.",
        dictionaryType=None
    )
    virtual_volume_id = data_model.property(
        "virtualVolumeID", UUID,
        array=False, optional=False,
        documentation="The unique ID of the virtual volume.",
        dictionaryType=None
    )
    virtual_volume_secondary_id = data_model.property(
        "virtualVolumeSecondaryID", str,
        array=False, optional=False,
        documentation="The secondary ID of the virtual volume.",
        dictionaryType=None
    )
    virtual_volume = data_model.property(
        "virtualVolume", VirtualVolumeInfo,
        array=False, optional=False,
        documentation="An object describing the bound volume or snapshot.",
        dictionaryType=None
    )
    protocol_endpoint = data_model.property(
        "protocolEndpoint", UUID,
        array=False, optional=False,
        documentation="An object describing the protocol endpoint to which the virtual volume is bound.",
        dictionaryType=None
    )
    virtual_volume_host = data_model.property(
        "virtualVolumeHost", VirtualVolumeHost,
        array=False, optional=False,
        documentation="An object describing the host to which this binding corresponds.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ListVirtualVolumeBindingsResult(data_model.DataObject):
    """ListVirtualVolumeBindingsResult  

    :param bindings: [required] Describes the VVol <-> Host binding. 
    :type bindings: VirtualVolumeBinding

    """
    bindings = data_model.property(
        "bindings", VirtualVolumeBinding,
        array=True, optional=False,
        documentation="Describes the VVol &lt;-&gt; Host binding.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ListVolumesRequest(data_model.DataObject):
    """ListVolumesRequest  

    :param start_volume_id:  The ID of the first volume to list. This can be useful for paging results. By default, this starts at the lowest VolumeID. 
    :type start_volume_id: int

    :param limit:  The maximum number of volumes to return from the API. 
    :type limit: int

    :param volume_status:  If specified, filter to only volumes with the provided status. By default, list all volumes. 
    :type volume_status: str

    :param accounts:  If specified, only fetch volumes which belong to the provided accounts. By default, list volumes for all accounts. 
    :type accounts: int

    :param is_paired:  If specified, only fetch volumes which are paired (if true) or non-paired (if false). By default, list all volumes regardless of their pairing status. 
    :type is_paired: bool

    :param volume_ids:  If specified, only fetch volumes specified in this list. This option cannot be specified if startVolumeID, limit, or accounts option is specified. 
    :type volume_ids: int

    """
    start_volume_id = data_model.property(
        "startVolumeID", int,
        array=False, optional=True,
        documentation="[&#x27;The ID of the first volume to list.&#x27;, &#x27;This can be useful for paging results.&#x27;, &#x27;By default, this starts at the lowest VolumeID.&#x27;]",
        dictionaryType=None
    )
    limit = data_model.property(
        "limit", int,
        array=False, optional=True,
        documentation="[&#x27;The maximum number of volumes to return from the API.&#x27;]",
        dictionaryType=None
    )
    volume_status = data_model.property(
        "volumeStatus", str,
        array=False, optional=True,
        documentation="[&#x27;If specified, filter to only volumes with the provided status.&#x27;, &#x27;By default, list all volumes.&#x27;]",
        dictionaryType=None
    )
    accounts = data_model.property(
        "accounts", int,
        array=True, optional=True,
        documentation="[&#x27;If specified, only fetch volumes which belong to the provided accounts.&#x27;, &#x27;By default, list volumes for all accounts.&#x27;]",
        dictionaryType=None
    )
    is_paired = data_model.property(
        "isPaired", bool,
        array=False, optional=True,
        documentation="[&#x27;If specified, only fetch volumes which are paired (if true) or non-paired (if false).&#x27;, &#x27;By default, list all volumes regardless of their pairing status.&#x27;]",
        dictionaryType=None
    )
    volume_ids = data_model.property(
        "volumeIDs", int,
        array=True, optional=True,
        documentation="[&#x27;If specified, only fetch volumes specified in this list.&#x27;, &#x27;This option cannot be specified if startVolumeID, limit, or accounts option is specified.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ModifyClusterAdminRequest(data_model.DataObject):
    """ModifyClusterAdminRequest  

    :param cluster_admin_id: [required] ClusterAdminID for the Cluster Admin or LDAP Cluster Admin to modify. 
    :type cluster_admin_id: int

    :param password:  Password used to authenticate this Cluster Admin. 
    :type password: str

    :param access:  Controls which methods this Cluster Admin can use. For more details on the levels of access, see "Access Control" in the Element API Guide. 
    :type access: str

    :param attributes:  List of Name/Value pairs in JSON object format. 
    :type attributes: dict

    """
    cluster_admin_id = data_model.property(
        "clusterAdminID", int,
        array=False, optional=False,
        documentation="ClusterAdminID for the Cluster Admin or LDAP Cluster Admin to modify.",
        dictionaryType=None
    )
    password = data_model.property(
        "password", str,
        array=False, optional=True,
        documentation="Password used to authenticate this Cluster Admin.",
        dictionaryType=None
    )
    access = data_model.property(
        "access", str,
        array=True, optional=True,
        documentation="Controls which methods this Cluster Admin can use. For more details on the levels of access, see &quot;Access Control&quot; in the Element API Guide.",
        dictionaryType=None
    )
    attributes = data_model.property(
        "attributes", dict,
        array=False, optional=True,
        documentation="List of Name/Value pairs in JSON object format.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class AddAccountRequest(data_model.DataObject):
    """AddAccountRequest  

    :param username: [required] Unique username for this account. (May be 1 to 64 characters in length). 
    :type username: str

    :param initiator_secret:  CHAP secret to use for the initiator. Should be 12-16 characters long and impenetrable. The CHAP initiator secrets must be unique and cannot be the same as the target CHAP secret.  If not specified, a random secret is created. 
    :type initiator_secret: CHAPSecret

    :param target_secret:  CHAP secret to use for the target (mutual CHAP authentication). Should be 12-16 characters long and impenetrable. The CHAP target secrets must be unique and cannot be the same as the initiator CHAP secret.  If not specified, a random secret is created. 
    :type target_secret: CHAPSecret

    :param attributes:  List of Name/Value pairs in JSON object format. 
    :type attributes: dict

    """
    username = data_model.property(
        "username", str,
        array=False, optional=False,
        documentation="[&#x27;Unique username for this account.&#x27;, &#x27;(May be 1 to 64 characters in length).&#x27;]",
        dictionaryType=None
    )
    initiator_secret = data_model.property(
        "initiatorSecret", CHAPSecret,
        array=False, optional=True,
        documentation="[&#x27;CHAP secret to use for the initiator.&#x27;, &#x27;Should be 12-16 characters long and impenetrable.&#x27;, &#x27;The CHAP initiator secrets must be unique and cannot be the same as the target CHAP secret.&#x27;, u&#x27;&#x27;, &#x27;If not specified, a random secret is created.&#x27;]",
        dictionaryType=None
    )
    target_secret = data_model.property(
        "targetSecret", CHAPSecret,
        array=False, optional=True,
        documentation="[&#x27;CHAP secret to use for the target (mutual CHAP authentication).&#x27;, &#x27;Should be 12-16 characters long and impenetrable.&#x27;, &#x27;The CHAP target secrets must be unique and cannot be the same as the initiator CHAP secret.&#x27;, u&#x27;&#x27;, &#x27;If not specified, a random secret is created.&#x27;]",
        dictionaryType=None
    )
    attributes = data_model.property(
        "attributes", dict,
        array=False, optional=True,
        documentation="List of Name/Value pairs in JSON object format.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class GetAccountByNameRequest(data_model.DataObject):
    """GetAccountByNameRequest  

    :param username: [required] Username for the account. 
    :type username: str

    """
    username = data_model.property(
        "username", str,
        array=False, optional=False,
        documentation="Username for the account.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ModifyClusterAdminResult(data_model.DataObject):
    """ModifyClusterAdminResult  

    """

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class SnmpNetwork(data_model.DataObject):
    """SnmpNetwork  
    The SNMP network object contains information about SNMP configuration for the cluster nodes. SNMP v3 is supported on SolidFire clusters.

    :param access: [required] ro: read-only access.* rw: for read-write access. rosys: for read-only access to a restricted set of system information *SolidFire recommends that all networks other than the default "localhost" be set to "ro" access, because all SolidFire MIB objects are read-only. 
    :type access: str

    :param cidr: [required] A CIDR network mask. This network mask must be an integer greater than or equal to 0, and less than or equal to 32. It must also not be equal to 31. 
    :type cidr: int

    :param community: [required] SNMP community string. 
    :type community: str

    :param network: [required] This parameter along with the cidr variable is used to control which network the access and community string apply to. The special value of "default" is used to specify an entry that applies to all networks. The cidr mask is ignored when network value is either a host name or default. 
    :type network: str

    """
    access = data_model.property(
        "access", str,
        array=False, optional=False,
        documentation="[&#x27;ro: read-only access.*&#x27;, &#x27;rw: for read-write access.&#x27;, &#x27;rosys: for read-only access to a restricted set of system information&#x27;, &#x27;*SolidFire recommends that all networks other than the default &quot;localhost&quot; be set to &quot;ro&quot; access, because all SolidFire MIB objects are read-only.&#x27;]",
        dictionaryType=None
    )
    cidr = data_model.property(
        "cidr", int,
        array=False, optional=False,
        documentation="[&#x27;A CIDR network mask. This network mask must be an integer greater than or equal to 0, and less than or equal to 32. It must also not be equal to 31.&#x27;]",
        dictionaryType=None
    )
    community = data_model.property(
        "community", str,
        array=False, optional=False,
        documentation="[&#x27;SNMP community string.&#x27;]",
        dictionaryType=None
    )
    network = data_model.property(
        "network", str,
        array=False, optional=False,
        documentation="[&#x27;This parameter along with the cidr variable is used to control which network the access and community string apply to. The special value of &quot;default&quot; is used to specify an entry that applies to all networks. The cidr mask is ignored when network value is either a host name or default.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class GetSnmpACLResult(data_model.DataObject):
    """GetSnmpACLResult  

    :param networks: [required] List of networks and what type of access they have to the SNMP servers running on the cluster nodes. Present if SNMP v3 is disabled. 
    :type networks: SnmpNetwork

    :param usm_users: [required] List of users and the type of access they have to the SNMP servers running on the cluster nodes. Present if SNMP v3 is enabled. 
    :type usm_users: SnmpV3UsmUser

    """
    networks = data_model.property(
        "networks", SnmpNetwork,
        array=True, optional=False,
        documentation="List of networks and what type of access they have to the SNMP servers running on the cluster nodes. Present if SNMP v3 is disabled.",
        dictionaryType=None
    )
    usm_users = data_model.property(
        "usmUsers", SnmpV3UsmUser,
        array=True, optional=False,
        documentation="List of users and the type of access they have to the SNMP servers running on the cluster nodes. Present if SNMP v3 is enabled.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class RemoveVirtualNetworkResult(data_model.DataObject):
    """RemoveVirtualNetworkResult  

    """

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class EnableSnmpRequest(data_model.DataObject):
    """EnableSnmpRequest  

    :param snmp_v3_enabled: [required] If set to "true", then SNMP v3 is enabled on each node in the cluster. If set to "false", then SNMP v2 is enabled. 
    :type snmp_v3_enabled: bool

    """
    snmp_v3_enabled = data_model.property(
        "snmpV3Enabled", bool,
        array=False, optional=False,
        documentation="If set to &quot;true&quot;, then SNMP v3 is enabled on each node in the cluster. If set to &quot;false&quot;, then SNMP v2 is enabled.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class SetSnmpInfoResult(data_model.DataObject):
    """SetSnmpInfoResult  

    """

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class DisableLdapAuthenticationResult(data_model.DataObject):
    """DisableLdapAuthenticationResult  

    """

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class CreateVolumeResult(data_model.DataObject):
    """CreateVolumeResult  

    :param volume_id: [required] VolumeID for the newly created volume. 
    :type volume_id: int

    :param curve: [required] The curve is a set of key-value pairs. The keys are I/O sizes in bytes. The values represent the cost performing an IOP at a specific I/O size. The curve is calculated relative to a 4096 byte operation set at 100 IOPS. 
    :type curve: dict

    """
    volume_id = data_model.property(
        "volumeID", int,
        array=False, optional=False,
        documentation="VolumeID for the newly created volume.",
        dictionaryType=None
    )
    curve = data_model.property(
        "curve", dict,
        array=False, optional=False,
        documentation="[&#x27;The curve is a set of key-value pairs.&#x27;, &#x27;The keys are I/O sizes in bytes.&#x27;, &#x27;The values represent the cost performing an IOP at a specific I/O size.&#x27;, &#x27;The curve is calculated relative to a 4096 byte operation set at 100 IOPS.&#x27;]",
        dictionaryType=int
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class PurgeDeletedVolumesResult(data_model.DataObject):
    """PurgeDeletedVolumesResult  

    """

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class PurgeDeletedVolumesRequest(data_model.DataObject):
    """PurgeDeletedVolumesRequest  

    :param volume_ids:  A list of volumeIDs of volumes to be purged from the system. 
    :type volume_ids: int

    :param account_ids:  A list of accountIDs. All of the volumes from all of the specified accounts are purged from the system. 
    :type account_ids: int

    :param volume_access_group_ids:  A list of volumeAccessGroupIDs. All of the volumes from all of the specified Volume Access Groups are purged from the system. 
    :type volume_access_group_ids: int

    """
    volume_ids = data_model.property(
        "volumeIDs", int,
        array=True, optional=True,
        documentation="A list of volumeIDs of volumes to be purged from the system.",
        dictionaryType=None
    )
    account_ids = data_model.property(
        "accountIDs", int,
        array=True, optional=True,
        documentation="A list of accountIDs. All of the volumes from all of the specified accounts are purged from the system.",
        dictionaryType=None
    )
    volume_access_group_ids = data_model.property(
        "volumeAccessGroupIDs", int,
        array=True, optional=True,
        documentation="A list of volumeAccessGroupIDs. All of the volumes from all of the specified Volume Access Groups are purged from the system.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ListSnapshotsResult(data_model.DataObject):
    """ListSnapshotsResult  

    :param snapshots: [required] Information about each snapshot for each volume. If volumeID is not provided, all snapshots for all volumes is returned. Snapshots that are in a group will be returned with a "groupID". Snapshots that are enabled for replication. 
    :type snapshots: Snapshot

    """
    snapshots = data_model.property(
        "snapshots", Snapshot,
        array=True, optional=False,
        documentation="[&#x27;Information about each snapshot for each volume.&#x27;, &#x27;If volumeID is not provided, all snapshots for all volumes is returned.&#x27;, &#x27;Snapshots that are in a group will be returned with a &quot;groupID&quot;.&#x27;, &#x27;Snapshots that are enabled for replication.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class TestPingRequest(data_model.DataObject):
    """TestPingRequest  

    :param attempts:  Specifies the number of times the system should repeat the test ping. Default is 5. 
    :type attempts: int

    :param hosts:  Specify address or hostnames of devices to ping. 
    :type hosts: str

    :param total_timeout_sec:  Specifies the length of time the ping should wait for a system response before issuing the next ping attempt or ending the process. 
    :type total_timeout_sec: int

    :param packet_size:  Specify the number of bytes to send in the ICMP packet sent to each IP. Number be less than the maximum MTU specified in the network configuration. 
    :type packet_size: int

    :param ping_timeout_msec:  Specify the number of milliseconds to wait for each individual ping response. Default is 500ms. 
    :type ping_timeout_msec: int

    """
    attempts = data_model.property(
        "attempts", int,
        array=False, optional=True,
        documentation="Specifies the number of times the system should repeat the test ping. Default is 5.",
        dictionaryType=None
    )
    hosts = data_model.property(
        "hosts", str,
        array=False, optional=True,
        documentation="Specify address or hostnames of devices to ping.",
        dictionaryType=None
    )
    total_timeout_sec = data_model.property(
        "totalTimeoutSec", int,
        array=False, optional=True,
        documentation="Specifies the length of time the ping should wait for a system response before issuing the next ping attempt or ending the process.",
        dictionaryType=None
    )
    packet_size = data_model.property(
        "packetSize", int,
        array=False, optional=True,
        documentation="Specify the number of bytes to send in the ICMP packet sent to each IP. Number be less than the maximum MTU specified in the network configuration.",
        dictionaryType=None
    )
    ping_timeout_msec = data_model.property(
        "pingTimeoutMsec", int,
        array=False, optional=True,
        documentation="Specify the number of milliseconds to wait for each individual ping response. Default is 500ms.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ShutdownResult(data_model.DataObject):
    """ShutdownResult  

    :param failed: [required] 
    :type failed: int

    :param successful: [required] 
    :type successful: int

    """
    failed = data_model.property(
        "failed", int,
        array=True, optional=False,
        documentation="",
        dictionaryType=None
    )
    successful = data_model.property(
        "successful", int,
        array=True, optional=False,
        documentation="",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class NodeStatsNodes(data_model.DataObject):
    """NodeStatsNodes  

    :param nodes: [required] Node activity information for a single node. 
    :type nodes: NodeStatsInfo

    """
    nodes = data_model.property(
        "nodes", NodeStatsInfo,
        array=True, optional=False,
        documentation="Node activity information for a single node.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ListNodeStatsResult(data_model.DataObject):
    """ListNodeStatsResult  

    :param node_stats: [required] Node activity information for all nodes. 
    :type node_stats: NodeStatsNodes

    """
    node_stats = data_model.property(
        "nodeStats", NodeStatsNodes,
        array=False, optional=False,
        documentation="Node activity information for all nodes.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class CreateVolumeRequest(data_model.DataObject):
    """CreateVolumeRequest  

    :param name: [required] Name of the volume. Not required to be unique, but it is recommended. May be 1 to 64 characters in length. 
    :type name: str

    :param account_id: [required] AccountID for the owner of this volume. 
    :type account_id: int

    :param total_size: [required] Total size of the volume, in bytes. Size is rounded up to the nearest 1MB size. 
    :type total_size: int

    :param enable512e: [required] Should the volume provides 512-byte sector emulation? 
    :type enable512e: bool

    :param qos:  Initial quality of service settings for this volume.  Volumes created without specified QoS values are created with the default values for QoS. Default values for a volume can be found by running the GetDefaultQoS method. 
    :type qos: QoS

    :param attributes:  List of Name/Value pairs in JSON object format. 
    :type attributes: dict

    """
    name = data_model.property(
        "name", str,
        array=False, optional=False,
        documentation="[&#x27;Name of the volume.&#x27;, &#x27;Not required to be unique, but it is recommended.&#x27;, &#x27;May be 1 to 64 characters in length.&#x27;]",
        dictionaryType=None
    )
    account_id = data_model.property(
        "accountID", int,
        array=False, optional=False,
        documentation="AccountID for the owner of this volume.",
        dictionaryType=None
    )
    total_size = data_model.property(
        "totalSize", int,
        array=False, optional=False,
        documentation="Total size of the volume, in bytes. Size is rounded up to the nearest 1MB size.",
        dictionaryType=None
    )
    enable512e = data_model.property(
        "enable512e", bool,
        array=False, optional=False,
        documentation="Should the volume provides 512-byte sector emulation?",
        dictionaryType=None
    )
    qos = data_model.property(
        "qos", QoS,
        array=False, optional=True,
        documentation="[&#x27;Initial quality of service settings for this volume.&#x27;, u&#x27;&#x27;, &#x27;Volumes created without specified QoS values are created with the default values for QoS.&#x27;, &#x27;Default values for a volume can be found by running the GetDefaultQoS method.&#x27;]",
        dictionaryType=None
    )
    attributes = data_model.property(
        "attributes", dict,
        array=False, optional=True,
        documentation="List of Name/Value pairs in JSON object format.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class AddVirtualNetworkResult(data_model.DataObject):
    """AddVirtualNetworkResult  

    :param virtual_network_id: [required] The virtual network ID of the new virtual network. 
    :type virtual_network_id: int

    """
    virtual_network_id = data_model.property(
        "virtualNetworkID", int,
        array=False, optional=False,
        documentation="The virtual network ID of the new virtual network.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ClusterFaultInfo(data_model.DataObject):
    """ClusterFaultInfo  

    :param severity: [required] 
    :type severity: str

    :param type: [required] 
    :type type: str

    :param code: [required] 
    :type code: str

    :param details: [required] 
    :type details: str

    :param node_hardware_fault_id: [required] 
    :type node_hardware_fault_id: int

    :param node_id: [required] 
    :type node_id: int

    :param service_id: [required] 
    :type service_id: int

    :param drive_id: [required] 
    :type drive_id: int

    :param resolved: [required] 
    :type resolved: bool

    :param cluster_fault_id: [required] 
    :type cluster_fault_id: int

    :param date: [required] 
    :type date: str

    :param resolved_date: [required] 
    :type resolved_date: str

    :param data: [required] 
    :type data: str

    """
    severity = data_model.property(
        "severity", str,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    type = data_model.property(
        "type", str,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    code = data_model.property(
        "code", str,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    details = data_model.property(
        "details", str,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    node_hardware_fault_id = data_model.property(
        "nodeHardwareFaultID", int,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    node_id = data_model.property(
        "nodeID", int,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    service_id = data_model.property(
        "serviceID", int,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    drive_id = data_model.property(
        "driveID", int,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    resolved = data_model.property(
        "resolved", bool,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    cluster_fault_id = data_model.property(
        "clusterFaultID", int,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    date = data_model.property(
        "date", str,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    resolved_date = data_model.property(
        "resolvedDate", str,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    data = data_model.property(
        "data", str,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ListClusterFaultsResult(data_model.DataObject):
    """ListClusterFaultsResult  

    :param faults: [required] The list of Cluster Fault objects. 
    :type faults: ClusterFaultInfo

    """
    faults = data_model.property(
        "faults", ClusterFaultInfo,
        array=True, optional=False,
        documentation="The list of Cluster Fault objects.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class DeleteInitiatorsResult(data_model.DataObject):
    """DeleteInitiatorsResult  

    """

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class GetAsyncResultRequest(data_model.DataObject):
    """GetAsyncResultRequest  

    :param async_handle: [required] A value that was returned from the original asynchronous method call. 
    :type async_handle: int

    """
    async_handle = data_model.property(
        "asyncHandle", int,
        array=False, optional=False,
        documentation="A value that was returned from the original asynchronous method call.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class RemoveDrivesRequest(data_model.DataObject):
    """RemoveDrivesRequest  

    :param drives: [required] List of driveIDs to remove from the cluster. 
    :type drives: int

    """
    drives = data_model.property(
        "drives", int,
        array=True, optional=False,
        documentation="List of driveIDs to remove from the cluster.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class GetNodeStatsRequest(data_model.DataObject):
    """GetNodeStatsRequest  

    :param node_id: [required] Specifies the node for which statistics are gathered. 
    :type node_id: int

    """
    node_id = data_model.property(
        "nodeID", int,
        array=False, optional=False,
        documentation="Specifies the node for which statistics are gathered.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class AddLdapClusterAdminRequest(data_model.DataObject):
    """AddLdapClusterAdminRequest  

    :param username: [required] The distinguished user name for the new LDAP cluster admin. 
    :type username: str

    :param access: [required] Controls which methods this Cluster Admin can use. For more details on the levels of access, see the Access Control appendix in the SolidFire API Reference. 
    :type access: str

    :param accept_eula:  Indicate your acceptance of the End User License Agreement when creating this cluster admin. To accept the EULA, set this parameter to true. 
    :type accept_eula: bool

    :param attributes:  List of Name/Value pairs in JSON object format. 
    :type attributes: dict

    """
    username = data_model.property(
        "username", str,
        array=False, optional=False,
        documentation="The distinguished user name for the new LDAP cluster admin.",
        dictionaryType=None
    )
    access = data_model.property(
        "access", str,
        array=True, optional=False,
        documentation="Controls which methods this Cluster Admin can use. For more details on the levels of access, see the Access Control appendix in the SolidFire API Reference.",
        dictionaryType=None
    )
    accept_eula = data_model.property(
        "acceptEula", bool,
        array=False, optional=True,
        documentation="Indicate your acceptance of the End User License Agreement when creating this cluster admin. To accept the EULA, set this parameter to true.",
        dictionaryType=None
    )
    attributes = data_model.property(
        "attributes", dict,
        array=False, optional=True,
        documentation="List of Name/Value pairs in JSON object format.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class StartBulkVolumeReadResult(data_model.DataObject):
    """StartBulkVolumeReadResult  

    :param async_handle: [required] ID of the async process to be checked for completion. 
    :type async_handle: int

    :param key: [required] Opaque key uniquely identifying the session. 
    :type key: str

    :param url: [required] URL to access the node's web server 
    :type url: str

    """
    async_handle = data_model.property(
        "asyncHandle", int,
        array=False, optional=False,
        documentation="ID of the async process to be checked for completion.",
        dictionaryType=None
    )
    key = data_model.property(
        "key", str,
        array=False, optional=False,
        documentation="Opaque key uniquely identifying the session.",
        dictionaryType=None
    )
    url = data_model.property(
        "url", str,
        array=False, optional=False,
        documentation="URL to access the node&#x27;s web server",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class CancelCloneResult(data_model.DataObject):
    """CancelCloneResult  

    """

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class AddVirtualNetworkRequest(data_model.DataObject):
    """AddVirtualNetworkRequest  

    :param virtual_network_tag: [required] A unique virtual network (VLAN) tag. Supported values are 1 to 4095 (the number zero (0) is not supported). 
    :type virtual_network_tag: int

    :param name: [required] User defined name for the new virtual network. 
    :type name: str

    :param address_blocks: [required] Unique Range of IP addresses to include in the virtual network. Attributes for this parameter are: start: start of the IP address range. (String) size: numbre of IP addresses to include in the block. (Integer) 
    :type address_blocks: AddressBlock

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
    virtual_network_tag = data_model.property(
        "virtualNetworkTag", int,
        array=False, optional=False,
        documentation="A unique virtual network (VLAN) tag. Supported values are 1 to 4095 (the number zero (0) is not supported).",
        dictionaryType=None
    )
    name = data_model.property(
        "name", str,
        array=False, optional=False,
        documentation="User defined name for the new virtual network.",
        dictionaryType=None
    )
    address_blocks = data_model.property(
        "addressBlocks", AddressBlock,
        array=True, optional=False,
        documentation="[&#x27;Unique Range of IP addresses to include in the virtual network.&#x27;, &#x27;Attributes for this parameter are:&#x27;, &#x27;start: start of the IP address range. (String)&#x27;, &#x27;size: numbre of IP addresses to include in the block. (Integer)&#x27;]",
        dictionaryType=None
    )
    netmask = data_model.property(
        "netmask", str,
        array=False, optional=False,
        documentation="[&#x27;Unique netmask for the virtual network being created.&#x27;]",
        dictionaryType=None
    )
    svip = data_model.property(
        "svip", str,
        array=False, optional=False,
        documentation="[&#x27;Unique storage IP address for the virtual network being created.&#x27;]",
        dictionaryType=None
    )
    gateway = data_model.property(
        "gateway", str,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    namespace = data_model.property(
        "namespace", bool,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    attributes = data_model.property(
        "attributes", dict,
        array=False, optional=True,
        documentation="[&#x27;List of Name/Value pairs in JSON object format.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class CreateClusterRequest(data_model.DataObject):
    """CreateClusterRequest  

    :param accept_eula:  Indicate your acceptance of the End User License Agreement when creating this cluster. To accept the EULA, set this parameter to true. 
    :type accept_eula: bool

    :param mvip: [required] Floating (virtual) IP address for the cluster on the management network. 
    :type mvip: str

    :param svip: [required] Floating (virtual) IP address for the cluster on the storage (iSCSI) network. 
    :type svip: str

    :param rep_count: [required] Number of replicas of each piece of data to store in the cluster. Valid value is "2". 
    :type rep_count: int

    :param username: [required] User name for the cluster admin. 
    :type username: str

    :param password: [required] Initial password for the cluster admin account. 
    :type password: str

    :param nodes: [required] CIP/SIP addresses of the initial set of nodes making up the cluster. This node's IP must be in the list. 
    :type nodes: str

    :param attributes:  List of Name/Value pairs in JSON object format. 
    :type attributes: dict

    """
    accept_eula = data_model.property(
        "acceptEula", bool,
        array=False, optional=True,
        documentation="Indicate your acceptance of the End User License Agreement when creating this cluster. To accept the EULA, set this parameter to true.",
        dictionaryType=None
    )
    mvip = data_model.property(
        "mvip", str,
        array=False, optional=False,
        documentation="Floating (virtual) IP address for the cluster on the management network.",
        dictionaryType=None
    )
    svip = data_model.property(
        "svip", str,
        array=False, optional=False,
        documentation="Floating (virtual) IP address for the cluster on the storage (iSCSI) network.",
        dictionaryType=None
    )
    rep_count = data_model.property(
        "repCount", int,
        array=False, optional=False,
        documentation="Number of replicas of each piece of data to store in the cluster. Valid value is &quot;2&quot;.",
        dictionaryType=None
    )
    username = data_model.property(
        "username", str,
        array=False, optional=False,
        documentation="User name for the cluster admin.",
        dictionaryType=None
    )
    password = data_model.property(
        "password", str,
        array=False, optional=False,
        documentation="Initial password for the cluster admin account.",
        dictionaryType=None
    )
    nodes = data_model.property(
        "nodes", str,
        array=True, optional=False,
        documentation="CIP/SIP addresses of the initial set of nodes making up the cluster. This node&#x27;s IP must be in the list.",
        dictionaryType=None
    )
    attributes = data_model.property(
        "attributes", dict,
        array=False, optional=True,
        documentation="List of Name/Value pairs in JSON object format.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class TestLdapAuthenticationRequest(data_model.DataObject):
    """TestLdapAuthenticationRequest  

    :param username: [required] The username to be tested. 
    :type username: str

    :param password: [required] The password for the username to be tester. 
    :type password: str

    :param ldap_configuration:  An ldapConfiguration object to be tested. If this parameter is provided, the API call will test the provided configuration even if LDAP authentication is currently disabled. 
    :type ldap_configuration: LdapConfiguration

    """
    username = data_model.property(
        "username", str,
        array=False, optional=False,
        documentation="The username to be tested.",
        dictionaryType=None
    )
    password = data_model.property(
        "password", str,
        array=False, optional=False,
        documentation="The password for the username to be tester.",
        dictionaryType=None
    )
    ldap_configuration = data_model.property(
        "ldapConfiguration", LdapConfiguration,
        array=False, optional=True,
        documentation="An ldapConfiguration object to be tested. If this parameter is provided, the API call will test the provided configuration even if LDAP authentication is currently disabled.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class GetConfigResult(data_model.DataObject):
    """GetConfigResult  

    :param config: [required] The details of the cluster. Values returned in "config": cluster- Cluster information that identifies how the node communicates with the cluster it is associated with. (Object) network - Network information for bonding and Ethernet connections. (Object) 
    :type config: Config

    """
    config = data_model.property(
        "config", Config,
        array=False, optional=False,
        documentation="The details of the cluster. Values returned in &quot;config&quot;: cluster- Cluster information that identifies how the node communicates with the cluster it is associated with. (Object) network - Network information for bonding and Ethernet connections. (Object)",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ListEventsRequest(data_model.DataObject):
    """ListEventsRequest  

    :param max_events:  Specifies the maximum number of events to return. 
    :type max_events: int

    :param start_event_id:  Identifies the beginning of a range of events to return. 
    :type start_event_id: int

    :param end_event_id:  Identifies the end of a range of events to return. 
    :type end_event_id: int

    :param event_queue_type:  
    :type event_queue_type: str

    """
    max_events = data_model.property(
        "maxEvents", int,
        array=False, optional=True,
        documentation="Specifies the maximum number of events to return.",
        dictionaryType=None
    )
    start_event_id = data_model.property(
        "startEventID", int,
        array=False, optional=True,
        documentation="Identifies the beginning of a range of events to return.",
        dictionaryType=None
    )
    end_event_id = data_model.property(
        "endEventID", int,
        array=False, optional=True,
        documentation="Identifies the end of a range of events to return.",
        dictionaryType=None
    )
    event_queue_type = data_model.property(
        "eventQueueType", str,
        array=False, optional=True,
        documentation="",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class DriveConfigInfo(data_model.DataObject):
    """DriveConfigInfo  

    :param canonical_name: [required] 
    :type canonical_name: str

    :param connected: [required] 
    :type connected: bool

    :param dev: [required] 
    :type dev: int

    :param dev_path: [required] 
    :type dev_path: str

    :param drive_type: [required] 
    :type drive_type: str

    :param fs_type:  
    :type fs_type: str

    :param is_mounted:  
    :type is_mounted: bool

    :param product: [required] 
    :type product: str

    :param mount_point:  
    :type mount_point: str

    :param name: [required] 
    :type name: str

    :param path: [required] 
    :type path: str

    :param path_link: [required] 
    :type path_link: str

    :param scsi_compat_id: [required] 
    :type scsi_compat_id: str

    :param smart_ssd_write_capable:  
    :type smart_ssd_write_capable: bool

    :param security_enabled: [required] 
    :type security_enabled: bool

    :param security_frozen: [required] 
    :type security_frozen: bool

    :param security_locked: [required] 
    :type security_locked: bool

    :param security_supported: [required] 
    :type security_supported: bool

    :param size: [required] 
    :type size: int

    :param slot: [required] 
    :type slot: int

    :param uuid: [required] 
    :type uuid: UUID

    :param vendor: [required] 
    :type vendor: str

    :param version: [required] 
    :type version: str

    :param num_block_actual: [required] 
    :type num_block_actual: int

    :param num_block_expected: [required] 
    :type num_block_expected: int

    :param num_slice_actual: [required] 
    :type num_slice_actual: int

    :param num_slice_expected: [required] 
    :type num_slice_expected: int

    :param num_total_actual: [required] 
    :type num_total_actual: int

    :param num_total_expected: [required] 
    :type num_total_expected: int

    :param security_at_maximum: [required] 
    :type security_at_maximum: bool

    :param serial: [required] 
    :type serial: str

    :param scsi_state: [required] 
    :type scsi_state: str

    """
    canonical_name = data_model.property(
        "canonicalName", str,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    connected = data_model.property(
        "connected", bool,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    dev = data_model.property(
        "dev", int,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    dev_path = data_model.property(
        "devPath", str,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    drive_type = data_model.property(
        "driveType", str,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    fs_type = data_model.property(
        "fsType", str,
        array=False, optional=True,
        documentation="",
        dictionaryType=None
    )
    is_mounted = data_model.property(
        "isMounted", bool,
        array=False, optional=True,
        documentation="",
        dictionaryType=None
    )
    product = data_model.property(
        "product", str,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    mount_point = data_model.property(
        "mountPoint", str,
        array=False, optional=True,
        documentation="",
        dictionaryType=None
    )
    name = data_model.property(
        "name", str,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    path = data_model.property(
        "path", str,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    path_link = data_model.property(
        "pathLink", str,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    scsi_compat_id = data_model.property(
        "scsiCompatId", str,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    smart_ssd_write_capable = data_model.property(
        "smartSsdWriteCapable", bool,
        array=False, optional=True,
        documentation="",
        dictionaryType=None
    )
    security_enabled = data_model.property(
        "securityEnabled", bool,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    security_frozen = data_model.property(
        "securityFrozen", bool,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    security_locked = data_model.property(
        "securityLocked", bool,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    security_supported = data_model.property(
        "securitySupported", bool,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    size = data_model.property(
        "size", int,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    slot = data_model.property(
        "slot", int,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    uuid = data_model.property(
        "uuid", UUID,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    vendor = data_model.property(
        "vendor", str,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    version = data_model.property(
        "version", str,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    num_block_actual = data_model.property(
        "numBlockActual", int,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    num_block_expected = data_model.property(
        "numBlockExpected", int,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    num_slice_actual = data_model.property(
        "numSliceActual", int,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    num_slice_expected = data_model.property(
        "numSliceExpected", int,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    num_total_actual = data_model.property(
        "numTotalActual", int,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    num_total_expected = data_model.property(
        "numTotalExpected", int,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    security_at_maximum = data_model.property(
        "securityAtMaximum", bool,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    serial = data_model.property(
        "serial", str,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    scsi_state = data_model.property(
        "scsiState", str,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class DrivesConfigInfo(data_model.DataObject):
    """DrivesConfigInfo  

    :param drives: [required] 
    :type drives: DriveConfigInfo

    :param num_block_actual: [required] 
    :type num_block_actual: int

    :param num_block_expected: [required] 
    :type num_block_expected: int

    :param num_slice_actual: [required] 
    :type num_slice_actual: int

    :param num_slice_expected: [required] 
    :type num_slice_expected: int

    :param num_total_actual: [required] 
    :type num_total_actual: int

    :param num_total_expected: [required] 
    :type num_total_expected: int

    """
    drives = data_model.property(
        "drives", DriveConfigInfo,
        array=True, optional=False,
        documentation="",
        dictionaryType=None
    )
    num_block_actual = data_model.property(
        "numBlockActual", int,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    num_block_expected = data_model.property(
        "numBlockExpected", int,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    num_slice_actual = data_model.property(
        "numSliceActual", int,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    num_slice_expected = data_model.property(
        "numSliceExpected", int,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    num_total_actual = data_model.property(
        "numTotalActual", int,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    num_total_expected = data_model.property(
        "numTotalExpected", int,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class GetDriveConfigResult(data_model.DataObject):
    """GetDriveConfigResult  

    :param drive_config: [required] Configuration information for the drives that are connected to the cluster 
    :type drive_config: DrivesConfigInfo

    """
    drive_config = data_model.property(
        "driveConfig", DrivesConfigInfo,
        array=False, optional=False,
        documentation="[&#x27;Configuration information for the drives that are connected to the cluster&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class AddLdapClusterAdminResult(data_model.DataObject):
    """AddLdapClusterAdminResult  

    """

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ListProtocolEndpointsRequest(data_model.DataObject):
    """ListProtocolEndpointsRequest  

    :param protocol_endpoint_ids:  
    :type protocol_endpoint_ids: UUID

    """
    protocol_endpoint_ids = data_model.property(
        "protocolEndpointIDs", UUID,
        array=True, optional=True,
        documentation="",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ListVolumeAccessGroupsResult(data_model.DataObject):
    """ListVolumeAccessGroupsResult  

    :param volume_access_groups: [required] A list of objects describing each volume access group. 
    :type volume_access_groups: VolumeAccessGroup

    :param volume_access_groups_not_found: [required] A list of volume access groups not found by the system. Present if you used the "volumeAccessGroups" parameter and the system was unable to find one or more volume access groups that you specified. 
    :type volume_access_groups_not_found: int

    """
    volume_access_groups = data_model.property(
        "volumeAccessGroups", VolumeAccessGroup,
        array=True, optional=False,
        documentation="A list of objects describing each volume access group.",
        dictionaryType=None
    )
    volume_access_groups_not_found = data_model.property(
        "volumeAccessGroupsNotFound", int,
        array=True, optional=False,
        documentation="A list of volume access groups not found by the system. Present if you used the &quot;volumeAccessGroups&quot; parameter and the system was unable to find one or more volume access groups that you specified.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class TestLdapAuthenticationResult(data_model.DataObject):
    """TestLdapAuthenticationResult  

    :param groups: [required] List of LDAP groups that the tested user is a member of. 
    :type groups: str

    :param user_dn: [required] The tested user's full LDAP distinguished name. 
    :type user_dn: str

    """
    groups = data_model.property(
        "groups", str,
        array=True, optional=False,
        documentation="[&#x27;List of LDAP groups that the tested user is a member of.&#x27;]",
        dictionaryType=None
    )
    user_dn = data_model.property(
        "userDN", str,
        array=False, optional=False,
        documentation="[&quot;The tested user&#x27;s full LDAP distinguished name.&quot;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class Account(data_model.DataObject):
    """Account  
    The object containing information about an account.
    This object only includes "configured" information about the account, not any runtime or usage information.

    :param account_id: [required] Unique AccountID for the account. 
    :type account_id: int

    :param username: [required] User name for the account. 
    :type username: str

    :param status: [required] Current status of the account. 
    :type status: str

    :param volumes: [required] List of VolumeIDs for Volumes owned by this account. 
    :type volumes: int

    :param initiator_secret:  CHAP secret to use for the initiator. 
    :type initiator_secret: CHAPSecret

    :param target_secret:  CHAP secret to use for the target (mutual CHAP authentication). 
    :type target_secret: CHAPSecret

    :param attributes:  List of Name/Value pairs in JSON object format. 
    :type attributes: dict

    """
    account_id = data_model.property(
        "accountID", int,
        array=False, optional=False,
        documentation="Unique AccountID for the account.",
        dictionaryType=None
    )
    username = data_model.property(
        "username", str,
        array=False, optional=False,
        documentation="User name for the account.",
        dictionaryType=None
    )
    status = data_model.property(
        "status", str,
        array=False, optional=False,
        documentation="Current status of the account.",
        dictionaryType=None
    )
    volumes = data_model.property(
        "volumes", int,
        array=True, optional=False,
        documentation="List of VolumeIDs for Volumes owned by this account.",
        dictionaryType=None
    )
    initiator_secret = data_model.property(
        "initiatorSecret", CHAPSecret,
        array=False, optional=True,
        documentation="CHAP secret to use for the initiator.",
        dictionaryType=None
    )
    target_secret = data_model.property(
        "targetSecret", CHAPSecret,
        array=False, optional=True,
        documentation="CHAP secret to use for the target (mutual CHAP authentication).",
        dictionaryType=None
    )
    attributes = data_model.property(
        "attributes", dict,
        array=False, optional=True,
        documentation="List of Name/Value pairs in JSON object format.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ListAccountsResult(data_model.DataObject):
    """ListAccountsResult  

    :param accounts: [required] List of accounts. 
    :type accounts: Account

    """
    accounts = data_model.property(
        "accounts", Account,
        array=True, optional=False,
        documentation="List of accounts.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ResetDrivesRequest(data_model.DataObject):
    """ResetDrivesRequest  

    :param drives: [required] List of device names (not driveIDs) to reset. 
    :type drives: str

    :param force: [required] The "force" parameter must be included on this method to successfully reset a drive. 
    :type force: bool

    """
    drives = data_model.property(
        "drives", str,
        array=False, optional=False,
        documentation="List of device names (not driveIDs) to reset.",
        dictionaryType=None
    )
    force = data_model.property(
        "force", bool,
        array=False, optional=False,
        documentation="The &quot;force&quot; parameter must be included on this method to successfully reset a drive.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class EventInfo(data_model.DataObject):
    """EventInfo  

    :param event_id: [required] 
    :type event_id: int

    :param severity: [required] 
    :type severity: int

    :param event_info_type: [required] 
    :type event_info_type: str

    :param message: [required] 
    :type message: str

    :param service_id: [required] 
    :type service_id: int

    :param node_id: [required] 
    :type node_id: int

    :param drive_id: [required] 
    :type drive_id: int

    :param time_of_report: [required] 
    :type time_of_report: str

    :param time_of_publish: [required] 
    :type time_of_publish: str

    :param details: [required] 
    :type details: str

    """
    event_id = data_model.property(
        "eventID", int,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    severity = data_model.property(
        "severity", int,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    event_info_type = data_model.property(
        "eventInfoType", str,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    message = data_model.property(
        "message", str,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    service_id = data_model.property(
        "serviceID", int,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    node_id = data_model.property(
        "nodeID", int,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    drive_id = data_model.property(
        "driveID", int,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    time_of_report = data_model.property(
        "timeOfReport", str,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    time_of_publish = data_model.property(
        "timeOfPublish", str,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    details = data_model.property(
        "details", str,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ListEventsResult(data_model.DataObject):
    """ListEventsResult  

    :param event_queue_type: [required] 
    :type event_queue_type: str

    :param events: [required] 
    :type events: EventInfo

    """
    event_queue_type = data_model.property(
        "eventQueueType", str,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    events = data_model.property(
        "events", EventInfo,
        array=True, optional=False,
        documentation="",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ListAllNodesResult(data_model.DataObject):
    """ListAllNodesResult  

    :param nodes: [required] 
    :type nodes: Node

    :param pending_nodes: [required] 
    :type pending_nodes: PendingNode

    """
    nodes = data_model.property(
        "nodes", Node,
        array=True, optional=False,
        documentation="",
        dictionaryType=None
    )
    pending_nodes = data_model.property(
        "pendingNodes", PendingNode,
        array=True, optional=False,
        documentation="",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ListSchedulesResult(data_model.DataObject):
    """ListSchedulesResult  

    :param schedules: [required] The list of schedules currently on the cluster. 
    :type schedules: Schedule

    """
    schedules = data_model.property(
        "schedules", Schedule,
        array=True, optional=False,
        documentation="The list of schedules currently on the cluster.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ModifyBackupTargetRequest(data_model.DataObject):
    """ModifyBackupTargetRequest  

    :param backup_target_id: [required] Unique identifier assigned to the backup target. 
    :type backup_target_id: int

    :param name:  Name for the backup target. 
    :type name: str

    :param attributes:  List of Name/Value pairs in JSON object format. 
    :type attributes: dict

    """
    backup_target_id = data_model.property(
        "backupTargetID", int,
        array=False, optional=False,
        documentation="[&#x27;Unique identifier assigned to the backup target.&#x27;]",
        dictionaryType=None
    )
    name = data_model.property(
        "name", str,
        array=False, optional=True,
        documentation="[&#x27;Name for the backup target.&#x27;]",
        dictionaryType=None
    )
    attributes = data_model.property(
        "attributes", dict,
        array=False, optional=True,
        documentation="List of Name/Value pairs in JSON object format.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class SetNetworkConfigRequest(data_model.DataObject):
    """SetNetworkConfigRequest  

    :param network: [required] Objects that will be changed for the node network settings. 
    :type network: Network

    """
    network = data_model.property(
        "network", Network,
        array=False, optional=False,
        documentation="Objects that will be changed for the node network settings.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class GetSnmpInfoResult(data_model.DataObject):
    """GetSnmpInfoResult  

    :param networks: [required] List of networks and access types enabled for SNMP.  Note: "networks" will only be present if SNMP V3 is disabled. 
    :type networks: SnmpNetwork

    :param enabled: [required] If the nodes in the cluster are configured for SNMP. 
    :type enabled: bool

    :param snmp_v3_enabled: [required] If the nodes in the cluster are configured for SNMP v3. 
    :type snmp_v3_enabled: bool

    :param usm_users: [required] If SNMP v3 is enabled, the values returned is a list of user access parameters for SNMP information from the cluster. This will be returned instead of the "networks" parameter. 
    :type usm_users: SnmpV3UsmUser

    """
    networks = data_model.property(
        "networks", SnmpNetwork,
        array=True, optional=False,
        documentation="[&#x27;List of networks and access types enabled for SNMP.&#x27;, u&#x27;&#x27;, &#x27;Note: &quot;networks&quot; will only be present if SNMP V3 is disabled.&#x27;]",
        dictionaryType=None
    )
    enabled = data_model.property(
        "enabled", bool,
        array=False, optional=False,
        documentation="If the nodes in the cluster are configured for SNMP.",
        dictionaryType=None
    )
    snmp_v3_enabled = data_model.property(
        "snmpV3Enabled", bool,
        array=False, optional=False,
        documentation="If the nodes in the cluster are configured for SNMP v3.",
        dictionaryType=None
    )
    usm_users = data_model.property(
        "usmUsers", SnmpV3UsmUser,
        array=True, optional=False,
        documentation="If SNMP v3 is enabled, the values returned is a list of user access parameters for SNMP information from the cluster. This will be returned instead of the &quot;networks&quot; parameter.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ListActivePairedVolumesResult(data_model.DataObject):
    """ListActivePairedVolumesResult  

    :param volumes: [required] Volume information for the paired volumes. 
    :type volumes: Volume

    """
    volumes = data_model.property(
        "volumes", Volume,
        array=True, optional=False,
        documentation="Volume information for the paired volumes.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class StartBulkVolumeReadRequest(data_model.DataObject):
    """StartBulkVolumeReadRequest  

    :param volume_id: [required] ID of the volume to be read. 
    :type volume_id: int

    :param format: [required] The format of the volume data. Can be either: uncompressed: every byte of the volume is returned without any compression. native: opaque data is returned that is smaller and more efficiently stored and written on a subsequent bulk volume write. 
    :type format: str

    :param snapshot_id:  ID of a previously created snapshot used for bulk volume reads. If no ID is entered, a snapshot of the current active volume image is made. 
    :type snapshot_id: int

    :param script:  Executable name of a script. If no script name is given then the key and URL is necessary to access SolidFire nodes. The script is run on the primary node and the key and URL is returned to the script so the local web server can be contacted. 
    :type script: str

    :param script_parameters:  JSON parameters to pass to the script. 
    :type script_parameters: str

    :param attributes:  JSON attributes for the bulk volume job. 
    :type attributes: dict

    """
    volume_id = data_model.property(
        "volumeID", int,
        array=False, optional=False,
        documentation="ID of the volume to be read.",
        dictionaryType=None
    )
    format = data_model.property(
        "format", str,
        array=False, optional=False,
        documentation="[&#x27;The format of the volume data. Can be either:&#x27;, &#x27;uncompressed: every byte of the volume is returned without any compression.&#x27;, &#x27;native: opaque data is returned that is smaller and more efficiently stored and written on a subsequent bulk volume write.&#x27;]",
        dictionaryType=None
    )
    snapshot_id = data_model.property(
        "snapshotID", int,
        array=False, optional=True,
        documentation="[&#x27;ID of a previously created snapshot used for bulk volume reads.&#x27;, &#x27;If no ID is entered, a snapshot of the current active volume image is made.&#x27;]",
        dictionaryType=None
    )
    script = data_model.property(
        "script", str,
        array=False, optional=True,
        documentation="[&#x27;Executable name of a script.&#x27;, &#x27;If no script name is given then the key and URL is necessary to access SolidFire nodes.&#x27;, &#x27;The script is run on the primary node and the key and URL is returned to the script so the local web server can be contacted.&#x27;]",
        dictionaryType=None
    )
    script_parameters = data_model.property(
        "scriptParameters", str,
        array=False, optional=True,
        documentation="[&#x27;JSON parameters to pass to the script.&#x27;]",
        dictionaryType=None
    )
    attributes = data_model.property(
        "attributes", dict,
        array=False, optional=True,
        documentation="[&#x27;JSON attributes for the bulk volume job.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class PairedCluster(data_model.DataObject):
    """PairedCluster  

    :param cluster_name: [required] Name of the other cluster in the pair 
    :type cluster_name: str

    :param cluster_pair_id: [required] Unique ID given to each cluster in the pair. 
    :type cluster_pair_id: int

    :param cluster_pair_uuid: [required] Universally unique identifier. 
    :type cluster_pair_uuid: UUID

    :param latency: [required] Number, in milliseconds, of latency between clusters. 
    :type latency: int

    :param mvip: [required] IP of the management connection for paired clusters. 
    :type mvip: str

    :param status: [required] Can be one of the following: Connected Misconfigured Disconnected 
    :type status: str

    :param version: [required] The Element OS version of the other cluster in the pair. 
    :type version: str

    """
    cluster_name = data_model.property(
        "clusterName", str,
        array=False, optional=False,
        documentation="Name of the other cluster in the pair",
        dictionaryType=None
    )
    cluster_pair_id = data_model.property(
        "clusterPairID", int,
        array=False, optional=False,
        documentation="Unique ID given to each cluster in the pair.",
        dictionaryType=None
    )
    cluster_pair_uuid = data_model.property(
        "clusterPairUUID", UUID,
        array=False, optional=False,
        documentation="Universally unique identifier.",
        dictionaryType=None
    )
    latency = data_model.property(
        "latency", int,
        array=False, optional=False,
        documentation="Number, in milliseconds, of latency between clusters.",
        dictionaryType=None
    )
    mvip = data_model.property(
        "mvip", str,
        array=False, optional=False,
        documentation="IP of the management connection for paired clusters.",
        dictionaryType=None
    )
    status = data_model.property(
        "status", str,
        array=False, optional=False,
        documentation="[&#x27;Can be one of the following:&#x27;, &#x27;Connected&#x27;, &#x27;Misconfigured&#x27;, &#x27;Disconnected&#x27;]",
        dictionaryType=None
    )
    version = data_model.property(
        "version", str,
        array=False, optional=False,
        documentation="The Element OS version of the other cluster in the pair.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ListClusterPairsResult(data_model.DataObject):
    """ListClusterPairsResult  

    :param cluster_pairs: [required] Information about each paired cluster. 
    :type cluster_pairs: PairedCluster

    """
    cluster_pairs = data_model.property(
        "clusterPairs", PairedCluster,
        array=True, optional=False,
        documentation="Information about each paired cluster.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class AddDrivesRequest(data_model.DataObject):
    """AddDrivesRequest  

    :param drives: [required] List of drives to add to the cluster. 
    :type drives: NewDrive

    """
    drives = data_model.property(
        "drives", NewDrive,
        array=True, optional=False,
        documentation="List of drives to add to the cluster.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ClusterVersionInfo(data_model.DataObject):
    """ClusterVersionInfo  
    Version information for a node in the cluster.

    :param node_id: [required] 
    :type node_id: int

    :param node_version: [required] 
    :type node_version: str

    :param node_internal_revision: [required] 
    :type node_internal_revision: str

    """
    node_id = data_model.property(
        "nodeID", int,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    node_version = data_model.property(
        "nodeVersion", str,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    node_internal_revision = data_model.property(
        "nodeInternalRevision", str,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class SoftwareVersionInfo(data_model.DataObject):
    """SoftwareVersionInfo  

    :param current_version: [required] 
    :type current_version: str

    :param node_id: [required] 
    :type node_id: int

    :param package_name: [required] 
    :type package_name: str

    :param pending_version: [required] 
    :type pending_version: str

    :param start_time: [required] 
    :type start_time: str

    """
    current_version = data_model.property(
        "currentVersion", str,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    node_id = data_model.property(
        "nodeID", int,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    package_name = data_model.property(
        "packageName", str,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    pending_version = data_model.property(
        "pendingVersion", str,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    start_time = data_model.property(
        "startTime", str,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class GetClusterVersionInfoResult(data_model.DataObject):
    """GetClusterVersionInfoResult  

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
        documentation="",
        dictionaryType=None
    )
    cluster_version = data_model.property(
        "clusterVersion", str,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    cluster_version_info = data_model.property(
        "clusterVersionInfo", ClusterVersionInfo,
        array=True, optional=False,
        documentation="",
        dictionaryType=None
    )
    software_version_info = data_model.property(
        "softwareVersionInfo", SoftwareVersionInfo,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ModifyVolumesResult(data_model.DataObject):
    """ModifyVolumesResult  

    :param qos: [required] 
    :type qos: QoS

    :param volumes: [required] 
    :type volumes: Volume

    """
    qos = data_model.property(
        "qos", QoS,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    volumes = data_model.property(
        "volumes", Volume,
        array=True, optional=False,
        documentation="",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class DeleteVolumeRequest(data_model.DataObject):
    """DeleteVolumeRequest  

    :param volume_id: [required] The ID of the volume to delete. 
    :type volume_id: int

    """
    volume_id = data_model.property(
        "volumeID", int,
        array=False, optional=False,
        documentation="The ID of the volume to delete.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class SetSnmpACLRequest(data_model.DataObject):
    """SetSnmpACLRequest  

    :param networks: [required] List of networks and what type of access they have to the SNMP servers running on the cluster nodes. See SNMP Network Object for possible "networks" values. REQUIRED if SNMP v# is disabled. 
    :type networks: SnmpNetwork

    :param usm_users: [required] List of users and the type of access they have to the SNMP servers running on the cluster nodes. REQUIRED if SNMP v3 is enabled. 
    :type usm_users: SnmpV3UsmUser

    """
    networks = data_model.property(
        "networks", SnmpNetwork,
        array=True, optional=False,
        documentation="List of networks and what type of access they have to the SNMP servers running on the cluster nodes. See SNMP Network Object for possible &quot;networks&quot; values. REQUIRED if SNMP v# is disabled.",
        dictionaryType=None
    )
    usm_users = data_model.property(
        "usmUsers", SnmpV3UsmUser,
        array=True, optional=False,
        documentation="List of users and the type of access they have to the SNMP servers running on the cluster nodes. REQUIRED if SNMP v3 is enabled.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class SetSnmpACLResult(data_model.DataObject):
    """SetSnmpACLResult  

    """

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class CopyVolumeRequest(data_model.DataObject):
    """CopyVolumeRequest  

    :param volume_id: [required] Source volume to copy. 
    :type volume_id: int

    :param dst_volume_id: [required] Destination volume for the copy. 
    :type dst_volume_id: int

    :param snapshot_id:  Snapshot ID of the source volume to create the copy from. 
    :type snapshot_id: int

    """
    volume_id = data_model.property(
        "volumeID", int,
        array=False, optional=False,
        documentation="Source volume to copy.",
        dictionaryType=None
    )
    dst_volume_id = data_model.property(
        "dstVolumeID", int,
        array=False, optional=False,
        documentation="Destination volume for the copy.",
        dictionaryType=None
    )
    snapshot_id = data_model.property(
        "snapshotID", int,
        array=False, optional=True,
        documentation="Snapshot ID of the source volume to create the copy from.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class RemoveVolumePairRequest(data_model.DataObject):
    """RemoveVolumePairRequest  

    :param volume_id: [required] ID of the volume on which to stop the replication process. 
    :type volume_id: int

    """
    volume_id = data_model.property(
        "volumeID", int,
        array=False, optional=False,
        documentation="ID of the volume on which to stop the replication process.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class GetStorageContainerEfficiencyResult(data_model.DataObject):
    """GetStorageContainerEfficiencyResult  

    :param compression: [required] 
    :type compression: float

    :param deduplication: [required] 
    :type deduplication: float

    :param missing_volumes: [required] The volumes that could not be queried for efficiency data. Missing volumes can be caused by the Garbage Collection (GC) cycle being less than an hour old, temporary loss of network connectivity, or restarted services since the GC cycle. 
    :type missing_volumes: int

    :param thin_provisioning: [required] 
    :type thin_provisioning: float

    :param timestamp: [required] The last time efficiency data was collected after Garbage Collection (GC). 
    :type timestamp: str

    """
    compression = data_model.property(
        "compression", float,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    deduplication = data_model.property(
        "deduplication", float,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    missing_volumes = data_model.property(
        "missingVolumes", int,
        array=True, optional=False,
        documentation="The volumes that could not be queried for efficiency data. Missing volumes can be caused by the Garbage Collection (GC) cycle being less than an hour old, temporary loss of network connectivity, or restarted services since the GC cycle.",
        dictionaryType=None
    )
    thin_provisioning = data_model.property(
        "thinProvisioning", float,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    timestamp = data_model.property(
        "timestamp", str,
        array=False, optional=False,
        documentation="The last time efficiency data was collected after Garbage Collection (GC).",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class CreateScheduleResult(data_model.DataObject):
    """CreateScheduleResult  

    :param schedule_id: [required] 
    :type schedule_id: int

    """
    schedule_id = data_model.property(
        "scheduleID", int,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class SetLoginSessionInfoResult(data_model.DataObject):
    """SetLoginSessionInfoResult  

    """

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class AsyncHandleResult(data_model.DataObject):
    """AsyncHandleResult  

    :param async_handle: [required] 
    :type async_handle: int

    """
    async_handle = data_model.property(
        "asyncHandle", int,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ListVirtualVolumesRequest(data_model.DataObject):
    """ListVirtualVolumesRequest  

    :param details:  Possible values:true: Include more details about each VVOL in the response.false: Include the standard level of detail about each VVOL in the response. 
    :type details: bool

    :param limit:  The maximum number of virtual volumes to list. 
    :type limit: int

    :param recursive:  Possible values:true: Include information about the children of each VVOL in the response.false: Do not include information about the children of each VVOL in the response. 
    :type recursive: bool

    :param start_virtual_volume_id:  The ID of the virtual volume at which to begin the list. 
    :type start_virtual_volume_id: UUID

    :param virtual_volume_ids:  A list of virtual volume  IDs for which to retrieve information. If you specify this parameter, the method returns information about only these virtual volumes. 
    :type virtual_volume_ids: UUID

    """
    details = data_model.property(
        "details", bool,
        array=False, optional=True,
        documentation="Possible values:true: Include more details about each VVOL in the response.false: Include the standard level of detail about each VVOL in the response.",
        dictionaryType=None
    )
    limit = data_model.property(
        "limit", int,
        array=False, optional=True,
        documentation="The maximum number of virtual volumes to list.",
        dictionaryType=None
    )
    recursive = data_model.property(
        "recursive", bool,
        array=False, optional=True,
        documentation="Possible values:true: Include information about the children of each VVOL in the response.false: Do not include information about the children of each VVOL in the response.",
        dictionaryType=None
    )
    start_virtual_volume_id = data_model.property(
        "startVirtualVolumeID", UUID,
        array=False, optional=True,
        documentation="The ID of the virtual volume at which to begin the list.",
        dictionaryType=None
    )
    virtual_volume_ids = data_model.property(
        "virtualVolumeIDs", UUID,
        array=True, optional=True,
        documentation="A list of virtual volume  IDs for which to retrieve information. If you specify this parameter, the method returns information about only these virtual volumes.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class NetworkInterface(data_model.DataObject):
    """NetworkInterface  

    :param address: [required] IP address of the network. 
    :type address: str

    :param broadcast: [required] Address of NTP broadcast. 
    :type broadcast: str

    :param mac_address: [required] Address used to configure the interface. 
    :type mac_address: str

    :param mtu: [required] Packet size on the network interface. 
    :type mtu: int

    :param name: [required] Name of the network interface. 
    :type name: str

    :param netmask: [required] Netmask for the network interface. 
    :type netmask: str

    :param status: [required] Status of the network. 
    :type status: str

    :param type: [required] The type of network, ie, BondMaster. 
    :type type: str

    :param virtual_network_tag: [required] Virtual Network Tag if on virtual network. 
    :type virtual_network_tag: int

    """
    address = data_model.property(
        "address", str,
        array=False, optional=False,
        documentation="IP address of the network.",
        dictionaryType=None
    )
    broadcast = data_model.property(
        "broadcast", str,
        array=False, optional=False,
        documentation="Address of NTP broadcast.",
        dictionaryType=None
    )
    mac_address = data_model.property(
        "macAddress", str,
        array=False, optional=False,
        documentation="Address used to configure the interface.",
        dictionaryType=None
    )
    mtu = data_model.property(
        "mtu", int,
        array=False, optional=False,
        documentation="Packet size on the network interface.",
        dictionaryType=None
    )
    name = data_model.property(
        "name", str,
        array=False, optional=False,
        documentation="Name of the network interface.",
        dictionaryType=None
    )
    netmask = data_model.property(
        "netmask", str,
        array=False, optional=False,
        documentation="Netmask for the network interface.",
        dictionaryType=None
    )
    status = data_model.property(
        "status", str,
        array=False, optional=False,
        documentation="Status of the network.",
        dictionaryType=None
    )
    type = data_model.property(
        "type", str,
        array=False, optional=False,
        documentation="The type of network, ie, BondMaster.",
        dictionaryType=None
    )
    virtual_network_tag = data_model.property(
        "virtualNetworkTag", int,
        array=False, optional=False,
        documentation="Virtual Network Tag if on virtual network.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ListNetworkInterfacesResult(data_model.DataObject):
    """ListNetworkInterfacesResult  

    :param interfaces: [required] 
    :type interfaces: NetworkInterface

    """
    interfaces = data_model.property(
        "interfaces", NetworkInterface,
        array=True, optional=False,
        documentation="",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ListVolumeStatsByVolumeResult(data_model.DataObject):
    """ListVolumeStatsByVolumeResult  

    :param volume_stats: [required] List of account activity information. 
    :type volume_stats: VolumeStats

    """
    volume_stats = data_model.property(
        "volumeStats", VolumeStats,
        array=True, optional=False,
        documentation="[&#x27;List of account activity information.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class PurgeDeletedVolumeRequest(data_model.DataObject):
    """PurgeDeletedVolumeRequest  

    :param volume_id: [required] The ID of the volume to purge. 
    :type volume_id: int

    """
    volume_id = data_model.property(
        "volumeID", int,
        array=False, optional=False,
        documentation="The ID of the volume to purge.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class CompleteVolumePairingResult(data_model.DataObject):
    """CompleteVolumePairingResult  

    """

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class GetSystemStatusResult(data_model.DataObject):
    """GetSystemStatusResult  

    :param reboot_required: [required] 
    :type reboot_required: bool

    """
    reboot_required = data_model.property(
        "rebootRequired", bool,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class CreateStorageContainerRequest(data_model.DataObject):
    """CreateStorageContainerRequest  

    :param name: [required] Name of the storage container. 
    :type name: str

    :param initiator_secret:  The secret for CHAP authentication for the initiator 
    :type initiator_secret: str

    :param target_secret:  The secret for CHAP authentication for the target 
    :type target_secret: str

    """
    name = data_model.property(
        "name", str,
        array=False, optional=False,
        documentation="Name of the storage container.",
        dictionaryType=None
    )
    initiator_secret = data_model.property(
        "initiatorSecret", str,
        array=False, optional=True,
        documentation="The secret for CHAP authentication for the initiator",
        dictionaryType=None
    )
    target_secret = data_model.property(
        "targetSecret", str,
        array=False, optional=True,
        documentation="The secret for CHAP authentication for the target",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ListStorageContainersResult(data_model.DataObject):
    """ListStorageContainersResult  

    :param storage_containers: [required] 
    :type storage_containers: StorageContainer

    """
    storage_containers = data_model.property(
        "storageContainers", StorageContainer,
        array=True, optional=False,
        documentation="",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ModifyScheduleRequest(data_model.DataObject):
    """ModifyScheduleRequest  

    :param schedule: [required] The "Schedule" object will be used to modify an existing schedule. The ScheduleID property is required. Frequency property must be of type that inherits from Frequency. Valid types are: DaysOfMonthFrequency DaysOrWeekFrequency TimeIntervalFrequency 
    :type schedule: Schedule

    """
    schedule = data_model.property(
        "schedule", Schedule,
        array=False, optional=False,
        documentation="[&#x27;The &quot;Schedule&quot; object will be used to modify an existing schedule.&#x27;, &#x27;The ScheduleID property is required.&#x27;, &#x27;Frequency property must be of type that inherits from Frequency. Valid types are:&#x27;, &#x27;DaysOfMonthFrequency&#x27;, &#x27;DaysOrWeekFrequency&#x27;, &#x27;TimeIntervalFrequency&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class InvokeSFApiRequest(data_model.DataObject):
    """InvokeSFApiRequest  

    :param method: [required] The name of the method to invoke. This is case sensitive. 
    :type method: str

    :param parameters:  An object, normally a dictionary or hashtable of the key/value pairs, to be passed as the params for the method being invoked. 
    :type parameters: dict

    """
    method = data_model.property(
        "method", str,
        array=False, optional=False,
        documentation="The name of the method to invoke. This is case sensitive.",
        dictionaryType=None
    )
    parameters = data_model.property(
        "parameters", dict,
        array=False, optional=True,
        documentation="[&#x27;An object, normally a dictionary or hashtable of the key/value pairs, to be passed as the params for the method being invoked.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class CreateBackupTargetRequest(data_model.DataObject):
    """CreateBackupTargetRequest  

    :param name: [required] Name for the backup target. 
    :type name: str

    :param attributes:  List of Name/Value pairs in JSON object format. 
    :type attributes: dict

    """
    name = data_model.property(
        "name", str,
        array=False, optional=False,
        documentation="[&#x27;Name for the backup target.&#x27;]",
        dictionaryType=None
    )
    attributes = data_model.property(
        "attributes", dict,
        array=False, optional=True,
        documentation="List of Name/Value pairs in JSON object format.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class EnableFeatureRequest(data_model.DataObject):
    """EnableFeatureRequest  

    :param feature: [required] Valid values: vvols: Enable the Virtual Volumes (VVOLs) cluster feature. 
    :type feature: str

    """
    feature = data_model.property(
        "feature", str,
        array=False, optional=False,
        documentation="[&#x27;Valid values: vvols: Enable the Virtual Volumes (VVOLs) cluster feature.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ListVolumeStatsResult(data_model.DataObject):
    """ListVolumeStatsResult  

    :param volume_stats: [required] List of volume activity information. 
    :type volume_stats: VolumeStats

    """
    volume_stats = data_model.property(
        "volumeStats", VolumeStats,
        array=True, optional=False,
        documentation="List of volume activity information.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class SyncJob(data_model.DataObject):
    """SyncJob  

    :param bytes_per_second: [required] 
    :type bytes_per_second: float

    :param current_bytes: [required] 
    :type current_bytes: int

    :param dst_service_id: [required] 
    :type dst_service_id: int

    :param elapsed_time: [required] 
    :type elapsed_time: float

    :param percent_complete: [required] 
    :type percent_complete: float

    :param remaining_time: [required] 
    :type remaining_time: float

    :param slice_id: [required] 
    :type slice_id: int

    :param src_service_id: [required] 
    :type src_service_id: int

    :param total_bytes: [required] 
    :type total_bytes: int

    :param type: [required] 
    :type type: str

    :param clone_id: [required] 
    :type clone_id: int

    :param dst_volume_id: [required] 
    :type dst_volume_id: int

    :param node_id: [required] 
    :type node_id: int

    :param snapshot_id: [required] 
    :type snapshot_id: int

    :param src_volume_id: [required] 
    :type src_volume_id: int

    :param blocks_per_second: [required] 
    :type blocks_per_second: float

    :param stage: [required] 
    :type stage: int

    """
    bytes_per_second = data_model.property(
        "bytesPerSecond", float,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    current_bytes = data_model.property(
        "currentBytes", int,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    dst_service_id = data_model.property(
        "dstServiceID", int,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    elapsed_time = data_model.property(
        "elapsedTime", float,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    percent_complete = data_model.property(
        "percentComplete", float,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    remaining_time = data_model.property(
        "remainingTime", float,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    slice_id = data_model.property(
        "sliceID", int,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    src_service_id = data_model.property(
        "srcServiceID", int,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    total_bytes = data_model.property(
        "totalBytes", int,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    type = data_model.property(
        "type", str,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    clone_id = data_model.property(
        "cloneID", int,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    dst_volume_id = data_model.property(
        "dstVolumeID", int,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    node_id = data_model.property(
        "nodeID", int,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    snapshot_id = data_model.property(
        "snapshotID", int,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    src_volume_id = data_model.property(
        "srcVolumeID", int,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    blocks_per_second = data_model.property(
        "blocksPerSecond", float,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    stage = data_model.property(
        "stage", int,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ListSyncJobsResult(data_model.DataObject):
    """ListSyncJobsResult  

    :param sync_jobs: [required] 
    :type sync_jobs: SyncJob

    """
    sync_jobs = data_model.property(
        "syncJobs", SyncJob,
        array=True, optional=False,
        documentation="",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class BulkVolumeJob(data_model.DataObject):
    """BulkVolumeJob  

    :param bulk_volume_id: [required] The internal bulk volume job ID. 
    :type bulk_volume_id: int

    :param create_time: [required] Timestamp created for the bulk volume job. 
    :type create_time: str

    :param elapsed_time: [required] The number of seconds since the job began. 
    :type elapsed_time: int

    :param format: [required] Format is either "compressed" or "native". 
    :type format: str

    :param key: [required] The unique key created by the bulk volume session. 
    :type key: str

    :param percent_complete: [required] The completed percentage reported by the operation. 
    :type percent_complete: int

    :param remaining_time: [required] The estimated time remaining in seconds. 
    :type remaining_time: int

    :param src_volume_id: [required] The source volume ID. 
    :type src_volume_id: int

    :param status: [required] Can be one of the following: preparing active done failed 
    :type status: str

    :param script: [required] The name of the script if one is provided. 
    :type script: str

    :param snapshot_id: [required] ID of the snapshot if a snapshot is in the source of the bulk volume job. 
    :type snapshot_id: int

    :param type: [required] Can be one of the following: read write 
    :type type: str

    :param attributes: [required] JSON attributes on the bulk volume job. 
    :type attributes: dict

    """
    bulk_volume_id = data_model.property(
        "bulkVolumeID", int,
        array=False, optional=False,
        documentation="The internal bulk volume job ID.",
        dictionaryType=None
    )
    create_time = data_model.property(
        "createTime", str,
        array=False, optional=False,
        documentation="Timestamp created for the bulk volume job.",
        dictionaryType=None
    )
    elapsed_time = data_model.property(
        "elapsedTime", int,
        array=False, optional=False,
        documentation="The number of seconds since the job began.",
        dictionaryType=None
    )
    format = data_model.property(
        "format", str,
        array=False, optional=False,
        documentation="Format is either &quot;compressed&quot; or &quot;native&quot;.",
        dictionaryType=None
    )
    key = data_model.property(
        "key", str,
        array=False, optional=False,
        documentation="The unique key created by the bulk volume session.",
        dictionaryType=None
    )
    percent_complete = data_model.property(
        "percentComplete", int,
        array=False, optional=False,
        documentation="The completed percentage reported by the operation.",
        dictionaryType=None
    )
    remaining_time = data_model.property(
        "remainingTime", int,
        array=False, optional=False,
        documentation="The estimated time remaining in seconds.",
        dictionaryType=None
    )
    src_volume_id = data_model.property(
        "srcVolumeID", int,
        array=False, optional=False,
        documentation="The source volume ID.",
        dictionaryType=None
    )
    status = data_model.property(
        "status", str,
        array=False, optional=False,
        documentation="[&#x27;Can be one of the following:&#x27;, &#x27;preparing&#x27;, &#x27;active&#x27;, &#x27;done&#x27;, &#x27;failed&#x27;]",
        dictionaryType=None
    )
    script = data_model.property(
        "script", str,
        array=False, optional=False,
        documentation="The name of the script if one is provided.",
        dictionaryType=None
    )
    snapshot_id = data_model.property(
        "snapshotID", int,
        array=False, optional=False,
        documentation="ID of the snapshot if a snapshot is in the source of the bulk volume job.",
        dictionaryType=None
    )
    type = data_model.property(
        "type", str,
        array=False, optional=False,
        documentation="[&#x27;Can be one of the following:&#x27;, &#x27;read&#x27;, &#x27;write&#x27;]",
        dictionaryType=None
    )
    attributes = data_model.property(
        "attributes", dict,
        array=False, optional=False,
        documentation="JSON attributes on the bulk volume job.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ListBulkVolumeJobsResult(data_model.DataObject):
    """ListBulkVolumeJobsResult  

    :param bulk_volume_jobs: [required] An array of information for each bulk volume job. 
    :type bulk_volume_jobs: BulkVolumeJob

    """
    bulk_volume_jobs = data_model.property(
        "bulkVolumeJobs", BulkVolumeJob,
        array=True, optional=False,
        documentation="An array of information for each bulk volume job.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ModifyAccountRequest(data_model.DataObject):
    """ModifyAccountRequest  

    :param account_id: [required] AccountID for the account to modify. 
    :type account_id: int

    :param username:  Change the username of the account to this value. 
    :type username: str

    :param status:  Status of the account. 
    :type status: str

    :param initiator_secret:  CHAP secret to use for the initiator. Should be 12-16 characters long and impenetrable. 
    :type initiator_secret: CHAPSecret

    :param target_secret:  CHAP secret to use for the target (mutual CHAP authentication). Should be 12-16 characters long and impenetrable. 
    :type target_secret: CHAPSecret

    :param attributes:  List of Name/Value pairs in JSON object format. 
    :type attributes: dict

    """
    account_id = data_model.property(
        "accountID", int,
        array=False, optional=False,
        documentation="AccountID for the account to modify.",
        dictionaryType=None
    )
    username = data_model.property(
        "username", str,
        array=False, optional=True,
        documentation="Change the username of the account to this value.",
        dictionaryType=None
    )
    status = data_model.property(
        "status", str,
        array=False, optional=True,
        documentation="Status of the account.",
        dictionaryType=None
    )
    initiator_secret = data_model.property(
        "initiatorSecret", CHAPSecret,
        array=False, optional=True,
        documentation="[&#x27;CHAP secret to use for the initiator.&#x27;, &#x27;Should be 12-16 characters long and impenetrable.&#x27;]",
        dictionaryType=None
    )
    target_secret = data_model.property(
        "targetSecret", CHAPSecret,
        array=False, optional=True,
        documentation="[&#x27;CHAP secret to use for the target (mutual CHAP authentication).&#x27;, &#x27;Should be 12-16 characters long and impenetrable.&#x27;]",
        dictionaryType=None
    )
    attributes = data_model.property(
        "attributes", dict,
        array=False, optional=True,
        documentation="List of Name/Value pairs in JSON object format.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class FibreChannelPortInfo(data_model.DataObject):
    """FibreChannelPortInfo  
    Fibre Channel Node Port Info object returns information about all Fibre Channel ports on a node, or for one node in the cluster. The same information is returned for all ports or port information for one node. This information is returned with the API method ListNodeFibreChannelPortInfo (in the SolidFire API Guide).

    :param firmware: [required] The version of the firmware installed on the Fibre Channel port. 
    :type firmware: str

    :param hba_port: [required] The ID of the individual HBA port. 
    :type hba_port: int

    :param model: [required] Model of the HBA on the port. 
    :type model: str

    :param n_port_id: [required] Unique SolidFire port node ID. 
    :type n_port_id: str

    :param pci_slot: [required] Slot in which the pci card resides on the Fibre Channel node hardware. 
    :type pci_slot: int

    :param serial: [required] Serial number on the Fibre Channel port. 
    :type serial: str

    :param speed: [required] Speed of the HBA on the port. 
    :type speed: str

    :param state: [required] Possible values:  <strong>UnknownNotPresentOnlineOfflineBlockedBypassedDiagnosticsLinkdownErrorLoopbackDeleted</strong> 
    :type state: str

    :param switch_wwn: [required] The World Wide Name of the Fibre Channel switch port. 
    :type switch_wwn: str

    :param wwnn: [required] World Wide Node Name of the HBA node. 
    :type wwnn: str

    :param wwpn: [required] World Wide Port Name assigned to the physical port of the HBA. 
    :type wwpn: str

    """
    firmware = data_model.property(
        "firmware", str,
        array=False, optional=False,
        documentation="The version of the firmware installed on the Fibre Channel port.",
        dictionaryType=None
    )
    hba_port = data_model.property(
        "hbaPort", int,
        array=False, optional=False,
        documentation="The ID of the individual HBA port.",
        dictionaryType=None
    )
    model = data_model.property(
        "model", str,
        array=False, optional=False,
        documentation="Model of the HBA on the port.",
        dictionaryType=None
    )
    n_port_id = data_model.property(
        "nPortID", str,
        array=False, optional=False,
        documentation="Unique SolidFire port node ID.",
        dictionaryType=None
    )
    pci_slot = data_model.property(
        "pciSlot", int,
        array=False, optional=False,
        documentation="Slot in which the pci card resides on the Fibre Channel node hardware.",
        dictionaryType=None
    )
    serial = data_model.property(
        "serial", str,
        array=False, optional=False,
        documentation="Serial number on the Fibre Channel port.",
        dictionaryType=None
    )
    speed = data_model.property(
        "speed", str,
        array=False, optional=False,
        documentation="Speed of the HBA on the port.",
        dictionaryType=None
    )
    state = data_model.property(
        "state", str,
        array=False, optional=False,
        documentation="[&#x27;Possible values:&#x27;, u&#x27;&#x27;, &#x27;&lt;strong&gt;UnknownNotPresentOnlineOfflineBlockedBypassedDiagnosticsLinkdownErrorLoopbackDeleted&lt;/strong&gt;&#x27;]",
        dictionaryType=None
    )
    switch_wwn = data_model.property(
        "switchWwn", str,
        array=False, optional=False,
        documentation="The World Wide Name of the Fibre Channel switch port.",
        dictionaryType=None
    )
    wwnn = data_model.property(
        "wwnn", str,
        array=False, optional=False,
        documentation="World Wide Node Name of the HBA node.",
        dictionaryType=None
    )
    wwpn = data_model.property(
        "wwpn", str,
        array=False, optional=False,
        documentation="World Wide Port Name assigned to the physical port of the HBA.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class FibreChannelPortList(data_model.DataObject):
    """FibreChannelPortList  
    List of all Fibre Channel ports.

    :param fibre_channel_ports: [required] List of all physical Fibre Channel ports. 
    :type fibre_channel_ports: FibreChannelPortInfo

    """
    fibre_channel_ports = data_model.property(
        "fibreChannelPorts", FibreChannelPortInfo,
        array=True, optional=False,
        documentation="List of all physical Fibre Channel ports.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class NodeFibreChannelPortInfoResult(data_model.DataObject):
    """NodeFibreChannelPortInfoResult  
    Fibre channel port info results for a node.

    :param node_id: [required] The ID of the Fibre Channel node. 
    :type node_id: int

    :param result: [required] Contains a list of information about the Fibre Channel ports. 
    :type result: FibreChannelPortList

    """
    node_id = data_model.property(
        "nodeID", int,
        array=False, optional=False,
        documentation="The ID of the Fibre Channel node.",
        dictionaryType=None
    )
    result = data_model.property(
        "result", FibreChannelPortList,
        array=False, optional=False,
        documentation="Contains a list of information about the Fibre Channel ports.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ListNodeFibreChannelPortInfoResult(data_model.DataObject):
    """ListNodeFibreChannelPortInfoResult  
    List of fibre channel port info results grouped by node.

    :param nodes: [required] List of fibre channel port info results grouped by node. 
    :type nodes: NodeFibreChannelPortInfoResult

    """
    nodes = data_model.property(
        "nodes", NodeFibreChannelPortInfoResult,
        array=True, optional=False,
        documentation="List of fibre channel port info results grouped by node.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class CreateVolumeAccessGroupRequest(data_model.DataObject):
    """CreateVolumeAccessGroupRequest  

    :param name: [required] Name of the volume access group. It is not required to be unique, but recommended. 
    :type name: str

    :param initiators:  List of initiators to include in the volume access group. If unspecified, the access group will start out without configured initiators. 
    :type initiators: str

    :param volumes:  List of volumes to initially include in the volume access group. If unspecified, the access group will start without any volumes. 
    :type volumes: int

    :param virtual_network_id:  The ID of the SolidFire Virtual Network ID to associate the volume access group with. 
    :type virtual_network_id: int

    :param virtual_network_tags:  The ID of the VLAN Virtual Network Tag to associate the volume access group with. 
    :type virtual_network_tags: int

    :param attributes:  List of Name/Value pairs in JSON object format. 
    :type attributes: dict

    """
    name = data_model.property(
        "name", str,
        array=False, optional=False,
        documentation="[&#x27;Name of the volume access group.&#x27;, &#x27;It is not required to be unique, but recommended.&#x27;]",
        dictionaryType=None
    )
    initiators = data_model.property(
        "initiators", str,
        array=True, optional=True,
        documentation="[&#x27;List of initiators to include in the volume access group.&#x27;, &#x27;If unspecified, the access group will start out without configured initiators.&#x27;]",
        dictionaryType=None
    )
    volumes = data_model.property(
        "volumes", int,
        array=True, optional=True,
        documentation="[&#x27;List of volumes to initially include in the volume access group.&#x27;, &#x27;If unspecified, the access group will start without any volumes.&#x27;]",
        dictionaryType=None
    )
    virtual_network_id = data_model.property(
        "virtualNetworkID", int,
        array=True, optional=True,
        documentation="The ID of the SolidFire Virtual Network ID to associate the volume access group with.",
        dictionaryType=None
    )
    virtual_network_tags = data_model.property(
        "virtualNetworkTags", int,
        array=True, optional=True,
        documentation="The ID of the VLAN Virtual Network Tag to associate the volume access group with.",
        dictionaryType=None
    )
    attributes = data_model.property(
        "attributes", dict,
        array=False, optional=True,
        documentation="List of Name/Value pairs in JSON object format.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class DeleteInitiatorsRequest(data_model.DataObject):
    """DeleteInitiatorsRequest  

    :param initiators: [required] An array of IDs of initiators to delete. 
    :type initiators: int

    """
    initiators = data_model.property(
        "initiators", int,
        array=True, optional=False,
        documentation="[&#x27;An array of IDs of initiators to delete.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class TestConnectMvipRequest(data_model.DataObject):
    """TestConnectMvipRequest  

    :param mvip:  Optionally, use to test the management connection of a different MVIP. This is not needed to test the connection to the target cluster. 
    :type mvip: str

    """
    mvip = data_model.property(
        "mvip", str,
        array=False, optional=True,
        documentation="Optionally, use to test the management connection of a different MVIP. This is not needed to test the connection to the target cluster.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class CreateSnapshotRequest(data_model.DataObject):
    """CreateSnapshotRequest  

    :param volume_id: [required] ID of the volume image from which to copy. 
    :type volume_id: int

    :param snapshot_id:  Unique ID of a snapshot from which the new snapshot is made. The snapshotID passed must be a snapshot on the given volume. If a SnapshotID is not provided, a snapshot is created from the volume's active branch. 
    :type snapshot_id: int

    :param name:  A name for the snapshot. If no name is provided, the date and time the snapshot was taken is used. 
    :type name: str

    :param enable_remote_replication:  Identifies if snapshot is enabled for remote replication. 
    :type enable_remote_replication: bool

    :param retention:  The amount of time the snapshot will be retained. Enter in HH:mm:ss 
    :type retention: str

    :param attributes:  List of Name/Value pairs in JSON object format. 
    :type attributes: dict

    """
    volume_id = data_model.property(
        "volumeID", int,
        array=False, optional=False,
        documentation="ID of the volume image from which to copy.",
        dictionaryType=None
    )
    snapshot_id = data_model.property(
        "snapshotID", int,
        array=False, optional=True,
        documentation="[&#x27;Unique ID of a snapshot from which the new snapshot is made.&#x27;, &#x27;The snapshotID passed must be a snapshot on the given volume.&#x27;, &quot;If a SnapshotID is not provided, a snapshot is created from the volume&#x27;s active branch.&quot;]",
        dictionaryType=None
    )
    name = data_model.property(
        "name", str,
        array=False, optional=True,
        documentation="[&#x27;A name for the snapshot.&#x27;, &#x27;If no name is provided, the date and time the snapshot was taken is used.&#x27;]",
        dictionaryType=None
    )
    enable_remote_replication = data_model.property(
        "enableRemoteReplication", bool,
        array=False, optional=True,
        documentation="Identifies if snapshot is enabled for remote replication.",
        dictionaryType=None
    )
    retention = data_model.property(
        "retention", str,
        array=False, optional=True,
        documentation="[&#x27;The amount of time the snapshot will be retained. Enter in HH:mm:ss&#x27;]",
        dictionaryType=None
    )
    attributes = data_model.property(
        "attributes", dict,
        array=False, optional=True,
        documentation="List of Name/Value pairs in JSON object format.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ModifySnapshotResult(data_model.DataObject):
    """ModifySnapshotResult  

    """

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ResetNodeRequest(data_model.DataObject):
    """ResetNodeRequest  

    :param build: [required] Used to specify the URL to a remote Element software image to which the node will be reset. 
    :type build: str

    :param force: [required] The force parameter must be included in order to successfully reset the node. 
    :type force: bool

    :param option: [required] Used to enter specifications for running the reset operation. 
    :type option: str

    """
    build = data_model.property(
        "build", str,
        array=False, optional=False,
        documentation="Used to specify the URL to a remote Element software image to which the node will be reset.",
        dictionaryType=None
    )
    force = data_model.property(
        "force", bool,
        array=False, optional=False,
        documentation="The force parameter must be included in order to successfully reset the node.",
        dictionaryType=None
    )
    option = data_model.property(
        "option", str,
        array=False, optional=False,
        documentation="Used to enter specifications for running the reset operation.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class DeleteVolumesRequest(data_model.DataObject):
    """DeleteVolumesRequest  

    :param account_ids:  A list of account IDs. All volumes from these accounts are deleted from the system.  
    :type account_ids: int

    :param volume_access_group_ids:  A list of volume access group IDs. All of the volumes from all of the volume access groups you specify in this list are deleted from the system. 
    :type volume_access_group_ids: int

    :param volume_ids:  The list of IDs of the volumes to delete from the system. 
    :type volume_ids: int

    """
    account_ids = data_model.property(
        "accountIDs", int,
        array=True, optional=True,
        documentation="A list of account IDs. All volumes from these accounts are deleted from the system. ",
        dictionaryType=None
    )
    volume_access_group_ids = data_model.property(
        "volumeAccessGroupIDs", int,
        array=True, optional=True,
        documentation="A list of volume access group IDs. All of the volumes from all of the volume access groups you specify in this list are deleted from the system.",
        dictionaryType=None
    )
    volume_ids = data_model.property(
        "volumeIDs", int,
        array=True, optional=True,
        documentation="The list of IDs of the volumes to delete from the system.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ModifyStorageContainerRequest(data_model.DataObject):
    """ModifyStorageContainerRequest  

    :param storage_container_id: [required] 
    :type storage_container_id: UUID

    :param initiator_secret:  
    :type initiator_secret: str

    :param target_secret:  
    :type target_secret: str

    """
    storage_container_id = data_model.property(
        "storageContainerID", UUID,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    initiator_secret = data_model.property(
        "initiatorSecret", str,
        array=False, optional=True,
        documentation="",
        dictionaryType=None
    )
    target_secret = data_model.property(
        "targetSecret", str,
        array=False, optional=True,
        documentation="",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class SetLoginSessionInfoRequest(data_model.DataObject):
    """SetLoginSessionInfoRequest  

    :param timeout: [required] Cluster authentication expiration period. Formatted in HH:mm:ss. For example: 01:30:00, 00:90:00, and 00:00:5400 can all be used to equal a 90 minute timeout period. Default is 30 minutes. 
    :type timeout: str

    """
    timeout = data_model.property(
        "timeout", str,
        array=False, optional=False,
        documentation="Cluster authentication expiration period. Formatted in HH:mm:ss. For example: 01:30:00, 00:90:00, and 00:00:5400 can all be used to equal a 90 minute timeout period. Default is 30 minutes.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class CreateSnapshotResult(data_model.DataObject):
    """CreateSnapshotResult  

    :param snapshot_id: [required] ID of the newly-created snapshot. 
    :type snapshot_id: int

    :param checksum: [required] A string that represents the correct digits in the stored snapshot. This checksum can be used later to compare other snapshots to detect errors in the data. 
    :type checksum: str

    """
    snapshot_id = data_model.property(
        "snapshotID", int,
        array=False, optional=False,
        documentation="ID of the newly-created snapshot.",
        dictionaryType=None
    )
    checksum = data_model.property(
        "checksum", str,
        array=False, optional=False,
        documentation="[&#x27;A string that represents the correct digits in the stored snapshot.&#x27;, &#x27;This checksum can be used later to compare other snapshots to detect errors in the data.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class PendingActiveNode(data_model.DataObject):
    """PendingActiveNode  

    :param active_node_key: [required] 
    :type active_node_key: str

    :param assigned_node_id: [required] 
    :type assigned_node_id: int

    :param async_handle: [required] 
    :type async_handle: int

    :param cip: [required] 
    :type cip: str

    :param mip: [required] 
    :type mip: str

    :param pending_node_id: [required] 
    :type pending_node_id: int

    :param platform_info: [required] 
    :type platform_info: Platform

    :param sip: [required] 
    :type sip: str

    :param software_version: [required] 
    :type software_version: str

    """
    active_node_key = data_model.property(
        "activeNodeKey", str,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    assigned_node_id = data_model.property(
        "assignedNodeID", int,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    async_handle = data_model.property(
        "asyncHandle", int,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    cip = data_model.property(
        "cip", str,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    mip = data_model.property(
        "mip", str,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    pending_node_id = data_model.property(
        "pendingNodeID", int,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    platform_info = data_model.property(
        "platformInfo", Platform,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    sip = data_model.property(
        "sip", str,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    software_version = data_model.property(
        "softwareVersion", str,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ListPendingActiveNodesResult(data_model.DataObject):
    """ListPendingActiveNodesResult  

    :param pending_active_nodes: [required] List of objects detailing information about all PendingActive nodes in the system. 
    :type pending_active_nodes: PendingActiveNode

    """
    pending_active_nodes = data_model.property(
        "pendingActiveNodes", PendingActiveNode,
        array=True, optional=False,
        documentation="List of objects detailing information about all PendingActive nodes in the system.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class FibreChannelPortInfoResult(data_model.DataObject):
    """FibreChannelPortInfoResult  
    Used to return information about the Fibre Channel ports.

    :param result: [required] Used to return information about the Fibre Channel ports. 
    :type result: FibreChannelPortList

    """
    result = data_model.property(
        "result", FibreChannelPortList,
        array=False, optional=False,
        documentation="Used to return information about the Fibre Channel ports.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ListFibreChannelPortInfoResult(data_model.DataObject):
    """ListFibreChannelPortInfoResult  
    ListFibreChannelPortInfoResult is used to return information about the Fibre Channel ports.

    :param fibre_channel_port_info: [required] Used to return information about the Fibre Channel ports. 
    :type fibre_channel_port_info: dict

    """
    fibre_channel_port_info = data_model.property(
        "fibreChannelPortInfo", dict,
        array=False, optional=False,
        documentation="Used to return information about the Fibre Channel ports.",
        dictionaryType=FibreChannelPortInfoResult
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class CopyVolumeResult(data_model.DataObject):
    """CopyVolumeResult  

    :param clone_id: [required] 
    :type clone_id: int

    :param async_handle: [required] Handle value used to track the progress of the volume copy. 
    :type async_handle: int

    """
    clone_id = data_model.property(
        "cloneID", int,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    async_handle = data_model.property(
        "asyncHandle", int,
        array=False, optional=False,
        documentation="Handle value used to track the progress of the volume copy.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class AddNodesRequest(data_model.DataObject):
    """AddNodesRequest  

    :param pending_nodes: [required] List of PendingNodeIDs for the Nodes to be added. You can obtain the list of Pending Nodes via the ListPendingNodes method. 
    :type pending_nodes: int

    """
    pending_nodes = data_model.property(
        "pendingNodes", int,
        array=True, optional=False,
        documentation="List of PendingNodeIDs for the Nodes to be added. You can obtain the list of Pending Nodes via the ListPendingNodes method.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class RestartServicesRequest(data_model.DataObject):
    """RestartServicesRequest  

    :param force: [required] The "force" parameter must be included on this method to successfully restart services on a node.    
    :type force: bool

    :param service:  Service name to be restarted. 
    :type service: str

    :param action:  Action to perform on the service (start, stop, restart). 
    :type action: str

    """
    force = data_model.property(
        "force", bool,
        array=False, optional=False,
        documentation="The &quot;force&quot; parameter must be included on this method to successfully restart services on a node.   ",
        dictionaryType=None
    )
    service = data_model.property(
        "service", str,
        array=False, optional=True,
        documentation="Service name to be restarted.",
        dictionaryType=None
    )
    action = data_model.property(
        "action", str,
        array=False, optional=True,
        documentation="Action to perform on the service (start, stop, restart).",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class EnableLdapAuthenticationResult(data_model.DataObject):
    """EnableLdapAuthenticationResult  

    """

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ListVolumeStatsByAccountResult(data_model.DataObject):
    """ListVolumeStatsByAccountResult  

    :param volume_stats: [required] List of account activity information. Note: The volumeID member is 0 for each entry, as the values represent the summation of all volumes owned by the account. 
    :type volume_stats: VolumeStats

    """
    volume_stats = data_model.property(
        "volumeStats", VolumeStats,
        array=True, optional=False,
        documentation="[&#x27;List of account activity information.&#x27;, &#x27;Note: The volumeID member is 0 for each entry, as the values represent the summation of all volumes owned by the account.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class CreateGroupSnapshotResult(data_model.DataObject):
    """CreateGroupSnapshotResult  

    :param group_snapshot_id: [required] Unique ID of the new group snapshot. 
    :type group_snapshot_id: int

    :param members: [required] List of checksum, volumeIDs and snapshotIDs for each member of the group. 
    :type members: GroupSnapshotMembers

    """
    group_snapshot_id = data_model.property(
        "groupSnapshotID", int,
        array=False, optional=False,
        documentation="Unique ID of the new group snapshot.",
        dictionaryType=None
    )
    members = data_model.property(
        "members", GroupSnapshotMembers,
        array=True, optional=False,
        documentation="[&#x27;List of checksum, volumeIDs and snapshotIDs for each member of the group.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class RestoreDeletedVolumeResult(data_model.DataObject):
    """RestoreDeletedVolumeResult  

    """

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ClearClusterFaultsResult(data_model.DataObject):
    """ClearClusterFaultsResult  

    """

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class TestConnectSvipDetails(data_model.DataObject):
    """TestConnectSvipDetails  

    :param ping_bytes: [required] Details of the ping tests with 56 Bytes and 1500 Bytes. 
    :type ping_bytes: str

    :param svip: [required] The SVIP tested against. 
    :type svip: str

    :param connected: [required] Whether the test could connect to the MVIP. 
    :type connected: bool

    """
    ping_bytes = data_model.property(
        "pingBytes", str,
        array=False, optional=False,
        documentation="Details of the ping tests with 56 Bytes and 1500 Bytes.",
        dictionaryType=None
    )
    svip = data_model.property(
        "svip", str,
        array=False, optional=False,
        documentation="The SVIP tested against.",
        dictionaryType=None
    )
    connected = data_model.property(
        "connected", bool,
        array=False, optional=False,
        documentation="Whether the test could connect to the MVIP.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class TestConnectSvipResult(data_model.DataObject):
    """TestConnectSvipResult  

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
        documentation="Information about the test operation",
        dictionaryType=None
    )
    duration = data_model.property(
        "duration", str,
        array=False, optional=False,
        documentation="The length of time required to run the test.",
        dictionaryType=None
    )
    result = data_model.property(
        "result", str,
        array=False, optional=False,
        documentation="The results of the entire test",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ClusterCapacity(data_model.DataObject):
    """ClusterCapacity  
    High level capacity measurements for the entire cluster.

    :param active_block_space: [required] The amount of space on the block drives. This includes additional information such as metadata entries and space which can be cleaned up. 
    :type active_block_space: int

    :param active_sessions: [required] Number of active iSCSI sessions communicating with the cluster 
    :type active_sessions: int

    :param average_iops: [required] Average IPS for the cluster since midnight Coordinated Universal Time (UTC). 
    :type average_iops: int

    :param cluster_recent_iosize: [required] The average size of IOPS to all volumes in the cluster. 
    :type cluster_recent_iosize: int

    :param current_iops: [required] Average IOPS for all volumes in the cluster over the last 5 seconds. 
    :type current_iops: int

    :param max_iops: [required] Estimated maximum IOPS capability of the current cluster. 
    :type max_iops: int

    :param max_over_provisionable_space: [required] The maximum amount of provisionable space. This is a computed value. You cannot create new volumes if the current provisioned space plus the new volume size would exceed this number: maxOverProvisionableSpace = maxProvisionedSpace * GetClusterFull 
    :type max_over_provisionable_space: int

    :param max_provisioned_space: [required] The total amount of provisionable space if all volumes are 100% filled (no thin provisioned metadata). 
    :type max_provisioned_space: int

    :param max_used_metadata_space: [required] The amount of bytes on volume drives used to store metadata. 
    :type max_used_metadata_space: int

    :param max_used_space: [required] The total amount of space on all active block drives. 
    :type max_used_space: int

    :param non_zero_blocks: [required] Total number of 4KiB blocks with data after the last garbage collection operation has completed. 
    :type non_zero_blocks: int

    :param peak_active_sessions: [required] Peak number of iSCSI connections since midnight UTC. 
    :type peak_active_sessions: int

    :param peak_iops: [required] The highest value for currentIOPS since midnight UTC. 
    :type peak_iops: int

    :param provisioned_space: [required] Total amount of space provisioned in all volumes on the cluster. 
    :type provisioned_space: int

    :param snapshot_non_zero_blocks: [required] Total number of 4KiB blocks in snapshots with data. 
    :type snapshot_non_zero_blocks: int

    :param timestamp: [required] The date and time this cluster capacity sample was taken. 
    :type timestamp: str

    :param total_ops: [required] The total number of I/O operations performed throughout the lifetime of the cluster 
    :type total_ops: int

    :param unique_blocks: [required] The total number of blocks stored on the block drives. The value includes replicated blocks. 
    :type unique_blocks: int

    :param unique_blocks_used_space: [required] The total amount of data the uniqueBlocks take up on the block drives. This number is always consistent with the uniqueBlocks value. 
    :type unique_blocks_used_space: int

    :param used_metadata_space: [required] The total amount of bytes on volume drives used to store metadata 
    :type used_metadata_space: int

    :param used_metadata_space_in_snapshots: [required] The amount of bytes on volume drives used for storing unique data in snapshots. This number provides an estimate of how much metadata space would be regained by deleting all snapshots on the system. 
    :type used_metadata_space_in_snapshots: int

    :param used_space: [required] Total amount of space used by all block drives in the system. 
    :type used_space: int

    :param zero_blocks: [required] Total number of 4KiB blocks without data after the last round of garabage collection operation has completed. 
    :type zero_blocks: int

    """
    active_block_space = data_model.property(
        "activeBlockSpace", int,
        array=False, optional=False,
        documentation="[&#x27;The amount of space on the block drives.&#x27;, &#x27;This includes additional information such as metadata entries and space which can be cleaned up.&#x27;]",
        dictionaryType=None
    )
    active_sessions = data_model.property(
        "activeSessions", int,
        array=False, optional=False,
        documentation="Number of active iSCSI sessions communicating with the cluster",
        dictionaryType=None
    )
    average_iops = data_model.property(
        "averageIOPS", int,
        array=False, optional=False,
        documentation="Average IPS for the cluster since midnight Coordinated Universal Time (UTC).",
        dictionaryType=None
    )
    cluster_recent_iosize = data_model.property(
        "clusterRecentIOSize", int,
        array=False, optional=False,
        documentation="The average size of IOPS to all volumes in the cluster.",
        dictionaryType=None
    )
    current_iops = data_model.property(
        "currentIOPS", int,
        array=False, optional=False,
        documentation="Average IOPS for all volumes in the cluster over the last 5 seconds.",
        dictionaryType=None
    )
    max_iops = data_model.property(
        "maxIOPS", int,
        array=False, optional=False,
        documentation="Estimated maximum IOPS capability of the current cluster.",
        dictionaryType=None
    )
    max_over_provisionable_space = data_model.property(
        "maxOverProvisionableSpace", int,
        array=False, optional=False,
        documentation="[&#x27;The maximum amount of provisionable space.&#x27;, &#x27;This is a computed value.&#x27;, &#x27;You cannot create new volumes if the current provisioned space plus the new volume size would exceed this number:&#x27;, &#x27;maxOverProvisionableSpace = maxProvisionedSpace * GetClusterFull&#x27;]",
        dictionaryType=None
    )
    max_provisioned_space = data_model.property(
        "maxProvisionedSpace", int,
        array=False, optional=False,
        documentation="The total amount of provisionable space if all volumes are 100% filled (no thin provisioned metadata).",
        dictionaryType=None
    )
    max_used_metadata_space = data_model.property(
        "maxUsedMetadataSpace", int,
        array=False, optional=False,
        documentation="The amount of bytes on volume drives used to store metadata.",
        dictionaryType=None
    )
    max_used_space = data_model.property(
        "maxUsedSpace", int,
        array=False, optional=False,
        documentation="The total amount of space on all active block drives.",
        dictionaryType=None
    )
    non_zero_blocks = data_model.property(
        "nonZeroBlocks", int,
        array=False, optional=False,
        documentation="Total number of 4KiB blocks with data after the last garbage collection operation has completed.",
        dictionaryType=None
    )
    peak_active_sessions = data_model.property(
        "peakActiveSessions", int,
        array=False, optional=False,
        documentation="Peak number of iSCSI connections since midnight UTC.",
        dictionaryType=None
    )
    peak_iops = data_model.property(
        "peakIOPS", int,
        array=False, optional=False,
        documentation="The highest value for currentIOPS since midnight UTC.",
        dictionaryType=None
    )
    provisioned_space = data_model.property(
        "provisionedSpace", int,
        array=False, optional=False,
        documentation="Total amount of space provisioned in all volumes on the cluster.",
        dictionaryType=None
    )
    snapshot_non_zero_blocks = data_model.property(
        "snapshotNonZeroBlocks", int,
        array=False, optional=False,
        documentation="Total number of 4KiB blocks in snapshots with data.",
        dictionaryType=None
    )
    timestamp = data_model.property(
        "timestamp", str,
        array=False, optional=False,
        documentation="The date and time this cluster capacity sample was taken.",
        dictionaryType=None
    )
    total_ops = data_model.property(
        "totalOps", int,
        array=False, optional=False,
        documentation="The total number of I/O operations performed throughout the lifetime of the cluster",
        dictionaryType=None
    )
    unique_blocks = data_model.property(
        "uniqueBlocks", int,
        array=False, optional=False,
        documentation="[&#x27;The total number of blocks stored on the block drives.&#x27;, &#x27;The value includes replicated blocks.&#x27;]",
        dictionaryType=None
    )
    unique_blocks_used_space = data_model.property(
        "uniqueBlocksUsedSpace", int,
        array=False, optional=False,
        documentation="[&#x27;The total amount of data the uniqueBlocks take up on the block drives.&#x27;, &#x27;This number is always consistent with the uniqueBlocks value.&#x27;]",
        dictionaryType=None
    )
    used_metadata_space = data_model.property(
        "usedMetadataSpace", int,
        array=False, optional=False,
        documentation="The total amount of bytes on volume drives used to store metadata",
        dictionaryType=None
    )
    used_metadata_space_in_snapshots = data_model.property(
        "usedMetadataSpaceInSnapshots", int,
        array=False, optional=False,
        documentation="[&#x27;The amount of bytes on volume drives used for storing unique data in snapshots.&#x27;, &#x27;This number provides an estimate of how much metadata space would be regained by deleting all snapshots on the system.&#x27;]",
        dictionaryType=None
    )
    used_space = data_model.property(
        "usedSpace", int,
        array=False, optional=False,
        documentation="Total amount of space used by all block drives in the system.",
        dictionaryType=None
    )
    zero_blocks = data_model.property(
        "zeroBlocks", int,
        array=False, optional=False,
        documentation="Total number of 4KiB blocks without data after the last round of garabage collection operation has completed.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class GetClusterCapacityResult(data_model.DataObject):
    """GetClusterCapacityResult  

    :param cluster_capacity: [required] 
    :type cluster_capacity: ClusterCapacity

    """
    cluster_capacity = data_model.property(
        "clusterCapacity", ClusterCapacity,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class GetSnmpStateResult(data_model.DataObject):
    """GetSnmpStateResult  

    :param enabled: [required] If the nodes in the cluster are configured for SNMP. 
    :type enabled: bool

    :param snmp_v3_enabled: [required] If the node in the cluster is configured for SNMP v3. 
    :type snmp_v3_enabled: bool

    """
    enabled = data_model.property(
        "enabled", bool,
        array=False, optional=False,
        documentation="If the nodes in the cluster are configured for SNMP.",
        dictionaryType=None
    )
    snmp_v3_enabled = data_model.property(
        "snmpV3Enabled", bool,
        array=False, optional=False,
        documentation="If the node in the cluster is configured for SNMP v3.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ListActiveVolumesResult(data_model.DataObject):
    """ListActiveVolumesResult  

    :param volumes: [required] List of active volumes. 
    :type volumes: Volume

    """
    volumes = data_model.property(
        "volumes", Volume,
        array=True, optional=False,
        documentation="List of active volumes.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class GetNvramInfoResult(data_model.DataObject):
    """GetNvramInfoResult  

    :param nvram_info: [required] Arrays of events and errors detected on the NVRAM card. 
    :type nvram_info: dict

    """
    nvram_info = data_model.property(
        "nvramInfo", dict,
        array=False, optional=False,
        documentation="Arrays of events and errors detected on the NVRAM card.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class RestartNetworkingRequest(data_model.DataObject):
    """RestartNetworkingRequest  

    :param force: [required] The "force" parameter must be included on this method to successfully restart the networking. 
    :type force: bool

    """
    force = data_model.property(
        "force", bool,
        array=False, optional=False,
        documentation="The &quot;force&quot; parameter must be included on this method to successfully restart the networking.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class GetClusterMasterNodeIDResult(data_model.DataObject):
    """GetClusterMasterNodeIDResult  

    :param node_id: [required] ID of the master node. 
    :type node_id: int

    """
    node_id = data_model.property(
        "nodeID", int,
        array=False, optional=False,
        documentation="ID of the master node.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class GetNtpInfoResult(data_model.DataObject):
    """GetNtpInfoResult  

    :param broadcastclient: [required] Indicates whether or not the nodes in the cluster are listening for broadcast NTP messages. Possible values: true false 
    :type broadcastclient: bool

    :param servers: [required] List of NTP servers. 
    :type servers: str

    """
    broadcastclient = data_model.property(
        "broadcastclient", bool,
        array=False, optional=False,
        documentation="[&#x27;Indicates whether or not the nodes in the cluster are listening for broadcast NTP messages. Possible values:&#x27;, &#x27;true&#x27;, &#x27;false&#x27;]",
        dictionaryType=None
    )
    servers = data_model.property(
        "servers", str,
        array=True, optional=False,
        documentation="List of NTP servers.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ListAsyncResultsRequest(data_model.DataObject):
    """ListAsyncResultsRequest  

    :param async_result_types:  An optional list of types of results. You can use this list to restrict the results to only these types of operations. Possible values:BulkVolume: Copy operations between volumes, such as backups or restores.Clone: Volume cloning operations.DriveRemoval: Operations involving the system copying data from a drive in preparation to remove it from the cluster.RtfiPendingNode: Operations involving the system installing compatible software on a node before adding it to the cluster. 
    :type async_result_types: str

    """
    async_result_types = data_model.property(
        "asyncResultTypes", str,
        array=True, optional=True,
        documentation="An optional list of types of results. You can use this list to restrict the results to only these types of operations. Possible values:BulkVolume: Copy operations between volumes, such as backups or restores.Clone: Volume cloning operations.DriveRemoval: Operations involving the system copying data from a drive in preparation to remove it from the cluster.RtfiPendingNode: Operations involving the system installing compatible software on a node before adding it to the cluster.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ModifyAccountResult(data_model.DataObject):
    """ModifyAccountResult  

    """

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class GetAccountEfficiencyRequest(data_model.DataObject):
    """GetAccountEfficiencyRequest  

    :param account_id: [required] Specifies the volume account for which capacity is computed. 
    :type account_id: int

    """
    account_id = data_model.property(
        "accountID", int,
        array=False, optional=False,
        documentation="Specifies the volume account for which capacity is computed.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class CreateSupportBundleRequest(data_model.DataObject):
    """CreateSupportBundleRequest  

    :param bundle_name:  Unique name for each support bundle created. If no name is provided, then 'supportbundle' and the node name is used as a file name. 
    :type bundle_name: str

    :param extra_args:  This parameter is fed to the sf_make_support_bundle script. Should be used only at the request of SolidFire Support. 
    :type extra_args: str

    :param timeout_sec:  The number of seconds to let the support bundle script run before timing out and stopping. Default is 1500 seconds. 
    :type timeout_sec: int

    """
    bundle_name = data_model.property(
        "bundleName", str,
        array=False, optional=True,
        documentation="Unique name for each support bundle created. If no name is provided, then &#x27;supportbundle&#x27; and the node name is used as a file name.",
        dictionaryType=None
    )
    extra_args = data_model.property(
        "extraArgs", str,
        array=False, optional=True,
        documentation="This parameter is fed to the sf_make_support_bundle script. Should be used only at the request of SolidFire Support.",
        dictionaryType=None
    )
    timeout_sec = data_model.property(
        "timeoutSec", int,
        array=False, optional=True,
        documentation="[&#x27;The number of seconds to let the support bundle script run before timing out and stopping. Default is 1500 seconds.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ModifyInitiatorsRequest(data_model.DataObject):
    """ModifyInitiatorsRequest  

    :param initiators: [required] A list of Initiator objects containing characteristics of each initiator to modify. 
    :type initiators: ModifyInitiator

    """
    initiators = data_model.property(
        "initiators", ModifyInitiator,
        array=True, optional=False,
        documentation="[&#x27;A list of Initiator objects containing characteristics of each initiator to modify.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class GetClusterStateRequest(data_model.DataObject):
    """GetClusterStateRequest  

    :param force: [required] To run this command, the force parameter must be set to true. 
    :type force: bool

    """
    force = data_model.property(
        "force", bool,
        array=False, optional=False,
        documentation="To run this command, the force parameter must be set to true.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ListDriveHardwareRequest(data_model.DataObject):
    """ListDriveHardwareRequest  

    :param force: [required] To run this command, the force parameter must be set to true. 
    :type force: bool

    """
    force = data_model.property(
        "force", bool,
        array=False, optional=False,
        documentation="To run this command, the force parameter must be set to true.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class DriveHardware(data_model.DataObject):
    """DriveHardware  

    :param canonical_name: [required] 
    :type canonical_name: str

    :param connected: [required] 
    :type connected: bool

    :param dev: [required] 
    :type dev: int

    :param dev_path: [required] 
    :type dev_path: str

    :param drive_type: [required] 
    :type drive_type: str

    :param life_remaining_percent: [required] 
    :type life_remaining_percent: int

    :param lifetime_read_bytes: [required] 
    :type lifetime_read_bytes: int

    :param lifetime_write_bytes: [required] 
    :type lifetime_write_bytes: int

    :param name: [required] 
    :type name: str

    :param path: [required] 
    :type path: str

    :param path_link: [required] 
    :type path_link: str

    :param power_on_hours: [required] 
    :type power_on_hours: int

    :param product: [required] 
    :type product: str

    :param reallocated_sectors: [required] 
    :type reallocated_sectors: int

    :param reserve_capacity_percent: [required] 
    :type reserve_capacity_percent: int

    :param scsi_compat_id: [required] 
    :type scsi_compat_id: str

    :param scsi_state: [required] 
    :type scsi_state: str

    :param security_at_maximum: [required] 
    :type security_at_maximum: bool

    :param security_enabled: [required] 
    :type security_enabled: bool

    :param security_frozen: [required] 
    :type security_frozen: bool

    :param security_locked: [required] 
    :type security_locked: bool

    :param security_supported: [required] 
    :type security_supported: bool

    :param serial: [required] 
    :type serial: str

    :param size: [required] 
    :type size: int

    :param slot: [required] 
    :type slot: int

    :param smart_ssd_write_capable:  
    :type smart_ssd_write_capable: bool

    :param uuid: [required] 
    :type uuid: UUID

    :param vendor: [required] 
    :type vendor: str

    :param version: [required] 
    :type version: str

    """
    canonical_name = data_model.property(
        "canonicalName", str,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    connected = data_model.property(
        "connected", bool,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    dev = data_model.property(
        "dev", int,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    dev_path = data_model.property(
        "devPath", str,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    drive_type = data_model.property(
        "driveType", str,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    life_remaining_percent = data_model.property(
        "lifeRemainingPercent", int,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    lifetime_read_bytes = data_model.property(
        "lifetimeReadBytes", int,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    lifetime_write_bytes = data_model.property(
        "lifetimeWriteBytes", int,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    name = data_model.property(
        "name", str,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    path = data_model.property(
        "path", str,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    path_link = data_model.property(
        "pathLink", str,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    power_on_hours = data_model.property(
        "powerOnHours", int,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    product = data_model.property(
        "product", str,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    reallocated_sectors = data_model.property(
        "reallocatedSectors", int,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    reserve_capacity_percent = data_model.property(
        "reserveCapacityPercent", int,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    scsi_compat_id = data_model.property(
        "scsiCompatId", str,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    scsi_state = data_model.property(
        "scsiState", str,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    security_at_maximum = data_model.property(
        "securityAtMaximum", bool,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    security_enabled = data_model.property(
        "securityEnabled", bool,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    security_frozen = data_model.property(
        "securityFrozen", bool,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    security_locked = data_model.property(
        "securityLocked", bool,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    security_supported = data_model.property(
        "securitySupported", bool,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    serial = data_model.property(
        "serial", str,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    size = data_model.property(
        "size", int,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    slot = data_model.property(
        "slot", int,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    smart_ssd_write_capable = data_model.property(
        "smartSsdWriteCapable", bool,
        array=False, optional=True,
        documentation="",
        dictionaryType=None
    )
    uuid = data_model.property(
        "uuid", UUID,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    vendor = data_model.property(
        "vendor", str,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    version = data_model.property(
        "version", str,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class DrivesHardware(data_model.DataObject):
    """DrivesHardware  

    :param drive_hardware: [required] 
    :type drive_hardware: DriveHardware

    """
    drive_hardware = data_model.property(
        "driveHardware", DriveHardware,
        array=True, optional=False,
        documentation="",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class NodeDriveHardware(data_model.DataObject):
    """NodeDriveHardware  

    :param node_id: [required] 
    :type node_id: int

    :param result: [required] 
    :type result: DrivesHardware

    """
    node_id = data_model.property(
        "nodeID", int,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    result = data_model.property(
        "result", DrivesHardware,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ListDriveHardwareResult(data_model.DataObject):
    """ListDriveHardwareResult  

    :param nodes: [required] 
    :type nodes: NodeDriveHardware

    """
    nodes = data_model.property(
        "nodes", NodeDriveHardware,
        array=True, optional=False,
        documentation="",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class GetNodeHardwareInfoResult(data_model.DataObject):
    """GetNodeHardwareInfoResult  

    :param node_hardware_info: [required] Hardware information for the specified nodeID. 
    :type node_hardware_info: dict

    """
    node_hardware_info = data_model.property(
        "nodeHardwareInfo", dict,
        array=False, optional=False,
        documentation="Hardware information for the specified nodeID.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ModifyVolumeRequest(data_model.DataObject):
    """ModifyVolumeRequest  

    :param volume_id: [required] VolumeID for the volume to be modified. 
    :type volume_id: int

    :param account_id:  AccountID to which the volume is reassigned. If none is specified, the previous account name is used. 
    :type account_id: int

    :param access:  Access allowed for the volume. readOnly: Only read operations are allowed. readWrite: Reads and writes are allowed. locked: No reads or writes are allowed. replicationTarget: Identify a volume as the target volume for a paired set of volumes. If the volume is not paired, the access status is locked.  If unspecified, the access settings of the clone will be the same as the source. 
    :type access: str

    :param qos:  New quality of service settings for this volume. 
    :type qos: QoS

    :param total_size:  New size of the volume in bytes. Size is rounded up to the nearest 1MiB size. This parameter can only be used to *increase* the size of a volume. 
    :type total_size: int

    :param attributes:  List of Name/Value pairs in JSON object format. 
    :type attributes: dict

    """
    volume_id = data_model.property(
        "volumeID", int,
        array=False, optional=False,
        documentation="VolumeID for the volume to be modified.",
        dictionaryType=None
    )
    account_id = data_model.property(
        "accountID", int,
        array=False, optional=True,
        documentation="[&#x27;AccountID to which the volume is reassigned.&#x27;, &#x27;If none is specified, the previous account name is used.&#x27;]",
        dictionaryType=None
    )
    access = data_model.property(
        "access", str,
        array=False, optional=True,
        documentation="[&#x27;Access allowed for the volume.&#x27;, &#x27;readOnly: Only read operations are allowed.&#x27;, &#x27;readWrite: Reads and writes are allowed.&#x27;, &#x27;locked: No reads or writes are allowed.&#x27;, &#x27;replicationTarget: Identify a volume as the target volume for a paired set of volumes. If the volume is not paired, the access status is locked.&#x27;, u&#x27;&#x27;, &#x27;If unspecified, the access settings of the clone will be the same as the source.&#x27;]",
        dictionaryType=None
    )
    qos = data_model.property(
        "qos", QoS,
        array=False, optional=True,
        documentation="New quality of service settings for this volume.",
        dictionaryType=None
    )
    total_size = data_model.property(
        "totalSize", int,
        array=False, optional=True,
        documentation="[&#x27;New size of the volume in bytes.&#x27;, &#x27;Size is rounded up to the nearest 1MiB size.&#x27;, &#x27;This parameter can only be used to *increase* the size of a volume.&#x27;]",
        dictionaryType=None
    )
    attributes = data_model.property(
        "attributes", dict,
        array=False, optional=True,
        documentation="List of Name/Value pairs in JSON object format.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class GetDriveStatsResult(data_model.DataObject):
    """GetDriveStatsResult  

    :param drive_stats: [required] 
    :type drive_stats: DriveStats

    """
    drive_stats = data_model.property(
        "driveStats", DriveStats,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class GetIpmiInfoRequest(data_model.DataObject):
    """GetIpmiInfoRequest  

    :param force: [required] 
    :type force: bool

    """
    force = data_model.property(
        "force", bool,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class SnmpTrapRecipient(data_model.DataObject):
    """SnmpTrapRecipient  
    Host that is to receive the traps generated by the cluster.

    :param host: [required] The IP address or host name of the target network management station. 
    :type host: str

    :param community: [required] SNMP community string. 
    :type community: str

    :param port: [required] The UDP port number on the host where the trap is to be sent. Valid range is 1 - 65535. 0 (zero) is not a valid port number. Default is 162. 
    :type port: int

    """
    host = data_model.property(
        "host", str,
        array=False, optional=False,
        documentation="The IP address or host name of the target network management station.",
        dictionaryType=None
    )
    community = data_model.property(
        "community", str,
        array=False, optional=False,
        documentation="SNMP community string.",
        dictionaryType=None
    )
    port = data_model.property(
        "port", int,
        array=False, optional=False,
        documentation="The UDP port number on the host where the trap is to be sent. Valid range is 1 - 65535. 0 (zero) is not a valid port number. Default is 162.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class GetSnmpTrapInfoResult(data_model.DataObject):
    """GetSnmpTrapInfoResult  

    :param trap_recipients: [required] List of hosts that are to receive the traps generated by the cluster. 
    :type trap_recipients: SnmpTrapRecipient

    :param cluster_fault_traps_enabled: [required] If "true", when a cluster fault is logged a corresponding solidFireClusterFaultNotification is sent to the configured list of trap recipients. 
    :type cluster_fault_traps_enabled: bool

    :param cluster_fault_resolved_traps_enabled: [required] If "true", when a cluster fault is logged a corresponding solidFireClusterFaultResolvedNotification is sent to the configured list of trap recipients. 
    :type cluster_fault_resolved_traps_enabled: bool

    :param cluster_event_traps_enabled: [required] If "true", when a cluster fault is logged a corresponding solidFireClusterEventNotification is sent to the configured list of trap recipients. 
    :type cluster_event_traps_enabled: bool

    """
    trap_recipients = data_model.property(
        "trapRecipients", SnmpTrapRecipient,
        array=True, optional=False,
        documentation="List of hosts that are to receive the traps generated by the cluster.",
        dictionaryType=None
    )
    cluster_fault_traps_enabled = data_model.property(
        "clusterFaultTrapsEnabled", bool,
        array=False, optional=False,
        documentation="If &quot;true&quot;, when a cluster fault is logged a corresponding solidFireClusterFaultNotification is sent to the configured list of trap recipients.",
        dictionaryType=None
    )
    cluster_fault_resolved_traps_enabled = data_model.property(
        "clusterFaultResolvedTrapsEnabled", bool,
        array=False, optional=False,
        documentation="If &quot;true&quot;, when a cluster fault is logged a corresponding solidFireClusterFaultResolvedNotification is sent to the configured list of trap recipients.",
        dictionaryType=None
    )
    cluster_event_traps_enabled = data_model.property(
        "clusterEventTrapsEnabled", bool,
        array=False, optional=False,
        documentation="If &quot;true&quot;, when a cluster fault is logged a corresponding solidFireClusterEventNotification is sent to the configured list of trap recipients.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class CloneMultipleVolumesRequest(data_model.DataObject):
    """CloneMultipleVolumesRequest  

    :param volumes: [required] Array of Unique ID for each volume to include in the clone with optional parameters. If optional parameters are not specified, the values will be inherited from the source volumes. 
    :type volumes: CloneMultipleVolumeParams

    :param access:  New default access method for the new volumes if not overridden by information passed in the volumes array. readOnly: Only read operations are allowed. readWrite: Reads and writes are allowed. locked: No reads or writes are allowed. replicationTarget: Identify a volume as the target volume for a paired set of volumes. If the volume is not paired, the access status is locked.  If unspecified, the access settings of the clone will be the same as the source. 
    :type access: str

    :param group_snapshot_id:  ID of the group snapshot to use as a basis for the clone. 
    :type group_snapshot_id: int

    :param new_account_id:  New account ID for the volumes if not overridden by information passed in the volumes array. 
    :type new_account_id: int

    """
    volumes = data_model.property(
        "volumes", CloneMultipleVolumeParams,
        array=True, optional=False,
        documentation="Array of Unique ID for each volume to include in the clone with optional parameters. If optional parameters are not specified, the values will be inherited from the source volumes.",
        dictionaryType=None
    )
    access = data_model.property(
        "access", str,
        array=False, optional=True,
        documentation="[&#x27;New default access method for the new volumes if not overridden by information passed in the volumes array.&#x27;, &#x27;readOnly: Only read operations are allowed.&#x27;, &#x27;readWrite: Reads and writes are allowed.&#x27;, &#x27;locked: No reads or writes are allowed.&#x27;, &#x27;replicationTarget: Identify a volume as the target volume for a paired set of volumes. If the volume is not paired, the access status is locked.&#x27;, u&#x27;&#x27;, &#x27;If unspecified, the access settings of the clone will be the same as the source.&#x27;]",
        dictionaryType=None
    )
    group_snapshot_id = data_model.property(
        "groupSnapshotID", int,
        array=False, optional=True,
        documentation="ID of the group snapshot to use as a basis for the clone.",
        dictionaryType=None
    )
    new_account_id = data_model.property(
        "newAccountID", int,
        array=False, optional=True,
        documentation="New account ID for the volumes if not overridden by information passed in the volumes array.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ModifyVolumeAccessGroupLunAssignmentsResult(data_model.DataObject):
    """ModifyVolumeAccessGroupLunAssignmentsResult  

    """

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class SetRemoteLoggingHostsResult(data_model.DataObject):
    """SetRemoteLoggingHostsResult  

    """

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class GetAccountByIDRequest(data_model.DataObject):
    """GetAccountByIDRequest  

    :param account_id: [required] Specifies the account for which details are gathered. 
    :type account_id: int

    """
    account_id = data_model.property(
        "accountID", int,
        array=False, optional=False,
        documentation="Specifies the account for which details are gathered.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ListUtilitiesResult(data_model.DataObject):
    """ListUtilitiesResult  

    :param utilities: [required] List of utilities currently available to run on the node. 
    :type utilities: str

    """
    utilities = data_model.property(
        "utilities", str,
        array=True, optional=False,
        documentation="List of utilities currently available to run on the node.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ListTestsResult(data_model.DataObject):
    """ListTestsResult  

    :param tests: [required] List of tests that can be performed on the node. 
    :type tests: str

    """
    tests = data_model.property(
        "tests", str,
        array=True, optional=False,
        documentation="List of tests that can be performed on the node.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class GetVolumeEfficiencyResult(data_model.DataObject):
    """GetVolumeEfficiencyResult  

    :param compression: [required] The amount of space being saved by compressing data on a single volume. Stated as a ratio where "1" means data has been stored without being compressed. 
    :type compression: float

    :param deduplication: [required] The amount of space being saved on a single volume by not duplicating data. Stated as a ratio. 
    :type deduplication: float

    :param missing_volumes: [required] The volumes that could not be queried for efficiency data. Missing volumes can be caused by GC being less than hour old, temporary network loss or restarted services since the GC cycle. 
    :type missing_volumes: int

    :param thin_provisioning: [required] The ratio of space used to the amount of space allocated for storing data. Stated as a ratio. 
    :type thin_provisioning: float

    :param timestamp: [required] The last time efficiency data was collected after Garbage Collection (GC). 
    :type timestamp: str

    """
    compression = data_model.property(
        "compression", float,
        array=False, optional=False,
        documentation="[&#x27;The amount of space being saved by compressing data on a single volume.&#x27;, &#x27;Stated as a ratio where &quot;1&quot; means data has been stored without being compressed.&#x27;]",
        dictionaryType=None
    )
    deduplication = data_model.property(
        "deduplication", float,
        array=False, optional=False,
        documentation="[&#x27;The amount of space being saved on a single volume by not duplicating data.&#x27;, &#x27;Stated as a ratio.&#x27;]",
        dictionaryType=None
    )
    missing_volumes = data_model.property(
        "missingVolumes", int,
        array=True, optional=False,
        documentation="[&#x27;The volumes that could not be queried for efficiency data.&#x27;, &#x27;Missing volumes can be caused by GC being less than hour old, temporary network loss or restarted services since the GC cycle.&#x27;]",
        dictionaryType=None
    )
    thin_provisioning = data_model.property(
        "thinProvisioning", float,
        array=False, optional=False,
        documentation="[&#x27;The ratio of space used to the amount of space allocated for storing data.&#x27;, &#x27;Stated as a ratio.&#x27;]",
        dictionaryType=None
    )
    timestamp = data_model.property(
        "timestamp", str,
        array=False, optional=False,
        documentation="The last time efficiency data was collected after Garbage Collection (GC).",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class SetRemoteLoggingHostsRequest(data_model.DataObject):
    """SetRemoteLoggingHostsRequest  

    :param remote_hosts: [required] List of hosts to send log messages to. 
    :type remote_hosts: LoggingServer

    """
    remote_hosts = data_model.property(
        "remoteHosts", LoggingServer,
        array=True, optional=False,
        documentation="List of hosts to send log messages to.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ProtocolEndpoint(data_model.DataObject):
    """ProtocolEndpoint  

    :param protocol_endpoint_id: [required] 
    :type protocol_endpoint_id: UUID

    :param protocol_endpoint_state: [required] 
    :type protocol_endpoint_state: str

    :param provider_type: [required] 
    :type provider_type: str

    :param primary_provider_id: [required] 
    :type primary_provider_id: int

    :param secondary_provider_id: [required] 
    :type secondary_provider_id: int

    :param scsi_naadevice_id: [required] 
    :type scsi_naadevice_id: str

    """
    protocol_endpoint_id = data_model.property(
        "protocolEndpointID", UUID,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    protocol_endpoint_state = data_model.property(
        "protocolEndpointState", str,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    provider_type = data_model.property(
        "providerType", str,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    primary_provider_id = data_model.property(
        "primaryProviderID", int,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    secondary_provider_id = data_model.property(
        "secondaryProviderID", int,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    scsi_naadevice_id = data_model.property(
        "scsiNAADeviceID", str,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ListProtocolEndpointsResult(data_model.DataObject):
    """ListProtocolEndpointsResult  

    :param protocol_endpoints: [required] 
    :type protocol_endpoints: ProtocolEndpoint

    """
    protocol_endpoints = data_model.property(
        "protocolEndpoints", ProtocolEndpoint,
        array=True, optional=False,
        documentation="",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class SetClusterConfigRequest(data_model.DataObject):
    """SetClusterConfigRequest  

    :param cluster: [required] Objects that are changed for the cluster interface settings. Only the fields you want changed need to be added to this method as objects in the "cluster" parameter. 
    :type cluster: ClusterConfig

    """
    cluster = data_model.property(
        "cluster", ClusterConfig,
        array=False, optional=False,
        documentation="Objects that are changed for the cluster interface settings. Only the fields you want changed need to be added to this method as objects in the &quot;cluster&quot; parameter.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class GetNetworkConfigResult(data_model.DataObject):
    """GetNetworkConfigResult  

    :param network: [required] 
    :type network: Network

    """
    network = data_model.property(
        "network", Network,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ListDeletedVolumesResult(data_model.DataObject):
    """ListDeletedVolumesResult  

    :param volumes: [required] List of deleted volumes. 
    :type volumes: Volume

    """
    volumes = data_model.property(
        "volumes", Volume,
        array=True, optional=False,
        documentation="List of deleted volumes.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class DeleteVolumeResult(data_model.DataObject):
    """DeleteVolumeResult  

    """

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class SetSnmpTrapInfoResult(data_model.DataObject):
    """SetSnmpTrapInfoResult  

    """

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ResetDriveDetails(data_model.DataObject):
    """ResetDriveDetails  

    :param drive: [required] Drive name 
    :type drive: str

    :param return_code: [required] 
    :type return_code: int

    :param stderr: [required] 
    :type stderr: str

    :param stdout: [required] 
    :type stdout: str

    """
    drive = data_model.property(
        "drive", str,
        array=False, optional=False,
        documentation="Drive name",
        dictionaryType=None
    )
    return_code = data_model.property(
        "returnCode", int,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    stderr = data_model.property(
        "stderr", str,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    stdout = data_model.property(
        "stdout", str,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ResetDrivesDetails(data_model.DataObject):
    """ResetDrivesDetails  

    :param drives: [required] Details of a single drive that is being reset. 
    :type drives: ResetDriveDetails

    """
    drives = data_model.property(
        "drives", ResetDriveDetails,
        array=True, optional=False,
        documentation="Details of a single drive that is being reset.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ResetDrivesResult(data_model.DataObject):
    """ResetDrivesResult  

    :param details: [required] Details of drives that are being reset. 
    :type details: ResetDrivesDetails

    """
    details = data_model.property(
        "details", ResetDrivesDetails,
        array=False, optional=False,
        documentation="Details of drives that are being reset.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class TestConnectEnsembleRequest(data_model.DataObject):
    """TestConnectEnsembleRequest  

    :param ensemble:  A comma-separated list of ensemble node CIPs for connectivity testing 
    :type ensemble: str

    """
    ensemble = data_model.property(
        "ensemble", str,
        array=False, optional=True,
        documentation="A comma-separated list of ensemble node CIPs for connectivity testing",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ListVirtualVolumeHostsRequest(data_model.DataObject):
    """ListVirtualVolumeHostsRequest  

    :param virtual_volume_host_ids:  
    :type virtual_volume_host_ids: UUID

    """
    virtual_volume_host_ids = data_model.property(
        "virtualVolumeHostIDs", UUID,
        array=True, optional=True,
        documentation="",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class AsyncHandle(data_model.DataObject):
    """AsyncHandle  

    :param async_result_id: [required] The ID of the result. 
    :type async_result_id: int

    :param completed: [required] Returns true if it is completed and false if it isn't. 
    :type completed: bool

    :param create_time: [required] The time at which the asyncronous result was created 
    :type create_time: str

    :param last_update_time: [required] Time at which the result was last updated 
    :type last_update_time: str

    :param result_type: [required] The type of result. Could be Clone, DriveAdd, etc. 
    :type result_type: str

    :param success: [required] Returns whether the result was a success or failure. 
    :type success: bool

    :param data: [required] Attributes related to the result 
    :type data: dict

    """
    async_result_id = data_model.property(
        "asyncResultID", int,
        array=False, optional=False,
        documentation="The ID of the result.",
        dictionaryType=None
    )
    completed = data_model.property(
        "completed", bool,
        array=False, optional=False,
        documentation="Returns true if it is completed and false if it isn&#x27;t.",
        dictionaryType=None
    )
    create_time = data_model.property(
        "createTime", str,
        array=False, optional=False,
        documentation="The time at which the asyncronous result was created",
        dictionaryType=None
    )
    last_update_time = data_model.property(
        "lastUpdateTime", str,
        array=False, optional=False,
        documentation="Time at which the result was last updated",
        dictionaryType=None
    )
    result_type = data_model.property(
        "resultType", str,
        array=False, optional=False,
        documentation="The type of result. Could be Clone, DriveAdd, etc.",
        dictionaryType=None
    )
    success = data_model.property(
        "success", bool,
        array=False, optional=False,
        documentation="Returns whether the result was a success or failure.",
        dictionaryType=None
    )
    data = data_model.property(
        "data", dict,
        array=False, optional=False,
        documentation="Attributes related to the result",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ListAsyncResultsResult(data_model.DataObject):
    """ListAsyncResultsResult  

    :param async_handles: [required] An array of serialized asynchronous method results. 
    :type async_handles: AsyncHandle

    """
    async_handles = data_model.property(
        "asyncHandles", AsyncHandle,
        array=True, optional=False,
        documentation="An array of serialized asynchronous method results.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ListGroupSnapshotsRequest(data_model.DataObject):
    """ListGroupSnapshotsRequest  

    :param volume_id:  An array of unique volume IDs to query. If this parameter is not specified, all group snapshots on the cluster will be included. 
    :type volume_id: int

    """
    volume_id = data_model.property(
        "volumeID", int,
        array=False, optional=True,
        documentation="[&#x27;An array of unique volume IDs to query.&#x27;, &#x27;If this parameter is not specified, all group snapshots on the cluster will be included.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ModifyVolumeAccessGroupResult(data_model.DataObject):
    """ModifyVolumeAccessGroupResult  

    :param volume_access_group: [required] An object containing information about the newly modified volume access group. 
    :type volume_access_group: VolumeAccessGroup

    """
    volume_access_group = data_model.property(
        "volumeAccessGroup", VolumeAccessGroup,
        array=False, optional=False,
        documentation="An object containing information about the newly modified volume access group.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class RemoveClusterPairRequest(data_model.DataObject):
    """RemoveClusterPairRequest  

    :param cluster_pair_id: [required] Unique identifier used to pair two clusters. 
    :type cluster_pair_id: int

    """
    cluster_pair_id = data_model.property(
        "clusterPairID", int,
        array=False, optional=False,
        documentation="Unique identifier used to pair two clusters.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class GetScheduleRequest(data_model.DataObject):
    """GetScheduleRequest  

    :param schedule_id: [required] Unique ID of the schedule or multiple schedules to display 
    :type schedule_id: int

    """
    schedule_id = data_model.property(
        "scheduleID", int,
        array=False, optional=False,
        documentation="[&#x27;Unique ID of the schedule or multiple schedules to display&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class DeleteStorageContainersRequest(data_model.DataObject):
    """DeleteStorageContainersRequest  

    :param storage_container_ids: [required] list of storageContainerID of the storage container to delete. 
    :type storage_container_ids: UUID

    """
    storage_container_ids = data_model.property(
        "storageContainerIDs", UUID,
        array=True, optional=False,
        documentation="list of storageContainerID of the storage container to delete.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class RollbackToSnapshotRequest(data_model.DataObject):
    """RollbackToSnapshotRequest  

    :param volume_id: [required] VolumeID for the volume. 
    :type volume_id: int

    :param snapshot_id: [required] ID of a previously created snapshot on the given volume. 
    :type snapshot_id: int

    :param save_current_state: [required] true: The previous active volume image is kept. false: (default) The previous active volume image is deleted. 
    :type save_current_state: bool

    :param name:  Name for the snapshot. If no name is given, then the name of the snapshot being rolled back to is used with  "-copy" appended to the end of the name. 
    :type name: str

    :param attributes:  List of Name/Value pairs in JSON object format 
    :type attributes: dict

    """
    volume_id = data_model.property(
        "volumeID", int,
        array=False, optional=False,
        documentation="[&#x27;VolumeID for the volume.&#x27;]",
        dictionaryType=None
    )
    snapshot_id = data_model.property(
        "snapshotID", int,
        array=False, optional=False,
        documentation="[&#x27;ID of a previously created snapshot on the given volume.&#x27;]",
        dictionaryType=None
    )
    save_current_state = data_model.property(
        "saveCurrentState", bool,
        array=False, optional=False,
        documentation="[&#x27;true: The previous active volume image is kept.&#x27;, &#x27;false: (default) The previous active volume image is deleted.&#x27;]",
        dictionaryType=None
    )
    name = data_model.property(
        "name", str,
        array=False, optional=True,
        documentation="[&#x27;Name for the snapshot. If no name is given, then the name of the snapshot being rolled back to is used with &#x27;, &#x27;&quot;-copy&quot; appended to the end of the name.&#x27;]",
        dictionaryType=None
    )
    attributes = data_model.property(
        "attributes", dict,
        array=False, optional=True,
        documentation="[&#x27;List of Name/Value pairs in JSON object format&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class GetVolumeStatsResult(data_model.DataObject):
    """GetVolumeStatsResult  

    :param volume_stats: [required] Volume activity information. 
    :type volume_stats: VolumeStats

    """
    volume_stats = data_model.property(
        "volumeStats", VolumeStats,
        array=False, optional=False,
        documentation="Volume activity information.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class EnableSnmpResult(data_model.DataObject):
    """EnableSnmpResult  

    """

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class StartClusterPairingResult(data_model.DataObject):
    """StartClusterPairingResult  

    :param cluster_pairing_key: [required] A string of characters that is used by the "CompleteClusterPairing" API method. 
    :type cluster_pairing_key: str

    :param cluster_pair_id: [required] Unique identifier for the cluster pair. 
    :type cluster_pair_id: int

    """
    cluster_pairing_key = data_model.property(
        "clusterPairingKey", str,
        array=False, optional=False,
        documentation="A string of characters that is used by the &quot;CompleteClusterPairing&quot; API method.",
        dictionaryType=None
    )
    cluster_pair_id = data_model.property(
        "clusterPairID", int,
        array=False, optional=False,
        documentation="Unique identifier for the cluster pair.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ModifyClusterFullThresholdRequest(data_model.DataObject):
    """ModifyClusterFullThresholdRequest  

    :param stage2_aware_threshold:  Number of nodes worth of capacity remaining on the cluster that triggers a notification. 
    :type stage2_aware_threshold: int

    :param stage3_block_threshold_percent:  Percent below "Error" state to raise a cluster "Warning" alert. 
    :type stage3_block_threshold_percent: int

    :param max_metadata_over_provision_factor:  A value representative of the number of times metadata space can be over provisioned relative to the amount of space available. For example, if there was enough metadata space to store 100 TiB of volumes and this number was set to 5, then 500 TiB worth of volumes could be created. 
    :type max_metadata_over_provision_factor: int

    """
    stage2_aware_threshold = data_model.property(
        "stage2AwareThreshold", int,
        array=False, optional=True,
        documentation="Number of nodes worth of capacity remaining on the cluster that triggers a notification.",
        dictionaryType=None
    )
    stage3_block_threshold_percent = data_model.property(
        "stage3BlockThresholdPercent", int,
        array=False, optional=True,
        documentation="Percent below &quot;Error&quot; state to raise a cluster &quot;Warning&quot; alert.",
        dictionaryType=None
    )
    max_metadata_over_provision_factor = data_model.property(
        "maxMetadataOverProvisionFactor", int,
        array=False, optional=True,
        documentation="A value representative of the number of times metadata space can be over provisioned relative to the amount of space available. For example, if there was enough metadata space to store 100 TiB of volumes and this number was set to 5, then 500 TiB worth of volumes could be created.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class AddClusterAdminRequest(data_model.DataObject):
    """AddClusterAdminRequest  

    :param username: [required] Unique username for this Cluster Admin. 
    :type username: str

    :param password: [required] Password used to authenticate this Cluster Admin. 
    :type password: str

    :param access: [required] Controls which methods this Cluster Admin can use. For more details on the levels of access, see "Access Control" in the Element API Guide. 
    :type access: str

    :param accept_eula:  Indicate your acceptance of the End User License Agreement when creating this cluster admin. To accept the EULA, set this parameter to true. 
    :type accept_eula: bool

    :param attributes:  List of Name/Value pairs in JSON object format. 
    :type attributes: dict

    """
    username = data_model.property(
        "username", str,
        array=False, optional=False,
        documentation="Unique username for this Cluster Admin.",
        dictionaryType=None
    )
    password = data_model.property(
        "password", str,
        array=False, optional=False,
        documentation="Password used to authenticate this Cluster Admin.",
        dictionaryType=None
    )
    access = data_model.property(
        "access", str,
        array=True, optional=False,
        documentation="Controls which methods this Cluster Admin can use. For more details on the levels of access, see &quot;Access Control&quot; in the Element API Guide.",
        dictionaryType=None
    )
    accept_eula = data_model.property(
        "acceptEula", bool,
        array=False, optional=True,
        documentation="Indicate your acceptance of the End User License Agreement when creating this cluster admin. To accept the EULA, set this parameter to true.",
        dictionaryType=None
    )
    attributes = data_model.property(
        "attributes", dict,
        array=False, optional=True,
        documentation="List of Name/Value pairs in JSON object format.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class EnableFeatureResult(data_model.DataObject):
    """EnableFeatureResult  

    """

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class RestoreDeletedVolumeRequest(data_model.DataObject):
    """RestoreDeletedVolumeRequest  

    :param volume_id: [required] VolumeID for the deleted volume to restore. 
    :type volume_id: int

    """
    volume_id = data_model.property(
        "volumeID", int,
        array=False, optional=False,
        documentation="VolumeID for the deleted volume to restore.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class VirtualVolumeTask(data_model.DataObject):
    """VirtualVolumeTask  

    :param virtual_volume_task_id: [required] 
    :type virtual_volume_task_id: UUID

    :param virtualvolume_id: [required] 
    :type virtualvolume_id: UUID

    :param clone_virtual_volume_id: [required] 
    :type clone_virtual_volume_id: UUID

    :param status: [required] 
    :type status: str

    :param operation: [required] 
    :type operation: str

    :param virtual_volume_host_id: [required] 
    :type virtual_volume_host_id: UUID

    :param parent_metadata: [required] 
    :type parent_metadata: dict

    :param parent_total_size: [required] 
    :type parent_total_size: int

    :param parent_used_size: [required] 
    :type parent_used_size: int

    :param cancelled: [required] 
    :type cancelled: bool

    """
    virtual_volume_task_id = data_model.property(
        "virtualVolumeTaskID", UUID,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    virtualvolume_id = data_model.property(
        "virtualvolumeID", UUID,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    clone_virtual_volume_id = data_model.property(
        "cloneVirtualVolumeID", UUID,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    status = data_model.property(
        "status", str,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    operation = data_model.property(
        "operation", str,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    virtual_volume_host_id = data_model.property(
        "virtualVolumeHostID", UUID,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    parent_metadata = data_model.property(
        "parentMetadata", dict,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    parent_total_size = data_model.property(
        "parentTotalSize", int,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    parent_used_size = data_model.property(
        "parentUsedSize", int,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    cancelled = data_model.property(
        "cancelled", bool,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ListVirtualVolumeTasksResult(data_model.DataObject):
    """ListVirtualVolumeTasksResult  

    :param tasks: [required] List of VVol Async Tasks. 
    :type tasks: VirtualVolumeTask

    """
    tasks = data_model.property(
        "tasks", VirtualVolumeTask,
        array=True, optional=False,
        documentation="List of VVol Async Tasks.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class RemoveBackupTargetResult(data_model.DataObject):
    """RemoveBackupTargetResult  

    """

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class AddClusterAdminResult(data_model.DataObject):
    """AddClusterAdminResult  

    :param cluster_admin_id: [required] ClusterAdminID for the newly created Cluster Admin. 
    :type cluster_admin_id: int

    """
    cluster_admin_id = data_model.property(
        "clusterAdminID", int,
        array=False, optional=False,
        documentation="ClusterAdminID for the newly created Cluster Admin.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class GetHardwareConfigResult(data_model.DataObject):
    """GetHardwareConfigResult  

    :param hardware_config: [required] List of hardware information and current settings. 
    :type hardware_config: dict

    """
    hardware_config = data_model.property(
        "hardwareConfig", dict,
        array=False, optional=False,
        documentation="List of hardware information and current settings.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ListVirtualVolumesResult(data_model.DataObject):
    """ListVirtualVolumesResult  

    :param virtual_volumes: [required] 
    :type virtual_volumes: VirtualVolumeInfo

    :param next_virtual_volume_id: [required] 
    :type next_virtual_volume_id: UUID

    """
    virtual_volumes = data_model.property(
        "virtualVolumes", VirtualVolumeInfo,
        array=True, optional=False,
        documentation="",
        dictionaryType=None
    )
    next_virtual_volume_id = data_model.property(
        "nextVirtualVolumeID", UUID,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class CloneVolumeRequest(data_model.DataObject):
    """CloneVolumeRequest  

    :param volume_id: [required] The ID of the volume to clone. 
    :type volume_id: int

    :param name: [required] The name for the newly-created volume. 
    :type name: str

    :param new_account_id:  AccountID for the owner of the new volume. If unspecified, the AccountID of the owner of the volume being cloned is used. 
    :type new_account_id: int

    :param new_size:  New size of the volume, in bytes. May be greater or less than the size of the volume being cloned. If unspecified, the clone's volume size will be the same as the source volume. Size is rounded up to the nearest 1 MiB. 
    :type new_size: int

    :param access:  Access settings for the new volume. readOnly: Only read operations are allowed. readWrite: Reads and writes are allowed. locked: No reads or writes are allowed. replicationTarget: Identify a volume as the target volume for a paired set of volumes. If the volume is not paired, the access status is locked.  If unspecified, the access settings of the clone will be the same as the source. 
    :type access: str

    :param snapshot_id:  ID of the snapshot to use as the source of the clone. If unspecified, the clone will be created with a snapshot of the active volume. 
    :type snapshot_id: int

    :param attributes:  List of Name/Value pairs in JSON object format. 
    :type attributes: dict

    """
    volume_id = data_model.property(
        "volumeID", int,
        array=False, optional=False,
        documentation="The ID of the volume to clone.",
        dictionaryType=None
    )
    name = data_model.property(
        "name", str,
        array=False, optional=False,
        documentation="The name for the newly-created volume.",
        dictionaryType=None
    )
    new_account_id = data_model.property(
        "newAccountID", int,
        array=False, optional=True,
        documentation="[&#x27;AccountID for the owner of the new volume.&#x27;, &#x27;If unspecified, the AccountID of the owner of the volume being cloned is used.&#x27;]",
        dictionaryType=None
    )
    new_size = data_model.property(
        "newSize", int,
        array=False, optional=True,
        documentation="[&#x27;New size of the volume, in bytes.&#x27;, &#x27;May be greater or less than the size of the volume being cloned.&#x27;, &quot;If unspecified, the clone&#x27;s volume size will be the same as the source volume.&quot;, &#x27;Size is rounded up to the nearest 1 MiB.&#x27;]",
        dictionaryType=None
    )
    access = data_model.property(
        "access", str,
        array=False, optional=True,
        documentation="[&#x27;Access settings for the new volume.&#x27;, &#x27;readOnly: Only read operations are allowed.&#x27;, &#x27;readWrite: Reads and writes are allowed.&#x27;, &#x27;locked: No reads or writes are allowed.&#x27;, &#x27;replicationTarget: Identify a volume as the target volume for a paired set of volumes. If the volume is not paired, the access status is locked.&#x27;, u&#x27;&#x27;, &#x27;If unspecified, the access settings of the clone will be the same as the source.&#x27;]",
        dictionaryType=None
    )
    snapshot_id = data_model.property(
        "snapshotID", int,
        array=False, optional=True,
        documentation="[&#x27;ID of the snapshot to use as the source of the clone.&#x27;, &#x27;If unspecified, the clone will be created with a snapshot of the active volume.&#x27;]",
        dictionaryType=None
    )
    attributes = data_model.property(
        "attributes", dict,
        array=False, optional=True,
        documentation="List of Name/Value pairs in JSON object format.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class CompleteClusterPairingRequest(data_model.DataObject):
    """CompleteClusterPairingRequest  

    :param cluster_pairing_key: [required] A string of characters that is returned from the "StartClusterPairing" API method. 
    :type cluster_pairing_key: str

    """
    cluster_pairing_key = data_model.property(
        "clusterPairingKey", str,
        array=False, optional=False,
        documentation="A string of characters that is returned from the &quot;StartClusterPairing&quot; API method.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ResetNodeResult(data_model.DataObject):
    """ResetNodeResult  

    :param rtfi_info: [required] Details of nodes that are being reset. 
    :type rtfi_info: dict

    """
    rtfi_info = data_model.property(
        "rtfiInfo", dict,
        array=False, optional=False,
        documentation="Details of nodes that are being reset.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class DriveHardwareInfo(data_model.DataObject):
    """DriveHardwareInfo  

    :param description: [required] 
    :type description: str

    :param dev: [required] 
    :type dev: str

    :param devpath: [required] 
    :type devpath: str

    :param drive_security_at_maximum: [required] 
    :type drive_security_at_maximum: bool

    :param drive_security_frozen: [required] 
    :type drive_security_frozen: bool

    :param drive_security_locked: [required] 
    :type drive_security_locked: bool

    :param logicalname: [required] 
    :type logicalname: str

    :param product: [required] 
    :type product: str

    :param scsi_compat_id: [required] 
    :type scsi_compat_id: str

    :param security_feature_enabled: [required] 
    :type security_feature_enabled: bool

    :param security_feature_supported: [required] 
    :type security_feature_supported: bool

    :param serial: [required] 
    :type serial: str

    :param size: [required] 
    :type size: int

    :param uuid: [required] 
    :type uuid: UUID

    :param version: [required] 
    :type version: str

    """
    description = data_model.property(
        "description", str,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    dev = data_model.property(
        "dev", str,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    devpath = data_model.property(
        "devpath", str,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    drive_security_at_maximum = data_model.property(
        "driveSecurityAtMaximum", bool,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    drive_security_frozen = data_model.property(
        "driveSecurityFrozen", bool,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    drive_security_locked = data_model.property(
        "driveSecurityLocked", bool,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    logicalname = data_model.property(
        "logicalname", str,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    product = data_model.property(
        "product", str,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    scsi_compat_id = data_model.property(
        "scsiCompatID", str,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    security_feature_enabled = data_model.property(
        "securityFeatureEnabled", bool,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    security_feature_supported = data_model.property(
        "securityFeatureSupported", bool,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    serial = data_model.property(
        "serial", str,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    size = data_model.property(
        "size", int,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    uuid = data_model.property(
        "uuid", UUID,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    version = data_model.property(
        "version", str,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class GetDriveHardwareInfoResult(data_model.DataObject):
    """GetDriveHardwareInfoResult  

    :param drive_hardware_info: [required] 
    :type drive_hardware_info: DriveHardwareInfo

    """
    drive_hardware_info = data_model.property(
        "driveHardwareInfo", DriveHardwareInfo,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class EnableLdapAuthenticationRequest(data_model.DataObject):
    """EnableLdapAuthenticationRequest  

    :param auth_type:  Identifies which user authentcation method will be used.  Must be one of the following: DirectBind SearchAndBind (default) 
    :type auth_type: str

    :param group_search_base_dn:  The base DN of the tree to start the group search (will do a subtree search from here). 
    :type group_search_base_dn: str

    :param group_search_custom_filter:  REQUIRED for CustomFilter For use with the CustomFilter search type, an LDAP filter to use to return the DNs of a user's groups. The string can have placeholder text of %USERNAME% and %USERDN% to be replaced with their username and full userDN as needed. 
    :type group_search_custom_filter: str

    :param group_search_type:  Controls the default group search filter used, can be one of the following: NoGroups: No group support. ActiveDirectory: (default) Nested membership of all of a user's AD groups. MemberDN: MemberDN style groups (single-level). 
    :type group_search_type: str

    :param search_bind_dn:  REQUIRED for SearchAndBind A fully qualified DN to log in with to perform an LDAP search for the user (needs read access to the LDAP directory). 
    :type search_bind_dn: str

    :param search_bind_password:  REQUIRED for SearchAndBind The password for the searchBindDN account used for searching. 
    :type search_bind_password: str

    :param server_uris: [required] A list of LDAP server URIs (examples: "ldap://1.2.3.4" and ldaps://1.2.3.4:123") 
    :type server_uris: str

    :param user_dntemplate:  REQUIRED for DirectBind A string that is used to form a fully qualified user DN. The string should have the placeholder text "%USERNAME%" which will be replaced with the username of the authenticating user. 
    :type user_dntemplate: str

    :param user_search_base_dn:  REQUIRED for SearchAndBind The base DN of the tree used to start the search (will do a subtree search from here). 
    :type user_search_base_dn: str

    :param user_search_filter:  REQUIRED for SearchAndBind. The LDAP filter to use. The string should have the placeholder text "%USERNAME%" which will be replaced with the username of the authenticating user. Example: (&(objectClass=person) (sAMAccountName=%USERNAME%)) will use the sAMAccountName field in Active Directory to match the nusername entered at cluster login. 
    :type user_search_filter: str

    """
    auth_type = data_model.property(
        "authType", str,
        array=False, optional=True,
        documentation="[&#x27;Identifies which user authentcation method will be used. &#x27;, &#x27;Must be one of the following:&#x27;, &#x27;DirectBind&#x27;, &#x27;SearchAndBind (default)&#x27;]",
        dictionaryType=None
    )
    group_search_base_dn = data_model.property(
        "groupSearchBaseDN", str,
        array=False, optional=True,
        documentation="[&#x27;The base DN of the tree to start the group search (will do a subtree search from here).&#x27;]",
        dictionaryType=None
    )
    group_search_custom_filter = data_model.property(
        "groupSearchCustomFilter", str,
        array=False, optional=True,
        documentation="[&#x27;REQUIRED for CustomFilter&#x27;, &quot;For use with the CustomFilter search type, an LDAP filter to use to return the DNs of a user&#x27;s groups.&quot;, &#x27;The string can have placeholder text of %USERNAME% and %USERDN% to be replaced with their username and full userDN as needed.&#x27;]",
        dictionaryType=None
    )
    group_search_type = data_model.property(
        "groupSearchType", str,
        array=False, optional=True,
        documentation="[&#x27;Controls the default group search filter used, can be one of the following:&#x27;, &#x27;NoGroups: No group support.&#x27;, &quot;ActiveDirectory: (default) Nested membership of all of a user&#x27;s AD groups.&quot;, &#x27;MemberDN: MemberDN style groups (single-level).&#x27;]",
        dictionaryType=None
    )
    search_bind_dn = data_model.property(
        "searchBindDN", str,
        array=False, optional=True,
        documentation="[&#x27;REQUIRED for SearchAndBind&#x27;, &#x27;A fully qualified DN to log in with to perform an LDAP search for the user (needs read access to the LDAP directory).&#x27;]",
        dictionaryType=None
    )
    search_bind_password = data_model.property(
        "searchBindPassword", str,
        array=False, optional=True,
        documentation="[&#x27;REQUIRED for SearchAndBind&#x27;, &#x27;The password for the searchBindDN account used for searching.&#x27;]",
        dictionaryType=None
    )
    server_uris = data_model.property(
        "serverURIs", str,
        array=True, optional=False,
        documentation="[&#x27;A list of LDAP server URIs (examples: &quot;ldap://1.2.3.4&quot; and ldaps://1.2.3.4:123&quot;)&#x27;]",
        dictionaryType=None
    )
    user_dntemplate = data_model.property(
        "userDNTemplate", str,
        array=False, optional=True,
        documentation="[&#x27;REQUIRED for DirectBind&#x27;, &#x27;A string that is used to form a fully qualified user DN.&#x27;, &#x27;The string should have the placeholder text &quot;%USERNAME%&quot; which will be replaced with the username of the authenticating user.&#x27;]",
        dictionaryType=None
    )
    user_search_base_dn = data_model.property(
        "userSearchBaseDN", str,
        array=False, optional=True,
        documentation="[&#x27;REQUIRED for SearchAndBind&#x27;, &#x27;The base DN of the tree used to start the search (will do a subtree search from here).&#x27;]",
        dictionaryType=None
    )
    user_search_filter = data_model.property(
        "userSearchFilter", str,
        array=False, optional=True,
        documentation="[&#x27;REQUIRED for SearchAndBind.&#x27;, &#x27;The LDAP filter to use.&#x27;, &#x27;The string should have the placeholder text &quot;%USERNAME%&quot; which will be replaced with the username of the authenticating user.&#x27;, &#x27;Example: (&amp;(objectClass=person) (sAMAccountName=%USERNAME%)) will use the sAMAccountName field in Active Directory to match the nusername entered at cluster login.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class NodeStateInfo(data_model.DataObject):
    """NodeStateInfo  

    :param cluster: [required] Name of the cluster. 
    :type cluster: str

    :param state: [required] <strong>Available:</strong> Node has not been configured with a cluster name.<br><strong>Pending:</strong> Node is pending for a specific named cluster and can be added.<br><strong>Active:</strong> Node is active and a member of a cluster and may not be added to another cluster. 
    :type state: str

    """
    cluster = data_model.property(
        "cluster", str,
        array=False, optional=False,
        documentation="Name of the cluster.",
        dictionaryType=None
    )
    state = data_model.property(
        "state", str,
        array=False, optional=False,
        documentation="&lt;strong&gt;Available:&lt;/strong&gt; Node has not been configured with a cluster name.&lt;br&gt;&lt;strong&gt;Pending:&lt;/strong&gt; Node is pending for a specific named cluster and can be added.&lt;br&gt;&lt;strong&gt;Active:&lt;/strong&gt; Node is active and a member of a cluster and may not be added to another cluster.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class NodeStateResult(data_model.DataObject):
    """NodeStateResult  

    :param node_id: [required] ID of the node. 
    :type node_id: int

    :param result: [required] NodeStateInfo object. 
    :type result: NodeStateInfo

    """
    node_id = data_model.property(
        "nodeID", int,
        array=False, optional=False,
        documentation="ID of the node.",
        dictionaryType=None
    )
    result = data_model.property(
        "result", NodeStateInfo,
        array=False, optional=False,
        documentation="NodeStateInfo object.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class GetClusterStateResult(data_model.DataObject):
    """GetClusterStateResult  

    :param nodes: [required] Array of NodeStateResult objects for each node in the cluster. 
    :type nodes: NodeStateResult

    """
    nodes = data_model.property(
        "nodes", NodeStateResult,
        array=True, optional=False,
        documentation="Array of NodeStateResult objects for each node in the cluster.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class EnableEncryptionAtRestResult(data_model.DataObject):
    """EnableEncryptionAtRestResult  

    """

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class GetClusterConfigResult(data_model.DataObject):
    """GetClusterConfigResult  

    :param cluster: [required] Cluster configuration information the node uses to communicate with the cluster. 
    :type cluster: ClusterConfig

    """
    cluster = data_model.property(
        "cluster", ClusterConfig,
        array=False, optional=False,
        documentation="Cluster configuration information the node uses to communicate with the cluster.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class SetSnmpTrapInfoRequest(data_model.DataObject):
    """SetSnmpTrapInfoRequest  

    :param trap_recipients: [required] List of hosts that are to receive the traps generated by the Cluster Master. At least one object is required if any one of the trap types is enabled. 
    :type trap_recipients: SnmpTrapRecipient

    :param cluster_fault_traps_enabled: [required] If "true", when a cluster fault is logged a corresponding solidFireClusterFaultNotification is sent to the configured list of trap recipients. 
    :type cluster_fault_traps_enabled: bool

    :param cluster_fault_resolved_traps_enabled: [required] If "true", when a cluster fault is logged a corresponding solidFireClusterFaultResolvedNotification is sent to the configured list of trap recipients. 
    :type cluster_fault_resolved_traps_enabled: bool

    :param cluster_event_traps_enabled: [required] If "true", when a cluster fault is logged a corresponding solidFireClusterEventNotification is sent to the configured list of trap recipients. 
    :type cluster_event_traps_enabled: bool

    """
    trap_recipients = data_model.property(
        "trapRecipients", SnmpTrapRecipient,
        array=True, optional=False,
        documentation="List of hosts that are to receive the traps generated by the Cluster Master. At least one object is required if any one of the trap types is enabled.",
        dictionaryType=None
    )
    cluster_fault_traps_enabled = data_model.property(
        "clusterFaultTrapsEnabled", bool,
        array=False, optional=False,
        documentation="If &quot;true&quot;, when a cluster fault is logged a corresponding solidFireClusterFaultNotification is sent to the configured list of trap recipients.",
        dictionaryType=None
    )
    cluster_fault_resolved_traps_enabled = data_model.property(
        "clusterFaultResolvedTrapsEnabled", bool,
        array=False, optional=False,
        documentation="If &quot;true&quot;, when a cluster fault is logged a corresponding solidFireClusterFaultResolvedNotification is sent to the configured list of trap recipients.",
        dictionaryType=None
    )
    cluster_event_traps_enabled = data_model.property(
        "clusterEventTrapsEnabled", bool,
        array=False, optional=False,
        documentation="If &quot;true&quot;, when a cluster fault is logged a corresponding solidFireClusterEventNotification is sent to the configured list of trap recipients.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class GetCurrentClusterAdminResult(data_model.DataObject):
    """GetCurrentClusterAdminResult  

    :param cluster_admin: [required] Information about all cluster and LDAP administrators that exist for a cluster. 
    :type cluster_admin: ClusterAdmin

    """
    cluster_admin = data_model.property(
        "clusterAdmin", ClusterAdmin,
        array=False, optional=False,
        documentation="Information about all cluster and LDAP administrators that exist for a cluster.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ModifyBackupTargetResult(data_model.DataObject):
    """ModifyBackupTargetResult  

    """

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class VolumeAccessGroupLunAssignments(data_model.DataObject):
    """VolumeAccessGroupLunAssignments  
    VolumeAccessGroup ID and Lun to be assigned to all volumes within it.

    :param volume_access_group_id: [required] Unique volume access group ID for which the LUN assignments will be modified. 
    :type volume_access_group_id: int

    :param lun_assignments: [required] The volume IDs with assigned LUN values. 
    :type lun_assignments: LunAssignment

    :param deleted_lun_assignments: [required] The volume IDs with deleted LUN values. 
    :type deleted_lun_assignments: LunAssignment

    """
    volume_access_group_id = data_model.property(
        "volumeAccessGroupID", int,
        array=False, optional=False,
        documentation="Unique volume access group ID for which the LUN assignments will be modified.",
        dictionaryType=None
    )
    lun_assignments = data_model.property(
        "lunAssignments", LunAssignment,
        array=True, optional=False,
        documentation="The volume IDs with assigned LUN values.",
        dictionaryType=None
    )
    deleted_lun_assignments = data_model.property(
        "deletedLunAssignments", LunAssignment,
        array=True, optional=False,
        documentation="The volume IDs with deleted LUN values.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class GetVolumeAccessGroupLunAssignmentsResult(data_model.DataObject):
    """GetVolumeAccessGroupLunAssignmentsResult  

    :param volume_access_group_lun_assignments: [required] List of all physical Fibre Channel ports, or a port for a single node. 
    :type volume_access_group_lun_assignments: VolumeAccessGroupLunAssignments

    """
    volume_access_group_lun_assignments = data_model.property(
        "volumeAccessGroupLunAssignments", VolumeAccessGroupLunAssignments,
        array=False, optional=False,
        documentation="List of all physical Fibre Channel ports, or a port for a single node.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class NodeWaitingToJoin(data_model.DataObject):
    """NodeWaitingToJoin  

    :param name: [required] 
    :type name: str

    :param version: [required] 
    :type version: str

    :param node_id: [required] 
    :type node_id: int

    :param pending_node_id: [required] 
    :type pending_node_id: int

    :param mip: [required] 
    :type mip: str

    :param cip: [required] 
    :type cip: str

    :param sip: [required] 
    :type sip: str

    """
    name = data_model.property(
        "name", str,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    version = data_model.property(
        "version", str,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    node_id = data_model.property(
        "nodeID", int,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    pending_node_id = data_model.property(
        "pendingNodeID", int,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    mip = data_model.property(
        "mip", str,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    cip = data_model.property(
        "cip", str,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    sip = data_model.property(
        "sip", str,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class GetBootstrapConfigResult(data_model.DataObject):
    """GetBootstrapConfigResult  

    :param cluster_name: [required] Name of the cluster. 
    :type cluster_name: str

    :param node_name: [required] Name of the node. 
    :type node_name: str

    :param nodes: [required] List of descriptions for each node that is actively waiting to join this cluster: compatible - Indicates if the listed node is compatible with the node the API call was executed against. name - IP address of each node. version - version of SolidFire Element software currently installed on the node. 
    :type nodes: NodeWaitingToJoin

    :param version: [required] Version of the SolidFire Element software currently installed. 
    :type version: str

    """
    cluster_name = data_model.property(
        "clusterName", str,
        array=False, optional=False,
        documentation="Name of the cluster.",
        dictionaryType=None
    )
    node_name = data_model.property(
        "nodeName", str,
        array=False, optional=False,
        documentation="Name of the node.",
        dictionaryType=None
    )
    nodes = data_model.property(
        "nodes", NodeWaitingToJoin,
        array=True, optional=False,
        documentation="List of descriptions for each node that is actively waiting to join this cluster: compatible - Indicates if the listed node is compatible with the node the API call was executed against. name - IP address of each node. version - version of SolidFire Element software currently installed on the node.",
        dictionaryType=None
    )
    version = data_model.property(
        "version", str,
        array=False, optional=False,
        documentation="Version of the SolidFire Element software currently installed.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ClusterHardwareInfo(data_model.DataObject):
    """ClusterHardwareInfo  

    :param drives: [required] 
    :type drives: dict

    :param nodes: [required] 
    :type nodes: dict

    """
    drives = data_model.property(
        "drives", dict,
        array=False, optional=False,
        documentation="",
        dictionaryType=DriveHardwareInfo
    )
    nodes = data_model.property(
        "nodes", dict,
        array=False, optional=False,
        documentation="",
        dictionaryType=dict
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class GetClusterHardwareInfoResult(data_model.DataObject):
    """GetClusterHardwareInfoResult  

    :param cluster_hardware_info: [required] Hardware information for all nodes and drives in the cluster. Each object in this output is labeled with the nodeID of the given node. 
    :type cluster_hardware_info: ClusterHardwareInfo

    """
    cluster_hardware_info = data_model.property(
        "clusterHardwareInfo", ClusterHardwareInfo,
        array=False, optional=False,
        documentation="Hardware information for all nodes and drives in the cluster. Each object in this output is labeled with the nodeID of the given node.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class GetAccountResult(data_model.DataObject):
    """GetAccountResult  

    :param account: [required] Account details. 
    :type account: Account

    """
    account = data_model.property(
        "account", Account,
        array=False, optional=False,
        documentation="Account details.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class SupportBundleDetails(data_model.DataObject):
    """SupportBundleDetails  

    :param bundle_name: [required] The name specified in the 'CreateSupportBundle API method. If no name was specified, 'supportbundle' will be used. 
    :type bundle_name: str

    :param extra_args: [required] The arguments passed with this method. 
    :type extra_args: str

    :param files: [required] A list of the support bundle files that were created. 
    :type files: str

    :param url: [required] The URL that you can use to download the bundle file(s). Should correspond 1:1 with files list. 
    :type url: str

    :param output: [required] The commands that were run and their output, with newlines replaced by HTML <br> elements. 
    :type output: str

    :param timeout_sec: [required] The timeout specified for the support bundle creation process. 
    :type timeout_sec: int

    """
    bundle_name = data_model.property(
        "bundleName", str,
        array=False, optional=False,
        documentation="[&quot;The name specified in the &#x27;CreateSupportBundle API method. If no name was specified, &#x27;supportbundle&#x27; will be used.&quot;]",
        dictionaryType=None
    )
    extra_args = data_model.property(
        "extraArgs", str,
        array=False, optional=False,
        documentation="[&#x27;The arguments passed with this method.&#x27;]",
        dictionaryType=None
    )
    files = data_model.property(
        "files", str,
        array=True, optional=False,
        documentation="[&#x27;A list of the support bundle files that were created.&#x27;]",
        dictionaryType=None
    )
    url = data_model.property(
        "url", str,
        array=True, optional=False,
        documentation="[&#x27;The URL that you can use to download the bundle file(s). Should correspond 1:1 with files list.&#x27;]",
        dictionaryType=None
    )
    output = data_model.property(
        "output", str,
        array=False, optional=False,
        documentation="[&#x27;The commands that were run and their output, with newlines replaced by HTML &lt;br&gt; elements.&#x27;]",
        dictionaryType=None
    )
    timeout_sec = data_model.property(
        "timeoutSec", int,
        array=False, optional=False,
        documentation="[&#x27;The timeout specified for the support bundle creation process.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class CreateSupportBundleResult(data_model.DataObject):
    """CreateSupportBundleResult  

    :param details: [required] The details of the support bundle.  
    :type details: SupportBundleDetails

    :param duration: [required] The amount of time required to create the support bundle in the format HH:MM:SS.ssssss 
    :type duration: str

    :param result: [required] Whether the support bundle creation passed of failed. 
    :type result: str

    """
    details = data_model.property(
        "details", SupportBundleDetails,
        array=False, optional=False,
        documentation="[&#x27;The details of the support bundle. &#x27;]",
        dictionaryType=None
    )
    duration = data_model.property(
        "duration", str,
        array=False, optional=False,
        documentation="[&#x27;The amount of time required to create the support bundle in the format HH:MM:SS.ssssss&#x27;]",
        dictionaryType=None
    )
    result = data_model.property(
        "result", str,
        array=False, optional=False,
        documentation="[&#x27;Whether the support bundle creation passed of failed.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class SetClusterConfigResult(data_model.DataObject):
    """SetClusterConfigResult  

    :param cluster: [required] Settings for the cluster. All new and current settings are returned. 
    :type cluster: ClusterConfig

    """
    cluster = data_model.property(
        "cluster", ClusterConfig,
        array=False, optional=False,
        documentation="Settings for the cluster. All new and current settings are returned.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ListAccountsRequest(data_model.DataObject):
    """ListAccountsRequest  

    :param start_account_id:  Starting AccountID to return. If no Account exists with this AccountID, the next Account by AccountID order is used as the start of the list. To page through the list, pass the AccountID of the last Account in the previous response + 1 
    :type start_account_id: int

    :param limit:  Maximum number of AccountInfo objects to return. 
    :type limit: int

    """
    start_account_id = data_model.property(
        "startAccountID", int,
        array=False, optional=True,
        documentation="[&#x27;Starting AccountID to return.&#x27;, &#x27;If no Account exists with this AccountID,&#x27;, &#x27;the next Account by AccountID order is used as the start of the list.&#x27;, &#x27;To page through the list, pass the AccountID of the last Account in the previous response + 1&#x27;]",
        dictionaryType=None
    )
    limit = data_model.property(
        "limit", int,
        array=False, optional=True,
        documentation="Maximum number of AccountInfo objects to return.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class CreateBackupTargetResult(data_model.DataObject):
    """CreateBackupTargetResult  

    :param backup_target_id: [required] Unique identifier assigned to the backup target. 
    :type backup_target_id: int

    """
    backup_target_id = data_model.property(
        "backupTargetID", int,
        array=False, optional=False,
        documentation="[&#x27;Unique identifier assigned to the backup target.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class SetDefaultQoSResult(data_model.DataObject):
    """SetDefaultQoSResult  

    :param min_iops: [required] The minimum number of sustained IOPS that are provided by the cluster to a volume.  
    :type min_iops: int

    :param max_iops: [required] The maximum number of sustained IOPS that are provided by the cluster to a volume. 
    :type max_iops: int

    :param burst_iops: [required] The maximum number of IOPS allowed in a short burst scenario. 
    :type burst_iops: int

    """
    min_iops = data_model.property(
        "minIOPS", int,
        array=False, optional=False,
        documentation="The minimum number of sustained IOPS that are provided by the cluster to a volume. ",
        dictionaryType=None
    )
    max_iops = data_model.property(
        "maxIOPS", int,
        array=False, optional=False,
        documentation="The maximum number of sustained IOPS that are provided by the cluster to a volume.",
        dictionaryType=None
    )
    burst_iops = data_model.property(
        "burstIOPS", int,
        array=False, optional=False,
        documentation="The maximum number of IOPS allowed in a short burst scenario.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ModifyVolumePairResult(data_model.DataObject):
    """ModifyVolumePairResult  

    """

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class GetVolumeCountResult(data_model.DataObject):
    """GetVolumeCountResult  

    :param count: [required] The number of volumes currently in the system. 
    :type count: int

    """
    count = data_model.property(
        "count", int,
        array=False, optional=False,
        documentation="The number of volumes currently in the system.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class CancelGroupCloneRequest(data_model.DataObject):
    """CancelGroupCloneRequest  

    :param group_clone_id: [required] cloneID for the ongoing clone process. 
    :type group_clone_id: int

    """
    group_clone_id = data_model.property(
        "groupCloneID", int,
        array=False, optional=False,
        documentation="cloneID for the ongoing clone process.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class DeleteGroupSnapshotRequest(data_model.DataObject):
    """DeleteGroupSnapshotRequest  

    :param group_snapshot_id: [required] Unique ID of the group snapshot. 
    :type group_snapshot_id: int

    :param save_members: [required] true: Snapshots are kept, but group association is removed. false: The group and snapshots are deleted. 
    :type save_members: bool

    """
    group_snapshot_id = data_model.property(
        "groupSnapshotID", int,
        array=False, optional=False,
        documentation="Unique ID of the group snapshot.",
        dictionaryType=None
    )
    save_members = data_model.property(
        "saveMembers", bool,
        array=False, optional=False,
        documentation="[&#x27;true: Snapshots are kept, but group association is removed.&#x27;, &#x27;false: The group and snapshots are deleted.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class CompleteClusterPairingResult(data_model.DataObject):
    """CompleteClusterPairingResult  

    :param cluster_pair_id: [required] Unique identifier for the cluster pair. 
    :type cluster_pair_id: int

    """
    cluster_pair_id = data_model.property(
        "clusterPairID", int,
        array=False, optional=False,
        documentation="Unique identifier for the cluster pair.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class SetSnmpInfoRequest(data_model.DataObject):
    """SetSnmpInfoRequest  

    :param networks:  List of networks and what type of access they have to the SNMP servers running on the cluster nodes. See SNMP Network Object for possible "networks" values. SNMP v2 only. 
    :type networks: SnmpNetwork

    :param enabled:  If set to "true", then SNMP is enabled on each node in the cluster. 
    :type enabled: bool

    :param snmp_v3_enabled:  If set to "true", then SNMP v3 is enabled on each node in the cluster. 
    :type snmp_v3_enabled: bool

    :param usm_users:  If SNMP v3 is enabled, this value must be passed in place of the "networks" parameter. SNMP v3 only. 
    :type usm_users: SnmpV3UsmUser

    """
    networks = data_model.property(
        "networks", SnmpNetwork,
        array=True, optional=True,
        documentation="List of networks and what type of access they have to the SNMP servers running on the cluster nodes. See SNMP Network Object for possible &quot;networks&quot; values. SNMP v2 only.",
        dictionaryType=None
    )
    enabled = data_model.property(
        "enabled", bool,
        array=False, optional=True,
        documentation="If set to &quot;true&quot;, then SNMP is enabled on each node in the cluster.",
        dictionaryType=None
    )
    snmp_v3_enabled = data_model.property(
        "snmpV3Enabled", bool,
        array=False, optional=True,
        documentation="If set to &quot;true&quot;, then SNMP v3 is enabled on each node in the cluster.",
        dictionaryType=None
    )
    usm_users = data_model.property(
        "usmUsers", SnmpV3UsmUser,
        array=True, optional=True,
        documentation="If SNMP v3 is enabled, this value must be passed in place of the &quot;networks&quot; parameter. SNMP v3 only.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ListActiveVolumesRequest(data_model.DataObject):
    """ListActiveVolumesRequest  

    :param start_volume_id:  The ID of the first volume to list. This can be useful for paging results. By default, this starts at the lowest VolumeID. 
    :type start_volume_id: int

    :param limit:  The maximum number of volumes to return from the API. 
    :type limit: int

    """
    start_volume_id = data_model.property(
        "startVolumeID", int,
        array=False, optional=True,
        documentation="[&#x27;The ID of the first volume to list.&#x27;, &#x27;This can be useful for paging results.&#x27;, &#x27;By default, this starts at the lowest VolumeID.&#x27;]",
        dictionaryType=None
    )
    limit = data_model.property(
        "limit", int,
        array=False, optional=True,
        documentation="[&#x27;The maximum number of volumes to return from the API.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class CreateScheduleRequest(data_model.DataObject):
    """CreateScheduleRequest  

    :param schedule: [required] The "Schedule" object will be used to create a new schedule. Do not set ScheduleID property, it will be ignored. Frequency property must be of type that inherits from Frequency. Valid types are: DaysOfMonthFrequency DaysOrWeekFrequency TimeIntervalFrequency 
    :type schedule: Schedule

    """
    schedule = data_model.property(
        "schedule", Schedule,
        array=False, optional=False,
        documentation="[&#x27;The &quot;Schedule&quot; object will be used to create a new schedule.&#x27;, &#x27;Do not set ScheduleID property, it will be ignored.&#x27;, &#x27;Frequency property must be of type that inherits from Frequency. Valid types are:&#x27;, &#x27;DaysOfMonthFrequency&#x27;, &#x27;DaysOrWeekFrequency&#x27;, &#x27;TimeIntervalFrequency&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)