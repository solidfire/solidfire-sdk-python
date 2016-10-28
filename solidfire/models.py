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


class CHAPSecret(UserDefinedCHAPSecret):
    def __init__(self, **kwargs):
        self = UserDefinedCHAPSecret()
        data_model.DataObject.__init__(self, **kwargs)


class Frequency(UserDefinedFrequency):
    def __init__(self, **kwargs):
        self = UserDefinedFrequency()
        data_model.DataObject.__init__(self, **kwargs)

class DriveHardware(data_model.DataObject):
    """
    :param canonicalName: [required] 
    :type canonicalName: str
    
    :param connected: [required] 
    :type connected: bool
    
    :param dev: [required] 
    :type dev: int
    
    :param devPath: [required] 
    :type devPath: str
    
    :param driveType: [required] 
    :type driveType: str
    
    :param lifeRemainingPercent: [required] 
    :type lifeRemainingPercent: int
    
    :param lifetimeReadBytes: [required] 
    :type lifetimeReadBytes: int
    
    :param lifetimeWriteBytes: [required] 
    :type lifetimeWriteBytes: int
    
    :param name: [required] 
    :type name: str
    
    :param path: [required] 
    :type path: str
    
    :param pathLink: [required] 
    :type pathLink: str
    
    :param powerOnHours: [required] 
    :type powerOnHours: int
    
    :param product: [required] 
    :type product: str
    
    :param reallocatedSectors: [required] 
    :type reallocatedSectors: int
    
    :param reserveCapacityPercent: [required] 
    :type reserveCapacityPercent: int
    
    :param scsiCompatId: [required] 
    :type scsiCompatId: str
    
    :param scsiState: [required] 
    :type scsiState: str
    
    :param securityAtMaximum: [required] 
    :type securityAtMaximum: bool
    
    :param securityEnabled: [required] 
    :type securityEnabled: bool
    
    :param securityFrozen: [required] 
    :type securityFrozen: bool
    
    :param securityLocked: [required] 
    :type securityLocked: bool
    
    :param securitySupported: [required] 
    :type securitySupported: bool
    
    :param serial: [required] 
    :type serial: str
    
    :param size: [required] 
    :type size: int
    
    :param slot: [required] 
    :type slot: int
    
    :param smartSsdWriteCapable:  
    :type smartSsdWriteCapable: bool
    
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
    """
    :param driveHardware: [required] 
    :type driveHardware: DriveHardware
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
    """
    :param nodeID: [required] 
    :type nodeID: int
    
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
    """
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


class DriveHardwareInfo(data_model.DataObject):
    """
    :param description: [required] 
    :type description: str
    
    :param dev: [required] 
    :type dev: str
    
    :param devpath: [required] 
    :type devpath: str
    
    :param driveSecurityAtMaximum: [required] 
    :type driveSecurityAtMaximum: bool
    
    :param driveSecurityFrozen: [required] 
    :type driveSecurityFrozen: bool
    
    :param driveSecurityLocked: [required] 
    :type driveSecurityLocked: bool
    
    :param logicalname: [required] 
    :type logicalname: str
    
    :param product: [required] 
    :type product: str
    
    :param scsiCompatID: [required] 
    :type scsiCompatID: str
    
    :param securityFeatureEnabled: [required] 
    :type securityFeatureEnabled: bool
    
    :param securityFeatureSupported: [required] 
    :type securityFeatureSupported: bool
    
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


class ModifyScheduleResult(data_model.DataObject):
    """"""

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class SnmpV3UsmUser(data_model.DataObject):
    """
    The SNMP v3 usmUser object is used with the API method SetSnmpInfo to configure SNMP on the cluster.
    :param access: [required] [&#x27;&lt;br/&gt;&lt;b&gt;rouser&lt;/b&gt;: read-only access.*&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;rwuser&lt;/b&gt;: for read-write access.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;rosys&lt;/b&gt;: for read-only access to a restricted set of system information&#x27;, &#x27;*SolidFire recommends that all USM users be set to &quot;rouser&quot; access, because all SolidFire MIB objects are read-only.&#x27;][&#x27;&lt;br/&gt;&lt;b&gt;rouser&lt;/b&gt;: read-only access.*&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;rwuser&lt;/b&gt;: for read-write access.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;rosys&lt;/b&gt;: for read-only access to a restricted set of system information&#x27;, &#x27;*SolidFire recommends that all USM users be set to &quot;rouser&quot; access, because all SolidFire MIB objects are read-only.&#x27;][&#x27;&lt;br/&gt;&lt;b&gt;rouser&lt;/b&gt;: read-only access.*&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;rwuser&lt;/b&gt;: for read-write access.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;rosys&lt;/b&gt;: for read-only access to a restricted set of system information&#x27;, &#x27;*SolidFire recommends that all USM users be set to &quot;rouser&quot; access, because all SolidFire MIB objects are read-only.&#x27;][&#x27;&lt;br/&gt;&lt;b&gt;rouser&lt;/b&gt;: read-only access.*&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;rwuser&lt;/b&gt;: for read-write access.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;rosys&lt;/b&gt;: for read-only access to a restricted set of system information&#x27;, &#x27;*SolidFire recommends that all USM users be set to &quot;rouser&quot; access, because all SolidFire MIB objects are read-only.&#x27;]
    :type access: str
    
    :param name: [required] [&#x27;The name of the user. Must contain at least one character, but no more than 32 characters. Blank spaces are not allowed.&#x27;]
    :type name: str
    
    :param password: [required] [&#x27;The password of the user. Must be between 8 and 255 characters long (inclusive). Blank spaces are not allowed. Required if &quot;secLevel&quot; is &quot;auth&quot; or &quot;priv.&quot;&#x27;]
    :type password: str
    
    :param passphrase: [required] [&#x27;The passphrase of the user. Must be between 8 and 255 characters long (inclusive). Blank spaces are not allowed. Required if &quot;secLevel&quot; is &quot;priv.&quot;&#x27;]
    :type passphrase: str
    
    :param secLevel: [required] [&#x27;&lt;br/&gt;&lt;b&gt;noauth&lt;/b&gt;: No password or passphrase is required.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;auth&lt;/b&gt;: A password is required for user access.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;priv&lt;/b&gt;: A password and passphrase is required for user access.&#x27;][&#x27;&lt;br/&gt;&lt;b&gt;noauth&lt;/b&gt;: No password or passphrase is required.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;auth&lt;/b&gt;: A password is required for user access.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;priv&lt;/b&gt;: A password and passphrase is required for user access.&#x27;][&#x27;&lt;br/&gt;&lt;b&gt;noauth&lt;/b&gt;: No password or passphrase is required.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;auth&lt;/b&gt;: A password is required for user access.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;priv&lt;/b&gt;: A password and passphrase is required for user access.&#x27;]
    :type secLevel: str
    """
    access = data_model.property(
        "access", str,
        array=False, optional=False,
        documentation="[&#x27;&lt;br/&gt;&lt;b&gt;rouser&lt;/b&gt;: read-only access.*&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;rwuser&lt;/b&gt;: for read-write access.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;rosys&lt;/b&gt;: for read-only access to a restricted set of system information&#x27;, &#x27;*SolidFire recommends that all USM users be set to &quot;rouser&quot; access, because all SolidFire MIB objects are read-only.&#x27;]",
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
        documentation="[&#x27;&lt;br/&gt;&lt;b&gt;noauth&lt;/b&gt;: No password or passphrase is required.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;auth&lt;/b&gt;: A password is required for user access.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;priv&lt;/b&gt;: A password and passphrase is required for user access.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class PendingNodeToNode(data_model.DataObject):
    """
    :param nodeID: [required] 
    :type nodeID: int
    
    :param pendingNodeID: [required] 
    :type pendingNodeID: int
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


class RemoveNodesResult(data_model.DataObject):
    """"""

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class SnmpSendTestTrapsResult(data_model.DataObject):
    """
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


class DatabaseStats(data_model.DataObject):
    """
    Database entry statistics
    :param createTime: [required] 
    :type createTime: str
    
    :param dataVersion: [required] 
    :type dataVersion: int
    
    :param numChildren: [required] 
    :type numChildren: int
    
    :param size: [required] 
    :type size: int
    """
    create_time = data_model.property(
        "createTime", str,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    data_version = data_model.property(
        "dataVersion", int,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    num_children = data_model.property(
        "numChildren", int,
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

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class CreateDatabaseEntryResult(data_model.DataObject):
    """
    :param stat: [required] 
    :type stat: DatabaseStats
    """
    stat = data_model.property(
        "stat", DatabaseStats,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class MetadataHosts(data_model.DataObject):
    """
    The volume services on which the volume metadata resides.
    :param deadSecondaries: [required] Secondary metadata (slice) services that are in a dead state.
    :type deadSecondaries: int
    
    :param liveSecondaries: [required] Secondary metadata (slice) services that are currently in a &quot;live&quot; state.
    :type liveSecondaries: int
    
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


class EventInfo(data_model.DataObject):
    """
    :param eventID: [required] 
    :type eventID: int
    
    :param severity: [required] 
    :type severity: int
    
    :param eventInfoType: [required] 
    :type eventInfoType: str
    
    :param message: [required] 
    :type message: str
    
    :param serviceID: [required] 
    :type serviceID: int
    
    :param nodeID: [required] 
    :type nodeID: int
    
    :param driveID: [required] 
    :type driveID: int
    
    :param timeOfReport: [required] 
    :type timeOfReport: str
    
    :param timeOfPublish: [required] 
    :type timeOfPublish: str
    
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
    """
    :param eventQueueType: [required] 
    :type eventQueueType: str
    
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


class PendingOperation(data_model.DataObject):
    """
    :param pending: [required] [&#x27;&lt;br/&gt;&lt;b&gt;true&lt;/b&gt;: operation is still in progress.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;false&lt;/b&gt;: operation is no longer in progress.&#x27;][&#x27;&lt;br/&gt;&lt;b&gt;true&lt;/b&gt;: operation is still in progress.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;false&lt;/b&gt;: operation is no longer in progress.&#x27;]
    :type pending: bool
    
    :param operation: [required] Name of operation that is in progress or has completed.
    :type operation: str
    """
    pending = data_model.property(
        "pending", bool,
        array=False, optional=False,
        documentation="[&#x27;&lt;br/&gt;&lt;b&gt;true&lt;/b&gt;: operation is still in progress.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;false&lt;/b&gt;: operation is no longer in progress.&#x27;]",
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


class FibreChannelPortInfo(data_model.DataObject):
    """
    [&#x27;Fibre Channel Node Port Info object returns information about all Fibre Channel ports on a node, or for one node in the cluster. The same information is returned for all ports or port information for one node. This information is returned with the API method ListNodeFibreChannelPortInfo (in the SolidFire API Guide).&#x27;]
    :param firmware: [required] The version of the firmware installed on the Fibre Channel port.
    :type firmware: str
    
    :param hbaPort: [required] The ID of the individual HBA port.
    :type hbaPort: int
    
    :param model: [required] Model of the HBA on the port.
    :type model: str
    
    :param nPortID: [required] Unique SolidFire port node ID.
    :type nPortID: str
    
    :param pciSlot: [required] Slot in which the pci card resides on the Fibre Channel node hardware.
    :type pciSlot: int
    
    :param serial: [required] Serial number on the Fibre Channel port.
    :type serial: str
    
    :param speed: [required] Speed of the HBA on the port.
    :type speed: str
    
    :param state: [required] [&#x27;Possible values:&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;&lt;strong&gt;Unknown&lt;br/&gt;NotPresent&lt;br/&gt;Online&lt;br/&gt;Offline&lt;br/&gt;Blocked&lt;br/&gt;Bypassed&lt;br/&gt;Diagnostics&lt;br/&gt;Linkdown&lt;br/&gt;Error&lt;br/&gt;Loopback&lt;br/&gt;Deleted&lt;/strong&gt;&#x27;][&#x27;Possible values:&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;&lt;strong&gt;Unknown&lt;br/&gt;NotPresent&lt;br/&gt;Online&lt;br/&gt;Offline&lt;br/&gt;Blocked&lt;br/&gt;Bypassed&lt;br/&gt;Diagnostics&lt;br/&gt;Linkdown&lt;br/&gt;Error&lt;br/&gt;Loopback&lt;br/&gt;Deleted&lt;/strong&gt;&#x27;][&#x27;Possible values:&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;&lt;strong&gt;Unknown&lt;br/&gt;NotPresent&lt;br/&gt;Online&lt;br/&gt;Offline&lt;br/&gt;Blocked&lt;br/&gt;Bypassed&lt;br/&gt;Diagnostics&lt;br/&gt;Linkdown&lt;br/&gt;Error&lt;br/&gt;Loopback&lt;br/&gt;Deleted&lt;/strong&gt;&#x27;]
    :type state: str
    
    :param switchWwn: [required] The World Wide Name of the Fibre Channel switch port.
    :type switchWwn: str
    
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
        documentation="[&#x27;Possible values:&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;&lt;strong&gt;Unknown&lt;br/&gt;NotPresent&lt;br/&gt;Online&lt;br/&gt;Offline&lt;br/&gt;Blocked&lt;br/&gt;Bypassed&lt;br/&gt;Diagnostics&lt;br/&gt;Linkdown&lt;br/&gt;Error&lt;br/&gt;Loopback&lt;br/&gt;Deleted&lt;/strong&gt;&#x27;]",
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
    """
    List of all Fibre Channel ports.
    :param fibreChannelPorts: [required] List of all physical Fibre Channel ports.
    :type fibreChannelPorts: FibreChannelPortInfo
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
    """
    Fibre channel port info results for a node.
    :param nodeID: [required] The ID of the Fibre Channel node.
    :type nodeID: int
    
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
    """
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


class SnapshotReplication(data_model.DataObject):
    """
    :param state: [required] The state of the snapshot replication.
    :type state: str
    
    :param stateDetails: [required] Reserved for future use.
    :type stateDetails: str
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
    """
    Details on the volume replication.
    :param mode: [required] [&#x27;Volume replication mode.&lt;br/&gt;&#x27;, &#x27;Possible values:&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Async&lt;/b&gt;: Writes are acknowledged when they complete locally. The cluster does not wait for writes to be replicated to the target cluster.&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Sync&lt;/b&gt;: Source acknowledges write when the data is stored locally and on the remote cluster.&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;SnapshotsOnly&lt;/b&gt;: Only snapshots created on the source cluster will be replicated. Active writes from the source volume will not be replicated.&lt;br/&gt;&#x27;][&#x27;Volume replication mode.&lt;br/&gt;&#x27;, &#x27;Possible values:&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Async&lt;/b&gt;: Writes are acknowledged when they complete locally. The cluster does not wait for writes to be replicated to the target cluster.&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Sync&lt;/b&gt;: Source acknowledges write when the data is stored locally and on the remote cluster.&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;SnapshotsOnly&lt;/b&gt;: Only snapshots created on the source cluster will be replicated. Active writes from the source volume will not be replicated.&lt;br/&gt;&#x27;][&#x27;Volume replication mode.&lt;br/&gt;&#x27;, &#x27;Possible values:&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Async&lt;/b&gt;: Writes are acknowledged when they complete locally. The cluster does not wait for writes to be replicated to the target cluster.&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Sync&lt;/b&gt;: Source acknowledges write when the data is stored locally and on the remote cluster.&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;SnapshotsOnly&lt;/b&gt;: Only snapshots created on the source cluster will be replicated. Active writes from the source volume will not be replicated.&lt;br/&gt;&#x27;][&#x27;Volume replication mode.&lt;br/&gt;&#x27;, &#x27;Possible values:&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Async&lt;/b&gt;: Writes are acknowledged when they complete locally. The cluster does not wait for writes to be replicated to the target cluster.&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Sync&lt;/b&gt;: Source acknowledges write when the data is stored locally and on the remote cluster.&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;SnapshotsOnly&lt;/b&gt;: Only snapshots created on the source cluster will be replicated. Active writes from the source volume will not be replicated.&lt;br/&gt;&#x27;][&#x27;Volume replication mode.&lt;br/&gt;&#x27;, &#x27;Possible values:&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Async&lt;/b&gt;: Writes are acknowledged when they complete locally. The cluster does not wait for writes to be replicated to the target cluster.&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Sync&lt;/b&gt;: Source acknowledges write when the data is stored locally and on the remote cluster.&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;SnapshotsOnly&lt;/b&gt;: Only snapshots created on the source cluster will be replicated. Active writes from the source volume will not be replicated.&lt;br/&gt;&#x27;]
    :type mode: str
    
    :param pauseLimit: [required] The number of occurring write ops before auto-pausing, on a per volume pair level.
    :type pauseLimit: int
    
    :param remoteServiceID: [required] The remote slice service ID.
    :type remoteServiceID: int
    
    :param resumeDetails: [required] Reserved for future use.
    :type resumeDetails: str
    
    :param snapshotReplication: [required] The details of snapshot replication.
    :type snapshotReplication: SnapshotReplication
    
    :param state: [required] The state of the volume replication.
    :type state: str
    
    :param stateDetails: [required] Reserved for future use.
    :type stateDetails: str
    """
    mode = data_model.property(
        "mode", str,
        array=False, optional=False,
        documentation="[&#x27;Volume replication mode.&lt;br/&gt;&#x27;, &#x27;Possible values:&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Async&lt;/b&gt;: Writes are acknowledged when they complete locally. The cluster does not wait for writes to be replicated to the target cluster.&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Sync&lt;/b&gt;: Source acknowledges write when the data is stored locally and on the remote cluster.&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;SnapshotsOnly&lt;/b&gt;: Only snapshots created on the source cluster will be replicated. Active writes from the source volume will not be replicated.&lt;br/&gt;&#x27;]",
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
    """
    [&#x27;The Volume Pair Info is an object containing information about a volume that is paired on a remote cluster.&#x27;, &#x27;If the volume is not paired, this object is null.&#x27;]
    [&#x27;The Volume Pair Info is an object containing information about a volume that is paired on a remote cluster.&#x27;, &#x27;If the volume is not paired, this object is null.&#x27;]
    :param clusterPairID: [required] The remote cluster a volume is paired with.
    :type clusterPairID: int
    
    :param remoteVolumeID: [required] The VolumeID on the remote cluster a volume is paired with.
    :type remoteVolumeID: int
    
    :param remoteSliceID: [required] The SliceID on the remote cluster a volume is paired with.
    :type remoteSliceID: int
    
    :param remoteVolumeName: [required] The last-observed name of the volume on the remote cluster a volume is paired with.
    :type remoteVolumeName: str
    
    :param volumePairUUID: [required] A UUID in canonical form.
    :type volumePairUUID: UUID
    
    :param remoteReplication: [required] Details about the replication configuration for this volume pair.
    :type remoteReplication: RemoteReplication
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


class TestDrivesResult(data_model.DataObject):
    """
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


class StartBulkVolumeWriteResult(data_model.DataObject):
    """
    :param asyncHandle: [required] ID of the async process to be checked for completion.
    :type asyncHandle: int
    
    :param key: [required] Opaque key uniquely identifying the session.
    :type key: str
    
    :param url: [required] URL to access the node&#x27;s web server
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


class AddClusterAdminResult(data_model.DataObject):
    """
    :param clusterAdminID: [required] ClusterAdminID for the newly created Cluster Admin.
    :type clusterAdminID: int
    """
    cluster_admin_id = data_model.property(
        "clusterAdminID", int,
        array=False, optional=False,
        documentation="ClusterAdminID for the newly created Cluster Admin.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class ClusterHardwareInfo(data_model.DataObject):
    """
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


class DisableLdapAuthenticationResult(data_model.DataObject):
    """"""

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class NetworkInterface(data_model.DataObject):
    """
    :param address: [required] IP address of the network.
    :type address: str
    
    :param broadcast: [required] Address of NTP broadcast.
    :type broadcast: str
    
    :param macAddress: [required] Address used to configure the interface.
    :type macAddress: str
    
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
    
    :param virtualNetworkTag: [required] Virtual Network Tag if on virtual network.
    :type virtualNetworkTag: int
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


class NetworkInterfaces(data_model.DataObject):
    """
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


class NodeNetworkInterface(data_model.DataObject):
    """
    :param nodeID: [required] The ID of the node.
    :type nodeID: int
    
    :param result: [required] 
    :type result: NetworkInterfaces
    """
    node_id = data_model.property(
        "nodeID", int,
        array=False, optional=False,
        documentation="The ID of the node.",
        dictionaryType=None
    )
    result = data_model.property(
        "result", NetworkInterfaces,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class ListClusterNetworkInterfacesResult(data_model.DataObject):
    """
    :param nodes: [required] 
    :type nodes: NodeNetworkInterface
    """
    nodes = data_model.property(
        "nodes", NodeNetworkInterface,
        array=True, optional=False,
        documentation="",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class StartBulkVolumeReadResult(data_model.DataObject):
    """
    :param asyncHandle: [required] ID of the async process to be checked for completion.
    :type asyncHandle: int
    
    :param key: [required] Opaque key uniquely identifying the session.
    :type key: str
    
    :param url: [required] URL to access the node&#x27;s web server
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


class VolumeStats(data_model.DataObject):
    """
    Contains statistical data for an individual volume.
    :param accountID: [required] AccountID of the volume owner.
    :type accountID: int
    
    :param actualIOPS: [required] Current actual IOPS to the volume in the last 500 milliseconds.
    :type actualIOPS: int
    
    :param asyncDelay:  [&#x27;The length of time since the volume was last synced with the remote cluster.&#x27;, &#x27;If the volume is not paired, this is null.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;Note&lt;/b&gt;: A target volume in an active replication state always has an async delay of 0 (zero).&#x27;, &#x27;&lt;br/&gt;Target volumes are system-aware during replication and assume async delay is accurate at all times.&#x27;][&#x27;The length of time since the volume was last synced with the remote cluster.&#x27;, &#x27;If the volume is not paired, this is null.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;Note&lt;/b&gt;: A target volume in an active replication state always has an async delay of 0 (zero).&#x27;, &#x27;&lt;br/&gt;Target volumes are system-aware during replication and assume async delay is accurate at all times.&#x27;][&#x27;The length of time since the volume was last synced with the remote cluster.&#x27;, &#x27;If the volume is not paired, this is null.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;Note&lt;/b&gt;: A target volume in an active replication state always has an async delay of 0 (zero).&#x27;, &#x27;&lt;br/&gt;Target volumes are system-aware during replication and assume async delay is accurate at all times.&#x27;][&#x27;The length of time since the volume was last synced with the remote cluster.&#x27;, &#x27;If the volume is not paired, this is null.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;Note&lt;/b&gt;: A target volume in an active replication state always has an async delay of 0 (zero).&#x27;, &#x27;&lt;br/&gt;Target volumes are system-aware during replication and assume async delay is accurate at all times.&#x27;][&#x27;The length of time since the volume was last synced with the remote cluster.&#x27;, &#x27;If the volume is not paired, this is null.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;Note&lt;/b&gt;: A target volume in an active replication state always has an async delay of 0 (zero).&#x27;, &#x27;&lt;br/&gt;Target volumes are system-aware during replication and assume async delay is accurate at all times.&#x27;]
    :type asyncDelay: str
    
    :param averageIOPSize: [required] Average size in bytes of recent I/O to the volume in the last 500 milliseconds.
    :type averageIOPSize: int
    
    :param burstIOPSCredit: [required] [&#x27;The total number of IOP credits available to the user.&#x27;, &#x27;When users are not using up to the max IOPS, credits are accrued.&#x27;][&#x27;The total number of IOP credits available to the user.&#x27;, &#x27;When users are not using up to the max IOPS, credits are accrued.&#x27;]
    :type burstIOPSCredit: int
    
    :param clientQueueDepth: [required] The number of outstanding read and write operations to the cluster.
    :type clientQueueDepth: int
    
    :param desiredMetadataHosts: [required] [&#x27;The volume services being migrated to if the volume metadata is getting migrated between volume services.&#x27;, &#x27;A &quot;null&quot; value means the volume is not migrating.&#x27;][&#x27;The volume services being migrated to if the volume metadata is getting migrated between volume services.&#x27;, &#x27;A &quot;null&quot; value means the volume is not migrating.&#x27;]
    :type desiredMetadataHosts: MetadataHosts
    
    :param latencyUSec: [required] [&#x27;The observed latency time, in microseconds, to complete operations to a volume.&lt;br/&gt;&#x27;, &#x27;A &quot;0&quot; (zero) value means there is no I/O to the volume.&#x27;][&#x27;The observed latency time, in microseconds, to complete operations to a volume.&lt;br/&gt;&#x27;, &#x27;A &quot;0&quot; (zero) value means there is no I/O to the volume.&#x27;]
    :type latencyUSec: int
    
    :param metadataHosts: [required] The volume services on which the volume metadata resides.
    :type metadataHosts: MetadataHosts
    
    :param nonZeroBlocks: [required] The number of 4KiB blocks with data after the last garbage collection operation has completed.
    :type nonZeroBlocks: int
    
    :param readBytes: [required] Total bytes read by clients.
    :type readBytes: int
    
    :param readLatencyUSec: [required] The average time, in microseconds, to complete read operations.
    :type readLatencyUSec: int
    
    :param readOps: [required] Total read operations.
    :type readOps: int
    
    :param throttle: [required] [&#x27;A floating value between 0 and 1 that represents how much the system is throttling clients&#x27;, &#x27;below their max IOPS because of re-replication of data, transient errors and snapshots taken.&#x27;][&#x27;A floating value between 0 and 1 that represents how much the system is throttling clients&#x27;, &#x27;below their max IOPS because of re-replication of data, transient errors and snapshots taken.&#x27;]
    :type throttle: float
    
    :param timestamp: [required] The current time in UTC.
    :type timestamp: str
    
    :param totalLatencyUSec: [required] The average time, in microseconds, to complete read and write operations to a volume.
    :type totalLatencyUSec: int
    
    :param unalignedReads: [required] [&#x27;For 512e volumes, the number of read operations that were not on a 4k sector boundary.&#x27;, &#x27;High numbers of unaligned reads may indicate improper partition alignment.&#x27;][&#x27;For 512e volumes, the number of read operations that were not on a 4k sector boundary.&#x27;, &#x27;High numbers of unaligned reads may indicate improper partition alignment.&#x27;]
    :type unalignedReads: int
    
    :param unalignedWrites: [required] [&#x27;For 512e volumes, the number of write operations that were not on a 4k sector boundary.&#x27;, &#x27;High numbers of unaligned writes may indicate improper partition alignment.&#x27;][&#x27;For 512e volumes, the number of write operations that were not on a 4k sector boundary.&#x27;, &#x27;High numbers of unaligned writes may indicate improper partition alignment.&#x27;]
    :type unalignedWrites: int
    
    :param volumeAccessGroups: [required] List of volume access group(s) to which a volume belongs.
    :type volumeAccessGroups: int
    
    :param volumeID: [required] Volume ID of the volume.
    :type volumeID: int
    
    :param volumeSize: [required] Total provisioned capacity in bytes.
    :type volumeSize: int
    
    :param volumeUtilization: [required] [&#x27;A floating value that describes how much the client is using the volume.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;Values:&lt;br/&gt;&#x27;, &#x27; 0 = Client is not using the volume&lt;br/&gt;&#x27;, &#x27;1 = Client is using their max&lt;br/&gt;&#x27;, &#x27;&gt;1 = Client is using their burst&#x27;][&#x27;A floating value that describes how much the client is using the volume.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;Values:&lt;br/&gt;&#x27;, &#x27; 0 = Client is not using the volume&lt;br/&gt;&#x27;, &#x27;1 = Client is using their max&lt;br/&gt;&#x27;, &#x27;&gt;1 = Client is using their burst&#x27;][&#x27;A floating value that describes how much the client is using the volume.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;Values:&lt;br/&gt;&#x27;, &#x27; 0 = Client is not using the volume&lt;br/&gt;&#x27;, &#x27;1 = Client is using their max&lt;br/&gt;&#x27;, &#x27;&gt;1 = Client is using their burst&#x27;][&#x27;A floating value that describes how much the client is using the volume.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;Values:&lt;br/&gt;&#x27;, &#x27; 0 = Client is not using the volume&lt;br/&gt;&#x27;, &#x27;1 = Client is using their max&lt;br/&gt;&#x27;, &#x27;&gt;1 = Client is using their burst&#x27;][&#x27;A floating value that describes how much the client is using the volume.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;Values:&lt;br/&gt;&#x27;, &#x27; 0 = Client is not using the volume&lt;br/&gt;&#x27;, &#x27;1 = Client is using their max&lt;br/&gt;&#x27;, &#x27;&gt;1 = Client is using their burst&#x27;][&#x27;A floating value that describes how much the client is using the volume.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;Values:&lt;br/&gt;&#x27;, &#x27; 0 = Client is not using the volume&lt;br/&gt;&#x27;, &#x27;1 = Client is using their max&lt;br/&gt;&#x27;, &#x27;&gt;1 = Client is using their burst&#x27;]
    :type volumeUtilization: float
    
    :param writeBytes: [required] Total bytes written by clients.
    :type writeBytes: int
    
    :param writeLatencyUSec: [required] The average time, in microseconds, to complete write operations.
    :type writeLatencyUSec: int
    
    :param writeOps: [required] Total write operations occurring on the volume.
    :type writeOps: int
    
    :param zeroBlocks: [required] Total number of 4KiB blocks without data after the last round of garbage collection operation has completed.
    :type zeroBlocks: int
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
        documentation="[&#x27;The length of time since the volume was last synced with the remote cluster.&#x27;, &#x27;If the volume is not paired, this is null.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;Note&lt;/b&gt;: A target volume in an active replication state always has an async delay of 0 (zero).&#x27;, &#x27;&lt;br/&gt;Target volumes are system-aware during replication and assume async delay is accurate at all times.&#x27;]",
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
        documentation="[&#x27;The observed latency time, in microseconds, to complete operations to a volume.&lt;br/&gt;&#x27;, &#x27;A &quot;0&quot; (zero) value means there is no I/O to the volume.&#x27;]",
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
        documentation="[&#x27;A floating value that describes how much the client is using the volume.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;Values:&lt;br/&gt;&#x27;, &#x27; 0 = Client is not using the volume&lt;br/&gt;&#x27;, &#x27;1 = Client is using their max&lt;br/&gt;&#x27;, &#x27;&gt;1 = Client is using their burst&#x27;]",
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

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class ListVolumeStatsByVolumeAccessGroupResult(data_model.DataObject):
    """
    :param volumeStats: [required] [&#x27;List of account activity information.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;Note&lt;/b&gt;: The volumeID member is 0 for each entry, as the values represent the summation of all volumes owned by the account.&#x27;][&#x27;List of account activity information.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;Note&lt;/b&gt;: The volumeID member is 0 for each entry, as the values represent the summation of all volumes owned by the account.&#x27;]
    :type volumeStats: VolumeStats
    """
    volume_stats = data_model.property(
        "volumeStats", VolumeStats,
        array=True, optional=False,
        documentation="[&#x27;List of account activity information.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;Note&lt;/b&gt;: The volumeID member is 0 for each entry, as the values represent the summation of all volumes owned by the account.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class ClusterConfig(data_model.DataObject):
    """
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
    
    :param nodeID:  
    :type nodeID: int
    
    :param pendingNodeID:  
    :type pendingNodeID: int
    
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
    """
    :param address:  
    :type address: str
    
    :param macAddress:  
    :type macAddress: str
    
    :param macAddressPermanent:  
    :type macAddressPermanent: str
    
    :param mtu:  
    :type mtu: str
    
    :param netmask:  
    :type netmask: str
    
    :param network:  
    :type network: str
    
    :param upAndRunning:  
    :type upAndRunning: bool
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
    """
    :param _default:  
    :type _default: bool
    
    :param address:  
    :type address: str
    
    :param auto:  
    :type auto: bool
    
    :param bond_downdelay:  
    :type bond_downdelay: int
    
    :param bond_fail_over_mac:  
    :type bond_fail_over_mac: str
    
    :param bond_primary_reselect:  
    :type bond_primary_reselect: str
    
    :param bond_lacp_rate:  
    :type bond_lacp_rate: str
    
    :param bond_miimon:  
    :type bond_miimon: int
    
    :param bond_mode:  
    :type bond_mode: str
    
    :param bond_slaves:  
    :type bond_slaves: str
    
    :param bond_updelay:  
    :type bond_updelay: int
    
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
    
    :param macAddress:  
    :type macAddress: str
    
    :param macAddressPermanent:  
    :type macAddressPermanent: str
    
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
    
    :param symmetricRouteRules:  
    :type symmetricRouteRules: str
    
    :param upAndRunning:  
    :type upAndRunning: bool
    """
    _default = data_model.property(
        "_default", bool,
        array=False, optional=True,
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
        "bond_downdelay", int,
        array=False, optional=True,
        documentation="",
        dictionaryType=None
    )
    bond_fail_over_mac = data_model.property(
        "bond_fail_over_mac", str,
        array=False, optional=True,
        documentation="",
        dictionaryType=None
    )
    bond_primary_reselect = data_model.property(
        "bond_primary_reselect", str,
        array=False, optional=True,
        documentation="",
        dictionaryType=None
    )
    bond_lacp_rate = data_model.property(
        "bond_lacp_rate", str,
        array=False, optional=True,
        documentation="",
        dictionaryType=None
    )
    bond_miimon = data_model.property(
        "bond_miimon", int,
        array=False, optional=True,
        documentation="",
        dictionaryType=None
    )
    bond_mode = data_model.property(
        "bond_mode", str,
        array=False, optional=True,
        documentation="",
        dictionaryType=None
    )
    bond_slaves = data_model.property(
        "bond_slaves", str,
        array=False, optional=True,
        documentation="",
        dictionaryType=None
    )
    bond_updelay = data_model.property(
        "bond_updelay", int,
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
        "dns_nameservers", str,
        array=False, optional=True,
        documentation="",
        dictionaryType=None
    )
    dns_search = data_model.property(
        "dns_search", str,
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
    """
    :param Bond10G:  
    :type Bond10G: NetworkConfig
    
    :param Bond1G:  
    :type Bond1G: NetworkConfig
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

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class Config(data_model.DataObject):
    """
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


class ModifyVolumeAccessGroupLunAssignmentsResult(data_model.DataObject):
    """"""

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class SetNtpInfoResult(data_model.DataObject):
    """"""

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class VirtualVolumeHost(data_model.DataObject):
    """
    :param virtualVolumeHostID: [required] 
    :type virtualVolumeHostID: UUID
    
    :param clusterID: [required] 
    :type clusterID: UUID
    
    :param visibleProtocolEndpointIDs: [required] 
    :type visibleProtocolEndpointIDs: UUID
    
    :param bindings: [required] 
    :type bindings: int
    
    :param initiatorNames: [required] 
    :type initiatorNames: str
    
    :param hostAddress: [required] 
    :type hostAddress: str
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
    """
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


class ClusterAdmin(data_model.DataObject):
    """
    :param access: [required] 
    :type access: str
    
    :param clusterAdminID: [required] 
    :type clusterAdminID: int
    
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
    """
    :param clusterAdmins: [required] Information about the cluster admin.
    :type clusterAdmins: ClusterAdmin
    """
    cluster_admins = data_model.property(
        "clusterAdmins", ClusterAdmin,
        array=True, optional=False,
        documentation="Information about the cluster admin.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class VasaProviderInfo(data_model.DataObject):
    """
    :param keystore: [required] 
    :type keystore: str
    
    :param controlPort: [required] 
    :type controlPort: int
    
    :param vasaProviderID: [required] 
    :type vasaProviderID: UUID
    
    :param options: [required] 
    :type options: dict
    """
    keystore = data_model.property(
        "keystore", str,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    control_port = data_model.property(
        "controlPort", int,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    vasa_provider_id = data_model.property(
        "vasaProviderID", UUID,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    options = data_model.property(
        "options", dict,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class CompleteVolumePairingResult(data_model.DataObject):
    """"""

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class GetVirtualVolumeCountResult(data_model.DataObject):
    """
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


class SyncJob(data_model.DataObject):
    """
    :param bytesPerSecond: [required] 
    :type bytesPerSecond: float
    
    :param currentBytes: [required] 
    :type currentBytes: int
    
    :param dstServiceID: [required] 
    :type dstServiceID: int
    
    :param elapsedTime: [required] 
    :type elapsedTime: float
    
    :param percentComplete: [required] 
    :type percentComplete: float
    
    :param remainingTime: [required] 
    :type remainingTime: float
    
    :param sliceID: [required] 
    :type sliceID: int
    
    :param srcServiceID: [required] 
    :type srcServiceID: int
    
    :param totalBytes: [required] 
    :type totalBytes: int
    
    :param type: [required] 
    :type type: str
    
    :param cloneID: [required] 
    :type cloneID: int
    
    :param dstVolumeID: [required] 
    :type dstVolumeID: int
    
    :param nodeID: [required] 
    :type nodeID: int
    
    :param snapshotID: [required] 
    :type snapshotID: int
    
    :param srcVolumeID: [required] 
    :type srcVolumeID: int
    
    :param blocksPerSecond: [required] 
    :type blocksPerSecond: float
    
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


class LunAssignment(data_model.DataObject):
    """
    VolumeID and Lun assignment.
    :param volumeID: [required] The volume ID assigned to the Lun.
    :type volumeID: int
    
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


class VolumeAccessGroupLunAssignments(data_model.DataObject):
    """
    VolumeAccessGroup ID and Lun to be assigned to all volumes within it.
    :param volumeAccessGroupID: [required] Unique volume access group ID for which the LUN assignments will be modified.
    :type volumeAccessGroupID: int
    
    :param lunAssignments: [required] The volume IDs with assigned LUN values.
    :type lunAssignments: LunAssignment
    
    :param deletedLunAssignments: [required] The volume IDs with deleted LUN values.
    :type deletedLunAssignments: LunAssignment
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


class Platform(data_model.DataObject):
    """
    :param nodeType: [required] SolidFire&#x27;s name for this platform.
    :type nodeType: str
    
    :param chassisType: [required] Name of the chassis (example: &quot;R620&quot;).
    :type chassisType: str
    
    :param cpuModel: [required] The model of CPU used on this platform.
    :type cpuModel: str
    
    :param nodeMemoryGB: [required] The amount of memory on this platform in GiB.
    :type nodeMemoryGB: int
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


class Node(data_model.DataObject):
    """
    [&#x27;A node refers to an individual machine in a cluster.&#x27;, &#x27;Each active node hosts a master service, which is responsible for managing the drives and other services on its node.&#x27;, &#x27;After a node is made active, its drives will become available for addition to the cluster.&#x27;]
    [&#x27;A node refers to an individual machine in a cluster.&#x27;, &#x27;Each active node hosts a master service, which is responsible for managing the drives and other services on its node.&#x27;, &#x27;After a node is made active, its drives will become available for addition to the cluster.&#x27;]
    [&#x27;A node refers to an individual machine in a cluster.&#x27;, &#x27;Each active node hosts a master service, which is responsible for managing the drives and other services on its node.&#x27;, &#x27;After a node is made active, its drives will become available for addition to the cluster.&#x27;]
    :param nodeID: [required] [&#x27;The unique identifier for this node.&#x27;]
    :type nodeID: int
    
    :param associatedMasterServiceID: [required] [&#x27;The master service responsible for controlling other services on this node.&#x27;]
    :type associatedMasterServiceID: int
    
    :param associatedFServiceID: [required] 
    :type associatedFServiceID: int
    
    :param fibreChannelTargetPortGroup: [required] 
    :type fibreChannelTargetPortGroup: str
    
    :param name: [required] 
    :type name: str
    
    :param platformInfo: [required] Information about the platform this node is.
    :type platformInfo: Platform
    
    :param softwareVersion: [required] The version of SolidFire software this node is currently running.
    :type softwareVersion: str
    
    :param cip: [required] IP address used for both intra- and inter-cluster communication.
    :type cip: str
    
    :param cipi: [required] The machine&#x27;s name for the &quot;cip&quot; interface.
    :type cipi: str
    
    :param mip: [required] [&#x27;IP address used for cluster management (hosting the API and web site).&#x27;]
    :type mip: str
    
    :param mipi: [required] The machine&#x27;s name for the &quot;mip&quot; interface.
    :type mipi: str
    
    :param sip: [required] [&#x27;IP address used for iSCSI traffic.&#x27;]
    :type sip: str
    
    :param sipi: [required] The machine&#x27;s name for the &quot;sip&quot; interface.
    :type sipi: str
    
    :param uuid: [required] UUID of node.
    :type uuid: UUID
    
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
    attributes = data_model.property(
        "attributes", dict,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class PendingNode(data_model.DataObject):
    """
    [&#x27;A &quot;pending node&quot; is one that has not yet joined the cluster.&#x27;, &#x27;It can be added to a cluster using the AddNode method.&#x27;]
    [&#x27;A &quot;pending node&quot; is one that has not yet joined the cluster.&#x27;, &#x27;It can be added to a cluster using the AddNode method.&#x27;]
    :param pendingNodeID: [required] 
    :type pendingNodeID: int
    
    :param AssignedNodeID: [required] 
    :type AssignedNodeID: int
    
    :param name: [required] The host name for this node.
    :type name: str
    
    :param compatible: [required] 
    :type compatible: bool
    
    :param platformInfo: [required] Information about the platform this node is.
    :type platformInfo: Platform
    
    :param cip: [required] [&#x27;IP address used for both intra- and inter-cluster communication.&#x27;]
    :type cip: str
    
    :param cipi: [required] The machine&#x27;s name for the &quot;cip&quot; interface.
    :type cipi: str
    
    :param mip: [required] [&#x27;IP address used for cluster management (hosting the API and web site).&#x27;]
    :type mip: str
    
    :param mipi: [required] The machine&#x27;s name for the &quot;mip&quot; interface.
    :type mipi: str
    
    :param sip: [required] [&#x27;IP address used for iSCSI traffic.&#x27;]
    :type sip: str
    
    :param sipi: [required] The machine&#x27;s name for the &quot;sip&quot; interface.
    :type sipi: str
    
    :param softwareVersion: [required] The version of SolidFire software this node is currently running.
    :type softwareVersion: str
    
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


class ListAllNodesResult(data_model.DataObject):
    """
    :param nodes: [required] 
    :type nodes: Node
    
    :param pendingNodes: [required] 
    :type pendingNodes: PendingNode
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


class CreateVolumeAccessGroupResult(data_model.DataObject):
    """
    :param volumeAccessGroupID: [required] The ID for the newly-created volume access group.
    :type volumeAccessGroupID: int
    """
    volume_access_group_id = data_model.property(
        "volumeAccessGroupID", int,
        array=False, optional=False,
        documentation="The ID for the newly-created volume access group.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class DriveConfigInfo(data_model.DataObject):
    """
    :param canonicalName: [required] 
    :type canonicalName: str
    
    :param connected: [required] 
    :type connected: bool
    
    :param dev: [required] 
    :type dev: int
    
    :param devPath: [required] 
    :type devPath: str
    
    :param driveType: [required] 
    :type driveType: str
    
    :param fsType: [required] 
    :type fsType: str
    
    :param isMounted: [required] 
    :type isMounted: bool
    
    :param product: [required] 
    :type product: str
    
    :param mountPoint: [required] 
    :type mountPoint: str
    
    :param name: [required] 
    :type name: str
    
    :param path: [required] 
    :type path: str
    
    :param pathLink: [required] 
    :type pathLink: str
    
    :param scsiCompatId: [required] 
    :type scsiCompatId: str
    
    :param smartSsdWriteCapable: [required] 
    :type smartSsdWriteCapable: bool
    
    :param securityEnabled: [required] 
    :type securityEnabled: bool
    
    :param securityFrozen: [required] 
    :type securityFrozen: bool
    
    :param securityLocked: [required] 
    :type securityLocked: bool
    
    :param securitySupported: [required] 
    :type securitySupported: bool
    
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
    
    :param numBlockActual: [required] 
    :type numBlockActual: int
    
    :param numBlockExpected: [required] 
    :type numBlockExpected: int
    
    :param numSliceActual: [required] 
    :type numSliceActual: int
    
    :param numSliceExpected: [required] 
    :type numSliceExpected: int
    
    :param numTotalActual: [required] 
    :type numTotalActual: int
    
    :param numTotalExpected: [required] 
    :type numTotalExpected: int
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
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    is_mounted = data_model.property(
        "isMounted", bool,
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
    mount_point = data_model.property(
        "mountPoint", str,
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
    scsi_compat_id = data_model.property(
        "scsiCompatId", str,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    smart_ssd_write_capable = data_model.property(
        "smartSsdWriteCapable", bool,
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

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class AddressBlock(data_model.DataObject):
    """
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


class VirtualNetwork(data_model.DataObject):
    """
    :param virtualNetworkID: [required] SolidFire unique identifier for a virtual network.
    :type virtualNetworkID: int
    
    :param virtualNetworkTag: [required] VLAN Tag identifier.
    :type virtualNetworkTag: int
    
    :param addressBlocks: [required] [&#x27;Range of address blocks currently assigned to the virtual network.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;available:&lt;/b&gt; Binary string in &quot;1&quot;s and &quot;0&quot;s. 1 equals the IP is available and 0 equals the IP is not available. The string is read from right to left with the digit to the far right being the first IP address in the list of addressBlocks.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;size:&lt;/b&gt; the size of this block of addresses.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;start:&lt;/b&gt; first IP address in the block.&#x27;][&#x27;Range of address blocks currently assigned to the virtual network.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;available:&lt;/b&gt; Binary string in &quot;1&quot;s and &quot;0&quot;s. 1 equals the IP is available and 0 equals the IP is not available. The string is read from right to left with the digit to the far right being the first IP address in the list of addressBlocks.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;size:&lt;/b&gt; the size of this block of addresses.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;start:&lt;/b&gt; first IP address in the block.&#x27;][&#x27;Range of address blocks currently assigned to the virtual network.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;available:&lt;/b&gt; Binary string in &quot;1&quot;s and &quot;0&quot;s. 1 equals the IP is available and 0 equals the IP is not available. The string is read from right to left with the digit to the far right being the first IP address in the list of addressBlocks.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;size:&lt;/b&gt; the size of this block of addresses.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;start:&lt;/b&gt; first IP address in the block.&#x27;][&#x27;Range of address blocks currently assigned to the virtual network.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;available:&lt;/b&gt; Binary string in &quot;1&quot;s and &quot;0&quot;s. 1 equals the IP is available and 0 equals the IP is not available. The string is read from right to left with the digit to the far right being the first IP address in the list of addressBlocks.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;size:&lt;/b&gt; the size of this block of addresses.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;start:&lt;/b&gt; first IP address in the block.&#x27;]
    :type addressBlocks: AddressBlock
    
    :param name: [required] [&#x27;The name assigned to the virtual network.&#x27;]
    :type name: str
    
    :param netmask: [required] [&#x27;IP address of the netmask for the virtual network.&#x27;]
    :type netmask: str
    
    :param svip: [required] [&#x27;Storage IP address for the virtual network.&#x27;]
    :type svip: str
    
    :param gateway:  [&#x27;&#x27;]
    :type gateway: str
    
    :param namespace:  [&#x27;&#x27;]
    :type namespace: bool
    
    :param attributes: [required] [&#x27;List of Name/Value pairs in JSON object format.&#x27;]
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
        documentation="[&#x27;Range of address blocks currently assigned to the virtual network.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;available:&lt;/b&gt; Binary string in &quot;1&quot;s and &quot;0&quot;s. 1 equals the IP is available and 0 equals the IP is not available. The string is read from right to left with the digit to the far right being the first IP address in the list of addressBlocks.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;size:&lt;/b&gt; the size of this block of addresses.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;start:&lt;/b&gt; first IP address in the block.&#x27;]",
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
        documentation="[&#x27;&#x27;]",
        dictionaryType=None
    )
    namespace = data_model.property(
        "namespace", bool,
        array=False, optional=True,
        documentation="[&#x27;&#x27;]",
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
    """
    :param virtualNetworks: [required] Object containing virtual network IP addresses.
    :type virtualNetworks: VirtualNetwork
    """
    virtual_networks = data_model.property(
        "virtualNetworks", VirtualNetwork,
        array=True, optional=False,
        documentation="Object containing virtual network IP addresses.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class FibreChannelSession(data_model.DataObject):
    """
    FibreChannelSession contains information about each Fibre Channel session that is visible to the cluster and what target ports it is visible on.
    :param initiatorWWPN: [required] The WWPN of the initiator which is logged into the target port.
    :type initiatorWWPN: str
    
    :param nodeID: [required] The node owning the Fibre Channel session.
    :type nodeID: int
    
    :param serviceID: [required] The service ID of the FService owning this Fibre Channel session
    :type serviceID: int
    
    :param targetWWPN: [required] The WWPN of the target port involved in this session.
    :type targetWWPN: str
    
    :param volumeAccessGroupID: [required] The ID of the volume access group to which the initiatorWWPN belongs. If not in a volume access group, the value will be null.
    :type volumeAccessGroupID: int
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
        array=False, optional=False,
        documentation="The ID of the volume access group to which the initiatorWWPN belongs. If not in a volume access group, the value will be null.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class LoginSessionInfo(data_model.DataObject):
    """
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
    """
    :param loginSessionInfo: [required] [&#x27;The authentication expiration period. Formatted in H:mm:ss. For example: 1:30:00, 20:00, 5:00. All leading zeros and colons are removed regardless of the format the timeout was entered.&lt;br/&gt;&#x27;, &#x27;Objects returned are:&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;timeout&lt;/b&gt; - The time, in minutes, when this session will timeout and expire.&#x27;][&#x27;The authentication expiration period. Formatted in H:mm:ss. For example: 1:30:00, 20:00, 5:00. All leading zeros and colons are removed regardless of the format the timeout was entered.&lt;br/&gt;&#x27;, &#x27;Objects returned are:&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;timeout&lt;/b&gt; - The time, in minutes, when this session will timeout and expire.&#x27;][&#x27;The authentication expiration period. Formatted in H:mm:ss. For example: 1:30:00, 20:00, 5:00. All leading zeros and colons are removed regardless of the format the timeout was entered.&lt;br/&gt;&#x27;, &#x27;Objects returned are:&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;timeout&lt;/b&gt; - The time, in minutes, when this session will timeout and expire.&#x27;]
    :type loginSessionInfo: LoginSessionInfo
    """
    login_session_info = data_model.property(
        "loginSessionInfo", LoginSessionInfo,
        array=False, optional=False,
        documentation="[&#x27;The authentication expiration period. Formatted in H:mm:ss. For example: 1:30:00, 20:00, 5:00. All leading zeros and colons are removed regardless of the format the timeout was entered.&lt;br/&gt;&#x27;, &#x27;Objects returned are:&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;timeout&lt;/b&gt; - The time, in minutes, when this session will timeout and expire.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class EnableLdapAuthenticationResult(data_model.DataObject):
    """"""

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class EnableSnmpResult(data_model.DataObject):
    """"""

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class FibreChannelPortInfoResult(data_model.DataObject):
    """
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


class CHAPSecret(data_model.DataObject):
    """"""

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class ISCSISession(data_model.DataObject):
    """
    :param accountID: [required] 
    :type accountID: int
    
    :param accountName: [required] 
    :type accountName: str
    
    :param driveID: [required] 
    :type driveID: int
    
    :param initiatorIP: [required] 
    :type initiatorIP: str
    
    :param initiatorName: [required] 
    :type initiatorName: str
    
    :param nodeID: [required] 
    :type nodeID: int
    
    :param serviceID: [required] 
    :type serviceID: int
    
    :param sessionID: [required] 
    :type sessionID: int
    
    :param targetName: [required] 
    :type targetName: str
    
    :param targetIP: [required] 
    :type targetIP: str
    
    :param virtualNetworkID: [required] 
    :type virtualNetworkID: str
    
    :param volumeID: [required] 
    :type volumeID: int
    """
    account_id = data_model.property(
        "accountID", int,
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
        "virtualNetworkID", str,
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

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class ListISCSISessionsResult(data_model.DataObject):
    """
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


class PurgeDeletedVolumeResult(data_model.DataObject):
    """"""

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class SnapshotVirtualVolumeResult(data_model.DataObject):
    """
    :param volumeID: [required] The volume ID of the newly-created clone.
    :type volumeID: int
    
    :param snapshotID: [required] snapshotID for the prepared VVol snapshot.
    :type snapshotID: int
    
    :param virtualVolumeID: [required] virtualVolumeID for the newly created clone.
    :type virtualVolumeID: UUID
    """
    volume_id = data_model.property(
        "volumeID", int,
        array=False, optional=False,
        documentation="The volume ID of the newly-created clone.",
        dictionaryType=None
    )
    snapshot_id = data_model.property(
        "snapshotID", int,
        array=False, optional=False,
        documentation="snapshotID for the prepared VVol snapshot.",
        dictionaryType=None
    )
    virtual_volume_id = data_model.property(
        "virtualVolumeID", UUID,
        array=False, optional=False,
        documentation="virtualVolumeID for the newly created clone.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class ClusterInfo(data_model.DataObject):
    """
    Cluster Info object returns information the node uses to communicate with the cluster.
    :param attributes: [required] List of Name/Value pairs in JSON object format.
    :type attributes: dict
    
    :param encryptionAtRestState: [required] Encryption at rest state.
    :type encryptionAtRestState: str
    
    :param ensemble: [required] Array of Node IP addresses that are participating in the cluster.
    :type ensemble: str
    
    :param mvip: [required] Management network interface.
    :type mvip: str
    
    :param mvipNodeID: [required] Node holding the master MVIP address
    :type mvipNodeID: int
    
    :param name: [required] Unique cluster name.
    :type name: str
    
    :param repCount: [required] [&#x27;Number of replicas of each piece of data to store in the cluster.&#x27;, &#x27;Valid value is 2&#x27;][&#x27;Number of replicas of each piece of data to store in the cluster.&#x27;, &#x27;Valid value is 2&#x27;]
    :type repCount: int
    
    :param state: [required] 
    :type state: str
    
    :param svip: [required] Storage virtual IP
    :type svip: str
    
    :param svipNodeID: [required] Node holding the master SVIP address.
    :type svipNodeID: int
    
    :param uniqueID: [required] Unique ID for the cluster.
    :type uniqueID: str
    
    :param uuid: [required] 
    :type uuid: UUID
    """
    attributes = data_model.property(
        "attributes", dict,
        array=False, optional=False,
        documentation="List of Name/Value pairs in JSON object format.",
        dictionaryType=None
    )
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

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class GetClusterInfoResult(data_model.DataObject):
    """
    :param clusterInfo: [required] 
    :type clusterInfo: ClusterInfo
    """
    cluster_info = data_model.property(
        "clusterInfo", ClusterInfo,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class ListDatabaseChildrenResult(data_model.DataObject):
    """
    :param stat: [required] 
    :type stat: DatabaseStats
    
    :param children: [required] 
    :type children: str
    """
    stat = data_model.property(
        "stat", DatabaseStats,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    children = data_model.property(
        "children", str,
        array=True, optional=False,
        documentation="",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class SnmpNetwork(data_model.DataObject):
    """
    The SNMP network object contains information about SNMP configuration for the cluster nodes. SNMP v3 is supported on SolidFire clusters.
    :param access: [required] [&#x27;&lt;br/&gt;&lt;b&gt;ro&lt;/b&gt;: read-only access.*&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;rw&lt;/b&gt;: for read-write access.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;rosys&lt;/b&gt;: for read-only access to a restricted set of system information&#x27;, &#x27;*SolidFire recommends that all networks other than the default &quot;localhost&quot; be set to &quot;ro&quot; access, because all SolidFire MIB objects are read-only.&#x27;][&#x27;&lt;br/&gt;&lt;b&gt;ro&lt;/b&gt;: read-only access.*&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;rw&lt;/b&gt;: for read-write access.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;rosys&lt;/b&gt;: for read-only access to a restricted set of system information&#x27;, &#x27;*SolidFire recommends that all networks other than the default &quot;localhost&quot; be set to &quot;ro&quot; access, because all SolidFire MIB objects are read-only.&#x27;][&#x27;&lt;br/&gt;&lt;b&gt;ro&lt;/b&gt;: read-only access.*&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;rw&lt;/b&gt;: for read-write access.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;rosys&lt;/b&gt;: for read-only access to a restricted set of system information&#x27;, &#x27;*SolidFire recommends that all networks other than the default &quot;localhost&quot; be set to &quot;ro&quot; access, because all SolidFire MIB objects are read-only.&#x27;][&#x27;&lt;br/&gt;&lt;b&gt;ro&lt;/b&gt;: read-only access.*&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;rw&lt;/b&gt;: for read-write access.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;rosys&lt;/b&gt;: for read-only access to a restricted set of system information&#x27;, &#x27;*SolidFire recommends that all networks other than the default &quot;localhost&quot; be set to &quot;ro&quot; access, because all SolidFire MIB objects are read-only.&#x27;]
    :type access: str
    
    :param cidr: [required] [&#x27;A CIDR network mask. This network mask must be an integer greater than or equal to 0, and less than or equal to 32. It must also not be equal to 31.&#x27;]
    :type cidr: int
    
    :param community: [required] [&#x27;SNMP community string.&#x27;]
    :type community: str
    
    :param network: [required] [&#x27;This parameter along with the cidr variable is used to control which network the access and community string apply to. The special value of &quot;default&quot; is used to specify an entry that applies to all networks. The cidr mask is ignored when network value is either a host name or default.&#x27;]
    :type network: str
    """
    access = data_model.property(
        "access", str,
        array=False, optional=False,
        documentation="[&#x27;&lt;br/&gt;&lt;b&gt;ro&lt;/b&gt;: read-only access.*&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;rw&lt;/b&gt;: for read-write access.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;rosys&lt;/b&gt;: for read-only access to a restricted set of system information&#x27;, &#x27;*SolidFire recommends that all networks other than the default &quot;localhost&quot; be set to &quot;ro&quot; access, because all SolidFire MIB objects are read-only.&#x27;]",
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


class GetSnmpInfoResult(data_model.DataObject):
    """
    :param networks: [required] [&#x27;List of networks and access types enabled for SNMP.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Note&lt;/b&gt;: &quot;networks&quot; will only be present if SNMP V3 is disabled.&#x27;][&#x27;List of networks and access types enabled for SNMP.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Note&lt;/b&gt;: &quot;networks&quot; will only be present if SNMP V3 is disabled.&#x27;][&#x27;List of networks and access types enabled for SNMP.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Note&lt;/b&gt;: &quot;networks&quot; will only be present if SNMP V3 is disabled.&#x27;]
    :type networks: SnmpNetwork
    
    :param enabled: [required] If the nodes in the cluster are configured for SNMP.
    :type enabled: bool
    
    :param snmpV3Enabled: [required] If the nodes in the cluster are configured for SNMP v3.
    :type snmpV3Enabled: bool
    
    :param usmUsers: [required] If SNMP v3 is enabled, the values returned is a list of user access parameters for SNMP information from the cluster. This will be returned instead of the &quot;networks&quot; parameter.
    :type usmUsers: SnmpV3UsmUser
    """
    networks = data_model.property(
        "networks", SnmpNetwork,
        array=True, optional=False,
        documentation="[&#x27;List of networks and access types enabled for SNMP.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Note&lt;/b&gt;: &quot;networks&quot; will only be present if SNMP V3 is disabled.&#x27;]",
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


class DeleteDatabaseEntryResult(data_model.DataObject):
    """"""

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class ProtocolEndpoint(data_model.DataObject):
    """
    :param protocolEndpointID: [required] 
    :type protocolEndpointID: UUID
    
    :param protocolEndpointState: [required] 
    :type protocolEndpointState: str
    
    :param providerType: [required] 
    :type providerType: str
    
    :param primaryProviderID: [required] 
    :type primaryProviderID: int
    
    :param secondaryProviderID: [required] 
    :type secondaryProviderID: int
    
    :param scsiNAADeviceID: [required] 
    :type scsiNAADeviceID: str
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
    """
    :param protocolEndpoints: [required] 
    :type protocolEndpoints: ProtocolEndpoint
    """
    protocol_endpoints = data_model.property(
        "protocolEndpoints", ProtocolEndpoint,
        array=True, optional=False,
        documentation="",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class DeleteSnapshotResult(data_model.DataObject):
    """"""

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class BackupTarget(data_model.DataObject):
    """
    [&#x27;The object containing information about a backup target.&#x27;]
    :param name: [required] [&#x27;Name for the backup target.&#x27;]
    :type name: str
    
    :param backupTargetID: [required] [&#x27;Unique identifier assigned to the backup target.&#x27;]
    :type backupTargetID: int
    
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


class VolumeQOS(data_model.DataObject):
    """
    [&#x27;Quality of Service (QoS) Result values are used on SolidFire volumes to provision performance expectations.&#x27;]
    :param minIOPS: [required] [&#x27;Desired minimum 4KB IOPS to guarantee.&#x27;, &#x27;The allowed IOPS will only drop below this level if all volumes have been capped&#x27;, &#x27;at their min IOPS value and there is still insufficient performance capacity.&#x27;][&#x27;Desired minimum 4KB IOPS to guarantee.&#x27;, &#x27;The allowed IOPS will only drop below this level if all volumes have been capped&#x27;, &#x27;at their min IOPS value and there is still insufficient performance capacity.&#x27;][&#x27;Desired minimum 4KB IOPS to guarantee.&#x27;, &#x27;The allowed IOPS will only drop below this level if all volumes have been capped&#x27;, &#x27;at their min IOPS value and there is still insufficient performance capacity.&#x27;]
    :type minIOPS: int
    
    :param maxIOPS: [required] [&#x27;Desired maximum 4KB IOPS allowed over an extended period of time.&#x27;]
    :type maxIOPS: int
    
    :param burstIOPS: [required] [&#x27;Maximum &quot;peak&quot; 4KB IOPS allowed for short periods of time.&#x27;, &#x27;Allows for bursts of I/O activity over the normal max IOPS value.&#x27;][&#x27;Maximum &quot;peak&quot; 4KB IOPS allowed for short periods of time.&#x27;, &#x27;Allows for bursts of I/O activity over the normal max IOPS value.&#x27;]
    :type burstIOPS: int
    
    :param burstTime: [required] [&#x27;The length of time burst IOPS is allowed.&#x27;, &#x27;The value returned is represented in time units of seconds.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;Note&lt;/b&gt;: this value is calculated by the system based on IOPS set for QoS.&#x27;][&#x27;The length of time burst IOPS is allowed.&#x27;, &#x27;The value returned is represented in time units of seconds.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;Note&lt;/b&gt;: this value is calculated by the system based on IOPS set for QoS.&#x27;][&#x27;The length of time burst IOPS is allowed.&#x27;, &#x27;The value returned is represented in time units of seconds.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;Note&lt;/b&gt;: this value is calculated by the system based on IOPS set for QoS.&#x27;]
    :type burstTime: int
    
    :param curve: [required] [&#x27;The curve is a set of key-value pairs.&#x27;, &#x27;The keys are I/O sizes in bytes.&#x27;, &#x27;The values represent the cost performing an IOP at a specific I/O size.&#x27;, &#x27;The curve is calculated relative to a 4096 byte operation set at 100 IOPS.&#x27;][&#x27;The curve is a set of key-value pairs.&#x27;, &#x27;The keys are I/O sizes in bytes.&#x27;, &#x27;The values represent the cost performing an IOP at a specific I/O size.&#x27;, &#x27;The curve is calculated relative to a 4096 byte operation set at 100 IOPS.&#x27;][&#x27;The curve is a set of key-value pairs.&#x27;, &#x27;The keys are I/O sizes in bytes.&#x27;, &#x27;The values represent the cost performing an IOP at a specific I/O size.&#x27;, &#x27;The curve is calculated relative to a 4096 byte operation set at 100 IOPS.&#x27;][&#x27;The curve is a set of key-value pairs.&#x27;, &#x27;The keys are I/O sizes in bytes.&#x27;, &#x27;The values represent the cost performing an IOP at a specific I/O size.&#x27;, &#x27;The curve is calculated relative to a 4096 byte operation set at 100 IOPS.&#x27;]
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
        documentation="[&#x27;The length of time burst IOPS is allowed.&#x27;, &#x27;The value returned is represented in time units of seconds.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;Note&lt;/b&gt;: this value is calculated by the system based on IOPS set for QoS.&#x27;]",
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


class VirtualVolumeSyncResult(data_model.DataObject):
    """
    :param volumeID: [required] VolumeID for the newly created volume.
    :type volumeID: int
    
    :param virtualVolumeID: [required] virtualVolumeID for the newly created volume.
    :type virtualVolumeID: UUID
    """
    volume_id = data_model.property(
        "volumeID", int,
        array=False, optional=False,
        documentation="VolumeID for the newly created volume.",
        dictionaryType=None
    )
    virtual_volume_id = data_model.property(
        "virtualVolumeID", UUID,
        array=False, optional=False,
        documentation="virtualVolumeID for the newly created volume.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class ModifyVolumePairResult(data_model.DataObject):
    """"""

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class Snapshot(data_model.DataObject):
    """
    [&#x27;Snapshots is an object containing information about each snapshot made for a volume.&#x27;, &#x27;The return object includes information for the active snapshot as well as each snapshot created for the volume.&#x27;]
    [&#x27;Snapshots is an object containing information about each snapshot made for a volume.&#x27;, &#x27;The return object includes information for the active snapshot as well as each snapshot created for the volume.&#x27;]
    :param snapshotID: [required] Unique ID for this snapshot.
    :type snapshotID: int
    
    :param volumeID: [required] The volume this snapshot was taken of.
    :type volumeID: int
    
    :param name: [required] [&#x27;A name for this snapshot.&#x27;, &#x27;It is not necessarily unique.&#x27;][&#x27;A name for this snapshot.&#x27;, &#x27;It is not necessarily unique.&#x27;]
    :type name: str
    
    :param checksum: [required] [&#x27;A string that represents the correct digits in the stored snapshot.&#x27;, &#x27;This checksum can be used later to compare other snapshots to detect errors in the data.&#x27;][&#x27;A string that represents the correct digits in the stored snapshot.&#x27;, &#x27;This checksum can be used later to compare other snapshots to detect errors in the data.&#x27;]
    :type checksum: str
    
    :param enableRemoteReplication: [required] Identifies if snapshot is enabled for remote replication.
    :type enableRemoteReplication: bool
    
    :param expirationReason: [required] [&#x27;Indicates how the snapshot expiration was set. Possible values:&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;api&lt;/b&gt;: expiration time was set by using the API.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;none&lt;/b&gt;: there is no expiration time set.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;test&lt;/b&gt;: expiration time was set for testing.&#x27;][&#x27;Indicates how the snapshot expiration was set. Possible values:&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;api&lt;/b&gt;: expiration time was set by using the API.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;none&lt;/b&gt;: there is no expiration time set.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;test&lt;/b&gt;: expiration time was set for testing.&#x27;][&#x27;Indicates how the snapshot expiration was set. Possible values:&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;api&lt;/b&gt;: expiration time was set by using the API.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;none&lt;/b&gt;: there is no expiration time set.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;test&lt;/b&gt;: expiration time was set for testing.&#x27;][&#x27;Indicates how the snapshot expiration was set. Possible values:&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;api&lt;/b&gt;: expiration time was set by using the API.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;none&lt;/b&gt;: there is no expiration time set.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;test&lt;/b&gt;: expiration time was set for testing.&#x27;]
    :type expirationReason: str
    
    :param expirationTime: [required] The time at which this snapshot will expire and be purged from the cluster.
    :type expirationTime: str
    
    :param remoteStatuses: [required] [&#x27;Current remote status of the snapshot remoteStatus: Possible values:&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;Present&lt;/b&gt;: Snapshot exists on a remote cluster&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;Not Present&lt;/b&gt;: Snapshot does not exist on remote cluster&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;Syncing&lt;/b&gt;: This is a target cluster and it is currently replicating the snapshot&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;Deleted&lt;/b&gt;: This is a target cluster, the snapshot has been deleted, and it still exists on the source.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;volumePairUUID&lt;/b&gt;: universal identifier of the volume pair&#x27;][&#x27;Current remote status of the snapshot remoteStatus: Possible values:&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;Present&lt;/b&gt;: Snapshot exists on a remote cluster&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;Not Present&lt;/b&gt;: Snapshot does not exist on remote cluster&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;Syncing&lt;/b&gt;: This is a target cluster and it is currently replicating the snapshot&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;Deleted&lt;/b&gt;: This is a target cluster, the snapshot has been deleted, and it still exists on the source.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;volumePairUUID&lt;/b&gt;: universal identifier of the volume pair&#x27;][&#x27;Current remote status of the snapshot remoteStatus: Possible values:&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;Present&lt;/b&gt;: Snapshot exists on a remote cluster&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;Not Present&lt;/b&gt;: Snapshot does not exist on remote cluster&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;Syncing&lt;/b&gt;: This is a target cluster and it is currently replicating the snapshot&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;Deleted&lt;/b&gt;: This is a target cluster, the snapshot has been deleted, and it still exists on the source.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;volumePairUUID&lt;/b&gt;: universal identifier of the volume pair&#x27;][&#x27;Current remote status of the snapshot remoteStatus: Possible values:&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;Present&lt;/b&gt;: Snapshot exists on a remote cluster&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;Not Present&lt;/b&gt;: Snapshot does not exist on remote cluster&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;Syncing&lt;/b&gt;: This is a target cluster and it is currently replicating the snapshot&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;Deleted&lt;/b&gt;: This is a target cluster, the snapshot has been deleted, and it still exists on the source.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;volumePairUUID&lt;/b&gt;: universal identifier of the volume pair&#x27;][&#x27;Current remote status of the snapshot remoteStatus: Possible values:&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;Present&lt;/b&gt;: Snapshot exists on a remote cluster&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;Not Present&lt;/b&gt;: Snapshot does not exist on remote cluster&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;Syncing&lt;/b&gt;: This is a target cluster and it is currently replicating the snapshot&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;Deleted&lt;/b&gt;: This is a target cluster, the snapshot has been deleted, and it still exists on the source.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;volumePairUUID&lt;/b&gt;: universal identifier of the volume pair&#x27;][&#x27;Current remote status of the snapshot remoteStatus: Possible values:&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;Present&lt;/b&gt;: Snapshot exists on a remote cluster&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;Not Present&lt;/b&gt;: Snapshot does not exist on remote cluster&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;Syncing&lt;/b&gt;: This is a target cluster and it is currently replicating the snapshot&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;Deleted&lt;/b&gt;: This is a target cluster, the snapshot has been deleted, and it still exists on the source.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;volumePairUUID&lt;/b&gt;: universal identifier of the volume pair&#x27;]
    :type remoteStatuses: str
    
    :param status: [required] [&#x27;Current status of the snapshot&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;Preparing&lt;/b&gt;: A snapshot that is being prepared for use and is not yet writable.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;Done&lt;/b&gt;: A snapshot that has finished being prepared and is now usable.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;Active&lt;/b&gt;: This snapshot is the active branch.&#x27;][&#x27;Current status of the snapshot&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;Preparing&lt;/b&gt;: A snapshot that is being prepared for use and is not yet writable.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;Done&lt;/b&gt;: A snapshot that has finished being prepared and is now usable.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;Active&lt;/b&gt;: This snapshot is the active branch.&#x27;][&#x27;Current status of the snapshot&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;Preparing&lt;/b&gt;: A snapshot that is being prepared for use and is not yet writable.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;Done&lt;/b&gt;: A snapshot that has finished being prepared and is now usable.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;Active&lt;/b&gt;: This snapshot is the active branch.&#x27;][&#x27;Current status of the snapshot&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;Preparing&lt;/b&gt;: A snapshot that is being prepared for use and is not yet writable.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;Done&lt;/b&gt;: A snapshot that has finished being prepared and is now usable.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;Active&lt;/b&gt;: This snapshot is the active branch.&#x27;]
    :type status: str
    
    :param snapshotUUID: [required] Universal Unique ID of an existing snapshot.
    :type snapshotUUID: UUID
    
    :param totalSize: [required] [&#x27;Total size of this snapshot in bytes.&#x27;, &#x27;It is equivalent to totalSize of the volume when this snapshot was taken.&#x27;][&#x27;Total size of this snapshot in bytes.&#x27;, &#x27;It is equivalent to totalSize of the volume when this snapshot was taken.&#x27;]
    :type totalSize: int
    
    :param groupID:  [&#x27;If present, the ID of the group this snapshot is a part of.&#x27;, &#x27;If not present, this snapshot is not part of a group.&#x27;][&#x27;If present, the ID of the group this snapshot is a part of.&#x27;, &#x27;If not present, this snapshot is not part of a group.&#x27;]
    :type groupID: int
    
    :param groupSnapshotUUID: [required] [&#x27;The current &quot;members&quot; results contains information about each snapshot in the group.&#x27;, &#x27;Each of these members will have a &quot;uuid&quot; parameter for the snapshot\&#x27;s UUID.&#x27;][&#x27;The current &quot;members&quot; results contains information about each snapshot in the group.&#x27;, &#x27;Each of these members will have a &quot;uuid&quot; parameter for the snapshot\&#x27;s UUID.&#x27;]
    :type groupSnapshotUUID: UUID
    
    :param createTime: [required] The time this snapshot was taken.
    :type createTime: str
    
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
        documentation="[&#x27;Indicates how the snapshot expiration was set. Possible values:&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;api&lt;/b&gt;: expiration time was set by using the API.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;none&lt;/b&gt;: there is no expiration time set.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;test&lt;/b&gt;: expiration time was set for testing.&#x27;]",
        dictionaryType=None
    )
    expiration_time = data_model.property(
        "expirationTime", str,
        array=False, optional=False,
        documentation="The time at which this snapshot will expire and be purged from the cluster.",
        dictionaryType=None
    )
    remote_statuses = data_model.property(
        "remoteStatuses", str,
        array=False, optional=False,
        documentation="[&#x27;Current remote status of the snapshot remoteStatus: Possible values:&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;Present&lt;/b&gt;: Snapshot exists on a remote cluster&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;Not Present&lt;/b&gt;: Snapshot does not exist on remote cluster&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;Syncing&lt;/b&gt;: This is a target cluster and it is currently replicating the snapshot&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;Deleted&lt;/b&gt;: This is a target cluster, the snapshot has been deleted, and it still exists on the source.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;volumePairUUID&lt;/b&gt;: universal identifier of the volume pair&#x27;]",
        dictionaryType=None
    )
    status = data_model.property(
        "status", str,
        array=False, optional=False,
        documentation="[&#x27;Current status of the snapshot&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;Preparing&lt;/b&gt;: A snapshot that is being prepared for use and is not yet writable.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;Done&lt;/b&gt;: A snapshot that has finished being prepared and is now usable.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;Active&lt;/b&gt;: This snapshot is the active branch.&#x27;]",
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
    attributes = data_model.property(
        "attributes", dict,
        array=False, optional=False,
        documentation="List of Name/Value pairs in JSON object format.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class ListVolumeStatsByAccountResult(data_model.DataObject):
    """
    :param volumeStats: [required] [&#x27;List of account activity information.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;Note&lt;/b&gt;: The volumeID member is 0 for each entry, as the values represent the summation of all volumes owned by the account.&#x27;][&#x27;List of account activity information.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;Note&lt;/b&gt;: The volumeID member is 0 for each entry, as the values represent the summation of all volumes owned by the account.&#x27;]
    :type volumeStats: VolumeStats
    """
    volume_stats = data_model.property(
        "volumeStats", VolumeStats,
        array=True, optional=False,
        documentation="[&#x27;List of account activity information.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;Note&lt;/b&gt;: The volumeID member is 0 for each entry, as the values represent the summation of all volumes owned by the account.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class ModifyClusterAdminResult(data_model.DataObject):
    """"""

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class DeleteVolumeResult(data_model.DataObject):
    """"""

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class CreateClusterSupportBundleResult(data_model.DataObject):
    """
    :param details: [required] [&quot;The details of the support bundle. Values returned in &#x27;details&#x27;:&quot;, &quot;&lt;br/&gt;&lt;b&gt;bundleName&lt;/b&gt;- The name specified in the &#x27;CreateSupportBundle API method. If no name was specified, &#x27;supportbundle&#x27; will be used.&quot;, &#x27;&lt;br/&gt;&lt;b&gt;extraArgs&lt;/b&gt;- The arguments passed with this method.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;files&lt;/b&gt;- A list of the support bundle files that were created.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;output&lt;/b&gt;- The command line output from the script that creates the support bundle.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;timeoutSec&lt;/b&gt;- The timeout specified for the support bundle creation process.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;url&lt;/b&gt;- URL to the support bundle created.&#x27;][&quot;The details of the support bundle. Values returned in &#x27;details&#x27;:&quot;, &quot;&lt;br/&gt;&lt;b&gt;bundleName&lt;/b&gt;- The name specified in the &#x27;CreateSupportBundle API method. If no name was specified, &#x27;supportbundle&#x27; will be used.&quot;, &#x27;&lt;br/&gt;&lt;b&gt;extraArgs&lt;/b&gt;- The arguments passed with this method.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;files&lt;/b&gt;- A list of the support bundle files that were created.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;output&lt;/b&gt;- The command line output from the script that creates the support bundle.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;timeoutSec&lt;/b&gt;- The timeout specified for the support bundle creation process.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;url&lt;/b&gt;- URL to the support bundle created.&#x27;][&quot;The details of the support bundle. Values returned in &#x27;details&#x27;:&quot;, &quot;&lt;br/&gt;&lt;b&gt;bundleName&lt;/b&gt;- The name specified in the &#x27;CreateSupportBundle API method. If no name was specified, &#x27;supportbundle&#x27; will be used.&quot;, &#x27;&lt;br/&gt;&lt;b&gt;extraArgs&lt;/b&gt;- The arguments passed with this method.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;files&lt;/b&gt;- A list of the support bundle files that were created.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;output&lt;/b&gt;- The command line output from the script that creates the support bundle.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;timeoutSec&lt;/b&gt;- The timeout specified for the support bundle creation process.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;url&lt;/b&gt;- URL to the support bundle created.&#x27;][&quot;The details of the support bundle. Values returned in &#x27;details&#x27;:&quot;, &quot;&lt;br/&gt;&lt;b&gt;bundleName&lt;/b&gt;- The name specified in the &#x27;CreateSupportBundle API method. If no name was specified, &#x27;supportbundle&#x27; will be used.&quot;, &#x27;&lt;br/&gt;&lt;b&gt;extraArgs&lt;/b&gt;- The arguments passed with this method.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;files&lt;/b&gt;- A list of the support bundle files that were created.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;output&lt;/b&gt;- The command line output from the script that creates the support bundle.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;timeoutSec&lt;/b&gt;- The timeout specified for the support bundle creation process.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;url&lt;/b&gt;- URL to the support bundle created.&#x27;][&quot;The details of the support bundle. Values returned in &#x27;details&#x27;:&quot;, &quot;&lt;br/&gt;&lt;b&gt;bundleName&lt;/b&gt;- The name specified in the &#x27;CreateSupportBundle API method. If no name was specified, &#x27;supportbundle&#x27; will be used.&quot;, &#x27;&lt;br/&gt;&lt;b&gt;extraArgs&lt;/b&gt;- The arguments passed with this method.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;files&lt;/b&gt;- A list of the support bundle files that were created.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;output&lt;/b&gt;- The command line output from the script that creates the support bundle.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;timeoutSec&lt;/b&gt;- The timeout specified for the support bundle creation process.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;url&lt;/b&gt;- URL to the support bundle created.&#x27;][&quot;The details of the support bundle. Values returned in &#x27;details&#x27;:&quot;, &quot;&lt;br/&gt;&lt;b&gt;bundleName&lt;/b&gt;- The name specified in the &#x27;CreateSupportBundle API method. If no name was specified, &#x27;supportbundle&#x27; will be used.&quot;, &#x27;&lt;br/&gt;&lt;b&gt;extraArgs&lt;/b&gt;- The arguments passed with this method.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;files&lt;/b&gt;- A list of the support bundle files that were created.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;output&lt;/b&gt;- The command line output from the script that creates the support bundle.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;timeoutSec&lt;/b&gt;- The timeout specified for the support bundle creation process.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;url&lt;/b&gt;- URL to the support bundle created.&#x27;][&quot;The details of the support bundle. Values returned in &#x27;details&#x27;:&quot;, &quot;&lt;br/&gt;&lt;b&gt;bundleName&lt;/b&gt;- The name specified in the &#x27;CreateSupportBundle API method. If no name was specified, &#x27;supportbundle&#x27; will be used.&quot;, &#x27;&lt;br/&gt;&lt;b&gt;extraArgs&lt;/b&gt;- The arguments passed with this method.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;files&lt;/b&gt;- A list of the support bundle files that were created.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;output&lt;/b&gt;- The command line output from the script that creates the support bundle.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;timeoutSec&lt;/b&gt;- The timeout specified for the support bundle creation process.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;url&lt;/b&gt;- URL to the support bundle created.&#x27;]
    :type details: dict
    
    :param duration: [required] [&#x27;The amount of time required to create the support bundle in the format HH:MM:SS.ssssss&#x27;]
    :type duration: str
    
    :param result: [required] [&#x27;Whether the support bundle creation passed of failed.&#x27;]
    :type result: str
    """
    details = data_model.property(
        "details", dict,
        array=False, optional=False,
        documentation="[&quot;The details of the support bundle. Values returned in &#x27;details&#x27;:&quot;, &quot;&lt;br/&gt;&lt;b&gt;bundleName&lt;/b&gt;- The name specified in the &#x27;CreateSupportBundle API method. If no name was specified, &#x27;supportbundle&#x27; will be used.&quot;, &#x27;&lt;br/&gt;&lt;b&gt;extraArgs&lt;/b&gt;- The arguments passed with this method.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;files&lt;/b&gt;- A list of the support bundle files that were created.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;output&lt;/b&gt;- The command line output from the script that creates the support bundle.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;timeoutSec&lt;/b&gt;- The timeout specified for the support bundle creation process.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;url&lt;/b&gt;- URL to the support bundle created.&#x27;]",
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


class VirtualVolumeHostResult(data_model.DataObject):
    """
    :param host: [required] 
    :type host: VirtualVolumeHost
    """
    host = data_model.property(
        "host", VirtualVolumeHost,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class Frequency(data_model.DataObject):
    """"""

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class AddedNode(data_model.DataObject):
    """
    :param nodeID: [required] 
    :type nodeID: int
    
    :param pendingNodeID: [required] 
    :type pendingNodeID: int
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


class EnableFeatureResult(data_model.DataObject):
    """"""

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class TestConnectMvipDetails(data_model.DataObject):
    """
    :param pingBytes: [required] Details of the ping tests with 56 Bytes and 1500 Bytes.
    :type pingBytes: str
    
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


class DriveInfo(data_model.DataObject):
    """
    :param capacity: [required] [&#x27;Total capacity of the drive, in bytes.&#x27;]
    :type capacity: int
    
    :param driveID: [required] DriveID for this drive.
    :type driveID: int
    
    :param nodeID: [required] NodeID where this drive is located.
    :type nodeID: int
    
    :param serial: [required] Drive serial number.
    :type serial: str
    
    :param slot: [required] Slot number in the server chassis where this drive is located, or -1 if SATADimm used for internal metadata drive.
    :type slot: int
    
    :param status: [required] 
    :type status: str
    
    :param type: [required] 
    :type type: str
    
    :param attributes: [required] [&#x27;List of Name/Value pairs in JSON object format.&#x27;]
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


class AddVirtualNetworkResult(data_model.DataObject):
    """
    :param virtualNetworkID: [required] The virtual network ID of the new virtual network.
    :type virtualNetworkID: int
    """
    virtual_network_id = data_model.property(
        "virtualNetworkID", int,
        array=False, optional=False,
        documentation="The virtual network ID of the new virtual network.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class SetLoginSessionInfoResult(data_model.DataObject):
    """"""

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class VolumeAccessGroup(data_model.DataObject):
    """
    [&#x27;A volume access group is a useful way of grouping volumes and initiators together for ease of management.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;Volume Access Group Limits:&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;- A volume access group can contain up to sixty-four initiator IQNs.&#x27;, &#x27;- An initiator can only belong to only one volume access group.&#x27;, &#x27;- A volume access group can contain up to two thousand volumes.&#x27;, &#x27;- Each volume access group can belong to a maximum of four other volume access groups.&#x27;]
    [&#x27;A volume access group is a useful way of grouping volumes and initiators together for ease of management.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;Volume Access Group Limits:&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;- A volume access group can contain up to sixty-four initiator IQNs.&#x27;, &#x27;- An initiator can only belong to only one volume access group.&#x27;, &#x27;- A volume access group can contain up to two thousand volumes.&#x27;, &#x27;- Each volume access group can belong to a maximum of four other volume access groups.&#x27;]
    [&#x27;A volume access group is a useful way of grouping volumes and initiators together for ease of management.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;Volume Access Group Limits:&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;- A volume access group can contain up to sixty-four initiator IQNs.&#x27;, &#x27;- An initiator can only belong to only one volume access group.&#x27;, &#x27;- A volume access group can contain up to two thousand volumes.&#x27;, &#x27;- Each volume access group can belong to a maximum of four other volume access groups.&#x27;]
    [&#x27;A volume access group is a useful way of grouping volumes and initiators together for ease of management.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;Volume Access Group Limits:&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;- A volume access group can contain up to sixty-four initiator IQNs.&#x27;, &#x27;- An initiator can only belong to only one volume access group.&#x27;, &#x27;- A volume access group can contain up to two thousand volumes.&#x27;, &#x27;- Each volume access group can belong to a maximum of four other volume access groups.&#x27;]
    [&#x27;A volume access group is a useful way of grouping volumes and initiators together for ease of management.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;Volume Access Group Limits:&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;- A volume access group can contain up to sixty-four initiator IQNs.&#x27;, &#x27;- An initiator can only belong to only one volume access group.&#x27;, &#x27;- A volume access group can contain up to two thousand volumes.&#x27;, &#x27;- Each volume access group can belong to a maximum of four other volume access groups.&#x27;]
    [&#x27;A volume access group is a useful way of grouping volumes and initiators together for ease of management.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;Volume Access Group Limits:&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;- A volume access group can contain up to sixty-four initiator IQNs.&#x27;, &#x27;- An initiator can only belong to only one volume access group.&#x27;, &#x27;- A volume access group can contain up to two thousand volumes.&#x27;, &#x27;- Each volume access group can belong to a maximum of four other volume access groups.&#x27;]
    [&#x27;A volume access group is a useful way of grouping volumes and initiators together for ease of management.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;Volume Access Group Limits:&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;- A volume access group can contain up to sixty-four initiator IQNs.&#x27;, &#x27;- An initiator can only belong to only one volume access group.&#x27;, &#x27;- A volume access group can contain up to two thousand volumes.&#x27;, &#x27;- Each volume access group can belong to a maximum of four other volume access groups.&#x27;]
    [&#x27;A volume access group is a useful way of grouping volumes and initiators together for ease of management.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;Volume Access Group Limits:&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;- A volume access group can contain up to sixty-four initiator IQNs.&#x27;, &#x27;- An initiator can only belong to only one volume access group.&#x27;, &#x27;- A volume access group can contain up to two thousand volumes.&#x27;, &#x27;- Each volume access group can belong to a maximum of four other volume access groups.&#x27;]
    :param volumeAccessGroupID: [required] Unique ID for this volume access group.
    :type volumeAccessGroupID: int
    
    :param name: [required] Name of the volume access group.
    :type name: str
    
    :param initiators: [required] List of unique initiator names belonging to the volume access group.
    :type initiators: str
    
    :param volumes: [required] List of volumes belonging to the volume access group.
    :type volumes: int
    """
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

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class GetAPIResult(data_model.DataObject):
    """
    :param currentVersion: [required] 
    :type currentVersion: float
    
    :param supportedVersions: [required] 
    :type supportedVersions: float
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


class NodeWaitingToJoin(data_model.DataObject):
    """
    :param name: [required] 
    :type name: str
    
    :param version: [required] 
    :type version: str
    
    :param nodeID: [required] 
    :type nodeID: int
    
    :param pendingNodeID: [required] 
    :type pendingNodeID: int
    
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


class GetClusterFullThresholdResult(data_model.DataObject):
    """
    :param blockFullness: [required] [&#x27;Current computed level of block fullness of the cluster.&#x27;, &#x27;Possible values: &lt;br/&gt;&lt;b&gt;stage1Happy&lt;/b&gt;: No alerts or error conditions. &lt;br/&gt;&lt;b&gt;stage2Aware&lt;/b&gt;: 3 nodes of capacity available. &lt;br/&gt;&lt;b&gt;stage3Low&lt;/b&gt;: 2 nodes of capacity available. &lt;br/&gt;&lt;b&gt;stage4Critical&lt;/b&gt;: 1 node of capacity available. No new volumes or clones can be created. &lt;br/&gt;&lt;b&gt;stage5CompletelyConsumed&lt;/b&gt;: Completely consumed. Cluster is read-only, iSCSI connection is maintained but all writes are suspended.&#x27;][&#x27;Current computed level of block fullness of the cluster.&#x27;, &#x27;Possible values: &lt;br/&gt;&lt;b&gt;stage1Happy&lt;/b&gt;: No alerts or error conditions. &lt;br/&gt;&lt;b&gt;stage2Aware&lt;/b&gt;: 3 nodes of capacity available. &lt;br/&gt;&lt;b&gt;stage3Low&lt;/b&gt;: 2 nodes of capacity available. &lt;br/&gt;&lt;b&gt;stage4Critical&lt;/b&gt;: 1 node of capacity available. No new volumes or clones can be created. &lt;br/&gt;&lt;b&gt;stage5CompletelyConsumed&lt;/b&gt;: Completely consumed. Cluster is read-only, iSCSI connection is maintained but all writes are suspended.&#x27;]
    :type blockFullness: str
    
    :param fullness: [required] Reflects the highest level of fullness between &quot;blockFullness&quot; and &quot;metadataFullness&quot;.
    :type fullness: str
    
    :param maxMetadataOverProvisionFactor: [required] A value representative of the number of times metadata space can be over provisioned relative to the amount of space available. For example, if there was enough metadata space to store 100 TiB of volumes and this number was set to 5, then 500 TiB worth of volumes could be created.
    :type maxMetadataOverProvisionFactor: int
    
    :param metadataFullness: [required] Current computed level of metadata fullness of the cluster.
    :type metadataFullness: str
    
    :param sliceReserveUsedThresholdPct: [required] Error condition; message sent to &quot;Alerts&quot; if the reserved slice utilization is greater than the sliceReserveUsedThresholdPct value returned.
    :type sliceReserveUsedThresholdPct: int
    
    :param stage2AwareThreshold: [required] Awareness condition: Value that is set for &quot;Stage 2&quot; cluster threshold level.
    :type stage2AwareThreshold: int
    
    :param stage2BlockThresholdBytes: [required] Number of bytes being used by the cluster at which a stage2 condition will exist.
    :type stage2BlockThresholdBytes: int
    
    :param stage3BlockThresholdBytes: [required] Number of bytes being used by the cluster at which a stage3 condition will exist.
    :type stage3BlockThresholdBytes: int
    
    :param stage3BlockThresholdPercent: [required] The percent value set for stage3. At this percent full, a warning will be posted in the Alerts log.
    :type stage3BlockThresholdPercent: int
    
    :param stage3LowThreshold: [required] Error condition; message sent to &quot;Alerts&quot; that capacity on a cluster is getting low.
    :type stage3LowThreshold: int
    
    :param stage4CriticalThreshold: [required] Error condition; message sent to &quot;Alerts&quot; that capacity on a cluster is critically low.
    :type stage4CriticalThreshold: int
    
    :param stage4BlockThresholdBytes: [required] Number of bytes being used by the cluster at which a stage4 condition will exist.
    :type stage4BlockThresholdBytes: int
    
    :param stage5BlockThresholdBytes: [required] Number of bytes being used by the cluster at which a stage5 condition will exist.
    :type stage5BlockThresholdBytes: int
    
    :param sumTotalClusterBytes: [required] Physical capacity of the cluster measured in bytes.
    :type sumTotalClusterBytes: int
    
    :param sumTotalMetadataClusterBytes: [required] Total amount of space that can be used to store metadata.
    :type sumTotalMetadataClusterBytes: int
    
    :param sumUsedClusterBytes: [required] Number of bytes used on the cluster.
    :type sumUsedClusterBytes: int
    
    :param sumUsedMetadataClusterBytes: [required] Amount of space used on volume drives to store metadata.
    :type sumUsedMetadataClusterBytes: int
    """
    block_fullness = data_model.property(
        "blockFullness", str,
        array=False, optional=False,
        documentation="[&#x27;Current computed level of block fullness of the cluster.&#x27;, &#x27;Possible values: &lt;br/&gt;&lt;b&gt;stage1Happy&lt;/b&gt;: No alerts or error conditions. &lt;br/&gt;&lt;b&gt;stage2Aware&lt;/b&gt;: 3 nodes of capacity available. &lt;br/&gt;&lt;b&gt;stage3Low&lt;/b&gt;: 2 nodes of capacity available. &lt;br/&gt;&lt;b&gt;stage4Critical&lt;/b&gt;: 1 node of capacity available. No new volumes or clones can be created. &lt;br/&gt;&lt;b&gt;stage5CompletelyConsumed&lt;/b&gt;: Completely consumed. Cluster is read-only, iSCSI connection is maintained but all writes are suspended.&#x27;]",
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


class NodeStatsInfo(data_model.DataObject):
    """
    :param cBytesIn: [required] Bytes in on the cluster interface.
    :type cBytesIn: int
    
    :param cBytesOut: [required] Bytes out on the cluster interface.
    :type cBytesOut: int
    
    :param cpu: [required] CPU Usage %
    :type cpu: int
    
    :param mBytesIn: [required] Bytes in on the management interface.
    :type mBytesIn: int
    
    :param mBytesOut: [required] Bytes out on the management interface.
    :type mBytesOut: int
    
    :param networkUtilizationCluster: [required] Network interface utilization (in %) for the cluster network interface.
    :type networkUtilizationCluster: int
    
    :param networkUtilizationStorage: [required] Network interface utilization (in %) for the storage network interface.
    :type networkUtilizationStorage: int
    
    :param nodeID: [required] 
    :type nodeID: int
    
    :param sBytesIn: [required] Bytes in on the storage interface.
    :type sBytesIn: int
    
    :param sBytesOut: [required] Bytes out on the storage interface.
    :type sBytesOut: int
    
    :param timestamp: [required] Current time in UTC format ISO 8691 date string.
    :type timestamp: str
    
    :param usedMemory: [required] Total memory usage in bytes.
    :type usedMemory: int
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


class NodeStatsNodes(data_model.DataObject):
    """
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


class GroupSnapshotMembers(data_model.DataObject):
    """
    List of checksum, volumeIDs and snapshotIDs for each member of the group.
    :param volumeID: [required] The source volume ID for the snapshot.
    :type volumeID: int
    
    :param snapshotID: [required] [&#x27;Unique ID of a snapshot from which the new snapshot is made.&#x27;, &#x27;The snapshotID passed must be a snapshot on the given volume.&#x27;][&#x27;Unique ID of a snapshot from which the new snapshot is made.&#x27;, &#x27;The snapshotID passed must be a snapshot on the given volume.&#x27;]
    :type snapshotID: int
    
    :param snapshotUUID: [required] Universal Unique ID of an existing snapshot.
    :type snapshotUUID: str
    
    :param checksum: [required] [&#x27;A string that represents the correct digits in the stored snapshot.&#x27;, &#x27;This checksum can be used later to compare other snapshots to detect errors in the data.&#x27;][&#x27;A string that represents the correct digits in the stored snapshot.&#x27;, &#x27;This checksum can be used later to compare other snapshots to detect errors in the data.&#x27;]
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
    """
    [&#x27;Group Snapshot object represents a point-in-time copy of a group of volumes.&#x27;]
    :param groupSnapshotID: [required] Unique ID of the new group snapshot.
    :type groupSnapshotID: int
    
    :param groupSnapshotUUID: [required] UUID of the group snapshot.
    :type groupSnapshotUUID: UUID
    
    :param members: [required] List of volumeIDs and snapshotIDs for each member of the group.
    :type members: GroupSnapshotMembers
    
    :param name: [required] Name of the group snapshot, or, if none was given, the UTC formatted day and time on which the snapshot was created.
    :type name: str
    
    :param createTime: [required] The UTC formatted day and time on which the snapshot was created.
    :type createTime: str
    
    :param status: [required] [&#x27;Status of the snapshot.&#x27;, &#x27;Possible values:&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;Preparing&lt;/b&gt;: A snapshot that is being prepared for use and is not yet writable.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;Done&lt;/b&gt;: A snapshot that has finished being prepared and is now usable&#x27;][&#x27;Status of the snapshot.&#x27;, &#x27;Possible values:&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;Preparing&lt;/b&gt;: A snapshot that is being prepared for use and is not yet writable.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;Done&lt;/b&gt;: A snapshot that has finished being prepared and is now usable&#x27;][&#x27;Status of the snapshot.&#x27;, &#x27;Possible values:&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;Preparing&lt;/b&gt;: A snapshot that is being prepared for use and is not yet writable.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;Done&lt;/b&gt;: A snapshot that has finished being prepared and is now usable&#x27;][&#x27;Status of the snapshot.&#x27;, &#x27;Possible values:&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;Preparing&lt;/b&gt;: A snapshot that is being prepared for use and is not yet writable.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;Done&lt;/b&gt;: A snapshot that has finished being prepared and is now usable&#x27;]
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
        documentation="[&#x27;Status of the snapshot.&#x27;, &#x27;Possible values:&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;Preparing&lt;/b&gt;: A snapshot that is being prepared for use and is not yet writable.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;Done&lt;/b&gt;: A snapshot that has finished being prepared and is now usable&#x27;]",
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


class GetClusterMasterNodeIDResult(data_model.DataObject):
    """
    :param nodeID: [required] ID of the master node.
    :type nodeID: int
    """
    node_id = data_model.property(
        "nodeID", int,
        array=False, optional=False,
        documentation="ID of the master node.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class SetSnmpTrapInfoResult(data_model.DataObject):
    """"""

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class QoS(data_model.DataObject):
    """
    [&#x27;Quality of Service (QoS) values are used on SolidFire volumes to provision performance expectations.&#x27;, &#x27;Minimum, maximum and burst QoS values can be set within the ranges specified in the QoS table below.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;Volumes created without specified QoS values are created with the Default values listed below.&#x27;, &#x27;Default values can be found by running the GetDefaultQoS method.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;minIOPS&lt;/b&gt; Min: 100/50 (v7.0/v8.0), Default: 100, Max: 15,000&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;maxIOPS&lt;/b&gt; Min: 100/50 (v7.0/v8.0), Default: 15,000, Max: 100,000&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;burstIOPS&lt;/b&gt; Min: 100/50 (v7.0/v8.0), Default: 15,000, Max: 100,000&lt;br/&gt;&#x27;]
    [&#x27;Quality of Service (QoS) values are used on SolidFire volumes to provision performance expectations.&#x27;, &#x27;Minimum, maximum and burst QoS values can be set within the ranges specified in the QoS table below.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;Volumes created without specified QoS values are created with the Default values listed below.&#x27;, &#x27;Default values can be found by running the GetDefaultQoS method.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;minIOPS&lt;/b&gt; Min: 100/50 (v7.0/v8.0), Default: 100, Max: 15,000&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;maxIOPS&lt;/b&gt; Min: 100/50 (v7.0/v8.0), Default: 15,000, Max: 100,000&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;burstIOPS&lt;/b&gt; Min: 100/50 (v7.0/v8.0), Default: 15,000, Max: 100,000&lt;br/&gt;&#x27;]
    [&#x27;Quality of Service (QoS) values are used on SolidFire volumes to provision performance expectations.&#x27;, &#x27;Minimum, maximum and burst QoS values can be set within the ranges specified in the QoS table below.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;Volumes created without specified QoS values are created with the Default values listed below.&#x27;, &#x27;Default values can be found by running the GetDefaultQoS method.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;minIOPS&lt;/b&gt; Min: 100/50 (v7.0/v8.0), Default: 100, Max: 15,000&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;maxIOPS&lt;/b&gt; Min: 100/50 (v7.0/v8.0), Default: 15,000, Max: 100,000&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;burstIOPS&lt;/b&gt; Min: 100/50 (v7.0/v8.0), Default: 15,000, Max: 100,000&lt;br/&gt;&#x27;]
    [&#x27;Quality of Service (QoS) values are used on SolidFire volumes to provision performance expectations.&#x27;, &#x27;Minimum, maximum and burst QoS values can be set within the ranges specified in the QoS table below.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;Volumes created without specified QoS values are created with the Default values listed below.&#x27;, &#x27;Default values can be found by running the GetDefaultQoS method.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;minIOPS&lt;/b&gt; Min: 100/50 (v7.0/v8.0), Default: 100, Max: 15,000&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;maxIOPS&lt;/b&gt; Min: 100/50 (v7.0/v8.0), Default: 15,000, Max: 100,000&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;burstIOPS&lt;/b&gt; Min: 100/50 (v7.0/v8.0), Default: 15,000, Max: 100,000&lt;br/&gt;&#x27;]
    [&#x27;Quality of Service (QoS) values are used on SolidFire volumes to provision performance expectations.&#x27;, &#x27;Minimum, maximum and burst QoS values can be set within the ranges specified in the QoS table below.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;Volumes created without specified QoS values are created with the Default values listed below.&#x27;, &#x27;Default values can be found by running the GetDefaultQoS method.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;minIOPS&lt;/b&gt; Min: 100/50 (v7.0/v8.0), Default: 100, Max: 15,000&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;maxIOPS&lt;/b&gt; Min: 100/50 (v7.0/v8.0), Default: 15,000, Max: 100,000&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;burstIOPS&lt;/b&gt; Min: 100/50 (v7.0/v8.0), Default: 15,000, Max: 100,000&lt;br/&gt;&#x27;]
    [&#x27;Quality of Service (QoS) values are used on SolidFire volumes to provision performance expectations.&#x27;, &#x27;Minimum, maximum and burst QoS values can be set within the ranges specified in the QoS table below.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;Volumes created without specified QoS values are created with the Default values listed below.&#x27;, &#x27;Default values can be found by running the GetDefaultQoS method.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;minIOPS&lt;/b&gt; Min: 100/50 (v7.0/v8.0), Default: 100, Max: 15,000&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;maxIOPS&lt;/b&gt; Min: 100/50 (v7.0/v8.0), Default: 15,000, Max: 100,000&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;burstIOPS&lt;/b&gt; Min: 100/50 (v7.0/v8.0), Default: 15,000, Max: 100,000&lt;br/&gt;&#x27;]
    [&#x27;Quality of Service (QoS) values are used on SolidFire volumes to provision performance expectations.&#x27;, &#x27;Minimum, maximum and burst QoS values can be set within the ranges specified in the QoS table below.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;Volumes created without specified QoS values are created with the Default values listed below.&#x27;, &#x27;Default values can be found by running the GetDefaultQoS method.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;minIOPS&lt;/b&gt; Min: 100/50 (v7.0/v8.0), Default: 100, Max: 15,000&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;maxIOPS&lt;/b&gt; Min: 100/50 (v7.0/v8.0), Default: 15,000, Max: 100,000&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;burstIOPS&lt;/b&gt; Min: 100/50 (v7.0/v8.0), Default: 15,000, Max: 100,000&lt;br/&gt;&#x27;]
    [&#x27;Quality of Service (QoS) values are used on SolidFire volumes to provision performance expectations.&#x27;, &#x27;Minimum, maximum and burst QoS values can be set within the ranges specified in the QoS table below.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;Volumes created without specified QoS values are created with the Default values listed below.&#x27;, &#x27;Default values can be found by running the GetDefaultQoS method.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;minIOPS&lt;/b&gt; Min: 100/50 (v7.0/v8.0), Default: 100, Max: 15,000&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;maxIOPS&lt;/b&gt; Min: 100/50 (v7.0/v8.0), Default: 15,000, Max: 100,000&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;burstIOPS&lt;/b&gt; Min: 100/50 (v7.0/v8.0), Default: 15,000, Max: 100,000&lt;br/&gt;&#x27;]
    [&#x27;Quality of Service (QoS) values are used on SolidFire volumes to provision performance expectations.&#x27;, &#x27;Minimum, maximum and burst QoS values can be set within the ranges specified in the QoS table below.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;Volumes created without specified QoS values are created with the Default values listed below.&#x27;, &#x27;Default values can be found by running the GetDefaultQoS method.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;minIOPS&lt;/b&gt; Min: 100/50 (v7.0/v8.0), Default: 100, Max: 15,000&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;maxIOPS&lt;/b&gt; Min: 100/50 (v7.0/v8.0), Default: 15,000, Max: 100,000&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;burstIOPS&lt;/b&gt; Min: 100/50 (v7.0/v8.0), Default: 15,000, Max: 100,000&lt;br/&gt;&#x27;]
    :param minIOPS:  [&#x27;Desired minimum 4KB IOPS to guarantee.&#x27;, &#x27;The allowed IOPS will only drop below this level if all volumes have been capped&#x27;, &#x27;at their minimum IOPS value and there is still insufficient performance capacity.&#x27;][&#x27;Desired minimum 4KB IOPS to guarantee.&#x27;, &#x27;The allowed IOPS will only drop below this level if all volumes have been capped&#x27;, &#x27;at their minimum IOPS value and there is still insufficient performance capacity.&#x27;][&#x27;Desired minimum 4KB IOPS to guarantee.&#x27;, &#x27;The allowed IOPS will only drop below this level if all volumes have been capped&#x27;, &#x27;at their minimum IOPS value and there is still insufficient performance capacity.&#x27;]
    :type minIOPS: int
    
    :param maxIOPS:  [&#x27;Desired maximum 4KB IOPS allowed over an extended period of time.&#x27;]
    :type maxIOPS: int
    
    :param burstIOPS:  [&#x27;Maximum &quot;peak&quot; 4KB IOPS allowed for short periods of time.&#x27;, &#x27;Allows for bursts of I/O activity over the normal max IOPS value.&#x27;][&#x27;Maximum &quot;peak&quot; 4KB IOPS allowed for short periods of time.&#x27;, &#x27;Allows for bursts of I/O activity over the normal max IOPS value.&#x27;]
    :type burstIOPS: int
    
    :param burstTime:  [&#x27;The length of time burst IOPS is allowed.&#x27;, &#x27;The value returned is represented in time units of seconds.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;Note&lt;/b&gt;: this value is calculated by the system based on IOPS set for QoS.&#x27;][&#x27;The length of time burst IOPS is allowed.&#x27;, &#x27;The value returned is represented in time units of seconds.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;Note&lt;/b&gt;: this value is calculated by the system based on IOPS set for QoS.&#x27;][&#x27;The length of time burst IOPS is allowed.&#x27;, &#x27;The value returned is represented in time units of seconds.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;Note&lt;/b&gt;: this value is calculated by the system based on IOPS set for QoS.&#x27;]
    :type burstTime: int
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
        documentation="[&#x27;The length of time burst IOPS is allowed.&#x27;, &#x27;The value returned is represented in time units of seconds.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;Note&lt;/b&gt;: this value is calculated by the system based on IOPS set for QoS.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class AddNodesResult(data_model.DataObject):
    """
    :param nodes: [required] An array of objects mapping the previous &quot;pendingNodeID&quot; to the &quot;nodeID&quot;.
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


class VirtualVolumeBitmapResult(data_model.DataObject):
    """
    :param bitmap: [required] The b64 bitmap.
    :type bitmap: str
    
    :param segmentLength: [required] Byte length, adjusted to end on a chunk boundary.
    :type segmentLength: int
    """
    bitmap = data_model.property(
        "bitmap", str,
        array=False, optional=False,
        documentation="The b64 bitmap.",
        dictionaryType=None
    )
    segment_length = data_model.property(
        "segmentLength", int,
        array=False, optional=False,
        documentation="Byte length, adjusted to end on a chunk boundary.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class SetNetworkConfigResult(data_model.DataObject):
    """
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


class VirtualVolumeInfo(data_model.DataObject):
    """
    :param virtualVolumeID: [required] 
    :type virtualVolumeID: UUID
    
    :param parentVirtualVolumeID: [required] 
    :type parentVirtualVolumeID: UUID
    
    :param storageContainerID: [required] 
    :type storageContainerID: UUID
    
    :param volumeID: [required] 
    :type volumeID: int
    
    :param snapshotID: [required] 
    :type snapshotID: int
    
    :param virtualVolumeType: [required] 
    :type virtualVolumeType: str
    
    :param status: [required] 
    :type status: str
    
    :param bindings: [required] 
    :type bindings: int
    
    :param children: [required] 
    :type children: UUID
    
    :param metadata: [required] 
    :type metadata: dict
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

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class ResetDriveDetails(data_model.DataObject):
    """
    :param drive: [required] Drive name
    :type drive: str
    
    :param returnCode: [required] 
    :type returnCode: int
    
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
    """
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
    """
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


class TestPingResult(data_model.DataObject):
    """
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


class ListPendingNodesResult(data_model.DataObject):
    """
    :param pendingNodes: [required] 
    :type pendingNodes: PendingNode
    """
    pending_nodes = data_model.property(
        "pendingNodes", PendingNode,
        array=True, optional=False,
        documentation="",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class GetLimitsResult(data_model.DataObject):
    """
    Limits for the cluster
    :param accountCountMax: [required] 
    :type accountCountMax: int
    
    :param accountNameLengthMax: [required] 
    :type accountNameLengthMax: int
    
    :param accountNameLengthMin: [required] 
    :type accountNameLengthMin: int
    
    :param bulkVolumeJobsPerNodeMax: [required] 
    :type bulkVolumeJobsPerNodeMax: int
    
    :param bulkVolumeJobsPerVolumeMax: [required] 
    :type bulkVolumeJobsPerVolumeMax: int
    
    :param cloneJobsPerVolumeMax: [required] 
    :type cloneJobsPerVolumeMax: int
    
    :param clusterPairsCountMax: [required] 
    :type clusterPairsCountMax: int
    
    :param initiatorNameLengthMax: [required] 
    :type initiatorNameLengthMax: int
    
    :param initiatorsPerVolumeAccessGroupCountMax: [required] 
    :type initiatorsPerVolumeAccessGroupCountMax: int
    
    :param secretLengthMax: [required] 
    :type secretLengthMax: int
    
    :param secretLengthMin: [required] 
    :type secretLengthMin: int
    
    :param snapshotNameLengthMax: [required] 
    :type snapshotNameLengthMax: int
    
    :param snapshotsPerVolumeMax: [required] 
    :type snapshotsPerVolumeMax: int
    
    :param volumeAccessGroupCountMax: [required] 
    :type volumeAccessGroupCountMax: int
    
    :param volumeAccessGroupLunMax: [required] 
    :type volumeAccessGroupLunMax: int
    
    :param volumeAccessGroupNameLengthMax: [required] 
    :type volumeAccessGroupNameLengthMax: int
    
    :param volumeAccessGroupNameLengthMin: [required] 
    :type volumeAccessGroupNameLengthMin: int
    
    :param volumeAccessGroupsPerInitiatorCountMax: [required] 
    :type volumeAccessGroupsPerInitiatorCountMax: int
    
    :param volumeAccessGroupsPerVolumeCountMax: [required] 
    :type volumeAccessGroupsPerVolumeCountMax: int
    
    :param volumeBurstIOPSMax: [required] 
    :type volumeBurstIOPSMax: int
    
    :param volumeBurstIOPSMin: [required] 
    :type volumeBurstIOPSMin: int
    
    :param volumeCountMax: [required] 
    :type volumeCountMax: int
    
    :param volumeMaxIOPSMax: [required] 
    :type volumeMaxIOPSMax: int
    
    :param volumeMaxIOPSMin: [required] 
    :type volumeMaxIOPSMin: int
    
    :param volumeMinIOPSMax: [required] 
    :type volumeMinIOPSMax: int
    
    :param volumeMinIOPSMin: [required] 
    :type volumeMinIOPSMin: int
    
    :param volumeNameLengthMax: [required] 
    :type volumeNameLengthMax: int
    
    :param volumeNameLengthMin: [required] 
    :type volumeNameLengthMin: int
    
    :param volumeSizeMax: [required] 
    :type volumeSizeMax: int
    
    :param volumeSizeMin: [required] 
    :type volumeSizeMin: int
    
    :param volumesPerAccountCountMax: [required] 
    :type volumesPerAccountCountMax: int
    
    :param volumesPerGroupSnapshotMax: [required] 
    :type volumesPerGroupSnapshotMax: int
    
    :param volumesPerVolumeAccessGroupCountMax: [required] 
    :type volumesPerVolumeAccessGroupCountMax: int
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
    initiators_per_volume_access_group_count_max = data_model.property(
        "initiatorsPerVolumeAccessGroupCountMax", int,
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


class CreateClusterResult(data_model.DataObject):
    """"""

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class ListSnapshotsResult(data_model.DataObject):
    """
    :param snapshots: [required] [&#x27;Information about each snapshot for each volume.&#x27;, &#x27;If volumeID is not provided, all snapshots for all volumes is returned.&#x27;, &#x27;Snapshots that are in a group will be returned with a &quot;groupID&quot;.&#x27;, &#x27;Snapshots that are enabled for replication.&#x27;][&#x27;Information about each snapshot for each volume.&#x27;, &#x27;If volumeID is not provided, all snapshots for all volumes is returned.&#x27;, &#x27;Snapshots that are in a group will be returned with a &quot;groupID&quot;.&#x27;, &#x27;Snapshots that are enabled for replication.&#x27;][&#x27;Information about each snapshot for each volume.&#x27;, &#x27;If volumeID is not provided, all snapshots for all volumes is returned.&#x27;, &#x27;Snapshots that are in a group will be returned with a &quot;groupID&quot;.&#x27;, &#x27;Snapshots that are enabled for replication.&#x27;][&#x27;Information about each snapshot for each volume.&#x27;, &#x27;If volumeID is not provided, all snapshots for all volumes is returned.&#x27;, &#x27;Snapshots that are in a group will be returned with a &quot;groupID&quot;.&#x27;, &#x27;Snapshots that are enabled for replication.&#x27;]
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


class ScheduleInfo(data_model.DataObject):
    """
    :param volumeIDs:  A list of volume IDs to be included in the group snapshot.
    :type volumeIDs: int
    
    :param snapshotName:  The snapshot name to be used. 
    :type snapshotName: str
    
    :param enableRemoteReplication:  Indicates if the snapshot should be included in remote replication.
    :type enableRemoteReplication: bool
    
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
    """
    Schedule is an object containing information about each schedule created to autonomously make a snapshot of a volume. The return object includes information for all schedules. If scheduleID is used to identify a specific schedule then only information for that scheduleID is returned. Schedules information is returned with the API method, see ListSchedules on the SolidFire API guide page 245.
    :param frequency: [required] [&#x27;Indicates the frequency of the schedule occurrence. Set this to a type that inherits from Frequency.&lt;br/&gt;&#x27;, &#x27;Valid types are:&lt;br/&gt;&#x27;, &#x27;DayOfWeekFrequency&lt;br/&gt;&#x27;, &#x27;DayOfMonthFrequency&lt;br/&gt;&#x27;, &#x27;TimeIntervalFrequency&#x27;][&#x27;Indicates the frequency of the schedule occurrence. Set this to a type that inherits from Frequency.&lt;br/&gt;&#x27;, &#x27;Valid types are:&lt;br/&gt;&#x27;, &#x27;DayOfWeekFrequency&lt;br/&gt;&#x27;, &#x27;DayOfMonthFrequency&lt;br/&gt;&#x27;, &#x27;TimeIntervalFrequency&#x27;][&#x27;Indicates the frequency of the schedule occurrence. Set this to a type that inherits from Frequency.&lt;br/&gt;&#x27;, &#x27;Valid types are:&lt;br/&gt;&#x27;, &#x27;DayOfWeekFrequency&lt;br/&gt;&#x27;, &#x27;DayOfMonthFrequency&lt;br/&gt;&#x27;, &#x27;TimeIntervalFrequency&#x27;][&#x27;Indicates the frequency of the schedule occurrence. Set this to a type that inherits from Frequency.&lt;br/&gt;&#x27;, &#x27;Valid types are:&lt;br/&gt;&#x27;, &#x27;DayOfWeekFrequency&lt;br/&gt;&#x27;, &#x27;DayOfMonthFrequency&lt;br/&gt;&#x27;, &#x27;TimeIntervalFrequency&#x27;][&#x27;Indicates the frequency of the schedule occurrence. Set this to a type that inherits from Frequency.&lt;br/&gt;&#x27;, &#x27;Valid types are:&lt;br/&gt;&#x27;, &#x27;DayOfWeekFrequency&lt;br/&gt;&#x27;, &#x27;DayOfMonthFrequency&lt;br/&gt;&#x27;, &#x27;TimeIntervalFrequency&#x27;]
    :type frequency: Frequency
    
    :param hasError:  [&#x27;Indicates whether or not the schedule has errors.&#x27;]
    :type hasError: bool
    
    :param lastRunStatus: [required] [&#x27;Indicates the status of the last scheduled snapshot.&lt;br/&gt;&#x27;, &#x27;Valid values are:&lt;br/&gt;&#x27;, &#x27;Success&lt;br/&gt;&#x27;, &#x27;Failed&#x27;][&#x27;Indicates the status of the last scheduled snapshot.&lt;br/&gt;&#x27;, &#x27;Valid values are:&lt;br/&gt;&#x27;, &#x27;Success&lt;br/&gt;&#x27;, &#x27;Failed&#x27;][&#x27;Indicates the status of the last scheduled snapshot.&lt;br/&gt;&#x27;, &#x27;Valid values are:&lt;br/&gt;&#x27;, &#x27;Success&lt;br/&gt;&#x27;, &#x27;Failed&#x27;][&#x27;Indicates the status of the last scheduled snapshot.&lt;br/&gt;&#x27;, &#x27;Valid values are:&lt;br/&gt;&#x27;, &#x27;Success&lt;br/&gt;&#x27;, &#x27;Failed&#x27;]
    :type lastRunStatus: str
    
    :param lastRunTimeStart: [required] [&#x27;Indicates the last time the schedule started n ISO 8601 date string.&#x27;, &#x27;Valid values are:&lt;br/&gt;&#x27;, &#x27;Success&lt;br/&gt;&#x27;, &#x27;Failed&#x27;][&#x27;Indicates the last time the schedule started n ISO 8601 date string.&#x27;, &#x27;Valid values are:&lt;br/&gt;&#x27;, &#x27;Success&lt;br/&gt;&#x27;, &#x27;Failed&#x27;][&#x27;Indicates the last time the schedule started n ISO 8601 date string.&#x27;, &#x27;Valid values are:&lt;br/&gt;&#x27;, &#x27;Success&lt;br/&gt;&#x27;, &#x27;Failed&#x27;][&#x27;Indicates the last time the schedule started n ISO 8601 date string.&#x27;, &#x27;Valid values are:&lt;br/&gt;&#x27;, &#x27;Success&lt;br/&gt;&#x27;, &#x27;Failed&#x27;]
    :type lastRunTimeStart: str
    
    :param paused:  [&#x27;Indicates whether or not the schedule is paused.&#x27;]
    :type paused: bool
    
    :param recurring:  [&#x27;Indicates whether or not the schedule is recurring.&#x27;]
    :type recurring: bool
    
    :param runNextInterval:  [&#x27;Indicates whether or not the schedule will run the next time the scheduler is active. When set to &quot;true&quot;, the schedule will run the next time the scheduler is active and then reset back to &quot;false&quot;.&#x27;]
    :type runNextInterval: bool
    
    :param scheduleID:  [&#x27;Unique ID of the schedule&#x27;]
    :type scheduleID: int
    
    :param scheduleInfo: [required] [&#x27;Includes the unique name given to the schedule, the retention period for the snapshot that was created, and the volume ID of the volume from which the snapshot was created.&#x27;]
    :type scheduleInfo: ScheduleInfo
    
    :param name: [required] [&#x27;Unique name assigned to the schedule.&#x27;]
    :type name: str
    
    :param startingDate: [required] [&#x27;Indicates the date the first time the schedule began of will begin. Formatted in UTC time.&#x27;]
    :type startingDate: str
    
    :param toBeDeleted:  [&#x27;Indicates if the schedule is marked for deletion.&#x27;]
    :type toBeDeleted: bool
    """
    frequency = data_model.property(
        "frequency", Frequency,
        array=False, optional=False,
        documentation="[&#x27;Indicates the frequency of the schedule occurrence. Set this to a type that inherits from Frequency.&lt;br/&gt;&#x27;, &#x27;Valid types are:&lt;br/&gt;&#x27;, &#x27;DayOfWeekFrequency&lt;br/&gt;&#x27;, &#x27;DayOfMonthFrequency&lt;br/&gt;&#x27;, &#x27;TimeIntervalFrequency&#x27;]",
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
        documentation="[&#x27;Indicates the status of the last scheduled snapshot.&lt;br/&gt;&#x27;, &#x27;Valid values are:&lt;br/&gt;&#x27;, &#x27;Success&lt;br/&gt;&#x27;, &#x27;Failed&#x27;]",
        dictionaryType=None
    )
    last_run_time_start = data_model.property(
        "lastRunTimeStart", str,
        array=False, optional=False,
        documentation="[&#x27;Indicates the last time the schedule started n ISO 8601 date string.&#x27;, &#x27;Valid values are:&lt;br/&gt;&#x27;, &#x27;Success&lt;br/&gt;&#x27;, &#x27;Failed&#x27;]",
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


class TestConnectEnsembleDetails(data_model.DataObject):
    """
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


class ListActiveNodesResult(data_model.DataObject):
    """
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


class GetNodeHardwareInfoResult(data_model.DataObject):
    """
    :param nodeHardwareInfo: [required] Hardware information for the specified nodeID.
    :type nodeHardwareInfo: dict
    """
    node_hardware_info = data_model.property(
        "nodeHardwareInfo", dict,
        array=False, optional=False,
        documentation="Hardware information for the specified nodeID.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class DeleteGroupSnapshotResult(data_model.DataObject):
    """"""

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class BulkVolumeJob(data_model.DataObject):
    """
    :param bulkVolumeID: [required] The internal bulk volume job ID.
    :type bulkVolumeID: int
    
    :param createTime: [required] Timestamp created for the bulk volume job.
    :type createTime: str
    
    :param elapsedTime: [required] The number of seconds since the job began.
    :type elapsedTime: int
    
    :param format: [required] Format is either &quot;compressed&quot; or &quot;native&quot;.
    :type format: str
    
    :param key: [required] The unique key created by the bulk volume session.
    :type key: str
    
    :param percentComplete: [required] The completed percentage reported by the operation.
    :type percentComplete: int
    
    :param remainingTime: [required] The estimated time remaining in seconds.
    :type remainingTime: int
    
    :param srcVolumeID: [required] The source volume ID.
    :type srcVolumeID: int
    
    :param status: [required] [&#x27;Can be one of the following:&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;preparing&lt;/b&gt;&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;active&lt;/b&gt;&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;done&lt;/b&gt;&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;failed&lt;/b&gt;&#x27;][&#x27;Can be one of the following:&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;preparing&lt;/b&gt;&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;active&lt;/b&gt;&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;done&lt;/b&gt;&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;failed&lt;/b&gt;&#x27;][&#x27;Can be one of the following:&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;preparing&lt;/b&gt;&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;active&lt;/b&gt;&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;done&lt;/b&gt;&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;failed&lt;/b&gt;&#x27;][&#x27;Can be one of the following:&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;preparing&lt;/b&gt;&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;active&lt;/b&gt;&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;done&lt;/b&gt;&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;failed&lt;/b&gt;&#x27;][&#x27;Can be one of the following:&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;preparing&lt;/b&gt;&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;active&lt;/b&gt;&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;done&lt;/b&gt;&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;failed&lt;/b&gt;&#x27;]
    :type status: str
    
    :param script: [required] The name of the script if one is provided.
    :type script: str
    
    :param snapshotID: [required] ID of the snapshot if a snapshot is in the source of the bulk volume job.
    :type snapshotID: int
    
    :param type: [required] [&#x27;Can be one of the following:&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;read&lt;/b&gt;&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;write&lt;/b&gt;&#x27;][&#x27;Can be one of the following:&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;read&lt;/b&gt;&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;write&lt;/b&gt;&#x27;][&#x27;Can be one of the following:&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;read&lt;/b&gt;&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;write&lt;/b&gt;&#x27;]
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
        documentation="[&#x27;Can be one of the following:&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;preparing&lt;/b&gt;&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;active&lt;/b&gt;&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;done&lt;/b&gt;&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;failed&lt;/b&gt;&#x27;]",
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
        documentation="[&#x27;Can be one of the following:&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;read&lt;/b&gt;&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;write&lt;/b&gt;&#x27;]",
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
    """
    :param bulkVolumeJobs: [required] An array of information for each bulk volume job.
    :type bulkVolumeJobs: BulkVolumeJob
    """
    bulk_volume_jobs = data_model.property(
        "bulkVolumeJobs", BulkVolumeJob,
        array=True, optional=False,
        documentation="An array of information for each bulk volume job.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class DrivesConfigInfo(data_model.DataObject):
    """
    :param drives: [required] 
    :type drives: DriveConfigInfo
    """
    drives = data_model.property(
        "drives", DriveConfigInfo,
        array=True, optional=False,
        documentation="",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class GetVolumeStatsResult(data_model.DataObject):
    """
    :param volumeStats: [required] Volume activity information.
    :type volumeStats: VolumeStats
    """
    volume_stats = data_model.property(
        "volumeStats", VolumeStats,
        array=False, optional=False,
        documentation="Volume activity information.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class RemoveVirtualNetworkResult(data_model.DataObject):
    """"""

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class AsyncHandleResult(data_model.DataObject):
    """
    :param asyncHandle: [required] 
    :type asyncHandle: int
    """
    async_handle = data_model.property(
        "asyncHandle", int,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class TestConnectMvipResult(data_model.DataObject):
    """
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


class ModifyGroupSnapshotResult(data_model.DataObject):
    """"""

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class VirtualVolumeBinding(data_model.DataObject):
    """
    :param protocolEndpointID: [required] The unique ID of the protocol endpoint.
    :type protocolEndpointID: UUID
    
    :param protocolEndpointInBandID: [required] The scsiNAADeviceID of the protocol endpoint. For more information, see protocolEndpoint.
    :type protocolEndpointInBandID: str
    
    :param protocolEndpointType: [required] The type of protocol endpoint. SCSI is the only value returned for the protocol endpoint type.
    :type protocolEndpointType: str
    
    :param virtualVolumeBindingID: [required] The unique ID of the virtual volume binding object.
    :type virtualVolumeBindingID: int
    
    :param virtualVolumeHostID: [required] The unique ID of the virtual volume host.
    :type virtualVolumeHostID: UUID
    
    :param virtualVolumeID: [required] The unique ID of the virtual volume.
    :type virtualVolumeID: UUID
    
    :param virtualVolumeSecondaryID: [required] The secondary ID of the virtual volume.
    :type virtualVolumeSecondaryID: str
    
    :param virtualVolume: [required] An object describing the bound volume or snapshot.
    :type virtualVolume: VirtualVolumeInfo
    
    :param protocolEndpoint: [required] An object describing the protocol endpoint to which the virtual volume is bound.
    :type protocolEndpoint: UUID
    
    :param virtualVolumeHost: [required] An object describing the host to which this binding corresponds.
    :type virtualVolumeHost: VirtualVolumeHost
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
    """
    :param bindings: [required] Describes the VVol &lt;-&gt; Host binding.
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


class PrepareVirtualSnapshotResult(data_model.DataObject):
    """
    :param virtualVolumeTaskID: [required] The ID of the clone task.
    :type virtualVolumeTaskID: UUID
    
    :param volumeID: [required] The volume ID of the newly-created clone.
    :type volumeID: int
    
    :param snapshotID: [required] snapshotID for the prepared VVol snapshot.
    :type snapshotID: int
    
    :param virtualVolumeID: [required] virtualVolumeID for the newly created clone.
    :type virtualVolumeID: UUID
    """
    virtual_volume_task_id = data_model.property(
        "virtualVolumeTaskID", UUID,
        array=False, optional=False,
        documentation="The ID of the clone task.",
        dictionaryType=None
    )
    volume_id = data_model.property(
        "volumeID", int,
        array=False, optional=False,
        documentation="The volume ID of the newly-created clone.",
        dictionaryType=None
    )
    snapshot_id = data_model.property(
        "snapshotID", int,
        array=False, optional=False,
        documentation="snapshotID for the prepared VVol snapshot.",
        dictionaryType=None
    )
    virtual_volume_id = data_model.property(
        "virtualVolumeID", UUID,
        array=False, optional=False,
        documentation="virtualVolumeID for the newly created clone.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class GetPendingOperationResult(data_model.DataObject):
    """
    :param pendingOperation: [required] 
    :type pendingOperation: PendingOperation
    """
    pending_operation = data_model.property(
        "pendingOperation", PendingOperation,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class VasaProviderInfoResult(data_model.DataObject):
    """
    :param vasaProviderInfo: [required] 
    :type vasaProviderInfo: VasaProviderInfo
    """
    vasa_provider_info = data_model.property(
        "vasaProviderInfo", VasaProviderInfo,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class TestLdapAuthenticationResult(data_model.DataObject):
    """
    :param groups: [required] [&#x27;List of LDAP groups that the tested user is a member of.&#x27;]
    :type groups: str
    
    :param userDN: [required] [&quot;The tested user&#x27;s full LDAP distinguished name.&quot;]
    :type userDN: str
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


class ModifyClusterFullThresholdResult(data_model.DataObject):
    """
    :param blockFullness: [required] [&#x27;Current computed level of block fullness of the cluster.&#x27;, &#x27;Possible values: &lt;br/&gt;&lt;b&gt;stage1Happy&lt;/b&gt;: No alerts or error conditions. &lt;br/&gt;&lt;b&gt;stage2Aware&lt;/b&gt;: 3 nodes of capacity available. &lt;br/&gt;&lt;b&gt;stage3Low&lt;/b&gt;: 2 nodes of capacity available. &lt;br/&gt;&lt;b&gt;stage4Critical&lt;/b&gt;: 1 node of capacity available. No new volumes or clones can be created. &lt;br/&gt;&lt;b&gt;stage5CompletelyConsumed&lt;/b&gt;: Completely consumed. Cluster is read-only, iSCSI connection is maintained but all writes are suspended.&#x27;][&#x27;Current computed level of block fullness of the cluster.&#x27;, &#x27;Possible values: &lt;br/&gt;&lt;b&gt;stage1Happy&lt;/b&gt;: No alerts or error conditions. &lt;br/&gt;&lt;b&gt;stage2Aware&lt;/b&gt;: 3 nodes of capacity available. &lt;br/&gt;&lt;b&gt;stage3Low&lt;/b&gt;: 2 nodes of capacity available. &lt;br/&gt;&lt;b&gt;stage4Critical&lt;/b&gt;: 1 node of capacity available. No new volumes or clones can be created. &lt;br/&gt;&lt;b&gt;stage5CompletelyConsumed&lt;/b&gt;: Completely consumed. Cluster is read-only, iSCSI connection is maintained but all writes are suspended.&#x27;]
    :type blockFullness: str
    
    :param fullness: [required] Reflects the highest level of fullness between &quot;blockFullness&quot; and &quot;metadataFullness&quot;.
    :type fullness: str
    
    :param maxMetadataOverProvisionFactor: [required] A value representative of the number of times metadata space can be over provisioned relative to the amount of space available. For example, if there was enough metadata space to store 100 TiB of volumes and this number was set to 5, then 500 TiB worth of volumes could be created.
    :type maxMetadataOverProvisionFactor: int
    
    :param metadataFullness: [required] Current computed level of metadata fullness of the cluster.
    :type metadataFullness: str
    
    :param sliceReserveUsedThresholdPct: [required] Error condition; message sent to &quot;Alerts&quot; if the reserved slice utilization is greater than the sliceReserveUsedThresholdPct value returned.
    :type sliceReserveUsedThresholdPct: int
    
    :param stage2AwareThreshold: [required] Awareness condition: Value that is set for &quot;Stage 2&quot; cluster threshold level.
    :type stage2AwareThreshold: int
    
    :param stage2BlockThresholdBytes: [required] Number of bytes being used by the cluster at which a stage2 condition will exist.
    :type stage2BlockThresholdBytes: int
    
    :param stage3BlockThresholdBytes: [required] Number of bytes being used by the cluster at which a stage3 condition will exist.
    :type stage3BlockThresholdBytes: int
    
    :param stage3BlockThresholdPercent: [required] The percent value set for stage3. At this percent full, a warning will be posted in the Alerts log.
    :type stage3BlockThresholdPercent: int
    
    :param stage3LowThreshold: [required] Error condition; message sent to &quot;Alerts&quot; that capacity on a cluster is getting low.
    :type stage3LowThreshold: int
    
    :param stage4CriticalThreshold: [required] Error condition; message sent to &quot;Alerts&quot; that capacity on a cluster is critically low.
    :type stage4CriticalThreshold: int
    
    :param stage4BlockThresholdBytes: [required] Number of bytes being used by the cluster at which a stage4 condition will exist.
    :type stage4BlockThresholdBytes: int
    
    :param stage5BlockThresholdBytes: [required] Number of bytes being used by the cluster at which a stage5 condition will exist.
    :type stage5BlockThresholdBytes: int
    
    :param sumTotalClusterBytes: [required] Physical capacity of the cluster measured in bytes.
    :type sumTotalClusterBytes: int
    
    :param sumTotalMetadataClusterBytes: [required] Total amount of space that can be used to store metadata.
    :type sumTotalMetadataClusterBytes: int
    
    :param sumUsedClusterBytes: [required] Number of bytes used on the cluster.
    :type sumUsedClusterBytes: int
    
    :param sumUsedMetadataClusterBytes: [required] Amount of space used on volume drives to store metadata.
    :type sumUsedMetadataClusterBytes: int
    """
    block_fullness = data_model.property(
        "blockFullness", str,
        array=False, optional=False,
        documentation="[&#x27;Current computed level of block fullness of the cluster.&#x27;, &#x27;Possible values: &lt;br/&gt;&lt;b&gt;stage1Happy&lt;/b&gt;: No alerts or error conditions. &lt;br/&gt;&lt;b&gt;stage2Aware&lt;/b&gt;: 3 nodes of capacity available. &lt;br/&gt;&lt;b&gt;stage3Low&lt;/b&gt;: 2 nodes of capacity available. &lt;br/&gt;&lt;b&gt;stage4Critical&lt;/b&gt;: 1 node of capacity available. No new volumes or clones can be created. &lt;br/&gt;&lt;b&gt;stage5CompletelyConsumed&lt;/b&gt;: Completely consumed. Cluster is read-only, iSCSI connection is maintained but all writes are suspended.&#x27;]",
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


class UnbindResult(data_model.DataObject):
    """
    :param fault: [required] 
    :type fault: str
    """
    fault = data_model.property(
        "fault", str,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class LdapConfiguration(data_model.DataObject):
    """
    [&#x27;LDAP Configuration object returns information about the LDAP configuration on SolidFire storage. LDAP information is returned with the API method GetLdapConfiguration.&#x27;]
    :param authType: [required] [&#x27;Identifies which user authentcation method will be used. &lt;br/&gt;&#x27;, &#x27;Valid values:&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;DirectBind&lt;/b&gt;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;SearchAndBind&lt;/b&gt;&#x27;][&#x27;Identifies which user authentcation method will be used. &lt;br/&gt;&#x27;, &#x27;Valid values:&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;DirectBind&lt;/b&gt;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;SearchAndBind&lt;/b&gt;&#x27;][&#x27;Identifies which user authentcation method will be used. &lt;br/&gt;&#x27;, &#x27;Valid values:&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;DirectBind&lt;/b&gt;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;SearchAndBind&lt;/b&gt;&#x27;][&#x27;Identifies which user authentcation method will be used. &lt;br/&gt;&#x27;, &#x27;Valid values:&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;DirectBind&lt;/b&gt;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;SearchAndBind&lt;/b&gt;&#x27;]
    :type authType: str
    
    :param enabled: [required] [&#x27;Identifies whether or not the system is enabled for LDAP. &lt;br/&gt;&#x27;, &#x27;Valid values:&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;true&lt;/b&gt;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;false&lt;/b&gt;&#x27;][&#x27;Identifies whether or not the system is enabled for LDAP. &lt;br/&gt;&#x27;, &#x27;Valid values:&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;true&lt;/b&gt;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;false&lt;/b&gt;&#x27;][&#x27;Identifies whether or not the system is enabled for LDAP. &lt;br/&gt;&#x27;, &#x27;Valid values:&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;true&lt;/b&gt;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;false&lt;/b&gt;&#x27;][&#x27;Identifies whether or not the system is enabled for LDAP. &lt;br/&gt;&#x27;, &#x27;Valid values:&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;true&lt;/b&gt;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;false&lt;/b&gt;&#x27;]
    :type enabled: bool
    
    :param groupSearchBaseDN: [required] [&#x27;The base DN of the tree to start the group search (will do a subtree search from here).&#x27;]
    :type groupSearchBaseDN: str
    
    :param groupSearchCustomFilter: [required] [&#x27;The custom search filter used.&#x27;]
    :type groupSearchCustomFilter: str
    
    :param groupSearchType: [required] [&#x27;Controls the default group search filter used, can be one of the following:&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;NoGroups&lt;/b&gt;: No group support.&lt;br/&gt;&#x27;, &quot;&lt;b&gt;ActiveDirectory&lt;/b&gt;: Nested membership of all of a user&#x27;s AD groups.&lt;br/&gt;&quot;, &#x27;&lt;b&gt;MemberDN&lt;/b&gt;: MemberDN style groups (single-level).&#x27;][&#x27;Controls the default group search filter used, can be one of the following:&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;NoGroups&lt;/b&gt;: No group support.&lt;br/&gt;&#x27;, &quot;&lt;b&gt;ActiveDirectory&lt;/b&gt;: Nested membership of all of a user&#x27;s AD groups.&lt;br/&gt;&quot;, &#x27;&lt;b&gt;MemberDN&lt;/b&gt;: MemberDN style groups (single-level).&#x27;][&#x27;Controls the default group search filter used, can be one of the following:&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;NoGroups&lt;/b&gt;: No group support.&lt;br/&gt;&#x27;, &quot;&lt;b&gt;ActiveDirectory&lt;/b&gt;: Nested membership of all of a user&#x27;s AD groups.&lt;br/&gt;&quot;, &#x27;&lt;b&gt;MemberDN&lt;/b&gt;: MemberDN style groups (single-level).&#x27;][&#x27;Controls the default group search filter used, can be one of the following:&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;NoGroups&lt;/b&gt;: No group support.&lt;br/&gt;&#x27;, &quot;&lt;b&gt;ActiveDirectory&lt;/b&gt;: Nested membership of all of a user&#x27;s AD groups.&lt;br/&gt;&quot;, &#x27;&lt;b&gt;MemberDN&lt;/b&gt;: MemberDN style groups (single-level).&#x27;]
    :type groupSearchType: str
    
    :param searchBindDN: [required] [&#x27;A fully qualified DN to log in with to perform an LDAP search for the user (needs read access to the LDAP directory).&#x27;]
    :type searchBindDN: str
    
    :param serverURIs: [required] [&#x27;A comma-separated list of LDAP server URIs (examples: &quot;ldap://1.2.3.4&quot; and ldaps://1.2.3.4:123&quot;)&#x27;]
    :type serverURIs: str
    
    :param userDNTemplate: [required] [&#x27;A string that is used to form a fully qualified user DN.&#x27;]
    :type userDNTemplate: str
    
    :param userSearchBaseDN: [required] [&#x27;The base DN of the tree used to start the search (will do a subtree search from here).&#x27;]
    :type userSearchBaseDN: str
    
    :param userSearchFilter: [required] [&#x27;The LDAP filter used.&#x27;]
    :type userSearchFilter: str
    """
    auth_type = data_model.property(
        "authType", str,
        array=False, optional=False,
        documentation="[&#x27;Identifies which user authentcation method will be used. &lt;br/&gt;&#x27;, &#x27;Valid values:&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;DirectBind&lt;/b&gt;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;SearchAndBind&lt;/b&gt;&#x27;]",
        dictionaryType=None
    )
    enabled = data_model.property(
        "enabled", bool,
        array=False, optional=False,
        documentation="[&#x27;Identifies whether or not the system is enabled for LDAP. &lt;br/&gt;&#x27;, &#x27;Valid values:&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;true&lt;/b&gt;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;false&lt;/b&gt;&#x27;]",
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
        documentation="[&#x27;Controls the default group search filter used, can be one of the following:&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;NoGroups&lt;/b&gt;: No group support.&lt;br/&gt;&#x27;, &quot;&lt;b&gt;ActiveDirectory&lt;/b&gt;: Nested membership of all of a user&#x27;s AD groups.&lt;br/&gt;&quot;, &#x27;&lt;b&gt;MemberDN&lt;/b&gt;: MemberDN style groups (single-level).&#x27;]",
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


class GetLdapConfigurationResult(data_model.DataObject):
    """
    :param ldapConfiguration: [required] [&#x27;List of the current LDAP configuration settings. This API call will not return the plain text of the search account password.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Note&lt;/b&gt;: If LDAP authentication is currently disabled, all the returned settings will be empty with the exception of &quot;authType&quot;, and &quot;groupSearchType&quot; which are set to &quot;SearchAndBind&quot; and &quot;ActiveDirectory&quot; respectively.&#x27;][&#x27;List of the current LDAP configuration settings. This API call will not return the plain text of the search account password.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Note&lt;/b&gt;: If LDAP authentication is currently disabled, all the returned settings will be empty with the exception of &quot;authType&quot;, and &quot;groupSearchType&quot; which are set to &quot;SearchAndBind&quot; and &quot;ActiveDirectory&quot; respectively.&#x27;][&#x27;List of the current LDAP configuration settings. This API call will not return the plain text of the search account password.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Note&lt;/b&gt;: If LDAP authentication is currently disabled, all the returned settings will be empty with the exception of &quot;authType&quot;, and &quot;groupSearchType&quot; which are set to &quot;SearchAndBind&quot; and &quot;ActiveDirectory&quot; respectively.&#x27;]
    :type ldapConfiguration: LdapConfiguration
    """
    ldap_configuration = data_model.property(
        "ldapConfiguration", LdapConfiguration,
        array=False, optional=False,
        documentation="[&#x27;List of the current LDAP configuration settings. This API call will not return the plain text of the search account password.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Note&lt;/b&gt;: If LDAP authentication is currently disabled, all the returned settings will be empty with the exception of &quot;authType&quot;, and &quot;groupSearchType&quot; which are set to &quot;SearchAndBind&quot; and &quot;ActiveDirectory&quot; respectively.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class ListTestsResult(data_model.DataObject):
    """
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


class AsyncResult(data_model.DataObject):
    """
    [&#x27;The wrapped object returned by the &quot;GetAsyncResult&quot; API Service call.&#x27;, &#x27;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Note&lt;/b&gt;: The return value of GetAsyncResult is essentially a nested version of the standard JSON response with an additional status field.&#x27;]
    [&#x27;The wrapped object returned by the &quot;GetAsyncResult&quot; API Service call.&#x27;, &#x27;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Note&lt;/b&gt;: The return value of GetAsyncResult is essentially a nested version of the standard JSON response with an additional status field.&#x27;]
    [&#x27;The wrapped object returned by the &quot;GetAsyncResult&quot; API Service call.&#x27;, &#x27;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Note&lt;/b&gt;: The return value of GetAsyncResult is essentially a nested version of the standard JSON response with an additional status field.&#x27;]
    :param message: [required] [&#x27;The return value for the original method call if the call was completed successfully.&#x27;]
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
    """
    [&#x27;The object returned by the &quot;GetAsyncResult&quot; API Service call.&#x27;, &#x27;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Note&lt;/b&gt;: The return value of GetAsyncResult is essentially a nested version of the standard JSON response with an additional status field.&#x27;]
    [&#x27;The object returned by the &quot;GetAsyncResult&quot; API Service call.&#x27;, &#x27;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Note&lt;/b&gt;: The return value of GetAsyncResult is essentially a nested version of the standard JSON response with an additional status field.&#x27;]
    [&#x27;The object returned by the &quot;GetAsyncResult&quot; API Service call.&#x27;, &#x27;&lt;br/&gt;&#x27;, &#x27;&lt;b&gt;Note&lt;/b&gt;: The return value of GetAsyncResult is essentially a nested version of the standard JSON response with an additional status field.&#x27;]
    :param result: [required] [&#x27;The resulting message for the original method call if the call was completed successfully.&#x27;]
    :type result: AsyncResult
    
    :param status: [required] [&#x27;Status of the asynchronous method call&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;running&lt;/b&gt;: The method is still running.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;complete&lt;/b&gt;: The method is complete and the result or error is available.&#x27;][&#x27;Status of the asynchronous method call&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;running&lt;/b&gt;: The method is still running.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;complete&lt;/b&gt;: The method is complete and the result or error is available.&#x27;][&#x27;Status of the asynchronous method call&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;running&lt;/b&gt;: The method is still running.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;complete&lt;/b&gt;: The method is complete and the result or error is available.&#x27;]
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
        documentation="[&#x27;Status of the asynchronous method call&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;running&lt;/b&gt;: The method is still running.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;complete&lt;/b&gt;: The method is complete and the result or error is available.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class ListFibreChannelPortInfoResult(data_model.DataObject):
    """
    ListFibreChannelPortInfoResult is used to return information about the Fibre Channel ports.
    :param fibreChannelPortInfo: [required] Used to return information about the Fibre Channel ports.
    :type fibreChannelPortInfo: dict
    """
    fibre_channel_port_info = data_model.property(
        "fibreChannelPortInfo", dict,
        array=False, optional=False,
        documentation="Used to return information about the Fibre Channel ports.",
        dictionaryType=FibreChannelPortInfoResult
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class SupportBundleDetails(data_model.DataObject):
    """
    :param bundleName: [required] [&quot;The name specified in the &#x27;CreateSupportBundle API method. If no name was specified, &#x27;supportbundle&#x27; will be used.&quot;]
    :type bundleName: str
    
    :param extraArgs: [required] [&#x27;The arguments passed with this method.&#x27;]
    :type extraArgs: str
    
    :param files: [required] [&#x27;A list of the support bundle files that were created.&#x27;]
    :type files: str
    
    :param url: [required] [&#x27;The URL that you can use to download the bundle file(s). Should correspond 1:1 with files list.&#x27;]
    :type url: str
    
    :param output: [required] [&#x27;The commands that were run and their output, with newlines replaced by HTML &lt;br&gt; elements.&#x27;]
    :type output: str
    
    :param timeoutSec: [required] [&#x27;The timeout specified for the support bundle creation process.&#x27;]
    :type timeoutSec: int
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


class GetBackupTargetResult(data_model.DataObject):
    """
    :param backupTarget: [required] Object returned for backup target.
    :type backupTarget: BackupTarget
    """
    backup_target = data_model.property(
        "backupTarget", BackupTarget,
        array=False, optional=False,
        documentation="Object returned for backup target.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class DatabaseChildEntry(data_model.DataObject):
    """
    :param data: [required] 
    :type data: dict
    
    :param stat: [required] 
    :type stat: DatabaseStats
    
    :param name: [required] 
    :type name: str
    """
    data = data_model.property(
        "data", dict,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    stat = data_model.property(
        "stat", DatabaseStats,
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

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class ListDatabaseChildrenDataResult(data_model.DataObject):
    """
    :param children: [required] 
    :type children: DatabaseChildEntry
    """
    children = data_model.property(
        "children", DatabaseChildEntry,
        array=True, optional=False,
        documentation="",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class ListVolumeStatsByVolumeResult(data_model.DataObject):
    """
    :param volumeStats: [required] [&#x27;List of account activity information.&#x27;]
    :type volumeStats: VolumeStats
    """
    volume_stats = data_model.property(
        "volumeStats", VolumeStats,
        array=True, optional=False,
        documentation="[&#x27;List of account activity information.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class CreateGroupSnapshotResult(data_model.DataObject):
    """
    :param groupSnapshotID: [required] Unique ID of the new group snapshot.
    :type groupSnapshotID: int
    
    :param members: [required] [&#x27;List of checksum, volumeIDs and snapshotIDs for each member of the group.&#x27;]
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


class GetClusterStateResult(data_model.DataObject):
    """
    :param cluster: [required] Name of the cluster.
    :type cluster: str
    
    :param state: [required] &lt;strong&gt;Available:&lt;/strong&gt; Node has not been configured with a cluster name.&lt;br&gt;&lt;strong&gt;Pending:&lt;/strong&gt; Node is pending for a specific named cluster and can be added.&lt;br&gt;&lt;strong&gt;Active:&lt;/strong&gt; Node is active and a member of a cluster and may not be added to another cluster.
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


class VirtualVolumeUnbindResult(data_model.DataObject):
    """
    :param unbindResults: [required] 
    :type unbindResults: UnbindResult
    """
    unbind_results = data_model.property(
        "unbindResults", UnbindResult,
        array=True, optional=False,
        documentation="",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class ListVirtualVolumesResult(data_model.DataObject):
    """
    :param virtualVolumes: [required] 
    :type virtualVolumes: VirtualVolumeInfo
    
    :param nextVirtualVolumeID: [required] 
    :type nextVirtualVolumeID: UUID
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


class Service(data_model.DataObject):
    """
    :param serviceID: [required] Unique identifier for this service.
    :type serviceID: int
    
    :param serviceType: [required] 
    :type serviceType: str
    
    :param nodeID: [required] [&#x27;The node this service resides on.&#x27;]
    :type nodeID: int
    
    :param associatedBV:  [&quot;This service&#x27;s associated bulk volume service.&quot;, &#x27;This will only be set if the service type is a slice service.&#x27;][&quot;This service&#x27;s associated bulk volume service.&quot;, &#x27;This will only be set if the service type is a slice service.&#x27;]
    :type associatedBV: int
    
    :param associatedTS:  [&quot;This service&#x27;s associated transport service.&quot;, &#x27;This will only be set if the service type is a slice service.&#x27;][&quot;This service&#x27;s associated transport service.&quot;, &#x27;This will only be set if the service type is a slice service.&#x27;]
    :type associatedTS: int
    
    :param associatedVS:  [&quot;This service&#x27;s associated volume service.&quot;, &#x27;This will only be set if the service type is a slice service.&#x27;][&quot;This service&#x27;s associated volume service.&quot;, &#x27;This will only be set if the service type is a slice service.&#x27;]
    :type associatedVS: int
    
    :param asyncResultIDs: [required] [&#x27;The list of asynchronous jobs currently running for this service.&#x27;]
    :type asyncResultIDs: int
    
    :param driveID:  [&#x27;If this service resides on a drive, the ID of that drive.&#x27;]
    :type driveID: int
    
    :param firstTimeStartup: [required] [&#x27;Has this service started successfully?&#x27;, &#x27;When a new drive is added to the system, the created service will initially have a value of false here.&#x27;, &#x27;After the service has started, this value will be set to true.&#x27;, &#x27;This can be used to check if the service has ever started.&#x27;][&#x27;Has this service started successfully?&#x27;, &#x27;When a new drive is added to the system, the created service will initially have a value of false here.&#x27;, &#x27;After the service has started, this value will be set to true.&#x27;, &#x27;This can be used to check if the service has ever started.&#x27;][&#x27;Has this service started successfully?&#x27;, &#x27;When a new drive is added to the system, the created service will initially have a value of false here.&#x27;, &#x27;After the service has started, this value will be set to true.&#x27;, &#x27;This can be used to check if the service has ever started.&#x27;][&#x27;Has this service started successfully?&#x27;, &#x27;When a new drive is added to the system, the created service will initially have a value of false here.&#x27;, &#x27;After the service has started, this value will be set to true.&#x27;, &#x27;This can be used to check if the service has ever started.&#x27;]
    :type firstTimeStartup: bool
    
    :param ipcPort: [required] [&#x27;The port used for intra-cluster communication.&#x27;, &#x27;This will be in the 4000-4100 range.&#x27;][&#x27;The port used for intra-cluster communication.&#x27;, &#x27;This will be in the 4000-4100 range.&#x27;]
    :type ipcPort: int
    
    :param iscsiPort: [required] [&#x27;The port used for iSCSI traffic.&#x27;, &#x27;This will only be set if the service type is a transport service.&#x27;][&#x27;The port used for iSCSI traffic.&#x27;, &#x27;This will only be set if the service type is a transport service.&#x27;]
    :type iscsiPort: int
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

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class Drive(data_model.DataObject):
    """
    :param driveID: [required] [&#x27;A unique identifier for this drive.&#x27;]
    :type driveID: int
    
    :param nodeID: [required] [&#x27;The node this drive is located.&#x27;, &#x27;If the drive has been physically removed from the node, this is where it was last seen.&#x27;][&#x27;The node this drive is located.&#x27;, &#x27;If the drive has been physically removed from the node, this is where it was last seen.&#x27;]
    :type nodeID: int
    
    :param assignedService:  [&#x27;If this drive is hosting a service, the identifier for that service.&#x27;]
    :type assignedService: int
    
    :param asyncResultIDs: [required] [&#x27;The list of asynchronous jobs currently running on the drive (for example: a secure erase job).&#x27;]
    :type asyncResultIDs: int
    
    :param capacity: [required] [&#x27;The raw capacity of this drive in bytes.&#x27;]
    :type capacity: int
    
    :param serial: [required] The manufacturer&#x27;s serial number for this drive.
    :type serial: str
    
    :param slot:  [&#x27;Slot number in the server chassis where this drive is located.&#x27;, &#x27;If the drive has been physically removed from the node, this will not have a value.&#x27;][&#x27;Slot number in the server chassis where this drive is located.&#x27;, &#x27;If the drive has been physically removed from the node, this will not have a value.&#x27;]
    :type slot: int
    
    :param driveStatus: [required] The current status of this drive.
    :type driveStatus: str
    
    :param driveType: [required] The type of this drive.
    :type driveType: str
    
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
    attributes = data_model.property(
        "attributes", dict,
        array=False, optional=False,
        documentation="List of Name/Value pairs in JSON object format.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class DetailedService(data_model.DataObject):
    """
    :param service: [required] 
    :type service: Service
    
    :param node: [required] 
    :type node: Node
    
    :param drive:  
    :type drive: Drive
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

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class ListServicesResult(data_model.DataObject):
    """
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


class LoggingServer(data_model.DataObject):
    """
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
    """
    :param remoteHosts: [required] [&#x27;List of hosts to forward logging information to.&#x27;]
    :type remoteHosts: LoggingServer
    """
    remote_hosts = data_model.property(
        "remoteHosts", LoggingServer,
        array=True, optional=False,
        documentation="[&#x27;List of hosts to forward logging information to.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class SetConfigResult(data_model.DataObject):
    """
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


class CreateSupportBundleResult(data_model.DataObject):
    """
    :param details: [required] [&#x27;The details of the support bundle. &#x27;]
    :type details: SupportBundleDetails
    
    :param duration: [required] [&#x27;The amount of time required to create the support bundle in the format HH:MM:SS.ssssss&#x27;]
    :type duration: str
    
    :param result: [required] [&#x27;Whether the support bundle creation passed of failed.&#x27;]
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


class GetScheduleResult(data_model.DataObject):
    """
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


class UnbindArguments(data_model.DataObject):
    """
    :param virtualVolumeID: [required] 
    :type virtualVolumeID: UUID
    
    :param protocolEndpointType: [required] 
    :type protocolEndpointType: str
    
    :param protocolEndpointInBandID: [required] 
    :type protocolEndpointInBandID: str
    
    :param virtualVolumeSecondaryID: [required] 
    :type virtualVolumeSecondaryID: str
    """
    virtual_volume_id = data_model.property(
        "virtualVolumeID", UUID,
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
    protocol_endpoint_in_band_id = data_model.property(
        "protocolEndpointInBandID", str,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    virtual_volume_secondary_id = data_model.property(
        "virtualVolumeSecondaryID", str,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class SnmpTrapRecipient(data_model.DataObject):
    """
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


class Account(data_model.DataObject):
    """
    [&#x27;The object containing information about an account.&#x27;, &#x27;This object only includes &quot;configured&quot; information about the account, not any runtime or usage information.&#x27;]
    [&#x27;The object containing information about an account.&#x27;, &#x27;This object only includes &quot;configured&quot; information about the account, not any runtime or usage information.&#x27;]
    :param accountID: [required] Unique AccountID for the account.
    :type accountID: int
    
    :param username: [required] User name for the account.
    :type username: str
    
    :param status: [required] Current status of the account.
    :type status: str
    
    :param volumes: [required] List of VolumeIDs for Volumes owned by this account.
    :type volumes: int
    
    :param initiatorSecret:  CHAP secret to use for the initiator.
    :type initiatorSecret: CHAPSecret
    
    :param targetSecret:  CHAP secret to use for the target (mutual CHAP authentication).
    :type targetSecret: CHAPSecret
    
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


class GetAccountResult(data_model.DataObject):
    """
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


class DeleteVolumeAccessGroupResult(data_model.DataObject):
    """"""

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class GetClusterConfigResult(data_model.DataObject):
    """
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


class DisableEncryptionAtRestResult(data_model.DataObject):
    """"""

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class FeatureObject(data_model.DataObject):
    """
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


class ClusterStats(data_model.DataObject):
    """
    :param clusterUtilization: [required] The amount of cluster capacity being utilized.
    :type clusterUtilization: float
    
    :param clientQueueDepth: [required] 
    :type clientQueueDepth: int
    
    :param readBytes: [required] Total bytes read by clients.
    :type readBytes: int
    
    :param readOps: [required] Total read operations.
    :type readOps: int
    
    :param timestamp: [required] Current time in UTC format. ISO 8601 date string.
    :type timestamp: str
    
    :param writeBytes: [required] Total bytes written by clients.
    :type writeBytes: int
    
    :param writeOps: [required] Total write operations.
    :type writeOps: int
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
    """
    :param clusterStats: [required] 
    :type clusterStats: ClusterStats
    """
    cluster_stats = data_model.property(
        "clusterStats", ClusterStats,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class RemoveAccountResult(data_model.DataObject):
    """"""

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class GetEfficiencyResult(data_model.DataObject):
    """
    :param compression:  The amount of space being saved by compressing data on a single volume. Stated as a ratio where &quot;1&quot; means data has been stored without being compressed.
    :type compression: float
    
    :param deduplication:  The amount of space being saved on a single volume by not duplicating data. Stated as a ratio.
    :type deduplication: float
    
    :param thinProvisioning:  The ratio of space used to the amount of space allocated for storing data. Stated as a ratio.
    :type thinProvisioning: float
    
    :param timestamp: [required] The last time efficiency data was collected after Garbage Collection (GC). ISO 8601 data string.
    :type timestamp: str
    
    :param missingVolumes: [required] The volumes that could not be queried for efficiency data. Missing volumes can be caused by GC being less than hour old, temporary network loss or restarted services since the GC cycle.
    :type missingVolumes: int
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


class GroupCloneVolumeMember(data_model.DataObject):
    """
    Represents the relationship between the source Volume and cloned Volume IDs.
    :param volumeID: [required] The VolumeID of the cloned volume.
    :type volumeID: int
    
    :param srcVolumeID: [required] The VolumeID of the source volume.
    :type srcVolumeID: int
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


class AddDrivesResult(data_model.DataObject):
    """"""

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class ClusterFaultInfo(data_model.DataObject):
    """
    :param severity: [required] 
    :type severity: str
    
    :param type: [required] 
    :type type: str
    
    :param code: [required] 
    :type code: str
    
    :param details: [required] 
    :type details: str
    
    :param nodeHardwareFaultID: [required] 
    :type nodeHardwareFaultID: int
    
    :param nodeID: [required] 
    :type nodeID: int
    
    :param serviceID: [required] 
    :type serviceID: int
    
    :param driveID: [required] 
    :type driveID: int
    
    :param resolved: [required] 
    :type resolved: bool
    
    :param clusterFaultID: [required] 
    :type clusterFaultID: int
    
    :param date: [required] 
    :type date: str
    
    :param resolvedDate: [required] 
    :type resolvedDate: str
    
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
    """
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


class Volume(data_model.DataObject):
    """
    [&#x27;Volumes Info is an object containing information about a volume.&#x27;, &#x27;The return objects only include &quot;configured&quot; information about the volume and not runtime or usage information.&#x27;, &#x27;Information about paired volumes will also be returned.&#x27;]
    [&#x27;Volumes Info is an object containing information about a volume.&#x27;, &#x27;The return objects only include &quot;configured&quot; information about the volume and not runtime or usage information.&#x27;, &#x27;Information about paired volumes will also be returned.&#x27;]
    [&#x27;Volumes Info is an object containing information about a volume.&#x27;, &#x27;The return objects only include &quot;configured&quot; information about the volume and not runtime or usage information.&#x27;, &#x27;Information about paired volumes will also be returned.&#x27;]
    :param volumeID: [required] Unique VolumeID for the volume.
    :type volumeID: int
    
    :param name: [required] Name of the volume as provided at creation time.
    :type name: str
    
    :param accountID: [required] Unique AccountID for the account.
    :type accountID: int
    
    :param createTime: [required] UTC formatted time the volume was created.
    :type createTime: str
    
    :param status: [required] [&#x27;Current status of the volume&#x27;, &#x27;init: A volume that is being initialized and is not ready for connections.&#x27;, &#x27;active: An active volume ready for connections.&#x27;][&#x27;Current status of the volume&#x27;, &#x27;init: A volume that is being initialized and is not ready for connections.&#x27;, &#x27;active: An active volume ready for connections.&#x27;][&#x27;Current status of the volume&#x27;, &#x27;init: A volume that is being initialized and is not ready for connections.&#x27;, &#x27;active: An active volume ready for connections.&#x27;]
    :type status: str
    
    :param access: [required] [&#x27;Access allowed for the volume&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;readOnly&lt;/b&gt;: Only read operations are allowed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;readWrite&lt;/b&gt;: Reads and writes are allowed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;locked&lt;/b&gt;: No reads or writes are allowed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;replicationTarget&lt;/b&gt;: Designated as a target volume in a replicated volume pair.&#x27;][&#x27;Access allowed for the volume&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;readOnly&lt;/b&gt;: Only read operations are allowed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;readWrite&lt;/b&gt;: Reads and writes are allowed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;locked&lt;/b&gt;: No reads or writes are allowed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;replicationTarget&lt;/b&gt;: Designated as a target volume in a replicated volume pair.&#x27;][&#x27;Access allowed for the volume&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;readOnly&lt;/b&gt;: Only read operations are allowed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;readWrite&lt;/b&gt;: Reads and writes are allowed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;locked&lt;/b&gt;: No reads or writes are allowed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;replicationTarget&lt;/b&gt;: Designated as a target volume in a replicated volume pair.&#x27;][&#x27;Access allowed for the volume&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;readOnly&lt;/b&gt;: Only read operations are allowed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;readWrite&lt;/b&gt;: Reads and writes are allowed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;locked&lt;/b&gt;: No reads or writes are allowed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;replicationTarget&lt;/b&gt;: Designated as a target volume in a replicated volume pair.&#x27;][&#x27;Access allowed for the volume&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;readOnly&lt;/b&gt;: Only read operations are allowed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;readWrite&lt;/b&gt;: Reads and writes are allowed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;locked&lt;/b&gt;: No reads or writes are allowed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;replicationTarget&lt;/b&gt;: Designated as a target volume in a replicated volume pair.&#x27;]
    :type access: str
    
    :param enable512e: [required] If &quot;true&quot;, the volume provides 512 byte sector emulation.
    :type enable512e: bool
    
    :param iqn: [required] Volume iSCSI Qualified Name.
    :type iqn: str
    
    :param scsiEUIDeviceID: [required] Globally unique SCSI device identifier for the volume in EUI-64 based 16-byte format.
    :type scsiEUIDeviceID: str
    
    :param scsiNAADeviceID: [required] Globally unique SCSI device identifier for the volume in NAA IEEE Registered Extended format.
    :type scsiNAADeviceID: str
    
    :param qos: [required] Quality of service settings for this volume.
    :type qos: VolumeQOS
    
    :param volumeAccessGroups: [required] List of volume access groups to which a volume belongs.
    :type volumeAccessGroups: int
    
    :param volumePairs: [required] [&#x27;Information about a paired volume.&#x27;, &#x27;Available only if a volume is paired.&#x27;, &#x27;@see VolumePairs for return values.&#x27;][&#x27;Information about a paired volume.&#x27;, &#x27;Available only if a volume is paired.&#x27;, &#x27;@see VolumePairs for return values.&#x27;][&#x27;Information about a paired volume.&#x27;, &#x27;Available only if a volume is paired.&#x27;, &#x27;@see VolumePairs for return values.&#x27;]
    :type volumePairs: VolumePair
    
    :param deleteTime:  [&#x27;The time this volume was deleted.&#x27;, &#x27;If this has no value, the volume has not yet been deleted.&#x27;][&#x27;The time this volume was deleted.&#x27;, &#x27;If this has no value, the volume has not yet been deleted.&#x27;]
    :type deleteTime: str
    
    :param purgeTime:  [&#x27;The time this volume will be purged from the system.&#x27;, &#x27;If this has no value, the volume has not yet been deleted (and is not scheduled for purging).&#x27;][&#x27;The time this volume will be purged from the system.&#x27;, &#x27;If this has no value, the volume has not yet been deleted (and is not scheduled for purging).&#x27;]
    :type purgeTime: str
    
    :param sliceCount: [required] [&#x27;The number of slices backing this volume.&#x27;, &#x27;In the current software, this value will always be 1.&#x27;][&#x27;The number of slices backing this volume.&#x27;, &#x27;In the current software, this value will always be 1.&#x27;]
    :type sliceCount: int
    
    :param totalSize: [required] [&#x27;Total size of this volume in bytes.&#x27;]
    :type totalSize: int
    
    :param blockSize: [required] [&#x27;Size of the blocks on the volume.&#x27;]
    :type blockSize: int
    
    :param virtualVolumeID: [required] [&#x27;Virtual volume ID this volume backs.&#x27;]
    :type virtualVolumeID: UUID
    
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
        documentation="[&#x27;Access allowed for the volume&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;readOnly&lt;/b&gt;: Only read operations are allowed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;readWrite&lt;/b&gt;: Reads and writes are allowed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;locked&lt;/b&gt;: No reads or writes are allowed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;replicationTarget&lt;/b&gt;: Designated as a target volume in a replicated volume pair.&#x27;]",
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


class ListVolumesResult(data_model.DataObject):
    """
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


class SetSnmpInfoResult(data_model.DataObject):
    """"""

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class GetDriveHardwareInfoResult(data_model.DataObject):
    """
    :param driveHardwareInfo: [required] 
    :type driveHardwareInfo: DriveHardwareInfo
    """
    drive_hardware_info = data_model.property(
        "driveHardwareInfo", DriveHardwareInfo,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class ListActiveVolumesResult(data_model.DataObject):
    """
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


class RemoveClusterAdminResult(data_model.DataObject):
    """"""

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class TestConnectEnsembleResult(data_model.DataObject):
    """
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


class StorageContainer(data_model.DataObject):
    """
    :param name: [required] 
    :type name: str
    
    :param storageContainerID: [required] 
    :type storageContainerID: UUID
    
    :param accountID: [required] 
    :type accountID: int
    
    :param protocolEndpointType: [required] 
    :type protocolEndpointType: str
    
    :param initiatorSecret: [required] 
    :type initiatorSecret: CHAPSecret
    
    :param targetSecret: [required] 
    :type targetSecret: CHAPSecret
    
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
        "initiatorSecret", CHAPSecret,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    target_secret = data_model.property(
        "targetSecret", CHAPSecret,
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


class CreateStorageContainerResult(data_model.DataObject):
    """
    :param storageContainer: [required] 
    :type storageContainer: StorageContainer
    """
    storage_container = data_model.property(
        "storageContainer", StorageContainer,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class VirtualVolumeAsyncResult(data_model.DataObject):
    """
    :param virtualVolumeTaskID: [required] The ID of the clone task.
    :type virtualVolumeTaskID: UUID
    
    :param volumeID: [required] The volume ID of the newly-created clone.
    :type volumeID: int
    
    :param virtualVolumeID: [required] virtualVolumeID for the newly created clone.
    :type virtualVolumeID: UUID
    """
    virtual_volume_task_id = data_model.property(
        "virtualVolumeTaskID", UUID,
        array=False, optional=False,
        documentation="The ID of the clone task.",
        dictionaryType=None
    )
    volume_id = data_model.property(
        "volumeID", int,
        array=False, optional=False,
        documentation="The volume ID of the newly-created clone.",
        dictionaryType=None
    )
    virtual_volume_id = data_model.property(
        "virtualVolumeID", UUID,
        array=False, optional=False,
        documentation="virtualVolumeID for the newly created clone.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class CompleteClusterPairingResult(data_model.DataObject):
    """
    :param clusterPairID: [required] Unique identifier for the cluster pair.
    :type clusterPairID: int
    """
    cluster_pair_id = data_model.property(
        "clusterPairID", int,
        array=False, optional=False,
        documentation="Unique identifier for the cluster pair.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class GetSnmpACLResult(data_model.DataObject):
    """
    :param networks: [required] List of networks and what type of access they have to the SNMP servers running on the cluster nodes. Present if SNMP v3 is disabled.
    :type networks: SnmpNetwork
    
    :param usmUsers: [required] List of users and the type of access they have to the SNMP servers running on the cluster nodes. Present if SNMP v3 is enabled.
    :type usmUsers: SnmpV3UsmUser
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


class ModifyVolumeAccessGroupResult(data_model.DataObject):
    """"""

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class ListGroupSnapshotsResult(data_model.DataObject):
    """
    :param groupSnapshots: [required] List of Group Snapshots.
    :type groupSnapshots: GroupSnapshot
    """
    group_snapshots = data_model.property(
        "groupSnapshots", GroupSnapshot,
        array=True, optional=False,
        documentation="List of Group Snapshots.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class KernelCrashDump(data_model.DataObject):
    """
    :param kernelCrashDumpMinFreeGb: [required] 
    :type kernelCrashDumpMinFreeGb: int
    
    :param kernelCrashDumpDirectory: [required] 
    :type kernelCrashDumpDirectory: str
    
    :param kernelCrashDumpKernelOptions: [required] 
    :type kernelCrashDumpKernelOptions: str
    
    :param kernelCrashDumpMakedumpfileLevel: [required] 
    :type kernelCrashDumpMakedumpfileLevel: int
    
    :param kernelCrashDumpDefaultState: [required] 
    :type kernelCrashDumpDefaultState: str
    """
    kernel_crash_dump_min_free_gb = data_model.property(
        "kernelCrashDumpMinFreeGb", int,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    kernel_crash_dump_directory = data_model.property(
        "kernelCrashDumpDirectory", str,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    kernel_crash_dump_kernel_options = data_model.property(
        "kernelCrashDumpKernelOptions", str,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    kernel_crash_dump_makedumpfile_level = data_model.property(
        "kernelCrashDumpMakedumpfileLevel", int,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    kernel_crash_dump_default_state = data_model.property(
        "kernelCrashDumpDefaultState", str,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class VirtualVolumeBindResult(data_model.DataObject):
    """
    :param binding: [required] Describes the VVol &lt;-&gt; Host binding.
    :type binding: VirtualVolumeBinding
    """
    binding = data_model.property(
        "binding", VirtualVolumeBinding,
        array=False, optional=False,
        documentation="Describes the VVol &lt;-&gt; Host binding.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class ListSchedulesResult(data_model.DataObject):
    """
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


class ModifySnapshotResult(data_model.DataObject):
    """"""

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class ClusterVersionInfo(data_model.DataObject):
    """
    Version information for a node in the cluster.
    :param nodeID: [required] 
    :type nodeID: int
    
    :param nodeVersion: [required] 
    :type nodeVersion: str
    
    :param nodeInternalRevision: [required] 
    :type nodeInternalRevision: str
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


class GetBootstrapConfigResult(data_model.DataObject):
    """
    :param clusterName: [required] Name of the cluster.
    :type clusterName: str
    
    :param nodeName: [required] Name of the node.
    :type nodeName: str
    
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


class GetVolumeEfficiencyResult(data_model.DataObject):
    """
    :param compression: [required] [&#x27;The amount of space being saved by compressing data on a single volume.&#x27;, &#x27;Stated as a ratio where &quot;1&quot; means data has been stored without being compressed.&#x27;][&#x27;The amount of space being saved by compressing data on a single volume.&#x27;, &#x27;Stated as a ratio where &quot;1&quot; means data has been stored without being compressed.&#x27;]
    :type compression: float
    
    :param deduplication: [required] [&#x27;The amount of space being saved on a single volume by not duplicating data.&#x27;, &#x27;Stated as a ratio.&#x27;][&#x27;The amount of space being saved on a single volume by not duplicating data.&#x27;, &#x27;Stated as a ratio.&#x27;]
    :type deduplication: float
    
    :param missingVolumes: [required] [&#x27;The volumes that could not be queried for efficiency data.&#x27;, &#x27;Missing volumes can be caused by GC being less than hour old, temporary network loss or restarted services since the GC cycle.&#x27;][&#x27;The volumes that could not be queried for efficiency data.&#x27;, &#x27;Missing volumes can be caused by GC being less than hour old, temporary network loss or restarted services since the GC cycle.&#x27;]
    :type missingVolumes: int
    
    :param thinProvisioning: [required] [&#x27;The ratio of space used to the amount of space allocated for storing data.&#x27;, &#x27;Stated as a ratio.&#x27;][&#x27;The ratio of space used to the amount of space allocated for storing data.&#x27;, &#x27;Stated as a ratio.&#x27;]
    :type thinProvisioning: float
    
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


class CancelCloneResult(data_model.DataObject):
    """"""

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class SoftwareVersionInfo(data_model.DataObject):
    """
    :param currentVersion: [required] 
    :type currentVersion: str
    
    :param nodeID: [required] 
    :type nodeID: int
    
    :param packageName: [required] 
    :type packageName: str
    
    :param pendingVersion: [required] 
    :type pendingVersion: str
    
    :param startTime: [required] 
    :type startTime: str
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
    """
    :param clusterAPIVersion: [required] 
    :type clusterAPIVersion: str
    
    :param clusterVersion: [required] 
    :type clusterVersion: str
    
    :param clusterVersionInfo: [required] 
    :type clusterVersionInfo: ClusterVersionInfo
    
    :param softwareVersionInfo: [required] 
    :type softwareVersionInfo: SoftwareVersionInfo
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


class AddLdapClusterAdminResult(data_model.DataObject):
    """"""

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class CreateBackupTargetResult(data_model.DataObject):
    """
    :param backupTargetID: [required] [&#x27;Unique identifier assigned to the backup target.&#x27;]
    :type backupTargetID: int
    """
    backup_target_id = data_model.property(
        "backupTargetID", int,
        array=False, optional=False,
        documentation="[&#x27;Unique identifier assigned to the backup target.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class NewDrive(data_model.DataObject):
    """
    :param driveID: [required] [&#x27;A unique identifier for this drive.&#x27;]
    :type driveID: int
    """
    drive_id = data_model.property(
        "driveID", int,
        array=False, optional=False,
        documentation="[&#x27;A unique identifier for this drive.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class NodeSystemStatusInfo(data_model.DataObject):
    """
    :param rebootRequired: [required] 
    :type rebootRequired: bool
    """
    reboot_required = data_model.property(
        "rebootRequired", bool,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class NodeSystemStatus(data_model.DataObject):
    """
    :param nodeID: [required] 
    :type nodeID: int
    
    :param result: [required] 
    :type result: NodeSystemStatusInfo
    """
    node_id = data_model.property(
        "nodeID", int,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    result = data_model.property(
        "result", NodeSystemStatusInfo,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class PairedCluster(data_model.DataObject):
    """
    :param clusterName: [required] Name of the other cluster in the pair
    :type clusterName: str
    
    :param clusterPairID: [required] Unique ID given to each cluster in the pair.
    :type clusterPairID: int
    
    :param clusterPairUUID: [required] Universally unique identifier.
    :type clusterPairUUID: UUID
    
    :param latency: [required] Number, in milliseconds, of latency between clusters.
    :type latency: int
    
    :param mvip: [required] IP of the management connection for paired clusters.
    :type mvip: str
    
    :param status: [required] [&#x27;Can be one of the following:&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;Connected&lt;/b&gt;&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;Misconfigured&lt;/b&gt;&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;Disconnected&lt;/b&gt;&#x27;][&#x27;Can be one of the following:&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;Connected&lt;/b&gt;&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;Misconfigured&lt;/b&gt;&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;Disconnected&lt;/b&gt;&#x27;][&#x27;Can be one of the following:&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;Connected&lt;/b&gt;&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;Misconfigured&lt;/b&gt;&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;Disconnected&lt;/b&gt;&#x27;][&#x27;Can be one of the following:&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;Connected&lt;/b&gt;&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;Misconfigured&lt;/b&gt;&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;Disconnected&lt;/b&gt;&#x27;]
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
        documentation="[&#x27;Can be one of the following:&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;Connected&lt;/b&gt;&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;Misconfigured&lt;/b&gt;&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;Disconnected&lt;/b&gt;&#x27;]",
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
    """
    :param clusterPairs: [required] Information about each paired cluster.
    :type clusterPairs: PairedCluster
    """
    cluster_pairs = data_model.property(
        "clusterPairs", PairedCluster,
        array=True, optional=False,
        documentation="Information about each paired cluster.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class ModifyVolumeResult(data_model.DataObject):
    """
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


class GetNtpInfoResult(data_model.DataObject):
    """
    :param broadcastclient: [required] [&#x27;Indicates whether or not the nodes in the cluster are listening for broadcast NTP messages. Possible values:&#x27;, &#x27;true&#x27;, &#x27;false&#x27;][&#x27;Indicates whether or not the nodes in the cluster are listening for broadcast NTP messages. Possible values:&#x27;, &#x27;true&#x27;, &#x27;false&#x27;][&#x27;Indicates whether or not the nodes in the cluster are listening for broadcast NTP messages. Possible values:&#x27;, &#x27;true&#x27;, &#x27;false&#x27;]
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


class UpdateBulkVolumeStatusResult(data_model.DataObject):
    """
    :param status: [required] [&#x27;Status of the session requested. Returned status:&lt;br/&gt;&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;preparing&lt;/b&gt;&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;active&lt;/b&gt;&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;done&lt;/b&gt;&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;failed&lt;/b&gt;&#x27;][&#x27;Status of the session requested. Returned status:&lt;br/&gt;&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;preparing&lt;/b&gt;&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;active&lt;/b&gt;&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;done&lt;/b&gt;&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;failed&lt;/b&gt;&#x27;][&#x27;Status of the session requested. Returned status:&lt;br/&gt;&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;preparing&lt;/b&gt;&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;active&lt;/b&gt;&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;done&lt;/b&gt;&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;failed&lt;/b&gt;&#x27;][&#x27;Status of the session requested. Returned status:&lt;br/&gt;&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;preparing&lt;/b&gt;&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;active&lt;/b&gt;&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;done&lt;/b&gt;&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;failed&lt;/b&gt;&#x27;][&#x27;Status of the session requested. Returned status:&lt;br/&gt;&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;preparing&lt;/b&gt;&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;active&lt;/b&gt;&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;done&lt;/b&gt;&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;failed&lt;/b&gt;&#x27;]
    :type status: str
    
    :param url: [required] The URL to access the node&#x27;s web server provided only if the session is still active.
    :type url: str
    
    :param attributes: [required] Returns attributes that were specified in the BulkVolumeStatusUpdate method. Values are returned if they have changed or not.
    :type attributes: dict
    """
    status = data_model.property(
        "status", str,
        array=False, optional=False,
        documentation="[&#x27;Status of the session requested. Returned status:&lt;br/&gt;&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;preparing&lt;/b&gt;&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;active&lt;/b&gt;&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;done&lt;/b&gt;&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;failed&lt;/b&gt;&#x27;]",
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


class GetDefaultQoSResult(data_model.DataObject):
    """
    :param qos: [required] Default QoS values.
    :type qos: VolumeQOS
    """
    qos = data_model.property(
        "qos", VolumeQOS,
        array=False, optional=False,
        documentation="Default QoS values.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class VirtualVolumeNullResult(data_model.DataObject):
    """"""

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class ListStorageContainersResult(data_model.DataObject):
    """
    :param storageContainers: [required] 
    :type storageContainers: StorageContainer
    """
    storage_containers = data_model.property(
        "storageContainers", StorageContainer,
        array=True, optional=False,
        documentation="",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class VirtualVolumeTask(data_model.DataObject):
    """
    :param virtualVolumeTaskID: [required] 
    :type virtualVolumeTaskID: UUID
    
    :param virtualvolumeID: [required] 
    :type virtualvolumeID: UUID
    
    :param cloneVirtualVolumeID: [required] 
    :type cloneVirtualVolumeID: UUID
    
    :param status: [required] 
    :type status: str
    
    :param operation: [required] 
    :type operation: str
    
    :param virtualVolumeHostID: [required] 
    :type virtualVolumeHostID: UUID
    
    :param parentMetadata: [required] 
    :type parentMetadata: dict
    
    :param parentTotalSize: [required] 
    :type parentTotalSize: int
    
    :param parentUsedSize: [required] 
    :type parentUsedSize: int
    
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


class GetNetworkConfigResult(data_model.DataObject):
    """
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
    """
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


class GetClusterHardwareInfoResult(data_model.DataObject):
    """
    :param clusterHardwareInfo: [required] Hardware information for all nodes and drives in the cluster. Each object in this output is labeled with the nodeID of the given node.
    :type clusterHardwareInfo: ClusterHardwareInfo
    """
    cluster_hardware_info = data_model.property(
        "clusterHardwareInfo", ClusterHardwareInfo,
        array=False, optional=False,
        documentation="Hardware information for all nodes and drives in the cluster. Each object in this output is labeled with the nodeID of the given node.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class DriveStats(data_model.DataObject):
    """
    :param activeSessions: [required] 
    :type activeSessions: int
    
    :param failedDieCount: [required] 
    :type failedDieCount: int
    
    :param lifeRemainingPercent: [required] 
    :type lifeRemainingPercent: int
    
    :param lifetimeReadBytes: [required] 
    :type lifetimeReadBytes: int
    
    :param lifetimeWriteBytes: [required] 
    :type lifetimeWriteBytes: int
    
    :param powerOnHours: [required] 
    :type powerOnHours: int
    
    :param readBytes: [required] 
    :type readBytes: int
    
    :param readOps: [required] 
    :type readOps: int
    
    :param reallocatedSectors: [required] 
    :type reallocatedSectors: int
    
    :param reserveCapacityPercent: [required] 
    :type reserveCapacityPercent: int
    
    :param timestamp: [required] 
    :type timestamp: str
    
    :param totalCapacity: [required] 
    :type totalCapacity: int
    
    :param usedCapacity:  
    :type usedCapacity: int
    
    :param usedMemory: [required] 
    :type usedMemory: int
    
    :param writeBytes: [required] 
    :type writeBytes: int
    
    :param writeOps: [required] 
    :type writeOps: int
    """
    active_sessions = data_model.property(
        "activeSessions", int,
        array=False, optional=False,
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


class ModifyBackupTargetResult(data_model.DataObject):
    """"""

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class VirtualVolumeUnsharedChunkResult(data_model.DataObject):
    """
    :param chunks: [required] Number of allocated/unshared chunks.
    :type chunks: int
    
    :param scannedChunks: [required] Number of chunks scanned.
    :type scannedChunks: int
    
    :param chunkSize: [required] Size of each chunk.
    :type chunkSize: int
    """
    chunks = data_model.property(
        "chunks", int,
        array=False, optional=False,
        documentation="Number of allocated/unshared chunks.",
        dictionaryType=None
    )
    scanned_chunks = data_model.property(
        "scannedChunks", int,
        array=False, optional=False,
        documentation="Number of chunks scanned.",
        dictionaryType=None
    )
    chunk_size = data_model.property(
        "chunkSize", int,
        array=False, optional=False,
        documentation="Size of each chunk.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class ListUtilitiesResult(data_model.DataObject):
    """
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


class GetFeatureStatusResult(data_model.DataObject):
    """
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


class ClearClusterFaultsResult(data_model.DataObject):
    """"""

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class StartClusterPairingResult(data_model.DataObject):
    """
    :param clusterPairingKey: [required] A string of characters that is used by the &quot;CompleteClusterPairing&quot; API method.
    :type clusterPairingKey: str
    
    :param clusterPairID: [required] Unique identifier for the cluster pair.
    :type clusterPairID: int
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


class GetDriveStatsResult(data_model.DataObject):
    """
    :param driveStats: [required] 
    :type driveStats: DriveStats
    """
    drive_stats = data_model.property(
        "driveStats", DriveStats,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class ListSyncJobsResult(data_model.DataObject):
    """
    :param syncJobs: [required] 
    :type syncJobs: SyncJob
    """
    sync_jobs = data_model.property(
        "syncJobs", SyncJob,
        array=True, optional=False,
        documentation="",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class ListDrivesResult(data_model.DataObject):
    """
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


class CreateSnapshotResult(data_model.DataObject):
    """
    :param snapshotID: [required] ID of the newly-created snapshot.
    :type snapshotID: int
    
    :param checksum: [required] [&#x27;A string that represents the correct digits in the stored snapshot.&#x27;, &#x27;This checksum can be used later to compare other snapshots to detect errors in the data.&#x27;][&#x27;A string that represents the correct digits in the stored snapshot.&#x27;, &#x27;This checksum can be used later to compare other snapshots to detect errors in the data.&#x27;]
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


class GetStorageContainerEfficiencyResult(data_model.DataObject):
    """
    :param compression: [required] 
    :type compression: float
    
    :param deduplication: [required] 
    :type deduplication: float
    
    :param missingVolumes: [required] The volumes that could not be queried for efficiency data. Missing volumes can be caused by the Garbage Collection (GC) cycle being less than an hour old, temporary loss of network connectivity, or restarted services since the GC cycle.
    :type missingVolumes: int
    
    :param thinProvisioning: [required] 
    :type thinProvisioning: float
    
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


class CloneMultipleVolumeParams(data_model.DataObject):
    """
    :param volumeID: [required] Required parameter for &quot;volumes&quot; array: volumeID.
    :type volumeID: int
    
    :param access:  [&#x27;Access settings for the new volume.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;readOnly&lt;/b&gt;: Only read operations are allowed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;readWrite&lt;/b&gt;: Reads and writes are allowed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;locked&lt;/b&gt;: No reads or writes are allowed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;replicationTarget&lt;/b&gt;: Identify a volume as the target volume for a paired set of volumes. If the volume is not paired, the access status is locked.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;If unspecified, the access settings of the clone will be the same as the source.&#x27;][&#x27;Access settings for the new volume.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;readOnly&lt;/b&gt;: Only read operations are allowed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;readWrite&lt;/b&gt;: Reads and writes are allowed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;locked&lt;/b&gt;: No reads or writes are allowed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;replicationTarget&lt;/b&gt;: Identify a volume as the target volume for a paired set of volumes. If the volume is not paired, the access status is locked.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;If unspecified, the access settings of the clone will be the same as the source.&#x27;][&#x27;Access settings for the new volume.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;readOnly&lt;/b&gt;: Only read operations are allowed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;readWrite&lt;/b&gt;: Reads and writes are allowed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;locked&lt;/b&gt;: No reads or writes are allowed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;replicationTarget&lt;/b&gt;: Identify a volume as the target volume for a paired set of volumes. If the volume is not paired, the access status is locked.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;If unspecified, the access settings of the clone will be the same as the source.&#x27;][&#x27;Access settings for the new volume.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;readOnly&lt;/b&gt;: Only read operations are allowed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;readWrite&lt;/b&gt;: Reads and writes are allowed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;locked&lt;/b&gt;: No reads or writes are allowed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;replicationTarget&lt;/b&gt;: Identify a volume as the target volume for a paired set of volumes. If the volume is not paired, the access status is locked.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;If unspecified, the access settings of the clone will be the same as the source.&#x27;][&#x27;Access settings for the new volume.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;readOnly&lt;/b&gt;: Only read operations are allowed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;readWrite&lt;/b&gt;: Reads and writes are allowed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;locked&lt;/b&gt;: No reads or writes are allowed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;replicationTarget&lt;/b&gt;: Identify a volume as the target volume for a paired set of volumes. If the volume is not paired, the access status is locked.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;If unspecified, the access settings of the clone will be the same as the source.&#x27;][&#x27;Access settings for the new volume.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;readOnly&lt;/b&gt;: Only read operations are allowed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;readWrite&lt;/b&gt;: Reads and writes are allowed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;locked&lt;/b&gt;: No reads or writes are allowed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;replicationTarget&lt;/b&gt;: Identify a volume as the target volume for a paired set of volumes. If the volume is not paired, the access status is locked.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;If unspecified, the access settings of the clone will be the same as the source.&#x27;][&#x27;Access settings for the new volume.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;readOnly&lt;/b&gt;: Only read operations are allowed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;readWrite&lt;/b&gt;: Reads and writes are allowed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;locked&lt;/b&gt;: No reads or writes are allowed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;replicationTarget&lt;/b&gt;: Identify a volume as the target volume for a paired set of volumes. If the volume is not paired, the access status is locked.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;If unspecified, the access settings of the clone will be the same as the source.&#x27;]
    :type access: str
    
    :param name:  New name for the clone.
    :type name: str
    
    :param newAccountID:  Account ID for the new volume.
    :type newAccountID: int
    
    :param newSize:  New size Total size of the volume, in bytes. Size is rounded up to the nearest 1MB size.
    :type newSize: int
    
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
        documentation="[&#x27;Access settings for the new volume.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;readOnly&lt;/b&gt;: Only read operations are allowed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;readWrite&lt;/b&gt;: Reads and writes are allowed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;locked&lt;/b&gt;: No reads or writes are allowed.&#x27;, &#x27;&lt;br/&gt;&lt;b&gt;replicationTarget&lt;/b&gt;: Identify a volume as the target volume for a paired set of volumes. If the volume is not paired, the access status is locked.&#x27;, &#x27;&lt;br/&gt;&lt;br/&gt;&#x27;, &#x27;If unspecified, the access settings of the clone will be the same as the source.&#x27;]",
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


class ListNodeStatsResult(data_model.DataObject):
    """
    :param nodeStats: [required] Node activity information for all nodes.
    :type nodeStats: NodeStatsNodes
    """
    node_stats = data_model.property(
        "nodeStats", NodeStatsNodes,
        array=False, optional=False,
        documentation="Node activity information for all nodes.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class ListVolumeAccessGroupsResult(data_model.DataObject):
    """
    :param volumeAccessGroups: [required] List of volume access groups.
    :type volumeAccessGroups: VolumeAccessGroup
    """
    volume_access_groups = data_model.property(
        "volumeAccessGroups", VolumeAccessGroup,
        array=True, optional=False,
        documentation="List of volume access groups.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class GetVolumeAccessGroupLunAssignmentsResult(data_model.DataObject):
    """
    :param volumeAccessGroupLunAssignments: [required] List of all physical Fibre Channel ports, or a port for a single node.
    :type volumeAccessGroupLunAssignments: VolumeAccessGroupLunAssignments
    """
    volume_access_group_lun_assignments = data_model.property(
        "volumeAccessGroupLunAssignments", VolumeAccessGroupLunAssignments,
        array=False, optional=False,
        documentation="List of all physical Fibre Channel ports, or a port for a single node.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class SolidfireDefaults(data_model.DataObject):
    """
    :param sliceFileLogFileCapacity: [required] 
    :type sliceFileLogFileCapacity: int
    
    :param postCallbackThreadCount: [required] 
    :type postCallbackThreadCount: int
    
    :param cpuDmaLatency: [required] 
    :type cpuDmaLatency: int
    
    :param bufferCacheGB: [required] 
    :type bufferCacheGB: int
    
    :param maxIncomingSliceSyncs: [required] 
    :type maxIncomingSliceSyncs: int
    
    :param configuredIops: [required] 
    :type configuredIops: int
    
    :param sCacheFileCapacity: [required] 
    :type sCacheFileCapacity: int
    """
    slice_file_log_file_capacity = data_model.property(
        "sliceFileLogFileCapacity", int,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    post_callback_thread_count = data_model.property(
        "postCallbackThreadCount", int,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    cpu_dma_latency = data_model.property(
        "cpuDmaLatency", int,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    buffer_cache_gb = data_model.property(
        "bufferCacheGB", int,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    max_incoming_slice_syncs = data_model.property(
        "maxIncomingSliceSyncs", int,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    configured_iops = data_model.property(
        "configuredIops", int,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    s_cache_file_capacity = data_model.property(
        "sCacheFileCapacity", int,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class HardwareConfig(data_model.DataObject):
    """
    :param scsiBusInternalDriver: [required] 
    :type scsiBusInternalDriver: str
    
    :param networkDriver: [required] 
    :type networkDriver: str
    
    :param biosRevision: [required] 
    :type biosRevision: str
    
    :param slotOffset: [required] 
    :type slotOffset: int
    
    :param numCpu: [required] 
    :type numCpu: int
    
    :param sliceDrives: [required] 
    :type sliceDrives: str
    
    :param numDrives: [required] 
    :type numDrives: int
    
    :param kernelCrashDump: [required] 
    :type kernelCrashDump: KernelCrashDump
    
    :param blockDriveSizeBytes: [required] 
    :type blockDriveSizeBytes: int
    
    :param cpuModel: [required] 
    :type cpuModel: str
    
    :param bmcFirmwareRevision: [required] 
    :type bmcFirmwareRevision: str
    
    :param cpuCoresEnabled: [required] 
    :type cpuCoresEnabled: int
    
    :param fibreChannelModel: [required] 
    :type fibreChannelModel: str
    
    :param chassisType: [required] 
    :type chassisType: str
    
    :param bmcIpmiVersion: [required] 
    :type bmcIpmiVersion: str
    
    :param nodeType: [required] 
    :type nodeType: str
    
    :param solidfireDefaults: [required] 
    :type solidfireDefaults: SolidfireDefaults
    
    :param idracVersion: [required] 
    :type idracVersion: str
    
    :param blockDrives: [required] 
    :type blockDrives: str
    
    :param biosVendor: [required] 
    :type biosVendor: str
    
    :param fibreChannelFirmwareRevision: [required] 
    :type fibreChannelFirmwareRevision: str
    
    :param scsiBusExternalDriver: [required] 
    :type scsiBusExternalDriver: str
    
    :param numDrivesInternal: [required] 
    :type numDrivesInternal: int
    
    :param sliceDriveSizeBytes: [required] 
    :type sliceDriveSizeBytes: int
    
    :param biosVersion: [required] 
    :type biosVersion: str
    
    :param memoryMhz: [required] 
    :type memoryMhz: int
    
    :param cpuCores: [required] 
    :type cpuCores: int
    
    :param rootDrive: [required] 
    :type rootDrive: str
    
    :param driveSizeBytesInternal: [required] 
    :type driveSizeBytesInternal: int
    
    :param lifecycleVersion: [required] 
    :type lifecycleVersion: str
    
    :param memoryGB: [required] 
    :type memoryGB: int
    
    :param cpuThreads: [required] 
    :type cpuThreads: int
    """
    scsi_bus_internal_driver = data_model.property(
        "scsiBusInternalDriver", str,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    network_driver = data_model.property(
        "networkDriver", str,
        array=True, optional=False,
        documentation="",
        dictionaryType=None
    )
    bios_revision = data_model.property(
        "biosRevision", str,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    slot_offset = data_model.property(
        "slotOffset", int,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    num_cpu = data_model.property(
        "numCpu", int,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    slice_drives = data_model.property(
        "sliceDrives", str,
        array=True, optional=False,
        documentation="",
        dictionaryType=None
    )
    num_drives = data_model.property(
        "numDrives", int,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    kernel_crash_dump = data_model.property(
        "kernelCrashDump", KernelCrashDump,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    block_drive_size_bytes = data_model.property(
        "blockDriveSizeBytes", int,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    cpu_model = data_model.property(
        "cpuModel", str,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    bmc_firmware_revision = data_model.property(
        "bmcFirmwareRevision", str,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    cpu_cores_enabled = data_model.property(
        "cpuCoresEnabled", int,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    fibre_channel_model = data_model.property(
        "fibreChannelModel", str,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    chassis_type = data_model.property(
        "chassisType", str,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    bmc_ipmi_version = data_model.property(
        "bmcIpmiVersion", str,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    node_type = data_model.property(
        "nodeType", str,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    solidfire_defaults = data_model.property(
        "solidfireDefaults", SolidfireDefaults,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    idrac_version = data_model.property(
        "idracVersion", str,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    block_drives = data_model.property(
        "blockDrives", str,
        array=True, optional=False,
        documentation="",
        dictionaryType=None
    )
    bios_vendor = data_model.property(
        "biosVendor", str,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    fibre_channel_firmware_revision = data_model.property(
        "fibreChannelFirmwareRevision", str,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    scsi_bus_external_driver = data_model.property(
        "scsiBusExternalDriver", str,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    num_drives_internal = data_model.property(
        "numDrivesInternal", int,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    slice_drive_size_bytes = data_model.property(
        "sliceDriveSizeBytes", int,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    bios_version = data_model.property(
        "biosVersion", str,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    memory_mhz = data_model.property(
        "memoryMhz", int,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    cpu_cores = data_model.property(
        "cpuCores", int,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    root_drive = data_model.property(
        "rootDrive", str,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    drive_size_bytes_internal = data_model.property(
        "driveSizeBytesInternal", int,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    lifecycle_version = data_model.property(
        "lifecycleVersion", str,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    memory_gb = data_model.property(
        "memoryGB", int,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    cpu_threads = data_model.property(
        "cpuThreads", int,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class RemoveBackupTargetResult(data_model.DataObject):
    """"""

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class TestConnectSvipDetails(data_model.DataObject):
    """
    :param pingBytes: [required] Details of the ping tests with 56 Bytes and 1500 Bytes.
    :type pingBytes: str
    
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


class RestoreDeletedVolumeResult(data_model.DataObject):
    """"""

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class ProtocolEndpointResult(data_model.DataObject):
    """
    :param protocolEndpoint: [required] 
    :type protocolEndpoint: ProtocolEndpoint
    """
    protocol_endpoint = data_model.property(
        "protocolEndpoint", ProtocolEndpoint,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class RemoveClusterPairResult(data_model.DataObject):
    """"""

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class ListVirtualVolumeTasksResult(data_model.DataObject):
    """
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


class GetDriveConfigResult(data_model.DataObject):
    """
    :param driveConfig: [required] [&#x27;Configuration information for the drives that are connected to the cluster&#x27;]
    :type driveConfig: DrivesConfigInfo
    """
    drive_config = data_model.property(
        "driveConfig", DrivesConfigInfo,
        array=False, optional=False,
        documentation="[&#x27;Configuration information for the drives that are connected to the cluster&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class CloneMultipleVolumesResult(data_model.DataObject):
    """
    :param asyncHandle: [required] A value returned from an asynchronous method call.
    :type asyncHandle: int
    
    :param groupCloneID: [required] Unique ID of the new group clone.
    :type groupCloneID: int
    
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


class ModifyAccountResult(data_model.DataObject):
    """"""

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class SetSnmpACLResult(data_model.DataObject):
    """"""

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class StartVolumePairingResult(data_model.DataObject):
    """
    :param volumePairingKey: [required] A string of characters that is used by the &quot;CompleteVolumePairing&quot; API method.
    :type volumePairingKey: str
    """
    volume_pairing_key = data_model.property(
        "volumePairingKey", str,
        array=False, optional=False,
        documentation="A string of characters that is used by the &quot;CompleteVolumePairing&quot; API method.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class SetClusterConfigResult(data_model.DataObject):
    """
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


class QueryVirtualVolumeMetadataResult(data_model.DataObject):
    """
    :param matchingVirtualVolumeIDs: [required] 
    :type matchingVirtualVolumeIDs: UUID
    """
    matching_virtual_volume_ids = data_model.property(
        "matchingVirtualVolumeIDs", UUID,
        array=True, optional=False,
        documentation="",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class ListActivePairedVolumesResult(data_model.DataObject):
    """
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


class ListNetworkInterfacesResult(data_model.DataObject):
    """
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


class GetNvramInfoResult(data_model.DataObject):
    """
    :param nvramInfo: [required] Arrays of events and errors detected on the NVRAM card.
    :type nvramInfo: dict
    """
    nvram_info = data_model.property(
        "nvramInfo", dict,
        array=False, optional=False,
        documentation="Arrays of events and errors detected on the NVRAM card.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class ListVolumesForAccountResult(data_model.DataObject):
    """
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


class DeleteAllSupportBundlesResult(data_model.DataObject):
    """"""

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class AddAccountResult(data_model.DataObject):
    """
    :param accountID: [required] AccountID for the newly created Account.
    :type accountID: int
    """
    account_id = data_model.property(
        "accountID", int,
        array=False, optional=False,
        documentation="AccountID for the newly created Account.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class SetRemoteLoggingHostsResult(data_model.DataObject):
    """"""

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class EnableEncryptionAtRestResult(data_model.DataObject):
    """"""

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class CopyVolumeResult(data_model.DataObject):
    """
    :param cloneID: [required] 
    :type cloneID: int
    
    :param asyncHandle: [required] Handle value used to track the progress of the volume copy.
    :type asyncHandle: int
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


class DeleteStorageContainerResult(data_model.DataObject):
    """"""

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class VirtualVolumeTaskResult(data_model.DataObject):
    """
    :param task: [required] Returns the state of a VVol Async Task.
    :type task: VirtualVolumeTask
    """
    task = data_model.property(
        "task", VirtualVolumeTask,
        array=False, optional=False,
        documentation="Returns the state of a VVol Async Task.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class ListFibreChannelSessionsResult(data_model.DataObject):
    """
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


class CreateVolumeResult(data_model.DataObject):
    """
    :param volumeID: [required] VolumeID for the newly created volume.
    :type volumeID: int
    
    :param curve: [required] [&#x27;The curve is a set of key-value pairs.&#x27;, &#x27;The keys are I/O sizes in bytes.&#x27;, &#x27;The values represent the cost performing an IOP at a specific I/O size.&#x27;, &#x27;The curve is calculated relative to a 4096 byte operation set at 100 IOPS.&#x27;][&#x27;The curve is a set of key-value pairs.&#x27;, &#x27;The keys are I/O sizes in bytes.&#x27;, &#x27;The values represent the cost performing an IOP at a specific I/O size.&#x27;, &#x27;The curve is calculated relative to a 4096 byte operation set at 100 IOPS.&#x27;][&#x27;The curve is a set of key-value pairs.&#x27;, &#x27;The keys are I/O sizes in bytes.&#x27;, &#x27;The values represent the cost performing an IOP at a specific I/O size.&#x27;, &#x27;The curve is calculated relative to a 4096 byte operation set at 100 IOPS.&#x27;][&#x27;The curve is a set of key-value pairs.&#x27;, &#x27;The keys are I/O sizes in bytes.&#x27;, &#x27;The values represent the cost performing an IOP at a specific I/O size.&#x27;, &#x27;The curve is calculated relative to a 4096 byte operation set at 100 IOPS.&#x27;]
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


class DatabaseEntryResult(data_model.DataObject):
    """
    :param data: [required] 
    :type data: dict
    
    :param stat: [required] 
    :type stat: DatabaseStats
    """
    data = data_model.property(
        "data", dict,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )
    stat = data_model.property(
        "stat", DatabaseStats,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class GetCurrentClusterAdminResult(data_model.DataObject):
    """
    :param clusterAdmin: [required] Information about all cluster and LDAP administrators that exist for a cluster.
    :type clusterAdmin: ClusterAdmin
    """
    cluster_admin = data_model.property(
        "clusterAdmin", ClusterAdmin,
        array=False, optional=False,
        documentation="Information about all cluster and LDAP administrators that exist for a cluster.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class DisableSnmpResult(data_model.DataObject):
    """"""

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class CreateScheduleResult(data_model.DataObject):
    """
    :param scheduleID: [required] 
    :type scheduleID: int
    """
    schedule_id = data_model.property(
        "scheduleID", int,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class ListAccountsResult(data_model.DataObject):
    """
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


class RemoveVolumePairResult(data_model.DataObject):
    """"""

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class GetConfigResult(data_model.DataObject):
    """
    :param config: [required] The details of the cluster. Values returned in &quot;config&quot;: cluster- Cluster information that identifies how the node communicates with the cluster it is associated with. (Object) network - Network information for bonding and Ethernet connections. (Object)
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


class GetHardwareConfigResult(data_model.DataObject):
    """
    :param hardwareConfig: [required] List of hardware information and current settings.
    :type hardwareConfig: HardwareConfig
    """
    hardware_config = data_model.property(
        "hardwareConfig", HardwareConfig,
        array=False, optional=False,
        documentation="List of hardware information and current settings.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class ClusterCapacity(data_model.DataObject):
    """
    High level capacity measurements for the entire cluster.
    :param activeBlockSpace: [required] [&#x27;The amount of space on the block drives.&#x27;, &#x27;This includes additional information such as metadata entries and space which can be cleaned up.&#x27;][&#x27;The amount of space on the block drives.&#x27;, &#x27;This includes additional information such as metadata entries and space which can be cleaned up.&#x27;]
    :type activeBlockSpace: int
    
    :param activeSessions: [required] Number of active iSCSI sessions communicating with the cluster
    :type activeSessions: int
    
    :param averageIOPS: [required] Average IPS for the cluster since midnight Coordinated Universal Time (UTC).
    :type averageIOPS: int
    
    :param clusterRecentIOSize: [required] The average size of IOPS to all volumes in the cluster.
    :type clusterRecentIOSize: int
    
    :param currentIOPS: [required] Average IOPS for all volumes in the cluster over the last 5 seconds.
    :type currentIOPS: int
    
    :param maxIOPS: [required] Estimated maximum IOPS capability of the current cluster.
    :type maxIOPS: int
    
    :param maxOverProvisionableSpace: [required] [&#x27;The maximum amount of provisionable space.&#x27;, &#x27;This is a computed value.&#x27;, &#x27;You cannot create new volumes if the current provisioned space plus the new volume size would exceed this number:&#x27;, &#x27;maxOverProvisionableSpace = maxProvisionedSpace * GetClusterFull&#x27;][&#x27;The maximum amount of provisionable space.&#x27;, &#x27;This is a computed value.&#x27;, &#x27;You cannot create new volumes if the current provisioned space plus the new volume size would exceed this number:&#x27;, &#x27;maxOverProvisionableSpace = maxProvisionedSpace * GetClusterFull&#x27;][&#x27;The maximum amount of provisionable space.&#x27;, &#x27;This is a computed value.&#x27;, &#x27;You cannot create new volumes if the current provisioned space plus the new volume size would exceed this number:&#x27;, &#x27;maxOverProvisionableSpace = maxProvisionedSpace * GetClusterFull&#x27;][&#x27;The maximum amount of provisionable space.&#x27;, &#x27;This is a computed value.&#x27;, &#x27;You cannot create new volumes if the current provisioned space plus the new volume size would exceed this number:&#x27;, &#x27;maxOverProvisionableSpace = maxProvisionedSpace * GetClusterFull&#x27;]
    :type maxOverProvisionableSpace: int
    
    :param maxProvisionedSpace: [required] The total amount of provisionable space if all volumes are 100% filled (no thin provisioned metadata).
    :type maxProvisionedSpace: int
    
    :param maxUsedMetadataSpace: [required] The amount of bytes on volume drives used to store metadata.
    :type maxUsedMetadataSpace: int
    
    :param maxUsedSpace: [required] The total amount of space on all active block drives.
    :type maxUsedSpace: int
    
    :param nonZeroBlocks: [required] Total number of 4KiB blocks with data after the last garbage collection operation has completed.
    :type nonZeroBlocks: int
    
    :param peakActiveSessions: [required] Peak number of iSCSI connections since midnight UTC.
    :type peakActiveSessions: int
    
    :param peakIOPS: [required] The highest value for currentIOPS since midnight UTC.
    :type peakIOPS: int
    
    :param provisionedSpace: [required] Total amount of space provisioned in all volumes on the cluster.
    :type provisionedSpace: int
    
    :param snapshotNonZeroBlocks: [required] Total number of 4KiB blocks in snapshots with data.
    :type snapshotNonZeroBlocks: int
    
    :param timestamp: [required] The date and time this cluster capacity sample was taken.
    :type timestamp: str
    
    :param totalOps: [required] The total number of I/O operations performed throughout the lifetime of the cluster
    :type totalOps: int
    
    :param uniqueBlocks: [required] [&#x27;The total number of blocks stored on the block drives.&#x27;, &#x27;The value includes replicated blocks.&#x27;][&#x27;The total number of blocks stored on the block drives.&#x27;, &#x27;The value includes replicated blocks.&#x27;]
    :type uniqueBlocks: int
    
    :param uniqueBlocksUsedSpace: [required] [&#x27;The total amount of data the uniqueBlocks take up on the block drives.&#x27;, &#x27;This number is always consistent with the uniqueBlocks value.&#x27;][&#x27;The total amount of data the uniqueBlocks take up on the block drives.&#x27;, &#x27;This number is always consistent with the uniqueBlocks value.&#x27;]
    :type uniqueBlocksUsedSpace: int
    
    :param usedMetadataSpace: [required] The total amount of bytes on volume drives used to store metadata
    :type usedMetadataSpace: int
    
    :param usedMetadataSpaceInSnapshots: [required] [&#x27;The amount of bytes on volume drives used for storing unique data in snapshots.&#x27;, &#x27;This number provides an estimate of how much metadata space would be regained by deleting all snapshots on the system.&#x27;][&#x27;The amount of bytes on volume drives used for storing unique data in snapshots.&#x27;, &#x27;This number provides an estimate of how much metadata space would be regained by deleting all snapshots on the system.&#x27;]
    :type usedMetadataSpaceInSnapshots: int
    
    :param usedSpace: [required] Total amount of space used by all block drives in the system.
    :type usedSpace: int
    
    :param zeroBlocks: [required] Total number of 4KiB blocks without data after the last round of garabage collection operation has completed.
    :type zeroBlocks: int
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
    """
    :param clusterCapacity: [required] 
    :type clusterCapacity: ClusterCapacity
    """
    cluster_capacity = data_model.property(
        "clusterCapacity", ClusterCapacity,
        array=False, optional=False,
        documentation="",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class GetSnmpTrapInfoResult(data_model.DataObject):
    """
    :param trapRecipients: [required] List of hosts that are to receive the traps generated by the cluster.
    :type trapRecipients: SnmpTrapRecipient
    
    :param clusterFaultTrapsEnabled: [required] If &quot;true&quot;, when a cluster fault is logged a corresponding solidFireClusterFaultNotification is sent to the configured list of trap recipients.
    :type clusterFaultTrapsEnabled: bool
    
    :param clusterFaultResolvedTrapsEnabled: [required] If &quot;true&quot;, when a cluster fault is logged a corresponding solidFireClusterFaultResolvedNotification is sent to the configured list of trap recipients.
    :type clusterFaultResolvedTrapsEnabled: bool
    
    :param clusterEventTrapsEnabled: [required] If &quot;true&quot;, when a cluster fault is logged a corresponding solidFireClusterEventNotification is sent to the configured list of trap recipients.
    :type clusterEventTrapsEnabled: bool
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


class GetSystemStatusResult(data_model.DataObject):
    """
    :param nodes: [required] 
    :type nodes: NodeSystemStatus
    """
    nodes = data_model.property(
        "nodes", NodeSystemStatus,
        array=True, optional=False,
        documentation="",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class ListBackupTargetsResult(data_model.DataObject):
    """
    :param backupTargets: [required] Objects returned for each backup target.
    :type backupTargets: BackupTarget
    """
    backup_targets = data_model.property(
        "backupTargets", BackupTarget,
        array=True, optional=False,
        documentation="Objects returned for each backup target.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class GetNodeStatsResult(data_model.DataObject):
    """
    :param nodeStats: [required] Node activity information.
    :type nodeStats: NodeStatsInfo
    """
    node_stats = data_model.property(
        "nodeStats", NodeStatsInfo,
        array=False, optional=False,
        documentation="Node activity information.",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)


class GetSnmpStateResult(data_model.DataObject):
    """
    :param enabled: [required] If the nodes in the cluster are configured for SNMP.
    :type enabled: bool
    
    :param snmpV3Enabled: [required] If the node in the cluster is configured for SNMP v3.
    :type snmpV3Enabled: bool
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


class TestConnectSvipResult(data_model.DataObject):
    """
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


class CloneVolumeResult(data_model.DataObject):
    """
    :param cloneID: [required] The ID of the newly-created clone.
    :type cloneID: int
    
    :param volumeID: [required] The volume ID of the newly-created clone.
    :type volumeID: int
    
    :param asyncHandle: [required] Handle value used to track the progress of the clone.
    :type asyncHandle: int
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
