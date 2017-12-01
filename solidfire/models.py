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

class RemoveClusterAdminRequest(data_model.DataObject):
    """RemoveClusterAdminRequest  
    You can use RemoveClusterAdmin to remove a Cluster Admin. You cannot remove the administrator cluster admin account.

    :param cluster_admin_id: [required] ClusterAdminID for the cluster admin to remove. 
    :type cluster_admin_id: int

    """
    cluster_admin_id = data_model.property(
        "clusterAdminID", int,
        array=False, optional=False,
        documentation="""ClusterAdminID for the cluster admin to remove. """,
        dictionaryType=None
    )

    def __init__(self,
            cluster_admin_id):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class TestDrivesResult(data_model.DataObject):
    """TestDrivesResult  

    :param details: [required]  
    :type details: str

    :param duration: [required]  
    :type duration: str

    :param result: [required]  
    :type result: str

    """
    details = data_model.property(
        "details", str,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    duration = data_model.property(
        "duration", str,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    result = data_model.property(
        "result", str,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )

    def __init__(self,
            details,
            duration,
            result):
        kwargs = locals()
        del kwargs["self"]
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
        documentation=""" """,
        dictionaryType=None
    )
    cluster_id = data_model.property(
        "clusterID", UUID,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    visible_protocol_endpoint_ids = data_model.property(
        "visibleProtocolEndpointIDs", UUID,
        array=True, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    bindings = data_model.property(
        "bindings", int,
        array=True, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    initiator_names = data_model.property(
        "initiatorNames", str,
        array=True, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    host_address = data_model.property(
        "hostAddress", str,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )

    def __init__(self,
            virtual_volume_host_id,
            cluster_id,
            visible_protocol_endpoint_ids,
            bindings,
            initiator_names,
            host_address):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class ListVirtualVolumeHostsResult(data_model.DataObject):
    """ListVirtualVolumeHostsResult  

    :param hosts: [required] List of known ESX hosts. 
    :type hosts: VirtualVolumeHost

    """
    hosts = data_model.property(
        "hosts", VirtualVolumeHost,
        array=True, optional=False,
        documentation="""List of known ESX hosts. """,
        dictionaryType=None
    )

    def __init__(self,
            hosts):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class GetNodeSSLCertificateResult(data_model.DataObject):
    """GetNodeSSLCertificateResult  

    :param certificate: [required] The full PEM-encoded test of the certificate. 
    :type certificate: str

    :param details: [required] The decoded information of the certificate. 
    :type details: dict

    """
    certificate = data_model.property(
        "certificate", str,
        array=False, optional=False,
        documentation="""The full PEM-encoded test of the certificate. """,
        dictionaryType=None
    )
    details = data_model.property(
        "details", dict,
        array=False, optional=False,
        documentation="""The decoded information of the certificate. """,
        dictionaryType=None
    )

    def __init__(self,
            certificate,
            details):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class AddVolumesToVolumeAccessGroupRequest(data_model.DataObject):
    """AddVolumesToVolumeAccessGroupRequest  
    AddVolumesToVolumeAccessGroup enables you to add
    volumes to a specified volume access group.

    :param volume_access_group_id: [required] The ID of the volume access group to which volumes are added. 
    :type volume_access_group_id: int

    :param volumes: [required] The list of volumes to add to the volume access group. 
    :type volumes: int

    """
    volume_access_group_id = data_model.property(
        "volumeAccessGroupID", int,
        array=False, optional=False,
        documentation="""The ID of the volume access group to which volumes are added. """,
        dictionaryType=None
    )
    volumes = data_model.property(
        "volumes", int,
        array=True, optional=False,
        documentation="""The list of volumes to add to the volume access group. """,
        dictionaryType=None
    )

    def __init__(self,
            volume_access_group_id,
            volumes):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class CreateGroupSnapshotRequest(data_model.DataObject):
    """CreateGroupSnapshotRequest  
    CreateGroupSnapshot enables you to create a point-in-time copy of a group of volumes. You can use this snapshot later as a backup or rollback to ensure the data on the group of volumes is consistent for the point in time that you created the snapshot.
    Note: Creating a group snapshot is allowed if cluster fullness is at stage 2 or 3. Snapshots are not created when cluster fullness is at stage 4 or 5.

    :param volumes: [required] Unique ID of the volume image from which to copy. 
    :type volumes: int

    :param name:  Name for the group snapshot. If unspecified, the date and time the group snapshot was taken is used. 
    :type name: str

    :param enable_remote_replication:  Replicates the snapshot created to remote storage. Possible values are: true: The snapshot is replicated to remote storage. false: Default. The snapshot is not replicated. 
    :type enable_remote_replication: bool

    :param retention:  Specifies the amount of time for which the snapshots are retained. The format is HH:mm:ss. 
    :type retention: str

    :param attributes:  List of name-value pairs in JSON object format. 
    :type attributes: dict

    :param snap_mirror_label:  Label used by SnapMirror software to specify snapshot retention policy on SnapMirror endpoint. 
    :type snap_mirror_label: str

    """
    volumes = data_model.property(
        "volumes", int,
        array=True, optional=False,
        documentation="""Unique ID of the volume image from which to copy. """,
        dictionaryType=None
    )
    name = data_model.property(
        "name", str,
        array=False, optional=True,
        documentation="""Name for the group snapshot. If unspecified, the date and time the group snapshot was taken is used. """,
        dictionaryType=None
    )
    enable_remote_replication = data_model.property(
        "enableRemoteReplication", bool,
        array=False, optional=True,
        documentation="""Replicates the snapshot created to remote storage. Possible values are: true: The snapshot is replicated to remote storage. false: Default. The snapshot is not replicated. """,
        dictionaryType=None
    )
    retention = data_model.property(
        "retention", str,
        array=False, optional=True,
        documentation="""Specifies the amount of time for which the snapshots are retained. The format is HH:mm:ss. """,
        dictionaryType=None
    )
    attributes = data_model.property(
        "attributes", dict,
        array=False, optional=True,
        documentation="""List of name-value pairs in JSON object format. """,
        dictionaryType=None
    )
    snap_mirror_label = data_model.property(
        "snapMirrorLabel", str,
        array=False, optional=True,
        documentation="""Label used by SnapMirror software to specify snapshot retention policy on SnapMirror endpoint. """,
        dictionaryType=None
    )

    def __init__(self,
            volumes,
            name=None,
            enable_remote_replication=None,
            retention=None,
            attributes=None,
            snap_mirror_label=None):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class GetSSLCertificateResult(data_model.DataObject):
    """GetSSLCertificateResult  

    :param certificate: [required] The full PEM-encoded test of the certificate. 
    :type certificate: str

    :param details: [required] The decoded information of the certificate. 
    :type details: dict

    """
    certificate = data_model.property(
        "certificate", str,
        array=False, optional=False,
        documentation="""The full PEM-encoded test of the certificate. """,
        dictionaryType=None
    )
    details = data_model.property(
        "details", dict,
        array=False, optional=False,
        documentation="""The decoded information of the certificate. """,
        dictionaryType=None
    )

    def __init__(self,
            certificate,
            details):
        kwargs = locals()
        del kwargs["self"]
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

    :param encryption_capable:   
    :type encryption_capable: bool

    :param has_local_admin:   
    :type has_local_admin: bool

    :param version:   
    :type version: str

    """
    cipi = data_model.property(
        "cipi", str,
        array=False, optional=True,
        documentation="""Network interface used for cluster communication. """,
        dictionaryType=None
    )
    cluster = data_model.property(
        "cluster", str,
        array=False, optional=True,
        documentation="""Unique cluster name. """,
        dictionaryType=None
    )
    ensemble = data_model.property(
        "ensemble", str,
        array=True, optional=True,
        documentation="""Nodes that are participating in the cluster. """,
        dictionaryType=None
    )
    mipi = data_model.property(
        "mipi", str,
        array=False, optional=True,
        documentation="""Network interface used for node management. """,
        dictionaryType=None
    )
    name = data_model.property(
        "name", str,
        array=False, optional=True,
        documentation="""Unique cluster name. """,
        dictionaryType=None
    )
    node_id = data_model.property(
        "nodeID", int,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )
    pending_node_id = data_model.property(
        "pendingNodeID", int,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )
    role = data_model.property(
        "role", str,
        array=False, optional=True,
        documentation="""Identifies the role of the node """,
        dictionaryType=None
    )
    sipi = data_model.property(
        "sipi", str,
        array=False, optional=True,
        documentation="""Network interface used for storage. """,
        dictionaryType=None
    )
    state = data_model.property(
        "state", str,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )
    encryption_capable = data_model.property(
        "encryptionCapable", bool,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )
    has_local_admin = data_model.property(
        "hasLocalAdmin", bool,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )
    version = data_model.property(
        "version", str,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )

    def __init__(self,
            cipi=None,
            cluster=None,
            ensemble=None,
            mipi=None,
            name=None,
            node_id=None,
            pending_node_id=None,
            role=None,
            sipi=None,
            state=None,
            encryption_capable=None,
            has_local_admin=None,
            version=None):
        kwargs = locals()
        del kwargs["self"]
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
        documentation=""" """,
        dictionaryType=None
    )
    mac_address = data_model.property(
        "macAddress", str,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )
    mac_address_permanent = data_model.property(
        "macAddressPermanent", str,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )
    mtu = data_model.property(
        "mtu", str,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )
    netmask = data_model.property(
        "netmask", str,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )
    network = data_model.property(
        "network", str,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )
    up_and_running = data_model.property(
        "upAndRunning", bool,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )

    def __init__(self,
            address=None,
            mac_address=None,
            mac_address_permanent=None,
            mtu=None,
            netmask=None,
            network=None,
            up_and_running=None):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class NetworkConfig(data_model.DataObject):
    """NetworkConfig  

    :param _default:   
    :type _default: bool

    :param bond_master:   
    :type bond_master: str

    :param virtual_network_tag:   
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
    :type routes: dict

    :param status:   
    :type status: str

    :param symmetric_route_rules:   
    :type symmetric_route_rules: str

    :param up_and_running:   
    :type up_and_running: bool

    :param bond_xmit_hash_policy:   
    :type bond_xmit_hash_policy: str

    :param bond_ad_num_ports:   
    :type bond_ad_num_ports: str

    """
    _default = data_model.property(
        "#default", bool,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )
    bond_master = data_model.property(
        "bond-master", str,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )
    virtual_network_tag = data_model.property(
        "virtualNetworkTag", str,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )
    address = data_model.property(
        "address", str,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )
    auto = data_model.property(
        "auto", bool,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )
    bond_downdelay = data_model.property(
        "bond-downdelay", str,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )
    bond_fail_over_mac = data_model.property(
        "bond-fail_over_mac", str,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )
    bond_primary_reselect = data_model.property(
        "bond-primary_reselect", str,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )
    bond_lacp_rate = data_model.property(
        "bond-lacp_rate", str,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )
    bond_miimon = data_model.property(
        "bond-miimon", str,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )
    bond_mode = data_model.property(
        "bond-mode", str,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )
    bond_slaves = data_model.property(
        "bond-slaves", str,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )
    bond_updelay = data_model.property(
        "bond-updelay", str,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )
    dns_nameservers = data_model.property(
        "dns-nameservers", str,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )
    dns_search = data_model.property(
        "dns-search", str,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )
    family = data_model.property(
        "family", str,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )
    gateway = data_model.property(
        "gateway", str,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )
    mac_address = data_model.property(
        "macAddress", str,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )
    mac_address_permanent = data_model.property(
        "macAddressPermanent", str,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )
    method = data_model.property(
        "method", str,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )
    mtu = data_model.property(
        "mtu", str,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )
    netmask = data_model.property(
        "netmask", str,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )
    network = data_model.property(
        "network", str,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )
    physical = data_model.property(
        "physical", PhysicalAdapter,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )
    routes = data_model.property(
        "routes", dict,
        array=True, optional=True,
        documentation=""" """,
        dictionaryType=None
    )
    status = data_model.property(
        "status", str,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )
    symmetric_route_rules = data_model.property(
        "symmetricRouteRules", str,
        array=True, optional=True,
        documentation=""" """,
        dictionaryType=None
    )
    up_and_running = data_model.property(
        "upAndRunning", bool,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )
    bond_xmit_hash_policy = data_model.property(
        "bond-xmit_hash_policy", str,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )
    bond_ad_num_ports = data_model.property(
        "bond-ad_num_ports", str,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )

    def __init__(self,
            _default=None,
            bond_master=None,
            virtual_network_tag=None,
            address=None,
            auto=None,
            bond_downdelay=None,
            bond_fail_over_mac=None,
            bond_primary_reselect=None,
            bond_lacp_rate=None,
            bond_miimon=None,
            bond_mode=None,
            bond_slaves=None,
            bond_updelay=None,
            dns_nameservers=None,
            dns_search=None,
            family=None,
            gateway=None,
            mac_address=None,
            mac_address_permanent=None,
            method=None,
            mtu=None,
            netmask=None,
            network=None,
            physical=None,
            routes=None,
            status=None,
            symmetric_route_rules=None,
            up_and_running=None,
            bond_xmit_hash_policy=None,
            bond_ad_num_ports=None):
        kwargs = locals()
        del kwargs["self"]
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

    :param eth4:   
    :type eth4: NetworkConfig

    :param eth5:   
    :type eth5: NetworkConfig

    :param lo:   
    :type lo: NetworkConfig

    """
    bond10_g = data_model.property(
        "Bond10G", NetworkConfig,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )
    bond1_g = data_model.property(
        "Bond1G", NetworkConfig,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )
    eth0 = data_model.property(
        "eth0", NetworkConfig,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )
    eth1 = data_model.property(
        "eth1", NetworkConfig,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )
    eth2 = data_model.property(
        "eth2", NetworkConfig,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )
    eth3 = data_model.property(
        "eth3", NetworkConfig,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )
    eth4 = data_model.property(
        "eth4", NetworkConfig,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )
    eth5 = data_model.property(
        "eth5", NetworkConfig,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )
    lo = data_model.property(
        "lo", NetworkConfig,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )

    def __init__(self,
            bond10_g=None,
            bond1_g=None,
            eth0=None,
            eth1=None,
            eth2=None,
            eth3=None,
            eth4=None,
            eth5=None,
            lo=None):
        kwargs = locals()
        del kwargs["self"]
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
        documentation=""" """,
        dictionaryType=None
    )
    network = data_model.property(
        "network", Network,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )

    def __init__(self,
            cluster,
            network):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class GetConfigResult(data_model.DataObject):
    """GetConfigResult  

    :param config: [required] The details of the cluster. Values returned in "config": cluster- Cluster information that identifies how the node communicates with the cluster it is associated with. (Object) network - Network information for bonding and Ethernet connections. (Object) 
    :type config: Config

    """
    config = data_model.property(
        "config", Config,
        array=False, optional=False,
        documentation="""The details of the cluster. Values returned in "config": cluster- Cluster information that identifies how the node communicates with the cluster it is associated with. (Object) network - Network information for bonding and Ethernet connections. (Object) """,
        dictionaryType=None
    )

    def __init__(self,
            config):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class StartVolumePairingResult(data_model.DataObject):
    """StartVolumePairingResult  

    :param volume_pairing_key: [required] A string of characters that is used by the "CompleteVolumePairing" API method. 
    :type volume_pairing_key: str

    """
    volume_pairing_key = data_model.property(
        "volumePairingKey", str,
        array=False, optional=False,
        documentation="""A string of characters that is used by the "CompleteVolumePairing" API method. """,
        dictionaryType=None
    )

    def __init__(self,
            volume_pairing_key):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class SetSSLCertificateResult(data_model.DataObject):
    """SetSSLCertificateResult  

    """

    def __init__(self):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class UpdateBulkVolumeStatusRequest(data_model.DataObject):
    """UpdateBulkVolumeStatusRequest  
    You can use UpdateBulkVolumeStatus in a script to update the status of a bulk volume job that you started with the
    StartBulkVolumeRead or StartBulkVolumeWrite methods.

    :param key: [required] The key assigned during initialization of a StartBulkVolumeRead or StartBulkVolumeWrite session. 
    :type key: str

    :param status: [required] The status of the given bulk volume job. The system sets the status. Possible values are:  running: Jobs that are still active. complete: Jobs that are done. failed: Jobs that failed. 
    :type status: str

    :param percent_complete:  The completed progress of the bulk volume job as a percentage value. 
    :type percent_complete: str

    :param message:  The message returned indicating the status of the bulk volume job after the job is complete. 
    :type message: str

    :param attributes:  JSON attributes; updates what is on the bulk volume job. 
    :type attributes: dict

    """
    key = data_model.property(
        "key", str,
        array=False, optional=False,
        documentation="""The key assigned during initialization of a StartBulkVolumeRead or StartBulkVolumeWrite session. """,
        dictionaryType=None
    )
    status = data_model.property(
        "status", str,
        array=False, optional=False,
        documentation="""The status of the given bulk volume job. The system sets the status. Possible values are:  running: Jobs that are still active. complete: Jobs that are done. failed: Jobs that failed. """,
        dictionaryType=None
    )
    percent_complete = data_model.property(
        "percentComplete", str,
        array=False, optional=True,
        documentation="""The completed progress of the bulk volume job as a percentage value. """,
        dictionaryType=None
    )
    message = data_model.property(
        "message", str,
        array=False, optional=True,
        documentation="""The message returned indicating the status of the bulk volume job after the job is complete. """,
        dictionaryType=None
    )
    attributes = data_model.property(
        "attributes", dict,
        array=False, optional=True,
        documentation="""JSON attributes; updates what is on the bulk volume job. """,
        dictionaryType=None
    )

    def __init__(self,
            key,
            status,
            percent_complete=None,
            message=None,
            attributes=None):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class GetAccountEfficiencyRequest(data_model.DataObject):
    """GetAccountEfficiencyRequest  
    GetAccountEfficiency enables you to retrieve efficiency statistics about a volume account. This method returns efficiency information
    only for the account you specify as a parameter.

    :param account_id: [required] Specifies the volume account for which efficiency statistics are returned. 
    :type account_id: int

    """
    account_id = data_model.property(
        "accountID", int,
        array=False, optional=False,
        documentation="""Specifies the volume account for which efficiency statistics are returned. """,
        dictionaryType=None
    )

    def __init__(self,
            account_id):
        kwargs = locals()
        del kwargs["self"]
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

    :param platform_config_version:   
    :type platform_config_version: str

    """
    node_type = data_model.property(
        "nodeType", str,
        array=False, optional=False,
        documentation="""SolidFire's name for this platform. """,
        dictionaryType=None
    )
    chassis_type = data_model.property(
        "chassisType", str,
        array=False, optional=False,
        documentation="""Name of the chassis (example: "R620"). """,
        dictionaryType=None
    )
    cpu_model = data_model.property(
        "cpuModel", str,
        array=False, optional=False,
        documentation="""The model of CPU used on this platform. """,
        dictionaryType=None
    )
    node_memory_gb = data_model.property(
        "nodeMemoryGB", int,
        array=False, optional=False,
        documentation="""The amount of memory on this platform in GiB. """,
        dictionaryType=None
    )
    platform_config_version = data_model.property(
        "platformConfigVersion", str,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )

    def __init__(self,
            node_type,
            chassis_type,
            cpu_model,
            node_memory_gb,
            platform_config_version=None):
        kwargs = locals()
        del kwargs["self"]
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
        documentation="""SolidFire unique identifier for a virtual network. """,
        dictionaryType=None
    )
    address = data_model.property(
        "address", str,
        array=False, optional=False,
        documentation="""Virtual Network Address. """,
        dictionaryType=None
    )

    def __init__(self,
            virtual_network_id,
            address):
        kwargs = locals()
        del kwargs["self"]
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

    :param fibre_channel_target_port_group:   
    :type fibre_channel_target_port_group: int

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

    :param node_slot:   
    :type node_slot: str

    """
    node_id = data_model.property(
        "nodeID", int,
        array=False, optional=False,
        documentation="""The unique identifier for this node. """,
        dictionaryType=None
    )
    associated_master_service_id = data_model.property(
        "associatedMasterServiceID", int,
        array=False, optional=False,
        documentation="""The master service responsible for controlling other services on this node. """,
        dictionaryType=None
    )
    associated_fservice_id = data_model.property(
        "associatedFServiceID", int,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    fibre_channel_target_port_group = data_model.property(
        "fibreChannelTargetPortGroup", int,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )
    name = data_model.property(
        "name", str,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    platform_info = data_model.property(
        "platformInfo", Platform,
        array=False, optional=False,
        documentation="""Information about the platform this node is. """,
        dictionaryType=None
    )
    software_version = data_model.property(
        "softwareVersion", str,
        array=False, optional=False,
        documentation="""The version of SolidFire software this node is currently running. """,
        dictionaryType=None
    )
    cip = data_model.property(
        "cip", str,
        array=False, optional=False,
        documentation="""IP address used for both intra- and inter-cluster communication. """,
        dictionaryType=None
    )
    cipi = data_model.property(
        "cipi", str,
        array=False, optional=False,
        documentation="""The machine's name for the "cip" interface. """,
        dictionaryType=None
    )
    mip = data_model.property(
        "mip", str,
        array=False, optional=False,
        documentation="""IP address used for cluster management (hosting the API and web site). """,
        dictionaryType=None
    )
    mipi = data_model.property(
        "mipi", str,
        array=False, optional=False,
        documentation="""The machine's name for the "mip" interface. """,
        dictionaryType=None
    )
    sip = data_model.property(
        "sip", str,
        array=False, optional=False,
        documentation="""IP address used for iSCSI traffic. """,
        dictionaryType=None
    )
    sipi = data_model.property(
        "sipi", str,
        array=False, optional=False,
        documentation="""The machine's name for the "sip" interface. """,
        dictionaryType=None
    )
    uuid = data_model.property(
        "uuid", UUID,
        array=False, optional=False,
        documentation="""UUID of node. """,
        dictionaryType=None
    )
    virtual_networks = data_model.property(
        "virtualNetworks", VirtualNetworkAddress,
        array=True, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    attributes = data_model.property(
        "attributes", dict,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    node_slot = data_model.property(
        "nodeSlot", str,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )

    def __init__(self,
            node_id,
            associated_master_service_id,
            associated_fservice_id,
            name,
            platform_info,
            software_version,
            cip,
            cipi,
            mip,
            mipi,
            sip,
            sipi,
            uuid,
            virtual_networks,
            attributes,
            fibre_channel_target_port_group=None,
            node_slot=None):
        kwargs = locals()
        del kwargs["self"]
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

    :param node_slot:  UUID of node. 
    :type node_slot: str

    """
    pending_node_id = data_model.property(
        "pendingNodeID", int,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    assigned_node_id = data_model.property(
        "assignedNodeID", int,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    name = data_model.property(
        "name", str,
        array=False, optional=False,
        documentation="""The host name for this node. """,
        dictionaryType=None
    )
    compatible = data_model.property(
        "compatible", bool,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    platform_info = data_model.property(
        "platformInfo", Platform,
        array=False, optional=False,
        documentation="""Information about the platform this node is. """,
        dictionaryType=None
    )
    cip = data_model.property(
        "cip", str,
        array=False, optional=False,
        documentation="""IP address used for both intra- and inter-cluster communication. """,
        dictionaryType=None
    )
    cipi = data_model.property(
        "cipi", str,
        array=False, optional=False,
        documentation="""The machine's name for the "cip" interface. """,
        dictionaryType=None
    )
    mip = data_model.property(
        "mip", str,
        array=False, optional=False,
        documentation="""IP address used for cluster management (hosting the API and web site). """,
        dictionaryType=None
    )
    mipi = data_model.property(
        "mipi", str,
        array=False, optional=False,
        documentation="""The machine's name for the "mip" interface. """,
        dictionaryType=None
    )
    sip = data_model.property(
        "sip", str,
        array=False, optional=False,
        documentation="""IP address used for iSCSI traffic. """,
        dictionaryType=None
    )
    sipi = data_model.property(
        "sipi", str,
        array=False, optional=False,
        documentation="""The machine's name for the "sip" interface. """,
        dictionaryType=None
    )
    software_version = data_model.property(
        "softwareVersion", str,
        array=False, optional=False,
        documentation="""The version of SolidFire software this node is currently running. """,
        dictionaryType=None
    )
    uuid = data_model.property(
        "uuid", UUID,
        array=False, optional=False,
        documentation="""UUID of node. """,
        dictionaryType=None
    )
    node_slot = data_model.property(
        "nodeSlot", str,
        array=False, optional=True,
        documentation="""UUID of node. """,
        dictionaryType=None
    )

    def __init__(self,
            pending_node_id,
            assigned_node_id,
            name,
            compatible,
            platform_info,
            cip,
            cipi,
            mip,
            mipi,
            sip,
            sipi,
            software_version,
            uuid,
            node_slot=None):
        kwargs = locals()
        del kwargs["self"]
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
        documentation=""" """,
        dictionaryType=None
    )
    assigned_node_id = data_model.property(
        "assignedNodeID", int,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    async_handle = data_model.property(
        "asyncHandle", int,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    cip = data_model.property(
        "cip", str,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    mip = data_model.property(
        "mip", str,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    pending_node_id = data_model.property(
        "pendingNodeID", int,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    platform_info = data_model.property(
        "platformInfo", Platform,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    sip = data_model.property(
        "sip", str,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    software_version = data_model.property(
        "softwareVersion", str,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )

    def __init__(self,
            active_node_key,
            assigned_node_id,
            async_handle,
            cip,
            mip,
            pending_node_id,
            platform_info,
            sip,
            software_version):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class ListAllNodesResult(data_model.DataObject):
    """ListAllNodesResult  

    :param nodes: [required]  
    :type nodes: Node

    :param pending_nodes: [required]  
    :type pending_nodes: PendingNode

    :param pending_active_nodes:  List of objects detailing information about all PendingActive nodes in the system. 
    :type pending_active_nodes: PendingActiveNode

    """
    nodes = data_model.property(
        "nodes", Node,
        array=True, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    pending_nodes = data_model.property(
        "pendingNodes", PendingNode,
        array=True, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    pending_active_nodes = data_model.property(
        "pendingActiveNodes", PendingActiveNode,
        array=True, optional=True,
        documentation="""List of objects detailing information about all PendingActive nodes in the system. """,
        dictionaryType=None
    )

    def __init__(self,
            nodes,
            pending_nodes,
            pending_active_nodes=None):
        kwargs = locals()
        del kwargs["self"]
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
        documentation=""" """,
        dictionaryType=None
    )
    successful = data_model.property(
        "successful", int,
        array=True, optional=False,
        documentation=""" """,
        dictionaryType=None
    )

    def __init__(self,
            failed,
            successful):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class GetAPIResult(data_model.DataObject):
    """GetAPIResult  

    :param supported_versions: [required]  
    :type supported_versions: float

    :param current_version: [required]  
    :type current_version: float

    """
    supported_versions = data_model.property(
        "supportedVersions", float,
        array=True, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    current_version = data_model.property(
        "currentVersion", float,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )

    def __init__(self,
            supported_versions,
            current_version):
        kwargs = locals()
        del kwargs["self"]
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
        documentation="""The volume ID assigned to the Lun. """,
        dictionaryType=None
    )
    lun = data_model.property(
        "lun", int,
        array=False, optional=False,
        documentation="""Correct LUN values are 0 - 16383. An exception will be seen if an incorrect LUN value is passed. """,
        dictionaryType=None
    )

    def __init__(self,
            volume_id,
            lun):
        kwargs = locals()
        del kwargs["self"]
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
        documentation="""Unique volume access group ID for which the LUN assignments will be modified. """,
        dictionaryType=None
    )
    lun_assignments = data_model.property(
        "lunAssignments", LunAssignment,
        array=True, optional=False,
        documentation="""The volume IDs with assigned LUN values. """,
        dictionaryType=None
    )
    deleted_lun_assignments = data_model.property(
        "deletedLunAssignments", LunAssignment,
        array=True, optional=False,
        documentation="""The volume IDs with deleted LUN values. """,
        dictionaryType=None
    )

    def __init__(self,
            volume_access_group_id,
            lun_assignments,
            deleted_lun_assignments):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class GetVolumeAccessGroupLunAssignmentsResult(data_model.DataObject):
    """GetVolumeAccessGroupLunAssignmentsResult  

    :param volume_access_group_lun_assignments: [required] List of all physical Fibre Channel ports, or a port for a single node. 
    :type volume_access_group_lun_assignments: VolumeAccessGroupLunAssignments

    """
    volume_access_group_lun_assignments = data_model.property(
        "volumeAccessGroupLunAssignments", VolumeAccessGroupLunAssignments,
        array=False, optional=False,
        documentation="""List of all physical Fibre Channel ports, or a port for a single node. """,
        dictionaryType=None
    )

    def __init__(self,
            volume_access_group_lun_assignments):
        kwargs = locals()
        del kwargs["self"]
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
        documentation="""Secondary metadata (slice) services that are in a dead state. """,
        dictionaryType=None
    )
    live_secondaries = data_model.property(
        "liveSecondaries", int,
        array=True, optional=False,
        documentation="""Secondary metadata (slice) services that are currently in a "live" state. """,
        dictionaryType=None
    )
    primary = data_model.property(
        "primary", int,
        array=False, optional=False,
        documentation="""The primary metadata (slice) services hosting the volume. """,
        dictionaryType=None
    )

    def __init__(self,
            dead_secondaries,
            live_secondaries,
            primary):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class VolumeStats(data_model.DataObject):
    """VolumeStats  
    Contains statistical data for an individual volume.

    :param account_id: [required] AccountID of the volume owner. 
    :type account_id: int

    :param actual_iops:  Current actual IOPS to the volume in the last 500 milliseconds. 
    :type actual_iops: int

    :param average_iopsize:  Average size in bytes of recent I/O to the volume in the last 500 milliseconds. 
    :type average_iopsize: int

    :param burst_iopscredit:  The total number of IOP credits available to the user. When users are not using up to the max IOPS, credits are accrued. 
    :type burst_iopscredit: int

    :param client_queue_depth:  The number of outstanding read and write operations to the cluster. 
    :type client_queue_depth: int

    :param latency_usec:  The observed latency time, in microseconds, to complete operations to a volume. A "0" (zero) value means there is no I/O to the volume. 
    :type latency_usec: int

    :param async_delay:  
    :type async_delay: int

    :param metadata_hosts:  The volume services on which the volume metadata resides. 
    :type metadata_hosts: MetadataHosts

    :param desired_metadata_hosts:  
    :type desired_metadata_hosts: MetadataHosts

    :param non_zero_blocks: [required] The number of 4KiB blocks with data after the last garbage collection operation has completed. 
    :type non_zero_blocks: int

    :param read_bytes: [required] Total bytes read by clients. 
    :type read_bytes: int

    :param read_latency_usec:  The average time, in microseconds, to complete read operations. 
    :type read_latency_usec: int

    :param read_ops: [required] Total read operations. 
    :type read_ops: int

    :param throttle:  A floating value between 0 and 1 that represents how much the system is throttling clients below their max IOPS because of re-replication of data, transient errors and snapshots taken. 
    :type throttle: float

    :param timestamp: [required] The current time in UTC. 
    :type timestamp: str

    :param total_latency_usec:  The average time, in microseconds, to complete read and write operations to a volume. 
    :type total_latency_usec: int

    :param unaligned_reads: [required] For 512e volumes, the number of read operations that were not on a 4k sector boundary. High numbers of unaligned reads may indicate improper partition alignment. 
    :type unaligned_reads: int

    :param unaligned_writes: [required] For 512e volumes, the number of write operations that were not on a 4k sector boundary. High numbers of unaligned writes may indicate improper partition alignment. 
    :type unaligned_writes: int

    :param volume_access_groups: [required] List of volume access group(s) to which a volume beintegers. 
    :type volume_access_groups: int

    :param volume_id: [required] Volume ID of the volume. 
    :type volume_id: int

    :param volume_size: [required] Total provisioned capacity in bytes. 
    :type volume_size: int

    :param volume_utilization:  A floating value that describes how much the client is using the volume.  Values:  0 = Client is not using the volume 1 = Client is using their max >1 = Client is using their burst 
    :type volume_utilization: float

    :param write_bytes: [required] Total bytes written by clients. 
    :type write_bytes: int

    :param write_latency_usec:  The average time, in microseconds, to complete write operations. 
    :type write_latency_usec: int

    :param write_ops: [required] Total write operations occurring on the volume. 
    :type write_ops: int

    :param zero_blocks: [required] Total number of 4KiB blocks without data after the last round of garbage collection operation has completed. 
    :type zero_blocks: int

    :param write_bytes_last_sample:  The total number of bytes written to the volume during the last sample period. 
    :type write_bytes_last_sample: int

    :param sample_period_msec:  The length of the sample period in milliseconds. 
    :type sample_period_msec: int

    :param read_bytes_last_sample:  The total number of bytes read from the volume during the last sample period. 
    :type read_bytes_last_sample: int

    :param read_ops_last_sample:  The total number of read operations durin gth elast sample period. 
    :type read_ops_last_sample: int

    :param write_ops_last_sample:  The total number of write operations during the last sample period. 
    :type write_ops_last_sample: int

    """
    account_id = data_model.property(
        "accountID", int,
        array=False, optional=False,
        documentation="""AccountID of the volume owner. """,
        dictionaryType=None
    )
    actual_iops = data_model.property(
        "actualIOPS", int,
        array=False, optional=True,
        documentation="""Current actual IOPS to the volume in the last 500 milliseconds. """,
        dictionaryType=None
    )
    average_iopsize = data_model.property(
        "averageIOPSize", int,
        array=False, optional=True,
        documentation="""Average size in bytes of recent I/O to the volume in the last 500 milliseconds. """,
        dictionaryType=None
    )
    burst_iopscredit = data_model.property(
        "burstIOPSCredit", int,
        array=False, optional=True,
        documentation="""The total number of IOP credits available to the user. When users are not using up to the max IOPS, credits are accrued. """,
        dictionaryType=None
    )
    client_queue_depth = data_model.property(
        "clientQueueDepth", int,
        array=False, optional=True,
        documentation="""The number of outstanding read and write operations to the cluster. """,
        dictionaryType=None
    )
    latency_usec = data_model.property(
        "latencyUSec", int,
        array=False, optional=True,
        documentation="""The observed latency time, in microseconds, to complete operations to a volume. A "0" (zero) value means there is no I/O to the volume. """,
        dictionaryType=None
    )
    async_delay = data_model.property(
        "asyncDelay", int,
        array=False, optional=True,
        documentation="""""",
        dictionaryType=None
    )
    metadata_hosts = data_model.property(
        "metadataHosts", MetadataHosts,
        array=False, optional=True,
        documentation="""The volume services on which the volume metadata resides. """,
        dictionaryType=None
    )
    desired_metadata_hosts = data_model.property(
        "desiredMetadataHosts", MetadataHosts,
        array=False, optional=True,
        documentation="""""",
        dictionaryType=None
    )
    non_zero_blocks = data_model.property(
        "nonZeroBlocks", int,
        array=False, optional=False,
        documentation="""The number of 4KiB blocks with data after the last garbage collection operation has completed. """,
        dictionaryType=None
    )
    read_bytes = data_model.property(
        "readBytes", int,
        array=False, optional=False,
        documentation="""Total bytes read by clients. """,
        dictionaryType=None
    )
    read_latency_usec = data_model.property(
        "readLatencyUSec", int,
        array=False, optional=True,
        documentation="""The average time, in microseconds, to complete read operations. """,
        dictionaryType=None
    )
    read_ops = data_model.property(
        "readOps", int,
        array=False, optional=False,
        documentation="""Total read operations. """,
        dictionaryType=None
    )
    throttle = data_model.property(
        "throttle", float,
        array=False, optional=True,
        documentation="""A floating value between 0 and 1 that represents how much the system is throttling clients below their max IOPS because of re-replication of data, transient errors and snapshots taken. """,
        dictionaryType=None
    )
    timestamp = data_model.property(
        "timestamp", str,
        array=False, optional=False,
        documentation="""The current time in UTC. """,
        dictionaryType=None
    )
    total_latency_usec = data_model.property(
        "totalLatencyUSec", int,
        array=False, optional=True,
        documentation="""The average time, in microseconds, to complete read and write operations to a volume. """,
        dictionaryType=None
    )
    unaligned_reads = data_model.property(
        "unalignedReads", int,
        array=False, optional=False,
        documentation="""For 512e volumes, the number of read operations that were not on a 4k sector boundary. High numbers of unaligned reads may indicate improper partition alignment. """,
        dictionaryType=None
    )
    unaligned_writes = data_model.property(
        "unalignedWrites", int,
        array=False, optional=False,
        documentation="""For 512e volumes, the number of write operations that were not on a 4k sector boundary. High numbers of unaligned writes may indicate improper partition alignment. """,
        dictionaryType=None
    )
    volume_access_groups = data_model.property(
        "volumeAccessGroups", int,
        array=True, optional=False,
        documentation="""List of volume access group(s) to which a volume beintegers. """,
        dictionaryType=None
    )
    volume_id = data_model.property(
        "volumeID", int,
        array=False, optional=False,
        documentation="""Volume ID of the volume. """,
        dictionaryType=None
    )
    volume_size = data_model.property(
        "volumeSize", int,
        array=False, optional=False,
        documentation="""Total provisioned capacity in bytes. """,
        dictionaryType=None
    )
    volume_utilization = data_model.property(
        "volumeUtilization", float,
        array=False, optional=True,
        documentation="""A floating value that describes how much the client is using the volume.  Values:  0 = Client is not using the volume 1 = Client is using their max >1 = Client is using their burst """,
        dictionaryType=None
    )
    write_bytes = data_model.property(
        "writeBytes", int,
        array=False, optional=False,
        documentation="""Total bytes written by clients. """,
        dictionaryType=None
    )
    write_latency_usec = data_model.property(
        "writeLatencyUSec", int,
        array=False, optional=True,
        documentation="""The average time, in microseconds, to complete write operations. """,
        dictionaryType=None
    )
    write_ops = data_model.property(
        "writeOps", int,
        array=False, optional=False,
        documentation="""Total write operations occurring on the volume. """,
        dictionaryType=None
    )
    zero_blocks = data_model.property(
        "zeroBlocks", int,
        array=False, optional=False,
        documentation="""Total number of 4KiB blocks without data after the last round of garbage collection operation has completed. """,
        dictionaryType=None
    )
    write_bytes_last_sample = data_model.property(
        "writeBytesLastSample", int,
        array=False, optional=True,
        documentation="""The total number of bytes written to the volume during the last sample period. """,
        dictionaryType=None
    )
    sample_period_msec = data_model.property(
        "samplePeriodMSec", int,
        array=False, optional=True,
        documentation="""The length of the sample period in milliseconds. """,
        dictionaryType=None
    )
    read_bytes_last_sample = data_model.property(
        "readBytesLastSample", int,
        array=False, optional=True,
        documentation="""The total number of bytes read from the volume during the last sample period. """,
        dictionaryType=None
    )
    read_ops_last_sample = data_model.property(
        "readOpsLastSample", int,
        array=False, optional=True,
        documentation="""The total number of read operations durin gth elast sample period. """,
        dictionaryType=None
    )
    write_ops_last_sample = data_model.property(
        "writeOpsLastSample", int,
        array=False, optional=True,
        documentation="""The total number of write operations during the last sample period. """,
        dictionaryType=None
    )

    def __init__(self,
            account_id,
            non_zero_blocks,
            read_bytes,
            read_ops,
            timestamp,
            unaligned_reads,
            unaligned_writes,
            volume_access_groups,
            volume_id,
            volume_size,
            write_bytes,
            write_ops,
            zero_blocks,
            actual_iops=None,
            average_iopsize=None,
            burst_iopscredit=None,
            client_queue_depth=None,
            latency_usec=None,
            async_delay=None,
            metadata_hosts=None,
            desired_metadata_hosts=None,
            read_latency_usec=None,
            throttle=None,
            total_latency_usec=None,
            volume_utilization=None,
            write_latency_usec=None,
            write_bytes_last_sample=None,
            sample_period_msec=None,
            read_bytes_last_sample=None,
            read_ops_last_sample=None,
            write_ops_last_sample=None):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class ListVolumeStatsByAccountResult(data_model.DataObject):
    """ListVolumeStatsByAccountResult  

    :param volume_stats: [required] List of account activity information. Note: The volumeID member is 0 for each entry, as the values represent the summation of all volumes owned by the account. 
    :type volume_stats: VolumeStats

    """
    volume_stats = data_model.property(
        "volumeStats", VolumeStats,
        array=True, optional=False,
        documentation="""List of account activity information. Note: The volumeID member is 0 for each entry, as the values represent the summation of all volumes owned by the account. """,
        dictionaryType=None
    )

    def __init__(self,
            volume_stats):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class ModifyGroupSnapshotRequest(data_model.DataObject):
    """ModifyGroupSnapshotRequest  
    ModifyGroupSnapshot enables you to change the attributes of a group of snapshots. You can also use this method to enable snapshots created on the Read/Write (source) volume to be remotely replicated to a target SolidFire storage system.

    :param group_snapshot_id: [required] Specifies the ID of the group of snapshots. 
    :type group_snapshot_id: int

    :param expiration_time:  Sets the time when the snapshot should be removed. If unspecified, the current time is used. 
    :type expiration_time: str

    :param enable_remote_replication:  Replicates the snapshot created to a remote cluster. Possible values are: true: The snapshot is replicated to remote storage. false: Default. The snapshot is not replicated. 
    :type enable_remote_replication: bool

    :param snap_mirror_label:  Label used by SnapMirror software to specify snapshot retention policy on SnapMirror endpoint. 
    :type snap_mirror_label: str

    """
    group_snapshot_id = data_model.property(
        "groupSnapshotID", int,
        array=False, optional=False,
        documentation="""Specifies the ID of the group of snapshots. """,
        dictionaryType=None
    )
    expiration_time = data_model.property(
        "expirationTime", str,
        array=False, optional=True,
        documentation="""Sets the time when the snapshot should be removed. If unspecified, the current time is used. """,
        dictionaryType=None
    )
    enable_remote_replication = data_model.property(
        "enableRemoteReplication", bool,
        array=False, optional=True,
        documentation="""Replicates the snapshot created to a remote cluster. Possible values are: true: The snapshot is replicated to remote storage. false: Default. The snapshot is not replicated. """,
        dictionaryType=None
    )
    snap_mirror_label = data_model.property(
        "snapMirrorLabel", str,
        array=False, optional=True,
        documentation="""Label used by SnapMirror software to specify snapshot retention policy on SnapMirror endpoint. """,
        dictionaryType=None
    )

    def __init__(self,
            group_snapshot_id,
            expiration_time=None,
            enable_remote_replication=None,
            snap_mirror_label=None):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class DeleteSnapshotRequest(data_model.DataObject):
    """DeleteSnapshotRequest  
    DeleteSnapshot enables you to delete a snapshot. A snapshot that is currently the "active" snapshot cannot be deleted. You must
    rollback and make another snapshot "active" before the current snapshot can be deleted. For more details on rolling back snapshots, see RollbackToSnapshot.

    :param snapshot_id: [required] The ID of the snapshot to be deleted. 
    :type snapshot_id: int

    """
    snapshot_id = data_model.property(
        "snapshotID", int,
        array=False, optional=False,
        documentation="""The ID of the snapshot to be deleted. """,
        dictionaryType=None
    )

    def __init__(self,
            snapshot_id):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class ScheduleInfo(data_model.DataObject):
    """ScheduleInfo  

    :param snapshot_name:  The snapshot name to be used.  
    :type snapshot_name: str

    :param enable_remote_replication:  Indicates if the snapshot should be included in remote replication. 
    :type enable_remote_replication: bool

    :param volume_ids:  A list of volume IDs to be included in the group snapshot. 
    :type volume_ids: int

    :param retention:  The amount of time the snapshot will be retained in HH:mm:ss. 
    :type retention: str

    """
    snapshot_name = data_model.property(
        "snapshotName", str,
        array=False, optional=True,
        documentation="""The snapshot name to be used.  """,
        dictionaryType=None
    )
    enable_remote_replication = data_model.property(
        "enableRemoteReplication", bool,
        array=False, optional=True,
        documentation="""Indicates if the snapshot should be included in remote replication. """,
        dictionaryType=None
    )
    volume_ids = data_model.property(
        "volumeIDs", int,
        array=True, optional=True,
        documentation="""A list of volume IDs to be included in the group snapshot. """,
        dictionaryType=None
    )
    retention = data_model.property(
        "retention", str,
        array=False, optional=True,
        documentation="""The amount of time the snapshot will be retained in HH:mm:ss. """,
        dictionaryType=None
    )

    def __init__(self,
            snapshot_name=None,
            enable_remote_replication=None,
            volume_ids=None,
            retention=None):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class Schedule(data_model.DataObject):
    """Schedule  
    Schedule is an object containing information about each schedule created to autonomously make a snapshot of a volume. The return object includes information for all schedules. If scheduleID is used to identify a specific schedule then only information for that scheduleID is returned. Schedules information is returned with the API method, see ListSchedules on the SolidFire API guide page 245.

    :param last_run_time_started:  Indicates the last time the schedule started n ISO 8601 date string. Valid values are: Success Failed 
    :type last_run_time_started: str

    :param has_error:  Indicates whether or not the schedule has errors. 
    :type has_error: bool

    :param schedule_info: [required] Includes the unique name given to the schedule, the retention period for the snapshot that was created, and the volume ID of the volume from which the snapshot was created. 
    :type schedule_info: ScheduleInfo

    :param run_next_interval:  Indicates whether or not the schedule will run the next time the scheduler is active. When set to "true", the schedule will run the next time the scheduler is active and then reset back to "false". 
    :type run_next_interval: bool

    :param name: [required] Unique name assigned to the schedule. 
    :type name: str

    :param last_run_status:  Indicates the status of the last scheduled snapshot. Valid values are: Success Failed 
    :type last_run_status: str

    :param schedule_id:  Unique ID of the schedule 
    :type schedule_id: int

    :param paused:  Indicates whether or not the schedule is paused. 
    :type paused: bool

    :param to_be_deleted:  Indicates if the schedule is marked for deletion. 
    :type to_be_deleted: bool

    :param frequency: [required] Indicates the frequency of the schedule occurrence. Set this to a type that inherits from Frequency. Valid types are: DayOfWeekFrequency DayOfMonthFrequency TimeIntervalFrequency 
    :type frequency: Frequency

    :param starting_date:  Indicates the date the first time the schedule began of will begin. Formatted in UTC time. 
    :type starting_date: str

    :param recurring:  Indicates whether or not the schedule is recurring. 
    :type recurring: bool

    """
    last_run_time_started = data_model.property(
        "lastRunTimeStarted", str,
        array=False, optional=True,
        documentation="""Indicates the last time the schedule started n ISO 8601 date string. Valid values are: Success Failed """,
        dictionaryType=None
    )
    has_error = data_model.property(
        "hasError", bool,
        array=False, optional=True,
        documentation="""Indicates whether or not the schedule has errors. """,
        dictionaryType=None
    )
    schedule_info = data_model.property(
        "scheduleInfo", ScheduleInfo,
        array=False, optional=False,
        documentation="""Includes the unique name given to the schedule, the retention period for the snapshot that was created, and the volume ID of the volume from which the snapshot was created. """,
        dictionaryType=None
    )
    run_next_interval = data_model.property(
        "runNextInterval", bool,
        array=False, optional=True,
        documentation="""Indicates whether or not the schedule will run the next time the scheduler is active. When set to "true", the schedule will run the next time the scheduler is active and then reset back to "false". """,
        dictionaryType=None
    )
    name = data_model.property(
        "name", str,
        array=False, optional=False,
        documentation="""Unique name assigned to the schedule. """,
        dictionaryType=None
    )
    last_run_status = data_model.property(
        "lastRunStatus", str,
        array=False, optional=True,
        documentation="""Indicates the status of the last scheduled snapshot. Valid values are: Success Failed """,
        dictionaryType=None
    )
    schedule_id = data_model.property(
        "scheduleID", int,
        array=False, optional=True,
        documentation="""Unique ID of the schedule """,
        dictionaryType=None
    )
    paused = data_model.property(
        "paused", bool,
        array=False, optional=True,
        documentation="""Indicates whether or not the schedule is paused. """,
        dictionaryType=None
    )
    to_be_deleted = data_model.property(
        "toBeDeleted", bool,
        array=False, optional=True,
        documentation="""Indicates if the schedule is marked for deletion. """,
        dictionaryType=None
    )
    frequency = data_model.property(
        "frequency", Frequency,
        array=False, optional=False,
        documentation="""Indicates the frequency of the schedule occurrence. Set this to a type that inherits from Frequency. Valid types are: DayOfWeekFrequency DayOfMonthFrequency TimeIntervalFrequency """,
        dictionaryType=None
    )
    starting_date = data_model.property(
        "startingDate", str,
        array=False, optional=True,
        documentation="""Indicates the date the first time the schedule began of will begin. Formatted in UTC time. """,
        dictionaryType=None
    )
    recurring = data_model.property(
        "recurring", bool,
        array=False, optional=True,
        documentation="""Indicates whether or not the schedule is recurring. """,
        dictionaryType=None
    )

    def __init__(self,
            schedule_info,
            name,
            frequency,
            last_run_time_started=None,
            has_error=None,
            run_next_interval=None,
            last_run_status=None,
            schedule_id=None,
            paused=None,
            to_be_deleted=None,
            starting_date=None,
            recurring=None):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class GetScheduleResult(data_model.DataObject):
    """GetScheduleResult  

    :param schedule: [required] The schedule attributes. 
    :type schedule: Schedule

    """
    schedule = data_model.property(
        "schedule", Schedule,
        array=False, optional=False,
        documentation="""The schedule attributes. """,
        dictionaryType=None
    )

    def __init__(self,
            schedule):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class ListVolumesRequest(data_model.DataObject):
    """ListVolumesRequest  
    The ListVolumes method enables you to retrieve a list of volumes that are in a cluster. You can specify the volumes you want to
    return in the list by using the available parameters.

    :param start_volume_id:  Only volumes with an ID greater than or equal to this value are returned. Mutually exclusive with the volumeIDs parameter. 
    :type start_volume_id: int

    :param limit:  Specifies the maximum number of volume results that are returned. Mutually exclusive with the volumeIDs parameter. 
    :type limit: int

    :param volume_status:  Only volumes with a status equal to the status value are returned. Possible values are: creating snapshotting active deleted 
    :type volume_status: str

    :param accounts:  Returns only the volumes owned by the accounts you specify here. Mutually exclusive with the volumeIDs parameter. 
    :type accounts: int

    :param is_paired:  Returns volumes that are paired or not paired. Possible values are: true: Returns all paired volumes. false: Returns all volumes that are not paired. 
    :type is_paired: bool

    :param volume_ids:  A list of volume IDs. If you supply this parameter, other parameters operate only on this set of volumes. Mutually exclusive with the accounts, startVolumeID, and limit parameters. 
    :type volume_ids: int

    :param volume_name:  Only volume object information matching the volume name is returned. 
    :type volume_name: str

    :param include_virtual_volumes:  Specifies that virtual volumes are included in the response by default. To exclude virtual volumes, set to false. 
    :type include_virtual_volumes: bool

    """
    start_volume_id = data_model.property(
        "startVolumeID", int,
        array=False, optional=True,
        documentation="""Only volumes with an ID greater than or equal to this value are returned. Mutually exclusive with the volumeIDs parameter. """,
        dictionaryType=None
    )
    limit = data_model.property(
        "limit", int,
        array=False, optional=True,
        documentation="""Specifies the maximum number of volume results that are returned. Mutually exclusive with the volumeIDs parameter. """,
        dictionaryType=None
    )
    volume_status = data_model.property(
        "volumeStatus", str,
        array=False, optional=True,
        documentation="""Only volumes with a status equal to the status value are returned. Possible values are: creating snapshotting active deleted """,
        dictionaryType=None
    )
    accounts = data_model.property(
        "accounts", int,
        array=True, optional=True,
        documentation="""Returns only the volumes owned by the accounts you specify here. Mutually exclusive with the volumeIDs parameter. """,
        dictionaryType=None
    )
    is_paired = data_model.property(
        "isPaired", bool,
        array=False, optional=True,
        documentation="""Returns volumes that are paired or not paired. Possible values are: true: Returns all paired volumes. false: Returns all volumes that are not paired. """,
        dictionaryType=None
    )
    volume_ids = data_model.property(
        "volumeIDs", int,
        array=True, optional=True,
        documentation="""A list of volume IDs. If you supply this parameter, other parameters operate only on this set of volumes. Mutually exclusive with the accounts, startVolumeID, and limit parameters. """,
        dictionaryType=None
    )
    volume_name = data_model.property(
        "volumeName", str,
        array=False, optional=True,
        documentation="""Only volume object information matching the volume name is returned. """,
        dictionaryType=None
    )
    include_virtual_volumes = data_model.property(
        "includeVirtualVolumes", bool,
        array=False, optional=True,
        documentation="""Specifies that virtual volumes are included in the response by default. To exclude virtual volumes, set to false. """,
        dictionaryType=None
    )

    def __init__(self,
            start_volume_id=None,
            limit=None,
            volume_status=None,
            accounts=None,
            is_paired=None,
            volume_ids=None,
            volume_name=None,
            include_virtual_volumes=None):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class NetworkConfigParams(data_model.DataObject):
    """NetworkConfigParams  

    :param _default:   
    :type _default: bool

    :param bond_master:   
    :type bond_master: str

    :param virtual_network_tag:   
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
    :type routes: dict

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
        documentation=""" """,
        dictionaryType=None
    )
    bond_master = data_model.property(
        "bond-master", str,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )
    virtual_network_tag = data_model.property(
        "virtualNetworkTag", str,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )
    address = data_model.property(
        "address", str,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )
    auto = data_model.property(
        "auto", bool,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )
    bond_downdelay = data_model.property(
        "bond-downdelay", str,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )
    bond_fail_over_mac = data_model.property(
        "bond-fail_over_mac", str,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )
    bond_primary_reselect = data_model.property(
        "bond-primary_reselect", str,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )
    bond_lacp_rate = data_model.property(
        "bond-lacp_rate", str,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )
    bond_miimon = data_model.property(
        "bond-miimon", str,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )
    bond_mode = data_model.property(
        "bond-mode", str,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )
    bond_slaves = data_model.property(
        "bond-slaves", str,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )
    bond_updelay = data_model.property(
        "bond-updelay", str,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )
    dns_nameservers = data_model.property(
        "dns-nameservers", str,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )
    dns_search = data_model.property(
        "dns-search", str,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )
    family = data_model.property(
        "family", str,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )
    gateway = data_model.property(
        "gateway", str,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )
    mac_address = data_model.property(
        "macAddress", str,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )
    mac_address_permanent = data_model.property(
        "macAddressPermanent", str,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )
    method = data_model.property(
        "method", str,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )
    mtu = data_model.property(
        "mtu", str,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )
    netmask = data_model.property(
        "netmask", str,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )
    network = data_model.property(
        "network", str,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )
    physical = data_model.property(
        "physical", PhysicalAdapter,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )
    routes = data_model.property(
        "routes", dict,
        array=True, optional=True,
        documentation=""" """,
        dictionaryType=None
    )
    status = data_model.property(
        "status", str,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )
    symmetric_route_rules = data_model.property(
        "symmetricRouteRules", str,
        array=True, optional=True,
        documentation=""" """,
        dictionaryType=None
    )
    up_and_running = data_model.property(
        "upAndRunning", bool,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )

    def __init__(self,
            _default=None,
            bond_master=None,
            virtual_network_tag=None,
            address=None,
            auto=None,
            bond_downdelay=None,
            bond_fail_over_mac=None,
            bond_primary_reselect=None,
            bond_lacp_rate=None,
            bond_miimon=None,
            bond_mode=None,
            bond_slaves=None,
            bond_updelay=None,
            dns_nameservers=None,
            dns_search=None,
            family=None,
            gateway=None,
            mac_address=None,
            mac_address_permanent=None,
            method=None,
            mtu=None,
            netmask=None,
            network=None,
            physical=None,
            routes=None,
            status=None,
            symmetric_route_rules=None,
            up_and_running=None):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class NetworkParams(data_model.DataObject):
    """NetworkParams  

    :param bond10_g:   
    :type bond10_g: NetworkConfigParams

    :param bond1_g:   
    :type bond1_g: NetworkConfigParams

    :param eth0:   
    :type eth0: NetworkConfigParams

    :param eth1:   
    :type eth1: NetworkConfigParams

    :param eth2:   
    :type eth2: NetworkConfigParams

    :param eth3:   
    :type eth3: NetworkConfigParams

    :param lo:   
    :type lo: NetworkConfigParams

    """
    bond10_g = data_model.property(
        "Bond10G", NetworkConfigParams,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )
    bond1_g = data_model.property(
        "Bond1G", NetworkConfigParams,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )
    eth0 = data_model.property(
        "eth0", NetworkConfigParams,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )
    eth1 = data_model.property(
        "eth1", NetworkConfigParams,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )
    eth2 = data_model.property(
        "eth2", NetworkConfigParams,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )
    eth3 = data_model.property(
        "eth3", NetworkConfigParams,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )
    lo = data_model.property(
        "lo", NetworkConfigParams,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )

    def __init__(self,
            bond10_g=None,
            bond1_g=None,
            eth0=None,
            eth1=None,
            eth2=None,
            eth3=None,
            lo=None):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class ConfigParams(data_model.DataObject):
    """ConfigParams  

    :param cluster: [required]  
    :type cluster: ClusterConfig

    :param network: [required]  
    :type network: NetworkParams

    """
    cluster = data_model.property(
        "cluster", ClusterConfig,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    network = data_model.property(
        "network", NetworkParams,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )

    def __init__(self,
            cluster,
            network):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class ModifyScheduleResult(data_model.DataObject):
    """ModifyScheduleResult  

    :param schedule:   
    :type schedule: Schedule

    """
    schedule = data_model.property(
        "schedule", Schedule,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )

    def __init__(self,
            schedule=None):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class ClearClusterFaultsRequest(data_model.DataObject):
    """ClearClusterFaultsRequest  
    You can use the ClearClusterFaults method to clear information about both current and previously detected faults. Both resolved
    and unresolved faults can be cleared.

    :param fault_types:  Determines the types of faults cleared. Possible values are: current: Faults that are currently detected and have not been resolved. resolved: (Default) Faults that were previously detected and resolved. all: Both current and resolved faults are cleared. The fault status can be determined by the resolved field of the fault object. 
    :type fault_types: str

    """
    fault_types = data_model.property(
        "faultTypes", str,
        array=False, optional=True,
        documentation="""Determines the types of faults cleared. Possible values are: current: Faults that are currently detected and have not been resolved. resolved: (Default) Faults that were previously detected and resolved. all: Both current and resolved faults are cleared. The fault status can be determined by the resolved field of the fault object. """,
        dictionaryType=None
    )

    def __init__(self,
            fault_types=None):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class RemoveClusterAdminResult(data_model.DataObject):
    """RemoveClusterAdminResult  

    """

    def __init__(self):
        kwargs = locals()
        del kwargs["self"]
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
        documentation="""The ID of the result. """,
        dictionaryType=None
    )
    completed = data_model.property(
        "completed", bool,
        array=False, optional=False,
        documentation="""Returns true if it is completed and false if it isn't. """,
        dictionaryType=None
    )
    create_time = data_model.property(
        "createTime", str,
        array=False, optional=False,
        documentation="""The time at which the asyncronous result was created """,
        dictionaryType=None
    )
    last_update_time = data_model.property(
        "lastUpdateTime", str,
        array=False, optional=False,
        documentation="""Time at which the result was last updated """,
        dictionaryType=None
    )
    result_type = data_model.property(
        "resultType", str,
        array=False, optional=False,
        documentation="""The type of result. Could be Clone, DriveAdd, etc. """,
        dictionaryType=None
    )
    success = data_model.property(
        "success", bool,
        array=False, optional=False,
        documentation="""Returns whether the result was a success or failure. """,
        dictionaryType=None
    )
    data = data_model.property(
        "data", dict,
        array=False, optional=False,
        documentation="""Attributes related to the result """,
        dictionaryType=None
    )

    def __init__(self,
            async_result_id,
            completed,
            create_time,
            last_update_time,
            result_type,
            success,
            data):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class ListAsyncResultsResult(data_model.DataObject):
    """ListAsyncResultsResult  

    :param async_handles: [required] An array of serialized asynchronous method results. 
    :type async_handles: AsyncHandle

    """
    async_handles = data_model.property(
        "asyncHandles", AsyncHandle,
        array=True, optional=False,
        documentation="""An array of serialized asynchronous method results. """,
        dictionaryType=None
    )

    def __init__(self,
            async_handles):
        kwargs = locals()
        del kwargs["self"]
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

    :param storage_container_id:  The id of the storage container associated with the account 
    :type storage_container_id: UUID

    :param attributes:  List of Name/Value pairs in JSON object format. 
    :type attributes: dict

    """
    account_id = data_model.property(
        "accountID", int,
        array=False, optional=False,
        documentation="""Unique AccountID for the account. """,
        dictionaryType=None
    )
    username = data_model.property(
        "username", str,
        array=False, optional=False,
        documentation="""User name for the account. """,
        dictionaryType=None
    )
    status = data_model.property(
        "status", str,
        array=False, optional=False,
        documentation="""Current status of the account. """,
        dictionaryType=None
    )
    volumes = data_model.property(
        "volumes", int,
        array=True, optional=False,
        documentation="""List of VolumeIDs for Volumes owned by this account. """,
        dictionaryType=None
    )
    initiator_secret = data_model.property(
        "initiatorSecret", CHAPSecret,
        array=False, optional=True,
        documentation="""CHAP secret to use for the initiator. """,
        dictionaryType=None
    )
    target_secret = data_model.property(
        "targetSecret", CHAPSecret,
        array=False, optional=True,
        documentation="""CHAP secret to use for the target (mutual CHAP authentication). """,
        dictionaryType=None
    )
    storage_container_id = data_model.property(
        "storageContainerID", UUID,
        array=False, optional=True,
        documentation="""The id of the storage container associated with the account """,
        dictionaryType=None
    )
    attributes = data_model.property(
        "attributes", dict,
        array=False, optional=True,
        documentation="""List of Name/Value pairs in JSON object format. """,
        dictionaryType=None
    )

    def __init__(self,
            account_id,
            username,
            status,
            volumes,
            initiator_secret=None,
            target_secret=None,
            storage_container_id=None,
            attributes=None):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class AddAccountResult(data_model.DataObject):
    """AddAccountResult  

    :param account_id: [required] AccountID for the newly created Account. 
    :type account_id: int

    :param account:  The full account object 
    :type account: Account

    """
    account_id = data_model.property(
        "accountID", int,
        array=False, optional=False,
        documentation="""AccountID for the newly created Account. """,
        dictionaryType=None
    )
    account = data_model.property(
        "account", Account,
        array=False, optional=True,
        documentation="""The full account object """,
        dictionaryType=None
    )

    def __init__(self,
            account_id,
            account=None):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class GetFeatureStatusRequest(data_model.DataObject):
    """GetFeatureStatusRequest  
    GetFeatureStatus enables you to retrieve the status of a cluster feature.

    :param feature:  Specifies the feature for which the status is returned. Valid value is: vvols: Retrieve status for the NetApp SolidFire VVols cluster feature. 
    :type feature: str

    """
    feature = data_model.property(
        "feature", str,
        array=False, optional=True,
        documentation="""Specifies the feature for which the status is returned. Valid value is: vvols: Retrieve status for the NetApp SolidFire VVols cluster feature. """,
        dictionaryType=None
    )

    def __init__(self,
            feature=None):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class GetIpmiConfigRequest(data_model.DataObject):
    """GetIpmiConfigRequest  
    GetIpmiConfig enables you to retrieve hardware sensor information from sensors that are in your node.

    :param chassis_type:  Displays information for each node chassis type. Valid values are: all: Returns sensor information for each chassis type. {chassis type}: Returns sensor information for a specified chassis type. 
    :type chassis_type: str

    """
    chassis_type = data_model.property(
        "chassisType", str,
        array=False, optional=True,
        documentation="""Displays information for each node chassis type. Valid values are: all: Returns sensor information for each chassis type. {chassis type}: Returns sensor information for a specified chassis type. """,
        dictionaryType=None
    )

    def __init__(self,
            chassis_type=None):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class ModifySnapshotRequest(data_model.DataObject):
    """ModifySnapshotRequest  
    ModifySnapshot enables you to change the attributes currently assigned to a snapshot. You can use this method to enable snapshots created on
    the Read/Write (source) volume to be remotely replicated to a target SolidFire storage system.

    :param snapshot_id: [required] Specifies the ID of the snapshot. 
    :type snapshot_id: int

    :param expiration_time:  Sets the time when the snapshot should be removed. 
    :type expiration_time: str

    :param enable_remote_replication:  Replicates the snapshot created to a remote cluster. Possible values are: true: The snapshot is replicated to remote storage. false: Default. The snapshot is not replicated. 
    :type enable_remote_replication: bool

    :param snap_mirror_label:  Label used by SnapMirror software to specify snapshot retention policy on SnapMirror endpoint. 
    :type snap_mirror_label: str

    """
    snapshot_id = data_model.property(
        "snapshotID", int,
        array=False, optional=False,
        documentation="""Specifies the ID of the snapshot. """,
        dictionaryType=None
    )
    expiration_time = data_model.property(
        "expirationTime", str,
        array=False, optional=True,
        documentation="""Sets the time when the snapshot should be removed. """,
        dictionaryType=None
    )
    enable_remote_replication = data_model.property(
        "enableRemoteReplication", bool,
        array=False, optional=True,
        documentation="""Replicates the snapshot created to a remote cluster. Possible values are: true: The snapshot is replicated to remote storage. false: Default. The snapshot is not replicated. """,
        dictionaryType=None
    )
    snap_mirror_label = data_model.property(
        "snapMirrorLabel", str,
        array=False, optional=True,
        documentation="""Label used by SnapMirror software to specify snapshot retention policy on SnapMirror endpoint. """,
        dictionaryType=None
    )

    def __init__(self,
            snapshot_id,
            expiration_time=None,
            enable_remote_replication=None,
            snap_mirror_label=None):
        kwargs = locals()
        del kwargs["self"]
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
        documentation="""Current computed level of block fullness of the cluster. Possible values: stage1Happy: No alerts or error conditions. stage2Aware: 3 nodes of capacity available. stage3Low: 2 nodes of capacity available. stage4Critical: 1 node of capacity available. No new volumes or clones can be created. stage5CompletelyConsumed: Completely consumed. Cluster is read-only, iSCSI connection is maintained but all writes are suspended. """,
        dictionaryType=None
    )
    fullness = data_model.property(
        "fullness", str,
        array=False, optional=False,
        documentation="""Reflects the highest level of fullness between "blockFullness" and "metadataFullness". """,
        dictionaryType=None
    )
    max_metadata_over_provision_factor = data_model.property(
        "maxMetadataOverProvisionFactor", int,
        array=False, optional=False,
        documentation="""A value representative of the number of times metadata space can be over provisioned relative to the amount of space available. For example, if there was enough metadata space to store 100 TiB of volumes and this number was set to 5, then 500 TiB worth of volumes could be created. """,
        dictionaryType=None
    )
    metadata_fullness = data_model.property(
        "metadataFullness", str,
        array=False, optional=False,
        documentation="""Current computed level of metadata fullness of the cluster. """,
        dictionaryType=None
    )
    slice_reserve_used_threshold_pct = data_model.property(
        "sliceReserveUsedThresholdPct", int,
        array=False, optional=False,
        documentation="""Error condition; message sent to "Alerts" if the reserved slice utilization is greater than the sliceReserveUsedThresholdPct value returned. """,
        dictionaryType=None
    )
    stage2_aware_threshold = data_model.property(
        "stage2AwareThreshold", int,
        array=False, optional=False,
        documentation="""Awareness condition: Value that is set for "Stage 2" cluster threshold level. """,
        dictionaryType=None
    )
    stage2_block_threshold_bytes = data_model.property(
        "stage2BlockThresholdBytes", int,
        array=False, optional=False,
        documentation="""Number of bytes being used by the cluster at which a stage2 condition will exist. """,
        dictionaryType=None
    )
    stage3_block_threshold_bytes = data_model.property(
        "stage3BlockThresholdBytes", int,
        array=False, optional=False,
        documentation="""Number of bytes being used by the cluster at which a stage3 condition will exist. """,
        dictionaryType=None
    )
    stage3_block_threshold_percent = data_model.property(
        "stage3BlockThresholdPercent", int,
        array=False, optional=False,
        documentation="""The percent value set for stage3. At this percent full, a warning will be posted in the Alerts log. """,
        dictionaryType=None
    )
    stage3_low_threshold = data_model.property(
        "stage3LowThreshold", int,
        array=False, optional=False,
        documentation="""Error condition; message sent to "Alerts" that capacity on a cluster is getting low. """,
        dictionaryType=None
    )
    stage4_critical_threshold = data_model.property(
        "stage4CriticalThreshold", int,
        array=False, optional=False,
        documentation="""Error condition; message sent to "Alerts" that capacity on a cluster is critically low. """,
        dictionaryType=None
    )
    stage4_block_threshold_bytes = data_model.property(
        "stage4BlockThresholdBytes", int,
        array=False, optional=False,
        documentation="""Number of bytes being used by the cluster at which a stage4 condition will exist. """,
        dictionaryType=None
    )
    stage5_block_threshold_bytes = data_model.property(
        "stage5BlockThresholdBytes", int,
        array=False, optional=False,
        documentation="""Number of bytes being used by the cluster at which a stage5 condition will exist. """,
        dictionaryType=None
    )
    sum_total_cluster_bytes = data_model.property(
        "sumTotalClusterBytes", int,
        array=False, optional=False,
        documentation="""Physical capacity of the cluster measured in bytes. """,
        dictionaryType=None
    )
    sum_total_metadata_cluster_bytes = data_model.property(
        "sumTotalMetadataClusterBytes", int,
        array=False, optional=False,
        documentation="""Total amount of space that can be used to store metadata. """,
        dictionaryType=None
    )
    sum_used_cluster_bytes = data_model.property(
        "sumUsedClusterBytes", int,
        array=False, optional=False,
        documentation="""Number of bytes used on the cluster. """,
        dictionaryType=None
    )
    sum_used_metadata_cluster_bytes = data_model.property(
        "sumUsedMetadataClusterBytes", int,
        array=False, optional=False,
        documentation="""Amount of space used on volume drives to store metadata. """,
        dictionaryType=None
    )

    def __init__(self,
            block_fullness,
            fullness,
            max_metadata_over_provision_factor,
            metadata_fullness,
            slice_reserve_used_threshold_pct,
            stage2_aware_threshold,
            stage2_block_threshold_bytes,
            stage3_block_threshold_bytes,
            stage3_block_threshold_percent,
            stage3_low_threshold,
            stage4_critical_threshold,
            stage4_block_threshold_bytes,
            stage5_block_threshold_bytes,
            sum_total_cluster_bytes,
            sum_total_metadata_cluster_bytes,
            sum_used_cluster_bytes,
            sum_used_metadata_cluster_bytes):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class ModifyScheduleRequest(data_model.DataObject):
    """ModifyScheduleRequest  
    ModifySchedule enables you to change the intervals at which a scheduled snapshot occurs. This allows for adjustment to the snapshot frequency and retention.

    :param schedule: [required] The "Schedule" object will be used to modify an existing schedule. The ScheduleID property is required. Frequency property must be of type that inherits from Frequency. Valid types are: DaysOfMonthFrequency DaysOrWeekFrequency TimeIntervalFrequency 
    :type schedule: Schedule

    """
    schedule = data_model.property(
        "schedule", Schedule,
        array=False, optional=False,
        documentation="""The "Schedule" object will be used to modify an existing schedule. The ScheduleID property is required. Frequency property must be of type that inherits from Frequency. Valid types are: DaysOfMonthFrequency DaysOrWeekFrequency TimeIntervalFrequency """,
        dictionaryType=None
    )

    def __init__(self,
            schedule):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class SetDefaultQoSRequest(data_model.DataObject):
    """SetDefaultQoSRequest  
    SetDefaultQoS enables you to configure the default Quality of Service (QoS) values (measured in inputs and outputs per second, or
    IOPS) for a volume. For more information about QoS in a SolidFire cluster, see the User Guide.

    :param min_iops:  The minimum number of sustained IOPS provided by the cluster to a volume. 
    :type min_iops: int

    :param max_iops:  The maximum number of sustained IOPS provided by the cluster to a volume. 
    :type max_iops: int

    :param burst_iops:  The maximum number of IOPS allowed in a short burst scenario. 
    :type burst_iops: int

    """
    min_iops = data_model.property(
        "minIOPS", int,
        array=False, optional=True,
        documentation="""The minimum number of sustained IOPS provided by the cluster to a volume. """,
        dictionaryType=None
    )
    max_iops = data_model.property(
        "maxIOPS", int,
        array=False, optional=True,
        documentation="""The maximum number of sustained IOPS provided by the cluster to a volume. """,
        dictionaryType=None
    )
    burst_iops = data_model.property(
        "burstIOPS", int,
        array=False, optional=True,
        documentation="""The maximum number of IOPS allowed in a short burst scenario. """,
        dictionaryType=None
    )

    def __init__(self,
            min_iops=None,
            max_iops=None,
            burst_iops=None):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class NewDrive(data_model.DataObject):
    """NewDrive  

    :param drive_id: [required] A unique identifier for this drive. 
    :type drive_id: int

    :param type:  block or slice 
    :type type: str

    """
    drive_id = data_model.property(
        "driveID", int,
        array=False, optional=False,
        documentation="""A unique identifier for this drive. """,
        dictionaryType=None
    )
    type = data_model.property(
        "type", str,
        array=False, optional=True,
        documentation="""block or slice """,
        dictionaryType=None
    )

    def __init__(self,
            drive_id,
            type=None):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class ClusterStats(data_model.DataObject):
    """ClusterStats  

    :param cluster_utilization: [required] The amount of cluster capacity being utilized. 
    :type cluster_utilization: float

    :param client_queue_depth: [required]  
    :type client_queue_depth: int

    :param normalized_iops: [required]  
    :type normalized_iops: int

    :param read_bytes: [required] Total bytes read by clients. 
    :type read_bytes: int

    :param read_latency_usec_total: [required]  
    :type read_latency_usec_total: int

    :param read_ops: [required] Total read operations. 
    :type read_ops: int

    :param services_count: [required] Services count 
    :type services_count: int

    :param services_total: [required] Total services. 
    :type services_total: int

    :param timestamp: [required] Current time in UTC format. ISO 8601 date string. 
    :type timestamp: str

    :param write_bytes: [required] Total bytes written by clients. 
    :type write_bytes: int

    :param write_latency_usec_total: [required]  
    :type write_latency_usec_total: int

    :param write_ops: [required] Total write operations. 
    :type write_ops: int

    :param actual_iops:   
    :type actual_iops: int

    :param average_iopsize:   
    :type average_iopsize: int

    :param latency_usec:   
    :type latency_usec: int

    :param read_bytes_last_sample:   
    :type read_bytes_last_sample: int

    :param read_latency_usec:   
    :type read_latency_usec: int

    :param read_ops_last_sample:   
    :type read_ops_last_sample: int

    :param sample_period_msec:   
    :type sample_period_msec: int

    :param unaligned_reads:   
    :type unaligned_reads: int

    :param unaligned_writes:   
    :type unaligned_writes: int

    :param write_bytes_last_sample:   
    :type write_bytes_last_sample: int

    :param write_latency_usec:   
    :type write_latency_usec: int

    :param write_ops_last_sample:   
    :type write_ops_last_sample: int

    """
    cluster_utilization = data_model.property(
        "clusterUtilization", float,
        array=False, optional=False,
        documentation="""The amount of cluster capacity being utilized. """,
        dictionaryType=None
    )
    client_queue_depth = data_model.property(
        "clientQueueDepth", int,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    normalized_iops = data_model.property(
        "normalizedIOPS", int,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    read_bytes = data_model.property(
        "readBytes", int,
        array=False, optional=False,
        documentation="""Total bytes read by clients. """,
        dictionaryType=None
    )
    read_latency_usec_total = data_model.property(
        "readLatencyUSecTotal", int,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    read_ops = data_model.property(
        "readOps", int,
        array=False, optional=False,
        documentation="""Total read operations. """,
        dictionaryType=None
    )
    services_count = data_model.property(
        "servicesCount", int,
        array=False, optional=False,
        documentation="""Services count """,
        dictionaryType=None
    )
    services_total = data_model.property(
        "servicesTotal", int,
        array=False, optional=False,
        documentation="""Total services. """,
        dictionaryType=None
    )
    timestamp = data_model.property(
        "timestamp", str,
        array=False, optional=False,
        documentation="""Current time in UTC format. ISO 8601 date string. """,
        dictionaryType=None
    )
    write_bytes = data_model.property(
        "writeBytes", int,
        array=False, optional=False,
        documentation="""Total bytes written by clients. """,
        dictionaryType=None
    )
    write_latency_usec_total = data_model.property(
        "writeLatencyUSecTotal", int,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    write_ops = data_model.property(
        "writeOps", int,
        array=False, optional=False,
        documentation="""Total write operations. """,
        dictionaryType=None
    )
    actual_iops = data_model.property(
        "actualIOPS", int,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )
    average_iopsize = data_model.property(
        "averageIOPSize", int,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )
    latency_usec = data_model.property(
        "latencyUSec", int,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )
    read_bytes_last_sample = data_model.property(
        "readBytesLastSample", int,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )
    read_latency_usec = data_model.property(
        "readLatencyUSec", int,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )
    read_ops_last_sample = data_model.property(
        "readOpsLastSample", int,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )
    sample_period_msec = data_model.property(
        "samplePeriodMsec", int,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )
    unaligned_reads = data_model.property(
        "unalignedReads", int,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )
    unaligned_writes = data_model.property(
        "unalignedWrites", int,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )
    write_bytes_last_sample = data_model.property(
        "writeBytesLastSample", int,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )
    write_latency_usec = data_model.property(
        "writeLatencyUSec", int,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )
    write_ops_last_sample = data_model.property(
        "writeOpsLastSample", int,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )

    def __init__(self,
            cluster_utilization,
            client_queue_depth,
            normalized_iops,
            read_bytes,
            read_latency_usec_total,
            read_ops,
            services_count,
            services_total,
            timestamp,
            write_bytes,
            write_latency_usec_total,
            write_ops,
            actual_iops=None,
            average_iopsize=None,
            latency_usec=None,
            read_bytes_last_sample=None,
            read_latency_usec=None,
            read_ops_last_sample=None,
            sample_period_msec=None,
            unaligned_reads=None,
            unaligned_writes=None,
            write_bytes_last_sample=None,
            write_latency_usec=None,
            write_ops_last_sample=None):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class GetClusterStatsResult(data_model.DataObject):
    """GetClusterStatsResult  

    :param cluster_stats: [required]  
    :type cluster_stats: ClusterStats

    """
    cluster_stats = data_model.property(
        "clusterStats", ClusterStats,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )

    def __init__(self,
            cluster_stats):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class ModifyVolumeAccessGroupRequest(data_model.DataObject):
    """ModifyVolumeAccessGroupRequest  
    You can use ModifyVolumeAccessGroup to update initiators and add or remove volumes from a volume access group. If a specified initiator or volume is a duplicate of what currently exists, the volume access group is left as-is. If you do not specify a value for volumes or initiators, the current list of initiators and volumes is not changed.

    :param volume_access_group_id: [required] The ID of the volume access group to modify. 
    :type volume_access_group_id: int

    :param virtual_network_id:  The ID of the SolidFire virtual network to associate the volume access group with. 
    :type virtual_network_id: int

    :param virtual_network_tags:  The ID of the SolidFire virtual network to associate the volume access group with. 
    :type virtual_network_tags: int

    :param name:  The new name for this volume access group. Not required to be unique, but recommended. 
    :type name: str

    :param initiators:  List of initiators to include in the volume access group. If unspecified, the access group's configured initiators are not modified. 
    :type initiators: str

    :param volumes:  List of volumes to initially include in the volume access group. If unspecified, the access group's volumes are not modified. 
    :type volumes: int

    :param delete_orphan_initiators:  true: Delete initiator objects after they are removed from a volume access group. false: Do not delete initiator objects after they are removed from a volume access group. 
    :type delete_orphan_initiators: bool

    :param attributes:  List of name-value pairs in JSON object format. 
    :type attributes: dict

    """
    volume_access_group_id = data_model.property(
        "volumeAccessGroupID", int,
        array=False, optional=False,
        documentation="""The ID of the volume access group to modify. """,
        dictionaryType=None
    )
    virtual_network_id = data_model.property(
        "virtualNetworkID", int,
        array=True, optional=True,
        documentation="""The ID of the SolidFire virtual network to associate the volume access group with. """,
        dictionaryType=None
    )
    virtual_network_tags = data_model.property(
        "virtualNetworkTags", int,
        array=True, optional=True,
        documentation="""The ID of the SolidFire virtual network to associate the volume access group with. """,
        dictionaryType=None
    )
    name = data_model.property(
        "name", str,
        array=False, optional=True,
        documentation="""The new name for this volume access group. Not required to be unique, but recommended. """,
        dictionaryType=None
    )
    initiators = data_model.property(
        "initiators", str,
        array=True, optional=True,
        documentation="""List of initiators to include in the volume access group. If unspecified, the access group's configured initiators are not modified. """,
        dictionaryType=None
    )
    volumes = data_model.property(
        "volumes", int,
        array=True, optional=True,
        documentation="""List of volumes to initially include in the volume access group. If unspecified, the access group's volumes are not modified. """,
        dictionaryType=None
    )
    delete_orphan_initiators = data_model.property(
        "deleteOrphanInitiators", bool,
        array=False, optional=True,
        documentation="""true: Delete initiator objects after they are removed from a volume access group. false: Do not delete initiator objects after they are removed from a volume access group. """,
        dictionaryType=None
    )
    attributes = data_model.property(
        "attributes", dict,
        array=False, optional=True,
        documentation="""List of name-value pairs in JSON object format. """,
        dictionaryType=None
    )

    def __init__(self,
            volume_access_group_id,
            virtual_network_id=None,
            virtual_network_tags=None,
            name=None,
            initiators=None,
            volumes=None,
            delete_orphan_initiators=None,
            attributes=None):
        kwargs = locals()
        del kwargs["self"]
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
        documentation="""Desired minimum 4KB IOPS to guarantee. The allowed IOPS will only drop below this level if all volumes have been capped at their min IOPS value and there is still insufficient performance capacity. """,
        dictionaryType=None
    )
    max_iops = data_model.property(
        "maxIOPS", int,
        array=False, optional=False,
        documentation="""Desired maximum 4KB IOPS allowed over an extended period of time. """,
        dictionaryType=None
    )
    burst_iops = data_model.property(
        "burstIOPS", int,
        array=False, optional=False,
        documentation="""Maximum "peak" 4KB IOPS allowed for short periods of time. Allows for bursts of I/O activity over the normal max IOPS value. """,
        dictionaryType=None
    )
    burst_time = data_model.property(
        "burstTime", int,
        array=False, optional=False,
        documentation="""The length of time burst IOPS is allowed. The value returned is represented in time units of seconds. Note: this value is calculated by the system based on IOPS set for QoS. """,
        dictionaryType=None
    )
    curve = data_model.property(
        "curve", dict,
        array=False, optional=False,
        documentation="""The curve is a set of key-value pairs. The keys are I/O sizes in bytes. The values represent the cost performing an IOP at a specific I/O size. The curve is calculated relative to a 4096 byte operation set at 100 IOPS. """,
        dictionaryType=int
    )

    def __init__(self,
            min_iops,
            max_iops,
            burst_iops,
            burst_time,
            curve):
        kwargs = locals()
        del kwargs["self"]
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
        documentation="""The state of the snapshot replication. """,
        dictionaryType=None
    )
    state_details = data_model.property(
        "stateDetails", str,
        array=False, optional=False,
        documentation="""Reserved for future use. """,
        dictionaryType=None
    )

    def __init__(self,
            state,
            state_details):
        kwargs = locals()
        del kwargs["self"]
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
        documentation="""Volume replication mode. Possible values: Async: Writes are acknowledged when they complete locally. The cluster does not wait for writes to be replicated to the target cluster. Sync: Source acknowledges write when the data is stored locally and on the remote cluster. SnapshotsOnly: Only snapshots created on the source cluster will be replicated. Active writes from the source volume will not be replicated. """,
        dictionaryType=None
    )
    pause_limit = data_model.property(
        "pauseLimit", int,
        array=False, optional=False,
        documentation="""The number of occurring write ops before auto-pausing, on a per volume pair level. """,
        dictionaryType=None
    )
    remote_service_id = data_model.property(
        "remoteServiceID", int,
        array=False, optional=False,
        documentation="""The remote slice service ID. """,
        dictionaryType=None
    )
    resume_details = data_model.property(
        "resumeDetails", str,
        array=False, optional=False,
        documentation="""Reserved for future use. """,
        dictionaryType=None
    )
    snapshot_replication = data_model.property(
        "snapshotReplication", SnapshotReplication,
        array=False, optional=False,
        documentation="""The details of snapshot replication. """,
        dictionaryType=None
    )
    state = data_model.property(
        "state", str,
        array=False, optional=False,
        documentation="""The state of the volume replication. """,
        dictionaryType=None
    )
    state_details = data_model.property(
        "stateDetails", str,
        array=False, optional=False,
        documentation="""Reserved for future use. """,
        dictionaryType=None
    )

    def __init__(self,
            mode,
            pause_limit,
            remote_service_id,
            resume_details,
            snapshot_replication,
            state,
            state_details):
        kwargs = locals()
        del kwargs["self"]
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
        documentation="""The remote cluster a volume is paired with. """,
        dictionaryType=None
    )
    remote_volume_id = data_model.property(
        "remoteVolumeID", int,
        array=False, optional=False,
        documentation="""The VolumeID on the remote cluster a volume is paired with. """,
        dictionaryType=None
    )
    remote_slice_id = data_model.property(
        "remoteSliceID", int,
        array=False, optional=False,
        documentation="""The SliceID on the remote cluster a volume is paired with. """,
        dictionaryType=None
    )
    remote_volume_name = data_model.property(
        "remoteVolumeName", str,
        array=False, optional=False,
        documentation="""The last-observed name of the volume on the remote cluster a volume is paired with. """,
        dictionaryType=None
    )
    volume_pair_uuid = data_model.property(
        "volumePairUUID", UUID,
        array=False, optional=False,
        documentation="""A UUID in canonical form. """,
        dictionaryType=None
    )
    remote_replication = data_model.property(
        "remoteReplication", RemoteReplication,
        array=False, optional=False,
        documentation="""Details about the replication configuration for this volume pair. """,
        dictionaryType=None
    )

    def __init__(self,
            cluster_pair_id,
            remote_volume_id,
            remote_slice_id,
            remote_volume_name,
            volume_pair_uuid,
            remote_replication):
        kwargs = locals()
        del kwargs["self"]
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

    :param volume_consistency_group_uuid: [required]  
    :type volume_consistency_group_uuid: UUID

    :param volume_uuid: [required]  
    :type volume_uuid: UUID

    :param enable_snap_mirror_replication: [required]  
    :type enable_snap_mirror_replication: bool

    :param status: [required] Current status of the volume init: A volume that is being initialized and is not ready for connections. active: An active volume ready for connections. 
    :type status: str

    :param access: [required] Access allowed for the volume readOnly: Only read operations are allowed. readWrite: Reads and writes are allowed. locked: No reads or writes are allowed. replicationTarget: Designated as a target volume in a replicated volume pair. 
    :type access: str

    :param enable512e: [required] If "true", the volume provides 512 byte sector emulation. 
    :type enable512e: bool

    :param iqn:  Volume iSCSI Qualified Name. 
    :type iqn: str

    :param scsi_euidevice_id: [required] Globally unique SCSI device identifier for the volume in EUI-64 based 16-byte format. 
    :type scsi_euidevice_id: str

    :param scsi_naadevice_id: [required] Globally unique SCSI device identifier for the volume in NAA IEEE Registered Extended format. 
    :type scsi_naadevice_id: str

    :param qos: [required] Quality of service settings for this volume. 
    :type qos: VolumeQOS

    :param qos_policy_id:  The QoS policy ID associated with the volume. The value is null if the volume is not associated with a policy. 
    :type qos_policy_id: int

    :param volume_access_groups: [required] List of volume access groups to which a volume beintegers. 
    :type volume_access_groups: int

    :param volume_pairs: [required] Information about a paired volume. Available only if a volume is paired. @see VolumePairs for return values. 
    :type volume_pairs: VolumePair

    :param delete_time:  The time this volume was deleted. If this has no value, the volume has not yet been deleted. 
    :type delete_time: str

    :param purge_time:  The time this volume will be purged from the system. If this has no value, the volume has not yet been deleted (and is not scheduled for purging). 
    :type purge_time: str

    :param last_access_time:  The last time any access to this volume occurred. If this has no value, the last access time is not known. 
    :type last_access_time: str

    :param last_access_time_io:  The last time I/O access to this volume occurred. If this has no value, the last I/O access time is not known. 
    :type last_access_time_io: str

    :param slice_count: [required] The number of slices backing this volume. In the current software, this value will always be 1. 
    :type slice_count: int

    :param total_size: [required] Total size of this volume in bytes. 
    :type total_size: int

    :param block_size: [required] Size of the blocks on the volume. 
    :type block_size: int

    :param virtual_volume_id:  Virtual volume ID this volume backs. 
    :type virtual_volume_id: UUID

    :param attributes: [required] List of Name/Value pairs in JSON object format. 
    :type attributes: dict

    """
    volume_id = data_model.property(
        "volumeID", int,
        array=False, optional=False,
        documentation="""Unique VolumeID for the volume. """,
        dictionaryType=None
    )
    name = data_model.property(
        "name", str,
        array=False, optional=False,
        documentation="""Name of the volume as provided at creation time. """,
        dictionaryType=None
    )
    account_id = data_model.property(
        "accountID", int,
        array=False, optional=False,
        documentation="""Unique AccountID for the account. """,
        dictionaryType=None
    )
    create_time = data_model.property(
        "createTime", str,
        array=False, optional=False,
        documentation="""UTC formatted time the volume was created. """,
        dictionaryType=None
    )
    volume_consistency_group_uuid = data_model.property(
        "volumeConsistencyGroupUUID", UUID,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    volume_uuid = data_model.property(
        "volumeUUID", UUID,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    enable_snap_mirror_replication = data_model.property(
        "enableSnapMirrorReplication", bool,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    status = data_model.property(
        "status", str,
        array=False, optional=False,
        documentation="""Current status of the volume init: A volume that is being initialized and is not ready for connections. active: An active volume ready for connections. """,
        dictionaryType=None
    )
    access = data_model.property(
        "access", str,
        array=False, optional=False,
        documentation="""Access allowed for the volume readOnly: Only read operations are allowed. readWrite: Reads and writes are allowed. locked: No reads or writes are allowed. replicationTarget: Designated as a target volume in a replicated volume pair. """,
        dictionaryType=None
    )
    enable512e = data_model.property(
        "enable512e", bool,
        array=False, optional=False,
        documentation="""If "true", the volume provides 512 byte sector emulation. """,
        dictionaryType=None
    )
    iqn = data_model.property(
        "iqn", str,
        array=False, optional=True,
        documentation="""Volume iSCSI Qualified Name. """,
        dictionaryType=None
    )
    scsi_euidevice_id = data_model.property(
        "scsiEUIDeviceID", str,
        array=False, optional=False,
        documentation="""Globally unique SCSI device identifier for the volume in EUI-64 based 16-byte format. """,
        dictionaryType=None
    )
    scsi_naadevice_id = data_model.property(
        "scsiNAADeviceID", str,
        array=False, optional=False,
        documentation="""Globally unique SCSI device identifier for the volume in NAA IEEE Registered Extended format. """,
        dictionaryType=None
    )
    qos = data_model.property(
        "qos", VolumeQOS,
        array=False, optional=False,
        documentation="""Quality of service settings for this volume. """,
        dictionaryType=None
    )
    qos_policy_id = data_model.property(
        "qosPolicyID", int,
        array=False, optional=True,
        documentation="""The QoS policy ID associated with the volume. The value is null if the volume is not associated with a policy. """,
        dictionaryType=None
    )
    volume_access_groups = data_model.property(
        "volumeAccessGroups", int,
        array=True, optional=False,
        documentation="""List of volume access groups to which a volume beintegers. """,
        dictionaryType=None
    )
    volume_pairs = data_model.property(
        "volumePairs", VolumePair,
        array=True, optional=False,
        documentation="""Information about a paired volume. Available only if a volume is paired. @see VolumePairs for return values. """,
        dictionaryType=None
    )
    delete_time = data_model.property(
        "deleteTime", str,
        array=False, optional=True,
        documentation="""The time this volume was deleted. If this has no value, the volume has not yet been deleted. """,
        dictionaryType=None
    )
    purge_time = data_model.property(
        "purgeTime", str,
        array=False, optional=True,
        documentation="""The time this volume will be purged from the system. If this has no value, the volume has not yet been deleted (and is not scheduled for purging). """,
        dictionaryType=None
    )
    last_access_time = data_model.property(
        "lastAccessTime", str,
        array=False, optional=True,
        documentation="""The last time any access to this volume occurred. If this has no value, the last access time is not known. """,
        dictionaryType=None
    )
    last_access_time_io = data_model.property(
        "lastAccessTimeIO", str,
        array=False, optional=True,
        documentation="""The last time I/O access to this volume occurred. If this has no value, the last I/O access time is not known. """,
        dictionaryType=None
    )
    slice_count = data_model.property(
        "sliceCount", int,
        array=False, optional=False,
        documentation="""The number of slices backing this volume. In the current software, this value will always be 1. """,
        dictionaryType=None
    )
    total_size = data_model.property(
        "totalSize", int,
        array=False, optional=False,
        documentation="""Total size of this volume in bytes. """,
        dictionaryType=None
    )
    block_size = data_model.property(
        "blockSize", int,
        array=False, optional=False,
        documentation="""Size of the blocks on the volume. """,
        dictionaryType=None
    )
    virtual_volume_id = data_model.property(
        "virtualVolumeID", UUID,
        array=False, optional=True,
        documentation="""Virtual volume ID this volume backs. """,
        dictionaryType=None
    )
    attributes = data_model.property(
        "attributes", dict,
        array=False, optional=False,
        documentation="""List of Name/Value pairs in JSON object format. """,
        dictionaryType=None
    )

    def __init__(self,
            volume_id,
            name,
            account_id,
            create_time,
            volume_consistency_group_uuid,
            volume_uuid,
            enable_snap_mirror_replication,
            status,
            access,
            enable512e,
            scsi_euidevice_id,
            scsi_naadevice_id,
            qos,
            volume_access_groups,
            volume_pairs,
            slice_count,
            total_size,
            block_size,
            attributes,
            iqn=None,
            qos_policy_id=None,
            delete_time=None,
            purge_time=None,
            last_access_time=None,
            last_access_time_io=None,
            virtual_volume_id=None):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class CloneVolumeResult(data_model.DataObject):
    """CloneVolumeResult  

    :param volume:  The resulting volume 
    :type volume: Volume

    :param clone_id: [required] The ID of the newly-created clone. 
    :type clone_id: int

    :param volume_id: [required] The volume ID of the newly-created clone. 
    :type volume_id: int

    :param async_handle: [required] Handle value used to track the progress of the clone. 
    :type async_handle: int

    """
    volume = data_model.property(
        "volume", Volume,
        array=False, optional=True,
        documentation="""The resulting volume """,
        dictionaryType=None
    )
    clone_id = data_model.property(
        "cloneID", int,
        array=False, optional=False,
        documentation="""The ID of the newly-created clone. """,
        dictionaryType=None
    )
    volume_id = data_model.property(
        "volumeID", int,
        array=False, optional=False,
        documentation="""The volume ID of the newly-created clone. """,
        dictionaryType=None
    )
    async_handle = data_model.property(
        "asyncHandle", int,
        array=False, optional=False,
        documentation="""Handle value used to track the progress of the clone. """,
        dictionaryType=None
    )

    def __init__(self,
            clone_id,
            volume_id,
            async_handle,
            volume=None):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class GetVolumeStatsRequest(data_model.DataObject):
    """GetVolumeStatsRequest  
    GetVolumeStats enables  you to retrieve high-level activity measurements for a single volume. Values are cumulative from the creation of the volume.

    :param volume_id: [required] Specifies the volume for which statistics are gathered. 
    :type volume_id: int

    """
    volume_id = data_model.property(
        "volumeID", int,
        array=False, optional=False,
        documentation="""Specifies the volume for which statistics are gathered. """,
        dictionaryType=None
    )

    def __init__(self,
            volume_id):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class QoSPolicy(data_model.DataObject):
    """QoSPolicy  
    The QoSPolicy object contains information about a QoS policy on the cluster.

    :param qos_policy_id: [required] A unique integer identifier for the QoSPolicy auto-assigned by the SolidFire cluster. 
    :type qos_policy_id: int

    :param name: [required] The name of the QoS policy. For example: gold, platinum, or silver. 
    :type name: str

    :param volume_ids: [required] A list of volumes associated with this policy. 
    :type volume_ids: int

    :param qos: [required] Quality of service settings for this volume. 
    :type qos: VolumeQOS

    """
    qos_policy_id = data_model.property(
        "qosPolicyID", int,
        array=False, optional=False,
        documentation="""A unique integer identifier for the QoSPolicy auto-assigned by the SolidFire cluster. """,
        dictionaryType=None
    )
    name = data_model.property(
        "name", str,
        array=False, optional=False,
        documentation="""The name of the QoS policy. For example: gold, platinum, or silver. """,
        dictionaryType=None
    )
    volume_ids = data_model.property(
        "volumeIDs", int,
        array=True, optional=False,
        documentation="""A list of volumes associated with this policy. """,
        dictionaryType=None
    )
    qos = data_model.property(
        "qos", VolumeQOS,
        array=False, optional=False,
        documentation="""Quality of service settings for this volume. """,
        dictionaryType=None
    )

    def __init__(self,
            qos_policy_id,
            name,
            volume_ids,
            qos):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class GetQoSPolicyResult(data_model.DataObject):
    """GetQoSPolicyResult  

    :param qos_policy: [required] Details of the requested QoS policy. 
    :type qos_policy: QoSPolicy

    """
    qos_policy = data_model.property(
        "qosPolicy", QoSPolicy,
        array=False, optional=False,
        documentation="""Details of the requested QoS policy. """,
        dictionaryType=None
    )

    def __init__(self,
            qos_policy):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class GetVolumeAccessGroupLunAssignmentsRequest(data_model.DataObject):
    """GetVolumeAccessGroupLunAssignmentsRequest  
    The GetVolumeAccessGroupLunAssignments
    method enables you to retrieve details on LUN mappings
    of a specified volume access group.

    :param volume_access_group_id: [required] The unique volume access group ID used to return information. 
    :type volume_access_group_id: int

    """
    volume_access_group_id = data_model.property(
        "volumeAccessGroupID", int,
        array=False, optional=False,
        documentation="""The unique volume access group ID used to return information. """,
        dictionaryType=None
    )

    def __init__(self,
            volume_access_group_id):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class ListVolumeStatsRequest(data_model.DataObject):
    """ListVolumeStatsRequest  
    ListVolumeStats returns high-level activity measurements for a single volume, list of volumes, or all volumes (if you omit the volumeIDs parameter). Measurement values are cumulative from the creation of the volume.

    :param volume_ids:  A list of volume IDs of volumes from which to retrieve activity information. 
    :type volume_ids: int

    """
    volume_ids = data_model.property(
        "volumeIDs", int,
        array=True, optional=True,
        documentation="""A list of volume IDs of volumes from which to retrieve activity information. """,
        dictionaryType=None
    )

    def __init__(self,
            volume_ids=None):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class AddAccountRequest(data_model.DataObject):
    """AddAccountRequest  
    You can use AddAccount to add a new account to the system. You can create new volumes under the new account. The CHAP settings you specify for the account apply to all volumes owned by the account.

    :param username: [required] Specifies the username for this account. (Might be 1 to 64 characters in length). 
    :type username: str

    :param initiator_secret:  The CHAP secret to use for the initiator. This secret must be 12-16 characters in length and should be impenetrable. The initiator CHAP secret must be unique and cannot be the same as the target CHAP secret. If unspecified, a random secret is created. 
    :type initiator_secret: CHAPSecret

    :param target_secret:  The CHAP secret to use for the target (mutual CHAP authentication). This secret must be 12-16 characters in length and should be impenetrable. The target CHAP secret must be unique and cannot be the same as the initiator CHAP secret. If unspecified, a random secret is created. 
    :type target_secret: CHAPSecret

    :param attributes:  List of name-value pairs in JSON object format. 
    :type attributes: dict

    """
    username = data_model.property(
        "username", str,
        array=False, optional=False,
        documentation="""Specifies the username for this account. (Might be 1 to 64 characters in length). """,
        dictionaryType=None
    )
    initiator_secret = data_model.property(
        "initiatorSecret", CHAPSecret,
        array=False, optional=True,
        documentation="""The CHAP secret to use for the initiator. This secret must be 12-16 characters in length and should be impenetrable. The initiator CHAP secret must be unique and cannot be the same as the target CHAP secret. If unspecified, a random secret is created. """,
        dictionaryType=None
    )
    target_secret = data_model.property(
        "targetSecret", CHAPSecret,
        array=False, optional=True,
        documentation="""The CHAP secret to use for the target (mutual CHAP authentication). This secret must be 12-16 characters in length and should be impenetrable. The target CHAP secret must be unique and cannot be the same as the initiator CHAP secret. If unspecified, a random secret is created. """,
        dictionaryType=None
    )
    attributes = data_model.property(
        "attributes", dict,
        array=False, optional=True,
        documentation="""List of name-value pairs in JSON object format. """,
        dictionaryType=None
    )

    def __init__(self,
            username,
            initiator_secret=None,
            target_secret=None,
            attributes=None):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class GetAccountByNameRequest(data_model.DataObject):
    """GetAccountByNameRequest  
    GetAccountByName enables you to retrieve details about a specific account, given its username.

    :param username: [required] Username for the account. 
    :type username: str

    """
    username = data_model.property(
        "username", str,
        array=False, optional=False,
        documentation="""Username for the account. """,
        dictionaryType=None
    )

    def __init__(self,
            username):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class ListVolumeStatsByVolumeAccessGroupResult(data_model.DataObject):
    """ListVolumeStatsByVolumeAccessGroupResult  

    :param volume_stats: [required] List of account activity information. Note: The volumeID member is 0 for each entry, as the values represent the summation of all volumes owned by the account. 
    :type volume_stats: VolumeStats

    """
    volume_stats = data_model.property(
        "volumeStats", VolumeStats,
        array=True, optional=False,
        documentation="""List of account activity information. Note: The volumeID member is 0 for each entry, as the values represent the summation of all volumes owned by the account. """,
        dictionaryType=None
    )

    def __init__(self,
            volume_stats):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class CreateBackupTargetResult(data_model.DataObject):
    """CreateBackupTargetResult  

    :param backup_target_id: [required] Unique identifier assigned to the backup target. 
    :type backup_target_id: int

    """
    backup_target_id = data_model.property(
        "backupTargetID", int,
        array=False, optional=False,
        documentation="""Unique identifier assigned to the backup target. """,
        dictionaryType=None
    )

    def __init__(self,
            backup_target_id):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class ListVirtualVolumeHostsRequest(data_model.DataObject):
    """ListVirtualVolumeHostsRequest  
    ListVirtualVolumeHosts returns a list of all virtual volume hosts known to the cluster. A virtual volume host is a VMware ESX host
    that has initiated a session with the VASA API provider.

    :param virtual_volume_host_ids:  A list of virtual volume host IDs for which to retrieve information. If you omit this parameter, the method returns information about all virtual volume hosts. 
    :type virtual_volume_host_ids: UUID

    """
    virtual_volume_host_ids = data_model.property(
        "virtualVolumeHostIDs", UUID,
        array=True, optional=True,
        documentation="""A list of virtual volume host IDs for which to retrieve information. If you omit this parameter, the method returns information about all virtual volume hosts. """,
        dictionaryType=None
    )

    def __init__(self,
            virtual_volume_host_ids=None):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class SetNodeSSLCertificateResult(data_model.DataObject):
    """SetNodeSSLCertificateResult  

    """

    def __init__(self):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class RemoveDrivesRequest(data_model.DataObject):
    """RemoveDrivesRequest  
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

    :param force_during_upgrade:  If you want to remove a drive during upgrade, this must be set to true. 
    :type force_during_upgrade: bool

    """
    drives = data_model.property(
        "drives", int,
        array=True, optional=False,
        documentation="""List of driveIDs to remove from the cluster. """,
        dictionaryType=None
    )
    force_during_upgrade = data_model.property(
        "forceDuringUpgrade", bool,
        array=False, optional=True,
        documentation="""If you want to remove a drive during upgrade, this must be set to true. """,
        dictionaryType=None
    )

    def __init__(self,
            drives,
            force_during_upgrade=None):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class CancelCloneResult(data_model.DataObject):
    """CancelCloneResult  

    """

    def __init__(self):
        kwargs = locals()
        del kwargs["self"]
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
        documentation="""Identifies which user authentcation method will be used.  Valid values: DirectBind SearchAndBind """,
        dictionaryType=None
    )
    enabled = data_model.property(
        "enabled", bool,
        array=False, optional=False,
        documentation="""Identifies whether or not the system is enabled for LDAP.  Valid values: true false """,
        dictionaryType=None
    )
    group_search_base_dn = data_model.property(
        "groupSearchBaseDN", str,
        array=False, optional=False,
        documentation="""The base DN of the tree to start the group search (will do a subtree search from here). """,
        dictionaryType=None
    )
    group_search_custom_filter = data_model.property(
        "groupSearchCustomFilter", str,
        array=False, optional=False,
        documentation="""The custom search filter used. """,
        dictionaryType=None
    )
    group_search_type = data_model.property(
        "groupSearchType", str,
        array=False, optional=False,
        documentation="""Controls the default group search filter used, can be one of the following: NoGroups: No group support. ActiveDirectory: Nested membership of all of a user's AD groups. MemberDN: MemberDN style groups (single-level). """,
        dictionaryType=None
    )
    search_bind_dn = data_model.property(
        "searchBindDN", str,
        array=False, optional=False,
        documentation="""A fully qualified DN to log in with to perform an LDAP search for the user (needs read access to the LDAP directory). """,
        dictionaryType=None
    )
    server_uris = data_model.property(
        "serverURIs", str,
        array=True, optional=False,
        documentation="""A comma-separated list of LDAP server URIs (examples: "ldap://1.2.3.4" and ldaps://1.2.3.4:123") """,
        dictionaryType=None
    )
    user_dntemplate = data_model.property(
        "userDNTemplate", str,
        array=False, optional=False,
        documentation="""A string that is used to form a fully qualified user DN. """,
        dictionaryType=None
    )
    user_search_base_dn = data_model.property(
        "userSearchBaseDN", str,
        array=False, optional=False,
        documentation="""The base DN of the tree used to start the search (will do a subtree search from here). """,
        dictionaryType=None
    )
    user_search_filter = data_model.property(
        "userSearchFilter", str,
        array=False, optional=False,
        documentation="""The LDAP filter used. """,
        dictionaryType=None
    )

    def __init__(self,
            auth_type,
            enabled,
            group_search_base_dn,
            group_search_custom_filter,
            group_search_type,
            search_bind_dn,
            server_uris,
            user_dntemplate,
            user_search_base_dn,
            user_search_filter):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class TestLdapAuthenticationRequest(data_model.DataObject):
    """TestLdapAuthenticationRequest  
    The TestLdapAuthentication method enables you to validate the currently enabled LDAP authentication settings. If the configuration is
    correct, the API call returns the group membership of the tested user.

    :param username: [required] The username to be tested. 
    :type username: str

    :param password: [required] The password for the username to be tested. 
    :type password: str

    :param ldap_configuration:  An ldapConfiguration object to be tested. If specified, the API call tests the provided configuration even if LDAP authentication is disabled. 
    :type ldap_configuration: LdapConfiguration

    """
    username = data_model.property(
        "username", str,
        array=False, optional=False,
        documentation="""The username to be tested. """,
        dictionaryType=None
    )
    password = data_model.property(
        "password", str,
        array=False, optional=False,
        documentation="""The password for the username to be tested. """,
        dictionaryType=None
    )
    ldap_configuration = data_model.property(
        "ldapConfiguration", LdapConfiguration,
        array=False, optional=True,
        documentation="""An ldapConfiguration object to be tested. If specified, the API call tests the provided configuration even if LDAP authentication is disabled. """,
        dictionaryType=None
    )

    def __init__(self,
            username,
            password,
            ldap_configuration=None):
        kwargs = locals()
        del kwargs["self"]
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

    :param product: [required]  
    :type product: str

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
        documentation=""" """,
        dictionaryType=None
    )
    connected = data_model.property(
        "connected", bool,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    dev = data_model.property(
        "dev", int,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    dev_path = data_model.property(
        "devPath", str,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    drive_type = data_model.property(
        "driveType", str,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    product = data_model.property(
        "product", str,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    name = data_model.property(
        "name", str,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    path = data_model.property(
        "path", str,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    path_link = data_model.property(
        "pathLink", str,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    scsi_compat_id = data_model.property(
        "scsiCompatId", str,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    smart_ssd_write_capable = data_model.property(
        "smartSsdWriteCapable", bool,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )
    security_enabled = data_model.property(
        "securityEnabled", bool,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    security_frozen = data_model.property(
        "securityFrozen", bool,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    security_locked = data_model.property(
        "securityLocked", bool,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    security_supported = data_model.property(
        "securitySupported", bool,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    size = data_model.property(
        "size", int,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    slot = data_model.property(
        "slot", int,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    uuid = data_model.property(
        "uuid", UUID,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    vendor = data_model.property(
        "vendor", str,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    version = data_model.property(
        "version", str,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    security_at_maximum = data_model.property(
        "securityAtMaximum", bool,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    serial = data_model.property(
        "serial", str,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    scsi_state = data_model.property(
        "scsiState", str,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )

    def __init__(self,
            canonical_name,
            connected,
            dev,
            dev_path,
            drive_type,
            product,
            name,
            path,
            path_link,
            scsi_compat_id,
            security_enabled,
            security_frozen,
            security_locked,
            security_supported,
            size,
            slot,
            uuid,
            vendor,
            version,
            security_at_maximum,
            serial,
            scsi_state,
            smart_ssd_write_capable=None):
        kwargs = locals()
        del kwargs["self"]
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
        documentation=""" """,
        dictionaryType=None
    )
    num_block_actual = data_model.property(
        "numBlockActual", int,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    num_block_expected = data_model.property(
        "numBlockExpected", int,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    num_slice_actual = data_model.property(
        "numSliceActual", int,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    num_slice_expected = data_model.property(
        "numSliceExpected", int,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    num_total_actual = data_model.property(
        "numTotalActual", int,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    num_total_expected = data_model.property(
        "numTotalExpected", int,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )

    def __init__(self,
            drives,
            num_block_actual,
            num_block_expected,
            num_slice_actual,
            num_slice_expected,
            num_total_actual,
            num_total_expected):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class GetDriveConfigResult(data_model.DataObject):
    """GetDriveConfigResult  

    :param drive_config: [required] Configuration information for the drives that are connected to the cluster 
    :type drive_config: DrivesConfigInfo

    """
    drive_config = data_model.property(
        "driveConfig", DrivesConfigInfo,
        array=False, optional=False,
        documentation="""Configuration information for the drives that are connected to the cluster """,
        dictionaryType=None
    )

    def __init__(self,
            drive_config):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class GetNodeStatsRequest(data_model.DataObject):
    """GetNodeStatsRequest  
    GetNodeStats enables you to retrieve the high-level activity measurements for a single node.

    :param node_id: [required] Specifies the node for which statistics are gathered. 
    :type node_id: int

    """
    node_id = data_model.property(
        "nodeID", int,
        array=False, optional=False,
        documentation="""Specifies the node for which statistics are gathered. """,
        dictionaryType=None
    )

    def __init__(self,
            node_id):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class ResetDrivesRequest(data_model.DataObject):
    """ResetDrivesRequest  
    ResetDrives enables you to proactively initialize drives and remove all data currently residing on a drive. The drive can then be reused
    in an existing node or used in an upgraded node. This method requires the force parameter to be included in the method call.

    :param drives: [required] List of device names (not driveIDs) to reset. 
    :type drives: str

    :param force: [required] Required parameter to successfully reset a drive. 
    :type force: bool

    """
    drives = data_model.property(
        "drives", str,
        array=False, optional=False,
        documentation="""List of device names (not driveIDs) to reset. """,
        dictionaryType=None
    )
    force = data_model.property(
        "force", bool,
        array=False, optional=False,
        documentation="""Required parameter to successfully reset a drive. """,
        dictionaryType=None
    )

    def __init__(self,
            drives,
            force):
        kwargs = locals()
        del kwargs["self"]
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

    :param drive_ids: [required]  
    :type drive_ids: int

    :param time_of_report: [required]  
    :type time_of_report: str

    :param time_of_publish: [required]  
    :type time_of_publish: str

    :param details:   
    :type details: str

    """
    event_id = data_model.property(
        "eventID", int,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    severity = data_model.property(
        "severity", int,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    event_info_type = data_model.property(
        "eventInfoType", str,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    message = data_model.property(
        "message", str,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    service_id = data_model.property(
        "serviceID", int,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    node_id = data_model.property(
        "nodeID", int,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    drive_id = data_model.property(
        "driveID", int,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    drive_ids = data_model.property(
        "driveIDs", int,
        array=True, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    time_of_report = data_model.property(
        "timeOfReport", str,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    time_of_publish = data_model.property(
        "timeOfPublish", str,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    details = data_model.property(
        "details", str,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )

    def __init__(self,
            event_id,
            severity,
            event_info_type,
            message,
            service_id,
            node_id,
            drive_id,
            drive_ids,
            time_of_report,
            time_of_publish,
            details=None):
        kwargs = locals()
        del kwargs["self"]
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
        documentation=""" """,
        dictionaryType=None
    )
    events = data_model.property(
        "events", EventInfo,
        array=True, optional=False,
        documentation=""" """,
        dictionaryType=None
    )

    def __init__(self,
            event_queue_type,
            events):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class ModifyBackupTargetRequest(data_model.DataObject):
    """ModifyBackupTargetRequest  
    ModifyBackupTarget enables you to change attributes of a backup target.

    :param backup_target_id: [required] The unique target ID for the target to modify. 
    :type backup_target_id: int

    :param name:  The new name for the backup target. 
    :type name: str

    :param attributes:  List of name-value pairs in JSON object format. 
    :type attributes: dict

    """
    backup_target_id = data_model.property(
        "backupTargetID", int,
        array=False, optional=False,
        documentation="""The unique target ID for the target to modify. """,
        dictionaryType=None
    )
    name = data_model.property(
        "name", str,
        array=False, optional=True,
        documentation="""The new name for the backup target. """,
        dictionaryType=None
    )
    attributes = data_model.property(
        "attributes", dict,
        array=False, optional=True,
        documentation="""List of name-value pairs in JSON object format. """,
        dictionaryType=None
    )

    def __init__(self,
            backup_target_id,
            name=None,
            attributes=None):
        kwargs = locals()
        del kwargs["self"]
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

    :param cluster_uuid:  The cluster UUID 
    :type cluster_uuid: str

    """
    cluster_name = data_model.property(
        "clusterName", str,
        array=False, optional=False,
        documentation="""Name of the other cluster in the pair """,
        dictionaryType=None
    )
    cluster_pair_id = data_model.property(
        "clusterPairID", int,
        array=False, optional=False,
        documentation="""Unique ID given to each cluster in the pair. """,
        dictionaryType=None
    )
    cluster_pair_uuid = data_model.property(
        "clusterPairUUID", UUID,
        array=False, optional=False,
        documentation="""Universally unique identifier. """,
        dictionaryType=None
    )
    latency = data_model.property(
        "latency", int,
        array=False, optional=False,
        documentation="""Number, in milliseconds, of latency between clusters. """,
        dictionaryType=None
    )
    mvip = data_model.property(
        "mvip", str,
        array=False, optional=False,
        documentation="""IP of the management connection for paired clusters. """,
        dictionaryType=None
    )
    status = data_model.property(
        "status", str,
        array=False, optional=False,
        documentation="""Can be one of the following: Connected Misconfigured Disconnected """,
        dictionaryType=None
    )
    version = data_model.property(
        "version", str,
        array=False, optional=False,
        documentation="""The Element OS version of the other cluster in the pair. """,
        dictionaryType=None
    )
    cluster_uuid = data_model.property(
        "clusterUUID", str,
        array=False, optional=True,
        documentation="""The cluster UUID """,
        dictionaryType=None
    )

    def __init__(self,
            cluster_name,
            cluster_pair_id,
            cluster_pair_uuid,
            latency,
            mvip,
            status,
            version,
            cluster_uuid=None):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class ListClusterPairsResult(data_model.DataObject):
    """ListClusterPairsResult  

    :param cluster_pairs: [required] Information about each paired cluster. 
    :type cluster_pairs: PairedCluster

    """
    cluster_pairs = data_model.property(
        "clusterPairs", PairedCluster,
        array=True, optional=False,
        documentation="""Information about each paired cluster. """,
        dictionaryType=None
    )

    def __init__(self,
            cluster_pairs):
        kwargs = locals()
        del kwargs["self"]
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
        documentation=""" """,
        dictionaryType=None
    )
    node_version = data_model.property(
        "nodeVersion", str,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    node_internal_revision = data_model.property(
        "nodeInternalRevision", str,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )

    def __init__(self,
            node_id,
            node_version,
            node_internal_revision):
        kwargs = locals()
        del kwargs["self"]
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
        documentation=""" """,
        dictionaryType=None
    )
    node_id = data_model.property(
        "nodeID", int,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    package_name = data_model.property(
        "packageName", str,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    pending_version = data_model.property(
        "pendingVersion", str,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    start_time = data_model.property(
        "startTime", str,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )

    def __init__(self,
            current_version,
            node_id,
            package_name,
            pending_version,
            start_time):
        kwargs = locals()
        del kwargs["self"]
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
        documentation=""" """,
        dictionaryType=None
    )
    cluster_version = data_model.property(
        "clusterVersion", str,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    cluster_version_info = data_model.property(
        "clusterVersionInfo", ClusterVersionInfo,
        array=True, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    software_version_info = data_model.property(
        "softwareVersionInfo", SoftwareVersionInfo,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )

    def __init__(self,
            cluster_apiversion,
            cluster_version,
            cluster_version_info,
            software_version_info):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class CopyVolumeRequest(data_model.DataObject):
    """CopyVolumeRequest  
    CopyVolume enables you to overwrite the data contents of an existing volume with the data contents of another volume (or
    snapshot). Attributes of the destination volume such as IQN, QoS settings, size, account, and volume access group membership are
    not changed. The destination volume must already exist and must be the same size as the source volume.
    NetApp strongly recommends that clients unmount the destination volume before the CopyVolume operation begins. If the
    destination volume is modified during the copy operation, the changes will be lost.
    This method is asynchronous and may take a variable amount of time to complete. You can use the GetAsyncResult method to
    determine when the process has finished, and ListSyncJobs to see the progress of the copy.

    :param volume_id: [required] VolumeID of the volume to be read from. 
    :type volume_id: int

    :param dst_volume_id: [required] VolumeID of the volume to be overwritten. 
    :type dst_volume_id: int

    :param snapshot_id:  ID of the snapshot that is used as the source of the clone. If no ID is provided, the current active volume is used. 
    :type snapshot_id: int

    """
    volume_id = data_model.property(
        "volumeID", int,
        array=False, optional=False,
        documentation="""VolumeID of the volume to be read from. """,
        dictionaryType=None
    )
    dst_volume_id = data_model.property(
        "dstVolumeID", int,
        array=False, optional=False,
        documentation="""VolumeID of the volume to be overwritten. """,
        dictionaryType=None
    )
    snapshot_id = data_model.property(
        "snapshotID", int,
        array=False, optional=True,
        documentation="""ID of the snapshot that is used as the source of the clone. If no ID is provided, the current active volume is used. """,
        dictionaryType=None
    )

    def __init__(self,
            volume_id,
            dst_volume_id,
            snapshot_id=None):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class CreateQoSPolicyResult(data_model.DataObject):
    """CreateQoSPolicyResult  

    :param qos_policy: [required] The newly created QoSPolicy object. 
    :type qos_policy: QoSPolicy

    """
    qos_policy = data_model.property(
        "qosPolicy", QoSPolicy,
        array=False, optional=False,
        documentation="""The newly created QoSPolicy object. """,
        dictionaryType=None
    )

    def __init__(self,
            qos_policy):
        kwargs = locals()
        del kwargs["self"]
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

    :param namespace:   
    :type namespace: bool

    """
    address = data_model.property(
        "address", str,
        array=False, optional=False,
        documentation="""IP address of the network. """,
        dictionaryType=None
    )
    broadcast = data_model.property(
        "broadcast", str,
        array=False, optional=False,
        documentation="""Address of NTP broadcast. """,
        dictionaryType=None
    )
    mac_address = data_model.property(
        "macAddress", str,
        array=False, optional=False,
        documentation="""Address used to configure the interface. """,
        dictionaryType=None
    )
    mtu = data_model.property(
        "mtu", int,
        array=False, optional=False,
        documentation="""Packet size on the network interface. """,
        dictionaryType=None
    )
    name = data_model.property(
        "name", str,
        array=False, optional=False,
        documentation="""Name of the network interface. """,
        dictionaryType=None
    )
    netmask = data_model.property(
        "netmask", str,
        array=False, optional=False,
        documentation="""Netmask for the network interface. """,
        dictionaryType=None
    )
    status = data_model.property(
        "status", str,
        array=False, optional=False,
        documentation="""Status of the network. """,
        dictionaryType=None
    )
    type = data_model.property(
        "type", str,
        array=False, optional=False,
        documentation="""The type of network, ie, BondMaster. """,
        dictionaryType=None
    )
    virtual_network_tag = data_model.property(
        "virtualNetworkTag", int,
        array=False, optional=False,
        documentation="""Virtual Network Tag if on virtual network. """,
        dictionaryType=None
    )
    namespace = data_model.property(
        "namespace", bool,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )

    def __init__(self,
            address,
            broadcast,
            mac_address,
            mtu,
            name,
            netmask,
            status,
            type,
            virtual_network_tag,
            namespace=None):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class ListNetworkInterfacesResult(data_model.DataObject):
    """ListNetworkInterfacesResult  

    :param interfaces: [required]  
    :type interfaces: NetworkInterface

    """
    interfaces = data_model.property(
        "interfaces", NetworkInterface,
        array=True, optional=False,
        documentation=""" """,
        dictionaryType=None
    )

    def __init__(self,
            interfaces):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class CreateVolumeAccessGroupRequest(data_model.DataObject):
    """CreateVolumeAccessGroupRequest  
    You can use CreateVolumeAccessGroup to create a new volume access group. When you create the volume access group, you need to give it a name, and you can optionally enter initiators and volumes. After you create the group, you can add volumes and initiator IQNs. Any initiator IQN that you add to the volume access group is able to access any volume in the group without CHAP authentication.

    :param name: [required] The name for this volume access group. Not required to be unique, but recommended. 
    :type name: str

    :param initiators:  List of initiators to include in the volume access group. If unspecified, the access group's configured initiators are not modified. 
    :type initiators: str

    :param volumes:  List of volumes to initially include in the volume access group. If unspecified, the access group's volumes are not modified. 
    :type volumes: int

    :param virtual_network_id:  The ID of the SolidFire virtual network to associate the volume access group with. 
    :type virtual_network_id: int

    :param virtual_network_tags:  The ID of the SolidFire virtual network to associate the volume access group with. 
    :type virtual_network_tags: int

    :param attributes:  List of name-value pairs in JSON object format. 
    :type attributes: dict

    """
    name = data_model.property(
        "name", str,
        array=False, optional=False,
        documentation="""The name for this volume access group. Not required to be unique, but recommended. """,
        dictionaryType=None
    )
    initiators = data_model.property(
        "initiators", str,
        array=True, optional=True,
        documentation="""List of initiators to include in the volume access group. If unspecified, the access group's configured initiators are not modified. """,
        dictionaryType=None
    )
    volumes = data_model.property(
        "volumes", int,
        array=True, optional=True,
        documentation="""List of volumes to initially include in the volume access group. If unspecified, the access group's volumes are not modified. """,
        dictionaryType=None
    )
    virtual_network_id = data_model.property(
        "virtualNetworkID", int,
        array=True, optional=True,
        documentation="""The ID of the SolidFire virtual network to associate the volume access group with. """,
        dictionaryType=None
    )
    virtual_network_tags = data_model.property(
        "virtualNetworkTags", int,
        array=True, optional=True,
        documentation="""The ID of the SolidFire virtual network to associate the volume access group with. """,
        dictionaryType=None
    )
    attributes = data_model.property(
        "attributes", dict,
        array=False, optional=True,
        documentation="""List of name-value pairs in JSON object format. """,
        dictionaryType=None
    )

    def __init__(self,
            name,
            initiators=None,
            volumes=None,
            virtual_network_id=None,
            virtual_network_tags=None,
            attributes=None):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class CreateSnapshotRequest(data_model.DataObject):
    """CreateSnapshotRequest  
    CreateSnapshot enables you to create a point-in-time copy of a volume. You can create a snapshot from any volume or from an existing snapshot. If you do not provide a SnapshotID with this API method, a snapshot is created from the volume's active branch.
    If the volume from which the snapshot is created is being replicated to a remote cluster, the snapshot can also be replicated to the same target. Use the enableRemoteReplication parameter to enable snapshot replication.
    Note: Creating a snapshot is allowed if cluster fullness is at stage 2 or 3. Snapshots are not created when cluster fullness is at stage 4 or 5.

    :param volume_id: [required] Specifies the unique ID of the volume image from which to copy. 
    :type volume_id: int

    :param snapshot_id:  Specifies the unique ID of a snapshot from which the new snapshot is made. The snapshotID passed must be a snapshot on the given volume. 
    :type snapshot_id: int

    :param name:  Specifies a name for the snapshot. If unspecified, the date and time the snapshot was taken is used. 
    :type name: str

    :param enable_remote_replication:  Replicates the snapshot created to a remote cluster. Possible values are: true: The snapshot is replicated to remote storage. false: Default. The snapshot is not replicated. 
    :type enable_remote_replication: bool

    :param retention:  Specifies the amount of time for which the snapshot is retained. The format is HH:mm:ss. 
    :type retention: str

    :param attributes:  List of name-value pairs in JSON object format. 
    :type attributes: dict

    :param snap_mirror_label:  Label used by SnapMirror software to specify snapshot retention policy on SnapMirror endpoint. 
    :type snap_mirror_label: str

    """
    volume_id = data_model.property(
        "volumeID", int,
        array=False, optional=False,
        documentation="""Specifies the unique ID of the volume image from which to copy. """,
        dictionaryType=None
    )
    snapshot_id = data_model.property(
        "snapshotID", int,
        array=False, optional=True,
        documentation="""Specifies the unique ID of a snapshot from which the new snapshot is made. The snapshotID passed must be a snapshot on the given volume. """,
        dictionaryType=None
    )
    name = data_model.property(
        "name", str,
        array=False, optional=True,
        documentation="""Specifies a name for the snapshot. If unspecified, the date and time the snapshot was taken is used. """,
        dictionaryType=None
    )
    enable_remote_replication = data_model.property(
        "enableRemoteReplication", bool,
        array=False, optional=True,
        documentation="""Replicates the snapshot created to a remote cluster. Possible values are: true: The snapshot is replicated to remote storage. false: Default. The snapshot is not replicated. """,
        dictionaryType=None
    )
    retention = data_model.property(
        "retention", str,
        array=False, optional=True,
        documentation="""Specifies the amount of time for which the snapshot is retained. The format is HH:mm:ss. """,
        dictionaryType=None
    )
    attributes = data_model.property(
        "attributes", dict,
        array=False, optional=True,
        documentation="""List of name-value pairs in JSON object format. """,
        dictionaryType=None
    )
    snap_mirror_label = data_model.property(
        "snapMirrorLabel", str,
        array=False, optional=True,
        documentation="""Label used by SnapMirror software to specify snapshot retention policy on SnapMirror endpoint. """,
        dictionaryType=None
    )

    def __init__(self,
            volume_id,
            snapshot_id=None,
            name=None,
            enable_remote_replication=None,
            retention=None,
            attributes=None,
            snap_mirror_label=None):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class DeleteVolumesRequest(data_model.DataObject):
    """DeleteVolumesRequest  
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
        documentation="""A list of account IDs. All volumes from these accounts are deleted from the system.  """,
        dictionaryType=None
    )
    volume_access_group_ids = data_model.property(
        "volumeAccessGroupIDs", int,
        array=True, optional=True,
        documentation="""A list of volume access group IDs. All of the volumes from all of the volume access groups you specify in this list are deleted from the system. """,
        dictionaryType=None
    )
    volume_ids = data_model.property(
        "volumeIDs", int,
        array=True, optional=True,
        documentation="""The list of IDs of the volumes to delete from the system. """,
        dictionaryType=None
    )

    def __init__(self,
            account_ids=None,
            volume_access_group_ids=None,
            volume_ids=None):
        kwargs = locals()
        del kwargs["self"]
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
        documentation=""" """,
        dictionaryType=None
    )
    async_handle = data_model.property(
        "asyncHandle", int,
        array=False, optional=False,
        documentation="""Handle value used to track the progress of the volume copy. """,
        dictionaryType=None
    )

    def __init__(self,
            clone_id,
            async_handle):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class RestartServicesRequest(data_model.DataObject):
    """RestartServicesRequest  
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
    force = data_model.property(
        "force", bool,
        array=False, optional=False,
        documentation="""Required parameter to successfully restart services on a node. """,
        dictionaryType=None
    )
    service = data_model.property(
        "service", str,
        array=False, optional=True,
        documentation="""Service name to be restarted. """,
        dictionaryType=None
    )
    action = data_model.property(
        "action", str,
        array=False, optional=True,
        documentation="""Action to perform on the service (start, stop, restart). """,
        dictionaryType=None
    )

    def __init__(self,
            force,
            service=None,
            action=None):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class SetNodeSSLCertificateRequest(data_model.DataObject):
    """SetNodeSSLCertificateRequest  
    You can use the SetNodeSSLCertificate method to set a user SSL certificate and private key for the management node.

    :param certificate: [required] The PEM-encoded text version of the certificate. 
    :type certificate: str

    :param private_key: [required] The PEM-encoded text version of the private key. 
    :type private_key: str

    """
    certificate = data_model.property(
        "certificate", str,
        array=False, optional=False,
        documentation="""The PEM-encoded text version of the certificate. """,
        dictionaryType=None
    )
    private_key = data_model.property(
        "privateKey", str,
        array=False, optional=False,
        documentation="""The PEM-encoded text version of the private key. """,
        dictionaryType=None
    )

    def __init__(self,
            certificate,
            private_key):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class DeleteQoSPolicyResult(data_model.DataObject):
    """DeleteQoSPolicyResult  

    """

    def __init__(self):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class SetSSLCertificateRequest(data_model.DataObject):
    """SetSSLCertificateRequest  
    You can use the SetSSLCertificate method to set a user SSL certificate and a private key for the cluster.

    :param certificate: [required] The PEM-encoded text version of the certificate. 
    :type certificate: str

    :param private_key: [required] The PEM-encoded text version of the private key. 
    :type private_key: str

    """
    certificate = data_model.property(
        "certificate", str,
        array=False, optional=False,
        documentation="""The PEM-encoded text version of the certificate. """,
        dictionaryType=None
    )
    private_key = data_model.property(
        "privateKey", str,
        array=False, optional=False,
        documentation="""The PEM-encoded text version of the private key. """,
        dictionaryType=None
    )

    def __init__(self,
            certificate,
            private_key):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class GetNvramInfoResult(data_model.DataObject):
    """GetNvramInfoResult  

    :param nvram_info: [required] Arrays of events and errors detected on the NVRAM card. 
    :type nvram_info: dict

    """
    nvram_info = data_model.property(
        "nvramInfo", dict,
        array=False, optional=False,
        documentation="""Arrays of events and errors detected on the NVRAM card. """,
        dictionaryType=None
    )

    def __init__(self,
            nvram_info):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class GetClusterMasterNodeIDResult(data_model.DataObject):
    """GetClusterMasterNodeIDResult  

    :param node_id: [required] ID of the master node. 
    :type node_id: int

    """
    node_id = data_model.property(
        "nodeID", int,
        array=False, optional=False,
        documentation="""ID of the master node. """,
        dictionaryType=None
    )

    def __init__(self,
            node_id):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class ListDriveHardwareRequest(data_model.DataObject):
    """ListDriveHardwareRequest  
    ListDriveHardware returns all the drives connected to a node. Use this method on individual nodes to return drive hardware
    information or use this method on the cluster master node MVIP to see information for all the drives on all nodes.
    Note: The "securitySupported": true line of the method response does not imply that the drives are capable of
    encryption; only that the security status can be queried. If you have a node type with a model number ending in "-NE",
    commands to enable security features on these drives will fail. See the EnableEncryptionAtRest method for more information.

    :param force: [required] To run this command, the force parameter must be set to true. 
    :type force: bool

    """
    force = data_model.property(
        "force", bool,
        array=False, optional=False,
        documentation="""To run this command, the force parameter must be set to true. """,
        dictionaryType=None
    )

    def __init__(self,
            force):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class DeleteVolumeResult(data_model.DataObject):
    """DeleteVolumeResult  

    :param volume:   
    :type volume: Volume

    """
    volume = data_model.property(
        "volume", Volume,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )

    def __init__(self,
            volume=None):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class NodeWaitingToJoin(data_model.DataObject):
    """NodeWaitingToJoin  

    :param name:   
    :type name: str

    :param version: [required]  
    :type version: str

    :param node_id:   
    :type node_id: int

    :param pending_node_id:   
    :type pending_node_id: int

    :param mip:   
    :type mip: str

    :param cip:   
    :type cip: str

    :param sip:   
    :type sip: str

    :param compatible: [required]  
    :type compatible: bool

    :param chassis_type:   
    :type chassis_type: str

    :param hostname:   
    :type hostname: str

    :param node_type:   
    :type node_type: str

    """
    name = data_model.property(
        "name", str,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )
    version = data_model.property(
        "version", str,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    node_id = data_model.property(
        "nodeID", int,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )
    pending_node_id = data_model.property(
        "pendingNodeID", int,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )
    mip = data_model.property(
        "mip", str,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )
    cip = data_model.property(
        "cip", str,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )
    sip = data_model.property(
        "sip", str,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )
    compatible = data_model.property(
        "compatible", bool,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    chassis_type = data_model.property(
        "chassisType", str,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )
    hostname = data_model.property(
        "hostname", str,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )
    node_type = data_model.property(
        "nodeType", str,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )

    def __init__(self,
            version,
            compatible,
            name=None,
            node_id=None,
            pending_node_id=None,
            mip=None,
            cip=None,
            sip=None,
            chassis_type=None,
            hostname=None,
            node_type=None):
        kwargs = locals()
        del kwargs["self"]
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
        documentation="""Name of the cluster. """,
        dictionaryType=None
    )
    node_name = data_model.property(
        "nodeName", str,
        array=False, optional=False,
        documentation="""Name of the node. """,
        dictionaryType=None
    )
    nodes = data_model.property(
        "nodes", NodeWaitingToJoin,
        array=True, optional=False,
        documentation="""List of descriptions for each node that is actively waiting to join this cluster: compatible - Indicates if the listed node is compatible with the node the API call was executed against. name - IP address of each node. version - version of SolidFire Element software currently installed on the node. """,
        dictionaryType=None
    )
    version = data_model.property(
        "version", str,
        array=False, optional=False,
        documentation="""Version of the SolidFire Element software currently installed. """,
        dictionaryType=None
    )

    def __init__(self,
            cluster_name,
            node_name,
            nodes,
            version):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class ListTestsResult(data_model.DataObject):
    """ListTestsResult  

    :param tests: [required] List of tests that can be performed on the node. 
    :type tests: str

    """
    tests = data_model.property(
        "tests", str,
        array=False, optional=False,
        documentation="""List of tests that can be performed on the node. """,
        dictionaryType=None
    )

    def __init__(self,
            tests):
        kwargs = locals()
        del kwargs["self"]
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
        documentation="""Hostname or IP address of the log server. """,
        dictionaryType=None
    )
    port = data_model.property(
        "port", int,
        array=False, optional=False,
        documentation="""Port number that the log server is listening on. """,
        dictionaryType=None
    )

    def __init__(self,
            host,
            port):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class SetRemoteLoggingHostsRequest(data_model.DataObject):
    """SetRemoteLoggingHostsRequest  
    SetRemoteLoggingHosts enables you to configure remote logging from the nodes in the storage cluster to a centralized log server or servers. Remote logging is performed over TCP using the default port 514. This API does not add to the existing logging hosts. Rather, it replaces what currently exists with new values specified by this API method. You can use GetRemoteLoggingHosts to determine what the current logging hosts are, and then use SetRemoteLoggingHosts to set the desired list of current and new logging hosts.

    :param remote_hosts: [required] A list of hosts to send log messages to. 
    :type remote_hosts: LoggingServer

    """
    remote_hosts = data_model.property(
        "remoteHosts", LoggingServer,
        array=True, optional=False,
        documentation="""A list of hosts to send log messages to. """,
        dictionaryType=None
    )

    def __init__(self,
            remote_hosts):
        kwargs = locals()
        del kwargs["self"]
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
        documentation=""" """,
        dictionaryType=None
    )
    result = data_model.property(
        "result", dict,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )

    def __init__(self,
            node_id,
            result):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class GetIpmiConfigResult(data_model.DataObject):
    """GetIpmiConfigResult  

    :param nodes: [required]  
    :type nodes: GetIpmiConfigNodesResult

    """
    nodes = data_model.property(
        "nodes", GetIpmiConfigNodesResult,
        array=True, optional=False,
        documentation=""" """,
        dictionaryType=None
    )

    def __init__(self,
            nodes):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class GetScheduleRequest(data_model.DataObject):
    """GetScheduleRequest  
    You can use the GetSchedule method to retrieve information about a scheduled snapshot. You can see information about a specific
    schedule if there are many snapshot schedules in the system. You also retrieve information about more than one schedule with this
    method by specifying additional scheduleIDs in the parameter.

    :param schedule_id: [required] Specifies the unique ID of the schedule or multiple schedules to display. 
    :type schedule_id: int

    """
    schedule_id = data_model.property(
        "scheduleID", int,
        array=False, optional=False,
        documentation="""Specifies the unique ID of the schedule or multiple schedules to display. """,
        dictionaryType=None
    )

    def __init__(self,
            schedule_id):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class LoginBanner(data_model.DataObject):
    """LoginBanner  

    :param banner: [required] The current text of the Terms of Use banner. This value can contain text even when the banner is disabled. 
    :type banner: str

    :param enabled: [required] The status of the Terms of Use banner. Possible values: true: The Terms of Use banner is displayed upon web interface login. false: The Terms of Use banner is not displayed upon web interface login. 
    :type enabled: bool

    """
    banner = data_model.property(
        "banner", str,
        array=False, optional=False,
        documentation="""The current text of the Terms of Use banner. This value can contain text even when the banner is disabled. """,
        dictionaryType=None
    )
    enabled = data_model.property(
        "enabled", bool,
        array=False, optional=False,
        documentation="""The status of the Terms of Use banner. Possible values: true: The Terms of Use banner is displayed upon web interface login. false: The Terms of Use banner is not displayed upon web interface login. """,
        dictionaryType=None
    )

    def __init__(self,
            banner,
            enabled):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class GetLoginBannerResult(data_model.DataObject):
    """GetLoginBannerResult  

    :param login_banner: [required] 
    :type login_banner: LoginBanner

    """
    login_banner = data_model.property(
        "loginBanner", LoginBanner,
        array=False, optional=False,
        documentation="""""",
        dictionaryType=None
    )

    def __init__(self,
            login_banner):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class AddLdapClusterAdminResult(data_model.DataObject):
    """AddLdapClusterAdminResult  

    :param cluster_admin_id:   
    :type cluster_admin_id: int

    """
    cluster_admin_id = data_model.property(
        "clusterAdminID", int,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )

    def __init__(self,
            cluster_admin_id=None):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class AddedNode(data_model.DataObject):
    """AddedNode  

    :param node_id:   
    :type node_id: int

    :param pending_node_id: [required]  
    :type pending_node_id: int

    :param active_node_key:   
    :type active_node_key: str

    :param assigned_node_id:   
    :type assigned_node_id: int

    :param async_handle:   
    :type async_handle: int

    :param cip:   
    :type cip: str

    :param mip:   
    :type mip: str

    :param platform_info:   
    :type platform_info: Platform

    :param sip:   
    :type sip: str

    :param software_version:   
    :type software_version: str

    """
    node_id = data_model.property(
        "nodeID", int,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )
    pending_node_id = data_model.property(
        "pendingNodeID", int,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    active_node_key = data_model.property(
        "activeNodeKey", str,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )
    assigned_node_id = data_model.property(
        "assignedNodeID", int,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )
    async_handle = data_model.property(
        "asyncHandle", int,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )
    cip = data_model.property(
        "cip", str,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )
    mip = data_model.property(
        "mip", str,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )
    platform_info = data_model.property(
        "platformInfo", Platform,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )
    sip = data_model.property(
        "sip", str,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )
    software_version = data_model.property(
        "softwareVersion", str,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )

    def __init__(self,
            pending_node_id,
            node_id=None,
            active_node_key=None,
            assigned_node_id=None,
            async_handle=None,
            cip=None,
            mip=None,
            platform_info=None,
            sip=None,
            software_version=None):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class AddNodesResult(data_model.DataObject):
    """AddNodesResult  

    :param auto_install:   
    :type auto_install: bool

    :param nodes: [required] An array of objects mapping the previous "pendingNodeID" to the "nodeID". 
    :type nodes: AddedNode

    """
    auto_install = data_model.property(
        "autoInstall", bool,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )
    nodes = data_model.property(
        "nodes", AddedNode,
        array=True, optional=False,
        documentation="""An array of objects mapping the previous "pendingNodeID" to the "nodeID". """,
        dictionaryType=None
    )

    def __init__(self,
            nodes,
            auto_install=None):
        kwargs = locals()
        del kwargs["self"]
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
        documentation="""The IP address or host name of the target network management station. """,
        dictionaryType=None
    )
    community = data_model.property(
        "community", str,
        array=False, optional=False,
        documentation="""SNMP community string. """,
        dictionaryType=None
    )
    port = data_model.property(
        "port", int,
        array=False, optional=False,
        documentation="""The UDP port number on the host where the trap is to be sent. Valid range is 1 - 65535. 0 (zero) is not a valid port number. Default is 162. """,
        dictionaryType=None
    )

    def __init__(self,
            host,
            community,
            port):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class AddClusterAdminResult(data_model.DataObject):
    """AddClusterAdminResult  

    :param cluster_admin_id: [required] ClusterAdminID for the newly created Cluster Admin. 
    :type cluster_admin_id: int

    """
    cluster_admin_id = data_model.property(
        "clusterAdminID", int,
        array=False, optional=False,
        documentation="""ClusterAdminID for the newly created Cluster Admin. """,
        dictionaryType=None
    )

    def __init__(self,
            cluster_admin_id):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class CompleteClusterPairingRequest(data_model.DataObject):
    """CompleteClusterPairingRequest  
    You can use the CompleteClusterPairing method with the encoded key received from the  StartClusterPairing method to complete the cluster pairing process. The CompleteClusterPairing method is the second step in the cluster pairing process. 

    :param cluster_pairing_key: [required] A string of characters that is returned from the "StartClusterPairing" API method. 
    :type cluster_pairing_key: str

    """
    cluster_pairing_key = data_model.property(
        "clusterPairingKey", str,
        array=False, optional=False,
        documentation="""A string of characters that is returned from the "StartClusterPairing" API method. """,
        dictionaryType=None
    )

    def __init__(self,
            cluster_pairing_key):
        kwargs = locals()
        del kwargs["self"]
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
        documentation=""" """,
        dictionaryType=None
    )
    dev = data_model.property(
        "dev", str,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    devpath = data_model.property(
        "devpath", str,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    drive_security_at_maximum = data_model.property(
        "driveSecurityAtMaximum", bool,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    drive_security_frozen = data_model.property(
        "driveSecurityFrozen", bool,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    drive_security_locked = data_model.property(
        "driveSecurityLocked", bool,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    logicalname = data_model.property(
        "logicalname", str,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    product = data_model.property(
        "product", str,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    scsi_compat_id = data_model.property(
        "scsiCompatID", str,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    security_feature_enabled = data_model.property(
        "securityFeatureEnabled", bool,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    security_feature_supported = data_model.property(
        "securityFeatureSupported", bool,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    serial = data_model.property(
        "serial", str,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    size = data_model.property(
        "size", int,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    uuid = data_model.property(
        "uuid", UUID,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    version = data_model.property(
        "version", str,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )

    def __init__(self,
            description,
            dev,
            devpath,
            drive_security_at_maximum,
            drive_security_frozen,
            drive_security_locked,
            logicalname,
            product,
            scsi_compat_id,
            security_feature_enabled,
            security_feature_supported,
            serial,
            size,
            uuid,
            version):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class GetDriveHardwareInfoResult(data_model.DataObject):
    """GetDriveHardwareInfoResult  

    :param drive_hardware_info: [required]  
    :type drive_hardware_info: DriveHardwareInfo

    """
    drive_hardware_info = data_model.property(
        "driveHardwareInfo", DriveHardwareInfo,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )

    def __init__(self,
            drive_hardware_info):
        kwargs = locals()
        del kwargs["self"]
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

    :param curve:  The curve is a set of key-value pairs. The keys are I/O sizes in bytes. The values represent the cost performing an IOP at a specific I/O size. The curve is calculated relative to a 4096 byte operation set at 100 IOPS. 
    :type curve: dict

    """
    min_iops = data_model.property(
        "minIOPS", int,
        array=False, optional=True,
        documentation="""Desired minimum 4KB IOPS to guarantee. The allowed IOPS will only drop below this level if all volumes have been capped at their minimum IOPS value and there is still insufficient performance capacity. """,
        dictionaryType=None
    )
    max_iops = data_model.property(
        "maxIOPS", int,
        array=False, optional=True,
        documentation="""Desired maximum 4KB IOPS allowed over an extended period of time. """,
        dictionaryType=None
    )
    burst_iops = data_model.property(
        "burstIOPS", int,
        array=False, optional=True,
        documentation="""Maximum "peak" 4KB IOPS allowed for short periods of time. Allows for bursts of I/O activity over the normal max IOPS value. """,
        dictionaryType=None
    )
    burst_time = data_model.property(
        "burstTime", int,
        array=False, optional=True,
        documentation="""The length of time burst IOPS is allowed. The value returned is represented in time units of seconds. Note: this value is calculated by the system based on IOPS set for QoS. """,
        dictionaryType=None
    )
    curve = data_model.property(
        "curve", dict,
        array=False, optional=True,
        documentation="""The curve is a set of key-value pairs. The keys are I/O sizes in bytes. The values represent the cost performing an IOP at a specific I/O size. The curve is calculated relative to a 4096 byte operation set at 100 IOPS. """,
        dictionaryType=None
    )

    def __init__(self,
            min_iops=None,
            max_iops=None,
            burst_iops=None,
            burst_time=None,
            curve=None):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class CreateQoSPolicyRequest(data_model.DataObject):
    """CreateQoSPolicyRequest  
    You can use the CreateQoSPolicy method to create a QoSPolicy object that you can later apply to a volume upon creation or modification. A QoS policy has a unique ID, a name, and QoS settings.

    :param name: [required] The name of the QoS policy; for example, gold, platinum, or silver. 
    :type name: str

    :param qos: [required] The QoS settings that this policy represents. 
    :type qos: QoS

    """
    name = data_model.property(
        "name", str,
        array=False, optional=False,
        documentation="""The name of the QoS policy; for example, gold, platinum, or silver. """,
        dictionaryType=None
    )
    qos = data_model.property(
        "qos", QoS,
        array=False, optional=False,
        documentation="""The QoS settings that this policy represents. """,
        dictionaryType=None
    )

    def __init__(self,
            name,
            qos):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class DeleteInitiatorsRequest(data_model.DataObject):
    """DeleteInitiatorsRequest  
    DeleteInitiators enables you to delete one or more initiators from the system (and from any associated volumes or volume access
    groups).
    If DeleteInitiators fails to delete one of the initiators provided in the parameter, the system returns an error and does not delete any
    initiators (no partial completion is possible).

    :param initiators: [required] An array of IDs of initiators to delete. 
    :type initiators: int

    """
    initiators = data_model.property(
        "initiators", int,
        array=True, optional=False,
        documentation="""An array of IDs of initiators to delete. """,
        dictionaryType=None
    )

    def __init__(self,
            initiators):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class SetSnmpTrapInfoRequest(data_model.DataObject):
    """SetSnmpTrapInfoRequest  
    You can use SetSnmpTrapInfo to enable and disable the generation of cluster SNMP notifications (traps) and to specify the set of network host computers that receive the notifications. The values you pass with each SetSnmpTrapInfo method call replace all values set in any previous call to SetSnmpTrapInfo.

    :param trap_recipients: [required] List of hosts that are to receive the traps generated by the Cluster Master. At least one object is required if any one of the trap types is enabled. 
    :type trap_recipients: SnmpTrapRecipient

    :param cluster_fault_traps_enabled: [required] If the value is set to true, a corresponding solidFireClusterFaultNotification is sent to the configured list of trap recipients when a cluster fault is logged. The default value is false. 
    :type cluster_fault_traps_enabled: bool

    :param cluster_fault_resolved_traps_enabled: [required] If the value is set to true, a corresponding solidFireClusterFaultResolvedNotification is sent to the configured list of trap recipients when a cluster fault is resolved. The default value is false. 
    :type cluster_fault_resolved_traps_enabled: bool

    :param cluster_event_traps_enabled: [required] If the value is set to true, a corresponding solidFireClusterEventNotification is sent to the configured list of trap recipients when a cluster event is logged. The default value is false. 
    :type cluster_event_traps_enabled: bool

    """
    trap_recipients = data_model.property(
        "trapRecipients", SnmpTrapRecipient,
        array=True, optional=False,
        documentation="""List of hosts that are to receive the traps generated by the Cluster Master. At least one object is required if any one of the trap types is enabled. """,
        dictionaryType=None
    )
    cluster_fault_traps_enabled = data_model.property(
        "clusterFaultTrapsEnabled", bool,
        array=False, optional=False,
        documentation="""If the value is set to true, a corresponding solidFireClusterFaultNotification is sent to the configured list of trap recipients when a cluster fault is logged. The default value is false. """,
        dictionaryType=None
    )
    cluster_fault_resolved_traps_enabled = data_model.property(
        "clusterFaultResolvedTrapsEnabled", bool,
        array=False, optional=False,
        documentation="""If the value is set to true, a corresponding solidFireClusterFaultResolvedNotification is sent to the configured list of trap recipients when a cluster fault is resolved. The default value is false. """,
        dictionaryType=None
    )
    cluster_event_traps_enabled = data_model.property(
        "clusterEventTrapsEnabled", bool,
        array=False, optional=False,
        documentation="""If the value is set to true, a corresponding solidFireClusterEventNotification is sent to the configured list of trap recipients when a cluster event is logged. The default value is false. """,
        dictionaryType=None
    )

    def __init__(self,
            trap_recipients,
            cluster_fault_traps_enabled,
            cluster_fault_resolved_traps_enabled,
            cluster_event_traps_enabled):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class RemoveVirtualNetworkRequest(data_model.DataObject):
    """RemoveVirtualNetworkRequest  
    RemoveVirtualNetwork enables you to remove a previously added virtual network.
    Note: This method requires either the virtualNetworkID or the virtualNetworkTag as a parameter, but not both.

    :param virtual_network_id:  Network ID that identifies the virtual network to remove. 
    :type virtual_network_id: int

    :param virtual_network_tag:  Network tag that identifies the virtual network to remove. 
    :type virtual_network_tag: int

    """
    virtual_network_id = data_model.property(
        "virtualNetworkID", int,
        array=False, optional=True,
        documentation="""Network ID that identifies the virtual network to remove. """,
        dictionaryType=None
    )
    virtual_network_tag = data_model.property(
        "virtualNetworkTag", int,
        array=False, optional=True,
        documentation="""Network tag that identifies the virtual network to remove. """,
        dictionaryType=None
    )

    def __init__(self,
            virtual_network_id=None,
            virtual_network_tag=None):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class ListVolumeStatsResult(data_model.DataObject):
    """ListVolumeStatsResult  

    :param volume_stats: [required] List of volume activity information. 
    :type volume_stats: VolumeStats

    """
    volume_stats = data_model.property(
        "volumeStats", VolumeStats,
        array=True, optional=False,
        documentation="""List of volume activity information. """,
        dictionaryType=None
    )

    def __init__(self,
            volume_stats):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class SetClusterConfigResult(data_model.DataObject):
    """SetClusterConfigResult  

    :param cluster: [required] Settings for the cluster. All new and current settings are returned. 
    :type cluster: ClusterConfig

    """
    cluster = data_model.property(
        "cluster", ClusterConfig,
        array=False, optional=False,
        documentation="""Settings for the cluster. All new and current settings are returned. """,
        dictionaryType=None
    )

    def __init__(self,
            cluster):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class CancelGroupCloneRequest(data_model.DataObject):
    """CancelGroupCloneRequest  
    CancelGroupClone enables you to stop an ongoing CloneMultipleVolumes process occurring on a group of volumes. When you cancel
    a group clone operation, the system completes and removes the operation's associated asyncHandle.

    :param group_clone_id: [required] The cloneID for the ongoing clone process. 
    :type group_clone_id: int

    """
    group_clone_id = data_model.property(
        "groupCloneID", int,
        array=False, optional=False,
        documentation="""The cloneID for the ongoing clone process. """,
        dictionaryType=None
    )

    def __init__(self,
            group_clone_id):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class ListActiveVolumesRequest(data_model.DataObject):
    """ListActiveVolumesRequest  
    ListActiveVolumes enables you to return the list of active volumes currently in the system. The list of volumes is returned sorted in
    VolumeID order and can be returned in multiple parts (pages).

    :param start_volume_id:  Starting VolumeID to return. If no volume exists with this VolumeID, the next volume by VolumeID order is used as the start of the list. To page through the list, pass the VolumeID of the last volume in the previous response + 1. 
    :type start_volume_id: int

    :param limit:  Maximum number of Volume Info objects to return. A value of 0 (zero) returns all volumes (unlimited). 
    :type limit: int

    :param include_virtual_volumes:  Specifies that virtual volumes are included in the response by default. To exclude virtual volumes, set to false. 
    :type include_virtual_volumes: bool

    """
    start_volume_id = data_model.property(
        "startVolumeID", int,
        array=False, optional=True,
        documentation="""Starting VolumeID to return. If no volume exists with this VolumeID, the next volume by VolumeID order is used as the start of the list. To page through the list, pass the VolumeID of the last volume in the previous response + 1. """,
        dictionaryType=None
    )
    limit = data_model.property(
        "limit", int,
        array=False, optional=True,
        documentation="""Maximum number of Volume Info objects to return. A value of 0 (zero) returns all volumes (unlimited). """,
        dictionaryType=None
    )
    include_virtual_volumes = data_model.property(
        "includeVirtualVolumes", bool,
        array=False, optional=True,
        documentation="""Specifies that virtual volumes are included in the response by default. To exclude virtual volumes, set to false. """,
        dictionaryType=None
    )

    def __init__(self,
            start_volume_id=None,
            limit=None,
            include_virtual_volumes=None):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class CreateScheduleRequest(data_model.DataObject):
    """CreateScheduleRequest  
    CreateSchedule enables you to schedule an automatic snapshot of a volume at a defined interval.
    You can use the created snapshot later as a backup or rollback to ensure the data on a volume or group of volumes is consistent for
    the point in time in which the snapshot was created.
    If you schedule a snapshot to run at a time period that is not divisible by 5 minutes, the snapshot runs at the next time period
    that is divisible by 5 minutes. For example, if you schedule a snapshot to run at 12:42:00 UTC, it runs at 12:45:00 UTC.
    Note: You can create snapshots if cluster fullness is at stage 1, 2 or 3. You cannot create snapshots after cluster fullness reaches stage 4 or 5.

    :param schedule: [required] The "Schedule" object will be used to create a new schedule. Do not set ScheduleID property, it will be ignored. Frequency property must be of type that inherits from Frequency. Valid types are: DaysOfMonthFrequency DaysOrWeekFrequency TimeIntervalFrequency 
    :type schedule: Schedule

    """
    schedule = data_model.property(
        "schedule", Schedule,
        array=False, optional=False,
        documentation="""The "Schedule" object will be used to create a new schedule. Do not set ScheduleID property, it will be ignored. Frequency property must be of type that inherits from Frequency. Valid types are: DaysOfMonthFrequency DaysOrWeekFrequency TimeIntervalFrequency """,
        dictionaryType=None
    )

    def __init__(self,
            schedule):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class DeleteAllSupportBundlesResult(data_model.DataObject):
    """DeleteAllSupportBundlesResult  

    :param duration: [required]  
    :type duration: str

    :param details: [required]  
    :type details: dict

    :param result: [required]  
    :type result: str

    """
    duration = data_model.property(
        "duration", str,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    details = data_model.property(
        "details", dict,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    result = data_model.property(
        "result", str,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )

    def __init__(self,
            duration,
            details,
            result):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class GetDriveHardwareInfoRequest(data_model.DataObject):
    """GetDriveHardwareInfoRequest  
    GetDriveHardwareInfo returns all the hardware information for the given drive. This generally includes details about manufacturers, vendors, versions, and
    other associated hardware identification information.

    :param drive_id: [required] DriveID for the drive information requested. You can get DriveIDs by using the ListDrives method. 
    :type drive_id: int

    """
    drive_id = data_model.property(
        "driveID", int,
        array=False, optional=False,
        documentation="""DriveID for the drive information requested. You can get DriveIDs by using the ListDrives method. """,
        dictionaryType=None
    )

    def __init__(self,
            drive_id):
        kwargs = locals()
        del kwargs["self"]
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

    :param virtual_volumes:   
    :type virtual_volumes: UUID

    """
    name = data_model.property(
        "name", str,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    storage_container_id = data_model.property(
        "storageContainerID", UUID,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    account_id = data_model.property(
        "accountID", int,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    protocol_endpoint_type = data_model.property(
        "protocolEndpointType", str,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    initiator_secret = data_model.property(
        "initiatorSecret", str,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    target_secret = data_model.property(
        "targetSecret", str,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    status = data_model.property(
        "status", str,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    virtual_volumes = data_model.property(
        "virtualVolumes", UUID,
        array=True, optional=True,
        documentation=""" """,
        dictionaryType=None
    )

    def __init__(self,
            name,
            storage_container_id,
            account_id,
            protocol_endpoint_type,
            initiator_secret,
            target_secret,
            status,
            virtual_volumes=None):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class ModifyStorageContainerResult(data_model.DataObject):
    """ModifyStorageContainerResult  

    :param storage_container: [required]  
    :type storage_container: StorageContainer

    """
    storage_container = data_model.property(
        "storageContainer", StorageContainer,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )

    def __init__(self,
            storage_container):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class InvokeSFApiRequest(data_model.DataObject):
    """InvokeSFApiRequest  
    This will invoke any API method supported by the SolidFire API for the version and port the connection is using.
    Returns a nested hashtable of key/value pairs that contain the result of the invoked method.

    :param method: [required] The name of the method to invoke. This is case sensitive. 
    :type method: str

    :param parameters:  An object, normally a dictionary or hashtable of the key/value pairs, to be passed as the params for the method being invoked. 
    :type parameters: str

    """
    method = data_model.property(
        "method", str,
        array=False, optional=False,
        documentation="""The name of the method to invoke. This is case sensitive. """,
        dictionaryType=None
    )
    parameters = data_model.property(
        "parameters", str,
        array=False, optional=True,
        documentation="""An object, normally a dictionary or hashtable of the key/value pairs, to be passed as the params for the method being invoked. """,
        dictionaryType=None
    )

    def __init__(self,
            method,
            parameters=None):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class RemoveNodesResult(data_model.DataObject):
    """RemoveNodesResult  

    """

    def __init__(self):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class RemoveAccountResult(data_model.DataObject):
    """RemoveAccountResult  

    """

    def __init__(self):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class GetVolumeCountResult(data_model.DataObject):
    """GetVolumeCountResult  

    :param count: [required] The number of volumes currently in the system. 
    :type count: int

    """
    count = data_model.property(
        "count", int,
        array=False, optional=False,
        documentation="""The number of volumes currently in the system. """,
        dictionaryType=None
    )

    def __init__(self,
            count):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class GetStorageContainerEfficiencyRequest(data_model.DataObject):
    """GetStorageContainerEfficiencyRequest  
    GetStorageContainerEfficiency enables you to retrieve efficiency information about a virtual volume storage container.

    :param storage_container_id: [required] The ID of the storage container for which to retrieve efficiency information. 
    :type storage_container_id: UUID

    """
    storage_container_id = data_model.property(
        "storageContainerID", UUID,
        array=False, optional=False,
        documentation="""The ID of the storage container for which to retrieve efficiency information. """,
        dictionaryType=None
    )

    def __init__(self,
            storage_container_id):
        kwargs = locals()
        del kwargs["self"]
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

    :param volume_access_groups: [required] A list of volumeAccessGroupIDs to which this initiator beintegers. (Array of Integers) 
    :type volume_access_groups: int

    :param attributes: [required] A set of JSON attributes assigned to this initiator. (JSON Object) 
    :type attributes: dict

    """
    alias = data_model.property(
        "alias", str,
        array=False, optional=False,
        documentation="""The friendly name assigned to this initiator. (String) """,
        dictionaryType=None
    )
    initiator_id = data_model.property(
        "initiatorID", int,
        array=False, optional=False,
        documentation="""The numeric ID of the initiator that has been created. (Integer) """,
        dictionaryType=None
    )
    initiator_name = data_model.property(
        "initiatorName", str,
        array=False, optional=False,
        documentation="""The name of the initiator that has been created. (String) """,
        dictionaryType=None
    )
    volume_access_groups = data_model.property(
        "volumeAccessGroups", int,
        array=True, optional=False,
        documentation="""A list of volumeAccessGroupIDs to which this initiator beintegers. (Array of Integers) """,
        dictionaryType=None
    )
    attributes = data_model.property(
        "attributes", dict,
        array=False, optional=False,
        documentation="""A set of JSON attributes assigned to this initiator. (JSON Object) """,
        dictionaryType=None
    )

    def __init__(self,
            alias,
            initiator_id,
            initiator_name,
            volume_access_groups,
            attributes):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class ISCSISession(data_model.DataObject):
    """ISCSISession  

    :param drive_ids:   
    :type drive_ids: int

    :param account_id: [required]  
    :type account_id: int

    :param initiator:   
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

    :param ms_since_last_scsi_command:   
    :type ms_since_last_scsi_command: int

    :param ms_since_last_iscsi_pdu:   
    :type ms_since_last_iscsi_pdu: int

    """
    drive_ids = data_model.property(
        "driveIDs", int,
        array=True, optional=True,
        documentation=""" """,
        dictionaryType=None
    )
    account_id = data_model.property(
        "accountID", int,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    initiator = data_model.property(
        "initiator", Initiator,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )
    account_name = data_model.property(
        "accountName", str,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    drive_id = data_model.property(
        "driveID", int,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    initiator_ip = data_model.property(
        "initiatorIP", str,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    initiator_port_name = data_model.property(
        "initiatorPortName", str,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    target_port_name = data_model.property(
        "targetPortName", str,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    initiator_name = data_model.property(
        "initiatorName", str,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    node_id = data_model.property(
        "nodeID", int,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    service_id = data_model.property(
        "serviceID", int,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    session_id = data_model.property(
        "sessionID", int,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    target_name = data_model.property(
        "targetName", str,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    target_ip = data_model.property(
        "targetIP", str,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    virtual_network_id = data_model.property(
        "virtualNetworkID", int,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    volume_id = data_model.property(
        "volumeID", int,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    create_time = data_model.property(
        "createTime", str,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    volume_instance = data_model.property(
        "volumeInstance", int,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    initiator_session_id = data_model.property(
        "initiatorSessionID", int,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    ms_since_last_scsi_command = data_model.property(
        "msSinceLastScsiCommand", int,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )
    ms_since_last_iscsi_pdu = data_model.property(
        "msSinceLastIscsiPDU", int,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )

    def __init__(self,
            account_id,
            account_name,
            drive_id,
            initiator_ip,
            initiator_port_name,
            target_port_name,
            initiator_name,
            node_id,
            service_id,
            session_id,
            target_name,
            target_ip,
            virtual_network_id,
            volume_id,
            create_time,
            volume_instance,
            initiator_session_id,
            drive_ids=None,
            initiator=None,
            ms_since_last_scsi_command=None,
            ms_since_last_iscsi_pdu=None):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class ListISCSISessionsResult(data_model.DataObject):
    """ListISCSISessionsResult  

    :param sessions: [required]  
    :type sessions: ISCSISession

    """
    sessions = data_model.property(
        "sessions", ISCSISession,
        array=True, optional=False,
        documentation=""" """,
        dictionaryType=None
    )

    def __init__(self,
            sessions):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class ListVirtualVolumesRequest(data_model.DataObject):
    """ListVirtualVolumesRequest  
    ListVirtualVolumes enables you to list the virtual volumes currently in the system. You can use this method to list all virtual volumes,
    or only list a subset.

    :param details:  Specifies the level of detail about each virtual volume that is returned. Possible values are: true: Include more details about each virtual volume in the response. false: Include the standard level of detail about each virtual volume in the response. 
    :type details: bool

    :param limit:  The maximum number of virtual volumes to list. 
    :type limit: int

    :param recursive:  Specifies whether to include information about the children of each virtual volume in the response. Possible values are: true: Include information about the children of each virtual volume in the response. false: Do not include information about the children of each virtual volume in the response. 
    :type recursive: bool

    :param start_virtual_volume_id:  The ID of the virtual volume at which to begin the list. 
    :type start_virtual_volume_id: UUID

    :param virtual_volume_ids:  A list of virtual volume IDs for which to retrieve information. If you specify this parameter, the method returns information about only these virtual volumes. 
    :type virtual_volume_ids: UUID

    """
    details = data_model.property(
        "details", bool,
        array=False, optional=True,
        documentation="""Specifies the level of detail about each virtual volume that is returned. Possible values are: true: Include more details about each virtual volume in the response. false: Include the standard level of detail about each virtual volume in the response. """,
        dictionaryType=None
    )
    limit = data_model.property(
        "limit", int,
        array=False, optional=True,
        documentation="""The maximum number of virtual volumes to list. """,
        dictionaryType=None
    )
    recursive = data_model.property(
        "recursive", bool,
        array=False, optional=True,
        documentation="""Specifies whether to include information about the children of each virtual volume in the response. Possible values are: true: Include information about the children of each virtual volume in the response. false: Do not include information about the children of each virtual volume in the response. """,
        dictionaryType=None
    )
    start_virtual_volume_id = data_model.property(
        "startVirtualVolumeID", UUID,
        array=False, optional=True,
        documentation="""The ID of the virtual volume at which to begin the list. """,
        dictionaryType=None
    )
    virtual_volume_ids = data_model.property(
        "virtualVolumeIDs", UUID,
        array=True, optional=True,
        documentation="""A list of virtual volume IDs for which to retrieve information. If you specify this parameter, the method returns information about only these virtual volumes. """,
        dictionaryType=None
    )

    def __init__(self,
            details=None,
            limit=None,
            recursive=None,
            start_virtual_volume_id=None,
            virtual_volume_ids=None):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class CompleteVolumePairingResult(data_model.DataObject):
    """CompleteVolumePairingResult  

    """

    def __init__(self):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class ListDeletedVolumesRequest(data_model.DataObject):
    """ListDeletedVolumesRequest  
    ListDeletedVolumes enables you to retrieve the list of volumes that have been marked for deletion and purged from the system.

    :param include_virtual_volumes:  Specifies that virtual volumes are included in the response by default. To exclude virtual volumes, set to false. 
    :type include_virtual_volumes: bool

    """
    include_virtual_volumes = data_model.property(
        "includeVirtualVolumes", bool,
        array=False, optional=True,
        documentation="""Specifies that virtual volumes are included in the response by default. To exclude virtual volumes, set to false. """,
        dictionaryType=None
    )

    def __init__(self,
            include_virtual_volumes=None):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class ListStorageContainersResult(data_model.DataObject):
    """ListStorageContainersResult  

    :param storage_containers: [required]  
    :type storage_containers: StorageContainer

    """
    storage_containers = data_model.property(
        "storageContainers", StorageContainer,
        array=True, optional=False,
        documentation=""" """,
        dictionaryType=None
    )

    def __init__(self,
            storage_containers):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class GetLdapConfigurationResult(data_model.DataObject):
    """GetLdapConfigurationResult  

    :param ldap_configuration: [required] List of the current LDAP configuration settings. This API call will not return the plain text of the search account password.  Note: If LDAP authentication is currently disabled, all the returned settings will be empty with the exception of "authType", and "groupSearchType" which are set to "SearchAndBind" and "ActiveDirectory" respectively. 
    :type ldap_configuration: LdapConfiguration

    """
    ldap_configuration = data_model.property(
        "ldapConfiguration", LdapConfiguration,
        array=False, optional=False,
        documentation="""List of the current LDAP configuration settings. This API call will not return the plain text of the search account password.  Note: If LDAP authentication is currently disabled, all the returned settings will be empty with the exception of "authType", and "groupSearchType" which are set to "SearchAndBind" and "ActiveDirectory" respectively. """,
        dictionaryType=None
    )

    def __init__(self,
            ldap_configuration):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class GroupSnapshotMembers(data_model.DataObject):
    """GroupSnapshotMembers  
    List of checksum, volumeIDs and snapshotIDs for each member of the group.

    :param volume_id: [required] The source volume ID for the snapshot. 
    :type volume_id: int

    :param snapshot_id: [required] Unique ID of a snapshot from which the new snapshot is made. The snapshotID passed must be a snapshot on the given volume. 
    :type snapshot_id: int

    :param snapshot_uuid: [required] Universal Unique ID of an existing snapshot. 
    :type snapshot_uuid: UUID

    :param checksum: [required] A string that represents the correct digits in the stored snapshot. This checksum can be used later to compare other snapshots to detect errors in the data. 
    :type checksum: str

    :param attributes:   
    :type attributes: dict

    :param create_time:   
    :type create_time: str

    :param enable_remote_replication:   
    :type enable_remote_replication: bool

    :param expiration_reason:   
    :type expiration_reason: str

    :param expiration_time:   
    :type expiration_time: str

    :param group_id:   
    :type group_id: int

    :param group_snapshot_uuid:   
    :type group_snapshot_uuid: UUID

    :param name:   
    :type name: str

    :param remote_status:   
    :type remote_status: str

    :param remote_statuses:   
    :type remote_statuses: dict

    :param status:   
    :type status: str

    :param total_size:   
    :type total_size: int

    :param virtual_volume_id:   
    :type virtual_volume_id: int

    :param volume_pair_uuid:   
    :type volume_pair_uuid: UUID

    """
    volume_id = data_model.property(
        "volumeID", int,
        array=False, optional=False,
        documentation="""The source volume ID for the snapshot. """,
        dictionaryType=None
    )
    snapshot_id = data_model.property(
        "snapshotID", int,
        array=False, optional=False,
        documentation="""Unique ID of a snapshot from which the new snapshot is made. The snapshotID passed must be a snapshot on the given volume. """,
        dictionaryType=None
    )
    snapshot_uuid = data_model.property(
        "snapshotUUID", UUID,
        array=False, optional=False,
        documentation="""Universal Unique ID of an existing snapshot. """,
        dictionaryType=None
    )
    checksum = data_model.property(
        "checksum", str,
        array=False, optional=False,
        documentation="""A string that represents the correct digits in the stored snapshot. This checksum can be used later to compare other snapshots to detect errors in the data. """,
        dictionaryType=None
    )
    attributes = data_model.property(
        "attributes", dict,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )
    create_time = data_model.property(
        "createTime", str,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )
    enable_remote_replication = data_model.property(
        "enableRemoteReplication", bool,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )
    expiration_reason = data_model.property(
        "expirationReason", str,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )
    expiration_time = data_model.property(
        "expirationTime", str,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )
    group_id = data_model.property(
        "groupID", int,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )
    group_snapshot_uuid = data_model.property(
        "groupSnapshotUUID", UUID,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )
    name = data_model.property(
        "name", str,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )
    remote_status = data_model.property(
        "remoteStatus", str,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )
    remote_statuses = data_model.property(
        "remoteStatuses", dict,
        array=True, optional=True,
        documentation=""" """,
        dictionaryType=None
    )
    status = data_model.property(
        "status", str,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )
    total_size = data_model.property(
        "totalSize", int,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )
    virtual_volume_id = data_model.property(
        "virtualVolumeID", int,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )
    volume_pair_uuid = data_model.property(
        "volumePairUUID", UUID,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )

    def __init__(self,
            volume_id,
            snapshot_id,
            snapshot_uuid,
            checksum,
            attributes=None,
            create_time=None,
            enable_remote_replication=None,
            expiration_reason=None,
            expiration_time=None,
            group_id=None,
            group_snapshot_uuid=None,
            name=None,
            remote_status=None,
            remote_statuses=None,
            status=None,
            total_size=None,
            virtual_volume_id=None,
            volume_pair_uuid=None):
        kwargs = locals()
        del kwargs["self"]
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
        documentation="""Unique ID of the new group snapshot. """,
        dictionaryType=None
    )
    group_snapshot_uuid = data_model.property(
        "groupSnapshotUUID", UUID,
        array=False, optional=False,
        documentation="""UUID of the group snapshot. """,
        dictionaryType=None
    )
    members = data_model.property(
        "members", GroupSnapshotMembers,
        array=True, optional=False,
        documentation="""List of volumeIDs and snapshotIDs for each member of the group. """,
        dictionaryType=None
    )
    name = data_model.property(
        "name", str,
        array=False, optional=False,
        documentation="""Name of the group snapshot, or, if none was given, the UTC formatted day and time on which the snapshot was created. """,
        dictionaryType=None
    )
    create_time = data_model.property(
        "createTime", str,
        array=False, optional=False,
        documentation="""The UTC formatted day and time on which the snapshot was created. """,
        dictionaryType=None
    )
    status = data_model.property(
        "status", str,
        array=False, optional=False,
        documentation="""Status of the snapshot. Possible values: Preparing: A snapshot that is being prepared for use and is not yet writable. Done: A snapshot that has finished being prepared and is now usable """,
        dictionaryType=None
    )
    attributes = data_model.property(
        "attributes", dict,
        array=False, optional=False,
        documentation="""List of Name/Value pairs in JSON object format. """,
        dictionaryType=None
    )

    def __init__(self,
            group_snapshot_id,
            group_snapshot_uuid,
            members,
            name,
            create_time,
            status,
            attributes):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class ModifyGroupSnapshotResult(data_model.DataObject):
    """ModifyGroupSnapshotResult  

    :param group_snapshot: [required]  
    :type group_snapshot: GroupSnapshot

    """
    group_snapshot = data_model.property(
        "groupSnapshot", GroupSnapshot,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )

    def __init__(self,
            group_snapshot):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class ListDriveStatsRequest(data_model.DataObject):
    """ListDriveStatsRequest  
    ListDriveStats enables you to retrieve high-level activity measurements for multiple drives in the cluster. By default, this method returns statistics for all drives in the cluster, and these measurements are cumulative from the addition of the drive to the cluster. Some values this method returns are specific to block drives, and some are specific to metadata drives.

    :param drives:  Optional list of DriveIDs for which to return drive statistics. If you omit this parameter, measurements for all drives are returned. 
    :type drives: int

    """
    drives = data_model.property(
        "drives", int,
        array=True, optional=True,
        documentation="""Optional list of DriveIDs for which to return drive statistics. If you omit this parameter, measurements for all drives are returned. """,
        dictionaryType=None
    )

    def __init__(self,
            drives=None):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class ListInitiatorsRequest(data_model.DataObject):
    """ListInitiatorsRequest  
    ListInitiators enables you to list initiator IQNs or World Wide Port Names (WWPNs).

    :param start_initiator_id:  The initiator ID at which to begin the listing. You can supply this parameter or the "initiators" parameter, but not both. 
    :type start_initiator_id: int

    :param limit:  The maximum number of initiator objects to return. 
    :type limit: int

    :param initiators:  A list of initiator IDs to retrieve. You can provide a value for this parameter or the "startInitiatorID" parameter, but not both. 
    :type initiators: int

    """
    start_initiator_id = data_model.property(
        "startInitiatorID", int,
        array=False, optional=True,
        documentation="""The initiator ID at which to begin the listing. You can supply this parameter or the "initiators" parameter, but not both. """,
        dictionaryType=None
    )
    limit = data_model.property(
        "limit", int,
        array=False, optional=True,
        documentation="""The maximum number of initiator objects to return. """,
        dictionaryType=None
    )
    initiators = data_model.property(
        "initiators", int,
        array=True, optional=True,
        documentation="""A list of initiator IDs to retrieve. You can provide a value for this parameter or the "startInitiatorID" parameter, but not both. """,
        dictionaryType=None
    )

    def __init__(self,
            start_initiator_id=None,
            limit=None,
            initiators=None):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class ListInitiatorsResult(data_model.DataObject):
    """ListInitiatorsResult  

    :param initiators: [required] List of the initiator information. 
    :type initiators: Initiator

    """
    initiators = data_model.property(
        "initiators", Initiator,
        array=True, optional=False,
        documentation="""List of the initiator information. """,
        dictionaryType=None
    )

    def __init__(self,
            initiators):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class AddressBlock(data_model.DataObject):
    """AddressBlock  
    Unique Range of IP addresses to include in the virtual network.

    :param start: [required] Start of the IP address range. 
    :type start: str

    :param size: [required] Number of IP addresses to include in the block. 
    :type size: int

    :param available: [required] Nuber of available blocks 
    :type available: str

    """
    start = data_model.property(
        "start", str,
        array=False, optional=False,
        documentation="""Start of the IP address range. """,
        dictionaryType=None
    )
    size = data_model.property(
        "size", int,
        array=False, optional=False,
        documentation="""Number of IP addresses to include in the block. """,
        dictionaryType=None
    )
    available = data_model.property(
        "available", str,
        array=False, optional=False,
        documentation="""Nuber of available blocks """,
        dictionaryType=None
    )

    def __init__(self,
            start,
            size,
            available):
        kwargs = locals()
        del kwargs["self"]
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

    :param attributes:  List of Name/Value pairs in JSON object format. 
    :type attributes: dict

    """
    virtual_network_id = data_model.property(
        "virtualNetworkID", int,
        array=False, optional=False,
        documentation="""SolidFire unique identifier for a virtual network. """,
        dictionaryType=None
    )
    virtual_network_tag = data_model.property(
        "virtualNetworkTag", int,
        array=False, optional=False,
        documentation="""VLAN Tag identifier. """,
        dictionaryType=None
    )
    address_blocks = data_model.property(
        "addressBlocks", AddressBlock,
        array=True, optional=False,
        documentation="""Range of address blocks currently assigned to the virtual network. available: Binary string in "1"s and "0"s. 1 equals the IP is available and 0 equals the IP is not available. The string is read from right to left with the digit to the far right being the first IP address in the list of addressBlocks. size: the size of this block of addresses. start: first IP address in the block. """,
        dictionaryType=None
    )
    name = data_model.property(
        "name", str,
        array=False, optional=False,
        documentation="""The name assigned to the virtual network. """,
        dictionaryType=None
    )
    netmask = data_model.property(
        "netmask", str,
        array=False, optional=False,
        documentation="""IP address of the netmask for the virtual network. """,
        dictionaryType=None
    )
    svip = data_model.property(
        "svip", str,
        array=False, optional=False,
        documentation="""Storage IP address for the virtual network. """,
        dictionaryType=None
    )
    gateway = data_model.property(
        "gateway", str,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )
    namespace = data_model.property(
        "namespace", bool,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )
    attributes = data_model.property(
        "attributes", dict,
        array=False, optional=True,
        documentation="""List of Name/Value pairs in JSON object format. """,
        dictionaryType=None
    )

    def __init__(self,
            virtual_network_id,
            virtual_network_tag,
            address_blocks,
            name,
            netmask,
            svip,
            gateway=None,
            namespace=None,
            attributes=None):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class ListVirtualNetworksResult(data_model.DataObject):
    """ListVirtualNetworksResult  

    :param virtual_networks: [required] Object containing virtual network IP addresses. 
    :type virtual_networks: VirtualNetwork

    """
    virtual_networks = data_model.property(
        "virtualNetworks", VirtualNetwork,
        array=True, optional=False,
        documentation="""Object containing virtual network IP addresses. """,
        dictionaryType=None
    )

    def __init__(self,
            virtual_networks):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class ListQoSPoliciesResult(data_model.DataObject):
    """ListQoSPoliciesResult  

    :param qos_policies: [required] A list of details about each QoS policy. 
    :type qos_policies: QoSPolicy

    """
    qos_policies = data_model.property(
        "qosPolicies", QoSPolicy,
        array=True, optional=False,
        documentation="""A list of details about each QoS policy. """,
        dictionaryType=None
    )

    def __init__(self,
            qos_policies):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class StartVolumePairingRequest(data_model.DataObject):
    """StartVolumePairingRequest  
    StartVolumePairing enables you to create an encoded key from a volume that is used to pair with another volume. The key that this
    method creates is used in the CompleteVolumePairing API method to establish a volume pairing.

    :param volume_id: [required] The ID of the volume on which to start the pairing process. 
    :type volume_id: int

    :param mode:  The mode of the volume on which to start the pairing process. The mode can only be set if the volume is the source volume. Possible values are: Async: (default if no mode parameter specified) Writes are acknowledged when they complete locally. The cluster does not wait for writes to be replicated to the target cluster. Sync: Source acknowledges write when the data is stored locally and on the remote cluster. SnapshotsOnly: Only snapshots created on the source cluster will be replicated. Active writes from the source volume are not replicated. 
    :type mode: str

    """
    volume_id = data_model.property(
        "volumeID", int,
        array=False, optional=False,
        documentation="""The ID of the volume on which to start the pairing process. """,
        dictionaryType=None
    )
    mode = data_model.property(
        "mode", str,
        array=False, optional=True,
        documentation="""The mode of the volume on which to start the pairing process. The mode can only be set if the volume is the source volume. Possible values are: Async: (default if no mode parameter specified) Writes are acknowledged when they complete locally. The cluster does not wait for writes to be replicated to the target cluster. Sync: Source acknowledges write when the data is stored locally and on the remote cluster. SnapshotsOnly: Only snapshots created on the source cluster will be replicated. Active writes from the source volume are not replicated. """,
        dictionaryType=None
    )

    def __init__(self,
            volume_id,
            mode=None):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class DisableSnmpResult(data_model.DataObject):
    """DisableSnmpResult  

    """

    def __init__(self):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class SetNetworkConfigResult(data_model.DataObject):
    """SetNetworkConfigResult  

    :param network: [required]  
    :type network: Network

    """
    network = data_model.property(
        "network", Network,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )

    def __init__(self,
            network):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class AddressBlockParams(data_model.DataObject):
    """AddressBlockParams  
    Unique Range of IP addresses to include in the virtual network.

    :param start: [required] Start of the IP address range. 
    :type start: str

    :param size: [required] Number of IP addresses to include in the block. 
    :type size: int

    """
    start = data_model.property(
        "start", str,
        array=False, optional=False,
        documentation="""Start of the IP address range. """,
        dictionaryType=None
    )
    size = data_model.property(
        "size", int,
        array=False, optional=False,
        documentation="""Number of IP addresses to include in the block. """,
        dictionaryType=None
    )

    def __init__(self,
            start,
            size):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class AddVirtualNetworkRequest(data_model.DataObject):
    """AddVirtualNetworkRequest  
    You can use the AddVirtualNetwork method to add a new virtual network to a cluster configuration. When you add a virtual network,
    an interface for each node is created and each interface will require a virtual network IP address. The number of IP addresses you
    specify as a parameter for this API method must be equal to or greater than the number of nodes in the cluster. The system bulk
    provisions virtual network addresses and assigns them to individual nodes automatically. You do not need to assign virtual
    network addresses to nodes manually.
    Note: You can use AddVirtualNetwork only to create a new virtual network. If you want to make changes to an
    existing virtual network, use ModifyVirtualNetwork.
    Note: Virtual network parameters must be unique to each virtual network when setting the namespace parameter to false.

    :param virtual_network_tag: [required] A unique virtual network (VLAN) tag. Supported values are 1 through 4094.The number zero (0) is not supported. 
    :type virtual_network_tag: int

    :param name: [required] A user-defined name for the new virtual network. 
    :type name: str

    :param address_blocks: [required] Unique range of IP addresses to include in the virtual network. Attributes for this parameter are: start: The start of the IP address range. (String) size: The number of IP addresses to include in the block. (Integer) 
    :type address_blocks: AddressBlockParams

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
    virtual_network_tag = data_model.property(
        "virtualNetworkTag", int,
        array=False, optional=False,
        documentation="""A unique virtual network (VLAN) tag. Supported values are 1 through 4094.The number zero (0) is not supported. """,
        dictionaryType=None
    )
    name = data_model.property(
        "name", str,
        array=False, optional=False,
        documentation="""A user-defined name for the new virtual network. """,
        dictionaryType=None
    )
    address_blocks = data_model.property(
        "addressBlocks", AddressBlockParams,
        array=True, optional=False,
        documentation="""Unique range of IP addresses to include in the virtual network. Attributes for this parameter are: start: The start of the IP address range. (String) size: The number of IP addresses to include in the block. (Integer) """,
        dictionaryType=None
    )
    netmask = data_model.property(
        "netmask", str,
        array=False, optional=False,
        documentation="""Unique network mask for the virtual network being created. """,
        dictionaryType=None
    )
    svip = data_model.property(
        "svip", str,
        array=False, optional=False,
        documentation="""Unique storage IP address for the virtual network being created. """,
        dictionaryType=None
    )
    gateway = data_model.property(
        "gateway", str,
        array=False, optional=True,
        documentation="""The IP address of a gateway of the virtual network. This parameter is only valid if the "namespace" parameter is set to true. """,
        dictionaryType=None
    )
    namespace = data_model.property(
        "namespace", bool,
        array=False, optional=True,
        documentation="""When set to true, enables the Routable Storage VLANs functionality by creating and configuring a namespace and the virtual network contained by it. """,
        dictionaryType=None
    )
    attributes = data_model.property(
        "attributes", dict,
        array=False, optional=True,
        documentation="""List of name-value pairs in JSON object format. """,
        dictionaryType=None
    )

    def __init__(self,
            virtual_network_tag,
            name,
            address_blocks,
            netmask,
            svip,
            gateway=None,
            namespace=None,
            attributes=None):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class ListClusterFaultsRequest(data_model.DataObject):
    """ListClusterFaultsRequest  
    ListClusterFaults enables you to retrieve information about any faults detected on the cluster. With this method, you can retrieve both current faults as well as faults that have been resolved. The system caches faults every 30 seconds.

    :param best_practices:  Specifies whether to include faults triggered by suboptimal system configuration. Possible values are: true false 
    :type best_practices: bool

    :param fault_types:  Determines the types of faults returned. Possible values are: current: List active, unresolved faults. resolved: List faults that were previously detected and resolved. all: (Default) List both current and resolved faults. You can see the fault status in the resolved field of the Cluster Fault object. 
    :type fault_types: str

    """
    best_practices = data_model.property(
        "bestPractices", bool,
        array=False, optional=True,
        documentation="""Specifies whether to include faults triggered by suboptimal system configuration. Possible values are: true false """,
        dictionaryType=None
    )
    fault_types = data_model.property(
        "faultTypes", str,
        array=False, optional=True,
        documentation="""Determines the types of faults returned. Possible values are: current: List active, unresolved faults. resolved: List faults that were previously detected and resolved. all: (Default) List both current and resolved faults. You can see the fault status in the resolved field of the Cluster Fault object. """,
        dictionaryType=None
    )

    def __init__(self,
            best_practices=None,
            fault_types=None):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class TestPingResult(data_model.DataObject):
    """TestPingResult  

    :param result: [required] Result of the ping test. 
    :type result: str

    :param duration: [required] The total duration of the ping test. 
    :type duration: str

    :param details: [required] List of each IP the node was able to communicate with. 
    :type details: dict

    """
    result = data_model.property(
        "result", str,
        array=False, optional=False,
        documentation="""Result of the ping test. """,
        dictionaryType=None
    )
    duration = data_model.property(
        "duration", str,
        array=False, optional=False,
        documentation="""The total duration of the ping test. """,
        dictionaryType=None
    )
    details = data_model.property(
        "details", dict,
        array=False, optional=False,
        documentation="""List of each IP the node was able to communicate with. """,
        dictionaryType=None
    )

    def __init__(self,
            result,
            duration,
            details):
        kwargs = locals()
        del kwargs["self"]
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
        documentation="""Name for the backup target. """,
        dictionaryType=None
    )
    backup_target_id = data_model.property(
        "backupTargetID", int,
        array=False, optional=False,
        documentation="""Unique identifier assigned to the backup target. """,
        dictionaryType=None
    )
    attributes = data_model.property(
        "attributes", dict,
        array=False, optional=True,
        documentation="""List of Name/Value pairs in JSON object format. """,
        dictionaryType=None
    )

    def __init__(self,
            name,
            backup_target_id,
            attributes=None):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class GetBackupTargetResult(data_model.DataObject):
    """GetBackupTargetResult  

    :param backup_target: [required] Object returned for backup target. 
    :type backup_target: BackupTarget

    """
    backup_target = data_model.property(
        "backupTarget", BackupTarget,
        array=False, optional=False,
        documentation="""Object returned for backup target. """,
        dictionaryType=None
    )

    def __init__(self,
            backup_target):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class AddDrivesResult(data_model.DataObject):
    """AddDrivesResult  

    :param async_handle:   
    :type async_handle: int

    """
    async_handle = data_model.property(
        "asyncHandle", int,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )

    def __init__(self,
            async_handle=None):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class ListVolumeStatsByVirtualVolumeRequest(data_model.DataObject):
    """ListVolumeStatsByVirtualVolumeRequest  
    ListVolumeStatsByVirtualVolume enables you to list volume statistics for any volumes in the system that are associated with virtual volumes. Statistics are cumulative from the creation of the volume.

    :param virtual_volume_ids:  A list of one or more virtual volume IDs for which to retrieve information. If you specify this parameter, the method returns information about only these virtual volumes. 
    :type virtual_volume_ids: UUID

    """
    virtual_volume_ids = data_model.property(
        "virtualVolumeIDs", UUID,
        array=True, optional=True,
        documentation="""A list of one or more virtual volume IDs for which to retrieve information. If you specify this parameter, the method returns information about only these virtual volumes. """,
        dictionaryType=None
    )

    def __init__(self,
            virtual_volume_ids=None):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class SetConfigResult(data_model.DataObject):
    """SetConfigResult  

    :param config: [required] The new and current configuration for the node. 
    :type config: Config

    """
    config = data_model.property(
        "config", Config,
        array=False, optional=False,
        documentation="""The new and current configuration for the node. """,
        dictionaryType=None
    )

    def __init__(self,
            config):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class StartBulkVolumeWriteRequest(data_model.DataObject):
    """StartBulkVolumeWriteRequest  
    StartBulkVolumeWrite enables you to initialize a bulk volume write session on a specified volume. Only two bulk volume processes can run simultaneously on a volume. When you initialize the write session, data is written to a SolidFire storage volume from an external backup source. The external data is accessed by a web server running on an SF-series node. Communications and server
    interaction information for external data access is passed by a script running on the storage system.

    :param volume_id: [required] The ID of the volume to be written to. 
    :type volume_id: int

    :param format: [required] The format of the volume data. It can be either of the following formats: uncompressed: Every byte of the volume is returned without any compression. native: Opaque data is returned that is smaller and more efficiently stored and written on a subsequent bulk volume write. 
    :type format: str

    :param script:  The executable name of a script. If unspecified, the key and URL are necessary to access SF-series nodes. The script runs on the primary node and the key and URL is returned to the script, so the local web server can be contacted. 
    :type script: str

    :param script_parameters:  JSON parameters to pass to the script. 
    :type script_parameters: dict

    :param attributes:  JSON attributes for the bulk volume job. 
    :type attributes: dict

    """
    volume_id = data_model.property(
        "volumeID", int,
        array=False, optional=False,
        documentation="""The ID of the volume to be written to. """,
        dictionaryType=None
    )
    format = data_model.property(
        "format", str,
        array=False, optional=False,
        documentation="""The format of the volume data. It can be either of the following formats: uncompressed: Every byte of the volume is returned without any compression. native: Opaque data is returned that is smaller and more efficiently stored and written on a subsequent bulk volume write. """,
        dictionaryType=None
    )
    script = data_model.property(
        "script", str,
        array=False, optional=True,
        documentation="""The executable name of a script. If unspecified, the key and URL are necessary to access SF-series nodes. The script runs on the primary node and the key and URL is returned to the script, so the local web server can be contacted. """,
        dictionaryType=None
    )
    script_parameters = data_model.property(
        "scriptParameters", dict,
        array=False, optional=True,
        documentation="""JSON parameters to pass to the script. """,
        dictionaryType=None
    )
    attributes = data_model.property(
        "attributes", dict,
        array=False, optional=True,
        documentation="""JSON attributes for the bulk volume job. """,
        dictionaryType=None
    )

    def __init__(self,
            volume_id,
            format,
            script=None,
            script_parameters=None,
            attributes=None):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class ModifyVolumeResult(data_model.DataObject):
    """ModifyVolumeResult  

    :param volume:  Object containing information about the newly modified volume. 
    :type volume: Volume

    """
    volume = data_model.property(
        "volume", Volume,
        array=False, optional=True,
        documentation="""Object containing information about the newly modified volume. """,
        dictionaryType=None
    )

    def __init__(self,
            volume=None):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class PurgeDeletedVolumeResult(data_model.DataObject):
    """PurgeDeletedVolumeResult  

    """

    def __init__(self):
        kwargs = locals()
        del kwargs["self"]
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
        documentation=""" """,
        dictionaryType=None
    )
    volume_pair_uuid = data_model.property(
        "volumePairUUID", UUID,
        array=False, optional=False,
        documentation="""The snapshot is done and is writable (the active branch of the slice). """,
        dictionaryType=None
    )

    def __init__(self,
            remote_status,
            volume_pair_uuid):
        kwargs = locals()
        del kwargs["self"]
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

    :param expiration_time:  The time at which this snapshot will expire and be purged from the cluster. 
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

    :param instance_create_time: [required]  
    :type instance_create_time: str

    :param volume_name: [required]  
    :type volume_name: str

    :param instance_snapshot_uuid: [required]  
    :type instance_snapshot_uuid: UUID

    :param virtual_volume_id:  The ID of the virtual volume with which the snapshot is associated. 
    :type virtual_volume_id: UUID

    :param attributes: [required] List of Name/Value pairs in JSON object format. 
    :type attributes: dict

    :param snap_mirror_label:  Label used by SnapMirror software to specify snapshot retention policy on SnapMirror endpoint. 
    :type snap_mirror_label: str

    """
    snapshot_id = data_model.property(
        "snapshotID", int,
        array=False, optional=False,
        documentation="""Unique ID for this snapshot. """,
        dictionaryType=None
    )
    volume_id = data_model.property(
        "volumeID", int,
        array=False, optional=False,
        documentation="""The volume this snapshot was taken of. """,
        dictionaryType=None
    )
    name = data_model.property(
        "name", str,
        array=False, optional=False,
        documentation="""A name for this snapshot. It is not necessarily unique. """,
        dictionaryType=None
    )
    checksum = data_model.property(
        "checksum", str,
        array=False, optional=False,
        documentation="""A string that represents the correct digits in the stored snapshot. This checksum can be used later to compare other snapshots to detect errors in the data. """,
        dictionaryType=None
    )
    enable_remote_replication = data_model.property(
        "enableRemoteReplication", bool,
        array=False, optional=False,
        documentation="""Identifies if snapshot is enabled for remote replication. """,
        dictionaryType=None
    )
    expiration_reason = data_model.property(
        "expirationReason", str,
        array=False, optional=False,
        documentation="""Indicates how the snapshot expiration was set. Possible values: api: expiration time was set by using the API. none: there is no expiration time set. test: expiration time was set for testing. """,
        dictionaryType=None
    )
    expiration_time = data_model.property(
        "expirationTime", str,
        array=False, optional=True,
        documentation="""The time at which this snapshot will expire and be purged from the cluster. """,
        dictionaryType=None
    )
    remote_statuses = data_model.property(
        "remoteStatuses", SnapshotRemoteStatus,
        array=True, optional=True,
        documentation="""Current remote status of the snapshot remoteStatus: Possible values: Present: Snapshot exists on a remote cluster Not Present: Snapshot does not exist on remote cluster Syncing: This is a target cluster and it is currently replicating the snapshot Deleted: This is a target cluster, the snapshot has been deleted, and it still exists on the source. volumePairUUID: universal identifier of the volume pair """,
        dictionaryType=None
    )
    status = data_model.property(
        "status", str,
        array=False, optional=False,
        documentation="""Current status of the snapshot Preparing: A snapshot that is being prepared for use and is not yet writable. Done: A snapshot that has finished being prepared and is now usable. Active: This snapshot is the active branch. """,
        dictionaryType=None
    )
    snapshot_uuid = data_model.property(
        "snapshotUUID", UUID,
        array=False, optional=False,
        documentation="""Universal Unique ID of an existing snapshot. """,
        dictionaryType=None
    )
    total_size = data_model.property(
        "totalSize", int,
        array=False, optional=False,
        documentation="""Total size of this snapshot in bytes. It is equivalent to totalSize of the volume when this snapshot was taken. """,
        dictionaryType=None
    )
    group_id = data_model.property(
        "groupID", int,
        array=False, optional=True,
        documentation="""If present, the ID of the group this snapshot is a part of. If not present, this snapshot is not part of a group. """,
        dictionaryType=None
    )
    group_snapshot_uuid = data_model.property(
        "groupSnapshotUUID", UUID,
        array=False, optional=False,
        documentation="""The current "members" results contains information about each snapshot in the group. Each of these members will have a "uuid" parameter for the snapshot's UUID. """,
        dictionaryType=None
    )
    create_time = data_model.property(
        "createTime", str,
        array=False, optional=False,
        documentation="""The time this snapshot was taken. """,
        dictionaryType=None
    )
    instance_create_time = data_model.property(
        "instanceCreateTime", str,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    volume_name = data_model.property(
        "volumeName", str,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    instance_snapshot_uuid = data_model.property(
        "instanceSnapshotUUID", UUID,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    virtual_volume_id = data_model.property(
        "virtualVolumeID", UUID,
        array=False, optional=True,
        documentation="""The ID of the virtual volume with which the snapshot is associated. """,
        dictionaryType=None
    )
    attributes = data_model.property(
        "attributes", dict,
        array=False, optional=False,
        documentation="""List of Name/Value pairs in JSON object format. """,
        dictionaryType=None
    )
    snap_mirror_label = data_model.property(
        "snapMirrorLabel", str,
        array=False, optional=True,
        documentation="""Label used by SnapMirror software to specify snapshot retention policy on SnapMirror endpoint. """,
        dictionaryType=None
    )

    def __init__(self,
            snapshot_id,
            volume_id,
            name,
            checksum,
            enable_remote_replication,
            expiration_reason,
            status,
            snapshot_uuid,
            total_size,
            group_snapshot_uuid,
            create_time,
            instance_create_time,
            volume_name,
            instance_snapshot_uuid,
            attributes,
            expiration_time=None,
            remote_statuses=None,
            group_id=None,
            virtual_volume_id=None,
            snap_mirror_label=None):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class VirtualVolumeInfo(data_model.DataObject):
    """VirtualVolumeInfo  

    :param virtual_volume_id: [required]  
    :type virtual_volume_id: UUID

    :param parent_virtual_volume_id: [required]  
    :type parent_virtual_volume_id: UUID

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

    :param snapshot_info:   
    :type snapshot_info: Snapshot

    :param volume_info:   
    :type volume_info: Volume

    :param descendants:   
    :type descendants: int

    """
    virtual_volume_id = data_model.property(
        "virtualVolumeID", UUID,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    parent_virtual_volume_id = data_model.property(
        "parentVirtualVolumeID", UUID,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    storage_container = data_model.property(
        "storageContainer", StorageContainer,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    volume_id = data_model.property(
        "volumeID", int,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    snapshot_id = data_model.property(
        "snapshotID", int,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    virtual_volume_type = data_model.property(
        "virtualVolumeType", str,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    status = data_model.property(
        "status", str,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    bindings = data_model.property(
        "bindings", int,
        array=True, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    children = data_model.property(
        "children", UUID,
        array=True, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    metadata = data_model.property(
        "metadata", dict,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    snapshot_info = data_model.property(
        "snapshotInfo", Snapshot,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )
    volume_info = data_model.property(
        "volumeInfo", Volume,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )
    descendants = data_model.property(
        "descendants", int,
        array=True, optional=True,
        documentation=""" """,
        dictionaryType=None
    )

    def __init__(self,
            virtual_volume_id,
            parent_virtual_volume_id,
            storage_container,
            volume_id,
            snapshot_id,
            virtual_volume_type,
            status,
            bindings,
            children,
            metadata,
            snapshot_info=None,
            volume_info=None,
            descendants=None):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class ListVirtualVolumesResult(data_model.DataObject):
    """ListVirtualVolumesResult  

    :param virtual_volumes: [required]  
    :type virtual_volumes: VirtualVolumeInfo

    :param next_virtual_volume_id:   
    :type next_virtual_volume_id: UUID

    """
    virtual_volumes = data_model.property(
        "virtualVolumes", VirtualVolumeInfo,
        array=True, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    next_virtual_volume_id = data_model.property(
        "nextVirtualVolumeID", UUID,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )

    def __init__(self,
            virtual_volumes,
            next_virtual_volume_id=None):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class DeleteVolumesResult(data_model.DataObject):
    """DeleteVolumesResult  

    :param volumes: [required] Information about the newly deleted volume. 
    :type volumes: Volume

    """
    volumes = data_model.property(
        "volumes", Volume,
        array=True, optional=False,
        documentation="""Information about the newly deleted volume. """,
        dictionaryType=None
    )

    def __init__(self,
            volumes):
        kwargs = locals()
        del kwargs["self"]
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
        documentation="""The amount of space on the block drives. This includes additional information such as metadata entries and space which can be cleaned up. """,
        dictionaryType=None
    )
    active_sessions = data_model.property(
        "activeSessions", int,
        array=False, optional=False,
        documentation="""Number of active iSCSI sessions communicating with the cluster """,
        dictionaryType=None
    )
    average_iops = data_model.property(
        "averageIOPS", int,
        array=False, optional=False,
        documentation="""Average IPS for the cluster since midnight Coordinated Universal Time (UTC). """,
        dictionaryType=None
    )
    cluster_recent_iosize = data_model.property(
        "clusterRecentIOSize", int,
        array=False, optional=False,
        documentation="""The average size of IOPS to all volumes in the cluster. """,
        dictionaryType=None
    )
    current_iops = data_model.property(
        "currentIOPS", int,
        array=False, optional=False,
        documentation="""Average IOPS for all volumes in the cluster over the last 5 seconds. """,
        dictionaryType=None
    )
    max_iops = data_model.property(
        "maxIOPS", int,
        array=False, optional=False,
        documentation="""Estimated maximum IOPS capability of the current cluster. """,
        dictionaryType=None
    )
    max_over_provisionable_space = data_model.property(
        "maxOverProvisionableSpace", int,
        array=False, optional=False,
        documentation="""The maximum amount of provisionable space. This is a computed value. You cannot create new volumes if the current provisioned space plus the new volume size would exceed this number: maxOverProvisionableSpace = maxProvisionedSpace * GetClusterFull """,
        dictionaryType=None
    )
    max_provisioned_space = data_model.property(
        "maxProvisionedSpace", int,
        array=False, optional=False,
        documentation="""The total amount of provisionable space if all volumes are 100% filled (no thin provisioned metadata). """,
        dictionaryType=None
    )
    max_used_metadata_space = data_model.property(
        "maxUsedMetadataSpace", int,
        array=False, optional=False,
        documentation="""The amount of bytes on volume drives used to store metadata. """,
        dictionaryType=None
    )
    max_used_space = data_model.property(
        "maxUsedSpace", int,
        array=False, optional=False,
        documentation="""The total amount of space on all active block drives. """,
        dictionaryType=None
    )
    non_zero_blocks = data_model.property(
        "nonZeroBlocks", int,
        array=False, optional=False,
        documentation="""Total number of 4KiB blocks with data after the last garbage collection operation has completed. """,
        dictionaryType=None
    )
    peak_active_sessions = data_model.property(
        "peakActiveSessions", int,
        array=False, optional=False,
        documentation="""Peak number of iSCSI connections since midnight UTC. """,
        dictionaryType=None
    )
    peak_iops = data_model.property(
        "peakIOPS", int,
        array=False, optional=False,
        documentation="""The highest value for currentIOPS since midnight UTC. """,
        dictionaryType=None
    )
    provisioned_space = data_model.property(
        "provisionedSpace", int,
        array=False, optional=False,
        documentation="""Total amount of space provisioned in all volumes on the cluster. """,
        dictionaryType=None
    )
    snapshot_non_zero_blocks = data_model.property(
        "snapshotNonZeroBlocks", int,
        array=False, optional=False,
        documentation="""Total number of 4KiB blocks in snapshots with data. """,
        dictionaryType=None
    )
    timestamp = data_model.property(
        "timestamp", str,
        array=False, optional=False,
        documentation="""The date and time this cluster capacity sample was taken. """,
        dictionaryType=None
    )
    total_ops = data_model.property(
        "totalOps", int,
        array=False, optional=False,
        documentation="""The total number of I/O operations performed throughout the lifetime of the cluster """,
        dictionaryType=None
    )
    unique_blocks = data_model.property(
        "uniqueBlocks", int,
        array=False, optional=False,
        documentation="""The total number of blocks stored on the block drives. The value includes replicated blocks. """,
        dictionaryType=None
    )
    unique_blocks_used_space = data_model.property(
        "uniqueBlocksUsedSpace", int,
        array=False, optional=False,
        documentation="""The total amount of data the uniqueBlocks take up on the block drives. This number is always consistent with the uniqueBlocks value. """,
        dictionaryType=None
    )
    used_metadata_space = data_model.property(
        "usedMetadataSpace", int,
        array=False, optional=False,
        documentation="""The total amount of bytes on volume drives used to store metadata """,
        dictionaryType=None
    )
    used_metadata_space_in_snapshots = data_model.property(
        "usedMetadataSpaceInSnapshots", int,
        array=False, optional=False,
        documentation="""The amount of bytes on volume drives used for storing unique data in snapshots. This number provides an estimate of how much metadata space would be regained by deleting all snapshots on the system. """,
        dictionaryType=None
    )
    used_space = data_model.property(
        "usedSpace", int,
        array=False, optional=False,
        documentation="""Total amount of space used by all block drives in the system. """,
        dictionaryType=None
    )
    zero_blocks = data_model.property(
        "zeroBlocks", int,
        array=False, optional=False,
        documentation="""Total number of 4KiB blocks without data after the last round of garabage collection operation has completed. """,
        dictionaryType=None
    )

    def __init__(self,
            active_block_space,
            active_sessions,
            average_iops,
            cluster_recent_iosize,
            current_iops,
            max_iops,
            max_over_provisionable_space,
            max_provisioned_space,
            max_used_metadata_space,
            max_used_space,
            non_zero_blocks,
            peak_active_sessions,
            peak_iops,
            provisioned_space,
            snapshot_non_zero_blocks,
            timestamp,
            total_ops,
            unique_blocks,
            unique_blocks_used_space,
            used_metadata_space,
            used_metadata_space_in_snapshots,
            used_space,
            zero_blocks):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class GetClusterCapacityResult(data_model.DataObject):
    """GetClusterCapacityResult  

    :param cluster_capacity: [required]  
    :type cluster_capacity: ClusterCapacity

    """
    cluster_capacity = data_model.property(
        "clusterCapacity", ClusterCapacity,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )

    def __init__(self,
            cluster_capacity):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class ModifyQoSPolicyResult(data_model.DataObject):
    """ModifyQoSPolicyResult  

    :param qos_policy: [required] Details of the newly modified QoSPolicy object. 
    :type qos_policy: QoSPolicy

    """
    qos_policy = data_model.property(
        "qosPolicy", QoSPolicy,
        array=False, optional=False,
        documentation="""Details of the newly modified QoSPolicy object. """,
        dictionaryType=None
    )

    def __init__(self,
            qos_policy):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class TestConnectSvipRequest(data_model.DataObject):
    """TestConnectSvipRequest  
    The TestConnectSvip API method enables you to test the storage connection to the cluster. The test pings the SVIP using ICMP packets, and when successful, connects as an iSCSI initiator.
    Note: This method is available only through the per-node API endpoint 5.0 or later.

    :param svip:  If specified, tests the storage connection of a different SVIP. You do not need to use this value when testing the connection to the target cluster. This parameter is optional. 
    :type svip: str

    """
    svip = data_model.property(
        "svip", str,
        array=False, optional=True,
        documentation="""If specified, tests the storage connection of a different SVIP. You do not need to use this value when testing the connection to the target cluster. This parameter is optional. """,
        dictionaryType=None
    )

    def __init__(self,
            svip=None):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class TestPingRequest(data_model.DataObject):
    """TestPingRequest  
    You can use the TestPing API method to validate the
    connection to all the nodes in a cluster on both 1G and 10G interfaces by using ICMP packets. The test uses the appropriate MTU sizes for each packet based on the MTU settings in the network configuration.
    Note: This method is available only through the per-node API endpoint 5.0 or later.

    :param attempts:  Specifies the number of times the system should repeat the test ping. The default value is 5. 
    :type attempts: int

    :param hosts:  Specifies a comma-separated list of addresses or hostnames of devices to ping. 
    :type hosts: str

    :param total_timeout_sec:  Specifies the length of time the ping should wait for a system response before issuing the next ping attempt or ending the process. 
    :type total_timeout_sec: int

    :param packet_size:  Specifies the number of bytes to send in the ICMP packet that is sent to each IP. The number must be less than the maximum MTU specified in the network configuration. 
    :type packet_size: int

    :param ping_timeout_msec:  Specifies the number of milliseconds to wait for each individual ping response. The default value is 500 ms. 
    :type ping_timeout_msec: int

    :param prohibit_fragmentation:  Specifies that the Do not Fragment (DF) flag is enabled for the ICMP packets. 
    :type prohibit_fragmentation: bool

    """
    attempts = data_model.property(
        "attempts", int,
        array=False, optional=True,
        documentation="""Specifies the number of times the system should repeat the test ping. The default value is 5. """,
        dictionaryType=None
    )
    hosts = data_model.property(
        "hosts", str,
        array=False, optional=True,
        documentation="""Specifies a comma-separated list of addresses or hostnames of devices to ping. """,
        dictionaryType=None
    )
    total_timeout_sec = data_model.property(
        "totalTimeoutSec", int,
        array=False, optional=True,
        documentation="""Specifies the length of time the ping should wait for a system response before issuing the next ping attempt or ending the process. """,
        dictionaryType=None
    )
    packet_size = data_model.property(
        "packetSize", int,
        array=False, optional=True,
        documentation="""Specifies the number of bytes to send in the ICMP packet that is sent to each IP. The number must be less than the maximum MTU specified in the network configuration. """,
        dictionaryType=None
    )
    ping_timeout_msec = data_model.property(
        "pingTimeoutMsec", int,
        array=False, optional=True,
        documentation="""Specifies the number of milliseconds to wait for each individual ping response. The default value is 500 ms. """,
        dictionaryType=None
    )
    prohibit_fragmentation = data_model.property(
        "prohibitFragmentation", bool,
        array=False, optional=True,
        documentation="""Specifies that the Do not Fragment (DF) flag is enabled for the ICMP packets. """,
        dictionaryType=None
    )

    def __init__(self,
            attempts=None,
            hosts=None,
            total_timeout_sec=None,
            packet_size=None,
            ping_timeout_msec=None,
            prohibit_fragmentation=None):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class NodeStatsInfo(data_model.DataObject):
    """NodeStatsInfo  

    :param c_bytes_in: [required] Bytes in on the cluster interface. 
    :type c_bytes_in: int

    :param c_bytes_out: [required] Bytes out on the cluster interface. 
    :type c_bytes_out: int

    :param count: [required]  
    :type count: int

    :param cpu: [required] CPU Usage % 
    :type cpu: int

    :param cpu_total: [required] CPU Total 
    :type cpu_total: int

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

    :param read_ops: [required] Read Operations. 
    :type read_ops: int

    :param read_latency_usec_total: [required]  
    :type read_latency_usec_total: int

    :param s_bytes_in: [required] Bytes in on the storage interface. 
    :type s_bytes_in: int

    :param s_bytes_out: [required] Bytes out on the storage interface. 
    :type s_bytes_out: int

    :param timestamp: [required] Current time in UTC format ISO 8691 date string. 
    :type timestamp: str

    :param used_memory: [required] Total memory usage in bytes. 
    :type used_memory: int

    :param write_latency_usec_total: [required]  
    :type write_latency_usec_total: int

    :param write_ops: [required] Write Operations 
    :type write_ops: int

    """
    c_bytes_in = data_model.property(
        "cBytesIn", int,
        array=False, optional=False,
        documentation="""Bytes in on the cluster interface. """,
        dictionaryType=None
    )
    c_bytes_out = data_model.property(
        "cBytesOut", int,
        array=False, optional=False,
        documentation="""Bytes out on the cluster interface. """,
        dictionaryType=None
    )
    count = data_model.property(
        "count", int,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    cpu = data_model.property(
        "cpu", int,
        array=False, optional=False,
        documentation="""CPU Usage % """,
        dictionaryType=None
    )
    cpu_total = data_model.property(
        "cpuTotal", int,
        array=False, optional=False,
        documentation="""CPU Total """,
        dictionaryType=None
    )
    m_bytes_in = data_model.property(
        "mBytesIn", int,
        array=False, optional=False,
        documentation="""Bytes in on the management interface. """,
        dictionaryType=None
    )
    m_bytes_out = data_model.property(
        "mBytesOut", int,
        array=False, optional=False,
        documentation="""Bytes out on the management interface. """,
        dictionaryType=None
    )
    network_utilization_cluster = data_model.property(
        "networkUtilizationCluster", int,
        array=False, optional=False,
        documentation="""Network interface utilization (in %) for the cluster network interface. """,
        dictionaryType=None
    )
    network_utilization_storage = data_model.property(
        "networkUtilizationStorage", int,
        array=False, optional=False,
        documentation="""Network interface utilization (in %) for the storage network interface. """,
        dictionaryType=None
    )
    node_id = data_model.property(
        "nodeID", int,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    read_ops = data_model.property(
        "readOps", int,
        array=False, optional=False,
        documentation="""Read Operations. """,
        dictionaryType=None
    )
    read_latency_usec_total = data_model.property(
        "readLatencyUSecTotal", int,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    s_bytes_in = data_model.property(
        "sBytesIn", int,
        array=False, optional=False,
        documentation="""Bytes in on the storage interface. """,
        dictionaryType=None
    )
    s_bytes_out = data_model.property(
        "sBytesOut", int,
        array=False, optional=False,
        documentation="""Bytes out on the storage interface. """,
        dictionaryType=None
    )
    timestamp = data_model.property(
        "timestamp", str,
        array=False, optional=False,
        documentation="""Current time in UTC format ISO 8691 date string. """,
        dictionaryType=None
    )
    used_memory = data_model.property(
        "usedMemory", int,
        array=False, optional=False,
        documentation="""Total memory usage in bytes. """,
        dictionaryType=None
    )
    write_latency_usec_total = data_model.property(
        "writeLatencyUSecTotal", int,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    write_ops = data_model.property(
        "writeOps", int,
        array=False, optional=False,
        documentation="""Write Operations """,
        dictionaryType=None
    )

    def __init__(self,
            c_bytes_in,
            c_bytes_out,
            count,
            cpu,
            cpu_total,
            m_bytes_in,
            m_bytes_out,
            network_utilization_cluster,
            network_utilization_storage,
            node_id,
            read_ops,
            read_latency_usec_total,
            s_bytes_in,
            s_bytes_out,
            timestamp,
            used_memory,
            write_latency_usec_total,
            write_ops):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class NodeStatsNodes(data_model.DataObject):
    """NodeStatsNodes  

    :param nodes: [required] Node activity information for a single node. 
    :type nodes: NodeStatsInfo

    """
    nodes = data_model.property(
        "nodes", NodeStatsInfo,
        array=True, optional=False,
        documentation="""Node activity information for a single node. """,
        dictionaryType=None
    )

    def __init__(self,
            nodes):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class ListNodeStatsResult(data_model.DataObject):
    """ListNodeStatsResult  

    :param node_stats: [required] Node activity information for all nodes. 
    :type node_stats: NodeStatsNodes

    """
    node_stats = data_model.property(
        "nodeStats", NodeStatsNodes,
        array=False, optional=False,
        documentation="""Node activity information for all nodes. """,
        dictionaryType=None
    )

    def __init__(self,
            node_stats):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class DeleteVolumeAccessGroupResult(data_model.DataObject):
    """DeleteVolumeAccessGroupResult  

    """

    def __init__(self):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class DeleteInitiatorsResult(data_model.DataObject):
    """DeleteInitiatorsResult  

    """

    def __init__(self):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class AddInitiatorsToVolumeAccessGroupRequest(data_model.DataObject):
    """AddInitiatorsToVolumeAccessGroupRequest  
    AddInitiatorsToVolumeAccessGroup enables you
    to add initiators to a specified volume access group.

    :param volume_access_group_id: [required] The ID of the volume access group to modify. 
    :type volume_access_group_id: int

    :param initiators: [required] The list of initiators to add to the volume access group. 
    :type initiators: str

    """
    volume_access_group_id = data_model.property(
        "volumeAccessGroupID", int,
        array=False, optional=False,
        documentation="""The ID of the volume access group to modify. """,
        dictionaryType=None
    )
    initiators = data_model.property(
        "initiators", str,
        array=True, optional=False,
        documentation="""The list of initiators to add to the volume access group. """,
        dictionaryType=None
    )

    def __init__(self,
            volume_access_group_id,
            initiators):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class DeleteVolumeAccessGroupRequest(data_model.DataObject):
    """DeleteVolumeAccessGroupRequest  
    DeleteVolumeAccessGroup enables you to delete a
    volume access group.

    :param volume_access_group_id: [required] The ID of the volume access group to be deleted. 
    :type volume_access_group_id: int

    :param delete_orphan_initiators:  true: Delete initiator objects after they are removed from a volume access group. false: Do not delete initiator objects after they are removed from a volume access group. 
    :type delete_orphan_initiators: bool

    :param force:  Adding this flag will force the volume access group to be deleted even though it has a Virtual Network ID or Tag. true: Volume access group will be deleted. false: Default. Do not delete the volume access group if it has a Virtual Network ID or Tag. 
    :type force: bool

    """
    volume_access_group_id = data_model.property(
        "volumeAccessGroupID", int,
        array=False, optional=False,
        documentation="""The ID of the volume access group to be deleted. """,
        dictionaryType=None
    )
    delete_orphan_initiators = data_model.property(
        "deleteOrphanInitiators", bool,
        array=False, optional=True,
        documentation="""true: Delete initiator objects after they are removed from a volume access group. false: Do not delete initiator objects after they are removed from a volume access group. """,
        dictionaryType=None
    )
    force = data_model.property(
        "force", bool,
        array=False, optional=True,
        documentation="""Adding this flag will force the volume access group to be deleted even though it has a Virtual Network ID or Tag. true: Volume access group will be deleted. false: Default. Do not delete the volume access group if it has a Virtual Network ID or Tag. """,
        dictionaryType=None
    )

    def __init__(self,
            volume_access_group_id,
            delete_orphan_initiators=None,
            force=None):
        kwargs = locals()
        del kwargs["self"]
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
        documentation="""True if the feature is enabled, otherwise false. """,
        dictionaryType=None
    )
    feature = data_model.property(
        "feature", str,
        array=False, optional=False,
        documentation="""The name of the feature. """,
        dictionaryType=None
    )

    def __init__(self,
            enabled,
            feature):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class GetFeatureStatusResult(data_model.DataObject):
    """GetFeatureStatusResult  

    :param features: [required] An array of feature objects indicating the feature name and its status. 
    :type features: FeatureObject

    """
    features = data_model.property(
        "features", FeatureObject,
        array=True, optional=False,
        documentation="""An array of feature objects indicating the feature name and its status. """,
        dictionaryType=None
    )

    def __init__(self,
            features):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class ListVirtualNetworksRequest(data_model.DataObject):
    """ListVirtualNetworksRequest  
    ListVirtualNetworks enables you to list all configured virtual networks for the cluster. You can use this method to verify the virtual
    network settings in the cluster.
    There are no required parameters for this method. However, to filter the results, you can pass one or more VirtualNetworkID or
    VirtualNetworkTag values.

    :param virtual_network_id:  Network ID to filter the list for a single virtual network. 
    :type virtual_network_id: int

    :param virtual_network_tag:  Network tag to filter the list for a single virtual network. 
    :type virtual_network_tag: int

    :param virtual_network_ids:  Network IDs to include in the list. 
    :type virtual_network_ids: int

    :param virtual_network_tags:  Network tag to include in the list. 
    :type virtual_network_tags: int

    """
    virtual_network_id = data_model.property(
        "virtualNetworkID", int,
        array=False, optional=True,
        documentation="""Network ID to filter the list for a single virtual network. """,
        dictionaryType=None
    )
    virtual_network_tag = data_model.property(
        "virtualNetworkTag", int,
        array=False, optional=True,
        documentation="""Network tag to filter the list for a single virtual network. """,
        dictionaryType=None
    )
    virtual_network_ids = data_model.property(
        "virtualNetworkIDs", int,
        array=True, optional=True,
        documentation="""Network IDs to include in the list. """,
        dictionaryType=None
    )
    virtual_network_tags = data_model.property(
        "virtualNetworkTags", int,
        array=True, optional=True,
        documentation="""Network tag to include in the list. """,
        dictionaryType=None
    )

    def __init__(self,
            virtual_network_id=None,
            virtual_network_tag=None,
            virtual_network_ids=None,
            virtual_network_tags=None):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class ListSchedulesResult(data_model.DataObject):
    """ListSchedulesResult  

    :param schedules: [required] The list of schedules currently on the cluster. 
    :type schedules: Schedule

    """
    schedules = data_model.property(
        "schedules", Schedule,
        array=True, optional=False,
        documentation="""The list of schedules currently on the cluster. """,
        dictionaryType=None
    )

    def __init__(self,
            schedules):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class SetNetworkConfigRequest(data_model.DataObject):
    """SetNetworkConfigRequest  
    The SetNetworkConfig API method enables you to set the network configuration for a node. To display the current network settings for a node, run the GetNetworkConfig API method. 
    Note: This method is available only through the per-node API endpoint 5.0 or later.
    Changing the "bond-mode" on a node can cause a temporary loss of network connectivity. Exercise caution when using this method.

    :param network: [required] An object containing node network settings to modify. 
    :type network: NetworkParams

    """
    network = data_model.property(
        "network", NetworkParams,
        array=False, optional=False,
        documentation="""An object containing node network settings to modify. """,
        dictionaryType=None
    )

    def __init__(self,
            network):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class StartBulkVolumeReadRequest(data_model.DataObject):
    """StartBulkVolumeReadRequest  
    StartBulkVolumeRead enables you to initialize a bulk volume read session on a specified volume. Only two bulk volume processes
    can run simultaneously on a volume. When you initialize the session, data is read from a SolidFire storage volume for the purposes
    of storing the data on an external backup source. The external data is accessed by a web server running on an SF-series node.
    Communications and server interaction information for external data access is passed by a script running on the storage system.
    At the start of a bulk volume read operation, a snapshot of the volume is made and the snapshot is deleted when the read is complete. You can also read a snapshot of the volume by entering the ID of the snapshot as a parameter. When you read a
    previous snapshot, the system does not create a new snapshot of the volume or delete the previous snapshot when the
    read completes.
    Note: This process creates a new snapshot if the ID of an existing snapshot is not provided. Snapshots can be created if cluster fullness is at stage 2 or 3. Snapshots are not created when cluster fullness is at stage 4 or 5.

    :param volume_id: [required] The ID of the volume to be read. 
    :type volume_id: int

    :param format: [required] The format of the volume data. It can be either of the following formats: uncompressed: Every byte of the volume is returned without any compression. native: Opaque data is returned that is smaller and more efficiently stored and written on a subsequent bulk volume write. 
    :type format: str

    :param snapshot_id:  The ID of a previously created snapshot used for bulk volume reads. If no ID is entered, a snapshot of the current active volume image is made. 
    :type snapshot_id: int

    :param script:  The executable name of a script. If unspecified, the key and URL is necessary to access SF-series nodes. The script is run on the primary node and the key and URL is returned to the script so the local web server can be contacted. 
    :type script: str

    :param script_parameters:  JSON parameters to pass to the script. 
    :type script_parameters: dict

    :param attributes:  JSON attributes for the bulk volume job. 
    :type attributes: dict

    """
    volume_id = data_model.property(
        "volumeID", int,
        array=False, optional=False,
        documentation="""The ID of the volume to be read. """,
        dictionaryType=None
    )
    format = data_model.property(
        "format", str,
        array=False, optional=False,
        documentation="""The format of the volume data. It can be either of the following formats: uncompressed: Every byte of the volume is returned without any compression. native: Opaque data is returned that is smaller and more efficiently stored and written on a subsequent bulk volume write. """,
        dictionaryType=None
    )
    snapshot_id = data_model.property(
        "snapshotID", int,
        array=False, optional=True,
        documentation="""The ID of a previously created snapshot used for bulk volume reads. If no ID is entered, a snapshot of the current active volume image is made. """,
        dictionaryType=None
    )
    script = data_model.property(
        "script", str,
        array=False, optional=True,
        documentation="""The executable name of a script. If unspecified, the key and URL is necessary to access SF-series nodes. The script is run on the primary node and the key and URL is returned to the script so the local web server can be contacted. """,
        dictionaryType=None
    )
    script_parameters = data_model.property(
        "scriptParameters", dict,
        array=False, optional=True,
        documentation="""JSON parameters to pass to the script. """,
        dictionaryType=None
    )
    attributes = data_model.property(
        "attributes", dict,
        array=False, optional=True,
        documentation="""JSON attributes for the bulk volume job. """,
        dictionaryType=None
    )

    def __init__(self,
            volume_id,
            format,
            snapshot_id=None,
            script=None,
            script_parameters=None,
            attributes=None):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class AddDrivesRequest(data_model.DataObject):
    """AddDrivesRequest  
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

    :param force_during_upgrade:  Allows the user to force the addition of drives during an upgrade. 
    :type force_during_upgrade: bool

    :param force_during_bin_sync:  Allows the user to force the addition of drives during a bin sync operation. 
    :type force_during_bin_sync: bool

    """
    drives = data_model.property(
        "drives", NewDrive,
        array=True, optional=False,
        documentation="""Returns information about each drive to be added to the cluster. Possible values are: driveID: The ID of the drive to add. (Integer) type: (Optional) The type of drive to add. Valid values are "slice" or "block". If omitted, the system assigns the correct type. (String) """,
        dictionaryType=None
    )
    force_during_upgrade = data_model.property(
        "forceDuringUpgrade", bool,
        array=False, optional=True,
        documentation="""Allows the user to force the addition of drives during an upgrade. """,
        dictionaryType=None
    )
    force_during_bin_sync = data_model.property(
        "forceDuringBinSync", bool,
        array=False, optional=True,
        documentation="""Allows the user to force the addition of drives during a bin sync operation. """,
        dictionaryType=None
    )

    def __init__(self,
            drives,
            force_during_upgrade=None,
            force_during_bin_sync=None):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class DeleteVolumeRequest(data_model.DataObject):
    """DeleteVolumeRequest  
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

    :param volume_id: [required] The ID of the volume to be deleted. 
    :type volume_id: int

    """
    volume_id = data_model.property(
        "volumeID", int,
        array=False, optional=False,
        documentation="""The ID of the volume to be deleted. """,
        dictionaryType=None
    )

    def __init__(self,
            volume_id):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class CreateScheduleResult(data_model.DataObject):
    """CreateScheduleResult  

    :param schedule_id: [required]  
    :type schedule_id: int

    """
    schedule_id = data_model.property(
        "scheduleID", int,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )

    def __init__(self,
            schedule_id):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class ShutdownRequest(data_model.DataObject):
    """ShutdownRequest  
    The Shutdown API method enables you to restart or shutdown a node that has not yet been added to a cluster. To use this method,
    log in to the MIP for the pending node, and enter the "shutdown" method with either the "restart" or "halt" options.

    :param nodes: [required] List of NodeIDs for the nodes to be shutdown. 
    :type nodes: int

    :param option:  Specifies the action to take for the node shutdown. Possible values are: restart: Restarts the node. halt: Shuts down the node. 
    :type option: str

    """
    nodes = data_model.property(
        "nodes", int,
        array=True, optional=False,
        documentation="""List of NodeIDs for the nodes to be shutdown. """,
        dictionaryType=None
    )
    option = data_model.property(
        "option", str,
        array=False, optional=True,
        documentation="""Specifies the action to take for the node shutdown. Possible values are: restart: Restarts the node. halt: Shuts down the node. """,
        dictionaryType=None
    )

    def __init__(self,
            nodes,
            option=None):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class GetAsyncResultRequest(data_model.DataObject):
    """GetAsyncResultRequest  
    You can use GetAsyncResult to retrieve the result of asynchronous method calls. Some method calls require some time to run, and
    might not be finished when the system sends the initial response. To obtain the status or result of the method call, use
    GetAsyncResult to poll the asyncHandle value returned by the method.
    GetAsyncResult returns the overall status of the operation (in progress, completed, or error) in a standard fashion, but the actual
    data returned for the operation depends on the original method call and the return data is documented with each method.

    :param async_handle: [required] A value that was returned from the original asynchronous method call. 
    :type async_handle: int

    :param keep_result:  If true, GetAsyncResult does not remove the asynchronous result upon returning it, enabling future queries to that asyncHandle. 
    :type keep_result: bool

    """
    async_handle = data_model.property(
        "asyncHandle", int,
        array=False, optional=False,
        documentation="""A value that was returned from the original asynchronous method call. """,
        dictionaryType=None
    )
    keep_result = data_model.property(
        "keepResult", bool,
        array=False, optional=True,
        documentation="""If true, GetAsyncResult does not remove the asynchronous result upon returning it, enabling future queries to that asyncHandle. """,
        dictionaryType=None
    )

    def __init__(self,
            async_handle,
            keep_result=None):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class CreateVolumeResult(data_model.DataObject):
    """CreateVolumeResult  

    :param volume:   
    :type volume: Volume

    :param volume_id: [required] VolumeID for the newly created volume. 
    :type volume_id: int

    :param curve: [required] The curve is a set of key-value pairs. The keys are I/O sizes in bytes. The values represent the cost performing an IOP at a specific I/O size. The curve is calculated relative to a 4096 byte operation set at 100 IOPS. 
    :type curve: dict

    """
    volume = data_model.property(
        "volume", Volume,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )
    volume_id = data_model.property(
        "volumeID", int,
        array=False, optional=False,
        documentation="""VolumeID for the newly created volume. """,
        dictionaryType=None
    )
    curve = data_model.property(
        "curve", dict,
        array=False, optional=False,
        documentation="""The curve is a set of key-value pairs. The keys are I/O sizes in bytes. The values represent the cost performing an IOP at a specific I/O size. The curve is calculated relative to a 4096 byte operation set at 100 IOPS. """,
        dictionaryType=int
    )

    def __init__(self,
            volume_id,
            curve,
            volume=None):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class ModifyAccountRequest(data_model.DataObject):
    """ModifyAccountRequest  
    ModifyAccount enables you to modify an existing account.
    When you lock an account, any existing connections from that account are immediately terminated. When you change an account's
    CHAP settings, any existing connections remain active, and the new CHAP settings are used on subsequent connections or
    reconnections.
    To clear an account's attributes, specify {} for the attributes parameter.

    :param account_id: [required] Specifies the AccountID for the account to be modified. 
    :type account_id: int

    :param username:  Specifies the username associated with the account. (Might be 1 to 64 characters in length). 
    :type username: str

    :param status:  Sets the status for the account. Possible values are: active: The account is active and connections are allowed. locked: The account is locked and connections are refused. 
    :type status: str

    :param initiator_secret:  Specifies the CHAP secret to use for the initiator. This secret must be 12-16 characters in length and should be impenetrable. The initiator CHAP secret must be unique and cannot be the same as the target CHAP secret. 
    :type initiator_secret: CHAPSecret

    :param target_secret:  Specifies the CHAP secret to use for the target (mutual CHAP authentication). This secret must be 12-16 characters in length and should be impenetrable. The target CHAP secret must be unique and cannot be the same as the initiator CHAP secret. 
    :type target_secret: CHAPSecret

    :param attributes:  List of name-value pairs in JSON object format. 
    :type attributes: dict

    """
    account_id = data_model.property(
        "accountID", int,
        array=False, optional=False,
        documentation="""Specifies the AccountID for the account to be modified. """,
        dictionaryType=None
    )
    username = data_model.property(
        "username", str,
        array=False, optional=True,
        documentation="""Specifies the username associated with the account. (Might be 1 to 64 characters in length). """,
        dictionaryType=None
    )
    status = data_model.property(
        "status", str,
        array=False, optional=True,
        documentation="""Sets the status for the account. Possible values are: active: The account is active and connections are allowed. locked: The account is locked and connections are refused. """,
        dictionaryType=None
    )
    initiator_secret = data_model.property(
        "initiatorSecret", CHAPSecret,
        array=False, optional=True,
        documentation="""Specifies the CHAP secret to use for the initiator. This secret must be 12-16 characters in length and should be impenetrable. The initiator CHAP secret must be unique and cannot be the same as the target CHAP secret. """,
        dictionaryType=None
    )
    target_secret = data_model.property(
        "targetSecret", CHAPSecret,
        array=False, optional=True,
        documentation="""Specifies the CHAP secret to use for the target (mutual CHAP authentication). This secret must be 12-16 characters in length and should be impenetrable. The target CHAP secret must be unique and cannot be the same as the initiator CHAP secret. """,
        dictionaryType=None
    )
    attributes = data_model.property(
        "attributes", dict,
        array=False, optional=True,
        documentation="""List of name-value pairs in JSON object format. """,
        dictionaryType=None
    )

    def __init__(self,
            account_id,
            username=None,
            status=None,
            initiator_secret=None,
            target_secret=None,
            attributes=None):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class ClusterAdmin(data_model.DataObject):
    """ClusterAdmin  

    :param auth_method: [required]  
    :type auth_method: str

    :param access: [required]  
    :type access: str

    :param cluster_admin_id: [required]  
    :type cluster_admin_id: int

    :param username: [required]  
    :type username: str

    :param attributes:  List of Name/Value pairs in JSON object format. 
    :type attributes: dict

    """
    auth_method = data_model.property(
        "authMethod", str,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    access = data_model.property(
        "access", str,
        array=True, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    cluster_admin_id = data_model.property(
        "clusterAdminID", int,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    username = data_model.property(
        "username", str,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    attributes = data_model.property(
        "attributes", dict,
        array=False, optional=True,
        documentation="""List of Name/Value pairs in JSON object format. """,
        dictionaryType=None
    )

    def __init__(self,
            auth_method,
            access,
            cluster_admin_id,
            username,
            attributes=None):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class GetCurrentClusterAdminResult(data_model.DataObject):
    """GetCurrentClusterAdminResult  

    :param cluster_admin: [required] Information about all cluster and LDAP administrators that exist for a cluster. 
    :type cluster_admin: ClusterAdmin

    """
    cluster_admin = data_model.property(
        "clusterAdmin", ClusterAdmin,
        array=False, optional=False,
        documentation="""Information about all cluster and LDAP administrators that exist for a cluster. """,
        dictionaryType=None
    )

    def __init__(self,
            cluster_admin):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class ResetNodeRequest(data_model.DataObject):
    """ResetNodeRequest  
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

    :param reboot:  Set to true if you want to reboot the node. 
    :type reboot: bool

    :param options:  Used to enter specifications for running the reset operation. Available options: 'edebug': '', 'sf_auto': '0', 'sf_bond_mode': 'ActivePassive', 'sf_check_hardware': '0', 'sf_disable_otpw': '0', 'sf_fa_host': '', 'sf_hostname': 'SF-FA18', 'sf_inplace': '1', 'sf_inplace_die_action': 'kexec', 'sf_inplace_safe': '0', 'sf_keep_cluster_config': '0', 'sf_keep_data': '0', 'sf_keep_hostname': '0', 'sf_keep_network_config': '0', 'sf_keep_paths': '/var/log/hardware.xml 'sf_max_archives': '5', 'sf_nvram_size': '', 'sf_oldroot': '', 'sf_postinst_erase_root_drive': '0', 'sf_root_drive': '', 'sf_rtfi_cleanup_state': '', 'sf_secure_erase': '1', 'sf_secure_erase_retries': '5', 'sf_slice_size': '', 'sf_ssh_key': '1', 'sf_ssh_root': '1', 'sf_start_rtfi': '1', 'sf_status_httpserver': '1', 'sf_status_httpserver_stop_delay': '5m', 'sf_status_inject_failure': '', 'sf_status_json': '0', 'sf_support_host': 'sfsupport.solidfire.com', 'sf_test_hardware': '0', 'sf_upgrade': '0', 'sf_upgrade_firmware': '0', 'sf_upload_logs_url': '' 
    :type options: str

    """
    build = data_model.property(
        "build", str,
        array=False, optional=False,
        documentation="""Specifies the URL to a remote Element software image to which the node will be reset. """,
        dictionaryType=None
    )
    force = data_model.property(
        "force", bool,
        array=False, optional=False,
        documentation="""Required parameter to successfully reset the node. """,
        dictionaryType=None
    )
    reboot = data_model.property(
        "reboot", bool,
        array=False, optional=True,
        documentation="""Set to true if you want to reboot the node. """,
        dictionaryType=None
    )
    options = data_model.property(
        "options", str,
        array=False, optional=True,
        documentation="""Used to enter specifications for running the reset operation. Available options: 'edebug': '', 'sf_auto': '0', 'sf_bond_mode': 'ActivePassive', 'sf_check_hardware': '0', 'sf_disable_otpw': '0', 'sf_fa_host': '', 'sf_hostname': 'SF-FA18', 'sf_inplace': '1', 'sf_inplace_die_action': 'kexec', 'sf_inplace_safe': '0', 'sf_keep_cluster_config': '0', 'sf_keep_data': '0', 'sf_keep_hostname': '0', 'sf_keep_network_config': '0', 'sf_keep_paths': '/var/log/hardware.xml 'sf_max_archives': '5', 'sf_nvram_size': '', 'sf_oldroot': '', 'sf_postinst_erase_root_drive': '0', 'sf_root_drive': '', 'sf_rtfi_cleanup_state': '', 'sf_secure_erase': '1', 'sf_secure_erase_retries': '5', 'sf_slice_size': '', 'sf_ssh_key': '1', 'sf_ssh_root': '1', 'sf_start_rtfi': '1', 'sf_status_httpserver': '1', 'sf_status_httpserver_stop_delay': '5m', 'sf_status_inject_failure': '', 'sf_status_json': '0', 'sf_support_host': 'sfsupport.solidfire.com', 'sf_test_hardware': '0', 'sf_upgrade': '0', 'sf_upgrade_firmware': '0', 'sf_upload_logs_url': '' """,
        dictionaryType=None
    )

    def __init__(self,
            build,
            force,
            reboot=None,
            options=None):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class SetLoginSessionInfoRequest(data_model.DataObject):
    """SetLoginSessionInfoRequest  
    You can use SetLoginSessionInfo to set the period of time that a session's login authentication is valid. After the log in period elapses without activity on the system, the authentication expires. New login credentials are required for continued access to the cluster after the timeout period has elapsed.

    :param timeout: [required] Cluster authentication expiration period. Formatted in HH:mm:ss. For example, 01:30:00, 00:90:00, and 00:00:5400 can be used to equal a 90 minute timeout period. The default value is 30 minutes. The minimum value is 1 minute. 
    :type timeout: str

    """
    timeout = data_model.property(
        "timeout", str,
        array=False, optional=False,
        documentation="""Cluster authentication expiration period. Formatted in HH:mm:ss. For example, 01:30:00, 00:90:00, and 00:00:5400 can be used to equal a 90 minute timeout period. The default value is 30 minutes. The minimum value is 1 minute. """,
        dictionaryType=None
    )

    def __init__(self,
            timeout):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class CreateSnapshotResult(data_model.DataObject):
    """CreateSnapshotResult  

    :param snapshot: [required]  
    :type snapshot: Snapshot

    :param snapshot_id: [required] ID of the newly-created snapshot. 
    :type snapshot_id: int

    :param checksum: [required] A string that represents the correct digits in the stored snapshot. This checksum can be used later to compare other snapshots to detect errors in the data. 
    :type checksum: str

    """
    snapshot = data_model.property(
        "snapshot", Snapshot,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    snapshot_id = data_model.property(
        "snapshotID", int,
        array=False, optional=False,
        documentation="""ID of the newly-created snapshot. """,
        dictionaryType=None
    )
    checksum = data_model.property(
        "checksum", str,
        array=False, optional=False,
        documentation="""A string that represents the correct digits in the stored snapshot. This checksum can be used later to compare other snapshots to detect errors in the data. """,
        dictionaryType=None
    )

    def __init__(self,
            snapshot,
            snapshot_id,
            checksum):
        kwargs = locals()
        del kwargs["self"]
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
        documentation="""The version of the firmware installed on the Fibre Channel port. """,
        dictionaryType=None
    )
    hba_port = data_model.property(
        "hbaPort", int,
        array=False, optional=False,
        documentation="""The ID of the individual HBA port. """,
        dictionaryType=None
    )
    model = data_model.property(
        "model", str,
        array=False, optional=False,
        documentation="""Model of the HBA on the port. """,
        dictionaryType=None
    )
    n_port_id = data_model.property(
        "nPortID", str,
        array=False, optional=False,
        documentation="""Unique SolidFire port node ID. """,
        dictionaryType=None
    )
    pci_slot = data_model.property(
        "pciSlot", int,
        array=False, optional=False,
        documentation="""Slot in which the pci card resides on the Fibre Channel node hardware. """,
        dictionaryType=None
    )
    serial = data_model.property(
        "serial", str,
        array=False, optional=False,
        documentation="""Serial number on the Fibre Channel port. """,
        dictionaryType=None
    )
    speed = data_model.property(
        "speed", str,
        array=False, optional=False,
        documentation="""Speed of the HBA on the port. """,
        dictionaryType=None
    )
    state = data_model.property(
        "state", str,
        array=False, optional=False,
        documentation="""Possible values:  <strong>UnknownNotPresentOnlineOfflineBlockedBypassedDiagnosticsLinkdownErrorLoopbackDeleted</strong> """,
        dictionaryType=None
    )
    switch_wwn = data_model.property(
        "switchWwn", str,
        array=False, optional=False,
        documentation="""The World Wide Name of the Fibre Channel switch port. """,
        dictionaryType=None
    )
    wwnn = data_model.property(
        "wwnn", str,
        array=False, optional=False,
        documentation="""World Wide Node Name of the HBA node. """,
        dictionaryType=None
    )
    wwpn = data_model.property(
        "wwpn", str,
        array=False, optional=False,
        documentation="""World Wide Port Name assigned to the physical port of the HBA. """,
        dictionaryType=None
    )

    def __init__(self,
            firmware,
            hba_port,
            model,
            n_port_id,
            pci_slot,
            serial,
            speed,
            state,
            switch_wwn,
            wwnn,
            wwpn):
        kwargs = locals()
        del kwargs["self"]
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
        documentation="""List of all physical Fibre Channel ports. """,
        dictionaryType=None
    )

    def __init__(self,
            fibre_channel_ports):
        kwargs = locals()
        del kwargs["self"]
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
        documentation="""Used to return information about the Fibre Channel ports. """,
        dictionaryType=None
    )

    def __init__(self,
            result):
        kwargs = locals()
        del kwargs["self"]
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
        documentation="""Used to return information about the Fibre Channel ports. """,
        dictionaryType=FibreChannelPortInfoResult
    )

    def __init__(self,
            fibre_channel_port_info):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class RollbackToSnapshotRequest(data_model.DataObject):
    """RollbackToSnapshotRequest  
    RollbackToSnapshot enables you to make an existing snapshot of the "active" volume image. This method creates a new snapshot
    from an existing snapshot. The new snapshot becomes "active" and the existing snapshot is preserved until you delete it.
    The previously "active" snapshot is deleted unless you set the parameter saveCurrentState to true.
    Note: Creating a snapshot is allowed if cluster fullness is at stage 2 or 3. Snapshots are not created when cluster fullness is
    at stage 4 or 5.

    :param volume_id: [required] VolumeID for the volume. 
    :type volume_id: int

    :param snapshot_id: [required] The ID of a previously created snapshot on the given volume. 
    :type snapshot_id: int

    :param save_current_state: [required] Specifies whether to save an active volume image or delete it. Values are: true: The previous active volume image is kept. false: (default) The previous active volume image is deleted. 
    :type save_current_state: bool

    :param name:  Name for the snapshot. If unspecified, the name of the snapshot being rolled back to is used with "- copy" appended to the end of the name. 
    :type name: str

    :param attributes:  List of name-value pairs in JSON object format. 
    :type attributes: dict

    """
    volume_id = data_model.property(
        "volumeID", int,
        array=False, optional=False,
        documentation="""VolumeID for the volume. """,
        dictionaryType=None
    )
    snapshot_id = data_model.property(
        "snapshotID", int,
        array=False, optional=False,
        documentation="""The ID of a previously created snapshot on the given volume. """,
        dictionaryType=None
    )
    save_current_state = data_model.property(
        "saveCurrentState", bool,
        array=False, optional=False,
        documentation="""Specifies whether to save an active volume image or delete it. Values are: true: The previous active volume image is kept. false: (default) The previous active volume image is deleted. """,
        dictionaryType=None
    )
    name = data_model.property(
        "name", str,
        array=False, optional=True,
        documentation="""Name for the snapshot. If unspecified, the name of the snapshot being rolled back to is used with "- copy" appended to the end of the name. """,
        dictionaryType=None
    )
    attributes = data_model.property(
        "attributes", dict,
        array=False, optional=True,
        documentation="""List of name-value pairs in JSON object format. """,
        dictionaryType=None
    )

    def __init__(self,
            volume_id,
            snapshot_id,
            save_current_state,
            name=None,
            attributes=None):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class RestoreDeletedVolumeResult(data_model.DataObject):
    """RestoreDeletedVolumeResult  

    """

    def __init__(self):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class ListDeletedVolumesResult(data_model.DataObject):
    """ListDeletedVolumesResult  

    :param volumes: [required] List of deleted volumes. 
    :type volumes: Volume

    """
    volumes = data_model.property(
        "volumes", Volume,
        array=True, optional=False,
        documentation="""List of deleted volumes. """,
        dictionaryType=None
    )

    def __init__(self,
            volumes):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class ListSnapshotsRequest(data_model.DataObject):
    """ListSnapshotsRequest  
    ListSnapshots enables you to return the attributes of each snapshot taken on the volume. Information about snapshots that reside on the target cluster is displayed on the source cluster when this method is called from the source cluster.

    :param volume_id:  Retrieves snapshots for a volume. If volumeID is not provided, all snapshots for all volumes are returned. 
    :type volume_id: int

    :param snapshot_id:  Retrieves information for a specific snapshot ID. 
    :type snapshot_id: int

    """
    volume_id = data_model.property(
        "volumeID", int,
        array=False, optional=True,
        documentation="""Retrieves snapshots for a volume. If volumeID is not provided, all snapshots for all volumes are returned. """,
        dictionaryType=None
    )
    snapshot_id = data_model.property(
        "snapshotID", int,
        array=False, optional=True,
        documentation="""Retrieves information for a specific snapshot ID. """,
        dictionaryType=None
    )

    def __init__(self,
            volume_id=None,
            snapshot_id=None):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class ListActiveVolumesResult(data_model.DataObject):
    """ListActiveVolumesResult  

    :param volumes: [required] List of active volumes. 
    :type volumes: Volume

    """
    volumes = data_model.property(
        "volumes", Volume,
        array=True, optional=False,
        documentation="""List of active volumes. """,
        dictionaryType=None
    )

    def __init__(self,
            volumes):
        kwargs = locals()
        del kwargs["self"]
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
        documentation="""Indicates whether or not the nodes in the cluster are listening for broadcast NTP messages. Possible values: true false """,
        dictionaryType=None
    )
    servers = data_model.property(
        "servers", str,
        array=True, optional=False,
        documentation="""List of NTP servers. """,
        dictionaryType=None
    )

    def __init__(self,
            broadcastclient,
            servers):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class ListAsyncResultsRequest(data_model.DataObject):
    """ListAsyncResultsRequest  
    You can use ListAsyncResults to list the results of all currently running and completed asynchronous methods on the system.
    Querying asynchronous results with ListAsyncResults does not cause completed asyncHandles to expire; you can use GetAsyncResult
    to query any of the asyncHandles returned by ListAsyncResults.

    :param async_result_types:  An optional list of types of results. You can use this list to restrict the results to only these types of operations. Possible values are: BulkVolume: Copy operations between volumes, such as backups or restores. Clone: Volume cloning operations. DriveRemoval: Operations involving the system copying data from a drive in preparation to remove it from the cluster. RtfiPendingNode: Operations involving the system installing compatible software on a node before adding it to the cluster 
    :type async_result_types: str

    """
    async_result_types = data_model.property(
        "asyncResultTypes", str,
        array=True, optional=True,
        documentation="""An optional list of types of results. You can use this list to restrict the results to only these types of operations. Possible values are: BulkVolume: Copy operations between volumes, such as backups or restores. Clone: Volume cloning operations. DriveRemoval: Operations involving the system copying data from a drive in preparation to remove it from the cluster. RtfiPendingNode: Operations involving the system installing compatible software on a node before adding it to the cluster """,
        dictionaryType=None
    )

    def __init__(self,
            async_result_types=None):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class ModifyAccountResult(data_model.DataObject):
    """ModifyAccountResult  

    :param account: [required]  
    :type account: Account

    """
    account = data_model.property(
        "account", Account,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )

    def __init__(self,
            account):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class ModifyInitiator(data_model.DataObject):
    """ModifyInitiator  
    Object containing characteristics of each initiator to modify

    :param initiator_id: [required] (Required) The numeric ID of the initiator to modify. (Integer) 
    :type initiator_id: int

    :param alias:  (Optional) A new friendly name to assign to the initiator. (String) 
    :type alias: str

    :param volume_access_group_id:  (Optional) The ID of the volume access group to which the newly created initiator should be added. If the initiator was previously in a different volume access group, it is removed from the old volume access group. If this key is present but null, the initiator is removed from its current volume access group, but not placed in any new volume access group. (Integer) 
    :type volume_access_group_id: int

    :param attributes:  (Optional) A new set of JSON attributes assigned to this initiator. (JSON Object) 
    :type attributes: dict

    """
    initiator_id = data_model.property(
        "initiatorID", int,
        array=False, optional=False,
        documentation="""(Required) The numeric ID of the initiator to modify. (Integer) """,
        dictionaryType=None
    )
    alias = data_model.property(
        "alias", str,
        array=False, optional=True,
        documentation="""(Optional) A new friendly name to assign to the initiator. (String) """,
        dictionaryType=None
    )
    volume_access_group_id = data_model.property(
        "volumeAccessGroupID", int,
        array=False, optional=True,
        documentation="""(Optional) The ID of the volume access group to which the newly created initiator should be added. If the initiator was previously in a different volume access group, it is removed from the old volume access group. If this key is present but null, the initiator is removed from its current volume access group, but not placed in any new volume access group. (Integer) """,
        dictionaryType=None
    )
    attributes = data_model.property(
        "attributes", dict,
        array=False, optional=True,
        documentation="""(Optional) A new set of JSON attributes assigned to this initiator. (JSON Object) """,
        dictionaryType=None
    )

    def __init__(self,
            initiator_id,
            alias=None,
            volume_access_group_id=None,
            attributes=None):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class ModifyInitiatorsRequest(data_model.DataObject):
    """ModifyInitiatorsRequest  
    ModifyInitiators enables you to change the attributes of one or more existing initiators. You cannot change the name of an existing
    initiator. If you need to change the name of an initiator, delete it first with DeleteInitiators and create a new one with
    CreateInitiators.
    If ModifyInitiators fails to change one of the initiators provided in the parameter, the method returns an error and does not modify
    any initiators (no partial completion is possible).

    :param initiators: [required] A list of objects containing characteristics of each initiator to modify. Values are: initiatorID: (Required) The ID of the initiator to modify. (Integer) alias: (Optional) A new friendly name to assign to the initiator. (String) attributes: (Optional) A new set of JSON attributes to assign to the initiator. (JSON Object) volumeAccessGroupID: (Optional) The ID of the volume access group into to which the initiator should be added. If the initiator was previously in a different volume access group, it is removed from the old volume access group. If this key is present but null, the initiator is removed from its current volume access group, but not placed in any new volume access group. (Integer) 
    :type initiators: ModifyInitiator

    """
    initiators = data_model.property(
        "initiators", ModifyInitiator,
        array=True, optional=False,
        documentation="""A list of objects containing characteristics of each initiator to modify. Values are: initiatorID: (Required) The ID of the initiator to modify. (Integer) alias: (Optional) A new friendly name to assign to the initiator. (String) attributes: (Optional) A new set of JSON attributes to assign to the initiator. (JSON Object) volumeAccessGroupID: (Optional) The ID of the volume access group into to which the initiator should be added. If the initiator was previously in a different volume access group, it is removed from the old volume access group. If this key is present but null, the initiator is removed from its current volume access group, but not placed in any new volume access group. (Integer) """,
        dictionaryType=None
    )

    def __init__(self,
            initiators):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class ListUtilitiesResult(data_model.DataObject):
    """ListUtilitiesResult  

    :param utilities: [required] List of utilities currently available to run on the node. 
    :type utilities: str

    """
    utilities = data_model.property(
        "utilities", str,
        array=False, optional=False,
        documentation="""List of utilities currently available to run on the node. """,
        dictionaryType=None
    )

    def __init__(self,
            utilities):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class RemoveInitiatorsFromVolumeAccessGroupRequest(data_model.DataObject):
    """RemoveInitiatorsFromVolumeAccessGroupRequest  
    RemoveInitiatorsFromVolumeAccessGroup enables
    you to remove initiators from a specified volume access
    group.

    :param volume_access_group_id: [required] The ID of the volume access group from which the initiators are removed. 
    :type volume_access_group_id: int

    :param initiators: [required] The list of initiators to remove from the volume access group. 
    :type initiators: str

    :param delete_orphan_initiators:  true: Delete initiator objects after they are removed from a volume access group. false: Do not delete initiator objects after they are removed from a volume access group. 
    :type delete_orphan_initiators: bool

    """
    volume_access_group_id = data_model.property(
        "volumeAccessGroupID", int,
        array=False, optional=False,
        documentation="""The ID of the volume access group from which the initiators are removed. """,
        dictionaryType=None
    )
    initiators = data_model.property(
        "initiators", str,
        array=True, optional=False,
        documentation="""The list of initiators to remove from the volume access group. """,
        dictionaryType=None
    )
    delete_orphan_initiators = data_model.property(
        "deleteOrphanInitiators", bool,
        array=False, optional=True,
        documentation="""true: Delete initiator objects after they are removed from a volume access group. false: Do not delete initiator objects after they are removed from a volume access group. """,
        dictionaryType=None
    )

    def __init__(self,
            volume_access_group_id,
            initiators,
            delete_orphan_initiators=None):
        kwargs = locals()
        del kwargs["self"]
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
        documentation=""" """,
        dictionaryType=None
    )
    protocol_endpoint_state = data_model.property(
        "protocolEndpointState", str,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    provider_type = data_model.property(
        "providerType", str,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    primary_provider_id = data_model.property(
        "primaryProviderID", int,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    secondary_provider_id = data_model.property(
        "secondaryProviderID", int,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    scsi_naadevice_id = data_model.property(
        "scsiNAADeviceID", str,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )

    def __init__(self,
            protocol_endpoint_id,
            protocol_endpoint_state,
            provider_type,
            primary_provider_id,
            secondary_provider_id,
            scsi_naadevice_id):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class ListProtocolEndpointsResult(data_model.DataObject):
    """ListProtocolEndpointsResult  

    :param protocol_endpoints: [required]  
    :type protocol_endpoints: ProtocolEndpoint

    """
    protocol_endpoints = data_model.property(
        "protocolEndpoints", ProtocolEndpoint,
        array=True, optional=False,
        documentation=""" """,
        dictionaryType=None
    )

    def __init__(self,
            protocol_endpoints):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class SetSnmpTrapInfoResult(data_model.DataObject):
    """SetSnmpTrapInfoResult  

    """

    def __init__(self):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class DeleteStorageContainersRequest(data_model.DataObject):
    """DeleteStorageContainersRequest  
    DeleteStorageContainers enables you to remove up to 2000 Virtual Volume (VVol) storage containers from the system at one time.
    The storage containers you remove must not contain any VVols.

    :param storage_container_ids: [required] A list of IDs of the storage containers to delete. You can specify up to 2000 IDs in the list. 
    :type storage_container_ids: UUID

    """
    storage_container_ids = data_model.property(
        "storageContainerIDs", UUID,
        array=True, optional=False,
        documentation="""A list of IDs of the storage containers to delete. You can specify up to 2000 IDs in the list. """,
        dictionaryType=None
    )

    def __init__(self,
            storage_container_ids):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class VolumeAccessGroup(data_model.DataObject):
    """VolumeAccessGroup  
    A volume access group is a useful way of grouping volumes and initiators together for ease of management.
    
    Volume Access Group Limits:
    
    - A volume access group can contain up to sixty-four initiator IQNs.
    - An initiator can only beinteger to only one volume access group.
    - A volume access group can contain up to two thousand volumes.
    - Each volume access group can beinteger to a maximum of four other volume access groups.

    :param deleted_volumes: [required] A list of deleted volumes that have yet to be purged from the VAG. 
    :type deleted_volumes: int

    :param volume_access_group_id: [required] Unique ID for this volume access group. 
    :type volume_access_group_id: int

    :param name: [required] Name of the volume access group. 
    :type name: str

    :param initiator_ids: [required] A list of IDs of initiators that are mapped to the VAG. 
    :type initiator_ids: int

    :param initiators: [required] List of unique initiator names beintegering to the volume access group. 
    :type initiators: str

    :param volumes: [required] List of volumes beintegering to the volume access group. 
    :type volumes: int

    :param attributes: [required] List of name/value pairs 
    :type attributes: dict

    """
    deleted_volumes = data_model.property(
        "deletedVolumes", int,
        array=True, optional=False,
        documentation="""A list of deleted volumes that have yet to be purged from the VAG. """,
        dictionaryType=None
    )
    volume_access_group_id = data_model.property(
        "volumeAccessGroupID", int,
        array=False, optional=False,
        documentation="""Unique ID for this volume access group. """,
        dictionaryType=None
    )
    name = data_model.property(
        "name", str,
        array=False, optional=False,
        documentation="""Name of the volume access group. """,
        dictionaryType=None
    )
    initiator_ids = data_model.property(
        "initiatorIDs", int,
        array=True, optional=False,
        documentation="""A list of IDs of initiators that are mapped to the VAG. """,
        dictionaryType=None
    )
    initiators = data_model.property(
        "initiators", str,
        array=True, optional=False,
        documentation="""List of unique initiator names beintegering to the volume access group. """,
        dictionaryType=None
    )
    volumes = data_model.property(
        "volumes", int,
        array=True, optional=False,
        documentation="""List of volumes beintegering to the volume access group. """,
        dictionaryType=None
    )
    attributes = data_model.property(
        "attributes", dict,
        array=False, optional=False,
        documentation="""List of name/value pairs """,
        dictionaryType=None
    )

    def __init__(self,
            deleted_volumes,
            volume_access_group_id,
            name,
            initiator_ids,
            initiators,
            volumes,
            attributes):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class CreateVolumeAccessGroupResult(data_model.DataObject):
    """CreateVolumeAccessGroupResult  

    :param volume_access_group_id: [required] The ID for the newly-created volume access group. 
    :type volume_access_group_id: int

    :param volume_access_group:   
    :type volume_access_group: VolumeAccessGroup

    """
    volume_access_group_id = data_model.property(
        "volumeAccessGroupID", int,
        array=False, optional=False,
        documentation="""The ID for the newly-created volume access group. """,
        dictionaryType=None
    )
    volume_access_group = data_model.property(
        "volumeAccessGroup", VolumeAccessGroup,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )

    def __init__(self,
            volume_access_group_id,
            volume_access_group=None):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class CreateStorageContainerRequest(data_model.DataObject):
    """CreateStorageContainerRequest  
    CreateStorageContainer enables you to create a Virtual Volume (VVol) storage container. Storage containers are associated with a SolidFire storage system account, and are used for reporting and resource allocation. Storage containers can only be associated with virtual volumes. You need at least one storage container to use the Virtual Volumes feature.

    :param name: [required] The name of the storage container. Follows SolidFire account naming restrictions. 
    :type name: str

    :param initiator_secret:  The secret for CHAP authentication for the initiator. 
    :type initiator_secret: str

    :param target_secret:  The secret for CHAP authentication for the target. 
    :type target_secret: str

    :param account_id:  Non-storage container account that will become a storage container. 
    :type account_id: int

    """
    name = data_model.property(
        "name", str,
        array=False, optional=False,
        documentation="""The name of the storage container. Follows SolidFire account naming restrictions. """,
        dictionaryType=None
    )
    initiator_secret = data_model.property(
        "initiatorSecret", str,
        array=False, optional=True,
        documentation="""The secret for CHAP authentication for the initiator. """,
        dictionaryType=None
    )
    target_secret = data_model.property(
        "targetSecret", str,
        array=False, optional=True,
        documentation="""The secret for CHAP authentication for the target. """,
        dictionaryType=None
    )
    account_id = data_model.property(
        "accountID", int,
        array=False, optional=True,
        documentation="""Non-storage container account that will become a storage container. """,
        dictionaryType=None
    )

    def __init__(self,
            name,
            initiator_secret=None,
            target_secret=None,
            account_id=None):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class AddVirtualNetworkResult(data_model.DataObject):
    """AddVirtualNetworkResult  

    :param virtual_network_id:  The virtual network ID of the new virtual network. 
    :type virtual_network_id: int

    """
    virtual_network_id = data_model.property(
        "virtualNetworkID", int,
        array=False, optional=True,
        documentation="""The virtual network ID of the new virtual network. """,
        dictionaryType=None
    )

    def __init__(self,
            virtual_network_id=None):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class AddNodesRequest(data_model.DataObject):
    """AddNodesRequest  
    AddNodes enables you to add one or more new nodes to a cluster. When a node that is not configured starts up for the first time, you are prompted to configure the node. After you configure the node, it is registered as a "pending node" with the cluster. 
    Note: It might take several seconds after adding a new node for it to start up and register its drives as available.

    :param pending_nodes: [required]  List of pending NodeIDs for the nodes to be added. You can  obtain the list of pending nodes using the ListPendingNodes method. 
    :type pending_nodes: int

    :param auto_install:  Whether these nodes should be autoinstalled 
    :type auto_install: bool

    """
    pending_nodes = data_model.property(
        "pendingNodes", int,
        array=True, optional=False,
        documentation=""" List of pending NodeIDs for the nodes to be added. You can  obtain the list of pending nodes using the ListPendingNodes method. """,
        dictionaryType=None
    )
    auto_install = data_model.property(
        "autoInstall", bool,
        array=False, optional=True,
        documentation="""Whether these nodes should be autoinstalled """,
        dictionaryType=None
    )

    def __init__(self,
            pending_nodes,
            auto_install=None):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class RtfiInfo(data_model.DataObject):
    """RtfiInfo  

    :param mipi:   
    :type mipi: str

    :param generation: [required]  
    :type generation: str

    :param status_url_logfile:   
    :type status_url_logfile: str

    :param build: [required]  
    :type build: str

    :param status_url_all: [required]  
    :type status_url_all: str

    :param generation_next:   
    :type generation_next: int

    :param mip:   
    :type mip: str

    :param status_url_current: [required]  
    :type status_url_current: str

    :param options:   
    :type options: dict

    """
    mipi = data_model.property(
        "mipi", str,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )
    generation = data_model.property(
        "generation", str,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    status_url_logfile = data_model.property(
        "statusUrlLogfile", str,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )
    build = data_model.property(
        "build", str,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    status_url_all = data_model.property(
        "statusUrlAll", str,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    generation_next = data_model.property(
        "generationNext", int,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )
    mip = data_model.property(
        "mip", str,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )
    status_url_current = data_model.property(
        "statusUrlCurrent", str,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    options = data_model.property(
        "options", dict,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )

    def __init__(self,
            generation,
            build,
            status_url_all,
            status_url_current,
            mipi=None,
            status_url_logfile=None,
            generation_next=None,
            mip=None,
            options=None):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class ResetNodeDetails(data_model.DataObject):
    """ResetNodeDetails  

    :param rtfi_info: [required]  
    :type rtfi_info: RtfiInfo

    """
    rtfi_info = data_model.property(
        "rtfiInfo", RtfiInfo,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )

    def __init__(self,
            rtfi_info):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class ResetNodeResult(data_model.DataObject):
    """ResetNodeResult  

    :param details:   
    :type details: ResetNodeDetails

    :param duration:   
    :type duration: str

    :param result:   
    :type result: str

    """
    details = data_model.property(
        "details", ResetNodeDetails,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )
    duration = data_model.property(
        "duration", str,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )
    result = data_model.property(
        "result", str,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )

    def __init__(self,
            details=None,
            duration=None,
            result=None):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class EnableLdapAuthenticationRequest(data_model.DataObject):
    """EnableLdapAuthenticationRequest  
    The EnableLdapAuthentication method enables you to configure an LDAP directory connection to use for LDAP authentication to a cluster. Users that are members of the LDAP directory can then log in to the storage system using their LDAP credentials.

    :param auth_type:  Identifies which user authentication method to use. Must be one of the following: DirectBind SearchAndBind 
    :type auth_type: str

    :param group_search_base_dn:  The base DN of the tree to start the group search (will do a subtree search from here). 
    :type group_search_base_dn: str

    :param group_search_custom_filter:  For use with the CustomFilter search type, an LDAP filter to use to return the DNs of a users groups. The string can have placeholder text of %USERNAME% and %USERDN% to be replaced with their username and full userDN as needed. 
    :type group_search_custom_filter: str

    :param group_search_type:  Controls the default group search filter used, and must be one of the following: NoGroups: No group support. ActiveDirectory: Nested membership of all of a users AD groups. MemberDN: MemberDN style groups (single level). 
    :type group_search_type: str

    :param search_bind_dn:  A fully qualified DN to log in with to perform an LDAP search for the user (needs read access to the LDAP directory). 
    :type search_bind_dn: str

    :param search_bind_password:  The password for the searchBindDN account used for searching. 
    :type search_bind_password: str

    :param server_uris: [required] A comma-separated list of LDAP server URIs (examples: "ldap://1.2.3.4" and ldaps://1.2.3.4:123") 
    :type server_uris: str

    :param user_dntemplate:  A string that is used to form a fully qualified user DN. The string should have the placeholder text %USERNAME%, which is replaced with the username of the authenticating user. 
    :type user_dntemplate: str

    :param user_search_base_dn:  The base DN of the tree to start the search (will do a subtree search from here). 
    :type user_search_base_dn: str

    :param user_search_filter:  The LDAP filter to use. The string should have the placeholder text %USERNAME% which is replaced with the username of the authenticating user. Example: (&(objectClass=person)(sAMAccountName=%USERNAME%)) will use the sAMAccountName field in Active Directory to match the username entered at cluster login. 
    :type user_search_filter: str

    """
    auth_type = data_model.property(
        "authType", str,
        array=False, optional=True,
        documentation="""Identifies which user authentication method to use. Must be one of the following: DirectBind SearchAndBind """,
        dictionaryType=None
    )
    group_search_base_dn = data_model.property(
        "groupSearchBaseDN", str,
        array=False, optional=True,
        documentation="""The base DN of the tree to start the group search (will do a subtree search from here). """,
        dictionaryType=None
    )
    group_search_custom_filter = data_model.property(
        "groupSearchCustomFilter", str,
        array=False, optional=True,
        documentation="""For use with the CustomFilter search type, an LDAP filter to use to return the DNs of a users groups. The string can have placeholder text of %USERNAME% and %USERDN% to be replaced with their username and full userDN as needed. """,
        dictionaryType=None
    )
    group_search_type = data_model.property(
        "groupSearchType", str,
        array=False, optional=True,
        documentation="""Controls the default group search filter used, and must be one of the following: NoGroups: No group support. ActiveDirectory: Nested membership of all of a users AD groups. MemberDN: MemberDN style groups (single level). """,
        dictionaryType=None
    )
    search_bind_dn = data_model.property(
        "searchBindDN", str,
        array=False, optional=True,
        documentation="""A fully qualified DN to log in with to perform an LDAP search for the user (needs read access to the LDAP directory). """,
        dictionaryType=None
    )
    search_bind_password = data_model.property(
        "searchBindPassword", str,
        array=False, optional=True,
        documentation="""The password for the searchBindDN account used for searching. """,
        dictionaryType=None
    )
    server_uris = data_model.property(
        "serverURIs", str,
        array=True, optional=False,
        documentation="""A comma-separated list of LDAP server URIs (examples: "ldap://1.2.3.4" and ldaps://1.2.3.4:123") """,
        dictionaryType=None
    )
    user_dntemplate = data_model.property(
        "userDNTemplate", str,
        array=False, optional=True,
        documentation="""A string that is used to form a fully qualified user DN. The string should have the placeholder text %USERNAME%, which is replaced with the username of the authenticating user. """,
        dictionaryType=None
    )
    user_search_base_dn = data_model.property(
        "userSearchBaseDN", str,
        array=False, optional=True,
        documentation="""The base DN of the tree to start the search (will do a subtree search from here). """,
        dictionaryType=None
    )
    user_search_filter = data_model.property(
        "userSearchFilter", str,
        array=False, optional=True,
        documentation="""The LDAP filter to use. The string should have the placeholder text %USERNAME% which is replaced with the username of the authenticating user. Example: (&(objectClass=person)(sAMAccountName=%USERNAME%)) will use the sAMAccountName field in Active Directory to match the username entered at cluster login. """,
        dictionaryType=None
    )

    def __init__(self,
            server_uris,
            auth_type=None,
            group_search_base_dn=None,
            group_search_custom_filter=None,
            group_search_type=None,
            search_bind_dn=None,
            search_bind_password=None,
            user_dntemplate=None,
            user_search_base_dn=None,
            user_search_filter=None):
        kwargs = locals()
        del kwargs["self"]
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
        documentation="""Name of the cluster. """,
        dictionaryType=None
    )
    state = data_model.property(
        "state", str,
        array=False, optional=False,
        documentation="""<strong>Available:</strong> Node has not been configured with a cluster name.<br><strong>Pending:</strong> Node is pending for a specific named cluster and can be added.<br><strong>Active:</strong> Node is active and a member of a cluster and may not be added to another cluster. """,
        dictionaryType=None
    )

    def __init__(self,
            cluster,
            state):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class NodeStateResult(data_model.DataObject):
    """NodeStateResult  

    :param node_id: [required] ID of the node. 
    :type node_id: int

    :param result:  NodeStateInfo object. 
    :type result: NodeStateInfo

    """
    node_id = data_model.property(
        "nodeID", int,
        array=False, optional=False,
        documentation="""ID of the node. """,
        dictionaryType=None
    )
    result = data_model.property(
        "result", NodeStateInfo,
        array=False, optional=True,
        documentation="""NodeStateInfo object. """,
        dictionaryType=None
    )

    def __init__(self,
            node_id,
            result=None):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class GetClusterStateResult(data_model.DataObject):
    """GetClusterStateResult  

    :param nodes:  Array of NodeStateResult objects for each node in the cluster. 
    :type nodes: NodeStateResult

    :param cluster:   
    :type cluster: str

    :param state:   
    :type state: str

    """
    nodes = data_model.property(
        "nodes", NodeStateResult,
        array=True, optional=True,
        documentation="""Array of NodeStateResult objects for each node in the cluster. """,
        dictionaryType=None
    )
    cluster = data_model.property(
        "cluster", str,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )
    state = data_model.property(
        "state", str,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )

    def __init__(self,
            nodes=None,
            cluster=None,
            state=None):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class EnableEncryptionAtRestResult(data_model.DataObject):
    """EnableEncryptionAtRestResult  

    """

    def __init__(self):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class ModifyBackupTargetResult(data_model.DataObject):
    """ModifyBackupTargetResult  

    """

    def __init__(self):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class CancelCloneRequest(data_model.DataObject):
    """CancelCloneRequest  
    CancelClone enables you to stop an ongoing CloneVolume or CopyVolume process. When you cancel a group clone operation, the
    system completes and removes the operation's associated asyncHandle.

    :param clone_id: [required] The cloneID for the ongoing clone process. 
    :type clone_id: int

    """
    clone_id = data_model.property(
        "cloneID", int,
        array=False, optional=False,
        documentation="""The cloneID for the ongoing clone process. """,
        dictionaryType=None
    )

    def __init__(self,
            clone_id):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class GetAccountResult(data_model.DataObject):
    """GetAccountResult  

    :param account: [required] Account details. 
    :type account: Account

    """
    account = data_model.property(
        "account", Account,
        array=False, optional=False,
        documentation="""Account details. """,
        dictionaryType=None
    )

    def __init__(self,
            account):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class GetAccountByIDRequest(data_model.DataObject):
    """GetAccountByIDRequest  
    GetAccountByID enables you to return details about a specific account, given its accountID.

    :param account_id: [required] Specifies the account for which details are gathered. 
    :type account_id: int

    """
    account_id = data_model.property(
        "accountID", int,
        array=False, optional=False,
        documentation="""Specifies the account for which details are gathered. """,
        dictionaryType=None
    )

    def __init__(self,
            account_id):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class TestConnectEnsembleRequest(data_model.DataObject):
    """TestConnectEnsembleRequest  
    The TestConnectEnsemble API method enables you to verify connectivity with a specified database ensemble. By default, it uses the ensemble for the cluster that the node is associated with. Alternatively, you can provide a different ensemble to test connectivity with.
    Note: This method is available only through the per-node API endpoint 5.0 or later.

    :param ensemble:  Uses a comma-separated list of ensemble node cluster IP addresses to test connectivity. This parameter is optional. 
    :type ensemble: str

    """
    ensemble = data_model.property(
        "ensemble", str,
        array=False, optional=True,
        documentation="""Uses a comma-separated list of ensemble node cluster IP addresses to test connectivity. This parameter is optional. """,
        dictionaryType=None
    )

    def __init__(self,
            ensemble=None):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class RollbackToSnapshotResult(data_model.DataObject):
    """RollbackToSnapshotResult  

    :param snapshot:   
    :type snapshot: Snapshot

    :param snapshot_id:  ID of the newly-created snapshot. 
    :type snapshot_id: int

    :param checksum:  A string that represents the correct digits in the stored snapshot. This checksum can be used later to compare other snapshots to detect errors in the data. 
    :type checksum: str

    """
    snapshot = data_model.property(
        "snapshot", Snapshot,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )
    snapshot_id = data_model.property(
        "snapshotID", int,
        array=False, optional=True,
        documentation="""ID of the newly-created snapshot. """,
        dictionaryType=None
    )
    checksum = data_model.property(
        "checksum", str,
        array=False, optional=True,
        documentation="""A string that represents the correct digits in the stored snapshot. This checksum can be used later to compare other snapshots to detect errors in the data. """,
        dictionaryType=None
    )

    def __init__(self,
            snapshot=None,
            snapshot_id=None,
            checksum=None):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class GetSystemStatusResult(data_model.DataObject):
    """GetSystemStatusResult  

    :param reboot_required: [required]  
    :type reboot_required: bool

    """
    reboot_required = data_model.property(
        "rebootRequired", bool,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )

    def __init__(self,
            reboot_required):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class GetClusterHardwareInfoRequest(data_model.DataObject):
    """GetClusterHardwareInfoRequest  
    You can use the GetClusterHardwareInfo method to retrieve the hardware status and information for all Fibre Channel nodes, iSCSI
    nodes and drives in the cluster. This generally includes details about manufacturers, vendors, versions, and other associated hardware
    identification information.

    :param type:  Includes only a certain type of hardware information in the response. Possible values are: drives: List only drive information in the response. nodes: List only node information in the response. all: Include both drive and node information in the response. If this parameter is omitted, a type of "all" is assumed. 
    :type type: str

    """
    type = data_model.property(
        "type", str,
        array=False, optional=True,
        documentation="""Includes only a certain type of hardware information in the response. Possible values are: drives: List only drive information in the response. nodes: List only node information in the response. all: Include both drive and node information in the response. If this parameter is omitted, a type of "all" is assumed. """,
        dictionaryType=None
    )

    def __init__(self,
            type=None):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class RemoveBackupTargetRequest(data_model.DataObject):
    """RemoveBackupTargetRequest  
    RemoveBackupTarget allows you to delete backup targets.

    :param backup_target_id: [required] The unique target ID of the target to remove. 
    :type backup_target_id: int

    """
    backup_target_id = data_model.property(
        "backupTargetID", int,
        array=False, optional=False,
        documentation="""The unique target ID of the target to remove. """,
        dictionaryType=None
    )

    def __init__(self,
            backup_target_id):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class CreateVolumeRequest(data_model.DataObject):
    """CreateVolumeRequest  
    CreateVolume enables you to create a new (empty) volume on the cluster. As soon as the volume creation is complete, the volume is
    available for connection via iSCSI.

    :param name: [required] The name of the volume access group (might be user specified). Not required to be unique, but recommended. Might be 1 to 64 characters in length. 
    :type name: str

    :param account_id: [required] AccountID for the owner of this volume. 
    :type account_id: int

    :param total_size: [required] Total size of the volume, in bytes. Size is rounded up to the nearest 1MB size. 
    :type total_size: int

    :param enable512e: [required] Specifies whether 512e emulation is enabled or not. Possible values are: true: The volume provides 512-byte sector emulation. false: 512e emulation is not enabled. 
    :type enable512e: bool

    :param qos:  Initial quality of service settings for this volume. Default values are used if none are specified. Valid settings are: minIOPS maxIOPS burstIOPS You can get the default values for a volume by using the GetDefaultQoS method. 
    :type qos: QoS

    :param attributes:  The list of name-value pairs in JSON object format. Total attribute size must be less than 1000B, or 1KB, including JSON formatting characters. 
    :type attributes: dict

    :param associate_with_qos_policy:  Associate the volume with the specified QoS policy. Possible values: true: Associate the volume with the QoS policy specified in the QoSPolicyID parameter. false: Do not assosciate the volume with the QoS policy specified in the QoSPolicyID parameter. When false, any existing policy association is removed regardless of whether you specify a QoS policy in the QoSPolicyID parameter. 
    :type associate_with_qos_policy: bool

    :param qos_policy_id:  The ID for the policy whose QoS settings should be applied to the specified volumes. This parameter is mutually exclusive with the qos parameter. 
    :type qos_policy_id: int

    """
    name = data_model.property(
        "name", str,
        array=False, optional=False,
        documentation="""The name of the volume access group (might be user specified). Not required to be unique, but recommended. Might be 1 to 64 characters in length. """,
        dictionaryType=None
    )
    account_id = data_model.property(
        "accountID", int,
        array=False, optional=False,
        documentation="""AccountID for the owner of this volume. """,
        dictionaryType=None
    )
    total_size = data_model.property(
        "totalSize", int,
        array=False, optional=False,
        documentation="""Total size of the volume, in bytes. Size is rounded up to the nearest 1MB size. """,
        dictionaryType=None
    )
    enable512e = data_model.property(
        "enable512e", bool,
        array=False, optional=False,
        documentation="""Specifies whether 512e emulation is enabled or not. Possible values are: true: The volume provides 512-byte sector emulation. false: 512e emulation is not enabled. """,
        dictionaryType=None
    )
    qos = data_model.property(
        "qos", QoS,
        array=False, optional=True,
        documentation="""Initial quality of service settings for this volume. Default values are used if none are specified. Valid settings are: minIOPS maxIOPS burstIOPS You can get the default values for a volume by using the GetDefaultQoS method. """,
        dictionaryType=None
    )
    attributes = data_model.property(
        "attributes", dict,
        array=False, optional=True,
        documentation="""The list of name-value pairs in JSON object format. Total attribute size must be less than 1000B, or 1KB, including JSON formatting characters. """,
        dictionaryType=None
    )
    associate_with_qos_policy = data_model.property(
        "associateWithQoSPolicy", bool,
        array=False, optional=True,
        documentation="""Associate the volume with the specified QoS policy. Possible values: true: Associate the volume with the QoS policy specified in the QoSPolicyID parameter. false: Do not assosciate the volume with the QoS policy specified in the QoSPolicyID parameter. When false, any existing policy association is removed regardless of whether you specify a QoS policy in the QoSPolicyID parameter. """,
        dictionaryType=None
    )
    qos_policy_id = data_model.property(
        "qosPolicyID", int,
        array=False, optional=True,
        documentation="""The ID for the policy whose QoS settings should be applied to the specified volumes. This parameter is mutually exclusive with the qos parameter. """,
        dictionaryType=None
    )

    def __init__(self,
            name,
            account_id,
            total_size,
            enable512e,
            qos=None,
            attributes=None,
            associate_with_qos_policy=None,
            qos_policy_id=None):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class CreateClusterResult(data_model.DataObject):
    """CreateClusterResult  

    """

    def __init__(self):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class SetConfigRequest(data_model.DataObject):
    """SetConfigRequest  
    The SetConfig API method enables you to set all the configuration information for the node. This includes the same information available via calls to SetClusterConfig and SetNetworkConfig in one API method. 
    Note: This method is available only through the per-node API endpoint 5.0 or later.
    Caution: Changing the "bond-mode" on a node can cause a temporary loss of network connectivity. Exercise caution when using this method.

    :param config: [required] Objects that you want changed for the cluster interface settings. 
    :type config: ConfigParams

    """
    config = data_model.property(
        "config", ConfigParams,
        array=False, optional=False,
        documentation="""Objects that you want changed for the cluster interface settings. """,
        dictionaryType=None
    )

    def __init__(self,
            config):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class ModifyVolumesRequest(data_model.DataObject):
    """ModifyVolumesRequest  
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

    :param associate_with_qos_policy:  Associate the volume with the specified QoS policy. Possible values: true: Associate the volume with the QoS policy specified in the QoSPolicyID parameter. false: Do not assosciate the volume with the QoS policy specified in the QoSPolicyID parameter. When false, any existing policy association is removed regardless of whether you specify a QoS policy in the QoSPolicyID parameter. 
    :type associate_with_qos_policy: bool

    :param qos_policy_id:  The ID for the policy whose QoS settings should be applied to the specified volumes. This parameter is mutually exclusive with the qos parameter. 
    :type qos_policy_id: int

    :param attributes:  List of name/value pairs in JSON object format. 
    :type attributes: dict

    """
    volume_ids = data_model.property(
        "volumeIDs", int,
        array=True, optional=False,
        documentation="""A list of volumeIDs for the volumes to be modified. """,
        dictionaryType=None
    )
    account_id = data_model.property(
        "accountID", int,
        array=False, optional=True,
        documentation="""AccountID to which the volume is reassigned. If none is specified, the previous account name is used. """,
        dictionaryType=None
    )
    access = data_model.property(
        "access", str,
        array=False, optional=True,
        documentation="""Access allowed for the volume. Possible values:readOnly: Only read operations are allowed.readWrite: Reads and writes are allowed.locked: No reads or writes are allowed.If not specified, the access value does not change.replicationTarget: Identify a volume as the target volume for a paired set of volumes. If the volume is not paired, the access status is locked.If a value is not specified, the access value does not change.  """,
        dictionaryType=None
    )
    qos = data_model.property(
        "qos", QoS,
        array=False, optional=True,
        documentation="""New quality of service settings for this volume.If not specified, the QoS settings are not changed. """,
        dictionaryType=None
    )
    total_size = data_model.property(
        "totalSize", int,
        array=False, optional=True,
        documentation="""New size of the volume in bytes. 1000000000 is equal to 1GB. Size is rounded up to the nearest 1MB in size. This parameter can only be used to increase the size of a volume. """,
        dictionaryType=None
    )
    associate_with_qos_policy = data_model.property(
        "associateWithQoSPolicy", bool,
        array=False, optional=True,
        documentation="""Associate the volume with the specified QoS policy. Possible values: true: Associate the volume with the QoS policy specified in the QoSPolicyID parameter. false: Do not assosciate the volume with the QoS policy specified in the QoSPolicyID parameter. When false, any existing policy association is removed regardless of whether you specify a QoS policy in the QoSPolicyID parameter. """,
        dictionaryType=None
    )
    qos_policy_id = data_model.property(
        "qosPolicyID", int,
        array=False, optional=True,
        documentation="""The ID for the policy whose QoS settings should be applied to the specified volumes. This parameter is mutually exclusive with the qos parameter. """,
        dictionaryType=None
    )
    attributes = data_model.property(
        "attributes", dict,
        array=False, optional=True,
        documentation="""List of name/value pairs in JSON object format. """,
        dictionaryType=None
    )

    def __init__(self,
            volume_ids,
            account_id=None,
            access=None,
            qos=None,
            total_size=None,
            associate_with_qos_policy=None,
            qos_policy_id=None,
            attributes=None):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class ListPendingNodesResult(data_model.DataObject):
    """ListPendingNodesResult  

    :param pending_nodes: [required]  
    :type pending_nodes: PendingNode

    """
    pending_nodes = data_model.property(
        "pendingNodes", PendingNode,
        array=True, optional=False,
        documentation=""" """,
        dictionaryType=None
    )

    def __init__(self,
            pending_nodes):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class CancelGroupCloneResult(data_model.DataObject):
    """CancelGroupCloneResult  

    """

    def __init__(self):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class ListActivePairedVolumesResult(data_model.DataObject):
    """ListActivePairedVolumesResult  

    :param volumes: [required] Volume information for the paired volumes. 
    :type volumes: Volume

    """
    volumes = data_model.property(
        "volumes", Volume,
        array=True, optional=False,
        documentation="""Volume information for the paired volumes. """,
        dictionaryType=None
    )

    def __init__(self,
            volumes):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class RestoreDeletedVolumeRequest(data_model.DataObject):
    """RestoreDeletedVolumeRequest  
    RestoreDeletedVolume marks a deleted volume as active again. This action makes the volume immediately available for iSCSI connection.

    :param volume_id: [required] VolumeID of the deleted volume to be restored. 
    :type volume_id: int

    """
    volume_id = data_model.property(
        "volumeID", int,
        array=False, optional=False,
        documentation="""VolumeID of the deleted volume to be restored. """,
        dictionaryType=None
    )

    def __init__(self,
            volume_id):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class SetNtpInfoRequest(data_model.DataObject):
    """SetNtpInfoRequest  
    SetNtpInfo enables you to configure NTP on cluster nodes. The values you set with this interface apply to all nodes in the cluster. If an NTP broadcast server periodically broadcasts time information on your network, you can optionally configure nodes as broadcast clients.
    Note: NetApp recommends using NTP servers that are internal to your network, rather than the installation defaults.

    :param servers: [required] List of NTP servers to add to each nodes NTP configuration. 
    :type servers: str

    :param broadcastclient:  Enables every node in the cluster as a broadcast client. 
    :type broadcastclient: bool

    """
    servers = data_model.property(
        "servers", str,
        array=True, optional=False,
        documentation="""List of NTP servers to add to each nodes NTP configuration. """,
        dictionaryType=None
    )
    broadcastclient = data_model.property(
        "broadcastclient", bool,
        array=False, optional=True,
        documentation="""Enables every node in the cluster as a broadcast client. """,
        dictionaryType=None
    )

    def __init__(self,
            servers,
            broadcastclient=None):
        kwargs = locals()
        del kwargs["self"]
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
        documentation="""A string of characters that is used by the "CompleteClusterPairing" API method. """,
        dictionaryType=None
    )
    cluster_pair_id = data_model.property(
        "clusterPairID", int,
        array=False, optional=False,
        documentation="""Unique identifier for the cluster pair. """,
        dictionaryType=None
    )

    def __init__(self,
            cluster_pairing_key,
            cluster_pair_id):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class RemoveVolumePairResult(data_model.DataObject):
    """RemoveVolumePairResult  

    """

    def __init__(self):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class RemoveAccountRequest(data_model.DataObject):
    """RemoveAccountRequest  
    RemoveAccount enables you to remove an existing account. You must delete and purge all volumes associated with the account
    using DeleteVolume before you can remove the account. If volumes on the account are still pending deletion, you cannot use
    RemoveAccount to remove the account.

    :param account_id: [required] Specifies the AccountID for the account to be removed. 
    :type account_id: int

    """
    account_id = data_model.property(
        "accountID", int,
        array=False, optional=False,
        documentation="""Specifies the AccountID for the account to be removed. """,
        dictionaryType=None
    )

    def __init__(self,
            account_id):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class CreateStorageContainerResult(data_model.DataObject):
    """CreateStorageContainerResult  

    :param storage_container: [required]  
    :type storage_container: StorageContainer

    """
    storage_container = data_model.property(
        "storageContainer", StorageContainer,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )

    def __init__(self,
            storage_container):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class DeleteGroupSnapshotResult(data_model.DataObject):
    """DeleteGroupSnapshotResult  

    """

    def __init__(self):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class GetVirtualVolumeCountResult(data_model.DataObject):
    """GetVirtualVolumeCountResult  

    :param count: [required] The number of virtual volumes currently in the system. 
    :type count: int

    """
    count = data_model.property(
        "count", int,
        array=False, optional=False,
        documentation="""The number of virtual volumes currently in the system. """,
        dictionaryType=None
    )

    def __init__(self,
            count):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class ListGroupSnapshotsResult(data_model.DataObject):
    """ListGroupSnapshotsResult  

    :param group_snapshots: [required] List of Group Snapshots. 
    :type group_snapshots: GroupSnapshot

    """
    group_snapshots = data_model.property(
        "groupSnapshots", GroupSnapshot,
        array=True, optional=False,
        documentation="""List of Group Snapshots. """,
        dictionaryType=None
    )

    def __init__(self,
            group_snapshots):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class GetNvramInfoRequest(data_model.DataObject):
    """GetNvramInfoRequest  
    GetNvramInfo enables you to retrieve information from each node about the NVRAM card.

    :param force:  Required parameter to successfully run on all nodes in the cluster. 
    :type force: bool

    """
    force = data_model.property(
        "force", bool,
        array=False, optional=True,
        documentation="""Required parameter to successfully run on all nodes in the cluster. """,
        dictionaryType=None
    )

    def __init__(self,
            force=None):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class GetVolumeEfficiencyResult(data_model.DataObject):
    """GetVolumeEfficiencyResult  

    :param compression:  The amount of space being saved by compressing data on a single volume. Stated as a ratio where "1" means data has been stored without being compressed. 
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
        array=False, optional=True,
        documentation="""The amount of space being saved by compressing data on a single volume. Stated as a ratio where "1" means data has been stored without being compressed. """,
        dictionaryType=None
    )
    deduplication = data_model.property(
        "deduplication", float,
        array=False, optional=False,
        documentation="""The amount of space being saved on a single volume by not duplicating data. Stated as a ratio. """,
        dictionaryType=None
    )
    missing_volumes = data_model.property(
        "missingVolumes", int,
        array=True, optional=False,
        documentation="""The volumes that could not be queried for efficiency data. Missing volumes can be caused by GC being less than hour old, temporary network loss or restarted services since the GC cycle. """,
        dictionaryType=None
    )
    thin_provisioning = data_model.property(
        "thinProvisioning", float,
        array=False, optional=False,
        documentation="""The ratio of space used to the amount of space allocated for storing data. Stated as a ratio. """,
        dictionaryType=None
    )
    timestamp = data_model.property(
        "timestamp", str,
        array=False, optional=False,
        documentation="""The last time efficiency data was collected after Garbage Collection (GC). """,
        dictionaryType=None
    )

    def __init__(self,
            deduplication,
            missing_volumes,
            thin_provisioning,
            timestamp,
            compression=None):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class PendingOperation(data_model.DataObject):
    """PendingOperation  

    :param pending: [required] true: operation is still in progress. false: operation is no integerer in progress. 
    :type pending: bool

    :param operation: [required] Name of operation that is in progress or has completed. 
    :type operation: str

    """
    pending = data_model.property(
        "pending", bool,
        array=False, optional=False,
        documentation="""true: operation is still in progress. false: operation is no integerer in progress. """,
        dictionaryType=None
    )
    operation = data_model.property(
        "operation", str,
        array=False, optional=False,
        documentation="""Name of operation that is in progress or has completed. """,
        dictionaryType=None
    )

    def __init__(self,
            pending,
            operation):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class GetPendingOperationResult(data_model.DataObject):
    """GetPendingOperationResult  

    :param pending_operation: [required]  
    :type pending_operation: PendingOperation

    """
    pending_operation = data_model.property(
        "pendingOperation", PendingOperation,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )

    def __init__(self,
            pending_operation):
        kwargs = locals()
        del kwargs["self"]
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
        documentation="""Required parameter for "volumes" array: volumeID. """,
        dictionaryType=None
    )
    access = data_model.property(
        "access", str,
        array=False, optional=True,
        documentation="""Access settings for the new volume. readOnly: Only read operations are allowed. readWrite: Reads and writes are allowed. locked: No reads or writes are allowed. replicationTarget: Identify a volume as the target volume for a paired set of volumes. If the volume is not paired, the access status is locked.  If unspecified, the access settings of the clone will be the same as the source. """,
        dictionaryType=None
    )
    name = data_model.property(
        "name", str,
        array=False, optional=True,
        documentation="""New name for the clone. """,
        dictionaryType=None
    )
    new_account_id = data_model.property(
        "newAccountID", int,
        array=False, optional=True,
        documentation="""Account ID for the new volume. """,
        dictionaryType=None
    )
    new_size = data_model.property(
        "newSize", int,
        array=False, optional=True,
        documentation="""New size Total size of the volume, in bytes. Size is rounded up to the nearest 1MB size. """,
        dictionaryType=None
    )
    attributes = data_model.property(
        "attributes", dict,
        array=False, optional=True,
        documentation="""List of Name/Value pairs in JSON object format. """,
        dictionaryType=None
    )

    def __init__(self,
            volume_id,
            access=None,
            name=None,
            new_account_id=None,
            new_size=None,
            attributes=None):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class SetNtpInfoResult(data_model.DataObject):
    """SetNtpInfoResult  

    """

    def __init__(self):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class GetVolumeAccessGroupEfficiencyRequest(data_model.DataObject):
    """GetVolumeAccessGroupEfficiencyRequest  
    GetVolumeAccessGroupEfficiency enables you to
    retrieve efficiency information about a volume access
    group. Only the volume access group you provide as the
    parameter in this API method is used to compute the
    capacity.

    :param volume_access_group_id: [required] The volume access group for which capacity is computed. 
    :type volume_access_group_id: int

    """
    volume_access_group_id = data_model.property(
        "volumeAccessGroupID", int,
        array=False, optional=False,
        documentation="""The volume access group for which capacity is computed. """,
        dictionaryType=None
    )

    def __init__(self,
            volume_access_group_id):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class ModifyVolumePairResult(data_model.DataObject):
    """ModifyVolumePairResult  

    """

    def __init__(self):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class CreateInitiator(data_model.DataObject):
    """CreateInitiator  
    Object containing characteristics of each new initiator.

    :param name: [required] (Required) The name of the initiator (IQN or WWPN) to create. (String) 
    :type name: str

    :param alias:  (Optional) The friendly name to assign to this initiator. (String) 
    :type alias: str

    :param volume_access_group_id:  (Optional) The ID of the volume access group to which this newly created initiator will be added. (Integer) 
    :type volume_access_group_id: int

    :param attributes:  (Optional) A set of JSON attributes assigned to this initiator. (JSON Object) 
    :type attributes: dict

    """
    name = data_model.property(
        "name", str,
        array=False, optional=False,
        documentation="""(Required) The name of the initiator (IQN or WWPN) to create. (String) """,
        dictionaryType=None
    )
    alias = data_model.property(
        "alias", str,
        array=False, optional=True,
        documentation="""(Optional) The friendly name to assign to this initiator. (String) """,
        dictionaryType=None
    )
    volume_access_group_id = data_model.property(
        "volumeAccessGroupID", int,
        array=False, optional=True,
        documentation="""(Optional) The ID of the volume access group to which this newly created initiator will be added. (Integer) """,
        dictionaryType=None
    )
    attributes = data_model.property(
        "attributes", dict,
        array=False, optional=True,
        documentation="""(Optional) A set of JSON attributes assigned to this initiator. (JSON Object) """,
        dictionaryType=None
    )

    def __init__(self,
            name,
            alias=None,
            volume_access_group_id=None,
            attributes=None):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class CreateInitiatorsRequest(data_model.DataObject):
    """CreateInitiatorsRequest  
    CreateInitiators enables you to create multiple new initiator IQNs or World Wide Port Names (WWPNs) and optionally assign them
    aliases and attributes. When you use CreateInitiators to create new initiators, you can also add them to volume access groups.
    If CreateInitiators fails to create one of the initiators provided in the parameter, the method returns an error and does not create
    any initiators (no partial completion is possible).

    :param initiators: [required] A list of objects containing characteristics of each new initiator. Values are: name: (Required) The name of the initiator (IQN or WWPN) to create. (String) alias: (Optional) The friendly name to assign to this initiator. (String) attributes: (Optional) A set of JSON attributes to assign to this initiator. (JSON Object) volumeAccessGroupID: (Optional) The ID of the volume access group into to which this newly created initiator will be added. (Integer) 
    :type initiators: CreateInitiator

    """
    initiators = data_model.property(
        "initiators", CreateInitiator,
        array=True, optional=False,
        documentation="""A list of objects containing characteristics of each new initiator. Values are: name: (Required) The name of the initiator (IQN or WWPN) to create. (String) alias: (Optional) The friendly name to assign to this initiator. (String) attributes: (Optional) A set of JSON attributes to assign to this initiator. (JSON Object) volumeAccessGroupID: (Optional) The ID of the volume access group into to which this newly created initiator will be added. (Integer) """,
        dictionaryType=None
    )

    def __init__(self,
            initiators):
        kwargs = locals()
        del kwargs["self"]
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
        documentation="""Current computed level of block fullness of the cluster. Possible values: stage1Happy: No alerts or error conditions. stage2Aware: 3 nodes of capacity available. stage3Low: 2 nodes of capacity available. stage4Critical: 1 node of capacity available. No new volumes or clones can be created. stage5CompletelyConsumed: Completely consumed. Cluster is read-only, iSCSI connection is maintained but all writes are suspended. """,
        dictionaryType=None
    )
    fullness = data_model.property(
        "fullness", str,
        array=False, optional=False,
        documentation="""Reflects the highest level of fullness between "blockFullness" and "metadataFullness". """,
        dictionaryType=None
    )
    max_metadata_over_provision_factor = data_model.property(
        "maxMetadataOverProvisionFactor", int,
        array=False, optional=False,
        documentation="""A value representative of the number of times metadata space can be over provisioned relative to the amount of space available. For example, if there was enough metadata space to store 100 TiB of volumes and this number was set to 5, then 500 TiB worth of volumes could be created. """,
        dictionaryType=None
    )
    metadata_fullness = data_model.property(
        "metadataFullness", str,
        array=False, optional=False,
        documentation="""Current computed level of metadata fullness of the cluster. """,
        dictionaryType=None
    )
    slice_reserve_used_threshold_pct = data_model.property(
        "sliceReserveUsedThresholdPct", int,
        array=False, optional=False,
        documentation="""Error condition; message sent to "Alerts" if the reserved slice utilization is greater than the sliceReserveUsedThresholdPct value returned. """,
        dictionaryType=None
    )
    stage2_aware_threshold = data_model.property(
        "stage2AwareThreshold", int,
        array=False, optional=False,
        documentation="""Awareness condition: Value that is set for "Stage 2" cluster threshold level. """,
        dictionaryType=None
    )
    stage2_block_threshold_bytes = data_model.property(
        "stage2BlockThresholdBytes", int,
        array=False, optional=False,
        documentation="""Number of bytes being used by the cluster at which a stage2 condition will exist. """,
        dictionaryType=None
    )
    stage3_block_threshold_bytes = data_model.property(
        "stage3BlockThresholdBytes", int,
        array=False, optional=False,
        documentation="""Number of bytes being used by the cluster at which a stage3 condition will exist. """,
        dictionaryType=None
    )
    stage3_block_threshold_percent = data_model.property(
        "stage3BlockThresholdPercent", int,
        array=False, optional=False,
        documentation="""The percent value set for stage3. At this percent full, a warning will be posted in the Alerts log. """,
        dictionaryType=None
    )
    stage3_low_threshold = data_model.property(
        "stage3LowThreshold", int,
        array=False, optional=False,
        documentation="""Error condition; message sent to "Alerts" that capacity on a cluster is getting low. """,
        dictionaryType=None
    )
    stage4_critical_threshold = data_model.property(
        "stage4CriticalThreshold", int,
        array=False, optional=False,
        documentation="""Error condition; message sent to "Alerts" that capacity on a cluster is critically low. """,
        dictionaryType=None
    )
    stage4_block_threshold_bytes = data_model.property(
        "stage4BlockThresholdBytes", int,
        array=False, optional=False,
        documentation="""Number of bytes being used by the cluster at which a stage4 condition will exist. """,
        dictionaryType=None
    )
    stage5_block_threshold_bytes = data_model.property(
        "stage5BlockThresholdBytes", int,
        array=False, optional=False,
        documentation="""Number of bytes being used by the cluster at which a stage5 condition will exist. """,
        dictionaryType=None
    )
    sum_total_cluster_bytes = data_model.property(
        "sumTotalClusterBytes", int,
        array=False, optional=False,
        documentation="""Physical capacity of the cluster measured in bytes. """,
        dictionaryType=None
    )
    sum_total_metadata_cluster_bytes = data_model.property(
        "sumTotalMetadataClusterBytes", int,
        array=False, optional=False,
        documentation="""Total amount of space that can be used to store metadata. """,
        dictionaryType=None
    )
    sum_used_cluster_bytes = data_model.property(
        "sumUsedClusterBytes", int,
        array=False, optional=False,
        documentation="""Number of bytes used on the cluster. """,
        dictionaryType=None
    )
    sum_used_metadata_cluster_bytes = data_model.property(
        "sumUsedMetadataClusterBytes", int,
        array=False, optional=False,
        documentation="""Amount of space used on volume drives to store metadata. """,
        dictionaryType=None
    )

    def __init__(self,
            block_fullness,
            fullness,
            max_metadata_over_provision_factor,
            metadata_fullness,
            slice_reserve_used_threshold_pct,
            stage2_aware_threshold,
            stage2_block_threshold_bytes,
            stage3_block_threshold_bytes,
            stage3_block_threshold_percent,
            stage3_low_threshold,
            stage4_critical_threshold,
            stage4_block_threshold_bytes,
            stage5_block_threshold_bytes,
            sum_total_cluster_bytes,
            sum_total_metadata_cluster_bytes,
            sum_used_cluster_bytes,
            sum_used_metadata_cluster_bytes):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class ListVolumesForAccountRequest(data_model.DataObject):
    """ListVolumesForAccountRequest  
    ListVolumesForAccount returns the list of active and (pending) deleted volumes for an account.

    :param account_id: [required] Returns all volumes owned by this AccountID. 
    :type account_id: int

    :param start_volume_id:  The ID of the first volume to list. This can be useful for paging results. By default, this starts at the lowest VolumeID. 
    :type start_volume_id: int

    :param limit:  The maximum number of volumes to return from the API. 
    :type limit: int

    :param include_virtual_volumes:  Specifies that virtual volumes are included in the response by default. To exclude virtual volumes, set to false. 
    :type include_virtual_volumes: bool

    """
    account_id = data_model.property(
        "accountID", int,
        array=False, optional=False,
        documentation="""Returns all volumes owned by this AccountID. """,
        dictionaryType=None
    )
    start_volume_id = data_model.property(
        "startVolumeID", int,
        array=False, optional=True,
        documentation="""The ID of the first volume to list. This can be useful for paging results. By default, this starts at the lowest VolumeID. """,
        dictionaryType=None
    )
    limit = data_model.property(
        "limit", int,
        array=False, optional=True,
        documentation="""The maximum number of volumes to return from the API. """,
        dictionaryType=None
    )
    include_virtual_volumes = data_model.property(
        "includeVirtualVolumes", bool,
        array=False, optional=True,
        documentation="""Specifies that virtual volumes are included in the response by default. To exclude virtual volumes, set to false. """,
        dictionaryType=None
    )

    def __init__(self,
            account_id,
            start_volume_id=None,
            limit=None,
            include_virtual_volumes=None):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class DisableEncryptionAtRestResult(data_model.DataObject):
    """DisableEncryptionAtRestResult  

    """

    def __init__(self):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class GetVolumeEfficiencyRequest(data_model.DataObject):
    """GetVolumeEfficiencyRequest  
    GetVolumeEfficiency enables you to retrieve information about a volume. Only the volume you give as a parameter in this API method is used to compute the capacity.

    :param volume_id: [required] Specifies the volume for which capacity is computed. 
    :type volume_id: int

    """
    volume_id = data_model.property(
        "volumeID", int,
        array=False, optional=False,
        documentation="""Specifies the volume for which capacity is computed. """,
        dictionaryType=None
    )

    def __init__(self,
            volume_id):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class ModifyVirtualNetworkRequest(data_model.DataObject):
    """ModifyVirtualNetworkRequest  
    You can use ModifyVirtualNetwork to change the attributes of an existing virtual network. This method enables you to add or remove
    address blocks, change the netmask, or modify the name or description of the virtual network. You can also use it to enable or
    disable namespaces, as well as add or remove a gateway if namespaces are enabled on the virtual network.
    Note: This method requires either the VirtualNetworkID or the VirtualNetworkTag as a parameter, but not both.
    Caution: Enabling or disabling the Routable Storage VLANs functionality for an existing virtual network by changing the
    "namespace" parameter disrupts any traffic handled by the virtual network. NetApp strongly recommends changing the
    "namespace" parameter only during a scheduled maintenance window.

    :param virtual_network_id:  The unique identifier of the virtual network to modify. This is the virtual network ID assigned by the cluster.  Note: This parameter is optional but either virtualNetworkID or virtualNetworkTag must be specified with this API method. 
    :type virtual_network_id: int

    :param virtual_network_tag:  The network tag that identifies the virtual network to modify. Note: This parameter is optional but either virtualNetworkID or virtualNetworkTag must be specified with this API method. 
    :type virtual_network_tag: int

    :param name:  The new name for the virtual network. 
    :type name: str

    :param address_blocks:  The new addressBlock to set for this virtual network. This might contain new address blocks to add to the existing object or omit unused address blocks that need to be removed. Alternatively, you can extend or reduce the size of existing address blocks. You can only increase the size of the starting addressBlocks for a virtual network object; you can never decrease it. Attributes for this parameter are: start: The start of the IP address range. (String) size: The number of IP addresses to include in the block. (Integer) 
    :type address_blocks: AddressBlockParams

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
    virtual_network_id = data_model.property(
        "virtualNetworkID", int,
        array=False, optional=True,
        documentation="""The unique identifier of the virtual network to modify. This is the virtual network ID assigned by the cluster.  Note: This parameter is optional but either virtualNetworkID or virtualNetworkTag must be specified with this API method. """,
        dictionaryType=None
    )
    virtual_network_tag = data_model.property(
        "virtualNetworkTag", int,
        array=False, optional=True,
        documentation="""The network tag that identifies the virtual network to modify. Note: This parameter is optional but either virtualNetworkID or virtualNetworkTag must be specified with this API method. """,
        dictionaryType=None
    )
    name = data_model.property(
        "name", str,
        array=False, optional=True,
        documentation="""The new name for the virtual network. """,
        dictionaryType=None
    )
    address_blocks = data_model.property(
        "addressBlocks", AddressBlockParams,
        array=True, optional=True,
        documentation="""The new addressBlock to set for this virtual network. This might contain new address blocks to add to the existing object or omit unused address blocks that need to be removed. Alternatively, you can extend or reduce the size of existing address blocks. You can only increase the size of the starting addressBlocks for a virtual network object; you can never decrease it. Attributes for this parameter are: start: The start of the IP address range. (String) size: The number of IP addresses to include in the block. (Integer) """,
        dictionaryType=None
    )
    netmask = data_model.property(
        "netmask", str,
        array=False, optional=True,
        documentation="""New network mask for this virtual network. """,
        dictionaryType=None
    )
    svip = data_model.property(
        "svip", str,
        array=False, optional=True,
        documentation="""The storage virtual IP address for this virtual network. The svip for a virtual network cannot be changed. You must create a new virtual network to use a different svip address. """,
        dictionaryType=None
    )
    gateway = data_model.property(
        "gateway", str,
        array=False, optional=True,
        documentation="""The IP address of a gateway of the virtual network. This parameter is only valid if the "namespace" parameter is set to true. """,
        dictionaryType=None
    )
    namespace = data_model.property(
        "namespace", bool,
        array=False, optional=True,
        documentation="""When set to true, enables Routable Storage VLANs functionality by recreating the virtual network and configuring a namespace to contain it. When set to false, disables the VRF functionality for the virtual network. Changing this value disrupts traffic running through this virtual network. """,
        dictionaryType=None
    )
    attributes = data_model.property(
        "attributes", dict,
        array=False, optional=True,
        documentation="""A new list of name-value pairs in JSON object format. """,
        dictionaryType=None
    )

    def __init__(self,
            virtual_network_id=None,
            virtual_network_tag=None,
            name=None,
            address_blocks=None,
            netmask=None,
            svip=None,
            gateway=None,
            namespace=None,
            attributes=None):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class VirtualVolumeStats(data_model.DataObject):
    """VirtualVolumeStats  
    Contains statistical data for an individual volume.

    :param account_id: [required] AccountID of the volume owner. 
    :type account_id: int

    :param actual_iops:  Current actual IOPS to the volume in the last 500 milliseconds. 
    :type actual_iops: int

    :param async_delay:  The length of time since the volume was last synced with the remote cluster. If the volume is not paired, this is null.  Note: A target volume in an active replication state always has an async delay of 0 (zero). Target volumes are system-aware during replication and assume async delay is accurate at all times. 
    :type async_delay: str

    :param average_iopsize:  Average size in bytes of recent I/O to the volume in the last 500 milliseconds. 
    :type average_iopsize: int

    :param burst_iopscredit:  The total number of IOP credits available to the user. When users are not using up to the max IOPS, credits are accrued. 
    :type burst_iopscredit: int

    :param client_queue_depth:  The number of outstanding read and write operations to the cluster. 
    :type client_queue_depth: int

    :param desired_metadata_hosts:  The volume services being migrated to if the volume metadata is getting migrated between volume services. A "null" value means the volume is not migrating. 
    :type desired_metadata_hosts: MetadataHosts

    :param latency_usec:  The observed latency time, in microseconds, to complete operations to a volume. A "0" (zero) value means there is no I/O to the volume. 
    :type latency_usec: int

    :param metadata_hosts:  The volume services on which the volume metadata resides. 
    :type metadata_hosts: MetadataHosts

    :param non_zero_blocks: [required] The number of 4KiB blocks with data after the last garbage collection operation has completed. 
    :type non_zero_blocks: int

    :param read_bytes: [required] Total bytes read by clients. 
    :type read_bytes: int

    :param read_latency_usec:  The average time, in microseconds, to complete read operations. 
    :type read_latency_usec: int

    :param read_ops: [required] Total read operations. 
    :type read_ops: int

    :param throttle:  A floating value between 0 and 1 that represents how much the system is throttling clients below their max IOPS because of re-replication of data, transient errors and snapshots taken. 
    :type throttle: float

    :param timestamp: [required] The current time in UTC. 
    :type timestamp: str

    :param total_latency_usec:  The average time, in microseconds, to complete read and write operations to a volume. 
    :type total_latency_usec: int

    :param unaligned_reads: [required] For 512e volumes, the number of read operations that were not on a 4k sector boundary. High numbers of unaligned reads may indicate improper partition alignment. 
    :type unaligned_reads: int

    :param unaligned_writes: [required] For 512e volumes, the number of write operations that were not on a 4k sector boundary. High numbers of unaligned writes may indicate improper partition alignment. 
    :type unaligned_writes: int

    :param volume_access_groups: [required] List of volume access group(s) to which a volume beintegers. 
    :type volume_access_groups: int

    :param volume_id: [required] Volume ID of the volume. 
    :type volume_id: int

    :param volume_size: [required] Total provisioned capacity in bytes. 
    :type volume_size: int

    :param volume_utilization:  A floating value that describes how much the client is using the volume.  Values:  0 = Client is not using the volume 1 = Client is using their max >1 = Client is using their burst 
    :type volume_utilization: float

    :param write_bytes: [required] Total bytes written by clients. 
    :type write_bytes: int

    :param write_latency_usec:  The average time, in microseconds, to complete write operations. 
    :type write_latency_usec: int

    :param write_ops: [required] Total write operations occurring on the volume. 
    :type write_ops: int

    :param zero_blocks: [required] Total number of 4KiB blocks without data after the last round of garbage collection operation has completed. 
    :type zero_blocks: int

    :param write_bytes_last_sample:  The total number of bytes written to the volume during the last sample period. 
    :type write_bytes_last_sample: int

    :param sample_period_msec:  The length of the sample period in milliseconds. 
    :type sample_period_msec: int

    :param read_bytes_last_sample:  The total number of bytes read from the volume during the last sample period. 
    :type read_bytes_last_sample: int

    :param read_ops_last_sample:  The total number of read operations durin gth elast sample period. 
    :type read_ops_last_sample: int

    :param write_ops_last_sample:  The total number of write operations during the last sample period. 
    :type write_ops_last_sample: int

    :param virtual_volume_id:  If the volume of interest is associated with a virtual volume, this is the virtual volume ID. 
    :type virtual_volume_id: UUID

    """
    account_id = data_model.property(
        "accountID", int,
        array=False, optional=False,
        documentation="""AccountID of the volume owner. """,
        dictionaryType=None
    )
    actual_iops = data_model.property(
        "actualIOPS", int,
        array=False, optional=True,
        documentation="""Current actual IOPS to the volume in the last 500 milliseconds. """,
        dictionaryType=None
    )
    async_delay = data_model.property(
        "asyncDelay", str,
        array=False, optional=True,
        documentation="""The length of time since the volume was last synced with the remote cluster. If the volume is not paired, this is null.  Note: A target volume in an active replication state always has an async delay of 0 (zero). Target volumes are system-aware during replication and assume async delay is accurate at all times. """,
        dictionaryType=None
    )
    average_iopsize = data_model.property(
        "averageIOPSize", int,
        array=False, optional=True,
        documentation="""Average size in bytes of recent I/O to the volume in the last 500 milliseconds. """,
        dictionaryType=None
    )
    burst_iopscredit = data_model.property(
        "burstIOPSCredit", int,
        array=False, optional=True,
        documentation="""The total number of IOP credits available to the user. When users are not using up to the max IOPS, credits are accrued. """,
        dictionaryType=None
    )
    client_queue_depth = data_model.property(
        "clientQueueDepth", int,
        array=False, optional=True,
        documentation="""The number of outstanding read and write operations to the cluster. """,
        dictionaryType=None
    )
    desired_metadata_hosts = data_model.property(
        "desiredMetadataHosts", MetadataHosts,
        array=False, optional=True,
        documentation="""The volume services being migrated to if the volume metadata is getting migrated between volume services. A "null" value means the volume is not migrating. """,
        dictionaryType=None
    )
    latency_usec = data_model.property(
        "latencyUSec", int,
        array=False, optional=True,
        documentation="""The observed latency time, in microseconds, to complete operations to a volume. A "0" (zero) value means there is no I/O to the volume. """,
        dictionaryType=None
    )
    metadata_hosts = data_model.property(
        "metadataHosts", MetadataHosts,
        array=False, optional=True,
        documentation="""The volume services on which the volume metadata resides. """,
        dictionaryType=None
    )
    non_zero_blocks = data_model.property(
        "nonZeroBlocks", int,
        array=False, optional=False,
        documentation="""The number of 4KiB blocks with data after the last garbage collection operation has completed. """,
        dictionaryType=None
    )
    read_bytes = data_model.property(
        "readBytes", int,
        array=False, optional=False,
        documentation="""Total bytes read by clients. """,
        dictionaryType=None
    )
    read_latency_usec = data_model.property(
        "readLatencyUSec", int,
        array=False, optional=True,
        documentation="""The average time, in microseconds, to complete read operations. """,
        dictionaryType=None
    )
    read_ops = data_model.property(
        "readOps", int,
        array=False, optional=False,
        documentation="""Total read operations. """,
        dictionaryType=None
    )
    throttle = data_model.property(
        "throttle", float,
        array=False, optional=True,
        documentation="""A floating value between 0 and 1 that represents how much the system is throttling clients below their max IOPS because of re-replication of data, transient errors and snapshots taken. """,
        dictionaryType=None
    )
    timestamp = data_model.property(
        "timestamp", str,
        array=False, optional=False,
        documentation="""The current time in UTC. """,
        dictionaryType=None
    )
    total_latency_usec = data_model.property(
        "totalLatencyUSec", int,
        array=False, optional=True,
        documentation="""The average time, in microseconds, to complete read and write operations to a volume. """,
        dictionaryType=None
    )
    unaligned_reads = data_model.property(
        "unalignedReads", int,
        array=False, optional=False,
        documentation="""For 512e volumes, the number of read operations that were not on a 4k sector boundary. High numbers of unaligned reads may indicate improper partition alignment. """,
        dictionaryType=None
    )
    unaligned_writes = data_model.property(
        "unalignedWrites", int,
        array=False, optional=False,
        documentation="""For 512e volumes, the number of write operations that were not on a 4k sector boundary. High numbers of unaligned writes may indicate improper partition alignment. """,
        dictionaryType=None
    )
    volume_access_groups = data_model.property(
        "volumeAccessGroups", int,
        array=True, optional=False,
        documentation="""List of volume access group(s) to which a volume beintegers. """,
        dictionaryType=None
    )
    volume_id = data_model.property(
        "volumeID", int,
        array=False, optional=False,
        documentation="""Volume ID of the volume. """,
        dictionaryType=None
    )
    volume_size = data_model.property(
        "volumeSize", int,
        array=False, optional=False,
        documentation="""Total provisioned capacity in bytes. """,
        dictionaryType=None
    )
    volume_utilization = data_model.property(
        "volumeUtilization", float,
        array=False, optional=True,
        documentation="""A floating value that describes how much the client is using the volume.  Values:  0 = Client is not using the volume 1 = Client is using their max >1 = Client is using their burst """,
        dictionaryType=None
    )
    write_bytes = data_model.property(
        "writeBytes", int,
        array=False, optional=False,
        documentation="""Total bytes written by clients. """,
        dictionaryType=None
    )
    write_latency_usec = data_model.property(
        "writeLatencyUSec", int,
        array=False, optional=True,
        documentation="""The average time, in microseconds, to complete write operations. """,
        dictionaryType=None
    )
    write_ops = data_model.property(
        "writeOps", int,
        array=False, optional=False,
        documentation="""Total write operations occurring on the volume. """,
        dictionaryType=None
    )
    zero_blocks = data_model.property(
        "zeroBlocks", int,
        array=False, optional=False,
        documentation="""Total number of 4KiB blocks without data after the last round of garbage collection operation has completed. """,
        dictionaryType=None
    )
    write_bytes_last_sample = data_model.property(
        "writeBytesLastSample", int,
        array=False, optional=True,
        documentation="""The total number of bytes written to the volume during the last sample period. """,
        dictionaryType=None
    )
    sample_period_msec = data_model.property(
        "samplePeriodMSec", int,
        array=False, optional=True,
        documentation="""The length of the sample period in milliseconds. """,
        dictionaryType=None
    )
    read_bytes_last_sample = data_model.property(
        "readBytesLastSample", int,
        array=False, optional=True,
        documentation="""The total number of bytes read from the volume during the last sample period. """,
        dictionaryType=None
    )
    read_ops_last_sample = data_model.property(
        "readOpsLastSample", int,
        array=False, optional=True,
        documentation="""The total number of read operations durin gth elast sample period. """,
        dictionaryType=None
    )
    write_ops_last_sample = data_model.property(
        "writeOpsLastSample", int,
        array=False, optional=True,
        documentation="""The total number of write operations during the last sample period. """,
        dictionaryType=None
    )
    virtual_volume_id = data_model.property(
        "virtualVolumeID", UUID,
        array=False, optional=True,
        documentation="""If the volume of interest is associated with a virtual volume, this is the virtual volume ID. """,
        dictionaryType=None
    )

    def __init__(self,
            account_id,
            non_zero_blocks,
            read_bytes,
            read_ops,
            timestamp,
            unaligned_reads,
            unaligned_writes,
            volume_access_groups,
            volume_id,
            volume_size,
            write_bytes,
            write_ops,
            zero_blocks,
            actual_iops=None,
            async_delay=None,
            average_iopsize=None,
            burst_iopscredit=None,
            client_queue_depth=None,
            desired_metadata_hosts=None,
            latency_usec=None,
            metadata_hosts=None,
            read_latency_usec=None,
            throttle=None,
            total_latency_usec=None,
            volume_utilization=None,
            write_latency_usec=None,
            write_bytes_last_sample=None,
            sample_period_msec=None,
            read_bytes_last_sample=None,
            read_ops_last_sample=None,
            write_ops_last_sample=None,
            virtual_volume_id=None):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class ListVolumeStatsByVirtualVolumeResult(data_model.DataObject):
    """ListVolumeStatsByVirtualVolumeResult  

    :param volume_stats: [required]  
    :type volume_stats: VirtualVolumeStats

    """
    volume_stats = data_model.property(
        "volumeStats", VirtualVolumeStats,
        array=True, optional=False,
        documentation=""" """,
        dictionaryType=None
    )

    def __init__(self,
            volume_stats):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class ListVolumesForAccountResult(data_model.DataObject):
    """ListVolumesForAccountResult  

    :param volumes: [required] List of volumes. 
    :type volumes: Volume

    """
    volumes = data_model.property(
        "volumes", Volume,
        array=True, optional=False,
        documentation="""List of volumes. """,
        dictionaryType=None
    )

    def __init__(self,
            volumes):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class GetNodeHardwareInfoRequest(data_model.DataObject):
    """GetNodeHardwareInfoRequest  
    GetNodeHardwareInfo enables you to return all the hardware information and status for the node specified. This generally includes details about
    manufacturers, vendors, versions, and other associated hardware identification information.

    :param node_id: [required] The ID of the node for which hardware information is being requested. Information about a Fibre Channel node is returned if a Fibre Channel node is specified. 
    :type node_id: int

    """
    node_id = data_model.property(
        "nodeID", int,
        array=False, optional=False,
        documentation="""The ID of the node for which hardware information is being requested. Information about a Fibre Channel node is returned if a Fibre Channel node is specified. """,
        dictionaryType=None
    )

    def __init__(self,
            node_id):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class SecureEraseDrivesRequest(data_model.DataObject):
    """SecureEraseDrivesRequest  
    SecureEraseDrives enables you to remove any residual data from drives that have a status of "available." You might want to use this method when replacing a drive nearing the end of its service life that contained sensitive data. This method uses a Security Erase Unit command to write a predetermined pattern to the drive and resets the encryption key on the drive. This asynchronous method might take up to two minutes to complete. You can use GetAsyncResult to check on the status of the secure erase operation.
    You can use the ListDrives method to obtain the driveIDs for the drives you want to secure erase.

    :param drives: [required] List of driveIDs to be secure erased. 
    :type drives: int

    """
    drives = data_model.property(
        "drives", int,
        array=True, optional=False,
        documentation="""List of driveIDs to be secure erased. """,
        dictionaryType=None
    )

    def __init__(self,
            drives):
        kwargs = locals()
        del kwargs["self"]
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

    :param chassis_slot: [required] For HCI platforms, this value is the node letter and slot number in the server chassis where this drive is located. For legacy platforms, the slot number is a string representation of the 'slot' integer. 
    :type chassis_slot: str

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
        documentation="""Total capacity of the drive, in bytes. """,
        dictionaryType=None
    )
    drive_id = data_model.property(
        "driveID", int,
        array=False, optional=False,
        documentation="""DriveID for this drive. """,
        dictionaryType=None
    )
    node_id = data_model.property(
        "nodeID", int,
        array=False, optional=False,
        documentation="""NodeID where this drive is located. """,
        dictionaryType=None
    )
    serial = data_model.property(
        "serial", str,
        array=False, optional=False,
        documentation="""Drive serial number. """,
        dictionaryType=None
    )
    chassis_slot = data_model.property(
        "chassisSlot", str,
        array=False, optional=False,
        documentation="""For HCI platforms, this value is the node letter and slot number in the server chassis where this drive is located. For legacy platforms, the slot number is a string representation of the 'slot' integer. """,
        dictionaryType=None
    )
    slot = data_model.property(
        "slot", int,
        array=False, optional=False,
        documentation="""Slot number in the server chassis where this drive is located, or -1 if SATADimm used for internal metadata drive. """,
        dictionaryType=None
    )
    status = data_model.property(
        "status", str,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    type = data_model.property(
        "type", str,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    attributes = data_model.property(
        "attributes", dict,
        array=False, optional=False,
        documentation="""List of Name/Value pairs in JSON object format. """,
        dictionaryType=None
    )

    def __init__(self,
            capacity,
            drive_id,
            node_id,
            serial,
            chassis_slot,
            slot,
            status,
            type,
            attributes):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class ListDrivesResult(data_model.DataObject):
    """ListDrivesResult  

    :param drives: [required] Information for the drives that are connected to the cluster. 
    :type drives: DriveInfo

    """
    drives = data_model.property(
        "drives", DriveInfo,
        array=True, optional=False,
        documentation="""Information for the drives that are connected to the cluster. """,
        dictionaryType=None
    )

    def __init__(self,
            drives):
        kwargs = locals()
        del kwargs["self"]
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

    """
    protocol_endpoint_id = data_model.property(
        "protocolEndpointID", UUID,
        array=False, optional=False,
        documentation="""The unique ID of the protocol endpoint. """,
        dictionaryType=None
    )
    protocol_endpoint_in_band_id = data_model.property(
        "protocolEndpointInBandID", str,
        array=False, optional=False,
        documentation="""The scsiNAADeviceID of the protocol endpoint. For more information, see protocolEndpoint. """,
        dictionaryType=None
    )
    protocol_endpoint_type = data_model.property(
        "protocolEndpointType", str,
        array=False, optional=False,
        documentation="""The type of protocol endpoint. SCSI is the only value returned for the protocol endpoint type. """,
        dictionaryType=None
    )
    virtual_volume_binding_id = data_model.property(
        "virtualVolumeBindingID", int,
        array=False, optional=False,
        documentation="""The unique ID of the virtual volume binding object. """,
        dictionaryType=None
    )
    virtual_volume_host_id = data_model.property(
        "virtualVolumeHostID", UUID,
        array=False, optional=False,
        documentation="""The unique ID of the virtual volume host. """,
        dictionaryType=None
    )
    virtual_volume_id = data_model.property(
        "virtualVolumeID", UUID,
        array=False, optional=False,
        documentation="""The unique ID of the virtual volume. """,
        dictionaryType=None
    )
    virtual_volume_secondary_id = data_model.property(
        "virtualVolumeSecondaryID", str,
        array=False, optional=False,
        documentation="""The secondary ID of the virtual volume. """,
        dictionaryType=None
    )

    def __init__(self,
            protocol_endpoint_id,
            protocol_endpoint_in_band_id,
            protocol_endpoint_type,
            virtual_volume_binding_id,
            virtual_volume_host_id,
            virtual_volume_id,
            virtual_volume_secondary_id):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class ListVirtualVolumeBindingsResult(data_model.DataObject):
    """ListVirtualVolumeBindingsResult  

    :param bindings: [required] Describes the VVol <-> Host binding. 
    :type bindings: VirtualVolumeBinding

    """
    bindings = data_model.property(
        "bindings", VirtualVolumeBinding,
        array=True, optional=False,
        documentation="""Describes the VVol <-> Host binding. """,
        dictionaryType=None
    )

    def __init__(self,
            bindings):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class GetDriveStatsRequest(data_model.DataObject):
    """GetDriveStatsRequest  
    GetDriveStats returns high-level activity measurements for a single drive. Values are cumulative from the addition of the drive to the
    cluster. Some values are specific to block drives. You might not obtain statistical data for both block and metadata drives when you
    run this method. 

    :param drive_id: [required] Specifies the drive for which statistics are gathered. 
    :type drive_id: int

    """
    drive_id = data_model.property(
        "driveID", int,
        array=False, optional=False,
        documentation="""Specifies the drive for which statistics are gathered. """,
        dictionaryType=None
    )

    def __init__(self,
            drive_id):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class ModifyClusterAdminResult(data_model.DataObject):
    """ModifyClusterAdminResult  

    """

    def __init__(self):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class EnableLdapAuthenticationResult(data_model.DataObject):
    """EnableLdapAuthenticationResult  

    """

    def __init__(self):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class ListVolumeStatsByVolumeRequest(data_model.DataObject):
    """ListVolumeStatsByVolumeRequest  
    ListVolumeStatsByVolume returns high-level activity measurements for every volume, by volume. Values are cumulative from the
    creation of the volume.

    :param include_virtual_volumes:  Specifies that virtual volumes are included in the response by default. To exclude virtual volumes, set to false. 
    :type include_virtual_volumes: bool

    """
    include_virtual_volumes = data_model.property(
        "includeVirtualVolumes", bool,
        array=False, optional=True,
        documentation="""Specifies that virtual volumes are included in the response by default. To exclude virtual volumes, set to false. """,
        dictionaryType=None
    )

    def __init__(self,
            include_virtual_volumes=None):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class ClusterFaultInfo(data_model.DataObject):
    """ClusterFaultInfo  

    :param drive_ids:   
    :type drive_ids: int

    :param network_interface:   
    :type network_interface: str

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

    :param data:   
    :type data: dict

    """
    drive_ids = data_model.property(
        "driveIDs", int,
        array=True, optional=True,
        documentation=""" """,
        dictionaryType=None
    )
    network_interface = data_model.property(
        "networkInterface", str,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )
    severity = data_model.property(
        "severity", str,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    type = data_model.property(
        "type", str,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    code = data_model.property(
        "code", str,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    details = data_model.property(
        "details", str,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    node_hardware_fault_id = data_model.property(
        "nodeHardwareFaultID", int,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    node_id = data_model.property(
        "nodeID", int,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    service_id = data_model.property(
        "serviceID", int,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    drive_id = data_model.property(
        "driveID", int,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    resolved = data_model.property(
        "resolved", bool,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    cluster_fault_id = data_model.property(
        "clusterFaultID", int,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    date = data_model.property(
        "date", str,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    resolved_date = data_model.property(
        "resolvedDate", str,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    data = data_model.property(
        "data", dict,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )

    def __init__(self,
            severity,
            type,
            code,
            details,
            node_hardware_fault_id,
            node_id,
            service_id,
            drive_id,
            resolved,
            cluster_fault_id,
            date,
            resolved_date,
            drive_ids=None,
            network_interface=None,
            data=None):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class ListClusterFaultsResult(data_model.DataObject):
    """ListClusterFaultsResult  

    :param faults: [required] The list of Cluster Fault objects. 
    :type faults: ClusterFaultInfo

    """
    faults = data_model.property(
        "faults", ClusterFaultInfo,
        array=True, optional=False,
        documentation="""The list of Cluster Fault objects. """,
        dictionaryType=None
    )

    def __init__(self,
            faults):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class AddLdapClusterAdminRequest(data_model.DataObject):
    """AddLdapClusterAdminRequest  
    AddLdapClusterAdmin enables you to add a new LDAP cluster administrator user. An LDAP cluster administrator can manage the
    cluster via the API and management tools. LDAP cluster admin accounts are completely separate and unrelated to standard tenant
    accounts.
    You can also use this method to add an LDAP group that has been defined in Active Directory. The access level that is given to the group is passed to the individual users in the LDAP group.

    :param username: [required] The distinguished user name for the new LDAP cluster admin. 
    :type username: str

    :param access: [required] Controls which methods this Cluster Admin can use. For more details on the levels of access, see the Access Control appendix in the SolidFire API Reference. 
    :type access: str

    :param accept_eula:  Accept the End User License Agreement. Set to true to add a cluster administrator account to the system. If omitted or set to false, the method call fails. 
    :type accept_eula: bool

    :param attributes:  List of name-value pairs in JSON object format. 
    :type attributes: dict

    """
    username = data_model.property(
        "username", str,
        array=False, optional=False,
        documentation="""The distinguished user name for the new LDAP cluster admin. """,
        dictionaryType=None
    )
    access = data_model.property(
        "access", str,
        array=True, optional=False,
        documentation="""Controls which methods this Cluster Admin can use. For more details on the levels of access, see the Access Control appendix in the SolidFire API Reference. """,
        dictionaryType=None
    )
    accept_eula = data_model.property(
        "acceptEula", bool,
        array=False, optional=True,
        documentation="""Accept the End User License Agreement. Set to true to add a cluster administrator account to the system. If omitted or set to false, the method call fails. """,
        dictionaryType=None
    )
    attributes = data_model.property(
        "attributes", dict,
        array=False, optional=True,
        documentation="""List of name-value pairs in JSON object format. """,
        dictionaryType=None
    )

    def __init__(self,
            username,
            access,
            accept_eula=None,
            attributes=None):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class ModifyVolumePairRequest(data_model.DataObject):
    """ModifyVolumePairRequest  
    ModifyVolumePair enables you to pause or restart replication between a pair of volumes.

    :param volume_id: [required] The ID of the volume to be modified. 
    :type volume_id: int

    :param paused_manual:  Specifies whether to pause or restart volume replication process. Valid values are:  true: Pauses volume replication false: Restarts volume replication 
    :type paused_manual: bool

    :param mode:  Specifies the volume replication mode. Possible values are: Async: Writes are acknowledged when they complete locally. The cluster does not wait for writes to be replicated to the target cluster. Sync: The source acknowledges the write when the data is stored locally and on the remote cluster. SnapshotsOnly: Only snapshots created on the source cluster are replicated. Active writes from the source volume are not replicated. 
    :type mode: str

    :param pause_limit:  Internal use only. 
    :type pause_limit: int

    """
    volume_id = data_model.property(
        "volumeID", int,
        array=False, optional=False,
        documentation="""The ID of the volume to be modified. """,
        dictionaryType=None
    )
    paused_manual = data_model.property(
        "pausedManual", bool,
        array=False, optional=True,
        documentation="""Specifies whether to pause or restart volume replication process. Valid values are:  true: Pauses volume replication false: Restarts volume replication """,
        dictionaryType=None
    )
    mode = data_model.property(
        "mode", str,
        array=False, optional=True,
        documentation="""Specifies the volume replication mode. Possible values are: Async: Writes are acknowledged when they complete locally. The cluster does not wait for writes to be replicated to the target cluster. Sync: The source acknowledges the write when the data is stored locally and on the remote cluster. SnapshotsOnly: Only snapshots created on the source cluster are replicated. Active writes from the source volume are not replicated. """,
        dictionaryType=None
    )
    pause_limit = data_model.property(
        "pauseLimit", int,
        array=False, optional=True,
        documentation="""Internal use only. """,
        dictionaryType=None
    )

    def __init__(self,
            volume_id,
            paused_manual=None,
            mode=None,
            pause_limit=None):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class CloneMultipleVolumesRequest(data_model.DataObject):
    """CloneMultipleVolumesRequest  
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

    :param group_snapshot_id:  ID of the group snapshot to use as a basis for the clone. 
    :type group_snapshot_id: int

    :param new_account_id:  New account ID for the volumes if not overridden by information passed in the volumes array. 
    :type new_account_id: int

    """
    volumes = data_model.property(
        "volumes", CloneMultipleVolumeParams,
        array=True, optional=False,
        documentation="""Unique ID for each volume to include in the clone. If optional parameters are not specified, the values are inherited from the source volumes. Required parameter for "volumes" array: volumeID Optional parameters for "volumes" array: access: Can be one of readOnly, readWrite, locked, or replicationTarget attributes: List of name-value pairs in JSON object format. name: New name for the clone. newAccountID: Account ID for the new volumes. newSize: New size Total size of the volume, in bytes. Size is rounded up to the nearest 1MB. """,
        dictionaryType=None
    )
    access = data_model.property(
        "access", str,
        array=False, optional=True,
        documentation="""New default access method for the new volumes if not overridden by information passed in the volume's array. """,
        dictionaryType=None
    )
    group_snapshot_id = data_model.property(
        "groupSnapshotID", int,
        array=False, optional=True,
        documentation="""ID of the group snapshot to use as a basis for the clone. """,
        dictionaryType=None
    )
    new_account_id = data_model.property(
        "newAccountID", int,
        array=False, optional=True,
        documentation="""New account ID for the volumes if not overridden by information passed in the volumes array. """,
        dictionaryType=None
    )

    def __init__(self,
            volumes,
            access=None,
            group_snapshot_id=None,
            new_account_id=None):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class ListVolumeAccessGroupsRequest(data_model.DataObject):
    """ListVolumeAccessGroupsRequest  
    ListVolumeAccessGroups enables you to return
    information about the volume access groups that are
    currently in the system.

    :param start_volume_access_group_id:  The volume access group ID at which to begin the listing. If unspecified, there is no lower limit (implicitly 0). 
    :type start_volume_access_group_id: int

    :param limit:  The maximum number of results to return. This can be useful for paging. 
    :type limit: int

    :param volume_access_groups:  The list of ids of the volume access groups you wish to list 
    :type volume_access_groups: int

    """
    start_volume_access_group_id = data_model.property(
        "startVolumeAccessGroupID", int,
        array=False, optional=True,
        documentation="""The volume access group ID at which to begin the listing. If unspecified, there is no lower limit (implicitly 0). """,
        dictionaryType=None
    )
    limit = data_model.property(
        "limit", int,
        array=False, optional=True,
        documentation="""The maximum number of results to return. This can be useful for paging. """,
        dictionaryType=None
    )
    volume_access_groups = data_model.property(
        "volumeAccessGroups", int,
        array=True, optional=True,
        documentation="""The list of ids of the volume access groups you wish to list """,
        dictionaryType=None
    )

    def __init__(self,
            start_volume_access_group_id=None,
            limit=None,
            volume_access_groups=None):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class DeleteQoSPolicyRequest(data_model.DataObject):
    """DeleteQoSPolicyRequest  
    You can use the DeleteQoSPolicy method to delete a QoS policy from the system.
    The QoS settings for all volumes created of modified with this policy are unaffected.

    :param qos_policy_id: [required] The ID of the QoS policy to be deleted. 
    :type qos_policy_id: int

    """
    qos_policy_id = data_model.property(
        "qosPolicyID", int,
        array=False, optional=False,
        documentation="""The ID of the QoS policy to be deleted. """,
        dictionaryType=None
    )

    def __init__(self,
            qos_policy_id):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class SetLoginBannerRequest(data_model.DataObject):
    """SetLoginBannerRequest  
    You can use the SetLoginBanner method to set the active Terms of Use banner users see when they log on to the web interface.

    :param banner:  The desired text of the Terms of Use banner. 
    :type banner: str

    :param enabled:  The status of the Terms of Use banner. Possible values: true: The Terms of Use banner is displayed upon web interface login. false: The Terms of Use banner is not displayed upon web interface login. 
    :type enabled: bool

    """
    banner = data_model.property(
        "banner", str,
        array=False, optional=True,
        documentation="""The desired text of the Terms of Use banner. """,
        dictionaryType=None
    )
    enabled = data_model.property(
        "enabled", bool,
        array=False, optional=True,
        documentation="""The status of the Terms of Use banner. Possible values: true: The Terms of Use banner is displayed upon web interface login. false: The Terms of Use banner is not displayed upon web interface login. """,
        dictionaryType=None
    )

    def __init__(self,
            banner=None,
            enabled=None):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class RemoveNodeSSLCertificateResult(data_model.DataObject):
    """RemoveNodeSSLCertificateResult  

    """

    def __init__(self):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class SetSnmpACLResult(data_model.DataObject):
    """SetSnmpACLResult  

    """

    def __init__(self):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class ListGroupSnapshotsRequest(data_model.DataObject):
    """ListGroupSnapshotsRequest  
    ListGroupSnapshots enables you to get information about all group snapshots that have been created.

    :param volumes:  An array of unique volume IDs to query. If you do not specify this parameter, all group snapshots on the cluster are included. 
    :type volumes: int

    :param group_snapshot_id:  Retrieves information for a specific group snapshot ID. 
    :type group_snapshot_id: int

    """
    volumes = data_model.property(
        "volumes", int,
        array=True, optional=True,
        documentation="""An array of unique volume IDs to query. If you do not specify this parameter, all group snapshots on the cluster are included. """,
        dictionaryType=None
    )
    group_snapshot_id = data_model.property(
        "groupSnapshotID", int,
        array=False, optional=True,
        documentation="""Retrieves information for a specific group snapshot ID. """,
        dictionaryType=None
    )

    def __init__(self,
            volumes=None,
            group_snapshot_id=None):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class EnableFeatureRequest(data_model.DataObject):
    """EnableFeatureRequest  
    You can use EnableFeature to enable cluster features that are disabled by default.

    :param feature: [required] Indicates which feature to enable. Valid value is: vvols: Enable the NetApp SolidFire VVols cluster feature. 
    :type feature: str

    """
    feature = data_model.property(
        "feature", str,
        array=False, optional=False,
        documentation="""Indicates which feature to enable. Valid value is: vvols: Enable the NetApp SolidFire VVols cluster feature. """,
        dictionaryType=None
    )

    def __init__(self,
            feature):
        kwargs = locals()
        del kwargs["self"]
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

    :param network: [required] This parameter ainteger with the cidr variable is used to control which network the access and community string apply to. The special value of "default" is used to specify an entry that applies to all networks. The cidr mask is ignored when network value is either a host name or default. 
    :type network: str

    """
    access = data_model.property(
        "access", str,
        array=False, optional=False,
        documentation="""ro: read-only access.* rw: for read-write access. rosys: for read-only access to a restricted set of system information *SolidFire recommends that all networks other than the default "localhost" be set to "ro" access, because all SolidFire MIB objects are read-only. """,
        dictionaryType=None
    )
    cidr = data_model.property(
        "cidr", int,
        array=False, optional=False,
        documentation="""A CIDR network mask. This network mask must be an integer greater than or equal to 0, and less than or equal to 32. It must also not be equal to 31. """,
        dictionaryType=None
    )
    community = data_model.property(
        "community", str,
        array=False, optional=False,
        documentation="""SNMP community string. """,
        dictionaryType=None
    )
    network = data_model.property(
        "network", str,
        array=False, optional=False,
        documentation="""This parameter ainteger with the cidr variable is used to control which network the access and community string apply to. The special value of "default" is used to specify an entry that applies to all networks. The cidr mask is ignored when network value is either a host name or default. """,
        dictionaryType=None
    )

    def __init__(self,
            access,
            cidr,
            community,
            network):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class RemoveNodesRequest(data_model.DataObject):
    """RemoveNodesRequest  
    You can use RemoveNodes to remove one or more nodes that should no longer participate in the cluster. Before removing a node, you must remove all drives the node contains using the RemoveDrives method. You cannot remove a node until the RemoveDrives process has completed and all data has been migrated away from the node.
    After you remove a node, it registers itself as a pending node. You can add the node again or shut it down (shutting the node down removes it from the Pending Node list).

    :param nodes: [required] List of NodeIDs for the nodes to be removed. 
    :type nodes: int

    """
    nodes = data_model.property(
        "nodes", int,
        array=True, optional=False,
        documentation="""List of NodeIDs for the nodes to be removed. """,
        dictionaryType=None
    )

    def __init__(self,
            nodes):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class DeleteGroupSnapshotRequest(data_model.DataObject):
    """DeleteGroupSnapshotRequest  
    DeleteGroupSnapshot enables you to delete a group snapshot. You can use the saveMembers parameter to preserve all the snapshots that were made for the volumes in the group, but the group association is removed.

    :param group_snapshot_id: [required] Specifies the unique ID of the group snapshot. 
    :type group_snapshot_id: int

    :param save_members: [required] Specifies whether to preserve snapshots or delete them. Valid values are: true: Snapshots are preserved, but group association is removed. false: The group and snapshots are deleted. 
    :type save_members: bool

    """
    group_snapshot_id = data_model.property(
        "groupSnapshotID", int,
        array=False, optional=False,
        documentation="""Specifies the unique ID of the group snapshot. """,
        dictionaryType=None
    )
    save_members = data_model.property(
        "saveMembers", bool,
        array=False, optional=False,
        documentation="""Specifies whether to preserve snapshots or delete them. Valid values are: true: Snapshots are preserved, but group association is removed. false: The group and snapshots are deleted. """,
        dictionaryType=None
    )

    def __init__(self,
            group_snapshot_id,
            save_members):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class ModifySnapshotResult(data_model.DataObject):
    """ModifySnapshotResult  

    :param snapshot:   
    :type snapshot: Snapshot

    """
    snapshot = data_model.property(
        "snapshot", Snapshot,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )

    def __init__(self,
            snapshot=None):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class RemoveVolumesFromVolumeAccessGroupRequest(data_model.DataObject):
    """RemoveVolumesFromVolumeAccessGroupRequest  
    The RemoveVolumeFromVolumeAccessGroup method enables you to remove volumes from a volume access group.

    :param volume_access_group_id: [required] The ID of the volume access group to remove volumes from. 
    :type volume_access_group_id: int

    :param volumes: [required] The ID of the volume access group to remove volumes from. 
    :type volumes: int

    """
    volume_access_group_id = data_model.property(
        "volumeAccessGroupID", int,
        array=False, optional=False,
        documentation="""The ID of the volume access group to remove volumes from. """,
        dictionaryType=None
    )
    volumes = data_model.property(
        "volumes", int,
        array=True, optional=False,
        documentation="""The ID of the volume access group to remove volumes from. """,
        dictionaryType=None
    )

    def __init__(self,
            volume_access_group_id,
            volumes):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class ModifyStorageContainerRequest(data_model.DataObject):
    """ModifyStorageContainerRequest  
    ModifyStorageContainer enables you to make changes to an existing virtual volume storage container.

    :param storage_container_id: [required] The unique ID of the virtual volume storage container to modify. 
    :type storage_container_id: UUID

    :param initiator_secret:  The new secret for CHAP authentication for the initiator. 
    :type initiator_secret: str

    :param target_secret:  The new secret for CHAP authentication for the target. 
    :type target_secret: str

    """
    storage_container_id = data_model.property(
        "storageContainerID", UUID,
        array=False, optional=False,
        documentation="""The unique ID of the virtual volume storage container to modify. """,
        dictionaryType=None
    )
    initiator_secret = data_model.property(
        "initiatorSecret", str,
        array=False, optional=True,
        documentation="""The new secret for CHAP authentication for the initiator. """,
        dictionaryType=None
    )
    target_secret = data_model.property(
        "targetSecret", str,
        array=False, optional=True,
        documentation="""The new secret for CHAP authentication for the target. """,
        dictionaryType=None
    )

    def __init__(self,
            storage_container_id,
            initiator_secret=None,
            target_secret=None):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class TestConnectMvipDetails(data_model.DataObject):
    """TestConnectMvipDetails  

    :param ping_bytes: [required] Details of the ping tests with 56 Bytes and 1500 Bytes. 
    :type ping_bytes: dict

    :param mvip: [required] The MVIP tested against. 
    :type mvip: str

    :param connected: [required] Whether the test could connect to the MVIP. 
    :type connected: bool

    """
    ping_bytes = data_model.property(
        "pingBytes", dict,
        array=False, optional=False,
        documentation="""Details of the ping tests with 56 Bytes and 1500 Bytes. """,
        dictionaryType=None
    )
    mvip = data_model.property(
        "mvip", str,
        array=False, optional=False,
        documentation="""The MVIP tested against. """,
        dictionaryType=None
    )
    connected = data_model.property(
        "connected", bool,
        array=False, optional=False,
        documentation="""Whether the test could connect to the MVIP. """,
        dictionaryType=None
    )

    def __init__(self,
            ping_bytes,
            mvip,
            connected):
        kwargs = locals()
        del kwargs["self"]
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
        documentation="""Information about the test operation """,
        dictionaryType=None
    )
    duration = data_model.property(
        "duration", str,
        array=False, optional=False,
        documentation="""The length of time required to run the test. """,
        dictionaryType=None
    )
    result = data_model.property(
        "result", str,
        array=False, optional=False,
        documentation="""The results of the entire test """,
        dictionaryType=None
    )

    def __init__(self,
            details,
            duration,
            result):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class ClearClusterFaultsResult(data_model.DataObject):
    """ClearClusterFaultsResult  

    """

    def __init__(self):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class TestConnectSvipDetails(data_model.DataObject):
    """TestConnectSvipDetails  

    :param ping_bytes: [required] Details of the ping tests with 56 Bytes and 1500 Bytes. 
    :type ping_bytes: dict

    :param svip: [required] The SVIP tested against. 
    :type svip: str

    :param connected: [required] Whether the test could connect to the MVIP. 
    :type connected: bool

    """
    ping_bytes = data_model.property(
        "pingBytes", dict,
        array=False, optional=False,
        documentation="""Details of the ping tests with 56 Bytes and 1500 Bytes. """,
        dictionaryType=None
    )
    svip = data_model.property(
        "svip", str,
        array=False, optional=False,
        documentation="""The SVIP tested against. """,
        dictionaryType=None
    )
    connected = data_model.property(
        "connected", bool,
        array=False, optional=False,
        documentation="""Whether the test could connect to the MVIP. """,
        dictionaryType=None
    )

    def __init__(self,
            ping_bytes,
            svip,
            connected):
        kwargs = locals()
        del kwargs["self"]
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
        documentation="""Information about the test operation """,
        dictionaryType=None
    )
    duration = data_model.property(
        "duration", str,
        array=False, optional=False,
        documentation="""The length of time required to run the test. """,
        dictionaryType=None
    )
    result = data_model.property(
        "result", str,
        array=False, optional=False,
        documentation="""The results of the entire test """,
        dictionaryType=None
    )

    def __init__(self,
            details,
            duration,
            result):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class ListVolumeStatsByVolumeResult(data_model.DataObject):
    """ListVolumeStatsByVolumeResult  

    :param volume_stats: [required] List of account activity information. 
    :type volume_stats: VolumeStats

    """
    volume_stats = data_model.property(
        "volumeStats", VolumeStats,
        array=True, optional=False,
        documentation="""List of account activity information. """,
        dictionaryType=None
    )

    def __init__(self,
            volume_stats):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class SnmpV3UsmUser(data_model.DataObject):
    """SnmpV3UsmUser  
    The SNMP v3 usmUser object is used with the API method SetSnmpInfo to configure SNMP on the cluster.

    :param access: [required] rouser: read-only access.* rwuser: for read-write access. rosys: for read-only access to a restricted set of system information *SolidFire recommends that all USM users be set to "rouser" access, because all SolidFire MIB objects are read-only. 
    :type access: str

    :param name: [required] The name of the user. Must contain at least one character, but no more than 32 characters. Blank spaces are not allowed. 
    :type name: str

    :param password: [required] The password of the user. Must be between 8 and 255 characters integer (inclusive). Blank spaces are not allowed. Required if "secLevel" is "auth" or "priv." 
    :type password: str

    :param passphrase: [required] The passphrase of the user. Must be between 8 and 255 characters integer (inclusive). Blank spaces are not allowed. Required if "secLevel" is "priv." 
    :type passphrase: str

    :param sec_level: [required] noauth: No password or passphrase is required. auth: A password is required for user access. priv: A password and passphrase is required for user access. 
    :type sec_level: str

    """
    access = data_model.property(
        "access", str,
        array=False, optional=False,
        documentation="""rouser: read-only access.* rwuser: for read-write access. rosys: for read-only access to a restricted set of system information *SolidFire recommends that all USM users be set to "rouser" access, because all SolidFire MIB objects are read-only. """,
        dictionaryType=None
    )
    name = data_model.property(
        "name", str,
        array=False, optional=False,
        documentation="""The name of the user. Must contain at least one character, but no more than 32 characters. Blank spaces are not allowed. """,
        dictionaryType=None
    )
    password = data_model.property(
        "password", str,
        array=False, optional=False,
        documentation="""The password of the user. Must be between 8 and 255 characters integer (inclusive). Blank spaces are not allowed. Required if "secLevel" is "auth" or "priv." """,
        dictionaryType=None
    )
    passphrase = data_model.property(
        "passphrase", str,
        array=False, optional=False,
        documentation="""The passphrase of the user. Must be between 8 and 255 characters integer (inclusive). Blank spaces are not allowed. Required if "secLevel" is "priv." """,
        dictionaryType=None
    )
    sec_level = data_model.property(
        "secLevel", str,
        array=False, optional=False,
        documentation="""noauth: No password or passphrase is required. auth: A password is required for user access. priv: A password and passphrase is required for user access. """,
        dictionaryType=None
    )

    def __init__(self,
            access,
            name,
            password,
            passphrase,
            sec_level):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class GetSnmpInfoResult(data_model.DataObject):
    """GetSnmpInfoResult  

    :param networks:  List of networks and access types enabled for SNMP.  Note: "networks" will only be present if SNMP V3 is disabled. 
    :type networks: SnmpNetwork

    :param enabled: [required] If the nodes in the cluster are configured for SNMP. 
    :type enabled: bool

    :param snmp_v3_enabled: [required] If the nodes in the cluster are configured for SNMP v3. 
    :type snmp_v3_enabled: bool

    :param usm_users:  If SNMP v3 is enabled, the values returned is a list of user access parameters for SNMP information from the cluster. This will be returned instead of the "networks" parameter. 
    :type usm_users: SnmpV3UsmUser

    """
    networks = data_model.property(
        "networks", SnmpNetwork,
        array=True, optional=True,
        documentation="""List of networks and access types enabled for SNMP.  Note: "networks" will only be present if SNMP V3 is disabled. """,
        dictionaryType=None
    )
    enabled = data_model.property(
        "enabled", bool,
        array=False, optional=False,
        documentation="""If the nodes in the cluster are configured for SNMP. """,
        dictionaryType=None
    )
    snmp_v3_enabled = data_model.property(
        "snmpV3Enabled", bool,
        array=False, optional=False,
        documentation="""If the nodes in the cluster are configured for SNMP v3. """,
        dictionaryType=None
    )
    usm_users = data_model.property(
        "usmUsers", SnmpV3UsmUser,
        array=True, optional=True,
        documentation="""If SNMP v3 is enabled, the values returned is a list of user access parameters for SNMP information from the cluster. This will be returned instead of the "networks" parameter. """,
        dictionaryType=None
    )

    def __init__(self,
            enabled,
            snmp_v3_enabled,
            networks=None,
            usm_users=None):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class ModifyVolumesResult(data_model.DataObject):
    """ModifyVolumesResult  

    :param volumes: [required]  
    :type volumes: Volume

    :param qos:   
    :type qos: QoS

    """
    volumes = data_model.property(
        "volumes", Volume,
        array=True, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    qos = data_model.property(
        "qos", QoS,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )

    def __init__(self,
            volumes,
            qos=None):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class RestartNetworkingRequest(data_model.DataObject):
    """RestartNetworkingRequest  
    The RestartNetworking API method enables you to restart the networking services on a node.
    Warning: This method restarts all networking services on a node, causing temporary loss of networking connectivity.
    Exercise caution when using this method.
    Note: This method is available only through the per-node API endpoint 5.0 or later.

    :param force: [required] Required parameter to successfully reset the node. 
    :type force: bool

    """
    force = data_model.property(
        "force", bool,
        array=False, optional=False,
        documentation="""Required parameter to successfully reset the node. """,
        dictionaryType=None
    )

    def __init__(self,
            force):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class ListNodeFibreChannelPortInfoResult(data_model.DataObject):
    """ListNodeFibreChannelPortInfoResult  
    List of fibre channel port info results grouped by node.

    :param fibre_channel_ports: [required] List of all physical Fibre Channel ports. 
    :type fibre_channel_ports: FibreChannelPortInfo

    """
    fibre_channel_ports = data_model.property(
        "fibreChannelPorts", FibreChannelPortInfo,
        array=True, optional=False,
        documentation="""List of all physical Fibre Channel ports. """,
        dictionaryType=None
    )

    def __init__(self,
            fibre_channel_ports):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class CreateSupportBundleRequest(data_model.DataObject):
    """CreateSupportBundleRequest  
    CreateSupportBundle enables you to create a support bundle file under the node's directory. After creation, the bundle is stored on the node as a tar.gz file.

    :param bundle_name:  The unique name for the support bundle. If no name is provided, "supportbundle" and the node name are used as the filename. 
    :type bundle_name: str

    :param extra_args:  Passed to the sf_make_support_bundle script. You should use this parameter only at the request of NetApp SolidFire Support. 
    :type extra_args: str

    :param timeout_sec:  The number of seconds to allow the support bundle script to run before stopping. The default value is 1500 seconds. 
    :type timeout_sec: int

    """
    bundle_name = data_model.property(
        "bundleName", str,
        array=False, optional=True,
        documentation="""The unique name for the support bundle. If no name is provided, "supportbundle" and the node name are used as the filename. """,
        dictionaryType=None
    )
    extra_args = data_model.property(
        "extraArgs", str,
        array=False, optional=True,
        documentation="""Passed to the sf_make_support_bundle script. You should use this parameter only at the request of NetApp SolidFire Support. """,
        dictionaryType=None
    )
    timeout_sec = data_model.property(
        "timeoutSec", int,
        array=False, optional=True,
        documentation="""The number of seconds to allow the support bundle script to run before stopping. The default value is 1500 seconds. """,
        dictionaryType=None
    )

    def __init__(self,
            bundle_name=None,
            extra_args=None,
            timeout_sec=None):
        kwargs = locals()
        del kwargs["self"]
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
        documentation=""" """,
        dictionaryType=None
    )
    drive_id = data_model.property(
        "driveID", int,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )
    failed_die_count = data_model.property(
        "failedDieCount", int,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    life_remaining_percent = data_model.property(
        "lifeRemainingPercent", int,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    lifetime_read_bytes = data_model.property(
        "lifetimeReadBytes", int,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    lifetime_write_bytes = data_model.property(
        "lifetimeWriteBytes", int,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    power_on_hours = data_model.property(
        "powerOnHours", int,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    read_bytes = data_model.property(
        "readBytes", int,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    read_ops = data_model.property(
        "readOps", int,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    reallocated_sectors = data_model.property(
        "reallocatedSectors", int,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    reserve_capacity_percent = data_model.property(
        "reserveCapacityPercent", int,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    timestamp = data_model.property(
        "timestamp", str,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    total_capacity = data_model.property(
        "totalCapacity", int,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    used_capacity = data_model.property(
        "usedCapacity", int,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )
    used_memory = data_model.property(
        "usedMemory", int,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    write_bytes = data_model.property(
        "writeBytes", int,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    write_ops = data_model.property(
        "writeOps", int,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )

    def __init__(self,
            failed_die_count,
            life_remaining_percent,
            lifetime_read_bytes,
            lifetime_write_bytes,
            power_on_hours,
            read_bytes,
            read_ops,
            reallocated_sectors,
            reserve_capacity_percent,
            timestamp,
            total_capacity,
            used_memory,
            write_bytes,
            write_ops,
            active_sessions=None,
            drive_id=None,
            used_capacity=None):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class GetDriveStatsResult(data_model.DataObject):
    """GetDriveStatsResult  

    :param drive_stats: [required]  
    :type drive_stats: DriveStats

    """
    drive_stats = data_model.property(
        "driveStats", DriveStats,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )

    def __init__(self,
            drive_stats):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class ModifyVolumeAccessGroupLunAssignmentsRequest(data_model.DataObject):
    """ModifyVolumeAccessGroupLunAssignmentsRequest  
    The ModifyVolumeAccessGroupLunAssignments
    method enables you to define custom LUN assignments
    for specific volumes. This method changes only LUN
    values set on the lunAssignments parameter in the
    volume access group. All other LUN assignments remain
    unchanged. LUN assignment values must be unique for volumes in a volume access group. You cannot define duplicate LUN values within a volume access group. However, you can use the same LUN values again in different volume access groups. 
    Note: Correct LUN values are 0 through 16383. The system generates an exception if you pass a LUN value outside of this range. None of the specified LUN assignments are modified if there is an exception. 
    Caution: If you change a LUN assignment for a volume with active I/O, the I/O can be disrupted. You might need to change the server configuration before changing volume LUN assignments.

    :param volume_access_group_id: [required] The ID of the volume access group for which the LUN assignments will be modified. 
    :type volume_access_group_id: int

    :param lun_assignments: [required] The volume IDs with new assigned LUN values. 
    :type lun_assignments: LunAssignment

    """
    volume_access_group_id = data_model.property(
        "volumeAccessGroupID", int,
        array=False, optional=False,
        documentation="""The ID of the volume access group for which the LUN assignments will be modified. """,
        dictionaryType=None
    )
    lun_assignments = data_model.property(
        "lunAssignments", LunAssignment,
        array=True, optional=False,
        documentation="""The volume IDs with new assigned LUN values. """,
        dictionaryType=None
    )

    def __init__(self,
            volume_access_group_id,
            lun_assignments):
        kwargs = locals()
        del kwargs["self"]
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
        documentation="""ID of the async process to be checked for completion. """,
        dictionaryType=None
    )
    key = data_model.property(
        "key", str,
        array=False, optional=False,
        documentation="""Opaque key uniquely identifying the session. """,
        dictionaryType=None
    )
    url = data_model.property(
        "url", str,
        array=False, optional=False,
        documentation="""URL to access the node's web server """,
        dictionaryType=None
    )

    def __init__(self,
            async_handle,
            key,
            url):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class GetNetworkConfigResult(data_model.DataObject):
    """GetNetworkConfigResult  

    :param network: [required]  
    :type network: Network

    """
    network = data_model.property(
        "network", Network,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )

    def __init__(self,
            network):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class ListVolumeStatsByVolumeAccessGroupRequest(data_model.DataObject):
    """ListVolumeStatsByVolumeAccessGroupRequest  
    ListVolumeStatsByVolumeAccessGroup enables you to get total activity measurements for all of the volumes that are a member of the
    specified volume access group(s).

    :param volume_access_groups:  An array of VolumeAccessGroupIDs for which volume activity is returned. If omitted, statistics for all volume access groups are returned. 
    :type volume_access_groups: int

    :param include_virtual_volumes:  Specifies that virtual volumes are included in the response by default. To exclude virtual volumes, set to false. 
    :type include_virtual_volumes: bool

    """
    volume_access_groups = data_model.property(
        "volumeAccessGroups", int,
        array=True, optional=True,
        documentation="""An array of VolumeAccessGroupIDs for which volume activity is returned. If omitted, statistics for all volume access groups are returned. """,
        dictionaryType=None
    )
    include_virtual_volumes = data_model.property(
        "includeVirtualVolumes", bool,
        array=False, optional=True,
        documentation="""Specifies that virtual volumes are included in the response by default. To exclude virtual volumes, set to false. """,
        dictionaryType=None
    )

    def __init__(self,
            volume_access_groups=None,
            include_virtual_volumes=None):
        kwargs = locals()
        del kwargs["self"]
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
        documentation="""Status of the session requested. Returned status: preparing active done failed """,
        dictionaryType=None
    )
    url = data_model.property(
        "url", str,
        array=False, optional=False,
        documentation="""The URL to access the node's web server provided only if the session is still active. """,
        dictionaryType=None
    )
    attributes = data_model.property(
        "attributes", dict,
        array=False, optional=False,
        documentation="""Returns attributes that were specified in the BulkVolumeStatusUpdate method. Values are returned if they have changed or not. """,
        dictionaryType=None
    )

    def __init__(self,
            status,
            url,
            attributes):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class EnableSnmpResult(data_model.DataObject):
    """EnableSnmpResult  

    """

    def __init__(self):
        kwargs = locals()
        del kwargs["self"]
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

    :param volume_access_group_id:  The ID of the volume access group to which the initiatorWWPN beintegers. If not in a volume access group, the value will be null. 
    :type volume_access_group_id: int

    """
    initiator_wwpn = data_model.property(
        "initiatorWWPN", str,
        array=False, optional=False,
        documentation="""The WWPN of the initiator which is logged into the target port. """,
        dictionaryType=None
    )
    node_id = data_model.property(
        "nodeID", int,
        array=False, optional=False,
        documentation="""The node owning the Fibre Channel session. """,
        dictionaryType=None
    )
    service_id = data_model.property(
        "serviceID", int,
        array=False, optional=False,
        documentation="""The service ID of the FService owning this Fibre Channel session """,
        dictionaryType=None
    )
    target_wwpn = data_model.property(
        "targetWWPN", str,
        array=False, optional=False,
        documentation="""The WWPN of the target port involved in this session. """,
        dictionaryType=None
    )
    volume_access_group_id = data_model.property(
        "volumeAccessGroupID", int,
        array=False, optional=True,
        documentation="""The ID of the volume access group to which the initiatorWWPN beintegers. If not in a volume access group, the value will be null. """,
        dictionaryType=None
    )

    def __init__(self,
            initiator_wwpn,
            node_id,
            service_id,
            target_wwpn,
            volume_access_group_id=None):
        kwargs = locals()
        del kwargs["self"]
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
        documentation="""A list of FibreChannelSession objects with information about the Fibre Channel session. """,
        dictionaryType=None
    )

    def __init__(self,
            sessions):
        kwargs = locals()
        del kwargs["self"]
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
        documentation=""" """,
        dictionaryType=None
    )
    virtualvolume_id = data_model.property(
        "virtualvolumeID", UUID,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    clone_virtual_volume_id = data_model.property(
        "cloneVirtualVolumeID", UUID,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    status = data_model.property(
        "status", str,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    operation = data_model.property(
        "operation", str,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    virtual_volume_host_id = data_model.property(
        "virtualVolumeHostID", UUID,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    parent_metadata = data_model.property(
        "parentMetadata", dict,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    parent_total_size = data_model.property(
        "parentTotalSize", int,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    parent_used_size = data_model.property(
        "parentUsedSize", int,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    cancelled = data_model.property(
        "cancelled", bool,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )

    def __init__(self,
            virtual_volume_task_id,
            virtualvolume_id,
            clone_virtual_volume_id,
            status,
            operation,
            virtual_volume_host_id,
            parent_metadata,
            parent_total_size,
            parent_used_size,
            cancelled):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class ListVirtualVolumeTasksResult(data_model.DataObject):
    """ListVirtualVolumeTasksResult  

    :param tasks: [required] List of VVol Async Tasks. 
    :type tasks: VirtualVolumeTask

    """
    tasks = data_model.property(
        "tasks", VirtualVolumeTask,
        array=True, optional=False,
        documentation="""List of VVol Async Tasks. """,
        dictionaryType=None
    )

    def __init__(self,
            tasks):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class ModifyQoSPolicyRequest(data_model.DataObject):
    """ModifyQoSPolicyRequest  
    You can use the ModifyQoSPolicy method to modify an existing QoSPolicy on the system.

    :param qos_policy_id: [required] The ID of the policy to be modified. 
    :type qos_policy_id: int

    :param name:  If supplied, the name of the QoS Policy (e.g. gold, platinum, silver) is changed to this value. 
    :type name: str

    :param qos:  If supplied, the QoS settings for this policy are changed to these sttings. You can supply partial QoS values and only change some of the QoS settings. 
    :type qos: QoS

    """
    qos_policy_id = data_model.property(
        "qosPolicyID", int,
        array=False, optional=False,
        documentation="""The ID of the policy to be modified. """,
        dictionaryType=None
    )
    name = data_model.property(
        "name", str,
        array=False, optional=True,
        documentation="""If supplied, the name of the QoS Policy (e.g. gold, platinum, silver) is changed to this value. """,
        dictionaryType=None
    )
    qos = data_model.property(
        "qos", QoS,
        array=False, optional=True,
        documentation="""If supplied, the QoS settings for this policy are changed to these sttings. You can supply partial QoS values and only change some of the QoS settings. """,
        dictionaryType=None
    )

    def __init__(self,
            qos_policy_id,
            name=None,
            qos=None):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class PurgeDeletedVolumesRequest(data_model.DataObject):
    """PurgeDeletedVolumesRequest  
    PurgeDeletedVolumes immediately and permanently purges volumes that have been deleted.
    You can use this method to purge up to 500 volumes at one time.
    You must delete volumes using DeleteVolumes before they can be purged.
    Volumes are purged by the system automatically after a period of time, so usage of this method is not typically required.

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
        documentation="""A list of volumeIDs of volumes to be purged from the system. """,
        dictionaryType=None
    )
    account_ids = data_model.property(
        "accountIDs", int,
        array=True, optional=True,
        documentation="""A list of accountIDs. All of the volumes from all of the specified accounts are purged from the system. """,
        dictionaryType=None
    )
    volume_access_group_ids = data_model.property(
        "volumeAccessGroupIDs", int,
        array=True, optional=True,
        documentation="""A list of volumeAccessGroupIDs. All of the volumes from all of the specified Volume Access Groups are purged from the system. """,
        dictionaryType=None
    )

    def __init__(self,
            volume_ids=None,
            account_ids=None,
            volume_access_group_ids=None):
        kwargs = locals()
        del kwargs["self"]
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
        documentation="""The amount of space being saved by compressing data on a single volume. Stated as a ratio where "1" means data has been stored without being compressed. """,
        dictionaryType=None
    )
    deduplication = data_model.property(
        "deduplication", float,
        array=False, optional=True,
        documentation="""The amount of space being saved on a single volume by not duplicating data. Stated as a ratio. """,
        dictionaryType=None
    )
    thin_provisioning = data_model.property(
        "thinProvisioning", float,
        array=False, optional=True,
        documentation="""The ratio of space used to the amount of space allocated for storing data. Stated as a ratio. """,
        dictionaryType=None
    )
    timestamp = data_model.property(
        "timestamp", str,
        array=False, optional=False,
        documentation="""The last time efficiency data was collected after Garbage Collection (GC). ISO 8601 data string. """,
        dictionaryType=None
    )
    missing_volumes = data_model.property(
        "missingVolumes", int,
        array=True, optional=False,
        documentation="""The volumes that could not be queried for efficiency data. Missing volumes can be caused by GC being less than hour old, temporary network loss or restarted services since the GC cycle. """,
        dictionaryType=None
    )

    def __init__(self,
            timestamp,
            missing_volumes,
            compression=None,
            deduplication=None,
            thin_provisioning=None):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class GetClusterConfigResult(data_model.DataObject):
    """GetClusterConfigResult  

    :param cluster: [required] Cluster configuration information the node uses to communicate with the cluster. 
    :type cluster: ClusterConfig

    """
    cluster = data_model.property(
        "cluster", ClusterConfig,
        array=False, optional=False,
        documentation="""Cluster configuration information the node uses to communicate with the cluster. """,
        dictionaryType=None
    )

    def __init__(self,
            cluster):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class GetVolumeStatsResult(data_model.DataObject):
    """GetVolumeStatsResult  

    :param volume_stats: [required] Volume activity information. 
    :type volume_stats: VolumeStats

    """
    volume_stats = data_model.property(
        "volumeStats", VolumeStats,
        array=False, optional=False,
        documentation="""Volume activity information. """,
        dictionaryType=None
    )

    def __init__(self,
            volume_stats):
        kwargs = locals()
        del kwargs["self"]
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
        documentation=""" """,
        dictionaryType=DriveHardwareInfo
    )
    nodes = data_model.property(
        "nodes", dict,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=dict
    )

    def __init__(self,
            drives,
            nodes):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class GetClusterHardwareInfoResult(data_model.DataObject):
    """GetClusterHardwareInfoResult  

    :param cluster_hardware_info: [required] Hardware information for all nodes and drives in the cluster. Each object in this output is labeled with the nodeID of the given node. 
    :type cluster_hardware_info: ClusterHardwareInfo

    """
    cluster_hardware_info = data_model.property(
        "clusterHardwareInfo", ClusterHardwareInfo,
        array=False, optional=False,
        documentation="""Hardware information for all nodes and drives in the cluster. Each object in this output is labeled with the nodeID of the given node. """,
        dictionaryType=None
    )

    def __init__(self,
            cluster_hardware_info):
        kwargs = locals()
        del kwargs["self"]
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
        documentation="""The name specified in the 'CreateSupportBundle API method. If no name was specified, 'supportbundle' will be used. """,
        dictionaryType=None
    )
    extra_args = data_model.property(
        "extraArgs", str,
        array=False, optional=False,
        documentation="""The arguments passed with this method. """,
        dictionaryType=None
    )
    files = data_model.property(
        "files", str,
        array=True, optional=False,
        documentation="""A list of the support bundle files that were created. """,
        dictionaryType=None
    )
    url = data_model.property(
        "url", str,
        array=True, optional=False,
        documentation="""The URL that you can use to download the bundle file(s). Should correspond 1:1 with files list. """,
        dictionaryType=None
    )
    output = data_model.property(
        "output", str,
        array=False, optional=False,
        documentation="""The commands that were run and their output, with newlines replaced by HTML <br> elements. """,
        dictionaryType=None
    )
    timeout_sec = data_model.property(
        "timeoutSec", int,
        array=False, optional=False,
        documentation="""The timeout specified for the support bundle creation process. """,
        dictionaryType=None
    )

    def __init__(self,
            bundle_name,
            extra_args,
            files,
            url,
            output,
            timeout_sec):
        kwargs = locals()
        del kwargs["self"]
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
        documentation="""The details of the support bundle.  """,
        dictionaryType=None
    )
    duration = data_model.property(
        "duration", str,
        array=False, optional=False,
        documentation="""The amount of time required to create the support bundle in the format HH:MM:SS.ssssss """,
        dictionaryType=None
    )
    result = data_model.property(
        "result", str,
        array=False, optional=False,
        documentation="""Whether the support bundle creation passed of failed. """,
        dictionaryType=None
    )

    def __init__(self,
            details,
            duration,
            result):
        kwargs = locals()
        del kwargs["self"]
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
        documentation="""The minimum number of sustained IOPS that are provided by the cluster to a volume.  """,
        dictionaryType=None
    )
    max_iops = data_model.property(
        "maxIOPS", int,
        array=False, optional=False,
        documentation="""The maximum number of sustained IOPS that are provided by the cluster to a volume. """,
        dictionaryType=None
    )
    burst_iops = data_model.property(
        "burstIOPS", int,
        array=False, optional=False,
        documentation="""The maximum number of IOPS allowed in a short burst scenario. """,
        dictionaryType=None
    )

    def __init__(self,
            min_iops,
            max_iops,
            burst_iops):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class SetSnmpInfoRequest(data_model.DataObject):
    """SetSnmpInfoRequest  
    SetSnmpInfo enables you to configure SNMP version 2 and version 3 on cluster nodes. The values you set with this interface apply to
    all nodes in the cluster, and the values that are passed replace, in whole, all values set in any previous call to SetSnmpInfo.
    Note: SetSnmpInfo is deprecated. Use the EnableSnmp and SetSnmpACL methods instead.

    :param networks:  List of networks and what type of access they have to the SNMP servers running on the cluster nodes. See the SNMP Network Object for possible "networks" values. This parameter is required only for SNMP v2. 
    :type networks: SnmpNetwork

    :param enabled:  If set to true, SNMP is enabled on each node in the cluster. 
    :type enabled: bool

    :param snmp_v3_enabled:  If set to true, SNMP v3 is enabled on each node in the cluster. 
    :type snmp_v3_enabled: bool

    :param usm_users:  If SNMP v3 is enabled, this value must be passed in place of the networks parameter. This parameter is required only for SNMP v3. 
    :type usm_users: SnmpV3UsmUser

    """
    networks = data_model.property(
        "networks", SnmpNetwork,
        array=True, optional=True,
        documentation="""List of networks and what type of access they have to the SNMP servers running on the cluster nodes. See the SNMP Network Object for possible "networks" values. This parameter is required only for SNMP v2. """,
        dictionaryType=None
    )
    enabled = data_model.property(
        "enabled", bool,
        array=False, optional=True,
        documentation="""If set to true, SNMP is enabled on each node in the cluster. """,
        dictionaryType=None
    )
    snmp_v3_enabled = data_model.property(
        "snmpV3Enabled", bool,
        array=False, optional=True,
        documentation="""If set to true, SNMP v3 is enabled on each node in the cluster. """,
        dictionaryType=None
    )
    usm_users = data_model.property(
        "usmUsers", SnmpV3UsmUser,
        array=True, optional=True,
        documentation="""If SNMP v3 is enabled, this value must be passed in place of the networks parameter. This parameter is required only for SNMP v3. """,
        dictionaryType=None
    )

    def __init__(self,
            networks=None,
            enabled=None,
            snmp_v3_enabled=None,
            usm_users=None):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class ListStorageContainersRequest(data_model.DataObject):
    """ListStorageContainersRequest  
    ListStorageContainers enables you to retrieve information about all virtual volume storage containers known to the system.

    :param storage_container_ids:  A list of storage container IDs for which to retrieve information. If you omit this parameter, the method returns information about all storage containers in the system. 
    :type storage_container_ids: UUID

    """
    storage_container_ids = data_model.property(
        "storageContainerIDs", UUID,
        array=True, optional=True,
        documentation="""A list of storage container IDs for which to retrieve information. If you omit this parameter, the method returns information about all storage containers in the system. """,
        dictionaryType=None
    )

    def __init__(self,
            storage_container_ids=None):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class GetHardwareInfoResult(data_model.DataObject):
    """GetHardwareInfoResult  

    :param hardware_info: [required] Hardware information for this node.  
    :type hardware_info: dict

    """
    hardware_info = data_model.property(
        "hardwareInfo", dict,
        array=False, optional=False,
        documentation="""Hardware information for this node.  """,
        dictionaryType=None
    )

    def __init__(self,
            hardware_info):
        kwargs = locals()
        del kwargs["self"]
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
        documentation="""List of drive activity information for each drive. """,
        dictionaryType=None
    )
    errors = data_model.property(
        "errors", dict,
        array=True, optional=False,
        documentation="""If there are errors retrieving information about a drive, this list contains the driveID and associated error message. Always present, and empty if there are no errors. """,
        dictionaryType=None
    )

    def __init__(self,
            drive_stats,
            errors):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class ModifyVolumeAccessGroupResult(data_model.DataObject):
    """ModifyVolumeAccessGroupResult  

    :param volume_access_group: [required] An object containing information about the newly modified volume access group. 
    :type volume_access_group: VolumeAccessGroup

    """
    volume_access_group = data_model.property(
        "volumeAccessGroup", VolumeAccessGroup,
        array=False, optional=False,
        documentation="""An object containing information about the newly modified volume access group. """,
        dictionaryType=None
    )

    def __init__(self,
            volume_access_group):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class LoginSessionInfo(data_model.DataObject):
    """LoginSessionInfo  

    :param timeout: [required] The time, in minutes, when this session will timeout and expire. Formatted in H:mm:ss. For example: 1:30:00, 20:00, 5:00. All leading zeros and colons are removed regardless of the format the timeout was entered. 
    :type timeout: str

    """
    timeout = data_model.property(
        "timeout", str,
        array=False, optional=False,
        documentation="""The time, in minutes, when this session will timeout and expire. Formatted in H:mm:ss. For example: 1:30:00, 20:00, 5:00. All leading zeros and colons are removed regardless of the format the timeout was entered. """,
        dictionaryType=None
    )

    def __init__(self,
            timeout):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class GetLoginSessionInfoResult(data_model.DataObject):
    """GetLoginSessionInfoResult  

    :param login_session_info: [required] The authentication expiration period. Formatted in H:mm:ss. For example: 1:30:00, 20:00, 5:00. All leading zeros and colons are removed regardless of the format the timeout was entered. Objects returned are: timeout - The time, in minutes, when this session will timeout and expire. 
    :type login_session_info: LoginSessionInfo

    """
    login_session_info = data_model.property(
        "loginSessionInfo", LoginSessionInfo,
        array=False, optional=False,
        documentation="""The authentication expiration period. Formatted in H:mm:ss. For example: 1:30:00, 20:00, 5:00. All leading zeros and colons are removed regardless of the format the timeout was entered. Objects returned are: timeout - The time, in minutes, when this session will timeout and expire. """,
        dictionaryType=None
    )

    def __init__(self,
            login_session_info):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class ListClusterAdminsResult(data_model.DataObject):
    """ListClusterAdminsResult  

    :param cluster_admins: [required] Information about the cluster admin. 
    :type cluster_admins: ClusterAdmin

    """
    cluster_admins = data_model.property(
        "clusterAdmins", ClusterAdmin,
        array=True, optional=False,
        documentation="""Information about the cluster admin. """,
        dictionaryType=None
    )

    def __init__(self,
            cluster_admins):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class GetNodeStatsResult(data_model.DataObject):
    """GetNodeStatsResult  

    :param node_stats: [required] Node activity information. 
    :type node_stats: NodeStatsInfo

    """
    node_stats = data_model.property(
        "nodeStats", NodeStatsInfo,
        array=False, optional=False,
        documentation="""Node activity information. """,
        dictionaryType=None
    )

    def __init__(self,
            node_stats):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class CreateInitiatorsResult(data_model.DataObject):
    """CreateInitiatorsResult  

    :param initiators: [required] List of objects containing details about the newly created initiators 
    :type initiators: Initiator

    """
    initiators = data_model.property(
        "initiators", Initiator,
        array=True, optional=False,
        documentation="""List of objects containing details about the newly created initiators """,
        dictionaryType=None
    )

    def __init__(self,
            initiators):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class GetRemoteLoggingHostsResult(data_model.DataObject):
    """GetRemoteLoggingHostsResult  

    :param remote_hosts: [required] List of hosts to forward logging information to. 
    :type remote_hosts: LoggingServer

    """
    remote_hosts = data_model.property(
        "remoteHosts", LoggingServer,
        array=True, optional=False,
        documentation="""List of hosts to forward logging information to. """,
        dictionaryType=None
    )

    def __init__(self,
            remote_hosts):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class RemoveClusterPairResult(data_model.DataObject):
    """RemoveClusterPairResult  

    """

    def __init__(self):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class ListVolumesResult(data_model.DataObject):
    """ListVolumesResult  

    :param volumes: [required] List of volumes. 
    :type volumes: Volume

    """
    volumes = data_model.property(
        "volumes", Volume,
        array=True, optional=False,
        documentation="""List of volumes. """,
        dictionaryType=None
    )

    def __init__(self,
            volumes):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class GetHardwareConfigResult(data_model.DataObject):
    """GetHardwareConfigResult  

    :param hardware_config: [required] List of hardware information and current settings. 
    :type hardware_config: dict

    """
    hardware_config = data_model.property(
        "hardwareConfig", dict,
        array=False, optional=False,
        documentation="""List of hardware information and current settings. """,
        dictionaryType=None
    )

    def __init__(self,
            hardware_config):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class GetQoSPolicyRequest(data_model.DataObject):
    """GetQoSPolicyRequest  
    You can use the GetQoSPolicy method to get details about a specific QoSPolicy from the system.

    :param qos_policy_id: [required] The ID of the policy to be retrieved. 
    :type qos_policy_id: int

    """
    qos_policy_id = data_model.property(
        "qosPolicyID", int,
        array=False, optional=False,
        documentation="""The ID of the policy to be retrieved. """,
        dictionaryType=None
    )

    def __init__(self,
            qos_policy_id):
        kwargs = locals()
        del kwargs["self"]
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

    :param qos_policy_count_max: [required]  
    :type qos_policy_count_max: int

    :param secret_length_max: [required]  
    :type secret_length_max: int

    :param schedule_name_length_max: [required]  
    :type schedule_name_length_max: int

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

    :param cluster_admin_account_max:   
    :type cluster_admin_account_max: int

    :param fibre_channel_volume_access_max:   
    :type fibre_channel_volume_access_max: int

    :param virtual_volumes_per_account_count_max:   
    :type virtual_volumes_per_account_count_max: int

    :param virtual_volume_count_max:   
    :type virtual_volume_count_max: int

    """
    account_count_max = data_model.property(
        "accountCountMax", int,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    account_name_length_max = data_model.property(
        "accountNameLengthMax", int,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    account_name_length_min = data_model.property(
        "accountNameLengthMin", int,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    bulk_volume_jobs_per_node_max = data_model.property(
        "bulkVolumeJobsPerNodeMax", int,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    bulk_volume_jobs_per_volume_max = data_model.property(
        "bulkVolumeJobsPerVolumeMax", int,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    clone_jobs_per_volume_max = data_model.property(
        "cloneJobsPerVolumeMax", int,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    cluster_pairs_count_max = data_model.property(
        "clusterPairsCountMax", int,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    initiator_name_length_max = data_model.property(
        "initiatorNameLengthMax", int,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    initiator_count_max = data_model.property(
        "initiatorCountMax", int,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    initiators_per_volume_access_group_count_max = data_model.property(
        "initiatorsPerVolumeAccessGroupCountMax", int,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    iscsi_sessions_from_fibre_channel_nodes_max = data_model.property(
        "iscsiSessionsFromFibreChannelNodesMax", int,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    qos_policy_count_max = data_model.property(
        "qosPolicyCountMax", int,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    secret_length_max = data_model.property(
        "secretLengthMax", int,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    schedule_name_length_max = data_model.property(
        "scheduleNameLengthMax", int,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    secret_length_min = data_model.property(
        "secretLengthMin", int,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    snapshot_name_length_max = data_model.property(
        "snapshotNameLengthMax", int,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    snapshots_per_volume_max = data_model.property(
        "snapshotsPerVolumeMax", int,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    volume_access_group_count_max = data_model.property(
        "volumeAccessGroupCountMax", int,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    volume_access_group_lun_max = data_model.property(
        "volumeAccessGroupLunMax", int,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    volume_access_group_name_length_max = data_model.property(
        "volumeAccessGroupNameLengthMax", int,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    volume_access_group_name_length_min = data_model.property(
        "volumeAccessGroupNameLengthMin", int,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    volume_access_groups_per_initiator_count_max = data_model.property(
        "volumeAccessGroupsPerInitiatorCountMax", int,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    volume_access_groups_per_volume_count_max = data_model.property(
        "volumeAccessGroupsPerVolumeCountMax", int,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    initiator_alias_length_max = data_model.property(
        "initiatorAliasLengthMax", int,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    volume_burst_iopsmax = data_model.property(
        "volumeBurstIOPSMax", int,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    volume_burst_iopsmin = data_model.property(
        "volumeBurstIOPSMin", int,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    volume_count_max = data_model.property(
        "volumeCountMax", int,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    volume_max_iopsmax = data_model.property(
        "volumeMaxIOPSMax", int,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    volume_max_iopsmin = data_model.property(
        "volumeMaxIOPSMin", int,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    volume_min_iopsmax = data_model.property(
        "volumeMinIOPSMax", int,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    volume_min_iopsmin = data_model.property(
        "volumeMinIOPSMin", int,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    volume_name_length_max = data_model.property(
        "volumeNameLengthMax", int,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    volume_name_length_min = data_model.property(
        "volumeNameLengthMin", int,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    volume_size_max = data_model.property(
        "volumeSizeMax", int,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    volume_size_min = data_model.property(
        "volumeSizeMin", int,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    volumes_per_account_count_max = data_model.property(
        "volumesPerAccountCountMax", int,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    volumes_per_group_snapshot_max = data_model.property(
        "volumesPerGroupSnapshotMax", int,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    volumes_per_volume_access_group_count_max = data_model.property(
        "volumesPerVolumeAccessGroupCountMax", int,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    cluster_admin_account_max = data_model.property(
        "clusterAdminAccountMax", int,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )
    fibre_channel_volume_access_max = data_model.property(
        "fibreChannelVolumeAccessMax", int,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )
    virtual_volumes_per_account_count_max = data_model.property(
        "virtualVolumesPerAccountCountMax", int,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )
    virtual_volume_count_max = data_model.property(
        "virtualVolumeCountMax", int,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )

    def __init__(self,
            account_count_max,
            account_name_length_max,
            account_name_length_min,
            bulk_volume_jobs_per_node_max,
            bulk_volume_jobs_per_volume_max,
            clone_jobs_per_volume_max,
            cluster_pairs_count_max,
            initiator_name_length_max,
            initiator_count_max,
            initiators_per_volume_access_group_count_max,
            iscsi_sessions_from_fibre_channel_nodes_max,
            qos_policy_count_max,
            secret_length_max,
            schedule_name_length_max,
            secret_length_min,
            snapshot_name_length_max,
            snapshots_per_volume_max,
            volume_access_group_count_max,
            volume_access_group_lun_max,
            volume_access_group_name_length_max,
            volume_access_group_name_length_min,
            volume_access_groups_per_initiator_count_max,
            volume_access_groups_per_volume_count_max,
            initiator_alias_length_max,
            volume_burst_iopsmax,
            volume_burst_iopsmin,
            volume_count_max,
            volume_max_iopsmax,
            volume_max_iopsmin,
            volume_min_iopsmax,
            volume_min_iopsmin,
            volume_name_length_max,
            volume_name_length_min,
            volume_size_max,
            volume_size_min,
            volumes_per_account_count_max,
            volumes_per_group_snapshot_max,
            volumes_per_volume_access_group_count_max,
            cluster_admin_account_max=None,
            fibre_channel_volume_access_max=None,
            virtual_volumes_per_account_count_max=None,
            virtual_volume_count_max=None):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class RollbackToGroupSnapshotRequest(data_model.DataObject):
    """RollbackToGroupSnapshotRequest  
    RollbackToGroupSnapshot enables you to roll back all individual volumes in a snapshot group to each volume's individual snapshot.
    Note: Rolling back to a group snapshot creates a temporary snapshot of each volume within the group snapshot.
    Snapshots are allowed if cluster fullness is at stage 2 or 3. Snapshots are not created when cluster fullness is at stage 4 or 5.

    :param group_snapshot_id: [required] Specifies the unique ID of the group snapshot. 
    :type group_snapshot_id: int

    :param save_current_state: [required] Specifies whether to save an active volume image or delete it. Values are: true: The previous active volume image is kept. false: (default) The previous active volume image is deleted. 
    :type save_current_state: bool

    :param name:  Name for the group snapshot of the volume's current state that is created if "saveCurrentState" is set to true. If you do not give a name, the name of the snapshots (group and individual volume) are set to a timestamp of the time that the rollback occurred. 
    :type name: str

    :param attributes:  List of name-value pairs in JSON object format. 
    :type attributes: dict

    """
    group_snapshot_id = data_model.property(
        "groupSnapshotID", int,
        array=False, optional=False,
        documentation="""Specifies the unique ID of the group snapshot. """,
        dictionaryType=None
    )
    save_current_state = data_model.property(
        "saveCurrentState", bool,
        array=False, optional=False,
        documentation="""Specifies whether to save an active volume image or delete it. Values are: true: The previous active volume image is kept. false: (default) The previous active volume image is deleted. """,
        dictionaryType=None
    )
    name = data_model.property(
        "name", str,
        array=False, optional=True,
        documentation="""Name for the group snapshot of the volume's current state that is created if "saveCurrentState" is set to true. If you do not give a name, the name of the snapshots (group and individual volume) are set to a timestamp of the time that the rollback occurred. """,
        dictionaryType=None
    )
    attributes = data_model.property(
        "attributes", dict,
        array=False, optional=True,
        documentation="""List of name-value pairs in JSON object format. """,
        dictionaryType=None
    )

    def __init__(self,
            group_snapshot_id,
            save_current_state,
            name=None,
            attributes=None):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class GetBackupTargetRequest(data_model.DataObject):
    """GetBackupTargetRequest  
    GetBackupTarget enables you to return information about a specific backup target that you have created.

    :param backup_target_id: [required] The unique identifier assigned to the backup target. 
    :type backup_target_id: int

    """
    backup_target_id = data_model.property(
        "backupTargetID", int,
        array=False, optional=False,
        documentation="""The unique identifier assigned to the backup target. """,
        dictionaryType=None
    )

    def __init__(self,
            backup_target_id):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class RollbackToGroupSnapshotResult(data_model.DataObject):
    """RollbackToGroupSnapshotResult  

    :param group_snapshot:   
    :type group_snapshot: GroupSnapshot

    :param group_snapshot_id:  Unique ID of the new group snapshot. 
    :type group_snapshot_id: int

    :param members:  List of checksum, volumeIDs and snapshotIDs for each member of the group. 
    :type members: GroupSnapshotMembers

    """
    group_snapshot = data_model.property(
        "groupSnapshot", GroupSnapshot,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )
    group_snapshot_id = data_model.property(
        "groupSnapshotID", int,
        array=False, optional=True,
        documentation="""Unique ID of the new group snapshot. """,
        dictionaryType=None
    )
    members = data_model.property(
        "members", GroupSnapshotMembers,
        array=True, optional=True,
        documentation="""List of checksum, volumeIDs and snapshotIDs for each member of the group. """,
        dictionaryType=None
    )

    def __init__(self,
            group_snapshot=None,
            group_snapshot_id=None,
            members=None):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class DeleteSnapshotResult(data_model.DataObject):
    """DeleteSnapshotResult  

    """

    def __init__(self):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class IpmiInfo(data_model.DataObject):
    """IpmiInfo  

    :param sensors: [required]  
    :type sensors: dict

    """
    sensors = data_model.property(
        "sensors", dict,
        array=True, optional=False,
        documentation=""" """,
        dictionaryType=None
    )

    def __init__(self,
            sensors):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class GetIpmiInfoNodesResultObject(data_model.DataObject):
    """GetIpmiInfoNodesResultObject  

    :param ipmi_info: [required]  
    :type ipmi_info: IpmiInfo

    """
    ipmi_info = data_model.property(
        "ipmiInfo", IpmiInfo,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )

    def __init__(self,
            ipmi_info):
        kwargs = locals()
        del kwargs["self"]
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
        documentation=""" """,
        dictionaryType=None
    )
    result = data_model.property(
        "result", GetIpmiInfoNodesResultObject,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )

    def __init__(self,
            node_id,
            result):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class GetIpmiInfoResult(data_model.DataObject):
    """GetIpmiInfoResult  

    :param nodes: [required] Detailed information from each sensor within a node.  
    :type nodes: GetIpmiInfoNodesResult

    """
    nodes = data_model.property(
        "nodes", GetIpmiInfoNodesResult,
        array=True, optional=False,
        documentation="""Detailed information from each sensor within a node.  """,
        dictionaryType=None
    )

    def __init__(self,
            nodes):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class DeleteStorageContainerResult(data_model.DataObject):
    """DeleteStorageContainerResult  

    """

    def __init__(self):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class ListVirtualVolumeTasksRequest(data_model.DataObject):
    """ListVirtualVolumeTasksRequest  
    ListVirtualVolumeTasks returns a list of virtual volume tasks in the system.

    :param virtual_volume_task_ids:  A list of virtual volume task IDs for which to retrieve information. If you omit this parameter, the method returns information about all virtual volume tasks. 
    :type virtual_volume_task_ids: UUID

    """
    virtual_volume_task_ids = data_model.property(
        "virtualVolumeTaskIDs", UUID,
        array=True, optional=True,
        documentation="""A list of virtual volume task IDs for which to retrieve information. If you omit this parameter, the method returns information about all virtual volume tasks. """,
        dictionaryType=None
    )

    def __init__(self,
            virtual_volume_task_ids=None):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class TestDrivesRequest(data_model.DataObject):
    """TestDrivesRequest  
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
    minutes = data_model.property(
        "minutes", int,
        array=False, optional=True,
        documentation="""Specifies the number of minutes to run the test. """,
        dictionaryType=None
    )
    force = data_model.property(
        "force", bool,
        array=False, optional=True,
        documentation="""Required parameter to successfully test the drives on the node. """,
        dictionaryType=None
    )

    def __init__(self,
            minutes=None,
            force=None):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class ModifyVolumeAccessGroupLunAssignmentsResult(data_model.DataObject):
    """ModifyVolumeAccessGroupLunAssignmentsResult  

    :param volume_access_group_lun_assignments: [required]  
    :type volume_access_group_lun_assignments: VolumeAccessGroupLunAssignments

    """
    volume_access_group_lun_assignments = data_model.property(
        "volumeAccessGroupLunAssignments", VolumeAccessGroupLunAssignments,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )

    def __init__(self,
            volume_access_group_lun_assignments):
        kwargs = locals()
        del kwargs["self"]
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
        documentation=""" """,
        dictionaryType=None
    )
    pubkey = data_model.property(
        "pubkey", str,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    version = data_model.property(
        "version", int,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )

    def __init__(self,
            data,
            pubkey,
            version):
        kwargs = locals()
        del kwargs["self"]
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
        documentation=""" """,
        dictionaryType=None
    )
    contract_date = data_model.property(
        "contract-date", str,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    contract_name = data_model.property(
        "contract-name", str,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    contract_quantity = data_model.property(
        "contract-quantity", int,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    contract_type = data_model.property(
        "contract-type", str,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    integrator = data_model.property(
        "integrator", str,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    location = data_model.property(
        "location", str,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    organization = data_model.property(
        "organization", str,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    type = data_model.property(
        "type", str,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )

    def __init__(self,
            signature,
            contract_date,
            contract_name,
            contract_quantity,
            contract_type,
            integrator,
            location,
            organization,
            type):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class GetOriginNodeResult(data_model.DataObject):
    """GetOriginNodeResult  

    :param origin:   
    :type origin: Origin

    """
    origin = data_model.property(
        "origin", Origin,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )

    def __init__(self,
            origin=None):
        kwargs = locals()
        del kwargs["self"]
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
        documentation=""" """,
        dictionaryType=None
    )
    result = data_model.property(
        "result", GetOriginNodeResult,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )

    def __init__(self,
            node_id,
            result):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class GetOriginResult(data_model.DataObject):
    """GetOriginResult  

    :param nodes: [required]  
    :type nodes: GetOriginNode

    """
    nodes = data_model.property(
        "nodes", GetOriginNode,
        array=True, optional=False,
        documentation=""" """,
        dictionaryType=None
    )

    def __init__(self,
            nodes):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class SetLoginBannerResult(data_model.DataObject):
    """SetLoginBannerResult  

    :param login_banner: [required] 
    :type login_banner: LoginBanner

    """
    login_banner = data_model.property(
        "loginBanner", LoginBanner,
        array=False, optional=False,
        documentation="""""",
        dictionaryType=None
    )

    def __init__(self,
            login_banner):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class ClusterInfo(data_model.DataObject):
    """ClusterInfo  
    Cluster Info object returns information the node uses to communicate with the cluster.

    :param mvip_interface:   
    :type mvip_interface: str

    :param mvip_vlan_tag:   
    :type mvip_vlan_tag: str

    :param svip_interface:   
    :type svip_interface: str

    :param svip_vlan_tag:   
    :type svip_vlan_tag: str

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
    mvip_interface = data_model.property(
        "mvipInterface", str,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )
    mvip_vlan_tag = data_model.property(
        "mvipVlanTag", str,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )
    svip_interface = data_model.property(
        "svipInterface", str,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )
    svip_vlan_tag = data_model.property(
        "svipVlanTag", str,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )
    encryption_at_rest_state = data_model.property(
        "encryptionAtRestState", str,
        array=False, optional=False,
        documentation="""Encryption at rest state. """,
        dictionaryType=None
    )
    ensemble = data_model.property(
        "ensemble", str,
        array=True, optional=False,
        documentation="""Array of Node IP addresses that are participating in the cluster. """,
        dictionaryType=None
    )
    mvip = data_model.property(
        "mvip", str,
        array=False, optional=False,
        documentation="""Management network interface. """,
        dictionaryType=None
    )
    mvip_node_id = data_model.property(
        "mvipNodeID", int,
        array=False, optional=False,
        documentation="""Node holding the master MVIP address """,
        dictionaryType=None
    )
    name = data_model.property(
        "name", str,
        array=False, optional=False,
        documentation="""Unique cluster name. """,
        dictionaryType=None
    )
    rep_count = data_model.property(
        "repCount", int,
        array=False, optional=False,
        documentation="""Number of replicas of each piece of data to store in the cluster. Valid value is 2 """,
        dictionaryType=None
    )
    svip = data_model.property(
        "svip", str,
        array=False, optional=False,
        documentation="""Storage virtual IP """,
        dictionaryType=None
    )
    svip_node_id = data_model.property(
        "svipNodeID", int,
        array=False, optional=False,
        documentation="""Node holding the master SVIP address. """,
        dictionaryType=None
    )
    unique_id = data_model.property(
        "uniqueID", str,
        array=False, optional=False,
        documentation="""Unique ID for the cluster. """,
        dictionaryType=None
    )
    uuid = data_model.property(
        "uuid", UUID,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    attributes = data_model.property(
        "attributes", dict,
        array=False, optional=False,
        documentation="""List of Name/Value pairs in JSON object format. """,
        dictionaryType=None
    )

    def __init__(self,
            encryption_at_rest_state,
            ensemble,
            mvip,
            mvip_node_id,
            name,
            rep_count,
            svip,
            svip_node_id,
            unique_id,
            uuid,
            attributes,
            mvip_interface=None,
            mvip_vlan_tag=None,
            svip_interface=None,
            svip_vlan_tag=None):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class GetClusterInfoResult(data_model.DataObject):
    """GetClusterInfoResult  

    :param cluster_info: [required]  
    :type cluster_info: ClusterInfo

    """
    cluster_info = data_model.property(
        "clusterInfo", ClusterInfo,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )

    def __init__(self,
            cluster_info):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class ListActivePairedVolumesRequest(data_model.DataObject):
    """ListActivePairedVolumesRequest  
    ListActivePairedVolumes enables you to list all the active volumes paired with a volume. This method returns information about volumes with active and pending pairings.

    :param start_volume_id:  The beginning of the range of active paired volumes to return. 
    :type start_volume_id: int

    :param limit:  Maximum number of active paired volumes to return. 
    :type limit: int

    """
    start_volume_id = data_model.property(
        "startVolumeID", int,
        array=False, optional=True,
        documentation="""The beginning of the range of active paired volumes to return. """,
        dictionaryType=None
    )
    limit = data_model.property(
        "limit", int,
        array=False, optional=True,
        documentation="""Maximum number of active paired volumes to return. """,
        dictionaryType=None
    )

    def __init__(self,
            start_volume_id=None,
            limit=None):
        kwargs = locals()
        del kwargs["self"]
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
        documentation="""ID of the async process to be checked for completion. """,
        dictionaryType=None
    )
    key = data_model.property(
        "key", str,
        array=False, optional=False,
        documentation="""Opaque key uniquely identifying the session. """,
        dictionaryType=None
    )
    url = data_model.property(
        "url", str,
        array=False, optional=False,
        documentation="""URL to access the node's web server """,
        dictionaryType=None
    )

    def __init__(self,
            async_handle,
            key,
            url):
        kwargs = locals()
        del kwargs["self"]
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

    :param smart_ssd_write_enabled:   
    :type smart_ssd_write_enabled: bool

    """
    service_id = data_model.property(
        "serviceID", int,
        array=False, optional=False,
        documentation="""Unique identifier for this service. """,
        dictionaryType=None
    )
    service_type = data_model.property(
        "serviceType", str,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    node_id = data_model.property(
        "nodeID", int,
        array=False, optional=False,
        documentation="""The node this service resides on. """,
        dictionaryType=None
    )
    associated_bv = data_model.property(
        "associatedBV", int,
        array=False, optional=True,
        documentation="""This service's associated bulk volume service. This will only be set if the service type is a slice service. """,
        dictionaryType=None
    )
    associated_ts = data_model.property(
        "associatedTS", int,
        array=False, optional=True,
        documentation="""This service's associated transport service. This will only be set if the service type is a slice service. """,
        dictionaryType=None
    )
    associated_vs = data_model.property(
        "associatedVS", int,
        array=False, optional=True,
        documentation="""This service's associated volume service. This will only be set if the service type is a slice service. """,
        dictionaryType=None
    )
    async_result_ids = data_model.property(
        "asyncResultIDs", int,
        array=True, optional=False,
        documentation="""The list of asynchronous jobs currently running for this service. """,
        dictionaryType=None
    )
    drive_id = data_model.property(
        "driveID", int,
        array=False, optional=True,
        documentation="""If this service resides on a drive, the ID of that drive. """,
        dictionaryType=None
    )
    first_time_startup = data_model.property(
        "firstTimeStartup", bool,
        array=False, optional=False,
        documentation="""Has this service started successfully? When a new drive is added to the system, the created service will initially have a value of false here. After the service has started, this value will be set to true. This can be used to check if the service has ever started. """,
        dictionaryType=None
    )
    ipc_port = data_model.property(
        "ipcPort", int,
        array=False, optional=False,
        documentation="""The port used for intra-cluster communication. This will be in the 4000-4100 range. """,
        dictionaryType=None
    )
    iscsi_port = data_model.property(
        "iscsiPort", int,
        array=False, optional=False,
        documentation="""The port used for iSCSI traffic. This will only be set if the service type is a transport service. """,
        dictionaryType=None
    )
    status = data_model.property(
        "status", str,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    started_drive_ids = data_model.property(
        "startedDriveIDs", int,
        array=True, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    drive_ids = data_model.property(
        "driveIDs", int,
        array=True, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    smart_ssd_write_enabled = data_model.property(
        "smartSsdWriteEnabled", bool,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )

    def __init__(self,
            service_id,
            service_type,
            node_id,
            async_result_ids,
            first_time_startup,
            ipc_port,
            iscsi_port,
            status,
            started_drive_ids,
            drive_ids,
            associated_bv=None,
            associated_ts=None,
            associated_vs=None,
            drive_id=None,
            smart_ssd_write_enabled=None):
        kwargs = locals()
        del kwargs["self"]
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

    :param smart_ssd_write_capable:  
    :type smart_ssd_write_capable: bool

    :param attributes: [required] List of Name/Value pairs in JSON object format. 
    :type attributes: dict

    """
    drive_id = data_model.property(
        "driveID", int,
        array=False, optional=False,
        documentation="""A unique identifier for this drive. """,
        dictionaryType=None
    )
    node_id = data_model.property(
        "nodeID", int,
        array=False, optional=False,
        documentation="""The node this drive is located. If the drive has been physically removed from the node, this is where it was last seen. """,
        dictionaryType=None
    )
    assigned_service = data_model.property(
        "assignedService", int,
        array=False, optional=True,
        documentation="""If this drive is hosting a service, the identifier for that service. """,
        dictionaryType=None
    )
    async_result_ids = data_model.property(
        "asyncResultIDs", int,
        array=True, optional=False,
        documentation="""The list of asynchronous jobs currently running on the drive (for example: a secure erase job). """,
        dictionaryType=None
    )
    capacity = data_model.property(
        "capacity", int,
        array=False, optional=False,
        documentation="""The raw capacity of this drive in bytes. """,
        dictionaryType=None
    )
    serial = data_model.property(
        "serial", str,
        array=False, optional=False,
        documentation="""The manufacturer's serial number for this drive. """,
        dictionaryType=None
    )
    slot = data_model.property(
        "slot", int,
        array=False, optional=True,
        documentation="""Slot number in the server chassis where this drive is located. If the drive has been physically removed from the node, this will not have a value. """,
        dictionaryType=None
    )
    drive_status = data_model.property(
        "driveStatus", str,
        array=False, optional=False,
        documentation="""The current status of this drive. """,
        dictionaryType=None
    )
    drive_type = data_model.property(
        "driveType", str,
        array=False, optional=False,
        documentation="""The type of this drive. """,
        dictionaryType=None
    )
    reserved_slice_file_capacity = data_model.property(
        "reservedSliceFileCapacity", int,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )
    customer_slice_file_capacity = data_model.property(
        "customerSliceFileCapacity", int,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )
    smart_ssd_write_capable = data_model.property(
        "smartSsdWriteCapable", bool,
        array=False, optional=True,
        documentation="""""",
        dictionaryType=None
    )
    attributes = data_model.property(
        "attributes", dict,
        array=False, optional=False,
        documentation="""List of Name/Value pairs in JSON object format. """,
        dictionaryType=None
    )

    def __init__(self,
            drive_id,
            node_id,
            async_result_ids,
            capacity,
            serial,
            drive_status,
            drive_type,
            attributes,
            assigned_service=None,
            slot=None,
            reserved_slice_file_capacity=None,
            customer_slice_file_capacity=None,
            smart_ssd_write_capable=None):
        kwargs = locals()
        del kwargs["self"]
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
        documentation=""" """,
        dictionaryType=None
    )
    node = data_model.property(
        "node", Node,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    drive = data_model.property(
        "drive", Drive,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )
    drives = data_model.property(
        "drives", Drive,
        array=True, optional=False,
        documentation=""" """,
        dictionaryType=None
    )

    def __init__(self,
            service,
            node,
            drives,
            drive=None):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class ListServicesResult(data_model.DataObject):
    """ListServicesResult  

    :param services: [required]  
    :type services: DetailedService

    """
    services = data_model.property(
        "services", DetailedService,
        array=True, optional=False,
        documentation=""" """,
        dictionaryType=None
    )

    def __init__(self,
            services):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class ListActiveNodesResult(data_model.DataObject):
    """ListActiveNodesResult  

    :param nodes: [required]  
    :type nodes: Node

    """
    nodes = data_model.property(
        "nodes", Node,
        array=True, optional=False,
        documentation=""" """,
        dictionaryType=None
    )

    def __init__(self,
            nodes):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class ListBackupTargetsResult(data_model.DataObject):
    """ListBackupTargetsResult  

    :param backup_targets: [required] Objects returned for each backup target. 
    :type backup_targets: BackupTarget

    """
    backup_targets = data_model.property(
        "backupTargets", BackupTarget,
        array=True, optional=False,
        documentation="""Objects returned for each backup target. """,
        dictionaryType=None
    )

    def __init__(self,
            backup_targets):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class SnmpSendTestTrapsResult(data_model.DataObject):
    """SnmpSendTestTrapsResult  

    :param status: [required]  
    :type status: str

    """
    status = data_model.property(
        "status", str,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )

    def __init__(self,
            status):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class ListVirtualVolumeBindingsRequest(data_model.DataObject):
    """ListVirtualVolumeBindingsRequest  
    ListVirtualVolumeBindings returns a list of all virtual volumes in the cluster that are bound to protocol endpoints.

    :param virtual_volume_binding_ids:  A list of virtual volume binding IDs for which to retrieve information. If you omit this parameter, the method returns information about all virtual volume bindings. 
    :type virtual_volume_binding_ids: int

    """
    virtual_volume_binding_ids = data_model.property(
        "virtualVolumeBindingIDs", int,
        array=True, optional=True,
        documentation="""A list of virtual volume binding IDs for which to retrieve information. If you omit this parameter, the method returns information about all virtual volume bindings. """,
        dictionaryType=None
    )

    def __init__(self,
            virtual_volume_binding_ids=None):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class ListVolumeStatsByAccountRequest(data_model.DataObject):
    """ListVolumeStatsByAccountRequest  
    ListVolumeStatsByAccount returns high-level activity measurements for every account. Values are summed from all the volumes owned by the account.

    :param accounts:  One or more account ids by which to filter the result. 
    :type accounts: int

    :param include_virtual_volumes:  Includes virtual volumes in the response by default. To exclude virtual volumes, set to false. 
    :type include_virtual_volumes: bool

    """
    accounts = data_model.property(
        "accounts", int,
        array=True, optional=True,
        documentation="""One or more account ids by which to filter the result. """,
        dictionaryType=None
    )
    include_virtual_volumes = data_model.property(
        "includeVirtualVolumes", bool,
        array=False, optional=True,
        documentation="""Includes virtual volumes in the response by default. To exclude virtual volumes, set to false. """,
        dictionaryType=None
    )

    def __init__(self,
            accounts=None,
            include_virtual_volumes=None):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class GetSnmpACLResult(data_model.DataObject):
    """GetSnmpACLResult  

    :param networks:  List of networks and what type of access they have to the SNMP servers running on the cluster nodes. Present if SNMP v3 is disabled. 
    :type networks: SnmpNetwork

    :param usm_users:  List of users and the type of access they have to the SNMP servers running on the cluster nodes. Present if SNMP v3 is enabled. 
    :type usm_users: SnmpV3UsmUser

    """
    networks = data_model.property(
        "networks", SnmpNetwork,
        array=True, optional=True,
        documentation="""List of networks and what type of access they have to the SNMP servers running on the cluster nodes. Present if SNMP v3 is disabled. """,
        dictionaryType=None
    )
    usm_users = data_model.property(
        "usmUsers", SnmpV3UsmUser,
        array=True, optional=True,
        documentation="""List of users and the type of access they have to the SNMP servers running on the cluster nodes. Present if SNMP v3 is enabled. """,
        dictionaryType=None
    )

    def __init__(self,
            networks=None,
            usm_users=None):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class RemoveVirtualNetworkResult(data_model.DataObject):
    """RemoveVirtualNetworkResult  

    """

    def __init__(self):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class EnableSnmpRequest(data_model.DataObject):
    """EnableSnmpRequest  
    EnableSnmp enables you to enable SNMP on cluster nodes. When you enable SNMP, the action applies to all nodes in the cluster, and
    the values that are passed replace, in whole, all values set in any previous call to EnableSnmp.

    :param snmp_v3_enabled: [required] If set to "true", then SNMP v3 is enabled on each node in the cluster. If set to "false", then SNMP v2 is enabled. 
    :type snmp_v3_enabled: bool

    """
    snmp_v3_enabled = data_model.property(
        "snmpV3Enabled", bool,
        array=False, optional=False,
        documentation="""If set to "true", then SNMP v3 is enabled on each node in the cluster. If set to "false", then SNMP v2 is enabled. """,
        dictionaryType=None
    )

    def __init__(self,
            snmp_v3_enabled):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class SetSnmpInfoResult(data_model.DataObject):
    """SetSnmpInfoResult  

    """

    def __init__(self):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class DisableLdapAuthenticationResult(data_model.DataObject):
    """DisableLdapAuthenticationResult  

    """

    def __init__(self):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class ListSnapshotsResult(data_model.DataObject):
    """ListSnapshotsResult  

    :param snapshots: [required] Information about each snapshot for each volume. If volumeID is not provided, all snapshots for all volumes is returned. Snapshots that are in a group will be returned with a "groupID". Snapshots that are enabled for replication. 
    :type snapshots: Snapshot

    """
    snapshots = data_model.property(
        "snapshots", Snapshot,
        array=True, optional=False,
        documentation="""Information about each snapshot for each volume. If volumeID is not provided, all snapshots for all volumes is returned. Snapshots that are in a group will be returned with a "groupID". Snapshots that are enabled for replication. """,
        dictionaryType=None
    )

    def __init__(self,
            snapshots):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class ModifyInitiatorsResult(data_model.DataObject):
    """ModifyInitiatorsResult  

    :param initiators: [required] List of objects containing details about the modified initiators 
    :type initiators: Initiator

    """
    initiators = data_model.property(
        "initiators", Initiator,
        array=True, optional=False,
        documentation="""List of objects containing details about the modified initiators """,
        dictionaryType=None
    )

    def __init__(self,
            initiators):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class CreateClusterRequest(data_model.DataObject):
    """CreateClusterRequest  
    The CreateCluster method enables you to initialize the node in a cluster that has ownership of the "mvip" and "svip" addresses. Each new cluster is initialized using the management IP (MIP) of the first node in the cluster. This method also automatically adds all the nodes being configured into the cluster. You only need to use this method once each time a new cluster is initialized.
    Note: You need to log in to the node that is used as the master node for the cluster. After you log in, run the GetBootstrapConfig method on the node to get the IP addresses for the rest of the nodes that you want to include in the
    cluster. Then, run the CreateCluster method.

    :param accept_eula:  Required to indicate your acceptance of the End User License Agreement when creating this cluster. To accept the EULA, set this parameter to true. 
    :type accept_eula: bool

    :param mvip: [required] Floating (virtual) IP address for the cluster on the management network. 
    :type mvip: str

    :param svip: [required] Floating (virtual) IP address for the cluster on the storage (iSCSI) network. 
    :type svip: str

    :param rep_count: [required] Number of replicas of each piece of data to store in the cluster. Valid value is "2". 
    :type rep_count: int

    :param username: [required] Username for the cluster admin. 
    :type username: str

    :param password: [required] Initial password for the cluster admin account. 
    :type password: str

    :param nodes: [required] CIP/SIP addresses of the initial set of nodes making up the cluster. This node's IP must be in the list. 
    :type nodes: str

    :param attributes:  List of name-value pairs in JSON object format. 
    :type attributes: dict

    """
    accept_eula = data_model.property(
        "acceptEula", bool,
        array=False, optional=True,
        documentation="""Required to indicate your acceptance of the End User License Agreement when creating this cluster. To accept the EULA, set this parameter to true. """,
        dictionaryType=None
    )
    mvip = data_model.property(
        "mvip", str,
        array=False, optional=False,
        documentation="""Floating (virtual) IP address for the cluster on the management network. """,
        dictionaryType=None
    )
    svip = data_model.property(
        "svip", str,
        array=False, optional=False,
        documentation="""Floating (virtual) IP address for the cluster on the storage (iSCSI) network. """,
        dictionaryType=None
    )
    rep_count = data_model.property(
        "repCount", int,
        array=False, optional=False,
        documentation="""Number of replicas of each piece of data to store in the cluster. Valid value is "2". """,
        dictionaryType=None
    )
    username = data_model.property(
        "username", str,
        array=False, optional=False,
        documentation="""Username for the cluster admin. """,
        dictionaryType=None
    )
    password = data_model.property(
        "password", str,
        array=False, optional=False,
        documentation="""Initial password for the cluster admin account. """,
        dictionaryType=None
    )
    nodes = data_model.property(
        "nodes", str,
        array=True, optional=False,
        documentation="""CIP/SIP addresses of the initial set of nodes making up the cluster. This node's IP must be in the list. """,
        dictionaryType=None
    )
    attributes = data_model.property(
        "attributes", dict,
        array=False, optional=True,
        documentation="""List of name-value pairs in JSON object format. """,
        dictionaryType=None
    )

    def __init__(self,
            mvip,
            svip,
            rep_count,
            username,
            password,
            nodes,
            accept_eula=None,
            attributes=None):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class ListEventsRequest(data_model.DataObject):
    """ListEventsRequest  
    ListEvents returns events detected on the cluster, sorted from oldest to newest.

    :param max_events:  Specifies the maximum number of events to return. 
    :type max_events: int

    :param start_event_id:  Identifies the beginning of a range of events to return. 
    :type start_event_id: int

    :param end_event_id:  Identifies the end of a range of events to return. 
    :type end_event_id: int

    :param event_type:  
    :type event_type: str

    """
    max_events = data_model.property(
        "maxEvents", int,
        array=False, optional=True,
        documentation="""Specifies the maximum number of events to return. """,
        dictionaryType=None
    )
    start_event_id = data_model.property(
        "startEventID", int,
        array=False, optional=True,
        documentation="""Identifies the beginning of a range of events to return. """,
        dictionaryType=None
    )
    end_event_id = data_model.property(
        "endEventID", int,
        array=False, optional=True,
        documentation="""Identifies the end of a range of events to return. """,
        dictionaryType=None
    )
    event_type = data_model.property(
        "eventType", str,
        array=False, optional=True,
        documentation="""""",
        dictionaryType=None
    )

    def __init__(self,
            max_events=None,
            start_event_id=None,
            end_event_id=None,
            event_type=None):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class PurgeDeletedVolumesResult(data_model.DataObject):
    """PurgeDeletedVolumesResult  

    """

    def __init__(self):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class ListProtocolEndpointsRequest(data_model.DataObject):
    """ListProtocolEndpointsRequest  
    ListProtocolEndpoints enables you to retrieve information about all protocol endpoints in the cluster. Protocol endpoints govern
    access to their associated virtual volume storage containers.

    :param protocol_endpoint_ids:  A list of protocol endpoint IDs for which to retrieve information. If you omit this parameter, the method returns information about all protocol endpoints. 
    :type protocol_endpoint_ids: UUID

    """
    protocol_endpoint_ids = data_model.property(
        "protocolEndpointIDs", UUID,
        array=True, optional=True,
        documentation="""A list of protocol endpoint IDs for which to retrieve information. If you omit this parameter, the method returns information about all protocol endpoints. """,
        dictionaryType=None
    )

    def __init__(self,
            protocol_endpoint_ids=None):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class ListVolumeAccessGroupsResult(data_model.DataObject):
    """ListVolumeAccessGroupsResult  

    :param volume_access_groups: [required] A list of objects describing each volume access group. 
    :type volume_access_groups: VolumeAccessGroup

    :param volume_access_groups_not_found:  A list of volume access groups not found by the system. Present if you used the "volumeAccessGroups" parameter and the system was unable to find one or more volume access groups that you specified. 
    :type volume_access_groups_not_found: int

    """
    volume_access_groups = data_model.property(
        "volumeAccessGroups", VolumeAccessGroup,
        array=True, optional=False,
        documentation="""A list of objects describing each volume access group. """,
        dictionaryType=None
    )
    volume_access_groups_not_found = data_model.property(
        "volumeAccessGroupsNotFound", int,
        array=True, optional=True,
        documentation="""A list of volume access groups not found by the system. Present if you used the "volumeAccessGroups" parameter and the system was unable to find one or more volume access groups that you specified. """,
        dictionaryType=None
    )

    def __init__(self,
            volume_access_groups,
            volume_access_groups_not_found=None):
        kwargs = locals()
        del kwargs["self"]
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
        documentation="""List of LDAP groups that the tested user is a member of. """,
        dictionaryType=None
    )
    user_dn = data_model.property(
        "userDN", str,
        array=False, optional=False,
        documentation="""The tested user's full LDAP distinguished name. """,
        dictionaryType=None
    )

    def __init__(self,
            groups,
            user_dn):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class ListAccountsResult(data_model.DataObject):
    """ListAccountsResult  

    :param accounts: [required] List of accounts. 
    :type accounts: Account

    """
    accounts = data_model.property(
        "accounts", Account,
        array=True, optional=False,
        documentation="""List of accounts. """,
        dictionaryType=None
    )

    def __init__(self,
            accounts):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class SetSnmpACLRequest(data_model.DataObject):
    """SetSnmpACLRequest  
    SetSnmpACL enables you to configure SNMP access permissions on the cluster nodes. The values you set with this interface apply to all
    nodes in the cluster, and the values that are passed replace, in whole, all values set in any previous call to SetSnmpACL. Also note
    that the values set with this interface replace all network or usmUsers values set with the older SetSnmpInfo.

    :param networks: [required] List of networks and what type of access they have to the SNMP servers running on the cluster nodes. See SNMP Network Object for possible "networks" values. This parameter is required if SNMP v3 is disabled. 
    :type networks: SnmpNetwork

    :param usm_users: [required] List of users and the type of access they have to the SNMP servers running on the cluster nodes. 
    :type usm_users: SnmpV3UsmUser

    """
    networks = data_model.property(
        "networks", SnmpNetwork,
        array=True, optional=False,
        documentation="""List of networks and what type of access they have to the SNMP servers running on the cluster nodes. See SNMP Network Object for possible "networks" values. This parameter is required if SNMP v3 is disabled. """,
        dictionaryType=None
    )
    usm_users = data_model.property(
        "usmUsers", SnmpV3UsmUser,
        array=True, optional=False,
        documentation="""List of users and the type of access they have to the SNMP servers running on the cluster nodes. """,
        dictionaryType=None
    )

    def __init__(self,
            networks,
            usm_users):
        kwargs = locals()
        del kwargs["self"]
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
        documentation="""The VolumeID of the cloned volume. """,
        dictionaryType=None
    )
    src_volume_id = data_model.property(
        "srcVolumeID", int,
        array=False, optional=False,
        documentation="""The VolumeID of the source volume. """,
        dictionaryType=None
    )

    def __init__(self,
            volume_id,
            src_volume_id):
        kwargs = locals()
        del kwargs["self"]
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
        documentation="""A value returned from an asynchronous method call. """,
        dictionaryType=None
    )
    group_clone_id = data_model.property(
        "groupCloneID", int,
        array=False, optional=False,
        documentation="""Unique ID of the new group clone. """,
        dictionaryType=None
    )
    members = data_model.property(
        "members", GroupCloneVolumeMember,
        array=True, optional=False,
        documentation="""List of volumeIDs for the source and destination volume pairs. """,
        dictionaryType=None
    )

    def __init__(self,
            async_handle,
            group_clone_id,
            members):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class RemoveVolumePairRequest(data_model.DataObject):
    """RemoveVolumePairRequest  
    RemoveVolumePair enables you to remove the remote pairing between two volumes. Use this method on both the source and target volumes that are paired together. When you remove the volume pairing information, data is no longer replicated to or from the volume.

    :param volume_id: [required] The ID of the volume on which to stop the replication process. 
    :type volume_id: int

    """
    volume_id = data_model.property(
        "volumeID", int,
        array=False, optional=False,
        documentation="""The ID of the volume on which to stop the replication process. """,
        dictionaryType=None
    )

    def __init__(self,
            volume_id):
        kwargs = locals()
        del kwargs["self"]
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
        documentation=""" """,
        dictionaryType=None
    )
    deduplication = data_model.property(
        "deduplication", float,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    missing_volumes = data_model.property(
        "missingVolumes", int,
        array=True, optional=False,
        documentation="""The volumes that could not be queried for efficiency data. Missing volumes can be caused by the Garbage Collection (GC) cycle being less than an hour old, temporary loss of network connectivity, or restarted services since the GC cycle. """,
        dictionaryType=None
    )
    thin_provisioning = data_model.property(
        "thinProvisioning", float,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    timestamp = data_model.property(
        "timestamp", str,
        array=False, optional=False,
        documentation="""The last time efficiency data was collected after Garbage Collection (GC). """,
        dictionaryType=None
    )

    def __init__(self,
            compression,
            deduplication,
            missing_volumes,
            thin_provisioning,
            timestamp):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class SetLoginSessionInfoResult(data_model.DataObject):
    """SetLoginSessionInfoResult  

    """

    def __init__(self):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class AsyncHandleResult(data_model.DataObject):
    """AsyncHandleResult  

    :param async_handle: [required]  
    :type async_handle: int

    """
    async_handle = data_model.property(
        "asyncHandle", int,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )

    def __init__(self,
            async_handle):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class PurgeDeletedVolumeRequest(data_model.DataObject):
    """PurgeDeletedVolumeRequest  
    PurgeDeletedVolume immediately and permanently purges a volume that has been deleted. You must delete a volume using
    DeleteVolume before it can be purged. Volumes are purged automatically after a period of time, so usage of this method is not
    typically required.

    :param volume_id: [required] The ID of the volume to be purged. 
    :type volume_id: int

    """
    volume_id = data_model.property(
        "volumeID", int,
        array=False, optional=False,
        documentation="""The ID of the volume to be purged. """,
        dictionaryType=None
    )

    def __init__(self,
            volume_id):
        kwargs = locals()
        del kwargs["self"]
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

    :param remaining_time:   
    :type remaining_time: int

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
    :type stage: str

    :param group_clone_id:   
    :type group_clone_id: int

    """
    bytes_per_second = data_model.property(
        "bytesPerSecond", float,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    current_bytes = data_model.property(
        "currentBytes", int,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    dst_service_id = data_model.property(
        "dstServiceID", int,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    elapsed_time = data_model.property(
        "elapsedTime", float,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    percent_complete = data_model.property(
        "percentComplete", float,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    remaining_time = data_model.property(
        "remainingTime", int,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )
    slice_id = data_model.property(
        "sliceID", int,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    src_service_id = data_model.property(
        "srcServiceID", int,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    total_bytes = data_model.property(
        "totalBytes", int,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    type = data_model.property(
        "type", str,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    clone_id = data_model.property(
        "cloneID", int,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    dst_volume_id = data_model.property(
        "dstVolumeID", int,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    node_id = data_model.property(
        "nodeID", int,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    snapshot_id = data_model.property(
        "snapshotID", int,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    src_volume_id = data_model.property(
        "srcVolumeID", int,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    blocks_per_second = data_model.property(
        "blocksPerSecond", float,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    stage = data_model.property(
        "stage", str,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    group_clone_id = data_model.property(
        "groupCloneID", int,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )

    def __init__(self,
            bytes_per_second,
            current_bytes,
            dst_service_id,
            elapsed_time,
            percent_complete,
            slice_id,
            src_service_id,
            total_bytes,
            type,
            clone_id,
            dst_volume_id,
            node_id,
            snapshot_id,
            src_volume_id,
            blocks_per_second,
            stage,
            remaining_time=None,
            group_clone_id=None):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class ListSyncJobsResult(data_model.DataObject):
    """ListSyncJobsResult  

    :param sync_jobs: [required]  
    :type sync_jobs: SyncJob

    """
    sync_jobs = data_model.property(
        "syncJobs", SyncJob,
        array=True, optional=False,
        documentation=""" """,
        dictionaryType=None
    )

    def __init__(self,
            sync_jobs):
        kwargs = locals()
        del kwargs["self"]
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

    :param script:  The name of the script if one is provided. 
    :type script: str

    :param snapshot_id:  ID of the snapshot if a snapshot is in the source of the bulk volume job. 
    :type snapshot_id: int

    :param type: [required] Can be one of the following: read write 
    :type type: str

    :param attributes: [required] JSON attributes on the bulk volume job. 
    :type attributes: dict

    """
    bulk_volume_id = data_model.property(
        "bulkVolumeID", int,
        array=False, optional=False,
        documentation="""The internal bulk volume job ID. """,
        dictionaryType=None
    )
    create_time = data_model.property(
        "createTime", str,
        array=False, optional=False,
        documentation="""Timestamp created for the bulk volume job. """,
        dictionaryType=None
    )
    elapsed_time = data_model.property(
        "elapsedTime", int,
        array=False, optional=False,
        documentation="""The number of seconds since the job began. """,
        dictionaryType=None
    )
    format = data_model.property(
        "format", str,
        array=False, optional=False,
        documentation="""Format is either "compressed" or "native". """,
        dictionaryType=None
    )
    key = data_model.property(
        "key", str,
        array=False, optional=False,
        documentation="""The unique key created by the bulk volume session. """,
        dictionaryType=None
    )
    percent_complete = data_model.property(
        "percentComplete", int,
        array=False, optional=False,
        documentation="""The completed percentage reported by the operation. """,
        dictionaryType=None
    )
    remaining_time = data_model.property(
        "remainingTime", int,
        array=False, optional=False,
        documentation="""The estimated time remaining in seconds. """,
        dictionaryType=None
    )
    src_volume_id = data_model.property(
        "srcVolumeID", int,
        array=False, optional=False,
        documentation="""The source volume ID. """,
        dictionaryType=None
    )
    status = data_model.property(
        "status", str,
        array=False, optional=False,
        documentation="""Can be one of the following: preparing active done failed """,
        dictionaryType=None
    )
    script = data_model.property(
        "script", str,
        array=False, optional=True,
        documentation="""The name of the script if one is provided. """,
        dictionaryType=None
    )
    snapshot_id = data_model.property(
        "snapshotID", int,
        array=False, optional=True,
        documentation="""ID of the snapshot if a snapshot is in the source of the bulk volume job. """,
        dictionaryType=None
    )
    type = data_model.property(
        "type", str,
        array=False, optional=False,
        documentation="""Can be one of the following: read write """,
        dictionaryType=None
    )
    attributes = data_model.property(
        "attributes", dict,
        array=False, optional=False,
        documentation="""JSON attributes on the bulk volume job. """,
        dictionaryType=None
    )

    def __init__(self,
            bulk_volume_id,
            create_time,
            elapsed_time,
            format,
            key,
            percent_complete,
            remaining_time,
            src_volume_id,
            status,
            type,
            attributes,
            script=None,
            snapshot_id=None):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class ListBulkVolumeJobsResult(data_model.DataObject):
    """ListBulkVolumeJobsResult  

    :param bulk_volume_jobs: [required] An array of information for each bulk volume job. 
    :type bulk_volume_jobs: BulkVolumeJob

    """
    bulk_volume_jobs = data_model.property(
        "bulkVolumeJobs", BulkVolumeJob,
        array=True, optional=False,
        documentation="""An array of information for each bulk volume job. """,
        dictionaryType=None
    )

    def __init__(self,
            bulk_volume_jobs):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class TestConnectMvipRequest(data_model.DataObject):
    """TestConnectMvipRequest  
    The TestConnectMvip API method enables you to test the
    management connection to the cluster. The test pings the MVIP and executes a simple API method to verify connectivity.
    Note: This method is available only through the per-node API endpoint 5.0 or later.

    :param mvip:  If specified, tests the management connection of a different MVIP. You do not need to use this value when testing the connection to the target cluster. This parameter is optional. 
    :type mvip: str

    """
    mvip = data_model.property(
        "mvip", str,
        array=False, optional=True,
        documentation="""If specified, tests the management connection of a different MVIP. You do not need to use this value when testing the connection to the target cluster. This parameter is optional. """,
        dictionaryType=None
    )

    def __init__(self,
            mvip=None):
        kwargs = locals()
        del kwargs["self"]
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
        documentation="""If the nodes in the cluster are configured for SNMP. """,
        dictionaryType=None
    )
    snmp_v3_enabled = data_model.property(
        "snmpV3Enabled", bool,
        array=False, optional=False,
        documentation="""If the node in the cluster is configured for SNMP v3. """,
        dictionaryType=None
    )

    def __init__(self,
            enabled,
            snmp_v3_enabled):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class ListPendingActiveNodesResult(data_model.DataObject):
    """ListPendingActiveNodesResult  

    :param pending_active_nodes: [required] List of objects detailing information about all PendingActive nodes in the system. 
    :type pending_active_nodes: PendingActiveNode

    """
    pending_active_nodes = data_model.property(
        "pendingActiveNodes", PendingActiveNode,
        array=True, optional=False,
        documentation="""List of objects detailing information about all PendingActive nodes in the system. """,
        dictionaryType=None
    )

    def __init__(self,
            pending_active_nodes):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class CompleteVolumePairingRequest(data_model.DataObject):
    """CompleteVolumePairingRequest  
    You can use the CompleteVolumePairing method to complete the pairing of two volumes.

    :param volume_pairing_key: [required] The key returned from the StartVolumePairing method. 
    :type volume_pairing_key: str

    :param volume_id: [required] The ID of the volume on which to complete the pairing process. 
    :type volume_id: int

    """
    volume_pairing_key = data_model.property(
        "volumePairingKey", str,
        array=False, optional=False,
        documentation="""The key returned from the StartVolumePairing method. """,
        dictionaryType=None
    )
    volume_id = data_model.property(
        "volumeID", int,
        array=False, optional=False,
        documentation="""The ID of the volume on which to complete the pairing process. """,
        dictionaryType=None
    )

    def __init__(self,
            volume_pairing_key,
            volume_id):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class GetClusterStateRequest(data_model.DataObject):
    """GetClusterStateRequest  
    The GetClusterState API method enables you to indicate if a node is part of a cluster or not. The three states are:
    Available: Node has not been configured with a cluster name.
    Pending: Node is pending for a specific named cluster and can be added.
    Active: Node is an active member of a cluster and may not be added to another
    cluster.
    Note: This method is available only through the per-node API endpoint 5.0 or later.

    :param force: [required] To run this command, the force parameter must be set to true. 
    :type force: bool

    """
    force = data_model.property(
        "force", bool,
        array=False, optional=False,
        documentation="""To run this command, the force parameter must be set to true. """,
        dictionaryType=None
    )

    def __init__(self,
            force):
        kwargs = locals()
        del kwargs["self"]
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
        documentation=""" """,
        dictionaryType=None
    )
    connected = data_model.property(
        "connected", bool,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    dev = data_model.property(
        "dev", int,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    dev_path = data_model.property(
        "devPath", str,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    drive_type = data_model.property(
        "driveType", str,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    life_remaining_percent = data_model.property(
        "lifeRemainingPercent", int,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    lifetime_read_bytes = data_model.property(
        "lifetimeReadBytes", int,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    lifetime_write_bytes = data_model.property(
        "lifetimeWriteBytes", int,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    name = data_model.property(
        "name", str,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    path = data_model.property(
        "path", str,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    path_link = data_model.property(
        "pathLink", str,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    power_on_hours = data_model.property(
        "powerOnHours", int,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    product = data_model.property(
        "product", str,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    reallocated_sectors = data_model.property(
        "reallocatedSectors", int,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    reserve_capacity_percent = data_model.property(
        "reserveCapacityPercent", int,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    scsi_compat_id = data_model.property(
        "scsiCompatId", str,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    scsi_state = data_model.property(
        "scsiState", str,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    security_at_maximum = data_model.property(
        "securityAtMaximum", bool,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    security_enabled = data_model.property(
        "securityEnabled", bool,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    security_frozen = data_model.property(
        "securityFrozen", bool,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    security_locked = data_model.property(
        "securityLocked", bool,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    security_supported = data_model.property(
        "securitySupported", bool,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    serial = data_model.property(
        "serial", str,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    size = data_model.property(
        "size", int,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    slot = data_model.property(
        "slot", int,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    smart_ssd_write_capable = data_model.property(
        "smartSsdWriteCapable", bool,
        array=False, optional=True,
        documentation=""" """,
        dictionaryType=None
    )
    uuid = data_model.property(
        "uuid", UUID,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    vendor = data_model.property(
        "vendor", str,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    version = data_model.property(
        "version", str,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )

    def __init__(self,
            canonical_name,
            connected,
            dev,
            dev_path,
            drive_type,
            life_remaining_percent,
            lifetime_read_bytes,
            lifetime_write_bytes,
            name,
            path,
            path_link,
            power_on_hours,
            product,
            reallocated_sectors,
            reserve_capacity_percent,
            scsi_compat_id,
            scsi_state,
            security_at_maximum,
            security_enabled,
            security_frozen,
            security_locked,
            security_supported,
            serial,
            size,
            slot,
            uuid,
            vendor,
            version,
            smart_ssd_write_capable=None):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class DrivesHardware(data_model.DataObject):
    """DrivesHardware  

    :param drive_hardware: [required]  
    :type drive_hardware: DriveHardware

    """
    drive_hardware = data_model.property(
        "driveHardware", DriveHardware,
        array=True, optional=False,
        documentation=""" """,
        dictionaryType=None
    )

    def __init__(self,
            drive_hardware):
        kwargs = locals()
        del kwargs["self"]
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
        documentation=""" """,
        dictionaryType=None
    )
    result = data_model.property(
        "result", DrivesHardware,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )

    def __init__(self,
            node_id,
            result):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class ListDriveHardwareResult(data_model.DataObject):
    """ListDriveHardwareResult  

    :param nodes: [required]  
    :type nodes: NodeDriveHardware

    """
    nodes = data_model.property(
        "nodes", NodeDriveHardware,
        array=True, optional=False,
        documentation=""" """,
        dictionaryType=None
    )

    def __init__(self,
            nodes):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class GetNodeHardwareInfoResult(data_model.DataObject):
    """GetNodeHardwareInfoResult  

    :param node_hardware_info: [required] Hardware information for the specified nodeID. 
    :type node_hardware_info: dict

    """
    node_hardware_info = data_model.property(
        "nodeHardwareInfo", dict,
        array=False, optional=False,
        documentation="""Hardware information for the specified nodeID. """,
        dictionaryType=None
    )

    def __init__(self,
            node_hardware_info):
        kwargs = locals()
        del kwargs["self"]
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
        documentation="""List of hosts that are to receive the traps generated by the cluster. """,
        dictionaryType=None
    )
    cluster_fault_traps_enabled = data_model.property(
        "clusterFaultTrapsEnabled", bool,
        array=False, optional=False,
        documentation="""If "true", when a cluster fault is logged a corresponding solidFireClusterFaultNotification is sent to the configured list of trap recipients. """,
        dictionaryType=None
    )
    cluster_fault_resolved_traps_enabled = data_model.property(
        "clusterFaultResolvedTrapsEnabled", bool,
        array=False, optional=False,
        documentation="""If "true", when a cluster fault is logged a corresponding solidFireClusterFaultResolvedNotification is sent to the configured list of trap recipients. """,
        dictionaryType=None
    )
    cluster_event_traps_enabled = data_model.property(
        "clusterEventTrapsEnabled", bool,
        array=False, optional=False,
        documentation="""If "true", when a cluster fault is logged a corresponding solidFireClusterEventNotification is sent to the configured list of trap recipients. """,
        dictionaryType=None
    )

    def __init__(self,
            trap_recipients,
            cluster_fault_traps_enabled,
            cluster_fault_resolved_traps_enabled,
            cluster_event_traps_enabled):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class SetRemoteLoggingHostsResult(data_model.DataObject):
    """SetRemoteLoggingHostsResult  

    """

    def __init__(self):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class SetClusterConfigRequest(data_model.DataObject):
    """SetClusterConfigRequest  
    The SetClusterConfig API method enables you to set the configuration this node uses to communicate with the cluster it is associated with. To see the states in which these objects can be modified, see Cluster Object Attributes. To display the current cluster
    interface settings for a node, run the GetClusterConfig API method.
    Note: This method is available only through the per-node API endpoint 5.0 or later.

    :param cluster: [required] Objects that are changed for the cluster interface settings. 
    :type cluster: ClusterConfig

    """
    cluster = data_model.property(
        "cluster", ClusterConfig,
        array=False, optional=False,
        documentation="""Objects that are changed for the cluster interface settings. """,
        dictionaryType=None
    )

    def __init__(self,
            cluster):
        kwargs = locals()
        del kwargs["self"]
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
        documentation="""Drive name """,
        dictionaryType=None
    )
    return_code = data_model.property(
        "returnCode", int,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    stderr = data_model.property(
        "stderr", str,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    stdout = data_model.property(
        "stdout", str,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )

    def __init__(self,
            drive,
            return_code,
            stderr,
            stdout):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class ResetDrivesDetails(data_model.DataObject):
    """ResetDrivesDetails  

    :param drives: [required] Details of a single drive that is being reset. 
    :type drives: ResetDriveDetails

    """
    drives = data_model.property(
        "drives", ResetDriveDetails,
        array=True, optional=False,
        documentation="""Details of a single drive that is being reset. """,
        dictionaryType=None
    )

    def __init__(self,
            drives):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class ResetDrivesResult(data_model.DataObject):
    """ResetDrivesResult  

    :param details: [required] Details of drives that are being reset. 
    :type details: ResetDrivesDetails

    :param duration:  
    :type duration: str

    :param result:  
    :type result: str

    """
    details = data_model.property(
        "details", ResetDrivesDetails,
        array=False, optional=False,
        documentation="""Details of drives that are being reset. """,
        dictionaryType=None
    )
    duration = data_model.property(
        "duration", str,
        array=False, optional=True,
        documentation="""""",
        dictionaryType=None
    )
    result = data_model.property(
        "result", str,
        array=False, optional=True,
        documentation="""""",
        dictionaryType=None
    )

    def __init__(self,
            details,
            duration=None,
            result=None):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class ListAccountsRequest(data_model.DataObject):
    """ListAccountsRequest  
    ListAccounts returns the entire list of accounts, with optional paging support.

    :param start_account_id:  Starting AccountID to return. If no account exists with this AccountID, the next account by AccountID order is used as the start of the list. To page through the list, pass the AccountID of the last account in the previous response + 1. 
    :type start_account_id: int

    :param limit:  Maximum number of AccountInfo objects to return. 
    :type limit: int

    :param include_storage_containers:  Includes storage containers in the response by default. To exclude storage containers, set to false. 
    :type include_storage_containers: bool

    """
    start_account_id = data_model.property(
        "startAccountID", int,
        array=False, optional=True,
        documentation="""Starting AccountID to return. If no account exists with this AccountID, the next account by AccountID order is used as the start of the list. To page through the list, pass the AccountID of the last account in the previous response + 1. """,
        dictionaryType=None
    )
    limit = data_model.property(
        "limit", int,
        array=False, optional=True,
        documentation="""Maximum number of AccountInfo objects to return. """,
        dictionaryType=None
    )
    include_storage_containers = data_model.property(
        "includeStorageContainers", bool,
        array=False, optional=True,
        documentation="""Includes storage containers in the response by default. To exclude storage containers, set to false. """,
        dictionaryType=None
    )

    def __init__(self,
            start_account_id=None,
            limit=None,
            include_storage_containers=None):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class ModifyClusterFullThresholdRequest(data_model.DataObject):
    """ModifyClusterFullThresholdRequest  
    You can use ModifyClusterFullThreshold to change the level at which the system generates an event when the storage cluster approaches a certain capacity utilization. You can use the threshold setting to indicate the acceptable amount of utilized block storage before the system generates a warning. For example, if you want to be alerted when the system reaches 3% below the "Error" level block storage utilization, enter a value of "3" for the stage3BlockThresholdPercent parameter. If this level is reached, the system sends an alert to the Event Log in the Cluster Management Console.

    :param stage2_aware_threshold:  The number of nodes of capacity remaining in the cluster before the system triggers a capacity notification. 
    :type stage2_aware_threshold: int

    :param stage3_block_threshold_percent:  The percentage of block storage utilization below the "Error" threshold that causes the system to trigger a cluster "Warning" alert. 
    :type stage3_block_threshold_percent: int

    :param max_metadata_over_provision_factor:  A value representative of the number of times metadata space can be overprovisioned relative to the amount of space available. For example, if there was enough metadata space to store 100 TiB of volumes and this number was set to 5, then 500 TiB worth of volumes can be created. 
    :type max_metadata_over_provision_factor: int

    """
    stage2_aware_threshold = data_model.property(
        "stage2AwareThreshold", int,
        array=False, optional=True,
        documentation="""The number of nodes of capacity remaining in the cluster before the system triggers a capacity notification. """,
        dictionaryType=None
    )
    stage3_block_threshold_percent = data_model.property(
        "stage3BlockThresholdPercent", int,
        array=False, optional=True,
        documentation="""The percentage of block storage utilization below the "Error" threshold that causes the system to trigger a cluster "Warning" alert. """,
        dictionaryType=None
    )
    max_metadata_over_provision_factor = data_model.property(
        "maxMetadataOverProvisionFactor", int,
        array=False, optional=True,
        documentation="""A value representative of the number of times metadata space can be overprovisioned relative to the amount of space available. For example, if there was enough metadata space to store 100 TiB of volumes and this number was set to 5, then 500 TiB worth of volumes can be created. """,
        dictionaryType=None
    )

    def __init__(self,
            stage2_aware_threshold=None,
            stage3_block_threshold_percent=None,
            max_metadata_over_provision_factor=None):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class AddClusterAdminRequest(data_model.DataObject):
    """AddClusterAdminRequest  
    You can use AddClusterAdmin to add a new cluster admin account. A cluster ddmin can manage the cluster using the API and management tools. Cluster admins are completely separate and unrelated to standard tenant accounts.
    Each cluster admin can be restricted to a subset of the API. NetApp recommends using multiple cluster admin accounts for different users and applications. You should give each cluster admin the minimal permissions necessary; this reduces the potential impact of credential compromise.
    You must accept the End User License Agreement (EULA) by setting the acceptEula parameter to true to add a cluster administrator account to the system.

    :param username: [required] Unique username for this cluster admin. Must be between 1 and 1024 characters in length. 
    :type username: str

    :param password: [required] Password used to authenticate this cluster admin. 
    :type password: str

    :param access: [required] Controls which methods this cluster admin can use. For more details on the levels of access, see Access Control in the Element API Reference Guide. 
    :type access: str

    :param accept_eula:  Required to indicate your acceptance of the End User License Agreement when creating this cluster. To accept the EULA, set this parameter to true. 
    :type accept_eula: bool

    :param attributes:  List of name-value pairs in JSON object format. 
    :type attributes: dict

    """
    username = data_model.property(
        "username", str,
        array=False, optional=False,
        documentation="""Unique username for this cluster admin. Must be between 1 and 1024 characters in length. """,
        dictionaryType=None
    )
    password = data_model.property(
        "password", str,
        array=False, optional=False,
        documentation="""Password used to authenticate this cluster admin. """,
        dictionaryType=None
    )
    access = data_model.property(
        "access", str,
        array=True, optional=False,
        documentation="""Controls which methods this cluster admin can use. For more details on the levels of access, see Access Control in the Element API Reference Guide. """,
        dictionaryType=None
    )
    accept_eula = data_model.property(
        "acceptEula", bool,
        array=False, optional=True,
        documentation="""Required to indicate your acceptance of the End User License Agreement when creating this cluster. To accept the EULA, set this parameter to true. """,
        dictionaryType=None
    )
    attributes = data_model.property(
        "attributes", dict,
        array=False, optional=True,
        documentation="""List of name-value pairs in JSON object format. """,
        dictionaryType=None
    )

    def __init__(self,
            username,
            password,
            access,
            accept_eula=None,
            attributes=None):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class EnableFeatureResult(data_model.DataObject):
    """EnableFeatureResult  

    """

    def __init__(self):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class RemoveBackupTargetResult(data_model.DataObject):
    """RemoveBackupTargetResult  

    """

    def __init__(self):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class CloneVolumeRequest(data_model.DataObject):
    """CloneVolumeRequest  
    CloneVolume enables you to create a copy of a volume. This method is asynchronous and might take a variable amount of time to complete. The cloning process begins immediately when you make the CloneVolume request and is representative of the state of the volume when the API method is issued. You can use the GetAsyncResult method to determine when the cloning process is complete and the new volume is available for connections. You can use ListSyncJobs to see the progress of creating the clone.
    Note: The initial attributes and QoS settings for the volume are inherited from the volume being cloned. You can change these settings with ModifyVolume.
    Note: Cloned volumes do not inherit volume access group memberships from the source volume.

    :param volume_id: [required] VolumeID for the volume to be cloned. 
    :type volume_id: int

    :param name: [required] The name of the new cloned volume. Might be 1 to 64 characters in length. 
    :type name: str

    :param new_account_id:  AccountID for the owner of the new volume. If unspecified, the accountID of the owner of the volume being cloned is used. 
    :type new_account_id: int

    :param new_size:  New size of the volume, in bytes. Might be greater or less than the size of the volume being cloned. If unspecified, the volume size is not changed. Size is rounded to the nearest 1MB. 
    :type new_size: int

    :param access:  Specifies the level of access allowed for the new volume. Possible values are: readOnly: Only read operations are allowed. readWrite: Reads and writes are allowed. locked: No reads or writes are allowed. If unspecified, the level of access of the volume being cloned is used. replicationTarget: Identify a volume as the target volume for a paired set of volumes. If the volume is not paired, the access status is locked. If a value is not specified, the access value does not change. 
    :type access: str

    :param snapshot_id:  ID of the snapshot that is used as the source of the clone. If no ID is provided, the current active volume is used. 
    :type snapshot_id: int

    :param attributes:  List of name-value pairs in JSON object format. 
    :type attributes: dict

    :param enable512e:  Should the volume provide 512-byte sector emulation? 
    :type enable512e: bool

    """
    volume_id = data_model.property(
        "volumeID", int,
        array=False, optional=False,
        documentation="""VolumeID for the volume to be cloned. """,
        dictionaryType=None
    )
    name = data_model.property(
        "name", str,
        array=False, optional=False,
        documentation="""The name of the new cloned volume. Might be 1 to 64 characters in length. """,
        dictionaryType=None
    )
    new_account_id = data_model.property(
        "newAccountID", int,
        array=False, optional=True,
        documentation="""AccountID for the owner of the new volume. If unspecified, the accountID of the owner of the volume being cloned is used. """,
        dictionaryType=None
    )
    new_size = data_model.property(
        "newSize", int,
        array=False, optional=True,
        documentation="""New size of the volume, in bytes. Might be greater or less than the size of the volume being cloned. If unspecified, the volume size is not changed. Size is rounded to the nearest 1MB. """,
        dictionaryType=None
    )
    access = data_model.property(
        "access", str,
        array=False, optional=True,
        documentation="""Specifies the level of access allowed for the new volume. Possible values are: readOnly: Only read operations are allowed. readWrite: Reads and writes are allowed. locked: No reads or writes are allowed. If unspecified, the level of access of the volume being cloned is used. replicationTarget: Identify a volume as the target volume for a paired set of volumes. If the volume is not paired, the access status is locked. If a value is not specified, the access value does not change. """,
        dictionaryType=None
    )
    snapshot_id = data_model.property(
        "snapshotID", int,
        array=False, optional=True,
        documentation="""ID of the snapshot that is used as the source of the clone. If no ID is provided, the current active volume is used. """,
        dictionaryType=None
    )
    attributes = data_model.property(
        "attributes", dict,
        array=False, optional=True,
        documentation="""List of name-value pairs in JSON object format. """,
        dictionaryType=None
    )
    enable512e = data_model.property(
        "enable512e", bool,
        array=False, optional=True,
        documentation="""Should the volume provide 512-byte sector emulation? """,
        dictionaryType=None
    )

    def __init__(self,
            volume_id,
            name,
            new_account_id=None,
            new_size=None,
            access=None,
            snapshot_id=None,
            attributes=None,
            enable512e=None):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class CreateBackupTargetRequest(data_model.DataObject):
    """CreateBackupTargetRequest  
    CreateBackupTarget enables you to create and store backup target information so that you do not need to re-enter it each time a backup is created.

    :param name: [required] The name of the backup target. 
    :type name: str

    :param attributes: [required] List of name-value pairs in JSON object format. 
    :type attributes: dict

    """
    name = data_model.property(
        "name", str,
        array=False, optional=False,
        documentation="""The name of the backup target. """,
        dictionaryType=None
    )
    attributes = data_model.property(
        "attributes", dict,
        array=False, optional=False,
        documentation="""List of name-value pairs in JSON object format. """,
        dictionaryType=None
    )

    def __init__(self,
            name,
            attributes):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class ModifyVolumeRequest(data_model.DataObject):
    """ModifyVolumeRequest  
    ModifyVolume enables you to modify settings on an existing volume. You can make modifications to one volume at a time and
    changes take place immediately. If you do not specify QoS values when you modify a volume, they remain the same as before the modification. You can retrieve
    default QoS values for a newly created volume by running the GetDefaultQoS method.
    When you need to increase the size of a volume that is being replicated, do so in the following order to prevent replication errors:
    1. Increase the size of the "Replication Target" volume.
    2. Increase the size of the source or "Read / Write" volume.
    NetApp recommends that both the target and source volumes are the same size.
    Note: If you change the "access" status to locked or target, all existing iSCSI connections are terminated.

    :param volume_id: [required] VolumeID for the volume to be modified. 
    :type volume_id: int

    :param account_id:  AccountID to which the volume is reassigned. If unspecified, the previous account name is used. 
    :type account_id: int

    :param access:  Specifies the access allowed for the volume. Possible values are: readOnly: Only read operations are allowed. readWrite: Reads and writes are allowed. locked: No reads or writes are allowed. If not specified, the access value does not change. replicationTarget: Identify a volume as the target volume for a paired set of volumes. If the volume is not paired, the access status is locked. If a value is not specified, the access value does not change. 
    :type access: str

    :param qos:  New QoS settings for this volume. If not specified, the QoS settings are not changed. 
    :type qos: QoS

    :param total_size:  New size of the volume in bytes. 1000000000 is equal to 1GB. Size is rounded up to the nearest 1MB. This parameter can only be used to increase the size of a volume. 
    :type total_size: int

    :param attributes:  List of name-value pairs in JSON object format. 
    :type attributes: dict

    :param associate_with_qos_policy:  Associate the volume with the specified QoS policy. Possible values: true: Associate the volume with the QoS policy specified in the QoSPolicyID parameter. false: Do not assosciate the volume with the QoS policy specified in the QoSPolicyID parameter. When false, any existing policy association is removed regardless of whether you specify a QoS policy in the QoSPolicyID parameter. 
    :type associate_with_qos_policy: bool

    :param qos_policy_id:  The ID for the policy whose QoS settings should be applied to the specified volumes. The volume will not maintain any association with the policy; this is an alternate way to apply QoS settings to the volume. This parameter and the qos parameter cannot be specified at the same time. 
    :type qos_policy_id: int

    """
    volume_id = data_model.property(
        "volumeID", int,
        array=False, optional=False,
        documentation="""VolumeID for the volume to be modified. """,
        dictionaryType=None
    )
    account_id = data_model.property(
        "accountID", int,
        array=False, optional=True,
        documentation="""AccountID to which the volume is reassigned. If unspecified, the previous account name is used. """,
        dictionaryType=None
    )
    access = data_model.property(
        "access", str,
        array=False, optional=True,
        documentation="""Specifies the access allowed for the volume. Possible values are: readOnly: Only read operations are allowed. readWrite: Reads and writes are allowed. locked: No reads or writes are allowed. If not specified, the access value does not change. replicationTarget: Identify a volume as the target volume for a paired set of volumes. If the volume is not paired, the access status is locked. If a value is not specified, the access value does not change. """,
        dictionaryType=None
    )
    qos = data_model.property(
        "qos", QoS,
        array=False, optional=True,
        documentation="""New QoS settings for this volume. If not specified, the QoS settings are not changed. """,
        dictionaryType=None
    )
    total_size = data_model.property(
        "totalSize", int,
        array=False, optional=True,
        documentation="""New size of the volume in bytes. 1000000000 is equal to 1GB. Size is rounded up to the nearest 1MB. This parameter can only be used to increase the size of a volume. """,
        dictionaryType=None
    )
    attributes = data_model.property(
        "attributes", dict,
        array=False, optional=True,
        documentation="""List of name-value pairs in JSON object format. """,
        dictionaryType=None
    )
    associate_with_qos_policy = data_model.property(
        "associateWithQoSPolicy", bool,
        array=False, optional=True,
        documentation="""Associate the volume with the specified QoS policy. Possible values: true: Associate the volume with the QoS policy specified in the QoSPolicyID parameter. false: Do not assosciate the volume with the QoS policy specified in the QoSPolicyID parameter. When false, any existing policy association is removed regardless of whether you specify a QoS policy in the QoSPolicyID parameter. """,
        dictionaryType=None
    )
    qos_policy_id = data_model.property(
        "qosPolicyID", int,
        array=False, optional=True,
        documentation="""The ID for the policy whose QoS settings should be applied to the specified volumes. The volume will not maintain any association with the policy; this is an alternate way to apply QoS settings to the volume. This parameter and the qos parameter cannot be specified at the same time. """,
        dictionaryType=None
    )

    def __init__(self,
            volume_id,
            account_id=None,
            access=None,
            qos=None,
            total_size=None,
            attributes=None,
            associate_with_qos_policy=None,
            qos_policy_id=None):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class CreateGroupSnapshotResult(data_model.DataObject):
    """CreateGroupSnapshotResult  

    :param group_snapshot: [required]  
    :type group_snapshot: GroupSnapshot

    :param group_snapshot_id: [required] Unique ID of the new group snapshot. 
    :type group_snapshot_id: int

    :param members: [required] List of checksum, volumeIDs and snapshotIDs for each member of the group. 
    :type members: GroupSnapshotMembers

    """
    group_snapshot = data_model.property(
        "groupSnapshot", GroupSnapshot,
        array=False, optional=False,
        documentation=""" """,
        dictionaryType=None
    )
    group_snapshot_id = data_model.property(
        "groupSnapshotID", int,
        array=False, optional=False,
        documentation="""Unique ID of the new group snapshot. """,
        dictionaryType=None
    )
    members = data_model.property(
        "members", GroupSnapshotMembers,
        array=True, optional=False,
        documentation="""List of checksum, volumeIDs and snapshotIDs for each member of the group. """,
        dictionaryType=None
    )

    def __init__(self,
            group_snapshot,
            group_snapshot_id,
            members):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class ModifyClusterAdminRequest(data_model.DataObject):
    """ModifyClusterAdminRequest  
    You can use ModifyClusterAdmin to change the settings for a cluster admin or LDAP cluster admin. You cannot change access for the administrator cluster admin account.

    :param cluster_admin_id: [required] ClusterAdminID for the cluster admin or LDAP cluster admin to modify. 
    :type cluster_admin_id: int

    :param password:  Password used to authenticate this cluster admin. 
    :type password: str

    :param access:  Controls which methods this cluster admin can use. For more details, see Access Control in the Element API Reference Guide. 
    :type access: str

    :param attributes:  List of name-value pairs in JSON object format. 
    :type attributes: dict

    """
    cluster_admin_id = data_model.property(
        "clusterAdminID", int,
        array=False, optional=False,
        documentation="""ClusterAdminID for the cluster admin or LDAP cluster admin to modify. """,
        dictionaryType=None
    )
    password = data_model.property(
        "password", str,
        array=False, optional=True,
        documentation="""Password used to authenticate this cluster admin. """,
        dictionaryType=None
    )
    access = data_model.property(
        "access", str,
        array=True, optional=True,
        documentation="""Controls which methods this cluster admin can use. For more details, see Access Control in the Element API Reference Guide. """,
        dictionaryType=None
    )
    attributes = data_model.property(
        "attributes", dict,
        array=False, optional=True,
        documentation="""List of name-value pairs in JSON object format. """,
        dictionaryType=None
    )

    def __init__(self,
            cluster_admin_id,
            password=None,
            access=None,
            attributes=None):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class RemoveSSLCertificateResult(data_model.DataObject):
    """RemoveSSLCertificateResult  

    """

    def __init__(self):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class RemoveClusterPairRequest(data_model.DataObject):
    """RemoveClusterPairRequest  
    You can use the RemoveClusterPair method to close the open connections between two paired clusters.
    Note: Before you remove a cluster pair, you must first remove all volume pairing to the clusters with the "RemoveVolumePair" API method.

    :param cluster_pair_id: [required] Unique identifier used to pair two clusters. 
    :type cluster_pair_id: int

    """
    cluster_pair_id = data_model.property(
        "clusterPairID", int,
        array=False, optional=False,
        documentation="""Unique identifier used to pair two clusters. """,
        dictionaryType=None
    )

    def __init__(self,
            cluster_pair_id):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class CompleteClusterPairingResult(data_model.DataObject):
    """CompleteClusterPairingResult  

    :param cluster_pair_id: [required] Unique identifier for the cluster pair. 
    :type cluster_pair_id: int

    """
    cluster_pair_id = data_model.property(
        "clusterPairID", int,
        array=False, optional=False,
        documentation="""Unique identifier for the cluster pair. """,
        dictionaryType=None
    )

    def __init__(self,
            cluster_pair_id):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)

class TestConnectEnsembleDetails(data_model.DataObject):
    """TestConnectEnsembleDetails  

    :param nodes: [required] A list of each ensemble node in the test and the results of the tests. 
    :type nodes: dict

    """
    nodes = data_model.property(
        "nodes", dict,
        array=False, optional=False,
        documentation="""A list of each ensemble node in the test and the results of the tests. """,
        dictionaryType=None
    )

    def __init__(self,
            nodes):
        kwargs = locals()
        del kwargs["self"]
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
        documentation=""" """,
        dictionaryType=None
    )
    duration = data_model.property(
        "duration", str,
        array=False, optional=False,
        documentation="""The length of time required to run the test. """,
        dictionaryType=None
    )
    result = data_model.property(
        "result", str,
        array=False, optional=False,
        documentation="""The results of the entire test """,
        dictionaryType=None
    )

    def __init__(self,
            details,
            duration,
            result):
        kwargs = locals()
        del kwargs["self"]
        data_model.DataObject.__init__(self, **kwargs)