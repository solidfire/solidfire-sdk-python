from unittest.mock import MagicMock
from solidfire.factory import ElementFactory
from solidfire.__init__ import *
import UnitTests.Resources as Resources

def test_cancel_clone_v9():
    ef = Element("10.117.60.15", "admin", "admin", 9.0)
    ef._dispatcher.post = MagicMock(return_value = Resources.RESP_CancelClone_v9)

    
    clone_id = 42 # clone_id
    result = ef.cancel_clone(clone_id,)

def test_cancel_group_clone_v9():
    ef = Element("10.117.60.15", "admin", "admin", 9.0)
    ef._dispatcher.post = MagicMock(return_value = Resources.RESP_CancelGroupClone_v9)

    
    group_clone_id = 42 # group_clone_id
    result = ef.cancel_group_clone(group_clone_id,)

def test_copy_volume_v9():
    ef = Element("10.117.60.15", "admin", "admin", 9.0)
    ef._dispatcher.post = MagicMock(return_value = Resources.RESP_CopyVolume_v9)

    
    volume_id = 42 # volume_id
    dst_volume_id = 42 # dst_volume_id
    snapshot_id = 42 # snapshot_id
    result = ef.copy_volume(volume_id,dst_volume_id,)
    assert result.async_handle == 9, "Died on +.async_handle"
    assert result.clone_id == 5, "Died on +.clone_id"

def test_create_storage_container_v9():
    ef = Element("10.117.60.15", "admin", "admin", 9.0)
    ef._dispatcher.post = MagicMock(return_value = Resources.RESP_CreateStorageContainer_v9)

    
    name = "" # name
    initiator_secret = "" # initiator_secret
    target_secret = "" # target_secret
    result = ef.create_storage_container(name,)
    assert result.storage_container.status == """active""", "Died on +.storage_container.status"
    assert result.storage_container.storage_container_id == UUID("2b0653fb-3d64-4ae0-9ef8-356e685b0b2e"), "Died on .storage_container.storage_container_id"
    assert result.storage_container.name == """ExampleName""", "Died on +.storage_container.name"
    assert result.storage_container.initiator_secret == """Z5k)Cf~jiIxp3R4[""", "Died on +.storage_container.initiator_secret"
    assert result.storage_container.target_secret == """N07S4}aEh5oU]L0l""", "Died on +.storage_container.target_secret"
    assert result.storage_container.protocol_endpoint_type == """SCSI""", "Died on +.storage_container.protocol_endpoint_type"
    assert result.storage_container.account_id == 111, "Died on +.storage_container.account_id"

def test_create_volume_access_group_v9():
    ef = Element("10.117.60.15", "admin", "admin", 9.0)
    ef._dispatcher.post = MagicMock(return_value = Resources.RESP_CreateVolumeAccessGroup_v9)

    
    name = "" # name
    initiators = "" # initiators
    volumes = 42 # volumes
    virtual_network_id = 42 # virtual_network_id
    virtual_network_tags = 42 # virtual_network_tags
    attributes = dict() # attributes
    result = ef.create_volume_access_group(name,)
    assert result.volume_access_group.name == """myaccessgroup""", "Died on +.volume_access_group.name"
    assert result.volume_access_group.initiator_ids[0] == 95, "Died on +.volume_access_group.initiator_ids[0]"
    assert result.volume_access_group.volumes[0] == 327, "Died on +.volume_access_group.volumes[0]"
    assert result.volume_access_group.initiators[0] == """iqn.1993-08.org.debian: 01: a31b1d799d5c""", "Died on +.volume_access_group.initiators[0]"
    assert type(result.volume_access_group.attributes) is dict, "Died on .volume_access_group.attributes"
    assert result.volume_access_group.volume_access_group_id == 96, "Died on +.volume_access_group.volume_access_group_id"
    assert result.volume_access_group_id == 96, "Died on +.volume_access_group_id"

def test_delete_storage_containers_v9():
    ef = Element("10.117.60.15", "admin", "admin", 9.0)
    ef._dispatcher.post = MagicMock(return_value = Resources.RESP_DeleteStorageContainers_v9)

    
    storage_container_ids = UUID("2b0653fb-3d64-4ae0-9ef8-356e685b0b2e") # storage_container_ids
    result = ef.delete_storage_containers(storage_container_ids,)

def test_delete_volumes_v9():
    ef = Element("10.117.60.15", "admin", "admin", 9.0)
    ef._dispatcher.post = MagicMock(return_value = Resources.RESP_DeleteVolumes_v9)

    
    account_ids = 42 # account_ids
    volume_access_group_ids = 42 # volume_access_group_ids
    volume_ids = 42 # volume_ids
    result = ef.delete_volumes()
    assert result.volumes[0].status == """active""", "Died on +.volumes[0].status"
    assert result.volumes[0].enable512e == False, "Died on +.volumes[0].enable512e"
    assert result.volumes[0].qos.burst_iops == 15000, "Died on +.volumes[0].qos.burst_iops"
    assert result.volumes[0].qos.min_iops == 100, "Died on +.volumes[0].qos.min_iops"
    assert result.volumes[0].qos.max_iops == 15000, "Died on +.volumes[0].qos.max_iops"
    assert result.volumes[0].qos.burst_time == 60, "Died on +.volumes[0].qos.burst_time"
    assert result.volumes[0].name == """vclient-030-v00001""", "Died on +.volumes[0].name"
    assert result.volumes[0].total_size == 10000003072, "Died on +.volumes[0].total_size"
    assert result.volumes[0].block_size == 4096, "Died on +.volumes[0].block_size"
    assert result.volumes[0].account_id == 1, "Died on +.volumes[0].account_id"
    assert result.volumes[0].scsi_euidevice_id == """707a737200000001f47acc0100000000""", "Died on +.volumes[0].scsi_euidevice_id"
    assert result.volumes[0].volume_id == 1, "Died on +.volumes[0].volume_id"
    assert result.volumes[0].access == """readWrite""", "Died on +.volumes[0].access"
    assert type(result.volumes[0].attributes) is dict, "Died on .volumes[0].attributes"
    assert result.volumes[0].slice_count == 1, "Died on +.volumes[0].slice_count"
    assert result.volumes[0].iqn == """iqn.2010-01.com.solidfire:pzsr.vclient-030-v00001.1""", "Died on +.volumes[0].iqn"
    assert result.volumes[0].scsi_naadevice_id == """6f47acc100000000707a737200000001""", "Died on +.volumes[0].scsi_naadevice_id"
    assert result.volumes[0].create_time == """2015-03-06T18:50:56Z""", "Died on +.volumes[0].create_time"
    assert result.volumes[0].virtual_volume_id == 5, "Died on +.volumes[0].virtual_volume_id"

def test_enable_feature_v9():
    ef = Element("10.117.60.15", "admin", "admin", 9.0)
    ef._dispatcher.post = MagicMock(return_value = Resources.RESP_EnableFeature_v9)

    
    feature = "" # feature
    result = ef.enable_feature(feature,)

def test_get_cluster_hardware_info_v9():
    ef = Element("10.117.60.15", "admin", "admin", 9.0)
    ef._dispatcher.post = MagicMock(return_value = Resources.RESP_GetClusterHardwareInfo_v9)

    
    type = "" # type
    result = ef.get_cluster_hardware_info()

def test_get_feature_status_v9():
    ef = Element("10.117.60.15", "admin", "admin", 9.0)
    ef._dispatcher.post = MagicMock(return_value = Resources.RESP_GetFeatureStatus_v9)

    
    feature = "" # feature
    result = ef.get_feature_status()
    assert result.features[0].enabled == True, "Died on +.features[0].enabled"
    assert result.features[0].feature == """Vvols""", "Died on +.features[0].feature"

def test_get_hardware_config_v9():
    ef = Element("10.117.60.15", "admin", "admin", 9.0)
    ef._dispatcher.post = MagicMock(return_value = Resources.RESP_GetHardwareConfig_v9)

    
    result = ef.get_hardware_config()
    assert result.hardware_config.scsi_bus_internal_driver == """ahci""", "Died on +.hardware_config.scsi_bus_internal_driver"
    assert result.hardware_config.network_driver[0] == """bnx2x""", "Died on +.hardware_config.network_driver[0]"
    assert result.hardware_config.bios_revision == """1.0""", "Died on +.hardware_config.bios_revision"
    assert result.hardware_config.slot_offset == 0, "Died on +.hardware_config.slot_offset"
    assert result.hardware_config.num_cpu == 2, "Died on +.hardware_config.num_cpu"
    assert result.hardware_config.slice_drives[0] == """/dev/sdimm0p4""", "Died on +.hardware_config.slice_drives[0]"
    assert result.hardware_config.num_drives == 10, "Died on +.hardware_config.num_drives"
    assert result.hardware_config.kernel_crash_dump.kernel_crash_dump_default_state == """enabled""", "Died on +.hardware_config.kernel_crash_dump.kernel_crash_dump_default_state"
    assert result.hardware_config.kernel_crash_dump.kernel_crash_dump_directory == """/var/crash""", "Died on +.hardware_config.kernel_crash_dump.kernel_crash_dump_directory"
    assert result.hardware_config.kernel_crash_dump.kernel_crash_dump_kernel_options == """ro console=tty10 console=ttyS1,115200n8 quiet splash vt.handoff=7 irqpoll maxcpus=1 reset_devices nousb modprobe.blacklist=qla2xxx,bnx2x,mpt2sas""", "Died on +.hardware_config.kernel_crash_dump.kernel_crash_dump_kernel_options"
    assert result.hardware_config.kernel_crash_dump.kernel_crash_dump_makedumpfile_level == 31, "Died on +.hardware_config.kernel_crash_dump.kernel_crash_dump_makedumpfile_level"
    assert result.hardware_config.kernel_crash_dump.kernel_crash_dump_min_free_gb == 5, "Died on +.hardware_config.kernel_crash_dump.kernel_crash_dump_min_free_gb"
    assert result.hardware_config.block_drive_size_bytes == 300069052416, "Died on +.hardware_config.block_drive_size_bytes"
    assert result.hardware_config.cpu_model == """Intel(R) Xeon(R) CPU E5-2640 0 @ 2.50GHz""", "Died on +.hardware_config.cpu_model"
    assert result.hardware_config.bmc_firmware_revision == """1.6""", "Died on +.hardware_config.bmc_firmware_revision"
    assert result.hardware_config.cpu_cores_enabled == 6, "Died on +.hardware_config.cpu_cores_enabled"
    assert result.hardware_config.chassis_type == """R620""", "Died on +.hardware_config.chassis_type"
    assert result.hardware_config.bmc_ipmi_version == """2.0""", "Died on +.hardware_config.bmc_ipmi_version"
    assert result.hardware_config.node_type == """SF3010""", "Died on +.hardware_config.node_type"
    assert result.hardware_config.memory_gb == 72, "Died on +.hardware_config.memory_gb"
    assert result.hardware_config.idrac_version == """1.06.06""", "Died on +.hardware_config.idrac_version"
    assert result.hardware_config.block_drives[9] == """/dev/slot9""", "Died on +.hardware_config.block_drives[9]"
    assert result.hardware_config.block_drives[8] == """/dev/slot8""", "Died on +.hardware_config.block_drives[8]"
    assert result.hardware_config.block_drives[7] == """/dev/slot7""", "Died on +.hardware_config.block_drives[7]"
    assert result.hardware_config.block_drives[6] == """/dev/slot6""", "Died on +.hardware_config.block_drives[6]"
    assert result.hardware_config.block_drives[5] == """/dev/slot5""", "Died on +.hardware_config.block_drives[5]"
    assert result.hardware_config.block_drives[4] == """/dev/slot4""", "Died on +.hardware_config.block_drives[4]"
    assert result.hardware_config.block_drives[3] == """/dev/slot3""", "Died on +.hardware_config.block_drives[3]"
    assert result.hardware_config.block_drives[2] == """/dev/slot2""", "Died on +.hardware_config.block_drives[2]"
    assert result.hardware_config.block_drives[1] == """/dev/slot1""", "Died on +.hardware_config.block_drives[1]"
    assert result.hardware_config.block_drives[0] == """/dev/slot0""", "Died on +.hardware_config.block_drives[0]"
    assert result.hardware_config.bios_vendor == """SolidFire""", "Died on +.hardware_config.bios_vendor"
    assert result.hardware_config.scsi_bus_external_driver == """mpt2sas""", "Died on +.hardware_config.scsi_bus_external_driver"
    assert result.hardware_config.num_drives_internal == 1, "Died on +.hardware_config.num_drives_internal"
    assert result.hardware_config.memory_mhz == 1333, "Died on +.hardware_config.memory_mhz"
    assert result.hardware_config.bios_version == """1.1.2""", "Died on +.hardware_config.bios_version"
    assert result.hardware_config.slice_drive_size_bytes == 299988156416, "Died on +.hardware_config.slice_drive_size_bytes"
    assert result.hardware_config.cpu_cores == 6, "Died on +.hardware_config.cpu_cores"
    assert result.hardware_config.root_drive == """/dev/sdimm0""", "Died on +.hardware_config.root_drive"
    assert result.hardware_config.drive_size_bytes_internal == 400088457216, "Died on +.hardware_config.drive_size_bytes_internal"
    assert result.hardware_config.lifecycle_version == """1.0.0.5747""", "Died on +.hardware_config.lifecycle_version"
    assert result.hardware_config.solidfire_defaults.max_drive_write_throughput_mbper_sec == 125, "Died on +.hardware_config.solidfire_defaults.max_drive_write_throughput_mbper_sec"
    assert result.hardware_config.solidfire_defaults.slice_file_log_file_capacity == 5000000000, "Died on +.hardware_config.solidfire_defaults.slice_file_log_file_capacity"
    assert result.hardware_config.solidfire_defaults.post_callback_thread_count == 8, "Died on +.hardware_config.solidfire_defaults.post_callback_thread_count"
    assert result.hardware_config.solidfire_defaults.cpu_dma_latency == -1, "Died on +.hardware_config.solidfire_defaults.cpu_dma_latency"
    assert result.hardware_config.solidfire_defaults.buffer_cache_gb == 12, "Died on +.hardware_config.solidfire_defaults.buffer_cache_gb"
    assert result.hardware_config.solidfire_defaults.max_incoming_slice_syncs == 10, "Died on +.hardware_config.solidfire_defaults.max_incoming_slice_syncs"
    assert result.hardware_config.solidfire_defaults.configured_iops == 50000, "Died on +.hardware_config.solidfire_defaults.configured_iops"
    assert result.hardware_config.solidfire_defaults.s_cache_file_capacity == 100000000, "Died on +.hardware_config.solidfire_defaults.s_cache_file_capacity"
    assert result.hardware_config.solidfire_defaults.drive_write_throughput_mbper_sleep == 10, "Died on +.hardware_config.solidfire_defaults.drive_write_throughput_mbper_sleep"
    assert result.hardware_config.cpu_threads == 12, "Died on +.hardware_config.cpu_threads"

def test_get_hardware_info_v9():
    ef = Element("10.117.60.15", "admin", "admin", 9.0)
    ef._dispatcher.post = MagicMock(return_value = Resources.RESP_GetHardwareInfo_v9)

    
    result = ef.get_hardware_info()
    assert type(result.hardware_info.bus) is dict, "Died on .hardware_info.bus"
    assert result.hardware_info.drive_hardware[0].security_locked == False, "Died on +.hardware_info.drive_hardware[0].security_locked"
    assert result.hardware_info.drive_hardware[0].path == """/dev/sdh""", "Died on +.hardware_info.drive_hardware[0].path"
    assert result.hardware_info.drive_hardware[0].serial == """AAAA33710886300AAA""", "Died on +.hardware_info.drive_hardware[0].serial"
    assert result.hardware_info.drive_hardware[0].size == 300069052416, "Died on +.hardware_info.drive_hardware[0].size"
    assert result.hardware_info.drive_hardware[0].slot == 1, "Died on +.hardware_info.drive_hardware[0].slot"
    assert result.hardware_info.drive_hardware[0].uuid == UUID("aea178b9-c336-6bab-a61d-87b615e8120c"), "Died on .hardware_info.drive_hardware[0].uuid"
    assert result.hardware_info.drive_hardware[0].dev_path == """/dev/disk/by-path/pci-0000:41:00.0-sas-0x500056b37789abf0-lun-0""", "Died on +.hardware_info.drive_hardware[0].dev_path"
    assert result.hardware_info.drive_hardware[0].version == """D2010370""", "Died on +.hardware_info.drive_hardware[0].version"
    assert result.hardware_info.drive_hardware[0].life_remaining_percent == 92, "Died on +.hardware_info.drive_hardware[0].life_remaining_percent"
    assert result.hardware_info.drive_hardware[0].drive_type == """Block""", "Died on +.hardware_info.drive_hardware[0].drive_type"
    assert result.hardware_info.drive_hardware[0].security_supported == True, "Died on +.hardware_info.drive_hardware[0].security_supported"
    assert result.hardware_info.drive_hardware[0].product == """INTEL SSDAA2AA300A4""", "Died on +.hardware_info.drive_hardware[0].product"
    assert result.hardware_info.drive_hardware[0].vendor == """Intel""", "Died on +.hardware_info.drive_hardware[0].vendor"
    assert result.hardware_info.drive_hardware[0].lifetime_read_bytes == 175436696911872, "Died on +.hardware_info.drive_hardware[0].lifetime_read_bytes"
    assert result.hardware_info.drive_hardware[0].security_enabled == False, "Died on +.hardware_info.drive_hardware[0].security_enabled"
    assert result.hardware_info.drive_hardware[0].security_frozen == False, "Died on +.hardware_info.drive_hardware[0].security_frozen"
    assert result.hardware_info.drive_hardware[0].connected == True, "Died on +.hardware_info.drive_hardware[0].connected"
    assert result.hardware_info.drive_hardware[0].canonical_name == """sdh""", "Died on +.hardware_info.drive_hardware[0].canonical_name"
    assert result.hardware_info.drive_hardware[0].reallocated_sectors == 0, "Died on +.hardware_info.drive_hardware[0].reallocated_sectors"
    assert result.hardware_info.drive_hardware[0].scsi_state == """Running""", "Died on +.hardware_info.drive_hardware[0].scsi_state"
    assert result.hardware_info.drive_hardware[0].scsi_compat_id == """scsi-SATA_INTEL_SSDSC2BB3BTWL12345686300AAA""", "Died on +.hardware_info.drive_hardware[0].scsi_compat_id"
    assert result.hardware_info.drive_hardware[0].reserve_capacity_percent == 100, "Died on +.hardware_info.drive_hardware[0].reserve_capacity_percent"
    assert result.hardware_info.drive_hardware[0].name == """scsi-SATA_INTEL_SSDSC2BB3BTWL12345686300AAA""", "Died on +.hardware_info.drive_hardware[0].name"
    assert result.hardware_info.drive_hardware[0].lifetime_write_bytes == 81941097349120, "Died on +.hardware_info.drive_hardware[0].lifetime_write_bytes"
    assert result.hardware_info.drive_hardware[0].dev == 2160, "Died on +.hardware_info.drive_hardware[0].dev"
    assert result.hardware_info.drive_hardware[0].security_at_maximum == False, "Died on +.hardware_info.drive_hardware[0].security_at_maximum"
    assert result.hardware_info.drive_hardware[0].path_link == """/dev/disk/by-path/pci-0000:41:00.0-sas-0x500056b37789abf0-lun-0""", "Died on +.hardware_info.drive_hardware[0].path_link"
    assert result.hardware_info.drive_hardware[0].power_on_hours == 17246, "Died on +.hardware_info.drive_hardware[0].power_on_hours"
    assert result.hardware_info.drive_hardware[0].smart_ssd_write_capable == False, "Died on +.hardware_info.drive_hardware[0].smart_ssd_write_capable"

def test_get_limits_v9():
    ef = Element("10.117.60.15", "admin", "admin", 9.0)
    ef._dispatcher.post = MagicMock(return_value = Resources.RESP_GetLimits_v9)

    
    result = ef.get_limits()
    assert result.initiator_count_max == 0, "Died on +.initiator_count_max"
    assert result.iscsi_sessions_from_fibre_channel_nodes_max == 4096, "Died on +.iscsi_sessions_from_fibre_channel_nodes_max"
    assert result.cluster_pairs_count_max == 4, "Died on +.cluster_pairs_count_max"
    assert result.volume_max_iopsmin == 100, "Died on +.volume_max_iopsmin"
    assert result.volume_size_max == 8000000491520, "Died on +.volume_size_max"
    assert result.volume_burst_iopsmax == 100000, "Died on +.volume_burst_iopsmax"
    assert result.clone_jobs_per_volume_max == 2, "Died on +.clone_jobs_per_volume_max"
    assert result.volumes_per_volume_access_group_count_max == 2000, "Died on +.volumes_per_volume_access_group_count_max"
    assert result.initiator_name_length_max == 224, "Died on +.initiator_name_length_max"
    assert result.volume_name_length_min == 1, "Died on +.volume_name_length_min"
    assert result.volume_min_iopsmin == 50, "Died on +.volume_min_iopsmin"
    assert result.snapshots_per_volume_max == 32, "Died on +.snapshots_per_volume_max"
    assert result.volume_access_groups_per_volume_count_max == 4, "Died on +.volume_access_groups_per_volume_count_max"
    assert result.volumes_per_group_snapshot_max == 32, "Died on +.volumes_per_group_snapshot_max"
    assert result.volume_max_iopsmax == 100000, "Died on +.volume_max_iopsmax"
    assert result.volume_access_groups_per_initiator_count_max == 1, "Died on +.volume_access_groups_per_initiator_count_max"
    assert result.bulk_volume_jobs_per_node_max == 8, "Died on +.bulk_volume_jobs_per_node_max"
    assert result.initiators_per_volume_access_group_count_max == 64, "Died on +.initiators_per_volume_access_group_count_max"
    assert result.volume_access_group_name_length_max == 64, "Died on +.volume_access_group_name_length_max"
    assert result.account_name_length_min == 1, "Died on +.account_name_length_min"
    assert result.volume_name_length_max == 64, "Died on +.volume_name_length_max"
    assert result.secret_length_max == 16, "Died on +.secret_length_max"
    assert result.account_count_max == 5000, "Died on +.account_count_max"
    assert result.volume_access_group_count_max == 1000, "Died on +.volume_access_group_count_max"
    assert result.secret_length_min == 12, "Died on +.secret_length_min"
    assert result.volume_access_group_lun_max == 16383, "Died on +.volume_access_group_lun_max"
    assert result.volume_access_group_name_length_min == 1, "Died on +.volume_access_group_name_length_min"
    assert result.bulk_volume_jobs_per_volume_max == 2, "Died on +.bulk_volume_jobs_per_volume_max"
    assert result.snapshot_name_length_max == 64, "Died on +.snapshot_name_length_max"
    assert result.volumes_per_account_count_max == 2000, "Died on +.volumes_per_account_count_max"
    assert result.volume_count_max == 4000, "Died on +.volume_count_max"
    assert result.volume_size_min == 1000000000, "Died on +.volume_size_min"
    assert result.initiator_alias_length_max == 224, "Died on +.initiator_alias_length_max"
    assert result.volume_burst_iopsmin == 100, "Died on +.volume_burst_iopsmin"
    assert result.volume_min_iopsmax == 15000, "Died on +.volume_min_iopsmax"
    assert result.account_name_length_max == 64, "Died on +.account_name_length_max"

def test_get_network_config_v9():
    ef = Element("10.117.60.15", "admin", "admin", 9.0)
    ef._dispatcher.post = MagicMock(return_value = Resources.RESP_GetNetworkConfig_v9)

    
    result = ef.get_network_config()
    assert result.network.bond1_g.mac_address == """d4:ae:52:8a:6c:7b""", "Died on +.network.bond1_g.mac_address"
    assert result.network.bond1_g.symmetric_route_rules[3] == """ip route add default via 10.30.95.254""", "Died on +.network.bond1_g.symmetric_route_rules[3]"
    assert result.network.bond1_g.symmetric_route_rules[2] == """ip rule add from 10.30.65.161 table Bond1G""", "Died on +.network.bond1_g.symmetric_route_rules[2]"
    assert result.network.bond1_g.symmetric_route_rules[1] == """ip route add default via 10.30.95.254 dev Bond1G src 10.30.65.161 table Bond1G""", "Died on +.network.bond1_g.symmetric_route_rules[1]"
    assert result.network.bond1_g.symmetric_route_rules[0] == """ip route add 10.30.64.0/19 dev Bond1G src 10.30.65.161 table Bond1G""", "Died on +.network.bond1_g.symmetric_route_rules[0]"
    assert result.network.bond1_g.family == """inet""", "Died on +.network.bond1_g.family"
    assert result.network.bond1_g._default == True, "Died on +.network.bond1_g._default"
    assert result.network.bond1_g.gateway == """10.30.95.254""", "Died on +.network.bond1_g.gateway"
    assert result.network.bond1_g.physical.mac_address_permanent == """00:00:00:00:00:00""", "Died on +.network.bond1_g.physical.mac_address_permanent"
    assert result.network.bond1_g.physical.mac_address == """d4:ae:52:8a:6c:7b""", "Died on +.network.bond1_g.physical.mac_address"
    assert result.network.bond1_g.physical.up_and_running == True, "Died on +.network.bond1_g.physical.up_and_running"
    assert result.network.bond1_g.physical.network == """10.30.64.0""", "Died on +.network.bond1_g.physical.network"
    assert result.network.bond1_g.physical.mtu == """1500""", "Died on +.network.bond1_g.physical.mtu"
    assert result.network.bond1_g.physical.netmask == """255.255.224.0""", "Died on +.network.bond1_g.physical.netmask"
    assert result.network.bond1_g.physical.address == """10.30.65.161""", "Died on +.network.bond1_g.physical.address"
    assert result.network.bond1_g.network == """10.30.64.0""", "Died on +.network.bond1_g.network"
    assert result.network.bond1_g.method == """static""", "Died on +.network.bond1_g.method"
    assert result.network.bond1_g.status == """UpAndRunning""", "Died on +.network.bond1_g.status"
    assert result.network.bond1_g.bond_fail_over_mac == """None""", "Died on +.network.bond1_g.bond_fail_over_mac"
    assert result.network.bond1_g.auto == True, "Died on +.network.bond1_g.auto"
    assert result.network.bond1_g.bond_slaves == """eth2 eth3""", "Died on +.network.bond1_g.bond_slaves"
    assert result.network.bond1_g.netmask == """255.255.224.0""", "Died on +.network.bond1_g.netmask"
    assert result.network.bond1_g.bond_mode == """ActivePassive""", "Died on +.network.bond1_g.bond_mode"
    assert result.network.bond1_g.address == """10.30.65.161""", "Died on +.network.bond1_g.address"
    assert result.network.bond1_g.mac_address_permanent == """00:00:00:00:00:00""", "Died on +.network.bond1_g.mac_address_permanent"
    assert result.network.bond1_g.up_and_running == True, "Died on +.network.bond1_g.up_and_running"
    assert result.network.bond1_g.mtu == """1500""", "Died on +.network.bond1_g.mtu"
    assert result.network.bond1_g.bond_primary_reselect == """Failure""", "Died on +.network.bond1_g.bond_primary_reselect"
    assert result.network.lo.mac_address_permanent == """00:00:00:00:00:00""", "Died on +.network.lo.mac_address_permanent"
    assert result.network.lo.mac_address == """00:00:00:00:00:00""", "Died on +.network.lo.mac_address"
    assert result.network.lo.up_and_running == True, "Died on +.network.lo.up_and_running"
    assert result.network.lo.family == """inet""", "Died on +.network.lo.family"
    assert result.network.lo.auto == True, "Died on +.network.lo.auto"
    assert result.network.lo.status == """UpAndRunning""", "Died on +.network.lo.status"
    assert result.network.lo.method == """loopback""", "Died on +.network.lo.method"
    assert result.network.lo.physical.mac_address_permanent == """00:00:00:00:00:00""", "Died on +.network.lo.physical.mac_address_permanent"
    assert result.network.lo.physical.mac_address == """00:00:00:00:00:00""", "Died on +.network.lo.physical.mac_address"
    assert result.network.lo.physical.up_and_running == True, "Died on +.network.lo.physical.up_and_running"
    assert result.network.lo.physical.network == """N/A""", "Died on +.network.lo.physical.network"
    assert result.network.lo.physical.netmask == """N/A""", "Died on +.network.lo.physical.netmask"
    assert result.network.lo.physical.address == """0.0.0.0""", "Died on +.network.lo.physical.address"
    assert result.network.bond10_g.mac_address == """d4:ae:52:8a:6c:77""", "Died on +.network.bond10_g.mac_address"
    assert result.network.bond10_g.symmetric_route_rules[2] == """ip rule add from 192.168.65.161 table Bond10G""", "Died on +.network.bond10_g.symmetric_route_rules[2]"
    assert result.network.bond10_g.symmetric_route_rules[1] == """ip route add default via 192.168.95.254 dev Bond10G src 192.168.65.161 table Bond10G""", "Died on +.network.bond10_g.symmetric_route_rules[1]"
    assert result.network.bond10_g.symmetric_route_rules[0] == """ip route add 192.168.64.0/19 dev Bond10G src 192.168.65.161 table Bond10G""", "Died on +.network.bond10_g.symmetric_route_rules[0]"
    assert result.network.bond10_g.family == """inet""", "Died on +.network.bond10_g.family"
    assert result.network.bond10_g._default == False, "Died on +.network.bond10_g._default"
    assert result.network.bond10_g.gateway == """192.168.95.254""", "Died on +.network.bond10_g.gateway"
    assert result.network.bond10_g.physical.mac_address_permanent == """00:00:00:00:00:00""", "Died on +.network.bond10_g.physical.mac_address_permanent"
    assert result.network.bond10_g.physical.mac_address == """d4:ae:52:8a:6c:77""", "Died on +.network.bond10_g.physical.mac_address"
    assert result.network.bond10_g.physical.up_and_running == True, "Died on +.network.bond10_g.physical.up_and_running"
    assert result.network.bond10_g.physical.network == """192.168.64.0""", "Died on +.network.bond10_g.physical.network"
    assert result.network.bond10_g.physical.mtu == """9000""", "Died on +.network.bond10_g.physical.mtu"
    assert result.network.bond10_g.physical.netmask == """255.255.224.0""", "Died on +.network.bond10_g.physical.netmask"
    assert result.network.bond10_g.physical.address == """192.168.65.161""", "Died on +.network.bond10_g.physical.address"
    assert result.network.bond10_g.network == """192.168.64.0""", "Died on +.network.bond10_g.network"
    assert result.network.bond10_g.method == """static""", "Died on +.network.bond10_g.method"
    assert result.network.bond10_g.status == """UpAndRunning""", "Died on +.network.bond10_g.status"
    assert result.network.bond10_g.bond_fail_over_mac == """None""", "Died on +.network.bond10_g.bond_fail_over_mac"
    assert result.network.bond10_g.auto == True, "Died on +.network.bond10_g.auto"
    assert result.network.bond10_g.bond_slaves == """eth0 eth1""", "Died on +.network.bond10_g.bond_slaves"
    assert result.network.bond10_g.netmask == """255.255.224.0""", "Died on +.network.bond10_g.netmask"
    assert result.network.bond10_g.bond_mode == """ActivePassive""", "Died on +.network.bond10_g.bond_mode"
    assert result.network.bond10_g.address == """192.168.65.161""", "Died on +.network.bond10_g.address"
    assert result.network.bond10_g.mac_address_permanent == """00:00:00:00:00:00""", "Died on +.network.bond10_g.mac_address_permanent"
    assert result.network.bond10_g.up_and_running == True, "Died on +.network.bond10_g.up_and_running"
    assert result.network.bond10_g.mtu == """9000""", "Died on +.network.bond10_g.mtu"
    assert result.network.bond10_g.bond_primary_reselect == """Failure""", "Died on +.network.bond10_g.bond_primary_reselect"
    assert result.network.eth3.mac_address_permanent == """d4:ae:52:8a:6c:7d""", "Died on +.network.eth3.mac_address_permanent"
    assert result.network.eth3.mac_address == """d4:ae:52:8a:6c:7b""", "Died on +.network.eth3.mac_address"
    assert result.network.eth3.up_and_running == True, "Died on +.network.eth3.up_and_running"
    assert result.network.eth3.family == """inet""", "Died on +.network.eth3.family"
    assert result.network.eth3.auto == True, "Died on +.network.eth3.auto"
    assert result.network.eth3.bond_master == """Bond1G""", "Died on +.network.eth3.bond_master"
    assert result.network.eth3.status == """UpAndRunning""", "Died on +.network.eth3.status"
    assert result.network.eth3.method == """bond""", "Died on +.network.eth3.method"
    assert result.network.eth3.physical.mac_address_permanent == """d4:ae:52:8a:6c:7d""", "Died on +.network.eth3.physical.mac_address_permanent"
    assert result.network.eth3.physical.mac_address == """d4:ae:52:8a:6c:7b""", "Died on +.network.eth3.physical.mac_address"
    assert result.network.eth3.physical.up_and_running == True, "Died on +.network.eth3.physical.up_and_running"
    assert result.network.eth3.physical.network == """N/A""", "Died on +.network.eth3.physical.network"
    assert result.network.eth3.physical.netmask == """N/A""", "Died on +.network.eth3.physical.netmask"
    assert result.network.eth3.physical.address == """0.0.0.0""", "Died on +.network.eth3.physical.address"
    assert result.network.eth2.mac_address_permanent == """d4:ae:52:8a:6c:7b""", "Died on +.network.eth2.mac_address_permanent"
    assert result.network.eth2.mac_address == """d4:ae:52:8a:6c:7b""", "Died on +.network.eth2.mac_address"
    assert result.network.eth2.up_and_running == True, "Died on +.network.eth2.up_and_running"
    assert result.network.eth2.family == """inet""", "Died on +.network.eth2.family"
    assert result.network.eth2.auto == True, "Died on +.network.eth2.auto"
    assert result.network.eth2.bond_master == """Bond1G""", "Died on +.network.eth2.bond_master"
    assert result.network.eth2.status == """UpAndRunning""", "Died on +.network.eth2.status"
    assert result.network.eth2.method == """bond""", "Died on +.network.eth2.method"
    assert result.network.eth2.physical.mac_address_permanent == """d4:ae:52:8a:6c:7b""", "Died on +.network.eth2.physical.mac_address_permanent"
    assert result.network.eth2.physical.mac_address == """d4:ae:52:8a:6c:7b""", "Died on +.network.eth2.physical.mac_address"
    assert result.network.eth2.physical.up_and_running == True, "Died on +.network.eth2.physical.up_and_running"
    assert result.network.eth2.physical.network == """N/A""", "Died on +.network.eth2.physical.network"
    assert result.network.eth2.physical.netmask == """N/A""", "Died on +.network.eth2.physical.netmask"
    assert result.network.eth2.physical.address == """0.0.0.0""", "Died on +.network.eth2.physical.address"
    assert result.network.eth1.mac_address_permanent == """d4:ae:52:8a:6c:79""", "Died on +.network.eth1.mac_address_permanent"
    assert result.network.eth1.mac_address == """d4:ae:52:8a:6c:77""", "Died on +.network.eth1.mac_address"
    assert result.network.eth1.up_and_running == True, "Died on +.network.eth1.up_and_running"
    assert result.network.eth1.family == """inet""", "Died on +.network.eth1.family"
    assert result.network.eth1.auto == True, "Died on +.network.eth1.auto"
    assert result.network.eth1.bond_master == """Bond10G""", "Died on +.network.eth1.bond_master"
    assert result.network.eth1.status == """UpAndRunning""", "Died on +.network.eth1.status"
    assert result.network.eth1.method == """bond""", "Died on +.network.eth1.method"
    assert result.network.eth1.physical.mac_address_permanent == """d4:ae:52:8a:6c:79""", "Died on +.network.eth1.physical.mac_address_permanent"
    assert result.network.eth1.physical.mac_address == """d4:ae:52:8a:6c:77""", "Died on +.network.eth1.physical.mac_address"
    assert result.network.eth1.physical.up_and_running == True, "Died on +.network.eth1.physical.up_and_running"
    assert result.network.eth1.physical.network == """N/A""", "Died on +.network.eth1.physical.network"
    assert result.network.eth1.physical.netmask == """N/A""", "Died on +.network.eth1.physical.netmask"
    assert result.network.eth1.physical.address == """0.0.0.0""", "Died on +.network.eth1.physical.address"
    assert result.network.eth0.mac_address_permanent == """d4:ae:52:8a:6c:77""", "Died on +.network.eth0.mac_address_permanent"
    assert result.network.eth0.mac_address == """d4:ae:52:8a:6c:77""", "Died on +.network.eth0.mac_address"
    assert result.network.eth0.up_and_running == True, "Died on +.network.eth0.up_and_running"
    assert result.network.eth0.family == """inet""", "Died on +.network.eth0.family"
    assert result.network.eth0.auto == True, "Died on +.network.eth0.auto"
    assert result.network.eth0.bond_master == """Bond10G""", "Died on +.network.eth0.bond_master"
    assert result.network.eth0.status == """UpAndRunning""", "Died on +.network.eth0.status"
    assert result.network.eth0.method == """bond""", "Died on +.network.eth0.method"
    assert result.network.eth0.physical.mac_address_permanent == """d4:ae:52:8a:6c:77""", "Died on +.network.eth0.physical.mac_address_permanent"
    assert result.network.eth0.physical.mac_address == """d4:ae:52:8a:6c:77""", "Died on +.network.eth0.physical.mac_address"
    assert result.network.eth0.physical.up_and_running == True, "Died on +.network.eth0.physical.up_and_running"
    assert result.network.eth0.physical.network == """N/A""", "Died on +.network.eth0.physical.network"
    assert result.network.eth0.physical.netmask == """N/A""", "Died on +.network.eth0.physical.netmask"
    assert result.network.eth0.physical.address == """0.0.0.0""", "Died on +.network.eth0.physical.address"

def test_get_node_hardware_info_v9():
    ef = Element("10.117.60.15", "admin", "admin", 9.0)
    ef._dispatcher.post = MagicMock(return_value = Resources.RESP_GetNodeHardwareInfo_v9)

    
    node_id = 42 # node_id
    result = ef.get_node_hardware_info(node_id,)
    assert type(result.node_hardware_info) is dict, "Died on .node_hardware_info"

def test_get_nvram_info_v9():
    ef = Element("10.117.60.15", "admin", "admin", 9.0)
    ef._dispatcher.post = MagicMock(return_value = Resources.RESP_GetNvramInfo_v9)

    
    result = ef.get_nvram_info()
    assert type(result.nvram_info) is dict, "Died on .nvram_info"

def test_get_storage_container_efficiency_v9():
    ef = Element("10.117.60.15", "admin", "admin", 9.0)
    ef._dispatcher.post = MagicMock(return_value = Resources.RESP_GetStorageContainerEfficiency_v9)

    
    storage_container_id = UUID("2b0653fb-3d64-4ae0-9ef8-356e685b0b2e") # storage_container_id
    result = ef.get_storage_container_efficiency(storage_container_id,)
    assert result.timestamp == """2016-10-14T22:41:24Z""", "Died on +.timestamp"
    assert result.thin_provisioning == 1, "Died on +.thin_provisioning"
    assert result.compression == 1, "Died on +.compression"
    assert result.deduplication == 1, "Died on +.deduplication"

def test_get_virtual_volume_count_v9():
    ef = Element("10.117.60.15", "admin", "admin", 9.0)
    ef._dispatcher.post = MagicMock(return_value = Resources.RESP_GetVirtualVolumeCount_v9)

    
    result = ef.get_virtual_volume_count()
    assert result.count == 0, "Died on +.count"

def test_list_async_results_v9():
    ef = Element("10.117.60.15", "admin", "admin", 9.0)
    ef._dispatcher.post = MagicMock(return_value = Resources.RESP_ListAsyncResults_v9)

    
    async_result_types = "" # async_result_types
    result = ef.list_async_results()
    assert result.async_handles[0].async_result_id == 1, "Died on +.async_handles[0].async_result_id"
    assert result.async_handles[0].success == True, "Died on +.async_handles[0].success"
    assert result.async_handles[0].completed == True, "Died on +.async_handles[0].completed"
    assert result.async_handles[0].last_update_time == """2016-10-27T16:09:49Z""", "Died on +.async_handles[0].last_update_time"
    assert result.async_handles[0].result_type == """DriveAdd""", "Died on +.async_handles[0].result_type"
    assert type(result.async_handles[0].data) is dict, "Died on .async_handles[0].data"
    assert result.async_handles[0].create_time == """2016-10-27T16:09:29Z""", "Died on +.async_handles[0].create_time"

def test_list_drive_stats_v9():
    ef = Element("10.117.60.15", "admin", "admin", 9.0)
    ef._dispatcher.post = MagicMock(return_value = Resources.RESP_ListDriveStats_v9)

    
    drives = 42 # drives
    result = ef.list_drive_stats(drives,)
    assert result.drive_stats[0].reserve_capacity_percent == 100, "Died on +.drive_stats[0].reserve_capacity_percent"
    assert result.drive_stats[0].total_capacity == 300069052416, "Died on +.drive_stats[0].total_capacity"
    assert result.drive_stats[0].write_bytes == 2462169894, "Died on +.drive_stats[0].write_bytes"
    assert result.drive_stats[0].power_on_hours == 17736, "Died on +.drive_stats[0].power_on_hours"
    assert result.drive_stats[0].failed_die_count == 0, "Died on +.drive_stats[0].failed_die_count"
    assert result.drive_stats[0].lifetime_read_bytes == 30171004403712, "Died on +.drive_stats[0].lifetime_read_bytes"
    assert result.drive_stats[0].timestamp == """2016-03-01T00:19:24.782735Z""", "Died on +.drive_stats[0].timestamp"
    assert result.drive_stats[0].read_ops == 3624, "Died on +.drive_stats[0].read_ops"
    assert result.drive_stats[0].lifetime_write_bytes == 103464755527680, "Died on +.drive_stats[0].lifetime_write_bytes"
    assert result.drive_stats[0].drive_id == 22, "Died on +.drive_stats[0].drive_id"
    assert result.drive_stats[0].used_memory == 879165440, "Died on +.drive_stats[0].used_memory"
    assert result.drive_stats[0].read_bytes == 14656542, "Died on +.drive_stats[0].read_bytes"
    assert result.drive_stats[0].life_remaining_percent == 84, "Died on +.drive_stats[0].life_remaining_percent"
    assert result.drive_stats[0].reallocated_sectors == 0, "Died on +.drive_stats[0].reallocated_sectors"
    assert result.drive_stats[0].write_ops == 608802, "Died on +.drive_stats[0].write_ops"
    assert result.drive_stats[0].used_capacity == 1783735635, "Died on +.drive_stats[0].used_capacity"
    assert type(result.errors[0]) is dict, "Died on .errors[0]"

def test_list_fibre_channel_sessions_v9():
    ef = Element("10.117.60.15", "admin", "admin", 9.0)
    ef._dispatcher.post = MagicMock(return_value = Resources.RESP_ListFibreChannelSessions_v9)

    
    result = ef.list_fibre_channel_sessions()
    assert result.sessions[1].target_wwpn == """5f:47:ac:c0:00:00:00:11""", "Died on +.sessions[1].target_wwpn"
    assert result.sessions[1].service_id == 22, "Died on +.sessions[1].service_id"
    assert result.sessions[1].node_id == 1, "Died on +.sessions[1].node_id"
    assert result.sessions[1].initiator_wwpn == """21:00:00:0e:1e:14:af:40""", "Died on +.sessions[1].initiator_wwpn"
    assert result.sessions[1].volume_access_group_id == 7, "Died on +.sessions[1].volume_access_group_id"
    assert result.sessions[0].target_wwpn == """5f:47:ac:c0:00:00:00:10""", "Died on +.sessions[0].target_wwpn"
    assert result.sessions[0].service_id == 21, "Died on +.sessions[0].service_id"
    assert result.sessions[0].node_id == 5, "Died on +.sessions[0].node_id"
    assert result.sessions[0].initiator_wwpn == """21:00:00:0e:1e:14:af:40""", "Died on +.sessions[0].initiator_wwpn"
    assert result.sessions[0].volume_access_group_id == 7, "Died on +.sessions[0].volume_access_group_id"

def test_list_iscsisessions_v9():
    ef = Element("10.117.60.15", "admin", "admin", 9.0)
    ef._dispatcher.post = MagicMock(return_value = Resources.RESP_ListISCSISessions_v9)

    
    result = ef.list_iscsisessions()
    assert result.sessions[1].volume_instance == 139922531221504, "Died on +.sessions[1].volume_instance"
    assert type(result.sessions[1].initiator.attributes) is dict, "Died on .sessions[1].initiator.attributes"
    assert result.sessions[1].initiator.initiator_name == """iqn.2010-01.net.solidfire.eng:zdc-3""", "Died on +.sessions[1].initiator.initiator_name"
    assert result.sessions[1].initiator.volume_access_groups[0] == 1, "Died on +.sessions[1].initiator.volume_access_groups[0]"
    assert result.sessions[1].initiator.initiator_id == 2, "Died on +.sessions[1].initiator.initiator_id"
    assert result.sessions[1].initiator_ip == """10.30.76.3:33995""", "Died on +.sessions[1].initiator_ip"
    assert result.sessions[1].initiator_session_id == 9613869056, "Died on +.sessions[1].initiator_session_id"
    assert result.sessions[1].initiator_port_name == """iqn.2010-01.net.solidfire.eng:zdc-3,i,0x23d080000""", "Died on +.sessions[1].initiator_port_name"
    assert result.sessions[1].node_id == 1, "Died on +.sessions[1].node_id"
    assert result.sessions[1].account_name == """myaccount""", "Died on +.sessions[1].account_name"
    assert result.sessions[1].drive_id == 1, "Died on +.sessions[1].drive_id"
    assert result.sessions[1].session_id == 17179882018, "Died on +.sessions[1].session_id"
    assert result.sessions[1].service_id == 4, "Died on +.sessions[1].service_id"
    assert result.sessions[1].initiator_name == """iqn.2010-01.net.solidfire.eng:zdc-3""", "Died on +.sessions[1].initiator_name"
    assert result.sessions[1].target_ip == """10.30.65.134:3260""", "Died on +.sessions[1].target_ip"
    assert result.sessions[1].virtual_network_id == 0, "Died on +.sessions[1].virtual_network_id"
    assert result.sessions[1].account_id == 1, "Died on +.sessions[1].account_id"
    assert result.sessions[1].target_name == """iqn.2010-01.com.solidfire:dvmj.trruw982e4vr2cgf.9""", "Died on +.sessions[1].target_name"
    assert result.sessions[1].create_time == """2016-08-12T16:40:04.827831Z""", "Died on +.sessions[1].create_time"
    assert result.sessions[1].volume_id == 9, "Died on +.sessions[1].volume_id"
    assert result.sessions[1].target_port_name == """iqn.2010-01.com.solidfire:dvmj.trruw982e4vr2cgf.9,t,0x1""", "Died on +.sessions[1].target_port_name"
    assert result.sessions[0].volume_instance == 139922648856576, "Died on +.sessions[0].volume_instance"
    assert type(result.sessions[0].initiator.attributes) is dict, "Died on .sessions[0].initiator.attributes"
    assert result.sessions[0].initiator.initiator_name == """iqn.2010-01.net.solidfire.eng:zdc-3""", "Died on +.sessions[0].initiator.initiator_name"
    assert result.sessions[0].initiator.volume_access_groups[0] == 1, "Died on +.sessions[0].initiator.volume_access_groups[0]"
    assert result.sessions[0].initiator.initiator_id == 2, "Died on +.sessions[0].initiator.initiator_id"
    assert result.sessions[0].initiator_ip == """10.30.76.3:33994""", "Died on +.sessions[0].initiator_ip"
    assert result.sessions[0].initiator_session_id == 9613803520, "Died on +.sessions[0].initiator_session_id"
    assert result.sessions[0].initiator_port_name == """iqn.2010-01.net.solidfire.eng:zdc-3,i,0x23d070000""", "Died on +.sessions[0].initiator_port_name"
    assert result.sessions[0].node_id == 1, "Died on +.sessions[0].node_id"
    assert result.sessions[0].account_name == """myaccount""", "Died on +.sessions[0].account_name"
    assert result.sessions[0].drive_id == 1, "Died on +.sessions[0].drive_id"
    assert result.sessions[0].session_id == 17179882017, "Died on +.sessions[0].session_id"
    assert result.sessions[0].service_id == 4, "Died on +.sessions[0].service_id"
    assert result.sessions[0].initiator_name == """iqn.2010-01.net.solidfire.eng:zdc-3""", "Died on +.sessions[0].initiator_name"
    assert result.sessions[0].target_ip == """10.30.65.134:3260""", "Died on +.sessions[0].target_ip"
    assert result.sessions[0].virtual_network_id == 0, "Died on +.sessions[0].virtual_network_id"
    assert result.sessions[0].account_id == 1, "Died on +.sessions[0].account_id"
    assert result.sessions[0].target_name == """iqn.2010-01.com.solidfire:dvmj.aawuanfmxukfnffl.3""", "Died on +.sessions[0].target_name"
    assert result.sessions[0].create_time == """2016-08-12T16:40:04.827786Z""", "Died on +.sessions[0].create_time"
    assert result.sessions[0].volume_id == 3, "Died on +.sessions[0].volume_id"
    assert result.sessions[0].target_port_name == """iqn.2010-01.com.solidfire:dvmj.aawuanfmxukfnffl.3,t,0x1""", "Died on +.sessions[0].target_port_name"

def test_list_protocol_endpoints_v9():
    ef = Element("10.117.60.15", "admin", "admin", 9.0)
    ef._dispatcher.post = MagicMock(return_value = Resources.RESP_ListProtocolEndpoints_v9)

    
    protocol_endpoint_ids = UUID("2b0653fb-3d64-4ae0-9ef8-356e685b0b2e") # protocol_endpoint_ids
    result = ef.list_protocol_endpoints()
    assert result.protocol_endpoints[3].primary_provider_id == 3, "Died on +.protocol_endpoints[3].primary_provider_id"
    assert result.protocol_endpoints[3].protocol_endpoint_state == """Active""", "Died on +.protocol_endpoints[3].protocol_endpoint_state"
    assert result.protocol_endpoints[3].provider_type == """Primary""", "Died on +.protocol_endpoints[3].provider_type"
    assert result.protocol_endpoints[3].protocol_endpoint_id == UUID("f3e7911d-0e86-4776-97db-7468c272213f"), "Died on .protocol_endpoints[3].protocol_endpoint_id"
    assert result.protocol_endpoints[3].secondary_provider_id == 4, "Died on +.protocol_endpoints[3].secondary_provider_id"
    assert result.protocol_endpoints[3].scsi_naadevice_id == """6f47acc2000000036970687200000000""", "Died on +.protocol_endpoints[3].scsi_naadevice_id"
    assert result.protocol_endpoints[2].primary_provider_id == 4, "Died on +.protocol_endpoints[2].primary_provider_id"
    assert result.protocol_endpoints[2].protocol_endpoint_state == """Active""", "Died on +.protocol_endpoints[2].protocol_endpoint_state"
    assert result.protocol_endpoints[2].provider_type == """Primary""", "Died on +.protocol_endpoints[2].provider_type"
    assert result.protocol_endpoints[2].protocol_endpoint_id == UUID("c6458dfe-9803-4350-bb4e-68a3feb7e830"), "Died on .protocol_endpoints[2].protocol_endpoint_id"
    assert result.protocol_endpoints[2].secondary_provider_id == 1, "Died on +.protocol_endpoints[2].secondary_provider_id"
    assert result.protocol_endpoints[2].scsi_naadevice_id == """6f47acc2000000046970687200000000""", "Died on +.protocol_endpoints[2].scsi_naadevice_id"
    assert result.protocol_endpoints[1].primary_provider_id == 2, "Died on +.protocol_endpoints[1].primary_provider_id"
    assert result.protocol_endpoints[1].protocol_endpoint_state == """Active""", "Died on +.protocol_endpoints[1].protocol_endpoint_state"
    assert result.protocol_endpoints[1].provider_type == """Primary""", "Died on +.protocol_endpoints[1].provider_type"
    assert result.protocol_endpoints[1].protocol_endpoint_id == UUID("1f16ed86-3f31-4c76-b004-a1251187700b"), "Died on .protocol_endpoints[1].protocol_endpoint_id"
    assert result.protocol_endpoints[1].secondary_provider_id == 3, "Died on +.protocol_endpoints[1].secondary_provider_id"
    assert result.protocol_endpoints[1].scsi_naadevice_id == """6f47acc2000000026970687200000000""", "Died on +.protocol_endpoints[1].scsi_naadevice_id"
    assert result.protocol_endpoints[0].primary_provider_id == 1, "Died on +.protocol_endpoints[0].primary_provider_id"
    assert result.protocol_endpoints[0].protocol_endpoint_state == """Active""", "Died on +.protocol_endpoints[0].protocol_endpoint_state"
    assert result.protocol_endpoints[0].provider_type == """Primary""", "Died on +.protocol_endpoints[0].provider_type"
    assert result.protocol_endpoints[0].protocol_endpoint_id == UUID("1387e257-d2e3-4446-be6d-39db71583e7b"), "Died on .protocol_endpoints[0].protocol_endpoint_id"
    assert result.protocol_endpoints[0].secondary_provider_id == 2, "Died on +.protocol_endpoints[0].secondary_provider_id"
    assert result.protocol_endpoints[0].scsi_naadevice_id == """6f47acc2000000016970687200000000""", "Died on +.protocol_endpoints[0].scsi_naadevice_id"

def test_list_virtual_volume_bindings_v9():
    ef = Element("10.117.60.15", "admin", "admin", 9.0)
    ef._dispatcher.post = MagicMock(return_value = Resources.RESP_ListVirtualVolumeBindings_v9)

    
    virtual_volume_binding_ids = 42 # virtual_volume_binding_ids
    calling_virtual_volume_host_id = UUID("2b0653fb-3d64-4ae0-9ef8-356e685b0b2e") # calling_virtual_volume_host_id
    result = ef.list_virtual_volume_bindings()
    assert result.bindings[0].virtual_volume_host_id == UUID("564de1a4-9a99-da0f-8b7c-3a41dfd64bf1"), "Died on .bindings[0].virtual_volume_host_id"
    assert result.bindings[0].protocol_endpoint_id == UUID("5dd53da0-b9b7-43f9-9b7e-b41c2558e92b"), "Died on .bindings[0].protocol_endpoint_id"
    assert result.bindings[0].virtual_volume_binding_id == 177, "Died on +.bindings[0].virtual_volume_binding_id"
    assert result.bindings[0].virtual_volume_secondary_id == """0xe200000000a6""", "Died on +.bindings[0].virtual_volume_secondary_id"
    assert result.bindings[0].protocol_endpoint_in_band_id == """naa.6f47acc2000000016a67746700000000""", "Died on +.bindings[0].protocol_endpoint_in_band_id"
    assert result.bindings[0].protocol_endpoint_type == """SCSI""", "Died on +.bindings[0].protocol_endpoint_type"
    assert result.bindings[0].virtual_volume_id == UUID("269d3378-1ca6-4175-a18f-6d4839e5c746"), "Died on .bindings[0].virtual_volume_id"

def test_list_virtual_volume_hosts_v9():
    ef = Element("10.117.60.15", "admin", "admin", 9.0)
    ef._dispatcher.post = MagicMock(return_value = Resources.RESP_ListVirtualVolumeHosts_v9)

    
    virtual_volume_host_ids = UUID("2b0653fb-3d64-4ae0-9ef8-356e685b0b2e") # virtual_volume_host_ids
    calling_virtual_volume_host_id = UUID("2b0653fb-3d64-4ae0-9ef8-356e685b0b2e") # calling_virtual_volume_host_id
    result = ef.list_virtual_volume_hosts()
    assert result.hosts[0].visible_protocol_endpoint_ids[0] == UUID("5dd53da0-b9b7-43f9-9b7e-b41c2558e92b"), "Died on .hosts[0].visible_protocol_endpoint_ids[0]"
    assert result.hosts[0].virtual_volume_host_id == UUID("564de1a4-9a99-da0f-8b7c-3a41dfd64bf1"), "Died on .hosts[0].virtual_volume_host_id"
    assert result.hosts[0].initiator_names[1] == """iqn.1998-01.com.vmware:zdc-dhcp-0-c-29-d6-4b-f1-5bcf9254""", "Died on +.hosts[0].initiator_names[1]"
    assert result.hosts[0].initiator_names[0] == """iqn.1998-01.com.vmware:zdc-dhcp-0-c-29-d6-4b-f1-1a0cd614""", "Died on +.hosts[0].initiator_names[0]"
    assert result.hosts[0].cluster_id == UUID("5ebdb4ad-9617-4647-adfd-c1013578483b"), "Died on .hosts[0].cluster_id"
    assert result.hosts[0].host_address == """172.30.89.117""", "Died on +.hosts[0].host_address"

def test_list_virtual_volumes_v9():
    ef = Element("10.117.60.15", "admin", "admin", 9.0)
    ef._dispatcher.post = MagicMock(return_value = Resources.RESP_ListVirtualVolumes_v9)

    
    details = True # details
    limit = 42 # limit
    recursive = True # recursive
    start_virtual_volume_id = UUID("2b0653fb-3d64-4ae0-9ef8-356e685b0b2e") # start_virtual_volume_id
    virtual_volume_ids = UUID("2b0653fb-3d64-4ae0-9ef8-356e685b0b2e") # virtual_volume_ids
    result = ef.list_virtual_volumes()
    assert result.virtual_volumes[0].status == """done""", "Died on +.virtual_volumes[0].status"
    assert result.virtual_volumes[0].volume_info is None, "Died on .virtual_volumes[0].volume_info"
    assert result.virtual_volumes[0].parent_virtual_volume_id == UUID("00000000-0000-0000-0000-000000000000"), "Died on .virtual_volumes[0].parent_virtual_volume_id"
    assert result.virtual_volumes[0].storage_container.status == """active""", "Died on +.virtual_volumes[0].storage_container.status"
    assert result.virtual_volumes[0].storage_container.storage_container_id == UUID("abaab415-bedc-44cd-98b8-f37495884db0"), "Died on .virtual_volumes[0].storage_container.storage_container_id"
    assert result.virtual_volumes[0].storage_container.name == """test""", "Died on +.virtual_volumes[0].storage_container.name"
    assert result.virtual_volumes[0].storage_container.initiator_secret == """B5)D1y10K)8IDN58""", "Died on +.virtual_volumes[0].storage_container.initiator_secret"
    assert result.virtual_volumes[0].storage_container.target_secret == """qgae@{o{~82U)U^""", "Died on +.virtual_volumes[0].storage_container.target_secret"
    assert result.virtual_volumes[0].storage_container.protocol_endpoint_type == """SCSI""", "Died on +.virtual_volumes[0].storage_container.protocol_endpoint_type"
    assert result.virtual_volumes[0].storage_container.account_id == 1, "Died on +.virtual_volumes[0].storage_container.account_id"
    assert result.virtual_volumes[0].volume_id == 166, "Died on +.virtual_volumes[0].volume_id"
    assert result.virtual_volumes[0].virtual_volume_type == """config""", "Died on +.virtual_volumes[0].virtual_volume_type"
    assert result.virtual_volumes[0].snapshot_id == 0, "Died on +.virtual_volumes[0].snapshot_id"
    assert result.virtual_volumes[0].snapshot_info is None, "Died on .virtual_volumes[0].snapshot_info"
    assert result.virtual_volumes[0].bindings[0] == 177, "Died on +.virtual_volumes[0].bindings[0]"
    assert type(result.virtual_volumes[0].metadata) is dict, "Died on .virtual_volumes[0].metadata"
    assert result.virtual_volumes[0].virtual_volume_id == UUID("269d3378-1ca6-4175-a18f-6d4839e5c746"), "Died on .virtual_volumes[0].virtual_volume_id"
    assert result.next_virtual_volume_id == UUID("00000000-0000-0000-0000-000000000000"), "Died on .next_virtual_volume_id"

def test_list_virtual_volume_tasks_v9():
    ef = Element("10.117.60.15", "admin", "admin", 9.0)
    ef._dispatcher.post = MagicMock(return_value = Resources.RESP_ListVirtualVolumeTasks_v9)

    
    virtual_volume_task_ids = UUID("2b0653fb-3d64-4ae0-9ef8-356e685b0b2e") # virtual_volume_task_ids
    calling_virtual_volume_host_id = UUID("2b0653fb-3d64-4ae0-9ef8-356e685b0b2e") # calling_virtual_volume_host_id
    result = ef.list_virtual_volume_tasks()
    assert result.tasks[0].status == """success""", "Died on +.tasks[0].status"
    assert result.tasks[0].virtual_volume_host_id == UUID("564de1a4-9a99-da0f-8b7c-3a41dfd64bf1"), "Died on .tasks[0].virtual_volume_host_id"
    assert result.tasks[0].virtual_volume_task_id == UUID("a1b72df7-66a6-489a-86e4-538d0dbe05bf"), "Died on .tasks[0].virtual_volume_task_id"
    assert result.tasks[0].parent_used_size == 0, "Died on +.tasks[0].parent_used_size"
    assert result.tasks[0].clone_virtual_volume_id == UUID("fafeb3a0-7dd9-4c9f-8a07-80e0bbf6f4d0"), "Died on .tasks[0].clone_virtual_volume_id"
    assert result.tasks[0].parent_total_size == 42949672960, "Died on +.tasks[0].parent_total_size"
    assert result.tasks[0].cancelled == False, "Died on +.tasks[0].cancelled"
    assert type(result.tasks[0].parent_metadata) is dict, "Died on .tasks[0].parent_metadata"
    assert result.tasks[0].operation == """clone""", "Died on +.tasks[0].operation"
    assert result.tasks[0].virtualvolume_id == UUID("fafeb3a0-7dd9-4c9f-8a07-80e0bbf6f4d0"), "Died on .tasks[0].virtualvolume_id"

def test_list_volume_access_groups_v9():
    ef = Element("10.117.60.15", "admin", "admin", 9.0)
    ef._dispatcher.post = MagicMock(return_value = Resources.RESP_ListVolumeAccessGroups_v9)

    
    start_volume_access_group_id = 42 # start_volume_access_group_id
    limit = 42 # limit
    result = ef.list_volume_access_groups()
    assert result.volume_access_groups[1].name == """loyds""", "Died on +.volume_access_groups[1].name"
    assert result.volume_access_groups[1].initiator_ids[1] == 5, "Died on +.volume_access_groups[1].initiator_ids[1]"
    assert result.volume_access_groups[1].initiator_ids[0] == 4, "Died on +.volume_access_groups[1].initiator_ids[0]"
    assert result.volume_access_groups[1].volumes[0] == 5, "Died on +.volume_access_groups[1].volumes[0]"
    assert result.volume_access_groups[1].initiators[1] == """21:00:00:0e:1e:1b:2a:41""", "Died on +.volume_access_groups[1].initiators[1]"
    assert result.volume_access_groups[1].initiators[0] == """21:00:00:0e:1e:1b:2a:40""", "Died on +.volume_access_groups[1].initiators[0]"
    assert type(result.volume_access_groups[1].attributes) is dict, "Died on .volume_access_groups[1].attributes"
    assert result.volume_access_groups[1].volume_access_group_id == 2, "Died on +.volume_access_groups[1].volume_access_group_id"
    assert result.volume_access_groups[0].name == """sra-site1-esxi""", "Died on +.volume_access_groups[0].name"
    assert result.volume_access_groups[0].initiator_ids[0] == 1, "Died on +.volume_access_groups[0].initiator_ids[0]"
    assert result.volume_access_groups[0].volumes[1] == 4, "Died on +.volume_access_groups[0].volumes[1]"
    assert result.volume_access_groups[0].volumes[0] == 2, "Died on +.volume_access_groups[0].volumes[0]"
    assert result.volume_access_groups[0].initiators[0] == """iqn.1998-01.com.vmware:sra-site1-esxi""", "Died on +.volume_access_groups[0].initiators[0]"
    assert type(result.volume_access_groups[0].attributes) is dict, "Died on .volume_access_groups[0].attributes"
    assert result.volume_access_groups[0].volume_access_group_id == 1, "Died on +.volume_access_groups[0].volume_access_group_id"

def test_modify_storage_container_v9():
    ef = Element("10.117.60.15", "admin", "admin", 9.0)
    ef._dispatcher.post = MagicMock(return_value = Resources.RESP_ModifyStorageContainer_v9)

    
    storage_container_id = UUID("2b0653fb-3d64-4ae0-9ef8-356e685b0b2e") # storage_container_id
    initiator_secret = "" # initiator_secret
    target_secret = "" # target_secret
    result = ef.modify_storage_container(storage_container_id,)
    assert result.storage_container.status == """active""", "Died on +.storage_container.status"
    assert result.storage_container.storage_container_id == UUID("b4528ea8-2930-41a0-8b8e-6361e1f0a71f"), "Died on .storage_container.storage_container_id"
    assert result.storage_container.name == """ExampleName""", "Died on +.storage_container.name"
    assert result.storage_container.initiator_secret == """e;~t5f4T~r8CQK9""", "Died on +.storage_container.initiator_secret"
    assert result.storage_container.target_secret == """LIU4?KW8mOlMZO^6""", "Died on +.storage_container.target_secret"
    assert result.storage_container.protocol_endpoint_type == """SCSI""", "Died on +.storage_container.protocol_endpoint_type"
    assert result.storage_container.account_id == 114, "Died on +.storage_container.account_id"

def test_modify_volume_access_group_v9():
    ef = Element("10.117.60.15", "admin", "admin", 9.0)
    ef._dispatcher.post = MagicMock(return_value = Resources.RESP_ModifyVolumeAccessGroup_v9)

    
    volume_access_group_id = 42 # volume_access_group_id
    virtual_network_id = 42 # virtual_network_id
    virtual_network_tags = 42 # virtual_network_tags
    name = "" # name
    initiators = "" # initiators
    volumes = 42 # volumes
    attributes = dict() # attributes
    result = ef.modify_volume_access_group(volume_access_group_id,)
    assert result.volume_access_group.name == """northbanktest""", "Died on +.volume_access_group.name"
    assert result.volume_access_group.deleted_volumes[0] == 327, "Died on +.volume_access_group.deleted_volumes[0]"
    assert result.volume_access_group.initiator_ids[1] == 115, "Died on +.volume_access_group.initiator_ids[1]"
    assert result.volume_access_group.initiator_ids[0] == 114, "Died on +.volume_access_group.initiator_ids[0]"
    assert result.volume_access_group.volumes[0] == 346, "Died on +.volume_access_group.volumes[0]"
    assert result.volume_access_group.initiators[1] == """iqn.1998-01.com.vmware:donesq-esx1-421b281b""", "Died on +.volume_access_group.initiators[1]"
    assert result.volume_access_group.initiators[0] == """iqn.1998-01.com.vmware:desk1-esx1-577b283a""", "Died on +.volume_access_group.initiators[0]"
    assert type(result.volume_access_group.attributes) is dict, "Died on .volume_access_group.attributes"
    assert result.volume_access_group.volume_access_group_id == 96, "Died on +.volume_access_group.volume_access_group_id"

def test_modify_volumes_v9():
    ef = Element("10.117.60.15", "admin", "admin", 9.0)
    ef._dispatcher.post = MagicMock(return_value = Resources.RESP_ModifyVolumes_v9)

    
    volume_ids = 42 # volume_ids
    account_id = 42 # account_id
    access = "" # access
    attributes = dict() # attributes
    mode = "" # mode
    qos = dict() # qos
    total_size = 42 # total_size
    result = ef.modify_volumes(volume_ids,)
    assert result.volumes[1].status == """active""", "Died on +.volumes[1].status"
    assert result.volumes[1].enable512e == False, "Died on +.volumes[1].enable512e"
    assert result.volumes[1].qos.burst_iops == 150, "Died on +.volumes[1].qos.burst_iops"
    assert result.volumes[1].qos.min_iops == 50, "Died on +.volumes[1].qos.min_iops"
    assert result.volumes[1].qos.max_iops == 100, "Died on +.volumes[1].qos.max_iops"
    assert result.volumes[1].qos.burst_time == 60, "Died on +.volumes[1].qos.burst_time"
    assert result.volumes[1].name == """doctest2""", "Died on +.volumes[1].name"
    assert result.volumes[1].total_size == 1000341504, "Died on +.volumes[1].total_size"
    assert result.volumes[1].block_size == 4096, "Died on +.volumes[1].block_size"
    assert result.volumes[1].account_id == 1, "Died on +.volumes[1].account_id"
    assert result.volumes[1].scsi_euidevice_id == """6a6f373300000003f47acc0100000000""", "Died on +.volumes[1].scsi_euidevice_id"
    assert result.volumes[1].volume_id == 3, "Died on +.volumes[1].volume_id"
    assert result.volumes[1].access == """replicationTarget""", "Died on +.volumes[1].access"
    assert type(result.volumes[1].attributes) is dict, "Died on .volumes[1].attributes"
    assert result.volumes[1].slice_count == 1, "Died on +.volumes[1].slice_count"
    assert result.volumes[1].iqn == """iqn.2010-01.com.solidfire:jo73.3""", "Died on +.volumes[1].iqn"
    assert result.volumes[1].scsi_naadevice_id == """6f47acc1000000006a6f373300000003""", "Died on +.volumes[1].scsi_naadevice_id"
    assert result.volumes[1].create_time == """2016-04-06T17:26:31Z""", "Died on +.volumes[1].create_time"
    assert result.volumes[1].virtual_volume_id is None, "Died on .volumes[1].virtual_volume_id"
    assert result.volumes[0].status == """active""", "Died on +.volumes[0].status"
    assert result.volumes[0].enable512e == False, "Died on +.volumes[0].enable512e"
    assert result.volumes[0].qos.burst_iops == 150, "Died on +.volumes[0].qos.burst_iops"
    assert result.volumes[0].qos.min_iops == 50, "Died on +.volumes[0].qos.min_iops"
    assert result.volumes[0].qos.max_iops == 100, "Died on +.volumes[0].qos.max_iops"
    assert result.volumes[0].qos.burst_time == 60, "Died on +.volumes[0].qos.burst_time"
    assert result.volumes[0].name == """doctest1""", "Died on +.volumes[0].name"
    assert result.volumes[0].total_size == 1000341504, "Died on +.volumes[0].total_size"
    assert result.volumes[0].block_size == 4096, "Died on +.volumes[0].block_size"
    assert result.volumes[0].account_id == 1, "Died on +.volumes[0].account_id"
    assert result.volumes[0].scsi_euidevice_id == """6a6f373300000002f47acc0100000000""", "Died on +.volumes[0].scsi_euidevice_id"
    assert result.volumes[0].volume_id == 2, "Died on +.volumes[0].volume_id"
    assert result.volumes[0].access == """replicationTarget""", "Died on +.volumes[0].access"
    assert type(result.volumes[0].attributes) is dict, "Died on .volumes[0].attributes"
    assert result.volumes[0].slice_count == 1, "Died on +.volumes[0].slice_count"
    assert result.volumes[0].iqn == """iqn.2010-01.com.solidfire:jo73.2""", "Died on +.volumes[0].iqn"
    assert result.volumes[0].scsi_naadevice_id == """6f47acc1000000006a6f373300000002""", "Died on +.volumes[0].scsi_naadevice_id"
    assert result.volumes[0].create_time == """2016-04-06T17:25:13Z""", "Died on +.volumes[0].create_time"
    assert result.volumes[0].virtual_volume_id is None, "Died on .volumes[0].virtual_volume_id"

def test_purge_deleted_volumes_v9():
    ef = Element("10.117.60.15", "admin", "admin", 9.0)
    ef._dispatcher.post = MagicMock(return_value = Resources.RESP_PurgeDeletedVolumes_v9)

    
    volume_ids = 42 # volume_ids
    account_ids = 42 # account_ids
    volume_access_group_ids = 42 # volume_access_group_ids
    result = ef.purge_deleted_volumes()

def test_set_default_qos_v9():
    ef = Element("10.117.60.15", "admin", "admin", 9.0)
    ef._dispatcher.post = MagicMock(return_value = Resources.RESP_SetDefaultQoS_v9)

    
    min_iops = 42 # min_iops
    max_iops = 42 # max_iops
    burst_iops = 42 # burst_iops
    result = ef.set_default_qos()
    assert result.burst_iops == 8000, "Died on +.burst_iops"
    assert result.min_iops == 200, "Died on +.min_iops"
    assert result.max_iops == 1000, "Died on +.max_iops"


if __name__ == "__main__":
    test_cancel_clone_v9()
    test_cancel_group_clone_v9()
    test_copy_volume_v9()
    test_create_storage_container_v9()
    test_create_volume_access_group_v9()
    test_delete_storage_containers_v9()
    test_delete_volumes_v9()
    test_enable_feature_v9()
    test_get_cluster_hardware_info_v9()
    test_get_feature_status_v9()
    test_get_hardware_config_v9()
    test_get_hardware_info_v9()
    test_get_limits_v9()
    test_get_network_config_v9()
    test_get_node_hardware_info_v9()
    test_get_nvram_info_v9()
    test_get_storage_container_efficiency_v9()
    test_get_virtual_volume_count_v9()
    test_list_async_results_v9()
    test_list_drive_stats_v9()
    test_list_fibre_channel_sessions_v9()
    test_list_iscsisessions_v9()
    test_list_protocol_endpoints_v9()
    test_list_virtual_volume_bindings_v9()
    test_list_virtual_volume_hosts_v9()
    test_list_virtual_volumes_v9()
    test_list_virtual_volume_tasks_v9()
    test_list_volume_access_groups_v9()
    test_modify_storage_container_v9()
    test_modify_volume_access_group_v9()
    test_modify_volumes_v9()
    test_purge_deleted_volumes_v9()
    test_set_default_qos_v9()