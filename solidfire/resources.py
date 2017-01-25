RESP_CancelClone_v9_0 = """{
  "id" : 1,
  "result" : {}
}"""

RESP_CancelGroupClone_v9_0 = """{
  "id" : 1,
  "result" : {}
}"""

RESP_CopyVolume_v9_0 = """{
  "id": 1,
  "result": {
    "asyncHandle": 9,
    "cloneID": 5
  }
}"""

RESP_CreateStorageContainer_v9_0 = """{
  "id": null,
  "result": {
    "storageContainer": {
      "accountID": 111,
      "initiatorSecret": "Z5k)Cf~jiIxp3R4[",
      "name": "ExampleName",
      "protocolEndpointType": "SCSI",
      "status": "active",
      "storageContainerID": "2b0653fb-3d64-4ae0-9ef8-356e685b0b2e",
      "targetSecret": "N07S4}aEh5oU]L0l"
    }
  }
}"""

RESP_CreateVolumeAccessGroup_v9_0 = """{
  "id": null,
  "result": {
    "volumeAccessGroup": {
      "attributes": {},
      "deletedVolumes": [],
      "initiatorIDs": [
        95
      ],
      "initiators": [
        "iqn.1993-08.org.debian: 01: a31b1d799d5c"
      ],
      "name": "myaccessgroup",
      "volumeAccessGroupID": 96,
      "volumes": [
        327
      ]
    },
    "volumeAccessGroupID": 96
  }
}"""

RESP_DeleteStorageContainers_v9_0 = """{
  "id": null,
  "result": {}
}"""

RESP_DeleteVolumes_v9_0 = """ {
  "id" : 1,
  "result": {
    "volumes" : [ {
      "access": "readWrite",
      "accountID": 1,
      "attributes": {},
      "blockSize": 4096,
      "createTime": "2015-03-06T18:50:56Z",
      "deleteTime": "",
      "enable512e": false,
      "iqn": "iqn.2010-01.com.solidfire:pzsr.vclient-030-v00001.1",
      "name": "vclient-030-v00001",
      "qos": {
        "burstIOPS": 15000,
        "burstTime": 60,
        "curve": {},
        "maxIOPS": 15000,
        "minIOPS": 100
      },
      "purgeTime": "",
      "sliceCount": 1,
      "scsiEUIDeviceID": "707a737200000001f47acc0100000000",
      "scsiNAADeviceID": "6f47acc100000000707a737200000001",
      "status": "active",
      "totalSize": 10000003072,
      "virtualVolumeID": "b4528ea8-2930-41a0-8b8e-6361e1f0a71f",
      "volumeAccessGroups": [],
      "volumePairs": [],
      "volumeID": 1
    } ]
  }
}"""

RESP_EnableFeature_v9_0 = """{
  "id": null,
  "result": {}
}"""

RESP_GetAccountEfficiency_v9_0 = """{"id":null,"result":{"compression":29.73816415189271,"deduplication":1.048435171385991,"missingVolumes":[],"thinProvisioning":7295.454157782516,"timestamp":"2016-12-08T16:00:03Z"}}"""

RESP_GetClusterHardwareInfo_v9_0 = """{
  "id": null,
  "result": {
    "clusterHardwareInfo": {
      "drives": {
        "1": {
          "description": "ATA      Drive",
          "dev": "8:0",
          "devpath": "/dev/sdimm0p4",
          "driveSecurityAtMaximum": false,
          "driveSecurityFrozen": true,
          "driveSecurityLocked": false,
          "logicalname": "/dev/sda",
          "product": "VRFSD3400GBCTMMAS1",
          "scsiCompatID": "scsi-SATA_VRFSD3400GBCTMM203529284-part4",
          "securityFeatureEnabled": false,
          "securityFeatureSupported": true,
          "serial": "203529284",
          "size": 299988156416,
          "uuid": "f0b19a4b-c9a2-2e58-335f-cceb20c306cd",
          "version": "365A13F0"
        },
        "2": {
          "description": "ATA      Drive",
          "dev": "8:16",
          "devpath": "/dev/slot0",
          "driveSecurityAtMaximum": false,
          "driveSecurityFrozen": false,
          "driveSecurityLocked": false,
          "logicalname": "/dev/sdb",
          "product": "INTEL SSDSA2CW300G3",
          "scsiCompatID": "scsi-SATA_INTEL_SSDSA2CW3CVPR14620193300EGN",
          "securityFeatureEnabled": true,
          "securityFeatureSupported": true,
          "serial": "CVPR14620193300EGN",
          "size": 300069052416,
          "uuid": "b198c917-5ffe-ae63-0940-8765f786ed64",
          "version": "4PC10362"
        },
        "3": {
          "description": "ATA      Drive",
          "dev": "8:112",
          "devpath": "/dev/slot1",
          "driveSecurityAtMaximum": false,
          "driveSecurityFrozen": false,
          "driveSecurityLocked": false,
          "logicalname": "/dev/sdh",
          "product": "INTEL SSDSA2CW300G3",
          "scsiCompatID": "scsi-SATA_INTEL_SSDSA2CW3CVPR1461053H300EGN",
          "securityFeatureEnabled": true,
          "securityFeatureSupported": true,
          "serial": "CVPR1461053H300EGN",
          "size": 300069052416,
          "uuid": "355b7f51-e861-97f3-48f5-0b9bb4bb86b6",
          "version": "4PC10362"
        },
        "4": {
          "description": "ATA      Drive",
          "dev": "8:144",
          "devpath": "/dev/slot2",
          "driveSecurityAtMaximum": false,
          "driveSecurityFrozen": false,
          "driveSecurityLocked": false,
          "logicalname": "/dev/sdj",
          "product": "INTEL SSDSA2CW300G3",
          "scsiCompatID": "scsi-SATA_INTEL_SSDSA2CW3CVPR146101TT300EGN",
          "securityFeatureEnabled": true,
          "securityFeatureSupported": true,
          "serial": "CVPR146101TT300EGN",
          "size": 300069052416,
          "uuid": "b62dbadf-e62e-894e-37df-ac9dce6594ff",
          "version": "4PC10362"
        },
        "5": {
          "description": "ATA      Drive",
          "dev": "8:96",
          "devpath": "/dev/slot3",
          "driveSecurityAtMaximum": false,
          "driveSecurityFrozen": false,
          "driveSecurityLocked": false,
          "logicalname": "/dev/sdg",
          "product": "INTEL SSDSA2CW300G3",
          "scsiCompatID": "scsi-SATA_INTEL_SSDSA2CW3CVPR14620AP5300EGN",
          "securityFeatureEnabled": true,
          "securityFeatureSupported": true,
          "serial": "CVPR14620AP5300EGN",
          "size": 300069052416,
          "uuid": "c5d7a7ee-7cdf-494a-76e3-72f2284023d4",
          "version": "4PC10362"
        },
        "6": {
          "description": "ATA      Drive",
          "dev": "8:128",
          "devpath": "/dev/slot4",
          "driveSecurityAtMaximum": false,
          "driveSecurityFrozen": false,
          "driveSecurityLocked": false,
          "logicalname": "/dev/sdi",
          "product": "INTEL SSDSA2CW300G3",
          "scsiCompatID": "scsi-SATA_INTEL_SSDSA2CW3CVPR142108T5300EGN",
          "securityFeatureEnabled": true,
          "securityFeatureSupported": true,
          "serial": "CVPR142108T5300EGN",
          "size": 300069052416,
          "uuid": "545dd40d-8344-dda5-2e3d-c2ad4005283b",
          "version": "4PC10362"
        },
        "7": {
          "description": "ATA      Drive",
          "dev": "8:160",
          "devpath": "/dev/slot5",
          "driveSecurityAtMaximum": false,
          "driveSecurityFrozen": false,
          "driveSecurityLocked": false,
          "logicalname": "/dev/sdk",
          "product": "INTEL SSDSA2CW300G3",
          "scsiCompatID": "scsi-SATA_INTEL_SSDSA2CW3CVPR146401ZY300EGN",
          "securityFeatureEnabled": true,
          "securityFeatureSupported": true,
          "serial": "CVPR146401ZY300EGN",
          "size": 300069052416,
          "uuid": "47175675-a5e0-267b-4288-015ca5e9ef1b",
          "version": "4PC10362"
        },
        "8": {
          "description": "ATA      Drive",
          "dev": "8:32",
          "devpath": "/dev/slot6",
          "driveSecurityAtMaximum": false,
          "driveSecurityFrozen": false,
          "driveSecurityLocked": false,
          "logicalname": "/dev/sdc",
          "product": "INTEL SSDSA2CW300G3",
          "scsiCompatID": "scsi-SATA_INTEL_SSDSA2CW3CVPR146007NL300EGN",
          "securityFeatureEnabled": true,
          "securityFeatureSupported": true,
          "serial": "CVPR146007NL300EGN",
          "size": 300069052416,
          "uuid": "7524866c-4a31-1a4a-7aad-32b4cf83d176",
          "version": "4PC10362"
        },
        "9": {
          "description": "ATA      Drive",
          "dev": "8:64",
          "devpath": "/dev/slot7",
          "driveSecurityAtMaximum": false,
          "driveSecurityFrozen": false,
          "driveSecurityLocked": false,
          "logicalname": "/dev/sde",
          "product": "INTEL SSDSA2CW300G3",
          "scsiCompatID": "scsi-SATA_INTEL_SSDSA2CW3CVPR146007NE300EGN",
          "securityFeatureEnabled": true,
          "securityFeatureSupported": true,
          "serial": "CVPR146007NE300EGN",
          "size": 300069052416,
          "uuid": "e498c538-5798-22e7-5933-48e1e0ef9960",
          "version": "4PC10362"
        },
        "10": {
          "description": "ATA      Drive",
          "dev": "8:80",
          "devpath": "/dev/slot8",
          "driveSecurityAtMaximum": false,
          "driveSecurityFrozen": false,
          "driveSecurityLocked": false,
          "logicalname": "/dev/sdf",
          "product": "INTEL SSDSA2CW300G3",
          "scsiCompatID": "scsi-SATA_INTEL_SSDSA2CW3CVPR146104SF300EGN",
          "securityFeatureEnabled": true,
          "securityFeatureSupported": true,
          "serial": "CVPR146104SF300EGN",
          "size": 300069052416,
          "uuid": "9cc657ad-b162-6a56-b3ae-2d5c4f85bf1e",
          "version": "4PC10362"
        },
        "11": {
          "description": "ATA      Drive",
          "dev": "8:48",
          "devpath": "/dev/slot9",
          "driveSecurityAtMaximum": false,
          "driveSecurityFrozen": false,
          "driveSecurityLocked": false,
          "logicalname": "/dev/sdd",
          "product": "INTEL SSDSA2CW300G3",
          "scsiCompatID": "scsi-SATA_INTEL_SSDSA2CW3CVPR1462045W300EGN",
          "securityFeatureEnabled": true,
          "securityFeatureSupported": true,
          "serial": "CVPR1462045W300EGN",
          "size": 300069052416,
          "uuid": "caa5012e-c5ce-f2c7-a02c-0f0e6e986c3a",
          "version": "4PC10362"
        }
      },
      "nodes": {
        "1": {
          "bus": {
            "core_DMI:0200": {
              "description": "Motherboard",
              "physid": "0",
              "product": "0H47HH",
              "serial": "..CN7475122J0059.",
              "vendor": "SolidFire",
              "version": "A00"
            }
          },
          "driveHardware": [
            {
              "canonicalName": "sda",
              "connected": true,
              "dev": 2052,
              "devPath": "/dev/sdimm0p4",
              "driveType": "Slice",
              "lifeRemainingPercent": 100,
              "lifetimeReadBytes": 1471026298880,
              "lifetimeWriteBytes": 657129996288,
              "name": "scsi-SATA_VRFSD3400GBCTMM203529284-part4",
              "path": "/dev/sda4",
              "pathLink": "/dev/sdimm0p4",
              "powerOnHours": 21889,
              "product": "VRFSD3400GBCTMMAS1",
              "reallocatedSectors": 0,
              "reserveCapacityPercent": 100,
              "scsiCompatId": "scsi-SATA_VRFSD3400GBCTMM203529284-part4",
              "scsiState": "Running",
              "securityAtMaximum": false,
              "securityEnabled": false,
              "securityFrozen": true,
              "securityLocked": false,
              "securitySupported": true,
              "serial": "203529284",
              "size": 299988156416,
              "slot": -1,
              "uuid": "f0b19a4b-c9a2-2e58-335f-cceb20c306cd",
              "vendor": "Viking",
              "version": "365A13F0"
            },
            {
              "canonicalName": "sdb",
              "connected": true,
              "dev": 2064,
              "devPath": "/dev/slot0",
              "driveType": "Block",
              "lifeRemainingPercent": 67,
              "lifetimeReadBytes": 21367697178624,
              "lifetimeWriteBytes": 28688770924544,
              "name": "scsi-SATA_INTEL_SSDSA2CW3CVPR14620193300EGN",
              "path": "/dev/sdb",
              "pathLink": "/dev/slot0",
              "powerOnHours": 37461,
              "product": "INTEL SSDSA2CW300G3",
              "reallocatedSectors": 0,
              "reserveCapacityPercent": 100,
              "scsiCompatId": "scsi-SATA_INTEL_SSDSA2CW3CVPR14620193300EGN",
              "scsiState": "Running",
              "securityAtMaximum": false,
              "securityEnabled": false,
              "securityFrozen": false,
              "securityLocked": false,
              "securitySupported": true,
              "serial": "CVPR14620193300EGN",
              "size": 300069052416,
              "slot": 0,
              "uuid": "b198c917-5ffe-ae63-0940-8765f786ed64",
              "vendor": "Intel",
              "version": "4PC10362"
            },
            {
              "canonicalName": "sdh",
              "connected": true,
              "dev": 2160,
              "devPath": "/dev/slot1",
              "driveType": "Block",
              "lifeRemainingPercent": 68,
              "lifetimeReadBytes": 21356489998336,
              "lifetimeWriteBytes": 28929087766528,
              "name": "scsi-SATA_INTEL_SSDSA2CW3CVPR1461053H300EGN",
              "path": "/dev/sdh",
              "pathLink": "/dev/slot1",
              "powerOnHours": 37345,
              "product": "INTEL SSDSA2CW300G3",
              "reallocatedSectors": 0,
              "reserveCapacityPercent": 100,
              "scsiCompatId": "scsi-SATA_INTEL_SSDSA2CW3CVPR1461053H300EGN",
              "scsiState": "Running",
              "securityAtMaximum": false,
              "securityEnabled": false,
              "securityFrozen": false,
              "securityLocked": false,
              "securitySupported": true,
              "serial": "CVPR1461053H300EGN",
              "size": 300069052416,
              "slot": 1,
              "uuid": "355b7f51-e861-97f3-48f5-0b9bb4bb86b6",
              "vendor": "Intel",
              "version": "4PC10362"
            },
            {
              "canonicalName": "sdj",
              "connected": true,
              "dev": 2192,
              "devPath": "/dev/slot2",
              "driveType": "Block",
              "lifeRemainingPercent": 68,
              "lifetimeReadBytes": 21170531336192,
              "lifetimeWriteBytes": 28565223505920,
              "name": "scsi-SATA_INTEL_SSDSA2CW3CVPR146101TT300EGN",
              "path": "/dev/sdj",
              "pathLink": "/dev/slot2",
              "powerOnHours": 37457,
              "product": "INTEL SSDSA2CW300G3",
              "reallocatedSectors": 0,
              "reserveCapacityPercent": 100,
              "scsiCompatId": "scsi-SATA_INTEL_SSDSA2CW3CVPR146101TT300EGN",
              "scsiState": "Running",
              "securityAtMaximum": false,
              "securityEnabled": false,
              "securityFrozen": false,
              "securityLocked": false,
              "securitySupported": true,
              "serial": "CVPR146101TT300EGN",
              "size": 300069052416,
              "slot": 2,
              "uuid": "b62dbadf-e62e-894e-37df-ac9dce6594ff",
              "vendor": "Intel",
              "version": "4PC10362"
            },
            {
              "canonicalName": "sdg",
              "connected": true,
              "dev": 2144,
              "devPath": "/dev/slot3",
              "driveType": "Block",
              "lifeRemainingPercent": 68,
              "lifetimeReadBytes": 21286562562048,
              "lifetimeWriteBytes": 28216995610624,
              "name": "scsi-SATA_INTEL_SSDSA2CW3CVPR14620AP5300EGN",
              "path": "/dev/sdg",
              "pathLink": "/dev/slot3",
              "powerOnHours": 37344,
              "product": "INTEL SSDSA2CW300G3",
              "reallocatedSectors": 0,
              "reserveCapacityPercent": 100,
              "scsiCompatId": "scsi-SATA_INTEL_SSDSA2CW3CVPR14620AP5300EGN",
              "scsiState": "Running",
              "securityAtMaximum": false,
              "securityEnabled": false,
              "securityFrozen": false,
              "securityLocked": false,
              "securitySupported": true,
              "serial": "CVPR14620AP5300EGN",
              "size": 300069052416,
              "slot": 3,
              "uuid": "c5d7a7ee-7cdf-494a-76e3-72f2284023d4",
              "vendor": "Intel",
              "version": "4PC10362"
            },
            {
              "canonicalName": "sdi",
              "connected": true,
              "dev": 2176,
              "devPath": "/dev/slot4",
              "driveType": "Block",
              "lifeRemainingPercent": 68,
              "lifetimeReadBytes": 16556394283008,
              "lifetimeWriteBytes": 24971912937472,
              "name": "scsi-SATA_INTEL_SSDSA2CW3CVPR142108T5300EGN",
              "path": "/dev/sdi",
              "pathLink": "/dev/slot4",
              "powerOnHours": 37495,
              "product": "INTEL SSDSA2CW300G3",
              "reallocatedSectors": 0,
              "reserveCapacityPercent": 100,
              "scsiCompatId": "scsi-SATA_INTEL_SSDSA2CW3CVPR142108T5300EGN",
              "scsiState": "Running",
              "securityAtMaximum": false,
              "securityEnabled": false,
              "securityFrozen": false,
              "securityLocked": false,
              "securitySupported": true,
              "serial": "CVPR142108T5300EGN",
              "size": 300069052416,
              "slot": 4,
              "uuid": "545dd40d-8344-dda5-2e3d-c2ad4005283b",
              "vendor": "Intel",
              "version": "4PC10362"
            },
            {
              "canonicalName": "sdk",
              "connected": true,
              "dev": 2208,
              "devPath": "/dev/slot5",
              "driveType": "Block",
              "lifeRemainingPercent": 68,
              "lifetimeReadBytes": 21341323395072,
              "lifetimeWriteBytes": 28911270363136,
              "name": "scsi-SATA_INTEL_SSDSA2CW3CVPR146401ZY300EGN",
              "path": "/dev/sdk",
              "pathLink": "/dev/slot5",
              "powerOnHours": 37458,
              "product": "INTEL SSDSA2CW300G3",
              "reallocatedSectors": 0,
              "reserveCapacityPercent": 100,
              "scsiCompatId": "scsi-SATA_INTEL_SSDSA2CW3CVPR146401ZY300EGN",
              "scsiState": "Running",
              "securityAtMaximum": false,
              "securityEnabled": false,
              "securityFrozen": false,
              "securityLocked": false,
              "securitySupported": true,
              "serial": "CVPR146401ZY300EGN",
              "size": 300069052416,
              "slot": 5,
              "uuid": "47175675-a5e0-267b-4288-015ca5e9ef1b",
              "vendor": "Intel",
              "version": "4PC10362"
            },
            {
              "canonicalName": "sdc",
              "connected": true,
              "dev": 2080,
              "devPath": "/dev/slot6",
              "driveType": "Block",
              "lifeRemainingPercent": 68,
              "lifetimeReadBytes": 21032555511808,
              "lifetimeWriteBytes": 28401511432192,
              "name": "scsi-SATA_INTEL_SSDSA2CW3CVPR146007NL300EGN",
              "path": "/dev/sdc",
              "pathLink": "/dev/slot6",
              "powerOnHours": 37261,
              "product": "INTEL SSDSA2CW300G3",
              "reallocatedSectors": 0,
              "reserveCapacityPercent": 100,
              "scsiCompatId": "scsi-SATA_INTEL_SSDSA2CW3CVPR146007NL300EGN",
              "scsiState": "Running",
              "securityAtMaximum": false,
              "securityEnabled": false,
              "securityFrozen": false,
              "securityLocked": false,
              "securitySupported": true,
              "serial": "CVPR146007NL300EGN",
              "size": 300069052416,
              "slot": 6,
              "uuid": "7524866c-4a31-1a4a-7aad-32b4cf83d176",
              "vendor": "Intel",
              "version": "4PC10362"
            },
            {
              "canonicalName": "sde",
              "connected": true,
              "dev": 2112,
              "devPath": "/dev/slot7",
              "driveType": "Block",
              "lifeRemainingPercent": 68,
              "lifetimeReadBytes": 21204454866944,
              "lifetimeWriteBytes": 28637466198016,
              "name": "scsi-SATA_INTEL_SSDSA2CW3CVPR146007NE300EGN",
              "path": "/dev/sde",
              "pathLink": "/dev/slot7",
              "powerOnHours": 37460,
              "product": "INTEL SSDSA2CW300G3",
              "reallocatedSectors": 0,
              "reserveCapacityPercent": 100,
              "scsiCompatId": "scsi-SATA_INTEL_SSDSA2CW3CVPR146007NE300EGN",
              "scsiState": "Running",
              "securityAtMaximum": false,
              "securityEnabled": false,
              "securityFrozen": false,
              "securityLocked": false,
              "securitySupported": true,
              "serial": "CVPR146007NE300EGN",
              "size": 300069052416,
              "slot": 7,
              "uuid": "e498c538-5798-22e7-5933-48e1e0ef9960",
              "vendor": "Intel",
              "version": "4PC10362"
            },
            {
              "canonicalName": "sdf",
              "connected": true,
              "dev": 2128,
              "devPath": "/dev/slot8",
              "driveType": "Block",
              "lifeRemainingPercent": 100,
              "lifetimeReadBytes": 201326592,
              "lifetimeWriteBytes": 167772160,
              "name": "scsi-SATA_INTEL_SSDSA2CW3CVPR146104SF300EGN",
              "path": "/dev/sdf",
              "pathLink": "/dev/slot8",
              "powerOnHours": 1843,
              "product": "INTEL SSDSA2CW300G3",
              "reallocatedSectors": 0,
              "reserveCapacityPercent": 100,
              "scsiCompatId": "scsi-SATA_INTEL_SSDSA2CW3CVPR146104SF300EGN",
              "scsiState": "Running",
              "securityAtMaximum": false,
              "securityEnabled": false,
              "securityFrozen": false,
              "securityLocked": false,
              "securitySupported": true,
              "serial": "CVPR146104SF300EGN",
              "size": 300069052416,
              "slot": 8,
              "uuid": "9cc657ad-b162-6a56-b3ae-2d5c4f85bf1e",
              "vendor": "Intel",
              "version": "4PC10362"
            },
            {
              "canonicalName": "sdd",
              "connected": true,
              "dev": 2096,
              "devPath": "/dev/slot9",
              "driveType": "Block",
              "lifeRemainingPercent": 68,
              "lifetimeReadBytes": 21338504822784,
              "lifetimeWriteBytes": 28405235974144,
              "name": "scsi-SATA_INTEL_SSDSA2CW3CVPR1462045W300EGN",
              "path": "/dev/sdd",
              "pathLink": "/dev/slot9",
              "powerOnHours": 37464,
              "product": "INTEL SSDSA2CW300G3",
              "reallocatedSectors": 0,
              "reserveCapacityPercent": 100,
              "scsiCompatId": "scsi-SATA_INTEL_SSDSA2CW3CVPR1462045W300EGN",
              "scsiState": "Running",
              "securityAtMaximum": false,
              "securityEnabled": false,
              "securityFrozen": false,
              "securityLocked": false,
              "securitySupported": true,
              "serial": "CVPR1462045W300EGN",
              "size": 300069052416,
              "slot": 9,
              "uuid": "caa5012e-c5ce-f2c7-a02c-0f0e6e986c3a",
              "vendor": "Intel",
              "version": "4PC10362"
            }
          ],
          "fibreChannelPorts": [],
          "fileSystemUsage": {},
          "hardwareConfig": {
            "BIOS_REVISION": {
              "Passed": true,
              "actual": "1.1",
              "comparator": ">=",
              "expected": "1.0.0.0"
            },
            "BIOS_VENDOR": {
              "Passed": true,
              "actual": "SolidFire",
              "comparator": "==",
              "expected": "SolidFire"
            },
            "BIOS_VERSION": {
              "Passed": true,
              "actual": "1.1.2",
              "comparator": ">=",
              "expected": "1.1.2"
            },
            "CPU_CORES_00": {
              "Passed": true,
              "actual": "6",
              "comparator": "==",
              "expected": "6"
            },
            "CPU_CORES_01": {
              "Passed": true,
              "actual": "6",
              "comparator": "==",
              "expected": "6"
            },
            "CPU_CORES_ENABLED_00": {
              "Passed": true,
              "actual": "6",
              "comparator": "==",
              "expected": "6"
            },
            "CPU_CORES_ENABLED_01": {
              "Passed": true,
              "actual": "6",
              "comparator": "==",
              "expected": "6"
            },
            "CPU_MODEL_00": {
              "Passed": true,
              "actual": "Intel(R) Xeon(R) CPU E5-2640 0 @ 2.50GHz",
              "comparator": "==",
              "expected": "Intel(R) Xeon(R) CPU E5-2640 0 @ 2.50GHz"
            },
            "CPU_MODEL_01": {
              "Passed": true,
              "actual": "Intel(R) Xeon(R) CPU E5-2640 0 @ 2.50GHz",
              "comparator": "==",
              "expected": "Intel(R) Xeon(R) CPU E5-2640 0 @ 2.50GHz"
            },
            "CPU_THREADS_00": {
              "Passed": true,
              "actual": "12",
              "comparator": "==",
              "expected": "12"
            },
            "CPU_THREADS_01": {
              "Passed": true,
              "actual": "12",
              "comparator": "==",
              "expected": "12"
            },
            "CPU_THREADS_ENABLED": {
              "Passed": true,
              "actual": "24",
              "comparator": "==",
              "expected": "24"
            },
            "IDRAC_VERSION": {
              "Passed": true,
              "actual": "1.06.06",
              "comparator": ">=",
              "expected": "1.06.06"
            },
            "LIFECYCLE_VERSION": {
              "Passed": true,
              "actual": "1.0.0.5747",
              "comparator": ">=",
              "expected": "1.0.0.5747"
            },
            "MEMORY_GB": {
              "Passed": true,
              "actual": "72",
              "comparator": ">=",
              "expected": "72"
            },
            "MEMORY_MHZ_00": {
              "Passed": true,
              "actual": "1333",
              "comparator": ">=",
              "expected": "1333"
            },
            "MEMORY_MHZ_01": {
              "Passed": true,
              "actual": "1333",
              "comparator": ">=",
              "expected": "1333"
            },
            "MEMORY_MHZ_02": {
              "Passed": true,
              "actual": "1333",
              "comparator": ">=",
              "expected": "1333"
            },
            "MEMORY_MHZ_03": {
              "Passed": true,
              "actual": "1333",
              "comparator": ">=",
              "expected": "1333"
            },
            "MEMORY_MHZ_04": {
              "Passed": true,
              "actual": "1333",
              "comparator": ">=",
              "expected": "1333"
            },
            "MEMORY_MHZ_05": {
              "Passed": true,
              "actual": "1333",
              "comparator": ">=",
              "expected": "1333"
            },
            "MEMORY_MHZ_06": {
              "Passed": true,
              "actual": "1333",
              "comparator": ">=",
              "expected": "1333"
            },
            "MEMORY_MHZ_07": {
              "Passed": true,
              "actual": "1333",
              "comparator": ">=",
              "expected": "1333"
            },
            "MEMORY_MHZ_08": {
              "Passed": true,
              "actual": "1333",
              "comparator": ">=",
              "expected": "1333"
            },
            "MEMORY_MHZ_09": {
              "Passed": true,
              "actual": "1333",
              "comparator": ">=",
              "expected": "1333"
            },
            "MEMORY_MHZ_10": {
              "Passed": true,
              "actual": "1333",
              "comparator": ">=",
              "expected": "1333"
            },
            "MEMORY_MHZ_11": {
              "Passed": true,
              "actual": "1333",
              "comparator": ">=",
              "expected": "1333"
            },
            "MPTSAS_BIOS_VERSION": {
              "Passed": true,
              "actual": "07.25.00.00",
              "comparator": "==",
              "expected": "7.25.0.0"
            },
            "MPTSAS_FIRMWARE_VERSION": {
              "Passed": true,
              "actual": "13.00.57.00",
              "comparator": "==",
              "expected": "13.0.57.0"
            },
            "NETWORK_DRIVER_ETH0": {
              "Passed": true,
              "actual": "bnx2x",
              "comparator": "==",
              "expected": "bnx2x"
            },
            "NETWORK_DRIVER_ETH1": {
              "Passed": true,
              "actual": "bnx2x",
              "comparator": "==",
              "expected": "bnx2x"
            },
            "NETWORK_DRIVER_ETH2": {
              "Passed": true,
              "actual": "bnx2x",
              "comparator": "==",
              "expected": "bnx2x"
            },
            "NETWORK_DRIVER_ETH3": {
              "Passed": true,
              "actual": "bnx2x",
              "comparator": "==",
              "expected": "bnx2x"
            },
            "NETWORK_FIRMWARE_VERSION_ETH0": {
              "Passed": true,
              "actual": "7.10.18-solidfire-386560b9d0e3.",
              "comparator": "==",
              "expected": "7.10.18-solidfire-386560b9d0e3."
            },
            "NETWORK_FIRMWARE_VERSION_ETH1": {
              "Passed": true,
              "actual": "7.10.18-solidfire-386560b9d0e3.",
              "comparator": "==",
              "expected": "7.10.18-solidfire-386560b9d0e3."
            },
            "NETWORK_FIRMWARE_VERSION_ETH2": {
              "Passed": true,
              "actual": "7.10.18-solidfire-386560b9d0e3.",
              "comparator": "==",
              "expected": "7.10.18-solidfire-386560b9d0e3."
            },
            "NETWORK_FIRMWARE_VERSION_ETH3": {
              "Passed": true,
              "actual": "7.10.18-solidfire-386560b9d0e3.",
              "comparator": "==",
              "expected": "7.10.18-solidfire-386560b9d0e3."
            },
            "NUM_CPU": {
              "Passed": true,
              "actual": "2",
              "comparator": "==",
              "expected": "2"
            }
          },
          "kernelCrashDumpState": "EnabledByDefault",
          "memory": {
            "firmware_": {
              "capacity": "8323072",
              "date": "03/08/2012",
              "description": "BIOS",
              "physid": "0",
              "size": "65536",
              "vendor": "SolidFire",
              "version": "1.1.2"
            },
            "memory_DMI:1000": {
              "description": "System Memory",
              "physid": "1000",
              "size": "77309411328",
              "slot": "System board or motherboard"
            }
          },
          "network": {
            "network:0_": {
              "description": "Ethernet interface",
              "logicalname": "Bond1G",
              "physid": "1",
              "serial": "d4:ae:52:7a:bb:b1"
            },
            "network:0_PCI:0000:01:00.0": {
              "businfo": "pci@0000:01:00.0",
              "capacity": "1000000000",
              "clock": "33000000",
              "description": "Ethernet interface",
              "logicalname": "eth0",
              "physid": "0",
              "product": "NetXtreme II BCM57800 1/10 Gigabit Ethernet",
              "serial": "d4:ae:52:7a:bb:ad",
              "vendor": "Broadcom Corporation",
              "version": "10",
              "width": "64"
            },
            "network:1_": {
              "description": "Ethernet interface",
              "logicalname": "Bond10G",
              "physid": "2",
              "serial": "d4:ae:52:7a:bb:ad"
            },
            "network:1_PCI:0000:01:00.1": {
              "businfo": "pci@0000:01:00.1",
              "capacity": "1000000000",
              "clock": "33000000",
              "description": "Ethernet interface",
              "logicalname": "eth1",
              "physid": "0.1",
              "product": "NetXtreme II BCM57800 1/10 Gigabit Ethernet",
              "serial": "d4:ae:52:7a:bb:ad",
              "vendor": "Broadcom Corporation",
              "version": "10",
              "width": "64"
            },
            "network:2_PCI:0000:01:00.2": {
              "businfo": "pci@0000:01:00.2",
              "capacity": "1000000000",
              "clock": "33000000",
              "description": "Ethernet interface",
              "logicalname": "eth2",
              "physid": "0.2",
              "product": "NetXtreme II BCM57800 1/10 Gigabit Ethernet",
              "serial": "d4:ae:52:7a:bb:b1",
              "size": "1000000000",
              "vendor": "Broadcom Corporation",
              "version": "10",
              "width": "64"
            },
            "network:3_PCI:0000:01:00.3": {
              "businfo": "pci@0000:01:00.3",
              "capacity": "1000000000",
              "clock": "33000000",
              "description": "Ethernet interface",
              "logicalname": "eth3",
              "physid": "0.3",
              "product": "NetXtreme II BCM57800 1/10 Gigabit Ethernet",
              "serial": "d4:ae:52:7a:bb:b1",
              "size": "1000000000",
              "vendor": "Broadcom Corporation",
              "version": "10",
              "width": "64"
            }
          },
          "networkInterfaces": {
            "Bond10G": {
              "isConfigured": true,
              "isUp": true
            },
            "Bond1G": {
              "isConfigured": true,
              "isUp": true
            },
            "eth0": {
              "isConfigured": true,
              "isUp": true
            },
            "eth1": {
              "isConfigured": true,
              "isUp": true
            },
            "eth2": {
              "isConfigured": true,
              "isUp": true
            },
            "eth3": {
              "isConfigured": true,
              "isUp": true
            }
          },
          "nvram": {
            "errors": {
              "numOfErrorLogEntries": "0"
            },
            "extended": {
              "dialogVersion": "4",
              "event": [
                {
                  "name": "flushToFlash",
                  "time": "2016-07-28 17:43:56",
                  "value": "0"
                },
                {
                  "name": "flushToFlash",
                  "time": "2016-07-28 17:59:28",
                  "value": "0"
                },
                {
                  "name": "flushToFlash",
                  "time": "1948-07-10 14:45:43",
                  "value": "0"
                },
                {
                  "name": "flushToFlash",
                  "time": "2016-07-28 18:37:02",
                  "value": "0"
                },
                {
                  "name": "flushToFlash",
                  "time": "1948-07-10 15:23:17",
                  "value": "0"
                },
                {
                  "name": "flushToFlash",
                  "time": "2016-07-28 20:28:01",
                  "value": "0"
                },
                {
                  "name": "flushToFlash",
                  "time": "2016-08-10 20:11:31",
                  "value": "0"
                },
                {
                  "name": "flushToFlash",
                  "time": "2016-08-10 20:31:47",
                  "value": "0"
                },
                {
                  "name": "excessiveCurrent",
                  "time": "2014-07-31 21:12:08",
                  "value": "244"
                }
              ],
              "eventOccurrences": [
                {
                  "count": "143",
                  "name": "flushToFlash"
                },
                {
                  "count": "1",
                  "name": "excessiveCurrent"
                }
              ],
              "initialCapacitance": "7.126 F",
              "initialEsr": "0.097 Ohm",
              "measurement": [
                {
                  "level_0": " 0",
                  "level_1": " 387",
                  "level_2": " 4235656",
                  "level_3": " 156318",
                  "level_4": " 18423236",
                  "level_5": " 11903",
                  "level_6": " 0",
                  "level_7": " 0",
                  "level_8": " 0",
                  "level_9": " 0",
                  "name": "enterpriseFlashControllerTemperature",
                  "recent": "72 C"
                },
                {
                  "level_0": " 0",
                  "level_1": " 428",
                  "level_2": " 318053",
                  "level_3": " 4069249",
                  "level_4": " 17460727",
                  "level_5": " 973002",
                  "level_6": " 1977",
                  "level_7": " 3919",
                  "level_8": " 145",
                  "level_9": " 0",
                  "name": "capacitor1And2Temperature",
                  "recent": "36.71 C"
                },
                {
                  "level_0": " 0",
                  "level_1": " 582",
                  "level_2": " 4137227",
                  "level_3": " 15410653",
                  "level_4": " 3267522",
                  "level_5": " 6589",
                  "level_6": " 1051",
                  "level_7": " 3876",
                  "level_8": " 0",
                  "level_9": " 0",
                  "name": "capacitor3And4Temperature",
                  "recent": "33.17 C"
                },
                {
                  "errorPeriod": [
                    {
                      "duration": "18",
                      "startTime": "2015-08-05 21:08:44",
                      "worst": "8"
                    },
                    {
                      "duration": "60",
                      "startTime": "2015-08-05 21:09:08",
                      "worst": "8"
                    },
                    {
                      "duration": "1238",
                      "startTime": "2015-08-05 21:10:21",
                      "worst": "8"
                    },
                    {
                      "duration": "48",
                      "startTime": "2015-08-05 21:31:29",
                      "worst": "8"
                    }
                  ],
                  "level_0": " 0",
                  "level_1": " 517",
                  "level_2": " 23121",
                  "level_3": " 949227",
                  "level_4": " 3418492",
                  "level_5": " 111906",
                  "level_6": " 16026707",
                  "level_7": " 2297078",
                  "level_8": " 452",
                  "level_9": " 0",
                  "name": "rearVentAmbientTemperature",
                  "recent": "52.76 C"
                },
                {
                  "level_0": " 0",
                  "level_1": " 4260284",
                  "level_2": " 16816949",
                  "level_3": " 1750179",
                  "level_4": " 88",
                  "level_5": " 0",
                  "level_6": " 0",
                  "level_7": " 0",
                  "level_8": " 0",
                  "level_9": " 0",
                  "name": "rms200BoardTemperature",
                  "recent": "58.00 C"
                },
                {
                  "name": "voltageOfCapacitor1",
                  "recent": "2.254 V"
                },
                {
                  "name": "voltageOfCapacitor2",
                  "recent": "2.262 V"
                },
                {
                  "name": "voltageOfCapacitor3",
                  "recent": "2.225 V"
                },
                {
                  "name": "voltageOfCapacitor4",
                  "recent": "2.208 V"
                },
                {
                  "level_0": " 4650290",
                  "level_1": " 16740368",
                  "level_2": " 1048777",
                  "level_3": " 123763",
                  "level_4": " 93659",
                  "level_5": " 80709",
                  "level_6": " 62446",
                  "level_7": " 27488",
                  "level_8": " 0",
                  "level_9": " 0",
                  "name": "capacitorPackVoltage",
                  "recent": "8.949 V"
                },
                {
                  "level_0": " 0",
                  "level_1": " 0",
                  "level_2": " 0",
                  "level_3": " 19",
                  "level_4": " 38",
                  "level_5": " 18",
                  "level_6": " 0",
                  "level_7": " 0",
                  "level_8": " 2",
                  "level_9": " 66",
                  "name": "capacitorPackVoltageAtEndOfFlushToFlash",
                  "recent": "4.470 V"
                },
                {
                  "name": "currentDerivedFromV3V4",
                  "recent": "0.004 A"
                },
                {
                  "level_0": " 8",
                  "level_1": " 6",
                  "level_2": " 4",
                  "level_3": " 106",
                  "level_4": " 17",
                  "level_5": " 2",
                  "level_6": " 0",
                  "level_7": " 0",
                  "level_8": " 0",
                  "level_9": " 0",
                  "name": "derivedEnergy",
                  "recent": "190 Joules"
                },
                {
                  "level_0": " 0",
                  "level_1": " 0",
                  "level_2": " 0",
                  "level_3": " 0",
                  "level_4": " 0",
                  "level_5": " 0",
                  "level_6": " 0",
                  "level_7": " 0",
                  "level_8": " 18",
                  "level_9": " 230",
                  "name": "derivedCapacitanceOfThePack",
                  "recent": "7.322 F"
                },
                {
                  "level_0": " 0",
                  "level_1": " 248",
                  "level_2": " 0",
                  "level_3": " 0",
                  "level_4": " 0",
                  "level_5": " 0",
                  "level_6": " 0",
                  "level_7": " 0",
                  "level_8": " 0",
                  "level_9": " 0",
                  "name": "derivedEsrOfCapacitorPack",
                  "recent": "0.096 Ohm"
                },
                {
                  "level_0": " 0",
                  "level_1": " 0",
                  "level_2": " 0",
                  "level_3": " 0",
                  "level_4": " 124",
                  "level_5": " 19",
                  "level_6": " 0",
                  "level_7": " 0",
                  "level_8": " 0",
                  "level_9": " 0",
                  "name": "timeToRunFlushToFlash",
                  "recent": "22.39 Seconds"
                },
                {
                  "level_0": " 0",
                  "level_1": " 0",
                  "level_2": " 77",
                  "level_3": " 0",
                  "level_4": " 0",
                  "level_5": " 0",
                  "level_6": " 0",
                  "level_7": " 0",
                  "level_8": " 0",
                  "level_9": " 0",
                  "name": "timeToRunRestore",
                  "recent": "20.49 Seconds"
                },
                {
                  "level_0": " 0",
                  "level_1": " 54",
                  "level_2": " 17",
                  "level_3": " 6",
                  "level_4": " 0",
                  "level_5": " 0",
                  "level_6": " 0",
                  "level_7": " 0",
                  "level_8": " 0",
                  "level_9": " 1",
                  "name": "timeToChargeCapacitors",
                  "recent": "42 Seconds"
                },
                {
                  "level_0": " 4945370",
                  "level_1": " 22054",
                  "level_2": " 0",
                  "level_3": " 0",
                  "level_4": " 0",
                  "level_5": " 0",
                  "level_6": " 0",
                  "level_7": " 0",
                  "level_8": " 0",
                  "level_9": " 0",
                  "name": "correctableBitsInErrorOnReadingAPage"
                },
                {
                  "level_0": " 22054",
                  "level_1": " 0",
                  "level_2": " 0",
                  "level_3": " 0",
                  "level_4": " 0",
                  "level_5": " 0",
                  "level_6": " 0",
                  "level_7": " 0",
                  "level_8": " 0",
                  "level_9": " 0",
                  "name": "correctableBitsInErrorOnReadingTheWorstBchRegionOfAPage"
                },
                {
                  "errorPeriod": [
                    {
                      "duration": "9",
                      "startTime": "2015-11-26 16:29:51",
                      "worst": "8"
                    },
                    {
                      "duration": "6",
                      "startTime": "2015-11-26 16:30:06",
                      "worst": "8"
                    },
                    {
                      "duration": "15",
                      "startTime": "2015-11-26 16:30:36",
                      "worst": "8"
                    }
                  ],
                  "level_0": " 0",
                  "level_1": " 3924463",
                  "level_2": " 337357",
                  "level_3": " 5942",
                  "level_4": " 451546",
                  "level_5": " 17237788",
                  "level_6": " 865372",
                  "level_7": " 5022",
                  "level_8": " 10",
                  "level_9": " 0",
                  "name": "fanInletAmbientTemperature",
                  "recent": "46.55 C"
                }
              ],
              "smartCounters": [
                {
                  "name": "numberOf512ByteBlocksReadFromDdr",
                  "value": "141895819"
                },
                {
                  "name": "numberOf512ByteBlocksWrittenToDdr",
                  "value": "89867121104"
                },
                {
                  "name": "numberOfHostReadCommands",
                  "value": "9326735"
                },
                {
                  "name": "numberOfHostWriteCommands",
                  "value": "12090520050"
                },
                {
                  "name": "controllerBusyTimeMinutes",
                  "value": "37318"
                },
                {
                  "name": "numberOfPowerCycles",
                  "value": "133"
                },
                {
                  "name": "powerOnHours",
                  "value": "18611"
                },
                {
                  "name": "unsafeShutdowns",
                  "value": "56"
                },
                {
                  "name": "mediaErrors",
                  "value": "0"
                },
                {
                  "name": "numberOfErrorLogs",
                  "value": "13"
                }
              ],
              "snapshotTime": "2016-10-13 16:33:27"
            },
            "firmware": {
              "activeSlotNumber": "2",
              "slot1Version": "1e5817bc",
              "slot2Version": "5fb7565c",
              "slot3Version": "1e5817bc",
              "slot4Version": "1e5817bc"
            },
            "identify": {
              "firmwareVersion": "5fb7565c on slot 2",
              "hardwareRevision": "B04",
              "modelNumber": "RMS-200",
              "serialNumber": "0000866"
            },
            "smart": {
              "availableSpace": "0%",
              "availableSpaceThreshold": "0%",
              "controllerBusyTimeMinutes": "37318",
              "criticalErrorVector": "0x0",
              "mediaErrors": "0",
              "numberOf512ByteBlocksRead": "141895819",
              "numberOf512ByteBlocksWritten": "89867121104",
              "numberOfErrorInfoLogs": "13",
              "numberOfHostReadCommands": "9326735",
              "numberOfHostWriteCommands": "12090520050",
              "numberOfPowerCycles": "133",
              "powerOnHours": "18611",
              "temperature": "331 Kelvin",
              "unsafeShutdowns": "56"
            }
          },
          "origin": null,
          "platform": {
            "chassisType": "R620",
            "cpuModel": "Intel(R) Xeon(R) CPU E5-2640 0 @ 2.50GHz",
            "nodeMemoryGB": 72,
            "nodeType": "SF3010"
          },
          "serial": "4QSR3T1",
          "storage": {
            "storage_PCI:0000:00:1f.2": {
              "businfo": "pci@0000:00:1f.2",
              "clock": "66000000",
              "description": "SATA controller",
              "physid": "1f.2",
              "product": "C600/X79 series chipset 6-Port SATA AHCI Controller",
              "vendor": "Intel Corporation",
              "version": "05",
              "width": "32"
            },
            "storage_PCI:0000:04:00.0": {
              "businfo": "pci@0000:04:00.0",
              "clock": "33000000",
              "description": "Non-Volatile memory controller",
              "physid": "0",
              "version": "03",
              "width": "64"
            },
            "storage_PCI:0000:41:00.0": {
              "businfo": "pci@0000:41:00.0",
              "clock": "33000000",
              "description": "Serial Attached SCSI controller",
              "physid": "0",
              "product": "SAS2008 PCI-Express Fusion-MPT SAS-2 [Falcon]",
              "vendor": "LSI Logic / Symbios Logic",
              "version": "03",
              "width": "64"
            }
          },
          "system": {
            "bdr-en92_DMI:0100": {
              "description": "Rack Mount Chassis",
              "product": "SFx010 ()",
              "serial": "4QSR3T1",
              "vendor": "SolidFire",
              "width": "64"
            }
          },
          "systemMemory": {
            "free": 47104417792,
            "total": 75566792704,
            "used": 28462374912
          },
          "uuid": "4C4C4544-0051-5310-8052-B4C04F335431"
        }
      }
    }
  }
}"""

RESP_GetDriveConfig_v9_0 = """{
   "id":9,
   "result":{
      "driveConfig":{
         "drives":[
            {
               "canonicalName":"boot",
               "connected":false,
               "dev":0,
               "devPath":"/boot",
               "driveType":"System",
               "name":"boot",
               "path":"/boot",
               "pathLink":"/boot",
               "product":"Unknown",
               "scsiCompatId":"boot",
               "scsiState":"Unknown",
               "securityAtMaximum":false,
               "securityEnabled":false,
               "securityFrozen":false,
               "securityLocked":false,
               "securitySupported":false,
               "serial":"boot",
               "size":1024,
               "slot":-2,
               "uuid":"881cc415-7ed6-41a3-65a8-6452f27ed745",
               "vendor":"Unknown",
               "version":"Unknown"
            },
            {
               "canonicalName":"/",
               "connected":false,
               "dev":0,
               "devPath":"/",
               "driveType":"System",
               "name":"/",
               "path":"/",
               "pathLink":"/",
               "product":"Unknown",
               "scsiCompatId":"/",
               "scsiState":"Unknown",
               "securityAtMaximum":false,
               "securityEnabled":false,
               "securityFrozen":false,
               "securityLocked":false,
               "securitySupported":false,
               "serial":"/",
               "size":9223372036854775807,
               "slot":-2,
               "uuid":"6666cd76-f969-5646-9e7b-e39d750cc7d9",
               "vendor":"Unknown",
               "version":"Unknown"
            },
            {
               "canonicalName":"log",
               "connected":false,
               "dev":0,
               "devPath":"/var/log",
               "driveType":"System",
               "name":"log",
               "path":"/var/log",
               "pathLink":"/var/log",
               "product":"Unknown",
               "scsiCompatId":"log",
               "scsiState":"Unknown",
               "securityAtMaximum":false,
               "securityEnabled":false,
               "securityFrozen":false,
               "securityLocked":false,
               "securitySupported":false,
               "serial":"log",
               "size":9223372036854775807,
               "slot":-2,
               "uuid":"dc1d71bb-b5c4-d2a5-e936-db79ef10c19f",
               "vendor":"Unknown",
               "version":"Unknown"
            },
            {
               "canonicalName":"pendingDirtyBlocks",
               "connected":false,
               "dev":0,
               "devPath":"/mnt/pendingDirtyBlocks",
               "driveType":"System",
               "name":"pendingDirtyBlocks",
               "path":"/mnt/pendingDirtyBlocks",
               "pathLink":"/mnt/pendingDirtyBlocks",
               "product":"Unknown",
               "scsiCompatId":"pendingDirtyBlocks",
               "scsiState":"Unknown",
               "securityAtMaximum":false,
               "securityEnabled":false,
               "securityFrozen":false,
               "securityLocked":false,
               "securitySupported":false,
               "serial":"pendingDirtyBlocks",
               "size":9223372036854775807,
               "slot":-2,
               "uuid":"00abd0dc-ff28-2825-7faa-38e9a49d66a4",
               "vendor":"Unknown",
               "version":"Unknown"
            },
            {
               "canonicalName":"sda",
               "connected":true,
               "dev":2054,
               "devPath":"/dev/slot0p6",
               "driveType":"Slice",
               "name":"scsi-36000c29551932b43ba5bb11c3cd54c1e-part6",
               "path":"/dev/sda6",
               "pathLink":"/dev/slot0p6",
               "product":"Unknown",
               "scsiCompatId":"scsi-36000c29551932b43ba5bb11c3cd54c1e-part6",
               "scsiState":"Running",
               "securityAtMaximum":false,
               "securityEnabled":false,
               "securityFrozen":false,
               "securityLocked":false,
               "securitySupported":false,
               "serial":"scsi-36000c29551932b43ba5bb11c3cd54c1e-part6",
               "size":216787845120,
               "slot":0,
               "uuid":"38b3c943-9e45-88e9-1ebe-130b4186d8da",
               "vendor":"Unknown",
               "version":"Unknown"
            },
            {
               "canonicalName":"sdb",
               "connected":true,
               "dev":2064,
               "devPath":"/dev/slot1",
               "driveType":"Block",
               "name":"scsi-36000c29b0d225d4342d5750a81af4ea6",
               "path":"/dev/sdb",
               "pathLink":"/dev/slot1",
               "product":"Unknown",
               "scsiCompatId":"scsi-36000c29b0d225d4342d5750a81af4ea6",
               "scsiState":"Running",
               "securityAtMaximum":false,
               "securityEnabled":false,
               "securityFrozen":false,
               "securityLocked":false,
               "securitySupported":false,
               "serial":"scsi-36000c29b0d225d4342d5750a81af4ea6",
               "size":268435456000,
               "slot":1,
               "uuid":"a6944a6f-46f4-addb-ba1e-4c237b5fedc5",
               "vendor":"Unknown",
               "version":"Unknown"
            },
            {
               "canonicalName":"",
               "connected":false,
               "dev":0,
               "devPath":"/dev/slot2",
               "driveType":"Block",
               "name":"slot2",
               "path":"/dev/slot2",
               "pathLink":"/dev/slot2",
               "product":"Unknown",
               "scsiCompatId":"slot2",
               "scsiState":"Unknown",
               "securityAtMaximum":false,
               "securityEnabled":false,
               "securityFrozen":false,
               "securityLocked":false,
               "securitySupported":false,
               "serial":"slot2",
               "size":0,
               "slot":2,
               "uuid":"d92f909d-c606-4c27-d17a-4cb6db95a35c",
               "vendor":"Unknown",
               "version":"Unknown"
            },
            {
               "canonicalName":"",
               "connected":false,
               "dev":0,
               "devPath":"/dev/slot3",
               "driveType":"Block",
               "name":"slot3",
               "path":"/dev/slot3",
               "pathLink":"/dev/slot3",
               "product":"Unknown",
               "scsiCompatId":"slot3",
               "scsiState":"Unknown",
               "securityAtMaximum":false,
               "securityEnabled":false,
               "securityFrozen":false,
               "securityLocked":false,
               "securitySupported":false,
               "serial":"slot3",
               "size":0,
               "slot":3,
               "uuid":"25b903d1-3b55-d53f-a556-47b28f91b728",
               "vendor":"Unknown",
               "version":"Unknown"
            },
            {
               "canonicalName":"",
               "connected":false,
               "dev":0,
               "devPath":"/dev/slot4",
               "driveType":"Block",
               "name":"slot4",
               "path":"/dev/slot4",
               "pathLink":"/dev/slot4",
               "product":"Unknown",
               "scsiCompatId":"slot4",
               "scsiState":"Unknown",
               "securityAtMaximum":false,
               "securityEnabled":false,
               "securityFrozen":false,
               "securityLocked":false,
               "securitySupported":false,
               "serial":"slot4",
               "size":0,
               "slot":4,
               "uuid":"76e3d13f-88c5-c334-8f0b-8486964d369e",
               "vendor":"Unknown",
               "version":"Unknown"
            },
            {
               "canonicalName":"",
               "connected":false,
               "dev":0,
               "devPath":"/dev/slot5",
               "driveType":"Block",
               "name":"slot5",
               "path":"/dev/slot5",
               "pathLink":"/dev/slot5",
               "product":"Unknown",
               "scsiCompatId":"slot5",
               "scsiState":"Unknown",
               "securityAtMaximum":false,
               "securityEnabled":false,
               "securityFrozen":false,
               "securityLocked":false,
               "securitySupported":false,
               "serial":"slot5",
               "size":0,
               "slot":5,
               "uuid":"b31123fa-9a17-0ccd-deab-deac32a58371",
               "vendor":"Unknown",
               "version":"Unknown"
            },
            {
               "canonicalName":"",
               "connected":false,
               "dev":0,
               "devPath":"/dev/slot6",
               "driveType":"Block",
               "name":"slot6",
               "path":"/dev/slot6",
               "pathLink":"/dev/slot6",
               "product":"Unknown",
               "scsiCompatId":"slot6",
               "scsiState":"Unknown",
               "securityAtMaximum":false,
               "securityEnabled":false,
               "securityFrozen":false,
               "securityLocked":false,
               "securitySupported":false,
               "serial":"slot6",
               "size":0,
               "slot":6,
               "uuid":"c1b04a69-49a0-fdee-b818-c6cdfafd6cd5",
               "vendor":"Unknown",
               "version":"Unknown"
            },
            {
               "canonicalName":"",
               "connected":false,
               "dev":0,
               "devPath":"/dev/slot7",
               "driveType":"Block",
               "name":"slot7",
               "path":"/dev/slot7",
               "pathLink":"/dev/slot7",
               "product":"Unknown",
               "scsiCompatId":"slot7",
               "scsiState":"Unknown",
               "securityAtMaximum":false,
               "securityEnabled":false,
               "securityFrozen":false,
               "securityLocked":false,
               "securitySupported":false,
               "serial":"slot7",
               "size":0,
               "slot":7,
               "uuid":"76c29a96-68a6-2d8e-6416-392f9fd07919",
               "vendor":"Unknown",
               "version":"Unknown"
            },
            {
               "canonicalName":"",
               "connected":false,
               "dev":0,
               "devPath":"/dev/slot8",
               "driveType":"Block",
               "name":"slot8",
               "path":"/dev/slot8",
               "pathLink":"/dev/slot8",
               "product":"Unknown",
               "scsiCompatId":"slot8",
               "scsiState":"Unknown",
               "securityAtMaximum":false,
               "securityEnabled":false,
               "securityFrozen":false,
               "securityLocked":false,
               "securitySupported":false,
               "serial":"slot8",
               "size":0,
               "slot":8,
               "uuid":"28384068-fdee-1dae-21e3-493558121657",
               "vendor":"Unknown",
               "version":"Unknown"
            },
            {
               "canonicalName":"",
               "connected":false,
               "dev":0,
               "devPath":"/dev/slot9",
               "driveType":"Block",
               "name":"slot9",
               "path":"/dev/slot9",
               "pathLink":"/dev/slot9",
               "product":"Unknown",
               "scsiCompatId":"slot9",
               "scsiState":"Unknown",
               "securityAtMaximum":false,
               "securityEnabled":false,
               "securityFrozen":false,
               "securityLocked":false,
               "securitySupported":false,
               "serial":"slot9",
               "size":0,
               "slot":9,
               "uuid":"612e2106-7032-850a-a16d-4980b53ffb23",
               "vendor":"Unknown",
               "version":"Unknown"
            },
            {
               "canonicalName":"",
               "connected":false,
               "dev":0,
               "devPath":"/dev/slot10",
               "driveType":"Block",
               "name":"slot10",
               "path":"/dev/slot10",
               "pathLink":"/dev/slot10",
               "product":"Unknown",
               "scsiCompatId":"slot10",
               "scsiState":"Unknown",
               "securityAtMaximum":false,
               "securityEnabled":false,
               "securityFrozen":false,
               "securityLocked":false,
               "securitySupported":false,
               "serial":"slot10",
               "size":0,
               "slot":10,
               "uuid":"9d62ad9e-a097-d5d6-d4f7-1d27193270a1",
               "vendor":"Unknown",
               "version":"Unknown"
            }
         ],
         "numBlockActual":1,
         "numBlockExpected":10,
         "numSliceActual":1,
         "numSliceExpected":1,
         "numTotalActual":2,
         "numTotalExpected":11
      }
   }
}"""

RESP_GetDriveConfig_v9_1 = """{  
   "id":129,
   "result":{  
      "driveConfig":{  
         "drives":[  
            {  
               "canonicalName":"boot",
               "connected":false,
               "dev":0,
               "devPath":"/boot",
               "driveType":"System",
               "name":"boot",
               "path":"/boot",
               "pathLink":"/boot",
               "product":"Unknown",
               "scsiCompatId":"boot",
               "scsiState":"Unknown",
               "securityAtMaximum":false,
               "securityEnabled":false,
               "securityFrozen":false,
               "securityLocked":false,
               "securitySupported":false,
               "serial":"boot",
               "size":1024,
               "slot":-2,
               "uuid":"881cc415-7ed6-41a3-65a8-6452f27ed745",
               "vendor":"Unknown",
               "version":"Unknown"
            },
            {  
               "canonicalName":"/",
               "connected":false,
               "dev":0,
               "devPath":"/",
               "driveType":"System",
               "name":"/",
               "path":"/",
               "pathLink":"/",
               "product":"Unknown",
               "scsiCompatId":"/",
               "scsiState":"Unknown",
               "securityAtMaximum":false,
               "securityEnabled":false,
               "securityFrozen":false,
               "securityLocked":false,
               "securitySupported":false,
               "serial":"/",
               "size":9223372036854775807,
               "slot":-2,
               "uuid":"6666cd76-f969-5646-9e7b-e39d750cc7d9",
               "vendor":"Unknown",
               "version":"Unknown"
            },
            {  
               "canonicalName":"log",
               "connected":false,
               "dev":0,
               "devPath":"/var/log",
               "driveType":"System",
               "name":"log",
               "path":"/var/log",
               "pathLink":"/var/log",
               "product":"Unknown",
               "scsiCompatId":"log",
               "scsiState":"Unknown",
               "securityAtMaximum":false,
               "securityEnabled":false,
               "securityFrozen":false,
               "securityLocked":false,
               "securitySupported":false,
               "serial":"log",
               "size":9223372036854775807,
               "slot":-2,
               "uuid":"dc1d71bb-b5c4-d2a5-e936-db79ef10c19f",
               "vendor":"Unknown",
               "version":"Unknown"
            },
            {  
               "canonicalName":"pendingDirtyBlocks",
               "connected":false,
               "dev":0,
               "devPath":"/mnt/pendingDirtyBlocks",
               "driveType":"System",
               "name":"pendingDirtyBlocks",
               "path":"/mnt/pendingDirtyBlocks",
               "pathLink":"/mnt/pendingDirtyBlocks",
               "product":"Unknown",
               "scsiCompatId":"pendingDirtyBlocks",
               "scsiState":"Unknown",
               "securityAtMaximum":false,
               "securityEnabled":false,
               "securityFrozen":false,
               "securityLocked":false,
               "securitySupported":false,
               "serial":"pendingDirtyBlocks",
               "size":9223372036854775807,
               "slot":-2,
               "uuid":"00abd0dc-ff28-2825-7faa-38e9a49d66a4",
               "vendor":"Unknown",
               "version":"Unknown"
            },
            {  
               "canonicalName":"sda",
               "connected":true,
               "dev":2054,
               "devPath":"/dev/slot0p6",
               "driveType":"Slice",
               "name":"scsi-36000c29551932b43ba5bb11c3cd54c1e-part6",
               "path":"/dev/sda6",
               "pathLink":"/dev/slot0p6",
               "product":"Unknown",
               "scsiCompatId":"scsi-36000c29551932b43ba5bb11c3cd54c1e-part6",
               "scsiState":"Running",
               "securityAtMaximum":false,
               "securityEnabled":false,
               "securityFrozen":false,
               "securityLocked":false,
               "securitySupported":false,
               "serial":"scsi-36000c29551932b43ba5bb11c3cd54c1e-part6",
               "size":216787845120,
               "slot":0,
               "uuid":"38b3c943-9e45-88e9-1ebe-130b4186d8da",
               "vendor":"Unknown",
               "version":"Unknown"
            },
            {  
               "canonicalName":"sdb",
               "connected":true,
               "dev":2064,
               "devPath":"/dev/slot1",
               "driveType":"Block",
               "name":"scsi-36000c29b0d225d4342d5750a81af4ea6",
               "path":"/dev/sdb",
               "pathLink":"/dev/slot1",
               "product":"Unknown",
               "scsiCompatId":"scsi-36000c29b0d225d4342d5750a81af4ea6",
               "scsiState":"Running",
               "securityAtMaximum":false,
               "securityEnabled":false,
               "securityFrozen":false,
               "securityLocked":false,
               "securitySupported":false,
               "serial":"scsi-36000c29b0d225d4342d5750a81af4ea6",
               "size":268435456000,
               "slot":1,
               "uuid":"a6944a6f-46f4-addb-ba1e-4c237b5fedc5",
               "vendor":"Unknown",
               "version":"Unknown"
            },
            {  
               "canonicalName":"",
               "connected":false,
               "dev":0,
               "devPath":"/dev/slot2",
               "driveType":"Block",
               "name":"slot2",
               "path":"/dev/slot2",
               "pathLink":"/dev/slot2",
               "product":"Unknown",
               "scsiCompatId":"slot2",
               "scsiState":"Unknown",
               "securityAtMaximum":false,
               "securityEnabled":false,
               "securityFrozen":false,
               "securityLocked":false,
               "securitySupported":false,
               "serial":"slot2",
               "size":0,
               "slot":2,
               "uuid":"d92f909d-c606-4c27-d17a-4cb6db95a35c",
               "vendor":"Unknown",
               "version":"Unknown"
            },
            {  
               "canonicalName":"",
               "connected":false,
               "dev":0,
               "devPath":"/dev/slot3",
               "driveType":"Block",
               "name":"slot3",
               "path":"/dev/slot3",
               "pathLink":"/dev/slot3",
               "product":"Unknown",
               "scsiCompatId":"slot3",
               "scsiState":"Unknown",
               "securityAtMaximum":false,
               "securityEnabled":false,
               "securityFrozen":false,
               "securityLocked":false,
               "securitySupported":false,
               "serial":"slot3",
               "size":0,
               "slot":3,
               "uuid":"25b903d1-3b55-d53f-a556-47b28f91b728",
               "vendor":"Unknown",
               "version":"Unknown"
            },
            {  
               "canonicalName":"",
               "connected":false,
               "dev":0,
               "devPath":"/dev/slot4",
               "driveType":"Block",
               "name":"slot4",
               "path":"/dev/slot4",
               "pathLink":"/dev/slot4",
               "product":"Unknown",
               "scsiCompatId":"slot4",
               "scsiState":"Unknown",
               "securityAtMaximum":false,
               "securityEnabled":false,
               "securityFrozen":false,
               "securityLocked":false,
               "securitySupported":false,
               "serial":"slot4",
               "size":0,
               "slot":4,
               "uuid":"76e3d13f-88c5-c334-8f0b-8486964d369e",
               "vendor":"Unknown",
               "version":"Unknown"
            },
            {  
               "canonicalName":"",
               "connected":false,
               "dev":0,
               "devPath":"/dev/slot5",
               "driveType":"Block",
               "name":"slot5",
               "path":"/dev/slot5",
               "pathLink":"/dev/slot5",
               "product":"Unknown",
               "scsiCompatId":"slot5",
               "scsiState":"Unknown",
               "securityAtMaximum":false,
               "securityEnabled":false,
               "securityFrozen":false,
               "securityLocked":false,
               "securitySupported":false,
               "serial":"slot5",
               "size":0,
               "slot":5,
               "uuid":"b31123fa-9a17-0ccd-deab-deac32a58371",
               "vendor":"Unknown",
               "version":"Unknown"
            },
            {  
               "canonicalName":"",
               "connected":false,
               "dev":0,
               "devPath":"/dev/slot6",
               "driveType":"Block",
               "name":"slot6",
               "path":"/dev/slot6",
               "pathLink":"/dev/slot6",
               "product":"Unknown",
               "scsiCompatId":"slot6",
               "scsiState":"Unknown",
               "securityAtMaximum":false,
               "securityEnabled":false,
               "securityFrozen":false,
               "securityLocked":false,
               "securitySupported":false,
               "serial":"slot6",
               "size":0,
               "slot":6,
               "uuid":"c1b04a69-49a0-fdee-b818-c6cdfafd6cd5",
               "vendor":"Unknown",
               "version":"Unknown"
            },
            {  
               "canonicalName":"",
               "connected":false,
               "dev":0,
               "devPath":"/dev/slot7",
               "driveType":"Block",
               "name":"slot7",
               "path":"/dev/slot7",
               "pathLink":"/dev/slot7",
               "product":"Unknown",
               "scsiCompatId":"slot7",
               "scsiState":"Unknown",
               "securityAtMaximum":false,
               "securityEnabled":false,
               "securityFrozen":false,
               "securityLocked":false,
               "securitySupported":false,
               "serial":"slot7",
               "size":0,
               "slot":7,
               "uuid":"76c29a96-68a6-2d8e-6416-392f9fd07919",
               "vendor":"Unknown",
               "version":"Unknown"
            },
            {  
               "canonicalName":"",
               "connected":false,
               "dev":0,
               "devPath":"/dev/slot8",
               "driveType":"Block",
               "name":"slot8",
               "path":"/dev/slot8",
               "pathLink":"/dev/slot8",
               "product":"Unknown",
               "scsiCompatId":"slot8",
               "scsiState":"Unknown",
               "securityAtMaximum":false,
               "securityEnabled":false,
               "securityFrozen":false,
               "securityLocked":false,
               "securitySupported":false,
               "serial":"slot8",
               "size":0,
               "slot":8,
               "uuid":"28384068-fdee-1dae-21e3-493558121657",
               "vendor":"Unknown",
               "version":"Unknown"
            },
            {  
               "canonicalName":"",
               "connected":false,
               "dev":0,
               "devPath":"/dev/slot9",
               "driveType":"Block",
               "name":"slot9",
               "path":"/dev/slot9",
               "pathLink":"/dev/slot9",
               "product":"Unknown",
               "scsiCompatId":"slot9",
               "scsiState":"Unknown",
               "securityAtMaximum":false,
               "securityEnabled":false,
               "securityFrozen":false,
               "securityLocked":false,
               "securitySupported":false,
               "serial":"slot9",
               "size":0,
               "slot":9,
               "uuid":"612e2106-7032-850a-a16d-4980b53ffb23",
               "vendor":"Unknown",
               "version":"Unknown"
            },
            {  
               "canonicalName":"",
               "connected":false,
               "dev":0,
               "devPath":"/dev/slot10",
               "driveType":"Block",
               "name":"slot10",
               "path":"/dev/slot10",
               "pathLink":"/dev/slot10",
               "product":"Unknown",
               "scsiCompatId":"slot10",
               "scsiState":"Unknown",
               "securityAtMaximum":false,
               "securityEnabled":false,
               "securityFrozen":false,
               "securityLocked":false,
               "securitySupported":false,
               "serial":"slot10",
               "size":0,
               "slot":10,
               "uuid":"9d62ad9e-a097-d5d6-d4f7-1d27193270a1",
               "vendor":"Unknown",
               "version":"Unknown"
            }
         ],
         "numBlockActual":1,
         "numBlockExpected":10,
         "numSliceActual":1,
         "numSliceExpected":1,
         "numTotalActual":2,
         "numTotalExpected":11
      }
   }
}"""

RESP_GetDriveConfig_v9_2 = """{
   "id":129,
   "result":{
      "driveConfig":{
         "drives":[
            {
               "canonicalName":"boot",
               "connected":false,
               "dev":0,
               "devPath":"/boot",
               "driveType":"System",
               "name":"boot",
               "path":"/boot",
               "pathLink":"/boot",
               "product":"Unknown",
               "scsiCompatId":"boot",
               "scsiState":"Unknown",
               "securityAtMaximum":false,
               "securityEnabled":false,
               "securityFrozen":false,
               "securityLocked":false,
               "securitySupported":false,
               "serial":"boot",
               "size":1024,
               "slot":-2,
               "uuid":"881cc415-7ed6-41a3-65a8-6452f27ed745",
               "vendor":"Unknown",
               "version":"Unknown"
            },
            {
               "canonicalName":"/",
               "connected":false,
               "dev":0,
               "devPath":"/",
               "driveType":"System",
               "name":"/",
               "path":"/",
               "pathLink":"/",
               "product":"Unknown",
               "scsiCompatId":"/",
               "scsiState":"Unknown",
               "securityAtMaximum":false,
               "securityEnabled":false,
               "securityFrozen":false,
               "securityLocked":false,
               "securitySupported":false,
               "serial":"/",
               "size":9223372036854775807,
               "slot":-2,
               "uuid":"6666cd76-f969-5646-9e7b-e39d750cc7d9",
               "vendor":"Unknown",
               "version":"Unknown"
            },
            {
               "canonicalName":"log",
               "connected":false,
               "dev":0,
               "devPath":"/var/log",
               "driveType":"System",
               "name":"log",
               "path":"/var/log",
               "pathLink":"/var/log",
               "product":"Unknown",
               "scsiCompatId":"log",
               "scsiState":"Unknown",
               "securityAtMaximum":false,
               "securityEnabled":false,
               "securityFrozen":false,
               "securityLocked":false,
               "securitySupported":false,
               "serial":"log",
               "size":9223372036854775807,
               "slot":-2,
               "uuid":"dc1d71bb-b5c4-d2a5-e936-db79ef10c19f",
               "vendor":"Unknown",
               "version":"Unknown"
            },
            {
               "canonicalName":"pendingDirtyBlocks",
               "connected":false,
               "dev":0,
               "devPath":"/mnt/pendingDirtyBlocks",
               "driveType":"System",
               "name":"pendingDirtyBlocks",
               "path":"/mnt/pendingDirtyBlocks",
               "pathLink":"/mnt/pendingDirtyBlocks",
               "product":"Unknown",
               "scsiCompatId":"pendingDirtyBlocks",
               "scsiState":"Unknown",
               "securityAtMaximum":false,
               "securityEnabled":false,
               "securityFrozen":false,
               "securityLocked":false,
               "securitySupported":false,
               "serial":"pendingDirtyBlocks",
               "size":9223372036854775807,
               "slot":-2,
               "uuid":"00abd0dc-ff28-2825-7faa-38e9a49d66a4",
               "vendor":"Unknown",
               "version":"Unknown"
            },
            {
               "canonicalName":"sda",
               "connected":true,
               "dev":2054,
               "devPath":"/dev/slot0p6",
               "driveType":"Slice",
               "name":"scsi-36000c29551932b43ba5bb11c3cd54c1e-part6",
               "path":"/dev/sda6",
               "pathLink":"/dev/slot0p6",
               "product":"Unknown",
               "scsiCompatId":"scsi-36000c29551932b43ba5bb11c3cd54c1e-part6",
               "scsiState":"Running",
               "securityAtMaximum":false,
               "securityEnabled":false,
               "securityFrozen":false,
               "securityLocked":false,
               "securitySupported":false,
               "serial":"scsi-36000c29551932b43ba5bb11c3cd54c1e-part6",
               "size":216787845120,
               "slot":0,
               "uuid":"38b3c943-9e45-88e9-1ebe-130b4186d8da",
               "vendor":"Unknown",
               "version":"Unknown"
            },
            {
               "canonicalName":"sdb",
               "connected":true,
               "dev":2064,
               "devPath":"/dev/slot1",
               "driveType":"Block",
               "name":"scsi-36000c29b0d225d4342d5750a81af4ea6",
               "path":"/dev/sdb",
               "pathLink":"/dev/slot1",
               "product":"Unknown",
               "scsiCompatId":"scsi-36000c29b0d225d4342d5750a81af4ea6",
               "scsiState":"Running",
               "securityAtMaximum":false,
               "securityEnabled":false,
               "securityFrozen":false,
               "securityLocked":false,
               "securitySupported":false,
               "serial":"scsi-36000c29b0d225d4342d5750a81af4ea6",
               "size":268435456000,
               "slot":1,
               "uuid":"a6944a6f-46f4-addb-ba1e-4c237b5fedc5",
               "vendor":"Unknown",
               "version":"Unknown"
            },
            {
               "canonicalName":"",
               "connected":false,
               "dev":0,
               "devPath":"/dev/slot2",
               "driveType":"Block",
               "name":"slot2",
               "path":"/dev/slot2",
               "pathLink":"/dev/slot2",
               "product":"Unknown",
               "scsiCompatId":"slot2",
               "scsiState":"Unknown",
               "securityAtMaximum":false,
               "securityEnabled":false,
               "securityFrozen":false,
               "securityLocked":false,
               "securitySupported":false,
               "serial":"slot2",
               "size":0,
               "slot":2,
               "uuid":"d92f909d-c606-4c27-d17a-4cb6db95a35c",
               "vendor":"Unknown",
               "version":"Unknown"
            },
            {
               "canonicalName":"",
               "connected":false,
               "dev":0,
               "devPath":"/dev/slot3",
               "driveType":"Block",
               "name":"slot3",
               "path":"/dev/slot3",
               "pathLink":"/dev/slot3",
               "product":"Unknown",
               "scsiCompatId":"slot3",
               "scsiState":"Unknown",
               "securityAtMaximum":false,
               "securityEnabled":false,
               "securityFrozen":false,
               "securityLocked":false,
               "securitySupported":false,
               "serial":"slot3",
               "size":0,
               "slot":3,
               "uuid":"25b903d1-3b55-d53f-a556-47b28f91b728",
               "vendor":"Unknown",
               "version":"Unknown"
            },
            {
               "canonicalName":"",
               "connected":false,
               "dev":0,
               "devPath":"/dev/slot4",
               "driveType":"Block",
               "name":"slot4",
               "path":"/dev/slot4",
               "pathLink":"/dev/slot4",
               "product":"Unknown",
               "scsiCompatId":"slot4",
               "scsiState":"Unknown",
               "securityAtMaximum":false,
               "securityEnabled":false,
               "securityFrozen":false,
               "securityLocked":false,
               "securitySupported":false,
               "serial":"slot4",
               "size":0,
               "slot":4,
               "uuid":"76e3d13f-88c5-c334-8f0b-8486964d369e",
               "vendor":"Unknown",
               "version":"Unknown"
            },
            {
               "canonicalName":"",
               "connected":false,
               "dev":0,
               "devPath":"/dev/slot5",
               "driveType":"Block",
               "name":"slot5",
               "path":"/dev/slot5",
               "pathLink":"/dev/slot5",
               "product":"Unknown",
               "scsiCompatId":"slot5",
               "scsiState":"Unknown",
               "securityAtMaximum":false,
               "securityEnabled":false,
               "securityFrozen":false,
               "securityLocked":false,
               "securitySupported":false,
               "serial":"slot5",
               "size":0,
               "slot":5,
               "uuid":"b31123fa-9a17-0ccd-deab-deac32a58371",
               "vendor":"Unknown",
               "version":"Unknown"
            },
            {
               "canonicalName":"",
               "connected":false,
               "dev":0,
               "devPath":"/dev/slot6",
               "driveType":"Block",
               "name":"slot6",
               "path":"/dev/slot6",
               "pathLink":"/dev/slot6",
               "product":"Unknown",
               "scsiCompatId":"slot6",
               "scsiState":"Unknown",
               "securityAtMaximum":false,
               "securityEnabled":false,
               "securityFrozen":false,
               "securityLocked":false,
               "securitySupported":false,
               "serial":"slot6",
               "size":0,
               "slot":6,
               "uuid":"c1b04a69-49a0-fdee-b818-c6cdfafd6cd5",
               "vendor":"Unknown",
               "version":"Unknown"
            },
            {
               "canonicalName":"",
               "connected":false,
               "dev":0,
               "devPath":"/dev/slot7",
               "driveType":"Block",
               "name":"slot7",
               "path":"/dev/slot7",
               "pathLink":"/dev/slot7",
               "product":"Unknown",
               "scsiCompatId":"slot7",
               "scsiState":"Unknown",
               "securityAtMaximum":false,
               "securityEnabled":false,
               "securityFrozen":false,
               "securityLocked":false,
               "securitySupported":false,
               "serial":"slot7",
               "size":0,
               "slot":7,
               "uuid":"76c29a96-68a6-2d8e-6416-392f9fd07919",
               "vendor":"Unknown",
               "version":"Unknown"
            },
            {
               "canonicalName":"",
               "connected":false,
               "dev":0,
               "devPath":"/dev/slot8",
               "driveType":"Block",
               "name":"slot8",
               "path":"/dev/slot8",
               "pathLink":"/dev/slot8",
               "product":"Unknown",
               "scsiCompatId":"slot8",
               "scsiState":"Unknown",
               "securityAtMaximum":false,
               "securityEnabled":false,
               "securityFrozen":false,
               "securityLocked":false,
               "securitySupported":false,
               "serial":"slot8",
               "size":0,
               "slot":8,
               "uuid":"28384068-fdee-1dae-21e3-493558121657",
               "vendor":"Unknown",
               "version":"Unknown"
            },
            {
               "canonicalName":"",
               "connected":false,
               "dev":0,
               "devPath":"/dev/slot9",
               "driveType":"Block",
               "name":"slot9",
               "path":"/dev/slot9",
               "pathLink":"/dev/slot9",
               "product":"Unknown",
               "scsiCompatId":"slot9",
               "scsiState":"Unknown",
               "securityAtMaximum":false,
               "securityEnabled":false,
               "securityFrozen":false,
               "securityLocked":false,
               "securitySupported":false,
               "serial":"slot9",
               "size":0,
               "slot":9,
               "uuid":"612e2106-7032-850a-a16d-4980b53ffb23",
               "vendor":"Unknown",
               "version":"Unknown"
            },
            {
               "canonicalName":"",
               "connected":false,
               "dev":0,
               "devPath":"/dev/slot10",
               "driveType":"Block",
               "name":"slot10",
               "path":"/dev/slot10",
               "pathLink":"/dev/slot10",
               "product":"Unknown",
               "scsiCompatId":"slot10",
               "scsiState":"Unknown",
               "securityAtMaximum":false,
               "securityEnabled":false,
               "securityFrozen":false,
               "securityLocked":false,
               "securitySupported":false,
               "serial":"slot10",
               "size":0,
               "slot":10,
               "uuid":"9d62ad9e-a097-d5d6-d4f7-1d27193270a1",
               "vendor":"Unknown",
               "version":"Unknown"
            }
         ],
         "numBlockActual":1,
         "numBlockExpected":10,
         "numSliceActual":1,
         "numSliceExpected":1,
         "numTotalActual":2,
         "numTotalExpected":11
      }
   }
}"""

RESP_GetFeatureStatus_v9_0 = """{
  "id": null,
  "result": {
    "features": [
      {
        "enabled": true,
        "feature": "Vvols"
      }
    ]
  }
}"""

RESP_GetHardwareConfig_v9_0 = """{
  "id": null,
  "result": {
    "hardwareConfig": {
      "biosRevision": "1.0",
      "biosVendor": "SolidFire",
      "biosVersion": "1.1.2",
      "blockDriveSizeBytes": 300069052416,
      "blockDrives": [
        "/dev/slot0",
        "/dev/slot1",
        "/dev/slot2",
        "/dev/slot3",
        "/dev/slot4",
        "/dev/slot5",
        "/dev/slot6",
        "/dev/slot7",
        "/dev/slot8",
        "/dev/slot9"
      ],
      "bmcFirmwareRevision": "1.6",
      "bmcIpmiVersion": "2.0",
      "chassisType": "R620",
      "cpuCores": 6,
      "cpuCoresEnabled": 6,
      "cpuModel": "Intel(R) Xeon(R) CPU E5-2640 0 @ 2.50GHz",
      "cpuThreads": 12,
      "driveSizeBytesInternal": 400088457216,
      "fibreChannelFirmwareRevision": "",
      "fibreChannelModel": "",
      "idracVersion": "1.06.06",
      "kernelCrashDump": {
        "kernelCrashDumpDefaultState": "enabled",
        "kernelCrashDumpDirectory": "/var/crash",
        "kernelCrashDumpKernelOptions": "ro console=tty10 console=ttyS1,115200n8 quiet splash vt.handoff=7 irqpoll maxcpus=1 reset_devices nousb modprobe.blacklist=qla2xxx,bnx2x,mpt2sas",
        "kernelCrashDumpMakedumpfileLevel": 31,
        "kernelCrashDumpMinFreeGb": 5
      },
      "lifecycleVersion": "1.0.0.5747",
      "memoryGB": 72,
      "memoryMhz": 1333,
      "networkDriver": [
        "bnx2x"
      ],
      "nodeType": "SF3010",
      "numCpu": 2,
      "numDrives": 10,
      "numDrivesInternal": 1,
      "rootDrive": "/dev/sdimm0",
      "scsiBusExternalDriver": "mpt2sas",
      "scsiBusInternalDriver": "ahci",
      "sliceDriveSizeBytes": 299988156416,
      "sliceDrives": [
        "/dev/sdimm0p4"
      ],
      "slotOffset": 0,
      "solidfireDefaults": {
        "bufferCacheGB": 12,
        "configuredIops": 50000,
        "cpuDmaLatency": -1,
        "driveWriteThroughputMBPerSleep": 10,
        "maxDriveWriteThroughputMBPerSec": 125,
        "maxIncomingSliceSyncs": 10,
        "postCallbackThreadCount": 8,
        "sCacheFileCapacity": 100000000,
        "sliceFileLogFileCapacity": 5000000000
      }
    }
  }
}"""

RESP_GetHardwareInfo_v9_0 = """{
  "id": 1,
  "result": {
    "hardwareInfo": {
      "bus": {
        "core_DMI:0200": {
          "description": "Motherboard",
          "physid": "0",
          "product": "0A47AA",
          "serial": "..AB123456C12354.",
          "version": "C07"
        }
      },
      "driveHardware": [
        {
          "canonicalName": "sdh",
          "connected": true,
          "dev": 2160,
          "devPath": "/dev/disk/by-path/pci-0000:41:00.0-sas-0x500056b37789abf0-lun-0",
          "driveType": "Block",
          "lifeRemainingPercent": 92,
          "lifetimeReadBytes": 175436696911872,
          "lifetimeWriteBytes": 81941097349120,
          "name": "scsi-SATA_INTEL_SSDSC2BB3BTWL12345686300AAA",
          "path": "/dev/sdh",
          "pathLink": "/dev/disk/by-path/pci-0000:41:00.0-sas-0x500056b37789abf0-lun-0",
          "powerOnHours": 17246,
          "product": "INTEL SSDAA2AA300A4",
          "reallocatedSectors": 0,
          "reserveCapacityPercent": 100,
          "scsiCompatId": "scsi-SATA_INTEL_SSDSC2BB3BTWL12345686300AAA",
          "scsiState": "Running",
          "securityAtMaximum": false,
          "securityEnabled": false,
          "securityFrozen": false,
          "securityLocked": false,
          "securitySupported": true,
          "serial": "AAAA33710886300AAA",
          "size": 300069052416,
          "slot": 1,
          "smartSsdWriteCapable": false,
          "uuid": "aea178b9-c336-6bab-a61d-87b615e8120c",
          "vendor": "Intel",
          "version": "D2010370"
        }
      ]
    }
  }
}"""

RESP_GetHardwareInfo_v9_1 = """{
   "id":1,
   "result":{
      "hardwareInfo":{
         "bus":{
            "core_DMI:0200":{
               "description":"Motherboard",
               "physid":"0",
               "product":"086D43",
               "serial":".JXBM382.CN7475163N0293.",
               "vendor":"SolidFire",
               "version":"A08"
            }
         },
         "driveHardware":[
            {
               "canonicalName":"sda",
               "connected":true,
               "dev":2048,
               "devPath":"/dev/slot0",
               "driveType":"Slice",
               "lifeRemainingPercent":100,
               "lifetimeReadBytes":26388279066624,
               "lifetimeWriteBytes":8796093022208,
               "name":"scsi-SATA_SDLFNCAR-960G-1_A0042192",
               "path":"/dev/sda",
               "pathLink":"/dev/slot0",
               "powerOnHours":1360,
               "product":"SDLFNCAR-960G-1HA2",
               "reallocatedSectors":0,
               "reserveCapacityPercent":100,
               "scsiCompatId":"scsi-SATA_SDLFNCAR-960G-1_A0042192",
               "scsiState":"Running",
               "securityAtMaximum":false,
               "securityEnabled":false,
               "securityFrozen":false,
               "securityLocked":false,
               "securitySupported":true,
               "serial":"A0042192",
               "size":960197124096,
               "slot":0,
               "uuid":"cd3c63b7-e769-4bdc-6453-7454f363a6bf",
               "vendor":"SanDisk",
               "version":"ZZ39RC93"
            },
            {
               "canonicalName":"sdb",
               "connected":true,
               "dev":2064,
               "devPath":"/dev/slot1",
               "driveType":"Block",
               "lifeRemainingPercent":100,
               "lifetimeReadBytes":26388279066624,
               "lifetimeWriteBytes":8796093022208,
               "name":"scsi-SATA_SDLFNCAR-960G-1_A00422F8",
               "path":"/dev/sdb",
               "pathLink":"/dev/slot1",
               "powerOnHours":1359,
               "product":"SDLFNCAR-960G-1HA2",
               "reallocatedSectors":0,
               "reserveCapacityPercent":100,
               "scsiCompatId":"scsi-SATA_SDLFNCAR-960G-1_A00422F8",
               "scsiState":"Running",
               "securityAtMaximum":false,
               "securityEnabled":false,
               "securityFrozen":false,
               "securityLocked":false,
               "securitySupported":true,
               "serial":"A00422F8",
               "size":960197124096,
               "slot":1,
               "uuid":"559cfb7f-12ff-a9ec-b238-61e62735d3ab",
               "vendor":"SanDisk",
               "version":"ZZ39RC93"
            },
            {
               "canonicalName":"sdc",
               "connected":true,
               "dev":2080,
               "devPath":"/dev/slot2",
               "driveType":"Block",
               "lifeRemainingPercent":100,
               "lifetimeReadBytes":26388279066624,
               "lifetimeWriteBytes":8796093022208,
               "name":"scsi-SATA_SDLFNCAR-960G-1_A0041F64",
               "path":"/dev/sdc",
               "pathLink":"/dev/slot2",
               "powerOnHours":1360,
               "product":"SDLFNCAR-960G-1HA2",
               "reallocatedSectors":0,
               "reserveCapacityPercent":100,
               "scsiCompatId":"scsi-SATA_SDLFNCAR-960G-1_A0041F64",
               "scsiState":"Running",
               "securityAtMaximum":false,
               "securityEnabled":false,
               "securityFrozen":false,
               "securityLocked":false,
               "securitySupported":true,
               "serial":"A0041F64",
               "size":960197124096,
               "slot":2,
               "uuid":"58b1771b-af45-636c-94a1-78bf7a96d3cb",
               "vendor":"SanDisk",
               "version":"ZZ39RC93"
            },
            {
               "canonicalName":"sdd",
               "connected":true,
               "dev":2096,
               "devPath":"/dev/slot3",
               "driveType":"Block",
               "lifeRemainingPercent":100,
               "lifetimeReadBytes":26388279066624,
               "lifetimeWriteBytes":8796093022208,
               "name":"scsi-SATA_SDLFNCAR-960G-1_A0042105",
               "path":"/dev/sdd",
               "pathLink":"/dev/slot3",
               "powerOnHours":1359,
               "product":"SDLFNCAR-960G-1HA2",
               "reallocatedSectors":0,
               "reserveCapacityPercent":100,
               "scsiCompatId":"scsi-SATA_SDLFNCAR-960G-1_A0042105",
               "scsiState":"Running",
               "securityAtMaximum":false,
               "securityEnabled":false,
               "securityFrozen":false,
               "securityLocked":false,
               "securitySupported":true,
               "serial":"A0042105",
               "size":960197124096,
               "slot":3,
               "uuid":"337011b3-3339-7ff6-161a-b9e872acf033",
               "vendor":"SanDisk",
               "version":"ZZ39RC93"
            },
            {
               "canonicalName":"sde",
               "connected":true,
               "dev":2112,
               "devPath":"/dev/slot4",
               "driveType":"Block",
               "lifeRemainingPercent":100,
               "lifetimeReadBytes":26388279066624,
               "lifetimeWriteBytes":8796093022208,
               "name":"scsi-SATA_SDLFNCAR-960G-1_A004220B",
               "path":"/dev/sde",
               "pathLink":"/dev/slot4",
               "powerOnHours":1360,
               "product":"SDLFNCAR-960G-1HA2",
               "reallocatedSectors":0,
               "reserveCapacityPercent":100,
               "scsiCompatId":"scsi-SATA_SDLFNCAR-960G-1_A004220B",
               "scsiState":"Running",
               "securityAtMaximum":false,
               "securityEnabled":false,
               "securityFrozen":false,
               "securityLocked":false,
               "securitySupported":true,
               "serial":"A004220B",
               "size":960197124096,
               "slot":4,
               "uuid":"774f2b16-d765-0cb6-ee0d-5e137a48c313",
               "vendor":"SanDisk",
               "version":"ZZ39RC93"
            },
            {
               "canonicalName":"sdf",
               "connected":true,
               "dev":2128,
               "devPath":"/dev/slot5",
               "driveType":"Block",
               "lifeRemainingPercent":100,
               "lifetimeReadBytes":26388279066624,
               "lifetimeWriteBytes":8796093022208,
               "name":"scsi-SATA_SDLFNCAR-960G-1_A004214D",
               "path":"/dev/sdf",
               "pathLink":"/dev/slot5",
               "powerOnHours":1360,
               "product":"SDLFNCAR-960G-1HA2",
               "reallocatedSectors":0,
               "reserveCapacityPercent":100,
               "scsiCompatId":"scsi-SATA_SDLFNCAR-960G-1_A004214D",
               "scsiState":"Running",
               "securityAtMaximum":false,
               "securityEnabled":false,
               "securityFrozen":false,
               "securityLocked":false,
               "securitySupported":true,
               "serial":"A004214D",
               "size":960197124096,
               "slot":5,
               "uuid":"f09d575a-8b1c-cd29-95e9-6a059f090f40",
               "vendor":"SanDisk",
               "version":"ZZ39RC93"
            },
            {
               "canonicalName":"sdg",
               "connected":true,
               "dev":2144,
               "devPath":"/dev/slot6",
               "driveType":"Block",
               "lifeRemainingPercent":100,
               "lifetimeReadBytes":26388279066624,
               "lifetimeWriteBytes":8796093022208,
               "name":"scsi-SATA_SDLFNCAR-960G-1_A0042245",
               "path":"/dev/sdg",
               "pathLink":"/dev/slot6",
               "powerOnHours":1360,
               "product":"SDLFNCAR-960G-1HA2",
               "reallocatedSectors":0,
               "reserveCapacityPercent":100,
               "scsiCompatId":"scsi-SATA_SDLFNCAR-960G-1_A0042245",
               "scsiState":"Running",
               "securityAtMaximum":false,
               "securityEnabled":false,
               "securityFrozen":false,
               "securityLocked":false,
               "securitySupported":true,
               "serial":"A0042245",
               "size":960197124096,
               "slot":6,
               "uuid":"142a1090-4f4c-e0a9-28a7-76f9f5735c3d",
               "vendor":"SanDisk",
               "version":"ZZ39RC93"
            },
            {
               "canonicalName":"sdh",
               "connected":true,
               "dev":2160,
               "devPath":"/dev/slot7",
               "driveType":"Block",
               "lifeRemainingPercent":100,
               "lifetimeReadBytes":26388279066624,
               "lifetimeWriteBytes":8796093022208,
               "name":"scsi-SATA_SDLFNCAR-960G-1_A0041F78",
               "path":"/dev/sdh",
               "pathLink":"/dev/slot7",
               "powerOnHours":1360,
               "product":"SDLFNCAR-960G-1HA2",
               "reallocatedSectors":0,
               "reserveCapacityPercent":100,
               "scsiCompatId":"scsi-SATA_SDLFNCAR-960G-1_A0041F78",
               "scsiState":"Running",
               "securityAtMaximum":false,
               "securityEnabled":false,
               "securityFrozen":false,
               "securityLocked":false,
               "securitySupported":true,
               "serial":"A0041F78",
               "size":960197124096,
               "slot":7,
               "uuid":"d0919cb3-bd2a-10e5-1ac6-9b13d7baae5d",
               "vendor":"SanDisk",
               "version":"ZZ39RC93"
            },
            {
               "canonicalName":"sdi",
               "connected":true,
               "dev":2176,
               "devPath":"/dev/slot8",
               "driveType":"Block",
               "lifeRemainingPercent":100,
               "lifetimeReadBytes":26388279066624,
               "lifetimeWriteBytes":8796093022208,
               "name":"scsi-SATA_SDLFNCAR-960G-1_A00422DB",
               "path":"/dev/sdi",
               "pathLink":"/dev/slot8",
               "powerOnHours":1359,
               "product":"SDLFNCAR-960G-1HA2",
               "reallocatedSectors":0,
               "reserveCapacityPercent":100,
               "scsiCompatId":"scsi-SATA_SDLFNCAR-960G-1_A00422DB",
               "scsiState":"Running",
               "securityAtMaximum":false,
               "securityEnabled":false,
               "securityFrozen":false,
               "securityLocked":false,
               "securitySupported":true,
               "serial":"A00422DB",
               "size":960197124096,
               "slot":8,
               "uuid":"872a8610-f7dc-c07c-e181-e5b27f49dc51",
               "vendor":"SanDisk",
               "version":"ZZ39RC93"
            },
            {
               "canonicalName":"sdj",
               "connected":true,
               "dev":2192,
               "devPath":"/dev/slot9",
               "driveType":"Block",
               "lifeRemainingPercent":100,
               "lifetimeReadBytes":26388279066624,
               "lifetimeWriteBytes":8796093022208,
               "name":"scsi-SATA_SDLFNCAR-960G-1_A0042195",
               "path":"/dev/sdj",
               "pathLink":"/dev/slot9",
               "powerOnHours":1360,
               "product":"SDLFNCAR-960G-1HA2",
               "reallocatedSectors":0,
               "reserveCapacityPercent":100,
               "scsiCompatId":"scsi-SATA_SDLFNCAR-960G-1_A0042195",
               "scsiState":"Running",
               "securityAtMaximum":false,
               "securityEnabled":false,
               "securityFrozen":false,
               "securityLocked":false,
               "securitySupported":true,
               "serial":"A0042195",
               "size":960197124096,
               "slot":9,
               "uuid":"97e3f7a6-9a7a-05c1-ff4c-ebe017783ec6",
               "vendor":"SanDisk",
               "version":"ZZ39RC93"
            }
         ],
         "fibreChannelPorts":[

         ],
         "fileSystemUsage":{

         },
         "hardwareConfig":null,
         "kernelCrashDumpState":"EnabledByDefault",
         "memory":{
            "firmware_":{
               "capacity":"16711680",
               "date":"03/09/2015",
               "description":"BIOS",
               "physid":"0",
               "size":"65536",
               "vendor":"SolidFire",
               "version":"1.2.10"
            },
            "memory_DMI:1000":{
               "description":"System Memory",
               "physid":"1000",
               "size":"274877906944",
               "slot":"System board or motherboard"
            }
         },
         "network":{
            "network:0_":{
               "description":"Ethernet interface",
               "logicalname":"Bond1G",
               "physid":"1",
               "serial":"14:18:77:71:7d:dd"
            },
            "network:0_PCI:0000:01:00.0":{
               "businfo":"pci@0000:01:00.0",
               "capacity":"1000000000",
               "clock":"33000000",
               "description":"Ethernet interface",
               "logicalname":"eth0",
               "physid":"0",
               "product":"NetXtreme II BCM57800 1/10 Gigabit Ethernet",
               "serial":"14:18:77:71:7d:d9",
               "vendor":"Broadcom Corporation",
               "version":"10",
               "width":"64"
            },
            "network:1_":{
               "description":"Ethernet interface",
               "logicalname":"Bond10G",
               "physid":"2",
               "serial":"14:18:77:71:7d:d9"
            },
            "network:1_PCI:0000:01:00.1":{
               "businfo":"pci@0000:01:00.1",
               "capacity":"1000000000",
               "clock":"33000000",
               "description":"Ethernet interface",
               "logicalname":"eth1",
               "physid":"0.1",
               "product":"NetXtreme II BCM57800 1/10 Gigabit Ethernet",
               "serial":"14:18:77:71:7d:d9",
               "vendor":"Broadcom Corporation",
               "version":"10",
               "width":"64"
            },
            "network:2_PCI:0000:01:00.2":{
               "businfo":"pci@0000:01:00.2",
               "capacity":"1000000000",
               "clock":"33000000",
               "description":"Ethernet interface",
               "logicalname":"eth2",
               "physid":"0.2",
               "product":"NetXtreme II BCM57800 1/10 Gigabit Ethernet",
               "serial":"14:18:77:71:7d:dd",
               "size":"1000000000",
               "vendor":"Broadcom Corporation",
               "version":"10",
               "width":"64"
            },
            "network:3_PCI:0000:01:00.3":{
               "businfo":"pci@0000:01:00.3",
               "capacity":"1000000000",
               "clock":"33000000",
               "description":"Ethernet interface",
               "logicalname":"eth3",
               "physid":"0.3",
               "product":"NetXtreme II BCM57800 1/10 Gigabit Ethernet",
               "serial":"14:18:77:71:7d:dd",
               "size":"1000000000",
               "vendor":"Broadcom Corporation",
               "version":"10",
               "width":"64"
            }
         },
         "networkInterfaces":{
            "Bond10G":{
               "isConfigured":true,
               "isUp":true
            },
            "Bond1G":{
               "isConfigured":true,
               "isUp":true
            },
            "eth0":{
               "isConfigured":true,
               "isUp":true
            },
            "eth1":{
               "isConfigured":true,
               "isUp":true
            },
            "eth2":{
               "isConfigured":true,
               "isUp":true
            },
            "eth3":{
               "isConfigured":true,
               "isUp":true
            }
         },
         "nvram":{
            "errors":{
               "numOfErrorLogEntries":"0"
            },
            "extended":{
               "dialogVersion":"4",
               "event":[
                  {
                     "name":"flushToFlash",
                     "time":"1948-05-19 10:51:42",
                     "value":"0"
                  },
                  {
                     "name":"flushToFlash",
                     "time":"1948-05-19 10:52:05",
                     "value":"0"
                  },
                  {
                     "name":"flushToFlash",
                     "time":"1948-05-19 10:52:05",
                     "value":"0"
                  },
                  {
                     "name":"flushToFlash",
                     "time":"1948-05-19 10:52:28",
                     "value":"0"
                  },
                  {
                     "name":"flushToFlash",
                     "time":"1948-05-19 10:52:28",
                     "value":"0"
                  },
                  {
                     "name":"flushToFlash",
                     "time":"2016-06-06 21:17:48",
                     "value":"0"
                  },
                  {
                     "name":"flushToFlash",
                     "time":"2016-11-11 17:46:27",
                     "value":"0"
                  },
                  {
                     "name":"flushToFlash",
                     "time":"2016-11-11 18:06:36",
                     "value":"0"
                  }
               ],
               "eventOccurrences":[
                  {
                     "count":"33",
                     "name":"flushToFlash"
                  }
               ],
               "initialCapacitance":"7.230 F",
               "initialEsr":"0.094 Ohm",
               "measurement":[
                  {
                     "level_0":" 0",
                     "level_1":" 248",
                     "level_2":" 81248",
                     "level_3":" 115282",
                     "level_4":" 1452745",
                     "level_5":" 2656",
                     "level_6":" 0",
                     "level_7":" 0",
                     "level_8":" 0",
                     "level_9":" 0",
                     "name":"enterpriseFlashControllerTemperature",
                     "recent":"71 C"
                  },
                  {
                     "level_0":" 0",
                     "level_1":" 19",
                     "level_2":" 17817",
                     "level_3":" 172973",
                     "level_4":" 86276",
                     "level_5":" 1371833",
                     "level_6":" 3261",
                     "level_7":" 0",
                     "level_8":" 0",
                     "level_9":" 0",
                     "name":"capacitor1And2Temperature",
                     "recent":"36.85 C"
                  },
                  {
                     "level_0":" 0",
                     "level_1":" 93",
                     "level_2":" 169360",
                     "level_3":" 79108",
                     "level_4":" 1335529",
                     "level_5":" 68089",
                     "level_6":" 0",
                     "level_7":" 0",
                     "level_8":" 0",
                     "level_9":" 0",
                     "name":"capacitor3And4Temperature",
                     "recent":"32.39 C"
                  },
                  {
                     "level_0":" 0",
                     "level_1":" 74000",
                     "level_2":" 12628",
                     "level_3":" 87751",
                     "level_4":" 177086",
                     "level_5":" 1298124",
                     "level_6":" 2590",
                     "level_7":" 0",
                     "level_8":" 0",
                     "level_9":" 0",
                     "name":"rearVentAmbientTemperature",
                     "recent":"40.97 C"
                  },
                  {
                     "level_0":" 0",
                     "level_1":" 143951",
                     "level_2":" 1211634",
                     "level_3":" 296594",
                     "level_4":" 0",
                     "level_5":" 0",
                     "level_6":" 0",
                     "level_7":" 0",
                     "level_8":" 0",
                     "level_9":" 0",
                     "name":"rms200BoardTemperature",
                     "recent":"54.81 C"
                  },
                  {
                     "name":"voltageOfCapacitor1",
                     "recent":"2.281 V"
                  },
                  {
                     "name":"voltageOfCapacitor2",
                     "recent":"2.267 V"
                  },
                  {
                     "name":"voltageOfCapacitor3",
                     "recent":"2.283 V"
                  },
                  {
                     "name":"voltageOfCapacitor4",
                     "recent":"2.251 V"
                  },
                  {
                     "level_0":" 81187",
                     "level_1":" 286238",
                     "level_2":" 1064490",
                     "level_3":" 171445",
                     "level_4":" 19579",
                     "level_5":" 12403",
                     "level_6":" 16837",
                     "level_7":" 0",
                     "level_8":" 0",
                     "level_9":" 0",
                     "name":"capacitorPackVoltage",
                     "recent":"9.082 V"
                  },
                  {
                     "level_0":" 0",
                     "level_1":" 0",
                     "level_2":" 0",
                     "level_3":" 0",
                     "level_4":" 0",
                     "level_5":" 23",
                     "level_6":" 3",
                     "level_7":" 0",
                     "level_8":" 0",
                     "level_9":" 7",
                     "name":"capacitorPackVoltageAtEndOfFlushToFlash",
                     "recent":"5.748 V"
                  },
                  {
                     "name":"currentDerivedFromV3V4",
                     "recent":"-0.002 A"
                  },
                  {
                     "level_0":" 12",
                     "level_1":" 20",
                     "level_2":" 1",
                     "level_3":" 0",
                     "level_4":" 0",
                     "level_5":" 0",
                     "level_6":" 0",
                     "level_7":" 0",
                     "level_8":" 0",
                     "level_9":" 0",
                     "name":"derivedEnergy",
                     "recent":"165 Joules"
                  },
                  {
                     "level_0":" 0",
                     "level_1":" 0",
                     "level_2":" 0",
                     "level_3":" 0",
                     "level_4":" 0",
                     "level_5":" 0",
                     "level_6":" 0",
                     "level_7":" 0",
                     "level_8":" 1",
                     "level_9":" 17",
                     "name":"derivedCapacitanceOfThePack",
                     "recent":"6.755 F"
                  },
                  {
                     "level_0":" 0",
                     "level_1":" 18",
                     "level_2":" 0",
                     "level_3":" 0",
                     "level_4":" 0",
                     "level_5":" 0",
                     "level_6":" 0",
                     "level_7":" 0",
                     "level_8":" 0",
                     "level_9":" 0",
                     "name":"derivedEsrOfCapacitorPack",
                     "recent":"0.096 Ohm"
                  },
                  {
                     "level_0":" 0",
                     "level_1":" 0",
                     "level_2":" 1",
                     "level_3":" 0",
                     "level_4":" 4",
                     "level_5":" 28",
                     "level_6":" 0",
                     "level_7":" 0",
                     "level_8":" 0",
                     "level_9":" 0",
                     "name":"timeToRunFlushToFlash",
                     "recent":"22.94 Seconds"
                  },
                  {
                     "level_0":" 0",
                     "level_1":" 0",
                     "level_2":" 16",
                     "level_3":" 0",
                     "level_4":" 0",
                     "level_5":" 0",
                     "level_6":" 0",
                     "level_7":" 0",
                     "level_8":" 0",
                     "level_9":" 0",
                     "name":"timeToRunRestore",
                     "recent":"20.40 Seconds"
                  },
                  {
                     "level_0":" 0",
                     "level_1":" 14",
                     "level_2":" 0",
                     "level_3":" 1",
                     "level_4":" 0",
                     "level_5":" 0",
                     "level_6":" 0",
                     "level_7":" 0",
                     "level_8":" 0",
                     "level_9":" 0",
                     "name":"timeToChargeCapacitors",
                     "recent":"42 Seconds"
                  },
                  {
                     "level_0":" 963010",
                     "level_1":" 69182",
                     "level_2":" 0",
                     "level_3":" 0",
                     "level_4":" 0",
                     "level_5":" 0",
                     "level_6":" 0",
                     "level_7":" 0",
                     "level_8":" 0",
                     "level_9":" 0",
                     "name":"correctableBitsInErrorOnReadingAPage"
                  },
                  {
                     "level_0":" 69182",
                     "level_1":" 0",
                     "level_2":" 0",
                     "level_3":" 0",
                     "level_4":" 0",
                     "level_5":" 0",
                     "level_6":" 0",
                     "level_7":" 0",
                     "level_8":" 0",
                     "level_9":" 0",
                     "name":"correctableBitsInErrorOnReadingTheWorstBchRegionOfAPage"
                  },
                  {
                     "level_0":" 0",
                     "level_1":" 116",
                     "level_2":" 79454",
                     "level_3":" 2959",
                     "level_4":" 60469",
                     "level_5":" 100691",
                     "level_6":" 1402834",
                     "level_7":" 5656",
                     "level_8":" 0",
                     "level_9":" 0",
                     "name":"fanInletAmbientTemperature",
                     "recent":"47.76 C"
                  }
               ],
               "smartCounters":[
                  {
                     "name":"numberOf512ByteBlocksReadFromDdr",
                     "value":"100583400471"
                  },
                  {
                     "name":"numberOf512ByteBlocksWrittenToDdr",
                     "value":"100461106048"
                  },
                  {
                     "name":"numberOfHostReadCommands",
                     "value":"440796905"
                  },
                  {
                     "name":"numberOfHostWriteCommands",
                     "value":"423222231"
                  },
                  {
                     "name":"controllerBusyTimeMinutes",
                     "value":"347"
                  },
                  {
                     "name":"numberOfPowerCycles",
                     "value":"13"
                  },
                  {
                     "name":"powerOnHours",
                     "value":"1318"
                  },
                  {
                     "name":"unsafeShutdowns",
                     "value":"7"
                  },
                  {
                     "name":"mediaErrors",
                     "value":"0"
                  },
                  {
                     "name":"numberOfErrorLogs",
                     "value":"16"
                  }
               ],
               "snapshotTime":"2016-11-29 16:16:09"
            },
            "firmware":{
               "activeSlotNumber":"2",
               "slot1Version":"5fb7565c",
               "slot2Version":"5fb7565c",
               "slot3Version":"5fb7565c",
               "slot4Version":"5fb7565c"
            },
            "identify":{
               "firmwareVersion":"5fb7565c on slot 2",
               "hardwareRevision":"B04",
               "modelNumber":"RMS-200",
               "serialNumber":"0038931"
            },
            "smart":{
               "availableSpace":"0%",
               "availableSpaceThreshold":"0%",
               "controllerBusyTimeMinutes":"347",
               "criticalErrorVector":"0x0",
               "mediaErrors":"0",
               "numberOf512ByteBlocksRead":"100583400471",
               "numberOf512ByteBlocksWritten":"100461106048",
               "numberOfErrorInfoLogs":"16",
               "numberOfHostReadCommands":"440796905",
               "numberOfHostWriteCommands":"423222231",
               "numberOfPowerCycles":"13",
               "powerOnHours":"1318",
               "temperature":"327 Kelvin",
               "unsafeShutdowns":"7"
            }
         },
         "origin":{
            "<signature>":{
               "data":"eiPNNA3TpfgO0bl+SnhjaO1ZEKJUPZJDG1PFZrbOmUu5JXfQ012Aq0RzhMSKIb8MVTgesZ/+urfzuVD9Zf1JKwnfv7h3UZLMzE7eC6rJnLNi+AgHEYvqBLLKMJ39HNj+xEOogpQmBIn5jKv7U05pk4tsQwbxv4HtoQNMEl+PdQuVdDGLD9ipU3jgAw5sHFFZ+hLq8Uk3fzUiiR7LcW2b9aAw4KEQdSj/OhCNB4/7IcKOq8YBpP3ONWb+N6jrqSfMtnD4sa7vzSX7vI0z++zBeUd6E0hJz7atonS6oAqtyT4F48giO6hBSfkqt0KLvvC1Mcgh0LQrQG+XZnQ5KWBIuQ==",
               "pubkey":"MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAxmKgEBzyZv2jFZpucao7HT9lYuR3g/18thP/7arwflrtDauIaPaIbnsuDVWgbPKHsqBkth9XCnDF16yBOFYoJLZ+vW0kNS7Z/CiCiLlmAXIa4voeEqLsQ55IbAhjMXfrGauyUHZYunMBhUG3xDJxdrs4Rgp24VqB/oBxihleyotIX+dLpv7nd7qbVA3juLMAy7cfgxUX7mAEmPAcx3gNiNw7SBBZaeFVrNSiXv3+Zrw5wLkLH1QDWwuBRK+3yGTkzVwD5QgLw0qkRMkFobBhk96Z7CQbf4B/8zi3bhvowoyaK+4Cv/jmEjs2TS0QFW0PQHKIjyC3ckkcLaZZ2DQcLQIDAQAB",
               "version":1
            },
            "contract-date":"10/1/2015",
            "contract-name":"00002265",
            "contract-quantity":0,
            "contract-type":"Master",
            "integrator":"StackVelocity",
            "location":"Memphis, Tennessee",
            "organization":"none",
            "type":"appliance"
         },
         "platform":{
            "chassisType":"R630",
            "cpuModel":"Intel(R) Xeon(R) CPU E5-2620 v3 @ 2.40GHz",
            "nodeMemoryGB":256,
            "nodeType":"SF9605"
         },
         "serial":"JXBM382",
         "storage":{
            "storage:0_PCI:0000:00:11.4":{
               "businfo":"pci@0000:00:11.4",
               "clock":"66000000",
               "description":"SATA controller",
               "physid":"11.4",
               "product":"Wellsburg sSATA Controller [AHCI mode]",
               "vendor":"Intel Corporation",
               "version":"05",
               "width":"32"
            },
            "storage:1_PCI:0000:00:1f.2":{
               "businfo":"pci@0000:00:1f.2",
               "clock":"66000000",
               "description":"SATA controller",
               "physid":"1f.2",
               "product":"Wellsburg 6-Port SATA Controller [AHCI mode]",
               "vendor":"Intel Corporation",
               "version":"05",
               "width":"32"
            },
            "storage_PCI:0000:03:00.0":{
               "businfo":"pci@0000:03:00.0",
               "clock":"33000000",
               "description":"Non-Volatile memory controller",
               "physid":"0",
               "version":"05",
               "width":"64"
            },
            "storage_PCI:0000:82:00.0":{
               "businfo":"pci@0000:82:00.0",
               "clock":"33000000",
               "description":"Serial Attached SCSI controller",
               "physid":"0",
               "product":"SAS2008 PCI-Express Fusion-MPT SAS-2 [Falcon]",
               "vendor":"LSI Logic / Symbios Logic",
               "version":"03",
               "width":"64"
            }
         },
         "system":{
            "vcpnode4_DMI:0100":{
               "description":"Rack Mount Chassis",
               "product":"Storage System (SKU=NotProvided;ModelName=Storage System)",
               "serial":"JXBM382",
               "vendor":"SolidFire",
               "width":"64"
            }
         },
         "systemMemory":{
            "free":216479330304,
            "total":269981622272,
            "used":53502291968
         },
         "uuid":"4C4C4544-0058-4210-804D-CAC04F333832"
      }
   }
}"""

RESP_GetHardwareInfo_v9_2 = """{
   "id":3,
   "result":{
      "hardwareInfo":{
         "bus":{
            "core_DMI:0200":{
               "description":"Motherboard",
               "physid":"0",
               "product":"0H47HH",
               "serial":"..CN747513450302.",
               "vendor":"SolidFire",
               "version":"A09"
            },
            "fiber:0_PCI:0000:04:00.0":{
               "businfo":"pci@0000:04:00.0",
               "clock":"33000000",
               "description":"Fibre Channel",
               "physid":"0",
               "product":"ISP8324-based 16Gb Fibre Channel to PCI Express Adapter",
               "vendor":"QLogic Corp.",
               "version":"02",
               "width":"64"
            },
            "fiber:0_PCI:0000:42:00.0":{
               "businfo":"pci@0000:42:00.0",
               "clock":"33000000",
               "description":"Fibre Channel",
               "physid":"0",
               "product":"ISP8324-based 16Gb Fibre Channel to PCI Express Adapter",
               "vendor":"QLogic Corp.",
               "version":"02",
               "width":"64"
            },
            "fiber:1_PCI:0000:04:00.1":{
               "businfo":"pci@0000:04:00.1",
               "clock":"33000000",
               "description":"Fibre Channel",
               "physid":"0.1",
               "product":"ISP8324-based 16Gb Fibre Channel to PCI Express Adapter",
               "vendor":"QLogic Corp.",
               "version":"02",
               "width":"64"
            },
            "fiber:1_PCI:0000:42:00.1":{
               "businfo":"pci@0000:42:00.1",
               "clock":"33000000",
               "description":"Fibre Channel",
               "physid":"0.1",
               "product":"ISP8324-based 16Gb Fibre Channel to PCI Express Adapter",
               "vendor":"QLogic Corp.",
               "version":"02",
               "width":"64"
            }
         },
         "driveHardware":[

         ],
         "fibreChannelPorts":[
            {
               "firmware":"8.02.03 (d0d5)",
               "hbaPort":1,
               "model":"QLE2672",
               "nPortID":"0x8d0200",
               "pciSlot":3,
               "serial":"BFE1435K26421",
               "speed":"16 Gbit",
               "state":"Online",
               "switchWwn":"20:01:8c:60:4f:f1:55:91",
               "wwnn":"5f:47:ac:c8:8d:08:96:00",
               "wwpn":"5f:47:ac:c0:8d:08:96:02"
            },
            {
               "firmware":"8.02.03 (d0d5)",
               "hbaPort":2,
               "model":"QLE2672",
               "nPortID":"0x6d0400",
               "pciSlot":3,
               "serial":"BFE1435K26421",
               "speed":"16 Gbit",
               "state":"Online",
               "switchWwn":"20:01:8c:60:4f:f1:5c:61",
               "wwnn":"5f:47:ac:c8:8d:08:96:00",
               "wwpn":"5f:47:ac:c0:8d:08:96:03"
            },
            {
               "firmware":"8.02.03 (d0d5)",
               "hbaPort":1,
               "model":"QLE2672",
               "nPortID":"0x6d0500",
               "pciSlot":2,
               "serial":"BFE1435K26220",
               "speed":"16 Gbit",
               "state":"Online",
               "switchWwn":"20:01:8c:60:4f:f1:5c:61",
               "wwnn":"5f:47:ac:c8:8d:08:96:00",
               "wwpn":"5f:47:ac:c0:8d:08:96:00"
            },
            {
               "firmware":"8.02.03 (d0d5)",
               "hbaPort":2,
               "model":"QLE2672",
               "nPortID":"0x8d0300",
               "pciSlot":2,
               "serial":"BFE1435K26220",
               "speed":"16 Gbit",
               "state":"Online",
               "switchWwn":"20:01:8c:60:4f:f1:55:91",
               "wwnn":"5f:47:ac:c8:8d:08:96:00",
               "wwpn":"5f:47:ac:c0:8d:08:96:01"
            }
         ],
         "fileSystemUsage":{

         },
         "hardwareConfig":null,
         "kernelCrashDumpState":"EnabledByDefault",
         "memory":{
            "firmware_":{
               "capacity":"8323072",
               "date":"01/16/2014",
               "description":"BIOS",
               "physid":"0",
               "size":"65536",
               "vendor":"SolidFire",
               "version":"2.2.2"
            },
            "memory_DMI:1000":{
               "description":"System Memory",
               "physid":"1000",
               "size":"34359738368",
               "slot":"System board or motherboard"
            }
         },
         "network":{
            "network:0_":{
               "description":"Ethernet interface",
               "logicalname":"Bond1G",
               "physid":"1",
               "serial":"b8:2a:72:cf:af:46"
            },
            "network:0_PCI:0000:01:00.0":{
               "businfo":"pci@0000:01:00.0",
               "capacity":"1000000000",
               "clock":"33000000",
               "description":"Ethernet interface",
               "logicalname":"eth0",
               "physid":"0",
               "product":"NetXtreme II BCM57800 1/10 Gigabit Ethernet",
               "serial":"b8:2a:72:cf:af:42",
               "vendor":"Broadcom Corporation",
               "version":"10",
               "width":"64"
            },
            "network:0_PCI:0000:41:00.0":{
               "businfo":"pci@0000:41:00.0",
               "capacity":"1000000000",
               "clock":"33000000",
               "description":"Ethernet interface",
               "logicalname":"eth4",
               "physid":"0",
               "product":"NetXtreme II BCM57810 10 Gigabit Ethernet",
               "serial":"b8:2a:72:cf:af:42",
               "vendor":"Broadcom Corporation",
               "version":"10",
               "width":"64"
            },
            "network:1_":{
               "description":"Ethernet interface",
               "logicalname":"Bond10G",
               "physid":"2",
               "serial":"b8:2a:72:cf:af:42"
            },
            "network:1_PCI:0000:01:00.1":{
               "businfo":"pci@0000:01:00.1",
               "capacity":"1000000000",
               "clock":"33000000",
               "description":"Ethernet interface",
               "logicalname":"eth1",
               "physid":"0.1",
               "product":"NetXtreme II BCM57800 1/10 Gigabit Ethernet",
               "serial":"b8:2a:72:cf:af:42",
               "vendor":"Broadcom Corporation",
               "version":"10",
               "width":"64"
            },
            "network:1_PCI:0000:41:00.1":{
               "businfo":"pci@0000:41:00.1",
               "capacity":"1000000000",
               "clock":"33000000",
               "description":"Ethernet interface",
               "logicalname":"eth5",
               "physid":"0.1",
               "product":"NetXtreme II BCM57810 10 Gigabit Ethernet",
               "serial":"b8:2a:72:cf:af:42",
               "vendor":"Broadcom Corporation",
               "version":"10",
               "width":"64"
            },
            "network:2_PCI:0000:01:00.2":{
               "businfo":"pci@0000:01:00.2",
               "capacity":"1000000000",
               "clock":"33000000",
               "description":"Ethernet interface",
               "logicalname":"eth2",
               "physid":"0.2",
               "product":"NetXtreme II BCM57800 1/10 Gigabit Ethernet",
               "serial":"b8:2a:72:cf:af:46",
               "size":"1000000000",
               "vendor":"Broadcom Corporation",
               "version":"10",
               "width":"64"
            },
            "network:3_PCI:0000:01:00.3":{
               "businfo":"pci@0000:01:00.3",
               "capacity":"1000000000",
               "clock":"33000000",
               "description":"Ethernet interface",
               "logicalname":"eth3",
               "physid":"0.3",
               "product":"NetXtreme II BCM57800 1/10 Gigabit Ethernet",
               "serial":"b8:2a:72:cf:af:46",
               "size":"1000000000",
               "vendor":"Broadcom Corporation",
               "version":"10",
               "width":"64"
            }
         },
         "networkInterfaces":{
            "Bond10G":{
               "isConfigured":true,
               "isUp":true
            },
            "Bond1G":{
               "isConfigured":true,
               "isUp":true
            },
            "eth0":{
               "isConfigured":true,
               "isUp":true
            },
            "eth1":{
               "isConfigured":true,
               "isUp":true
            },
            "eth2":{
               "isConfigured":true,
               "isUp":true
            },
            "eth3":{
               "isConfigured":true,
               "isUp":true
            },
            "eth4":{
               "isConfigured":true,
               "isUp":false
            },
            "eth5":{
               "isConfigured":true,
               "isUp":false
            }
         },
         "nvram":{
            "info":"No device found",
            "raw":"No device found",
            "status":"Error",
            "version":"1.0"
         },
         "origin":null,
         "platform":{
            "chassisType":"R620",
            "cpuModel":"Intel(R) Xeon(R) CPU E5-2640 0 @ 2.50GHz",
            "nodeMemoryGB":32,
            "nodeType":"FC0025"
         },
         "serial":"B2K8Q22",
         "storage":{
            "storage_PCI:0000:00:1f.2":{
               "businfo":"pci@0000:00:1f.2",
               "clock":"66000000",
               "description":"SATA controller",
               "physid":"1f.2",
               "product":"C600/X79 series chipset 6-Port SATA AHCI Controller",
               "vendor":"Intel Corporation",
               "version":"05",
               "width":"32"
            }
         },
         "system":{
            "sf-5391_DMI:0100":{
               "description":"Rack Mount Chassis",
               "product":"SFx010 (SKU=NotProvided;ModelName=SFx010)",
               "serial":"B2K8Q22",
               "vendor":"SolidFire",
               "width":"64"
            }
         },
         "systemMemory":{
            "free":25261801472,
            "total":33286406144,
            "used":8024604672
         },
         "uuid":"4C4C4544-0032-4B10-8038-C2C04F513232"
      }
   }
}"""

RESP_GetHardwareInfo_v9_3 = """{
   "id":3,
   "result":{
	   "hardwareInfo":{
		  "bus":{
			 "core_DMI:0002":{
				"description":"Motherboard",
				"physid":"0",
				"product":"440BX Desktop Reference Platform",
				"serial":"None",
				"vendor":"Intel Corporation",
				"version":"None"
			 }
		  },
		  "driveHardware":[
			 {
				"canonicalName":"sda",
				"connected":true,
				"dev":2054,
				"devPath":"/dev/slot0p6",
				"driveType":"Slice",
				"lifeRemainingPercent":100,
				"lifetimeReadBytes":0,
				"lifetimeWriteBytes":0,
				"name":"scsi-36000c29551932b43ba5bb11c3cd54c1e-part6",
				"path":"/dev/sda6",
				"pathLink":"/dev/slot0p6",
				"powerOnHours":0,
				"product":"Unknown",
				"reallocatedSectors":0,
				"reserveCapacityPercent":100,
				"scsiCompatId":"scsi-36000c29551932b43ba5bb11c3cd54c1e-part6",
				"scsiState":"Running",
				"securityAtMaximum":false,
				"securityEnabled":false,
				"securityFrozen":false,
				"securityLocked":false,
				"securitySupported":false,
				"serial":"scsi-36000c29551932b43ba5bb11c3cd54c1e-part6",
				"size":216787845120,
				"slot":0,
				"uuid":"38b3c943-9e45-88e9-1ebe-130b4186d8da",
				"vendor":"Unknown",
				"version":"Unknown"
			 },
			 {
				"canonicalName":"sdb",
				"connected":true,
				"dev":2064,
				"devPath":"/dev/slot1",
				"driveType":"Block",
				"lifeRemainingPercent":100,
				"lifetimeReadBytes":0,
				"lifetimeWriteBytes":0,
				"name":"scsi-36000c29b0d225d4342d5750a81af4ea6",
				"path":"/dev/sdb",
				"pathLink":"/dev/slot1",
				"powerOnHours":0,
				"product":"Unknown",
				"reallocatedSectors":0,
				"reserveCapacityPercent":100,
				"scsiCompatId":"scsi-36000c29b0d225d4342d5750a81af4ea6",
				"scsiState":"Running",
				"securityAtMaximum":false,
				"securityEnabled":false,
				"securityFrozen":false,
				"securityLocked":false,
				"securitySupported":false,
				"serial":"scsi-36000c29b0d225d4342d5750a81af4ea6",
				"size":268435456000,
				"slot":1,
				"uuid":"a6944a6f-46f4-addb-ba1e-4c237b5fedc5",
				"vendor":"Unknown",
				"version":"Unknown"
			 },
			 {
				"canonicalName":"",
				"connected":false,
				"dev":0,
				"devPath":"/dev/slot2",
				"driveType":"Block",
				"lifeRemainingPercent":100,
				"lifetimeReadBytes":0,
				"lifetimeWriteBytes":0,
				"name":"slot2",
				"path":"/dev/slot2",
				"pathLink":"/dev/slot2",
				"powerOnHours":0,
				"product":"Unknown",
				"reallocatedSectors":0,
				"reserveCapacityPercent":100,
				"scsiCompatId":"slot2",
				"scsiState":"Unknown",
				"securityAtMaximum":false,
				"securityEnabled":false,
				"securityFrozen":false,
				"securityLocked":false,
				"securitySupported":false,
				"serial":"slot2",
				"size":0,
				"slot":2,
				"uuid":"d92f909d-c606-4c27-d17a-4cb6db95a35c",
				"vendor":"Unknown",
				"version":"Unknown"
			 },
			 {
				"canonicalName":"",
				"connected":false,
				"dev":0,
				"devPath":"/dev/slot3",
				"driveType":"Block",
				"lifeRemainingPercent":100,
				"lifetimeReadBytes":0,
				"lifetimeWriteBytes":0,
				"name":"slot3",
				"path":"/dev/slot3",
				"pathLink":"/dev/slot3",
				"powerOnHours":0,
				"product":"Unknown",
				"reallocatedSectors":0,
				"reserveCapacityPercent":100,
				"scsiCompatId":"slot3",
				"scsiState":"Unknown",
				"securityAtMaximum":false,
				"securityEnabled":false,
				"securityFrozen":false,
				"securityLocked":false,
				"securitySupported":false,
				"serial":"slot3",
				"size":0,
				"slot":3,
				"uuid":"25b903d1-3b55-d53f-a556-47b28f91b728",
				"vendor":"Unknown",
				"version":"Unknown"
			 },
			 {
				"canonicalName":"",
				"connected":false,
				"dev":0,
				"devPath":"/dev/slot4",
				"driveType":"Block",
				"lifeRemainingPercent":100,
				"lifetimeReadBytes":0,
				"lifetimeWriteBytes":0,
				"name":"slot4",
				"path":"/dev/slot4",
				"pathLink":"/dev/slot4",
				"powerOnHours":0,
				"product":"Unknown",
				"reallocatedSectors":0,
				"reserveCapacityPercent":100,
				"scsiCompatId":"slot4",
				"scsiState":"Unknown",
				"securityAtMaximum":false,
				"securityEnabled":false,
				"securityFrozen":false,
				"securityLocked":false,
				"securitySupported":false,
				"serial":"slot4",
				"size":0,
				"slot":4,
				"uuid":"76e3d13f-88c5-c334-8f0b-8486964d369e",
				"vendor":"Unknown",
				"version":"Unknown"
			 },
			 {
				"canonicalName":"",
				"connected":false,
				"dev":0,
				"devPath":"/dev/slot5",
				"driveType":"Block",
				"lifeRemainingPercent":100,
				"lifetimeReadBytes":0,
				"lifetimeWriteBytes":0,
				"name":"slot5",
				"path":"/dev/slot5",
				"pathLink":"/dev/slot5",
				"powerOnHours":0,
				"product":"Unknown",
				"reallocatedSectors":0,
				"reserveCapacityPercent":100,
				"scsiCompatId":"slot5",
				"scsiState":"Unknown",
				"securityAtMaximum":false,
				"securityEnabled":false,
				"securityFrozen":false,
				"securityLocked":false,
				"securitySupported":false,
				"serial":"slot5",
				"size":0,
				"slot":5,
				"uuid":"b31123fa-9a17-0ccd-deab-deac32a58371",
				"vendor":"Unknown",
				"version":"Unknown"
			 },
			 {
				"canonicalName":"",
				"connected":false,
				"dev":0,
				"devPath":"/dev/slot6",
				"driveType":"Block",
				"lifeRemainingPercent":100,
				"lifetimeReadBytes":0,
				"lifetimeWriteBytes":0,
				"name":"slot6",
				"path":"/dev/slot6",
				"pathLink":"/dev/slot6",
				"powerOnHours":0,
				"product":"Unknown",
				"reallocatedSectors":0,
				"reserveCapacityPercent":100,
				"scsiCompatId":"slot6",
				"scsiState":"Unknown",
				"securityAtMaximum":false,
				"securityEnabled":false,
				"securityFrozen":false,
				"securityLocked":false,
				"securitySupported":false,
				"serial":"slot6",
				"size":0,
				"slot":6,
				"uuid":"c1b04a69-49a0-fdee-b818-c6cdfafd6cd5",
				"vendor":"Unknown",
				"version":"Unknown"
			 },
			 {
				"canonicalName":"",
				"connected":false,
				"dev":0,
				"devPath":"/dev/slot7",
				"driveType":"Block",
				"lifeRemainingPercent":100,
				"lifetimeReadBytes":0,
				"lifetimeWriteBytes":0,
				"name":"slot7",
				"path":"/dev/slot7",
				"pathLink":"/dev/slot7",
				"powerOnHours":0,
				"product":"Unknown",
				"reallocatedSectors":0,
				"reserveCapacityPercent":100,
				"scsiCompatId":"slot7",
				"scsiState":"Unknown",
				"securityAtMaximum":false,
				"securityEnabled":false,
				"securityFrozen":false,
				"securityLocked":false,
				"securitySupported":false,
				"serial":"slot7",
				"size":0,
				"slot":7,
				"uuid":"76c29a96-68a6-2d8e-6416-392f9fd07919",
				"vendor":"Unknown",
				"version":"Unknown"
			 },
			 {
				"canonicalName":"",
				"connected":false,
				"dev":0,
				"devPath":"/dev/slot8",
				"driveType":"Block",
				"lifeRemainingPercent":100,
				"lifetimeReadBytes":0,
				"lifetimeWriteBytes":0,
				"name":"slot8",
				"path":"/dev/slot8",
				"pathLink":"/dev/slot8",
				"powerOnHours":0,
				"product":"Unknown",
				"reallocatedSectors":0,
				"reserveCapacityPercent":100,
				"scsiCompatId":"slot8",
				"scsiState":"Unknown",
				"securityAtMaximum":false,
				"securityEnabled":false,
				"securityFrozen":false,
				"securityLocked":false,
				"securitySupported":false,
				"serial":"slot8",
				"size":0,
				"slot":8,
				"uuid":"28384068-fdee-1dae-21e3-493558121657",
				"vendor":"Unknown",
				"version":"Unknown"
			 },
			 {
				"canonicalName":"",
				"connected":false,
				"dev":0,
				"devPath":"/dev/slot9",
				"driveType":"Block",
				"lifeRemainingPercent":100,
				"lifetimeReadBytes":0,
				"lifetimeWriteBytes":0,
				"name":"slot9",
				"path":"/dev/slot9",
				"pathLink":"/dev/slot9",
				"powerOnHours":0,
				"product":"Unknown",
				"reallocatedSectors":0,
				"reserveCapacityPercent":100,
				"scsiCompatId":"slot9",
				"scsiState":"Unknown",
				"securityAtMaximum":false,
				"securityEnabled":false,
				"securityFrozen":false,
				"securityLocked":false,
				"securitySupported":false,
				"serial":"slot9",
				"size":0,
				"slot":9,
				"uuid":"612e2106-7032-850a-a16d-4980b53ffb23",
				"vendor":"Unknown",
				"version":"Unknown"
			 },
			 {
				"canonicalName":"",
				"connected":false,
				"dev":0,
				"devPath":"/dev/slot10",
				"driveType":"Block",
				"lifeRemainingPercent":100,
				"lifetimeReadBytes":0,
				"lifetimeWriteBytes":0,
				"name":"slot10",
				"path":"/dev/slot10",
				"pathLink":"/dev/slot10",
				"powerOnHours":0,
				"product":"Unknown",
				"reallocatedSectors":0,
				"reserveCapacityPercent":100,
				"scsiCompatId":"slot10",
				"scsiState":"Unknown",
				"securityAtMaximum":false,
				"securityEnabled":false,
				"securityFrozen":false,
				"securityLocked":false,
				"securitySupported":false,
				"serial":"slot10",
				"size":0,
				"slot":10,
				"uuid":"9d62ad9e-a097-d5d6-d4f7-1d27193270a1",
				"vendor":"Unknown",
				"version":"Unknown"
			 }
		  ],
		  "fibreChannelPorts":[

		  ],
		  "fileSystemUsage":{

		  },
		  "hardwareConfig":null,
		  "kernelCrashDumpState":"DisabledByPlatform",
		  "memory":{
			 "firmware_":{
				"date":"09/21/2015",
				"description":"BIOS",
				"physid":"0",
				"size":"91680",
				"vendor":"Phoenix Technologies LTD",
				"version":"6.00"
			 },
			 "memory_DMI:01A2":{
				"description":"System Memory",
				"physid":"1a2",
				"size":"8589934592",
				"slot":"System board or motherboard"
			 }
		  },
		  "network":{
			 "network_PCI:0000:03:00.0":{
				"businfo":"pci@0000:03:00.0",
				"capacity":"1000000000",
				"clock":"33000000",
				"description":"Ethernet interface",
				"logicalname":"eth0",
				"physid":"0",
				"product":"VMXNET3 Ethernet Controller",
				"serial":"00:50:56:b3:59:f6",
				"vendor":"VMware",
				"version":"01",
				"width":"32"
			 },
			 "network_PCI:0000:0b:00.0":{
				"businfo":"pci@0000:0b:00.0",
				"capacity":"1000000000",
				"clock":"33000000",
				"description":"Ethernet interface",
				"logicalname":"eth1",
				"physid":"0",
				"product":"VMXNET3 Ethernet Controller",
				"serial":"00:50:56:b3:59:f6",
				"vendor":"VMware",
				"version":"01",
				"width":"32"
			 },
			 "network_PCI:0000:13:00.0":{
				"businfo":"pci@0000:13:00.0",
				"capacity":"1000000000",
				"clock":"33000000",
				"description":"Ethernet interface",
				"logicalname":"eth2",
				"physid":"0",
				"product":"VMXNET3 Ethernet Controller",
				"serial":"00:50:56:b3:5c:1d",
				"vendor":"VMware",
				"version":"01",
				"width":"32"
			 },
			 "network_PCI:0000:1b:00.0":{
				"businfo":"pci@0000:1b:00.0",
				"capacity":"1000000000",
				"clock":"33000000",
				"description":"Ethernet interface",
				"logicalname":"eth3",
				"physid":"0",
				"product":"VMXNET3 Ethernet Controller",
				"serial":"00:50:56:b3:5c:1d",
				"vendor":"VMware",
				"version":"01",
				"width":"32"
			 }
		  },
		  "networkInterfaces":{
			 "Bond10G":{
				"isConfigured":true,
				"isUp":true
			 },
			 "Bond1G":{
				"isConfigured":true,
				"isUp":true
			 },
			 "eth0":{
				"isConfigured":true,
				"isUp":true
			 },
			 "eth1":{
				"isConfigured":true,
				"isUp":true
			 },
			 "eth2":{
				"isConfigured":true,
				"isUp":true
			 },
			 "eth3":{
				"isConfigured":true,
				"isUp":true
			 }
		  },
		  "nvram":{
			 "info":"No device found",
			 "raw":"No device found",
			 "status":"Error",
			 "version":"1.0"
		  },
		  "origin":null,
		  "platform":{
			 "chassisType":"SFVIRT",
			 "cpuModel":"Intel(R) Xeon(R) CPU E5645 @ 2.40GHz",
			 "nodeMemoryGB":4,
			 "nodeType":"SFVIRT"
		  },
		  "serial":"VMware-42 33 d5 76 59 41 85 38-ca c2 68 fd 99 47 17 1b",
		  "storage":{
			 "storage_PCI:0000:02:01.0":{
				"businfo":"pci@0000:02:01.0",
				"clock":"66000000",
				"description":"SATA controller",
				"physid":"1",
				"product":"VMware",
				"vendor":"VMware",
				"version":"00",
				"width":"32"
			 }
		  },
		  "system":{
			 "janode1_DMI:0001":{
				"description":"Computer",
				"product":"VMware Virtual Platform ()",
				"serial":"VMware-42 33 d5 76 59 41 85 38-ca c2 68 fd 99 47 17 1b",
				"vendor":"VMware, Inc.",
				"version":"None",
				"width":"64"
			 },
			 "remoteaccess_":{
				"physid":"1",
				"vendor":"Intel"
			 }
		  },
		  "systemMemory":{
			 "free":3296657408,
			 "total":7964655616,
			 "used":4667998208
		  },
		  "uuid":"4233D576-5941-8538-CAC2-68FD9947171B"
	   }
	}
}"""

RESP_GetIpmiConfig_v9_0 = """{
  "id": null,
  "result": {
    "nodes": [
      {
        "nodeID": 1,
        "result": {
          "ipmiConfig": [
            {
              "sensorName": "Fan1A RPM",
              "uniqueSensorID": "7.1:0x30"
            },
            {
              "sensorName": "Fan1B RPM",
              "uniqueSensorID": "7.1:0x31"
            },
            {
              "sensorName": "Fan2A RPM",
              "uniqueSensorID": "7.1:0x32"
            },
            {
              "sensorName": "Fan2B RPM",
              "uniqueSensorID": "7.1:0x33"
            },
            {
              "sensorName": "Fan3A RPM",
              "uniqueSensorID": "7.1:0x34"
            },
            {
              "sensorName": "Fan3B RPM",
              "uniqueSensorID": "7.1:0x35"
            },
            {
              "sensorName": "Fan4A RPM",
              "uniqueSensorID": "7.1:0x36"
            },
            {
              "sensorName": "Fan4B RPM",
              "uniqueSensorID": "7.1:0x37"
            },
            {
              "sensorName": "Fan5A RPM",
              "uniqueSensorID": "7.1:0x38"
            },
            {
              "sensorName": "Fan5B RPM",
              "uniqueSensorID": "7.1:0x39"
            },
            {
              "sensorName": "Fan6A RPM",
              "uniqueSensorID": "7.1:0x3a"
            },
            {
              "sensorName": "Fan6B RPM",
              "uniqueSensorID": "7.1:0x3b"
            },
            {
              "sensorName": "Fan7A RPM",
              "uniqueSensorID": "7.1:0x3c"
            },
            {
              "sensorName": "Fan7B RPM",
              "uniqueSensorID": "7.1:0x3d"
            },
            {
              "sensorName": "Exhaust Temp",
              "uniqueSensorID": "7.1:0x1"
            },
            {
              "sensorName": "Inlet Temp",
              "uniqueSensorID": "7.1:0x4"
            },
            {
              "sensorName": "PS1",
              "uniqueSensorID": "10.1:0x62"
            },
            {
              "sensorName": "PS2",
              "uniqueSensorID": "10.2:0x63"
            }
          ]
        }
      },
      {
        "nodeID": 2,
        "result": {
          "ipmiConfig": [
            {
              "sensorName": "Fan1A RPM",
              "uniqueSensorID": "7.1:0x30"
            },
            {
              "sensorName": "Fan1B RPM",
              "uniqueSensorID": "7.1:0x31"
            },
            {
              "sensorName": "Fan2A RPM",
              "uniqueSensorID": "7.1:0x32"
            },
            {
              "sensorName": "Fan2B RPM",
              "uniqueSensorID": "7.1:0x33"
            },
            {
              "sensorName": "Fan3A RPM",
              "uniqueSensorID": "7.1:0x34"
            },
            {
              "sensorName": "Fan3B RPM",
              "uniqueSensorID": "7.1:0x35"
            },
            {
              "sensorName": "Fan4A RPM",
              "uniqueSensorID": "7.1:0x36"
            },
            {
              "sensorName": "Fan4B RPM",
              "uniqueSensorID": "7.1:0x37"
            },
            {
              "sensorName": "Fan5A RPM",
              "uniqueSensorID": "7.1:0x38"
            },
            {
              "sensorName": "Fan5B RPM",
              "uniqueSensorID": "7.1:0x39"
            },
            {
              "sensorName": "Fan6A RPM",
              "uniqueSensorID": "7.1:0x3a"
            },
            {
              "sensorName": "Fan6B RPM",
              "uniqueSensorID": "7.1:0x3b"
            },
            {
              "sensorName": "Fan7A RPM",
              "uniqueSensorID": "7.1:0x3c"
            },
            {
              "sensorName": "Fan7B RPM",
              "uniqueSensorID": "7.1:0x3d"
            },
            {
              "sensorName": "Exhaust Temp",
              "uniqueSensorID": "7.1:0x1"
            },
            {
              "sensorName": "Inlet Temp",
              "uniqueSensorID": "7.1:0x4"
            },
            {
              "sensorName": "PS1",
              "uniqueSensorID": "10.1:0x62"
            },
            {
              "sensorName": "PS2",
              "uniqueSensorID": "10.2:0x63"
            }
          ]
        }
      },
      {
        "nodeID": 3,
        "result": {
          "ipmiConfig": [
            {
              "sensorName": "Fan1A RPM",
              "uniqueSensorID": "7.1:0x30"
            },
            {
              "sensorName": "Fan1B RPM",
              "uniqueSensorID": "7.1:0x31"
            },
            {
              "sensorName": "Fan2A RPM",
              "uniqueSensorID": "7.1:0x32"
            },
            {
              "sensorName": "Fan2B RPM",
              "uniqueSensorID": "7.1:0x33"
            },
            {
              "sensorName": "Fan3A RPM",
              "uniqueSensorID": "7.1:0x34"
            },
            {
              "sensorName": "Fan3B RPM",
              "uniqueSensorID": "7.1:0x35"
            },
            {
              "sensorName": "Fan4A RPM",
              "uniqueSensorID": "7.1:0x36"
            },
            {
              "sensorName": "Fan4B RPM",
              "uniqueSensorID": "7.1:0x37"
            },
            {
              "sensorName": "Fan5A RPM",
              "uniqueSensorID": "7.1:0x38"
            },
            {
              "sensorName": "Fan5B RPM",
              "uniqueSensorID": "7.1:0x39"
            },
            {
              "sensorName": "Fan6A RPM",
              "uniqueSensorID": "7.1:0x3a"
            },
            {
              "sensorName": "Fan6B RPM",
              "uniqueSensorID": "7.1:0x3b"
            },
            {
              "sensorName": "Fan7A RPM",
              "uniqueSensorID": "7.1:0x3c"
            },
            {
              "sensorName": "Fan7B RPM",
              "uniqueSensorID": "7.1:0x3d"
            },
            {
              "sensorName": "Exhaust Temp",
              "uniqueSensorID": "7.1:0x1"
            },
            {
              "sensorName": "Inlet Temp",
              "uniqueSensorID": "7.1:0x4"
            },
            {
              "sensorName": "PS1",
              "uniqueSensorID": "10.1:0x62"
            },
            {
              "sensorName": "PS2",
              "uniqueSensorID": "10.2:0x63"
            }
          ]
        }
      },
      {
        "nodeID": 4,
        "result": {
          "ipmiConfig": [
            {
              "sensorName": "Fan1A RPM",
              "uniqueSensorID": "7.1:0x30"
            },
            {
              "sensorName": "Fan1B RPM",
              "uniqueSensorID": "7.1:0x31"
            },
            {
              "sensorName": "Fan2A RPM",
              "uniqueSensorID": "7.1:0x32"
            },
            {
              "sensorName": "Fan2B RPM",
              "uniqueSensorID": "7.1:0x33"
            },
            {
              "sensorName": "Fan3A RPM",
              "uniqueSensorID": "7.1:0x34"
            },
            {
              "sensorName": "Fan3B RPM",
              "uniqueSensorID": "7.1:0x35"
            },
            {
              "sensorName": "Fan4A RPM",
              "uniqueSensorID": "7.1:0x36"
            },
            {
              "sensorName": "Fan4B RPM",
              "uniqueSensorID": "7.1:0x37"
            },
            {
              "sensorName": "Fan5A RPM",
              "uniqueSensorID": "7.1:0x38"
            },
            {
              "sensorName": "Fan5B RPM",
              "uniqueSensorID": "7.1:0x39"
            },
            {
              "sensorName": "Fan6A RPM",
              "uniqueSensorID": "7.1:0x3a"
            },
            {
              "sensorName": "Fan6B RPM",
              "uniqueSensorID": "7.1:0x3b"
            },
            {
              "sensorName": "Fan7A RPM",
              "uniqueSensorID": "7.1:0x3c"
            },
            {
              "sensorName": "Fan7B RPM",
              "uniqueSensorID": "7.1:0x3d"
            },
            {
              "sensorName": "Exhaust Temp",
              "uniqueSensorID": "7.1:0x1"
            },
            {
              "sensorName": "Inlet Temp",
              "uniqueSensorID": "7.1:0x4"
            },
            {
              "sensorName": "PS1",
              "uniqueSensorID": "10.1:0x62"
            },
            {
              "sensorName": "PS2",
              "uniqueSensorID": "10.2:0x63"
            }
          ]
        }
      }
    ]
  }
}"""

RESP_GetIpmiConfig_v9_1 = """{
   "id":169,
   "result":{
      "nodes":[
         {
            "nodeID":1,
            "result":{
               "ipmiConfig":{
                  "C220M4":[
                     {
                        "sensorName":"Fan1A RPM",
                        "uniqueSensorID":"29.1:0xf"
                     },
                     {
                        "sensorName":"Fan1B RPM",
                        "uniqueSensorID":"29.1:0x10"
                     },
                     {
                        "sensorName":"Fan2A RPM",
                        "uniqueSensorID":"29.2:0x11"
                     },
                     {
                        "sensorName":"Fan2B RPM",
                        "uniqueSensorID":"29.2:0x12"
                     },
                     {
                        "sensorName":"Fan3A RPM",
                        "uniqueSensorID":"29.3:0x13"
                     },
                     {
                        "sensorName":"Fan3B RPM",
                        "uniqueSensorID":"29.3:0x14"
                     },
                     {
                        "sensorName":"Fan4A RPM",
                        "uniqueSensorID":"29.4:0x15"
                     },
                     {
                        "sensorName":"Fan4B RPM",
                        "uniqueSensorID":"29.4:0x16"
                     },
                     {
                        "sensorName":"Fan5A RPM",
                        "uniqueSensorID":"29.5:0x17"
                     },
                     {
                        "sensorName":"Fan5B RPM",
                        "uniqueSensorID":"29.5:0x18"
                     },
                     {
                        "sensorName":"Fan6A RPM",
                        "uniqueSensorID":"29.6:0x19"
                     },
                     {
                        "sensorName":"Fan6B RPM",
                        "uniqueSensorID":"29.6:0x1a"
                     },
                     {
                        "sensorName":"Exhaust Temp",
                        "uniqueSensorID":"7.4:0xd6"
                     },
                     {
                        "sensorName":"Inlet Temp",
                        "uniqueSensorID":"12.1:0x43"
                     },
                     {
                        "sensorName":"PS1",
                        "uniqueSensorID":"10.1:0x26"
                     },
                     {
                        "sensorName":"PS2",
                        "uniqueSensorID":"10.2:0x2c"
                     }
                  ],
                  "R620":[
                     {
                        "sensorName":"Fan1A RPM",
                        "uniqueSensorID":"7.1:0x30"
                     },
                     {
                        "sensorName":"Fan1B RPM",
                        "uniqueSensorID":"7.1:0x31"
                     },
                     {
                        "sensorName":"Fan2A RPM",
                        "uniqueSensorID":"7.1:0x32"
                     },
                     {
                        "sensorName":"Fan2B RPM",
                        "uniqueSensorID":"7.1:0x33"
                     },
                     {
                        "sensorName":"Fan3A RPM",
                        "uniqueSensorID":"7.1:0x34"
                     },
                     {
                        "sensorName":"Fan3B RPM",
                        "uniqueSensorID":"7.1:0x35"
                     },
                     {
                        "sensorName":"Fan4A RPM",
                        "uniqueSensorID":"7.1:0x36"
                     },
                     {
                        "sensorName":"Fan4B RPM",
                        "uniqueSensorID":"7.1:0x37"
                     },
                     {
                        "sensorName":"Fan5A RPM",
                        "uniqueSensorID":"7.1:0x38"
                     },
                     {
                        "sensorName":"Fan5B RPM",
                        "uniqueSensorID":"7.1:0x39"
                     },
                     {
                        "sensorName":"Fan6A RPM",
                        "uniqueSensorID":"7.1:0x3a"
                     },
                     {
                        "sensorName":"Fan6B RPM",
                        "uniqueSensorID":"7.1:0x3b"
                     },
                     {
                        "sensorName":"Fan7A RPM",
                        "uniqueSensorID":"7.1:0x3c"
                     },
                     {
                        "sensorName":"Fan7B RPM",
                        "uniqueSensorID":"7.1:0x3d"
                     },
                     {
                        "sensorName":"Exhaust Temp",
                        "uniqueSensorID":"7.1:0x1"
                     },
                     {
                        "sensorName":"Inlet Temp",
                        "uniqueSensorID":"7.1:0x4"
                     },
                     {
                        "sensorName":"PS1",
                        "uniqueSensorID":"10.1:0x62"
                     },
                     {
                        "sensorName":"PS2",
                        "uniqueSensorID":"10.2:0x63"
                     }
                  ],
                  "R630":[
                     {
                        "sensorName":"Fan1A RPM",
                        "uniqueSensorID":"7.1:0x30"
                     },
                     {
                        "sensorName":"Fan1B RPM",
                        "uniqueSensorID":"7.1:0x31"
                     },
                     {
                        "sensorName":"Fan2A RPM",
                        "uniqueSensorID":"7.1:0x32"
                     },
                     {
                        "sensorName":"Fan2B RPM",
                        "uniqueSensorID":"7.1:0x33"
                     },
                     {
                        "sensorName":"Fan3A RPM",
                        "uniqueSensorID":"7.1:0x34"
                     },
                     {
                        "sensorName":"Fan3B RPM",
                        "uniqueSensorID":"7.1:0x35"
                     },
                     {
                        "sensorName":"Fan4A RPM",
                        "uniqueSensorID":"7.1:0x36"
                     },
                     {
                        "sensorName":"Fan4B RPM",
                        "uniqueSensorID":"7.1:0x37"
                     },
                     {
                        "sensorName":"Fan5A RPM",
                        "uniqueSensorID":"7.1:0x38"
                     },
                     {
                        "sensorName":"Fan5B RPM",
                        "uniqueSensorID":"7.1:0x39"
                     },
                     {
                        "sensorName":"Fan6A RPM",
                        "uniqueSensorID":"7.1:0x3a"
                     },
                     {
                        "sensorName":"Fan6B RPM",
                        "uniqueSensorID":"7.1:0x3b"
                     },
                     {
                        "sensorName":"Fan7A RPM",
                        "uniqueSensorID":"7.1:0x3c"
                     },
                     {
                        "sensorName":"Fan7B RPM",
                        "uniqueSensorID":"7.1:0x3d"
                     },
                     {
                        "sensorName":"Exhaust Temp",
                        "uniqueSensorID":"7.1:0x1"
                     },
                     {
                        "sensorName":"Inlet Temp",
                        "uniqueSensorID":"7.1:0x4"
                     },
                     {
                        "sensorName":"PS1",
                        "uniqueSensorID":"10.1:0x62"
                     },
                     {
                        "sensorName":"PS2",
                        "uniqueSensorID":"10.2:0x63"
                     }
                  ],
                  "SFVIRT":[

                  ],
                  "Unknown":[

                  ]
               }
            }
         }
      ]
   }
}"""

RESP_GetIpmiInfo_v9_0 = """{
  "id": null,
  "result": {
    "nodes": [
      {
        "nodeID": 1,
        "result": {
          "ipmiInfo": {
            "sensors": [
              {
                "entityID": "7.1 (System Board)",
                "sensorID": "0x72",
                "sensorName": "SEL",
                "sensorType": "Event Logging Disabled",
                "uniqueSensorID": "7.1:0x72"
              },
              {
                "assertionsEnabled": [
                  "General Chassis intrusion"
                ],
                "deassertionsEnabled": [
                  "General Chassis intrusion"
                ],
                "entityID": "7.1 (System Board)",
                "sensorID": "0x73",
                "sensorName": "Intrusion",
                "sensorType": "Physical Security",
                "uniqueSensorID": "7.1:0x73"
              },
              {
                "assertionEvents": [],
                "assertionsEnabled": [],
                "deassertionsEnabled": [],
                "entityID": "7.1 (System Board)",
                "eventMessageControl": "Per-threshold",
                "lowerCritical": "720.000",
                "lowerNonCritical": "840.000",
                "maximumSensorRange": "Unspecified",
                "minimumSensorRange": "Unspecified",
                "negativeHysteresis": "120.000",
                "nominalReading": "10080.000",
                "normalMaximum": "23640.000",
                "normalMinimum": "16680.000",
                "positiveHysteresis": "120.000",
                "readableThresholds": "lcr lnc",
                "sensorID": "0x30",
                "sensorName": "Fan1A RPM",
                "sensorReading": "4560 (+/- 120) RPM",
                "sensorType": "Fan",
                "settableThresholds": "",
                "status": "ok",
                "thresholdReadMask": "lcr lnc",
                "uniqueSensorID": "7.1:0x30"
              },
              {
                "assertionEvents": [],
                "assertionsEnabled": [],
                "deassertionsEnabled": [],
                "entityID": "7.1 (System Board)",
                "eventMessageControl": "Per-threshold",
                "lowerCritical": "720.000",
                "lowerNonCritical": "840.000",
                "maximumSensorRange": "Unspecified",
                "minimumSensorRange": "Unspecified",
                "negativeHysteresis": "120.000",
                "nominalReading": "10080.000",
                "normalMaximum": "23640.000",
                "normalMinimum": "16680.000",
                "positiveHysteresis": "120.000",
                "readableThresholds": "lcr lnc",
                "sensorID": "0x32",
                "sensorName": "Fan2A RPM",
                "sensorReading": "4440 (+/- 120) RPM",
                "sensorType": "Fan",
                "settableThresholds": "",
                "status": "ok",
                "thresholdReadMask": "lcr lnc",
                "uniqueSensorID": "7.1:0x32"
              },
              {
                "assertionEvents": [],
                "assertionsEnabled": [],
                "deassertionsEnabled": [],
                "entityID": "7.1 (System Board)",
                "eventMessageControl": "Per-threshold",
                "lowerCritical": "720.000",
                "lowerNonCritical": "840.000",
                "maximumSensorRange": "Unspecified",
                "minimumSensorRange": "Unspecified",
                "negativeHysteresis": "120.000",
                "nominalReading": "10080.000",
                "normalMaximum": "23640.000",
                "normalMinimum": "16680.000",
                "positiveHysteresis": "120.000",
                "readableThresholds": "lcr lnc",
                "sensorID": "0x34",
                "sensorName": "Fan3A RPM",
                "sensorReading": "4680 (+/- 120) RPM",
                "sensorType": "Fan",
                "settableThresholds": "",
                "status": "ok",
                "thresholdReadMask": "lcr lnc",
                "uniqueSensorID": "7.1:0x34"
              },
              {
                "assertionEvents": [],
                "assertionsEnabled": [],
                "deassertionsEnabled": [],
                "entityID": "7.1 (System Board)",
                "eventMessageControl": "Per-threshold",
                "lowerCritical": "720.000",
                "lowerNonCritical": "840.000",
                "maximumSensorRange": "Unspecified",
                "minimumSensorRange": "Unspecified",
                "negativeHysteresis": "120.000",
                "nominalReading": "10080.000",
                "normalMaximum": "23640.000",
                "normalMinimum": "16680.000",
                "positiveHysteresis": "120.000",
                "readableThresholds": "lcr lnc",
                "sensorID": "0x36",
                "sensorName": "Fan4A RPM",
                "sensorReading": "4560 (+/- 120) RPM",
                "sensorType": "Fan",
                "settableThresholds": "",
                "status": "ok",
                "thresholdReadMask": "lcr lnc",
                "uniqueSensorID": "7.1:0x36"
              },
              {
                "assertionEvents": [],
                "assertionsEnabled": [],
                "deassertionsEnabled": [],
                "entityID": "7.1 (System Board)",
                "eventMessageControl": "Per-threshold",
                "lowerCritical": "720.000",
                "lowerNonCritical": "840.000",
                "maximumSensorRange": "Unspecified",
                "minimumSensorRange": "Unspecified",
                "negativeHysteresis": "120.000",
                "nominalReading": "6720.000",
                "normalMaximum": "23640.000",
                "normalMinimum": "16680.000",
                "positiveHysteresis": "120.000",
                "readableThresholds": "lcr lnc",
                "sensorID": "0x38",
                "sensorName": "Fan5A RPM",
                "sensorReading": "4800 (+/- 120) RPM",
                "sensorType": "Fan",
                "settableThresholds": "",
                "status": "ok",
                "thresholdReadMask": "lcr lnc",
                "uniqueSensorID": "7.1:0x38"
              },
              {
                "assertionEvents": [],
                "assertionsEnabled": [],
                "deassertionsEnabled": [],
                "entityID": "7.1 (System Board)",
                "eventMessageControl": "Per-threshold",
                "lowerCritical": "720.000",
                "lowerNonCritical": "840.000",
                "maximumSensorRange": "Unspecified",
                "minimumSensorRange": "Unspecified",
                "negativeHysteresis": "120.000",
                "nominalReading": "6720.000",
                "normalMaximum": "23640.000",
                "normalMinimum": "16680.000",
                "positiveHysteresis": "120.000",
                "readableThresholds": "lcr lnc",
                "sensorID": "0x3a",
                "sensorName": "Fan6A RPM",
                "sensorReading": "4680 (+/- 120) RPM",
                "sensorType": "Fan",
                "settableThresholds": "",
                "status": "ok",
                "thresholdReadMask": "lcr lnc",
                "uniqueSensorID": "7.1:0x3a"
              },
              {
                "assertionEvents": [],
                "assertionsEnabled": [],
                "deassertionsEnabled": [],
                "entityID": "7.1 (System Board)",
                "eventMessageControl": "Per-threshold",
                "lowerCritical": "-7.000",
                "lowerNonCritical": "3.000",
                "maximumSensorRange": "Unspecified",
                "minimumSensorRange": "Unspecified",
                "negativeHysteresis": "1.000",
                "nominalReading": "23.000",
                "normalMaximum": "69.000",
                "normalMinimum": "11.000",
                "positiveHysteresis": "1.000",
                "readableThresholds": "lcr lnc unc ucr",
                "sensorID": "0x4",
                "sensorName": "Inlet Temp",
                "sensorReading": "22 (+/- 1) degrees C",
                "sensorType": "Temperature",
                "settableThresholds": "lcr lnc unc ucr",
                "status": "ok",
                "thresholdReadMask": "lcr lnc unc ucr",
                "uniqueSensorID": "7.1:0x4",
                "upperCritical": "47.000",
                "upperNonCritical": "42.000"
              },
              {
                "assertionEvents": [],
                "assertionsEnabled": [],
                "entityID": "7.1 (System Board)",
                "eventMessageControl": "Per-threshold",
                "lowerCritical": "3.000",
                "lowerNonCritical": "8.000",
                "maximumSensorRange": "Unspecified",
                "minimumSensorRange": "Unspecified",
                "negativeHysteresis": "1.000",
                "nominalReading": "23.000",
                "normalMaximum": "69.000",
                "normalMinimum": "11.000",
                "positiveHysteresis": "1.000",
                "readableThresholds": "lcr lnc unc ucr",
                "sensorID": "0x1",
                "sensorName": "Exhaust Temp",
                "sensorReading": "38 (+/- 1) degrees C",
                "sensorType": "Temperature",
                "settableThresholds": "",
                "status": "ok",
                "uniqueSensorID": "7.1:0x1",
                "upperCritical": "75.000",
                "upperNonCritical": "70.000"
              },
              {
                "assertionEvents": [],
                "assertionsEnabled": [],
                "entityID": "3.1 (Processor)",
                "eventMessageControl": "Per-threshold",
                "lowerCritical": "3.000",
                "lowerNonCritical": "8.000",
                "maximumSensorRange": "Unspecified",
                "minimumSensorRange": "Unspecified",
                "negativeHysteresis": "1.000",
                "nominalReading": "23.000",
                "normalMaximum": "69.000",
                "normalMinimum": "11.000",
                "positiveHysteresis": "1.000",
                "readableThresholds": "No Thresholds",
                "sensorID": "0xe",
                "sensorName": "Temp",
                "sensorReading": "46 (+/- 1) degrees C",
                "sensorType": "Temperature",
                "settableThresholds": "No Thresholds",
                "status": "ok",
                "uniqueSensorID": "3.1:0xe",
                "upperCritical": "83.000",
                "upperNonCritical": "77.000"
              },
              {
                "assertionEvents": [],
                "assertionsEnabled": [],
                "entityID": "3.2 (Processor)",
                "eventMessageControl": "Per-threshold",
                "lowerCritical": "3.000",
                "lowerNonCritical": "8.000",
                "maximumSensorRange": "Unspecified",
                "minimumSensorRange": "Unspecified",
                "negativeHysteresis": "1.000",
                "nominalReading": "23.000",
                "normalMaximum": "69.000",
                "normalMinimum": "11.000",
                "positiveHysteresis": "1.000",
                "readableThresholds": "No Thresholds",
                "sensorID": "0xf",
                "sensorName": "Temp",
                "sensorReading": "45 (+/- 1) degrees C",
                "sensorType": "Temperature",
                "settableThresholds": "No Thresholds",
                "status": "ok",
                "uniqueSensorID": "3.2:0xf",
                "upperCritical": "83.000",
                "upperNonCritical": "77.000"
              },
              {
                "assertionsEnabled": [
                  "Timer expired",
                  "Hard reset",
                  "Power down",
                  "Power cycle"
                ],
                "deassertionsEnabled": [
                  "Timer expired",
                  "Hard reset",
                  "Power down",
                  "Power cycle"
                ],
                "entityID": "7.1 (System Board)",
                "sensorID": "0x71",
                "sensorName": "OS Watchdog",
                "sensorType": "Watchdog",
                "uniqueSensorID": "7.1:0x71"
              },
              {
                "assertionEvents": [
                  "State Deasserted"
                ],
                "assertionsEnabled": [
                  "State Deasserted",
                  "State Asserted"
                ],
                "deassertionsEnabled": [
                  "State Deasserted",
                  "State Asserted"
                ],
                "entityID": "3.1 (Processor)",
                "sensorID": "0x23",
                "sensorName": "VCORE PG",
                "sensorType": "Voltage",
                "statesAsserted": [
                  "State Deasserted"
                ],
                "uniqueSensorID": "3.1:0x23"
              },
              {
                "assertionEvents": [
                  "State Deasserted"
                ],
                "assertionsEnabled": [
                  "State Deasserted",
                  "State Asserted"
                ],
                "entityID": "3.2 (Processor)",
                "sensorID": "0x24",
                "sensorName": "VCORE PG",
                "sensorType": "Voltage",
                "statesAsserted": [
                  "State Deasserted"
                ],
                "uniqueSensorID": "3.2:0x24"
              },
              {
                "assertionEvents": [
                  "State Deasserted"
                ],
                "assertionsEnabled": [
                  "State Deasserted",
                  "State Asserted"
                ],
                "entityID": "7.1 (System Board)",
                "sensorID": "0x19",
                "sensorName": "3.3V PG",
                "sensorType": "Voltage",
                "statesAsserted": [
                  "State Deasserted"
                ],
                "uniqueSensorID": "7.1:0x19"
              },
              {
                "assertionEvents": [
                  "State Deasserted"
                ],
                "assertionsEnabled": [
                  "State Deasserted",
                  "State Asserted"
                ],
                "entityID": "7.1 (System Board)",
                "sensorID": "0x1a",
                "sensorName": "5V PG",
                "sensorType": "Voltage",
                "statesAsserted": [
                  "State Deasserted"
                ],
                "uniqueSensorID": "7.1:0x1a"
              },
              {
                "assertionEvents": [
                  "Connected"
                ],
                "assertionsEnabled": [
                  "Config Error"
                ],
                "deassertionsEnabled": [
                  "Config Error"
                ],
                "entityID": "7.1 (System Board)",
                "sensorID": "0x50",
                "sensorName": "USB Cable Pres",
                "sensorType": "Cable / Interconnect",
                "statesAsserted": [
                  "Connected"
                ],
                "uniqueSensorID": "7.1:0x50"
              },
              {
                "assertionsEnabled": [
                  "Config Error"
                ],
                "deassertionsEnabled": [
                  "Config Error"
                ],
                "entityID": "7.1 (System Board)",
                "sensorID": "0x51",
                "sensorName": "VGA Cable Pres",
                "sensorType": "Cable / Interconnect",
                "uniqueSensorID": "7.1:0x51"
              },
              {
                "assertionEvents": [
                  "Present"
                ],
                "entityID": "7.1 (System Board)",
                "sensorID": "0x70",
                "sensorName": "Dedicated NIC",
                "sensorType": "Entity Presence",
                "statesAsserted": [
                  "Present"
                ],
                "uniqueSensorID": "7.1:0x70"
              },
              {
                "assertionEvents": [
                  "Absent"
                ],
                "entityID": "11.2 (Add-in Card)",
                "sensorID": "0x49",
                "sensorName": "Presence",
                "sensorType": "Entity Presence",
                "statesAsserted": [
                  "Absent"
                ],
                "uniqueSensorID": "11.2:0x49"
              },
              {
                "assertionEvents": [
                  "Present"
                ],
                "entityID": "3.1 (Processor)",
                "sensorID": "0x40",
                "sensorName": "Presence",
                "sensorType": "Entity Presence",
                "statesAsserted": [
                  "Present"
                ],
                "uniqueSensorID": "3.1:0x40"
              },
              {
                "assertionEvents": [
                  "Present"
                ],
                "entityID": "3.2 (Processor)",
                "sensorID": "0x41",
                "sensorName": "Presence",
                "sensorType": "Entity Presence",
                "statesAsserted": [
                  "Present"
                ],
                "uniqueSensorID": "3.2:0x41"
              },
              {
                "assertionEvents": [
                  "State Deasserted"
                ],
                "assertionsEnabled": [
                  "State Deasserted",
                  "State Asserted"
                ],
                "entityID": "3.2 (Processor)",
                "sensorID": "0x22",
                "sensorName": "PLL PG",
                "sensorType": "Voltage",
                "statesAsserted": [
                  "State Deasserted"
                ],
                "uniqueSensorID": "3.2:0x22"
              },
              {
                "assertionEvents": [
                  "State Deasserted"
                ],
                "assertionsEnabled": [
                  "State Deasserted",
                  "State Asserted"
                ],
                "entityID": "3.1 (Processor)",
                "sensorID": "0x25",
                "sensorName": "PLL PG",
                "sensorType": "Voltage",
                "statesAsserted": [
                  "State Deasserted"
                ],
                "uniqueSensorID": "3.1:0x25"
              },
              {
                "assertionEvents": [
                  "State Deasserted"
                ],
                "assertionsEnabled": [
                  "State Deasserted",
                  "State Asserted"
                ],
                "entityID": "7.1 (System Board)",
                "sensorID": "0x27",
                "sensorName": "1.1V PG",
                "sensorType": "Voltage",
                "statesAsserted": [
                  "State Deasserted"
                ],
                "uniqueSensorID": "7.1:0x27"
              },
              {
                "assertionEvents": [
                  "State Deasserted"
                ],
                "assertionsEnabled": [
                  "State Deasserted",
                  "State Asserted"
                ],
                "entityID": "3.1 (Processor)",
                "sensorID": "0x15",
                "sensorName": "M23 VDDQ PG",
                "sensorType": "Voltage",
                "statesAsserted": [
                  "State Deasserted"
                ],
                "uniqueSensorID": "3.1:0x15"
              },
              {
                "assertionEvents": [
                  "State Deasserted"
                ],
                "assertionsEnabled": [
                  "State Deasserted",
                  "State Asserted"
                ],
                "entityID": "3.1 (Processor)",
                "sensorID": "0x16",
                "sensorName": "M23 VTT PG",
                "sensorType": "Voltage",
                "statesAsserted": [
                  "State Deasserted"
                ],
                "uniqueSensorID": "3.1:0x16"
              },
              {
                "assertionEvents": [
                  "State Deasserted"
                ],
                "assertionsEnabled": [
                  "State Deasserted",
                  "State Asserted"
                ],
                "entityID": "7.1 (System Board)",
                "sensorID": "0x21",
                "sensorName": "FETDRV PG",
                "sensorType": "Voltage",
                "statesAsserted": [
                  "State Deasserted"
                ],
                "uniqueSensorID": "7.1:0x21"
              },
              {
                "assertionEvents": [
                  "Present"
                ],
                "entityID": "10.2 (Power Supply)",
                "sensorID": "0x43",
                "sensorName": "Presence",
                "sensorType": "Entity Presence",
                "statesAsserted": [
                  "Present"
                ],
                "uniqueSensorID": "10.2:0x43"
              },
              {
                "assertionEvents": [
                  "State Deasserted"
                ],
                "assertionsEnabled": [
                  "State Deasserted",
                  "State Asserted"
                ],
                "entityID": "3.2 (Processor)",
                "sensorID": "0x29",
                "sensorName": "VSA PG",
                "sensorType": "Voltage",
                "statesAsserted": [
                  "State Deasserted"
                ],
                "uniqueSensorID": "3.2:0x29"
              },
              {
                "assertionEvents": [
                  "State Deasserted"
                ],
                "assertionsEnabled": [
                  "State Deasserted",
                  "State Asserted"
                ],
                "entityID": "3.1 (Processor)",
                "sensorID": "0x2b",
                "sensorName": "VSA PG",
                "sensorType": "Voltage",
                "statesAsserted": [
                  "State Deasserted"
                ],
                "uniqueSensorID": "3.1:0x2b"
              },
              {
                "assertionEvents": [
                  "State Deasserted"
                ],
                "assertionsEnabled": [
                  "State Deasserted",
                  "State Asserted"
                ],
                "entityID": "3.2 (Processor)",
                "sensorID": "0x1b",
                "sensorName": "M01 VDDQ PG",
                "sensorType": "Voltage",
                "statesAsserted": [
                  "State Deasserted"
                ],
                "uniqueSensorID": "3.2:0x1b"
              },
              {
                "assertionEvents": [
                  "State Deasserted"
                ],
                "assertionsEnabled": [
                  "State Deasserted",
                  "State Asserted"
                ],
                "entityID": "3.1 (Processor)",
                "sensorID": "0x1e",
                "sensorName": "M01 VDDQ PG",
                "sensorType": "Voltage",
                "statesAsserted": [
                  "State Deasserted"
                ],
                "uniqueSensorID": "3.1:0x1e"
              },
              {
                "assertionEvents": [
                  "State Deasserted"
                ],
                "assertionsEnabled": [
                  "State Deasserted",
                  "State Asserted"
                ],
                "entityID": "3.2 (Processor)",
                "sensorID": "0x2e",
                "sensorName": "M23 VTT PG",
                "sensorType": "Voltage",
                "statesAsserted": [
                  "State Deasserted"
                ],
                "uniqueSensorID": "3.2:0x2e"
              },
              {
                "assertionEvents": [
                  "State Deasserted"
                ],
                "assertionsEnabled": [
                  "State Deasserted",
                  "State Asserted"
                ],
                "entityID": "3.2 (Processor)",
                "sensorID": "0x1c",
                "sensorName": "M01 VTT PG",
                "sensorType": "Voltage",
                "statesAsserted": [
                  "State Deasserted"
                ],
                "uniqueSensorID": "3.2:0x1c"
              },
              {
                "assertionEvents": [
                  "State Deasserted"
                ],
                "assertionsEnabled": [
                  "State Deasserted",
                  "State Asserted"
                ],
                "entityID": "7.1 (System Board)",
                "sensorID": "0x2f",
                "sensorName": "NDC PG",
                "sensorType": "Voltage",
                "statesAsserted": [
                  "State Deasserted"
                ],
                "uniqueSensorID": "7.1:0x2f"
              },
              {
                "entityID": "7.1 (System Board)",
                "sensorID": "0x4c",
                "sensorName": "LCD Cable Pres",
                "sensorType": "Cable / Interconnect",
                "uniqueSensorID": "7.1:0x4c"
              },
              {
                "assertionEvents": [
                  "State Deasserted"
                ],
                "assertionsEnabled": [
                  "State Deasserted",
                  "State Asserted"
                ],
                "entityID": "3.2 (Processor)",
                "sensorID": "0x1f",
                "sensorName": "VTT PG",
                "sensorType": "Voltage",
                "statesAsserted": [
                  "State Deasserted"
                ],
                "uniqueSensorID": "3.2:0x1f"
              },
              {
                "assertionEvents": [
                  "State Deasserted"
                ],
                "assertionsEnabled": [
                  "State Deasserted",
                  "State Asserted"
                ],
                "entityID": "3.1 (Processor)",
                "sensorID": "0x20",
                "sensorName": "VTT PG",
                "sensorType": "Voltage",
                "statesAsserted": [
                  "State Deasserted"
                ],
                "uniqueSensorID": "3.1:0x20"
              },
              {
                "assertionEvents": [
                  "State Deasserted"
                ],
                "assertionsEnabled": [
                  "State Deasserted",
                  "State Asserted"
                ],
                "entityID": "3.2 (Processor)",
                "sensorID": "0x1d",
                "sensorName": "M23 VDDQ PG",
                "sensorType": "Voltage",
                "statesAsserted": [
                  "State Deasserted"
                ],
                "uniqueSensorID": "3.2:0x1d"
              },
              {
                "assertionEvents": [
                  "Present"
                ],
                "assertionsEnabled": [
                  "Present",
                  "Absent"
                ],
                "entityID": "11.1 (Add-in Card)",
                "sensorID": "0x4a",
                "sensorName": "Presence",
                "sensorType": "Entity Presence",
                "statesAsserted": [
                  "Present"
                ],
                "uniqueSensorID": "11.1:0x4a"
              },
              {
                "assertionEvents": [
                  "Absent"
                ],
                "entityID": "11.3 (Add-in Card)",
                "sensorID": "0x48",
                "sensorName": "Presence",
                "sensorType": "Entity Presence",
                "statesAsserted": [
                  "Absent"
                ],
                "uniqueSensorID": "11.3:0x48"
              },
              {
                "assertionEvents": [
                  "Presence detected"
                ],
                "assertionsEnabled": [
                  "IERR",
                  "Thermal Trip",
                  "Configuration Error",
                  "Presence detected",
                  "Throttled"
                ],
                "deassertionsEnabled": [
                  "IERR",
                  "Thermal Trip",
                  "Configuration Error",
                  "Presence detected",
                  "Throttled"
                ],
                "entityID": "3.1 (Processor)",
                "sensorID": "0x60",
                "sensorName": "Status",
                "sensorType": "Processor",
                "statesAsserted": [
                  "Presence detected"
                ],
                "uniqueSensorID": "3.1:0x60"
              },
              {
                "assertionEvents": [
                  "Presence detected"
                ],
                "assertionsEnabled": [
                  "IERR",
                  "Thermal Trip",
                  "Configuration Error",
                  "Throttled"
                ],
                "deassertionsEnabled": [
                  "IERR",
                  "Thermal Trip",
                  "Configuration Error",
                  "Throttled"
                ],
                "entityID": "3.2 (Processor)",
                "sensorID": "0x61",
                "sensorName": "Status",
                "sensorType": "Processor",
                "statesAsserted": [
                  "Presence detected"
                ],
                "uniqueSensorID": "3.2:0x61"
              },
              {
                "assertionEvents": [
                  "Fully Redundant"
                ],
                "assertionsEnabled": [
                  "Fully Redundant",
                  "Redundancy Lost"
                ],
                "entityID": "7.1 (System Board)",
                "sensorID": "0x75",
                "sensorName": "Fan Redundancy",
                "sensorType": "Fan",
                "statesAsserted": [
                  "Fully Redundant"
                ],
                "uniqueSensorID": "7.1:0x75"
              },
              {
                "assertionEvents": [
                  "Connected"
                ],
                "assertionsEnabled": [
                  "Config Error"
                ],
                "deassertionsEnabled": [
                  "Config Error"
                ],
                "entityID": "7.1 (System Board)",
                "sensorID": "0x64",
                "sensorName": "Riser Config Err",
                "sensorType": "Cable / Interconnect",
                "statesAsserted": [
                  "Connected"
                ],
                "uniqueSensorID": "7.1:0x64"
              },
              {
                "assertionEvents": [
                  "Connected"
                ],
                "assertionsEnabled": [
                  "Config Error"
                ],
                "deassertionsEnabled": [
                  "Config Error"
                ],
                "entityID": "7.1 (System Board)",
                "sensorID": "0x4f",
                "sensorName": "Riser 3 Presence",
                "sensorType": "Cable / Interconnect",
                "statesAsserted": [
                  "Connected"
                ],
                "uniqueSensorID": "7.1:0x4f"
              },
              {
                "assertionEvents": [
                  "State Deasserted"
                ],
                "assertionsEnabled": [
                  "State Deasserted",
                  "State Asserted"
                ],
                "entityID": "7.1 (System Board)",
                "sensorID": "0x28",
                "sensorName": "1.5V PG",
                "sensorType": "Voltage",
                "statesAsserted": [
                  "State Deasserted"
                ],
                "uniqueSensorID": "7.1:0x28"
              },
              {
                "assertionEvents": [
                  "State Deasserted"
                ],
                "assertionsEnabled": [
                  "State Deasserted",
                  "State Asserted"
                ],
                "entityID": "7.1 (System Board)",
                "sensorID": "0x2c",
                "sensorName": "PS2 PG Fail",
                "sensorType": "Voltage",
                "statesAsserted": [
                  "State Deasserted"
                ],
                "uniqueSensorID": "7.1:0x2c"
              },
              {
                "assertionEvents": [
                  "State Deasserted"
                ],
                "assertionsEnabled": [
                  "State Deasserted",
                  "State Asserted"
                ],
                "entityID": "7.1 (System Board)",
                "sensorID": "0x2d",
                "sensorName": "PS1 PG Fail",
                "sensorType": "Voltage",
                "statesAsserted": [
                  "State Deasserted"
                ],
                "uniqueSensorID": "7.1:0x2d"
              },
              {
                "assertionEvents": [
                  "State Deasserted"
                ],
                "assertionsEnabled": [
                  "State Deasserted",
                  "State Asserted"
                ],
                "entityID": "7.1 (System Board)",
                "sensorID": "0xf6",
                "sensorName": "BP1 5V PG",
                "sensorType": "Voltage",
                "statesAsserted": [
                  "State Deasserted"
                ],
                "uniqueSensorID": "7.1:0xf6"
              },
              {
                "assertionEvents": [
                  "State Deasserted"
                ],
                "assertionsEnabled": [
                  "State Deasserted",
                  "State Asserted"
                ],
                "entityID": "7.1 (System Board)",
                "sensorID": "0xf7",
                "sensorName": "BP2 5V PG",
                "sensorType": "Voltage",
                "uniqueSensorID": "7.1:0xf7"
              },
              {
                "assertionEvents": [
                  "State Deasserted"
                ],
                "assertionsEnabled": [
                  "State Deasserted",
                  "State Asserted"
                ],
                "entityID": "3.1 (Processor)",
                "sensorID": "0x14",
                "sensorName": "M01 VTT PG",
                "sensorType": "Voltage",
                "statesAsserted": [
                  "State Deasserted"
                ],
                "uniqueSensorID": "3.1:0x14"
              },
              {
                "assertionEvents": [
                  "Present"
                ],
                "entityID": "10.1 (Power Supply)",
                "sensorID": "0x42",
                "sensorName": "Presence",
                "sensorType": "Entity Presence",
                "statesAsserted": [
                  "Present"
                ],
                "uniqueSensorID": "10.1:0x42"
              },
              {
                "assertionsEnabled": [
                  "NMI/Diag Interrupt",
                  "Bus Timeout"
                ],
                "deassertionsEnabled": [
                  "NMI/Diag Interrupt",
                  "Bus Timeout"
                ],
                "entityID": "7.1 (System Board)",
                "sensorID": "0x90",
                "sensorName": "PCIe Slot1",
                "sensorType": "Critical Interrupt",
                "uniqueSensorID": "7.1:0x90"
              },
              {
                "assertionsEnabled": [
                  "NMI/Diag Interrupt",
                  "Bus Timeout"
                ],
                "deassertionsEnabled": [
                  "NMI/Diag Interrupt",
                  "Bus Timeout"
                ],
                "entityID": "7.1 (System Board)",
                "sensorID": "0x91",
                "sensorName": "PCIe Slot2",
                "sensorType": "Critical Interrupt",
                "uniqueSensorID": "7.1:0x91"
              },
              {
                "assertionsEnabled": [
                  "NMI/Diag Interrupt",
                  "Bus Timeout"
                ],
                "deassertionsEnabled": [
                  "NMI/Diag Interrupt",
                  "Bus Timeout"
                ],
                "entityID": "7.1 (System Board)",
                "sensorID": "0x92",
                "sensorName": "PCIe Slot3",
                "sensorType": "Critical Interrupt",
                "uniqueSensorID": "7.1:0x92"
              },
              {
                "assertionsEnabled": [
                  "NMI/Diag Interrupt",
                  "Bus Timeout"
                ],
                "deassertionsEnabled": [
                  "NMI/Diag Interrupt",
                  "Bus Timeout"
                ],
                "entityID": "7.1 (System Board)",
                "sensorID": "0x93",
                "sensorName": "PCIe Slot4",
                "sensorType": "Critical Interrupt",
                "uniqueSensorID": "7.1:0x93"
              },
              {
                "assertionsEnabled": [
                  "NMI/Diag Interrupt",
                  "Bus Timeout"
                ],
                "deassertionsEnabled": [
                  "NMI/Diag Interrupt",
                  "Bus Timeout"
                ],
                "entityID": "7.1 (System Board)",
                "sensorID": "0x94",
                "sensorName": "PCIe Slot5",
                "sensorType": "Critical Interrupt",
                "uniqueSensorID": "7.1:0x94"
              },
              {
                "assertionsEnabled": [
                  "NMI/Diag Interrupt",
                  "Bus Timeout"
                ],
                "deassertionsEnabled": [
                  "NMI/Diag Interrupt",
                  "Bus Timeout"
                ],
                "entityID": "7.1 (System Board)",
                "sensorID": "0x95",
                "sensorName": "PCIe Slot6",
                "sensorType": "Critical Interrupt",
                "uniqueSensorID": "7.1:0x95"
              },
              {
                "assertionsEnabled": [
                  "NMI/Diag Interrupt",
                  "Bus Timeout"
                ],
                "deassertionsEnabled": [
                  "NMI/Diag Interrupt",
                  "Bus Timeout"
                ],
                "entityID": "7.1 (System Board)",
                "sensorID": "0x96",
                "sensorName": "PCIe Slot7",
                "sensorType": "Critical Interrupt",
                "uniqueSensorID": "7.1:0x96"
              },
              {
                "entityID": "0.1 (Unspecified)",
                "sensorID": "0xfa",
                "sensorName": "vFlash",
                "sensorType": "Module / Board",
                "uniqueSensorID": "0.1:0xfa"
              },
              {
                "assertionsEnabled": [
                  "Failed"
                ],
                "deassertionsEnabled": [
                  "Failed"
                ],
                "entityID": "7.1 (System Board)",
                "sensorID": "0x65",
                "sensorName": "CMOS Battery",
                "sensorType": "Battery",
                "uniqueSensorID": "7.1:0x65"
              },
              {
                "assertionsEnabled": [
                  "Failed"
                ],
                "deassertionsEnabled": [
                  "Failed"
                ],
                "entityID": "11.2 (Add-in Card)",
                "eventStatus": "Unavailable",
                "sensorID": "0x68",
                "sensorName": "ROMB Battery",
                "sensorType": "Battery",
                "uniqueSensorID": "11.2:0x68"
              },
              {
                "assertionsEnabled": [
                  "Failed"
                ],
                "deassertionsEnabled": [
                  "Failed"
                ],
                "entityID": "11.4 (Add-in Card)",
                "eventStatus": "Unavailable",
                "sensorID": "0x69",
                "sensorName": "ROMB Battery",
                "sensorType": "Battery",
                "uniqueSensorID": "11.4:0x69"
              },
              {
                "assertionEvents": [
                  "Present"
                ],
                "entityID": "26.1 (Disk Drive Bay)",
                "sensorID": "0x54",
                "sensorName": "Presence",
                "sensorType": "Entity Presence",
                "statesAsserted": [
                  "Present"
                ],
                "uniqueSensorID": "26.1:0x54"
              },
              {
                "assertionEvents": [
                  "Absent"
                ],
                "entityID": "26.2 (Disk Drive Bay)",
                "sensorID": "0x55",
                "sensorName": "Presence",
                "sensorType": "Entity Presence",
                "statesAsserted": [
                  "Absent"
                ],
                "uniqueSensorID": "26.2:0x55"
              },
              {
                "assertionEvents": [],
                "assertionsEnabled": [],
                "entityID": "10.1 (Power Supply)",
                "eventMessageControl": "Per-threshold",
                "maximumSensorRange": "Unspecified",
                "minimumSensorRange": "Unspecified",
                "negativeHysteresis": "Unspecified",
                "nominalReading": "0.000",
                "normalMaximum": "0.000",
                "positiveHysteresis": "Unspecified",
                "readableThresholds": "No Thresholds",
                "sensorID": "0x6a",
                "sensorName": "Current 1",
                "sensorReading": "1 (+/- 0) Amps",
                "sensorType": "Current",
                "settableThresholds": "No Thresholds",
                "status": "ok",
                "uniqueSensorID": "10.1:0x6a"
              },
              {
                "assertionEvents": [],
                "assertionsEnabled": [],
                "entityID": "10.2 (Power Supply)",
                "eventMessageControl": "Per-threshold",
                "maximumSensorRange": "Unspecified",
                "minimumSensorRange": "Unspecified",
                "negativeHysteresis": "Unspecified",
                "nominalReading": "0.000",
                "normalMaximum": "0.000",
                "positiveHysteresis": "Unspecified",
                "readableThresholds": "No Thresholds",
                "sensorID": "0x6b",
                "sensorName": "Current 2",
                "sensorReading": "0 (+/- 0) Amps",
                "sensorType": "Current",
                "settableThresholds": "No Thresholds",
                "status": "ok",
                "uniqueSensorID": "10.2:0x6b"
              },
              {
                "assertionEvents": [],
                "assertionsEnabled": [],
                "entityID": "10.1 (Power Supply)",
                "eventMessageControl": "Per-threshold",
                "maximumSensorRange": "Unspecified",
                "minimumSensorRange": "Unspecified",
                "negativeHysteresis": "Unspecified",
                "nominalReading": "0.000",
                "normalMaximum": "0.000",
                "positiveHysteresis": "Unspecified",
                "readableThresholds": "No Thresholds",
                "sensorID": "0x6c",
                "sensorName": "Voltage 1",
                "sensorReading": "118 (+/- 0) Volts",
                "sensorType": "Voltage",
                "settableThresholds": "No Thresholds",
                "status": "ok",
                "uniqueSensorID": "10.1:0x6c"
              },
              {
                "assertionEvents": [],
                "assertionsEnabled": [],
                "entityID": "10.2 (Power Supply)",
                "eventMessageControl": "Per-threshold",
                "maximumSensorRange": "Unspecified",
                "minimumSensorRange": "Unspecified",
                "negativeHysteresis": "Unspecified",
                "nominalReading": "0.000",
                "normalMaximum": "0.000",
                "positiveHysteresis": "Unspecified",
                "readableThresholds": "No Thresholds",
                "sensorID": "0x6d",
                "sensorName": "Voltage 2",
                "sensorReading": "118 (+/- 0) Volts",
                "sensorType": "Voltage",
                "settableThresholds": "No Thresholds",
                "status": "ok",
                "uniqueSensorID": "10.2:0x6d"
              },
              {
                "assertionEvents": [
                  "Fully Redundant"
                ],
                "assertionsEnabled": [
                  "Fully Redundant",
                  "Redundancy Lost"
                ],
                "entityID": "7.1 (System Board)",
                "sensorID": "0x74",
                "sensorName": "PS Redundancy",
                "sensorType": "Power Supply",
                "statesAsserted": [
                  "Fully Redundant"
                ],
                "uniqueSensorID": "7.1:0x74"
              },
              {
                "assertionEvents": [
                  "Presence detected"
                ],
                "assertionsEnabled": [
                  "Presence detected",
                  "Failure detected",
                  "Predictive failure",
                  "Power Supply AC lost",
                  "Config Error: Vendor Mismatch",
                  "Config Error: Revision Mismatch",
                  "Config Error: Processor Missing",
                  "Config Error"
                ],
                "deassertionsEnabled": [
                  "Presence detected",
                  "Failure detected",
                  "Predictive failure",
                  "Power Supply AC lost",
                  "Config Error: Vendor Mismatch",
                  "Config Error: Revision Mismatch",
                  "Config Error: Processor Missing",
                  "Config Error"
                ],
                "entityID": "10.1 (Power Supply)",
                "sensorID": "0x62",
                "sensorName": "Status",
                "sensorType": "Power Supply",
                "statesAsserted": [
                  "Presence detected"
                ],
                "uniqueSensorID": "10.1:0x62"
              },
              {
                "assertionEvents": [
                  "Presence detected"
                ],
                "assertionsEnabled": [
                  "Presence detected",
                  "Failure detected",
                  "Predictive failure",
                  "Power Supply AC lost",
                  "Config Error: Vendor Mismatch",
                  "Config Error: Revision Mismatch",
                  "Config Error: Processor Missing",
                  "Config Error"
                ],
                "deassertionsEnabled": [
                  "Presence detected",
                  "Failure detected",
                  "Predictive failure",
                  "Power Supply AC lost",
                  "Config Error: Vendor Mismatch",
                  "Config Error: Revision Mismatch",
                  "Config Error: Processor Missing",
                  "Config Error"
                ],
                "entityID": "10.2 (Power Supply)",
                "sensorID": "0x63",
                "sensorName": "Status",
                "sensorType": "Power Supply",
                "statesAsserted": [
                  "Presence detected"
                ],
                "uniqueSensorID": "10.2:0x63"
              },
              {
                "assertionEvents": [],
                "assertionsEnabled": [],
                "deassertionsEnabled": [],
                "entityID": "7.1 (System Board)",
                "eventMessageControl": "Per-threshold",
                "maximumSensorRange": "3556.000",
                "minimumSensorRange": "Unspecified",
                "negativeHysteresis": "Unspecified",
                "nominalReading": "658.000",
                "normalMaximum": "672.000",
                "positiveHysteresis": "Unspecified",
                "readableThresholds": "unc ucr",
                "sensorID": "0x77",
                "sensorName": "Pwr Consumption",
                "sensorReading": "126 (+/- 0) Watts",
                "sensorType": "Current",
                "settableThresholds": "unc",
                "status": "ok",
                "uniqueSensorID": "7.1:0x77",
                "upperCritical": "1218.000",
                "upperNonCritical": "1106.000"
              },
              {
                "assertionEvents": [
                  "OEM Specific"
                ],
                "assertionsEnabled": [],
                "deassertionsEnabled": [],
                "entityID": "7.1 (System Board)",
                "sensorID": "0x76",
                "sensorName": "Power Optimized",
                "sensorType": "Unknown (0xC0)",
                "statesAsserted": [
                  "OEM Specific"
                ],
                "uniqueSensorID": "7.1:0x76"
              },
              {
                "entityID": "11.3 (Add-in Card)",
                "sensorID": "0xf4",
                "sensorName": "SD1",
                "sensorType": "Unknown (0xC9)",
                "uniqueSensorID": "11.3:0xf4"
              },
              {
                "entityID": "11.3 (Add-in Card)",
                "sensorID": "0xf5",
                "sensorName": "SD2",
                "sensorType": "Unknown (0xC9)",
                "uniqueSensorID": "11.3:0xf5"
              },
              {
                "assertionEvents": [
                  "Fully Redundant"
                ],
                "assertionsEnabled": [
                  "Fully Redundant",
                  "Redundancy Lost"
                ],
                "entityID": "11.3 (Add-in Card)",
                "sensorID": "0x78",
                "sensorName": "Redundancy",
                "sensorType": "Unknown (0xC9)",
                "uniqueSensorID": "11.3:0x78"
              },
              {
                "entityID": "34.1 (BIOS)",
                "sensorID": "0x1",
                "sensorName": "ECC Corr Err",
                "sensorType": "Memory",
                "uniqueSensorID": "34.1:0x1"
              },
              {
                "entityID": "34.1 (BIOS)",
                "sensorID": "0x2",
                "sensorName": "ECC Uncorr Err",
                "sensorType": "Memory",
                "uniqueSensorID": "34.1:0x2"
              },
              {
                "entityID": "34.1 (BIOS)",
                "sensorID": "0x3",
                "sensorName": "I/O Channel Chk",
                "sensorType": "Critical Interrupt",
                "uniqueSensorID": "34.1:0x3"
              },
              {
                "entityID": "34.1 (BIOS)",
                "sensorID": "0x4",
                "sensorName": "PCI Parity Err",
                "sensorType": "Critical Interrupt",
                "uniqueSensorID": "34.1:0x4"
              },
              {
                "entityID": "34.1 (BIOS)",
                "sensorID": "0x5",
                "sensorName": "PCI System Err",
                "sensorType": "Critical Interrupt",
                "uniqueSensorID": "34.1:0x5"
              },
              {
                "entityID": "34.1 (BIOS)",
                "sensorID": "0x6",
                "sensorName": "SBE Log Disabled",
                "sensorType": "Event Logging Disabled",
                "uniqueSensorID": "34.1:0x6"
              },
              {
                "entityID": "34.1 (BIOS)",
                "sensorID": "0x7",
                "sensorName": "Logging Disabled",
                "sensorType": "Event Logging Disabled",
                "uniqueSensorID": "34.1:0x7"
              },
              {
                "entityID": "34.1 (BIOS)",
                "sensorID": "0x8",
                "sensorName": "Unknown",
                "sensorType": "System Event",
                "uniqueSensorID": "34.1:0x8"
              },
              {
                "entityID": "34.1 (BIOS)",
                "sensorID": "0xa",
                "sensorName": "CPU Protocol Err",
                "sensorType": "Processor",
                "uniqueSensorID": "34.1:0xa"
              },
              {
                "entityID": "34.1 (BIOS)",
                "sensorID": "0xb",
                "sensorName": "CPU Bus PERR",
                "sensorType": "Processor",
                "uniqueSensorID": "34.1:0xb"
              },
              {
                "entityID": "34.1 (BIOS)",
                "sensorID": "0xc",
                "sensorName": "CPU Init Err",
                "sensorType": "Processor",
                "uniqueSensorID": "34.1:0xc"
              },
              {
                "entityID": "34.1 (BIOS)",
                "sensorID": "0xd",
                "sensorName": "CPU Machine Chk",
                "sensorType": "Processor",
                "uniqueSensorID": "34.1:0xd"
              },
              {
                "entityID": "34.1 (BIOS)",
                "sensorID": "0x11",
                "sensorName": "Memory Spared",
                "sensorType": "Memory",
                "uniqueSensorID": "34.1:0x11"
              },
              {
                "entityID": "34.1 (BIOS)",
                "sensorID": "0x12",
                "sensorName": "Memory Mirrored",
                "sensorType": "Memory",
                "uniqueSensorID": "34.1:0x12"
              },
              {
                "entityID": "34.1 (BIOS)",
                "sensorID": "0x13",
                "sensorName": "Memory RAID",
                "sensorType": "Memory",
                "uniqueSensorID": "34.1:0x13"
              },
              {
                "entityID": "34.1 (BIOS)",
                "sensorID": "0x14",
                "sensorName": "Memory Added",
                "sensorType": "Memory",
                "uniqueSensorID": "34.1:0x14"
              },
              {
                "entityID": "34.1 (BIOS)",
                "sensorID": "0x15",
                "sensorName": "Memory Removed",
                "sensorType": "Memory",
                "uniqueSensorID": "34.1:0x15"
              },
              {
                "entityID": "34.1 (BIOS)",
                "sensorID": "0x16",
                "sensorName": "Memory Cfg Err",
                "sensorType": "Memory",
                "uniqueSensorID": "34.1:0x16"
              },
              {
                "entityID": "34.1 (BIOS)",
                "sensorID": "0x17",
                "sensorName": "Mem Redun Gain",
                "sensorType": "Memory",
                "uniqueSensorID": "34.1:0x17"
              },
              {
                "entityID": "34.1 (BIOS)",
                "sensorID": "0x18",
                "sensorName": "PCIE Fatal Err",
                "sensorType": "Critical Interrupt",
                "uniqueSensorID": "34.1:0x18"
              },
              {
                "entityID": "34.1 (BIOS)",
                "sensorID": "0x19",
                "sensorName": "Chipset Err",
                "sensorType": "Critical Interrupt",
                "uniqueSensorID": "34.1:0x19"
              },
              {
                "entityID": "34.1 (BIOS)",
                "sensorID": "0x1a",
                "sensorName": "Err Reg Pointer",
                "sensorType": "Unknown (0xC1)",
                "uniqueSensorID": "34.1:0x1a"
              },
              {
                "entityID": "34.1 (BIOS)",
                "sensorID": "0x1b",
                "sensorName": "Mem ECC Warning",
                "sensorType": "Memory",
                "uniqueSensorID": "34.1:0x1b"
              },
              {
                "entityID": "34.1 (BIOS)",
                "sensorID": "0x1c",
                "sensorName": "Mem CRC Err",
                "sensorType": "Memory",
                "uniqueSensorID": "34.1:0x1c"
              },
              {
                "entityID": "34.1 (BIOS)",
                "sensorID": "0x1d",
                "sensorName": "USB Over-current",
                "sensorType": "Memory",
                "uniqueSensorID": "34.1:0x1d"
              },
              {
                "entityID": "34.1 (BIOS)",
                "sensorID": "0x1e",
                "sensorName": "POST Err",
                "sensorType": "System Firmwares",
                "uniqueSensorID": "34.1:0x1e"
              },
              {
                "entityID": "34.1 (BIOS)",
                "sensorID": "0x1f",
                "sensorName": "Hdwr version err",
                "sensorType": "Version Change",
                "uniqueSensorID": "34.1:0x1f"
              },
              {
                "entityID": "34.1 (BIOS)",
                "sensorID": "0x20",
                "sensorName": "Mem Overtemp",
                "sensorType": "Memory",
                "uniqueSensorID": "34.1:0x20"
              },
              {
                "entityID": "34.1 (BIOS)",
                "sensorID": "0x21",
                "sensorName": "Mem Fatal SB CRC",
                "sensorType": "Memory",
                "uniqueSensorID": "34.1:0x21"
              },
              {
                "entityID": "34.1 (BIOS)",
                "sensorID": "0x22",
                "sensorName": "Mem Fatal NB CRC",
                "sensorType": "Memory",
                "uniqueSensorID": "34.1:0x22"
              },
              {
                "entityID": "34.1 (BIOS)",
                "sensorID": "0x71",
                "sensorName": "OS Watchdog Time",
                "sensorType": "Watchdog",
                "uniqueSensorID": "34.1:0x71"
              },
              {
                "entityID": "34.1 (BIOS)",
                "sensorID": "0x26",
                "sensorName": "Non Fatal PCI Er",
                "sensorType": "Unknown (0xC2)",
                "uniqueSensorID": "34.1:0x26"
              },
              {
                "entityID": "34.1 (BIOS)",
                "sensorID": "0x27",
                "sensorName": "Fatal IO Error",
                "sensorType": "Unknown (0xC3)",
                "uniqueSensorID": "34.1:0x27"
              },
              {
                "entityID": "34.1 (BIOS)",
                "sensorID": "0x28",
                "sensorName": "MSR Info Log",
                "sensorType": "Unknown (0xC1)",
                "uniqueSensorID": "34.1:0x28"
              },
              {
                "entityID": "34.1 (BIOS)",
                "sensorID": "0x2a",
                "sensorName": "TXT Status",
                "sensorType": "OS Critical Stop",
                "uniqueSensorID": "34.1:0x2a"
              },
              {
                "assertionsEnabled": [
                  "Drive Present",
                  "Drive Fault"
                ],
                "deassertionsEnabled": [
                  "Drive Present",
                  "Drive Fault"
                ],
                "entityID": "7.1 (System Board)",
                "sensorID": "0xa0",
                "sensorName": "Drive 0",
                "sensorType": "Drive Slot / Bay",
                "uniqueSensorID": "7.1:0xa0"
              },
              {
                "assertionEvents": [
                  "Connected"
                ],
                "assertionsEnabled": [
                  "Config Error"
                ],
                "deassertionsEnabled": [
                  "Config Error"
                ],
                "entityID": "26.1 (Disk Drive Bay)",
                "sensorID": "0xe0",
                "sensorName": "Cable SAS A",
                "sensorType": "Cable / Interconnect",
                "statesAsserted": [
                  "Connected"
                ],
                "uniqueSensorID": "26.1:0xe0"
              },
              {
                "assertionEvents": [
                  "Connected"
                ],
                "assertionsEnabled": [
                  "Config Error"
                ],
                "deassertionsEnabled": [
                  "Config Error"
                ],
                "entityID": "26.1 (Disk Drive Bay)",
                "sensorID": "0xe1",
                "sensorName": "Cable SAS B",
                "sensorType": "Cable / Interconnect",
                "statesAsserted": [
                  "Connected"
                ],
                "uniqueSensorID": "26.1:0xe1"
              },
              {
                "assertionsEnabled": [
                  "Config Error"
                ],
                "deassertionsEnabled": [
                  "Config Error"
                ],
                "entityID": "26.1 (Disk Drive Bay)",
                "sensorID": "0xe2",
                "sensorName": "Cable SAS C",
                "sensorType": "Cable / Interconnect",
                "uniqueSensorID": "26.1:0xe2"
              },
              {
                "assertionsEnabled": [
                  "Config Error"
                ],
                "deassertionsEnabled": [
                  "Config Error"
                ],
                "entityID": "26.1 (Disk Drive Bay)",
                "sensorID": "0xe3",
                "sensorName": "Cable SAS D",
                "sensorType": "Cable / Interconnect",
                "uniqueSensorID": "26.1:0xe3"
              },
              {
                "assertionsEnabled": [
                  "Config Error"
                ],
                "deassertionsEnabled": [
                  "Config Error"
                ],
                "entityID": "26.2 (Disk Drive Bay)",
                "sensorID": "0xe4",
                "sensorName": "Cable SAS A",
                "sensorType": "Cable / Interconnect",
                "uniqueSensorID": "26.2:0xe4"
              },
              {
                "assertionsEnabled": [
                  "Config Error"
                ],
                "deassertionsEnabled": [
                  "Config Error"
                ],
                "entityID": "26.2 (Disk Drive Bay)",
                "sensorID": "0xe5",
                "sensorName": "Cable SAS B",
                "sensorType": "Cable / Interconnect",
                "uniqueSensorID": "26.2:0xe5"
              },
              {
                "assertionsEnabled": [
                  "Config Error"
                ],
                "deassertionsEnabled": [
                  "Config Error"
                ],
                "entityID": "26.2 (Disk Drive Bay)",
                "sensorID": "0xe6",
                "sensorName": "Cable SAS C",
                "sensorType": "Cable / Interconnect",
                "uniqueSensorID": "26.2:0xe6"
              },
              {
                "assertionsEnabled": [
                  "Config Error"
                ],
                "deassertionsEnabled": [
                  "Config Error"
                ],
                "entityID": "26.2 (Disk Drive Bay)",
                "sensorID": "0xe7",
                "sensorName": "Cable SAS D",
                "sensorType": "Cable / Interconnect",
                "uniqueSensorID": "26.2:0xe7"
              },
              {
                "assertionEvents": [
                  "Connected"
                ],
                "assertionsEnabled": [
                  "Config Error"
                ],
                "deassertionsEnabled": [
                  "Config Error"
                ],
                "entityID": "26.1 (Disk Drive Bay)",
                "sensorID": "0x58",
                "sensorName": "Power Cable",
                "sensorType": "Cable / Interconnect",
                "statesAsserted": [
                  "Connected"
                ],
                "uniqueSensorID": "26.1:0x58"
              },
              {
                "assertionEvents": [
                  "Connected"
                ],
                "assertionsEnabled": [
                  "Config Error"
                ],
                "deassertionsEnabled": [
                  "Config Error"
                ],
                "entityID": "26.1 (Disk Drive Bay)",
                "sensorID": "0x59",
                "sensorName": "Signal Cable",
                "sensorType": "Cable / Interconnect",
                "statesAsserted": [
                  "Connected"
                ],
                "uniqueSensorID": "26.1:0x59"
              },
              {
                "assertionsEnabled": [
                  "Config Error"
                ],
                "deassertionsEnabled": [
                  "Config Error"
                ],
                "entityID": "26.2 (Disk Drive Bay)",
                "sensorID": "0x5a",
                "sensorName": "Power Cable",
                "sensorType": "Cable / Interconnect",
                "uniqueSensorID": "26.2:0x5a"
              },
              {
                "assertionsEnabled": [
                  "Config Error"
                ],
                "deassertionsEnabled": [
                  "Config Error"
                ],
                "entityID": "26.2 (Disk Drive Bay)",
                "sensorID": "0x5b",
                "sensorName": "Signal Cable",
                "sensorType": "Cable / Interconnect",
                "uniqueSensorID": "26.2:0x5b"
              },
              {
                "assertionEvents": [],
                "assertionsEnabled": [],
                "deassertionsEnabled": [],
                "entityID": "7.1 (System Board)",
                "eventMessageControl": "Per-threshold",
                "lowerCritical": "720.000",
                "lowerNonCritical": "840.000",
                "maximumSensorRange": "Unspecified",
                "minimumSensorRange": "Unspecified",
                "negativeHysteresis": "120.000",
                "nominalReading": "6720.000",
                "normalMaximum": "23640.000",
                "normalMinimum": "16680.000",
                "positiveHysteresis": "120.000",
                "readableThresholds": "lcr lnc",
                "sensorID": "0x3c",
                "sensorName": "Fan7A RPM",
                "sensorReading": "4800 (+/- 120) RPM",
                "sensorType": "Fan",
                "settableThresholds": "",
                "status": "ok",
                "thresholdReadMask": "lcr lnc",
                "uniqueSensorID": "7.1:0x3c"
              },
              {
                "assertionEvents": [],
                "assertionsEnabled": [],
                "deassertionsEnabled": [],
                "entityID": "7.1 (System Board)",
                "eventMessageControl": "Per-threshold",
                "lowerCritical": "720.000",
                "lowerNonCritical": "840.000",
                "maximumSensorRange": "Unspecified",
                "minimumSensorRange": "Unspecified",
                "negativeHysteresis": "120.000",
                "nominalReading": "6720.000",
                "normalMaximum": "23640.000",
                "normalMinimum": "16680.000",
                "positiveHysteresis": "120.000",
                "readableThresholds": "lcr lnc",
                "sensorID": "0x31",
                "sensorName": "Fan1B RPM",
                "sensorReading": "4320 (+/- 120) RPM",
                "sensorType": "Fan",
                "settableThresholds": "",
                "status": "ok",
                "thresholdReadMask": "lcr lnc",
                "uniqueSensorID": "7.1:0x31"
              },
              {
                "assertionEvents": [],
                "assertionsEnabled": [],
                "deassertionsEnabled": [],
                "entityID": "7.1 (System Board)",
                "eventMessageControl": "Per-threshold",
                "lowerCritical": "720.000",
                "lowerNonCritical": "840.000",
                "maximumSensorRange": "Unspecified",
                "minimumSensorRange": "Unspecified",
                "negativeHysteresis": "120.000",
                "nominalReading": "6720.000",
                "normalMaximum": "23640.000",
                "normalMinimum": "16680.000",
                "positiveHysteresis": "120.000",
                "readableThresholds": "lcr lnc",
                "sensorID": "0x33",
                "sensorName": "Fan2B RPM",
                "sensorReading": "4200 (+/- 120) RPM",
                "sensorType": "Fan",
                "settableThresholds": "",
                "status": "ok",
                "thresholdReadMask": "lcr lnc",
                "uniqueSensorID": "7.1:0x33"
              },
              {
                "assertionEvents": [],
                "assertionsEnabled": [],
                "deassertionsEnabled": [],
                "entityID": "7.1 (System Board)",
                "eventMessageControl": "Per-threshold",
                "lowerCritical": "720.000",
                "lowerNonCritical": "840.000",
                "maximumSensorRange": "Unspecified",
                "minimumSensorRange": "Unspecified",
                "negativeHysteresis": "120.000",
                "nominalReading": "6720.000",
                "normalMaximum": "23640.000",
                "normalMinimum": "16680.000",
                "positiveHysteresis": "120.000",
                "readableThresholds": "lcr lnc",
                "sensorID": "0x35",
                "sensorName": "Fan3B RPM",
                "sensorReading": "4320 (+/- 120) RPM",
                "sensorType": "Fan",
                "settableThresholds": "",
                "status": "ok",
                "thresholdReadMask": "lcr lnc",
                "uniqueSensorID": "7.1:0x35"
              },
              {
                "assertionEvents": [],
                "assertionsEnabled": [],
                "deassertionsEnabled": [],
                "entityID": "7.1 (System Board)",
                "eventMessageControl": "Per-threshold",
                "lowerCritical": "720.000",
                "lowerNonCritical": "840.000",
                "maximumSensorRange": "Unspecified",
                "minimumSensorRange": "Unspecified",
                "negativeHysteresis": "120.000",
                "nominalReading": "6720.000",
                "normalMaximum": "23640.000",
                "normalMinimum": "16680.000",
                "positiveHysteresis": "120.000",
                "readableThresholds": "lcr lnc",
                "sensorID": "0x37",
                "sensorName": "Fan4B RPM",
                "sensorReading": "4200 (+/- 120) RPM",
                "sensorType": "Fan",
                "settableThresholds": "",
                "status": "ok",
                "thresholdReadMask": "lcr lnc",
                "uniqueSensorID": "7.1:0x37"
              },
              {
                "assertionEvents": [],
                "assertionsEnabled": [],
                "deassertionsEnabled": [],
                "entityID": "7.1 (System Board)",
                "eventMessageControl": "Per-threshold",
                "lowerCritical": "720.000",
                "lowerNonCritical": "840.000",
                "maximumSensorRange": "Unspecified",
                "minimumSensorRange": "Unspecified",
                "negativeHysteresis": "120.000",
                "nominalReading": "6720.000",
                "normalMaximum": "23640.000",
                "normalMinimum": "16680.000",
                "positiveHysteresis": "120.000",
                "readableThresholds": "lcr lnc",
                "sensorID": "0x39",
                "sensorName": "Fan5B RPM",
                "sensorReading": "4320 (+/- 120) RPM",
                "sensorType": "Fan",
                "settableThresholds": "",
                "status": "ok",
                "thresholdReadMask": "lcr lnc",
                "uniqueSensorID": "7.1:0x39"
              },
              {
                "assertionEvents": [],
                "assertionsEnabled": [],
                "deassertionsEnabled": [],
                "entityID": "7.1 (System Board)",
                "eventMessageControl": "Per-threshold",
                "lowerCritical": "720.000",
                "lowerNonCritical": "840.000",
                "maximumSensorRange": "Unspecified",
                "minimumSensorRange": "Unspecified",
                "negativeHysteresis": "120.000",
                "nominalReading": "6720.000",
                "normalMaximum": "23640.000",
                "normalMinimum": "16680.000",
                "positiveHysteresis": "120.000",
                "readableThresholds": "lcr lnc",
                "sensorID": "0x3b",
                "sensorName": "Fan6B RPM",
                "sensorReading": "4320 (+/- 120) RPM",
                "sensorType": "Fan",
                "settableThresholds": "",
                "status": "ok",
                "thresholdReadMask": "lcr lnc",
                "uniqueSensorID": "7.1:0x3b"
              },
              {
                "assertionEvents": [],
                "assertionsEnabled": [],
                "deassertionsEnabled": [],
                "entityID": "7.1 (System Board)",
                "eventMessageControl": "Per-threshold",
                "lowerCritical": "720.000",
                "lowerNonCritical": "840.000",
                "maximumSensorRange": "Unspecified",
                "minimumSensorRange": "Unspecified",
                "negativeHysteresis": "120.000",
                "nominalReading": "6720.000",
                "normalMaximum": "23640.000",
                "normalMinimum": "16680.000",
                "positiveHysteresis": "120.000",
                "readableThresholds": "lcr lnc",
                "sensorID": "0x3d",
                "sensorName": "Fan7B RPM",
                "sensorReading": "4320 (+/- 120) RPM",
                "sensorType": "Fan",
                "settableThresholds": "",
                "status": "ok",
                "thresholdReadMask": "lcr lnc",
                "uniqueSensorID": "7.1:0x3d"
              },
              {
                "entityID": "7.1 (System Board)",
                "sensorID": "0x66",
                "sensorName": "PFault Fail Safe",
                "sensorType": "Voltage",
                "uniqueSensorID": "7.1:0x66"
              },
              {
                "assertionEvents": [
                  "Presence Detected"
                ],
                "entityID": "32.1 (Memory Device)",
                "sensorID": "0xc0",
                "sensorName": "A",
                "sensorType": "Memory",
                "statesAsserted": [
                  "Presence Detected"
                ],
                "uniqueSensorID": "32.1:0xc0"
              },
              {
                "assertionEvents": [
                  "Presence Detected"
                ],
                "entityID": "32.1 (Memory Device)",
                "sensorID": "0xcc",
                "sensorName": "B",
                "sensorType": "Memory",
                "statesAsserted": [
                  "Presence Detected"
                ],
                "uniqueSensorID": "32.1:0xcc"
              }
            ]
          }
        }
      },
      {
        "nodeID": 2,
        "result": {
          "ipmiInfo": {
            "sensors": [
              {
                "entityID": "7.1 (System Board)",
                "sensorID": "0x72",
                "sensorName": "SEL",
                "sensorType": "Event Logging Disabled",
                "uniqueSensorID": "7.1:0x72"
              },
              {
                "assertionsEnabled": [
                  "General Chassis intrusion"
                ],
                "deassertionsEnabled": [
                  "General Chassis intrusion"
                ],
                "entityID": "7.1 (System Board)",
                "sensorID": "0x73",
                "sensorName": "Intrusion",
                "sensorType": "Physical Security",
                "uniqueSensorID": "7.1:0x73"
              },
              {
                "assertionEvents": [],
                "assertionsEnabled": [],
                "deassertionsEnabled": [],
                "entityID": "7.1 (System Board)",
                "eventMessageControl": "Per-threshold",
                "lowerCritical": "720.000",
                "lowerNonCritical": "840.000",
                "maximumSensorRange": "Unspecified",
                "minimumSensorRange": "Unspecified",
                "negativeHysteresis": "120.000",
                "nominalReading": "10080.000",
                "normalMaximum": "23640.000",
                "normalMinimum": "16680.000",
                "positiveHysteresis": "120.000",
                "readableThresholds": "lcr lnc",
                "sensorID": "0x30",
                "sensorName": "Fan1A RPM",
                "sensorReading": "4800 (+/- 120) RPM",
                "sensorType": "Fan",
                "settableThresholds": "",
                "status": "ok",
                "thresholdReadMask": "lcr lnc",
                "uniqueSensorID": "7.1:0x30"
              },
              {
                "assertionEvents": [],
                "assertionsEnabled": [],
                "deassertionsEnabled": [],
                "entityID": "7.1 (System Board)",
                "eventMessageControl": "Per-threshold",
                "lowerCritical": "720.000",
                "lowerNonCritical": "840.000",
                "maximumSensorRange": "Unspecified",
                "minimumSensorRange": "Unspecified",
                "negativeHysteresis": "120.000",
                "nominalReading": "10080.000",
                "normalMaximum": "23640.000",
                "normalMinimum": "16680.000",
                "positiveHysteresis": "120.000",
                "readableThresholds": "lcr lnc",
                "sensorID": "0x32",
                "sensorName": "Fan2A RPM",
                "sensorReading": "4800 (+/- 120) RPM",
                "sensorType": "Fan",
                "settableThresholds": "",
                "status": "ok",
                "thresholdReadMask": "lcr lnc",
                "uniqueSensorID": "7.1:0x32"
              },
              {
                "assertionEvents": [],
                "assertionsEnabled": [],
                "deassertionsEnabled": [],
                "entityID": "7.1 (System Board)",
                "eventMessageControl": "Per-threshold",
                "lowerCritical": "720.000",
                "lowerNonCritical": "840.000",
                "maximumSensorRange": "Unspecified",
                "minimumSensorRange": "Unspecified",
                "negativeHysteresis": "120.000",
                "nominalReading": "10080.000",
                "normalMaximum": "23640.000",
                "normalMinimum": "16680.000",
                "positiveHysteresis": "120.000",
                "readableThresholds": "lcr lnc",
                "sensorID": "0x34",
                "sensorName": "Fan3A RPM",
                "sensorReading": "4680 (+/- 120) RPM",
                "sensorType": "Fan",
                "settableThresholds": "",
                "status": "ok",
                "thresholdReadMask": "lcr lnc",
                "uniqueSensorID": "7.1:0x34"
              },
              {
                "assertionEvents": [],
                "assertionsEnabled": [],
                "deassertionsEnabled": [],
                "entityID": "7.1 (System Board)",
                "eventMessageControl": "Per-threshold",
                "lowerCritical": "720.000",
                "lowerNonCritical": "840.000",
                "maximumSensorRange": "Unspecified",
                "minimumSensorRange": "Unspecified",
                "negativeHysteresis": "120.000",
                "nominalReading": "10080.000",
                "normalMaximum": "23640.000",
                "normalMinimum": "16680.000",
                "positiveHysteresis": "120.000",
                "readableThresholds": "lcr lnc",
                "sensorID": "0x36",
                "sensorName": "Fan4A RPM",
                "sensorReading": "4560 (+/- 120) RPM",
                "sensorType": "Fan",
                "settableThresholds": "",
                "status": "ok",
                "thresholdReadMask": "lcr lnc",
                "uniqueSensorID": "7.1:0x36"
              },
              {
                "assertionEvents": [],
                "assertionsEnabled": [],
                "deassertionsEnabled": [],
                "entityID": "7.1 (System Board)",
                "eventMessageControl": "Per-threshold",
                "lowerCritical": "720.000",
                "lowerNonCritical": "840.000",
                "maximumSensorRange": "Unspecified",
                "minimumSensorRange": "Unspecified",
                "negativeHysteresis": "120.000",
                "nominalReading": "6720.000",
                "normalMaximum": "23640.000",
                "normalMinimum": "16680.000",
                "positiveHysteresis": "120.000",
                "readableThresholds": "lcr lnc",
                "sensorID": "0x38",
                "sensorName": "Fan5A RPM",
                "sensorReading": "4800 (+/- 120) RPM",
                "sensorType": "Fan",
                "settableThresholds": "",
                "status": "ok",
                "thresholdReadMask": "lcr lnc",
                "uniqueSensorID": "7.1:0x38"
              },
              {
                "assertionEvents": [],
                "assertionsEnabled": [],
                "deassertionsEnabled": [],
                "entityID": "7.1 (System Board)",
                "eventMessageControl": "Per-threshold",
                "lowerCritical": "720.000",
                "lowerNonCritical": "840.000",
                "maximumSensorRange": "Unspecified",
                "minimumSensorRange": "Unspecified",
                "negativeHysteresis": "120.000",
                "nominalReading": "6720.000",
                "normalMaximum": "23640.000",
                "normalMinimum": "16680.000",
                "positiveHysteresis": "120.000",
                "readableThresholds": "lcr lnc",
                "sensorID": "0x3a",
                "sensorName": "Fan6A RPM",
                "sensorReading": "4560 (+/- 120) RPM",
                "sensorType": "Fan",
                "settableThresholds": "",
                "status": "ok",
                "thresholdReadMask": "lcr lnc",
                "uniqueSensorID": "7.1:0x3a"
              },
              {
                "assertionEvents": [],
                "assertionsEnabled": [],
                "deassertionsEnabled": [],
                "entityID": "7.1 (System Board)",
                "eventMessageControl": "Per-threshold",
                "lowerCritical": "-7.000",
                "lowerNonCritical": "3.000",
                "maximumSensorRange": "Unspecified",
                "minimumSensorRange": "Unspecified",
                "negativeHysteresis": "1.000",
                "nominalReading": "23.000",
                "normalMaximum": "69.000",
                "normalMinimum": "11.000",
                "positiveHysteresis": "1.000",
                "readableThresholds": "lcr lnc unc ucr",
                "sensorID": "0x4",
                "sensorName": "Inlet Temp",
                "sensorReading": "22 (+/- 1) degrees C",
                "sensorType": "Temperature",
                "settableThresholds": "lcr lnc unc ucr",
                "status": "ok",
                "thresholdReadMask": "lcr lnc unc ucr",
                "uniqueSensorID": "7.1:0x4",
                "upperCritical": "47.000",
                "upperNonCritical": "42.000"
              },
              {
                "assertionEvents": [],
                "assertionsEnabled": [],
                "entityID": "7.1 (System Board)",
                "eventMessageControl": "Per-threshold",
                "lowerCritical": "3.000",
                "lowerNonCritical": "8.000",
                "maximumSensorRange": "Unspecified",
                "minimumSensorRange": "Unspecified",
                "negativeHysteresis": "1.000",
                "nominalReading": "23.000",
                "normalMaximum": "69.000",
                "normalMinimum": "11.000",
                "positiveHysteresis": "1.000",
                "readableThresholds": "lcr lnc unc ucr",
                "sensorID": "0x1",
                "sensorName": "Exhaust Temp",
                "sensorReading": "36 (+/- 1) degrees C",
                "sensorType": "Temperature",
                "settableThresholds": "",
                "status": "ok",
                "uniqueSensorID": "7.1:0x1",
                "upperCritical": "75.000",
                "upperNonCritical": "70.000"
              },
              {
                "assertionEvents": [],
                "assertionsEnabled": [],
                "entityID": "3.1 (Processor)",
                "eventMessageControl": "Per-threshold",
                "lowerCritical": "3.000",
                "lowerNonCritical": "8.000",
                "maximumSensorRange": "Unspecified",
                "minimumSensorRange": "Unspecified",
                "negativeHysteresis": "1.000",
                "nominalReading": "23.000",
                "normalMaximum": "69.000",
                "normalMinimum": "11.000",
                "positiveHysteresis": "1.000",
                "readableThresholds": "No Thresholds",
                "sensorID": "0xe",
                "sensorName": "Temp",
                "sensorReading": "45 (+/- 1) degrees C",
                "sensorType": "Temperature",
                "settableThresholds": "No Thresholds",
                "status": "ok",
                "uniqueSensorID": "3.1:0xe",
                "upperCritical": "83.000",
                "upperNonCritical": "77.000"
              },
              {
                "assertionEvents": [],
                "assertionsEnabled": [],
                "entityID": "3.2 (Processor)",
                "eventMessageControl": "Per-threshold",
                "lowerCritical": "3.000",
                "lowerNonCritical": "8.000",
                "maximumSensorRange": "Unspecified",
                "minimumSensorRange": "Unspecified",
                "negativeHysteresis": "1.000",
                "nominalReading": "23.000",
                "normalMaximum": "69.000",
                "normalMinimum": "11.000",
                "positiveHysteresis": "1.000",
                "readableThresholds": "No Thresholds",
                "sensorID": "0xf",
                "sensorName": "Temp",
                "sensorReading": "45 (+/- 1) degrees C",
                "sensorType": "Temperature",
                "settableThresholds": "No Thresholds",
                "status": "ok",
                "uniqueSensorID": "3.2:0xf",
                "upperCritical": "83.000",
                "upperNonCritical": "77.000"
              },
              {
                "assertionsEnabled": [
                  "Timer expired",
                  "Hard reset",
                  "Power down",
                  "Power cycle"
                ],
                "deassertionsEnabled": [
                  "Timer expired",
                  "Hard reset",
                  "Power down",
                  "Power cycle"
                ],
                "entityID": "7.1 (System Board)",
                "sensorID": "0x71",
                "sensorName": "OS Watchdog",
                "sensorType": "Watchdog",
                "uniqueSensorID": "7.1:0x71"
              },
              {
                "assertionEvents": [
                  "State Deasserted"
                ],
                "assertionsEnabled": [
                  "State Deasserted",
                  "State Asserted"
                ],
                "deassertionsEnabled": [
                  "State Deasserted",
                  "State Asserted"
                ],
                "entityID": "3.1 (Processor)",
                "sensorID": "0x23",
                "sensorName": "VCORE PG",
                "sensorType": "Voltage",
                "statesAsserted": [
                  "State Deasserted"
                ],
                "uniqueSensorID": "3.1:0x23"
              },
              {
                "assertionEvents": [
                  "State Deasserted"
                ],
                "assertionsEnabled": [
                  "State Deasserted",
                  "State Asserted"
                ],
                "entityID": "3.2 (Processor)",
                "sensorID": "0x24",
                "sensorName": "VCORE PG",
                "sensorType": "Voltage",
                "statesAsserted": [
                  "State Deasserted"
                ],
                "uniqueSensorID": "3.2:0x24"
              },
              {
                "assertionEvents": [
                  "State Deasserted"
                ],
                "assertionsEnabled": [
                  "State Deasserted",
                  "State Asserted"
                ],
                "entityID": "7.1 (System Board)",
                "sensorID": "0x19",
                "sensorName": "3.3V PG",
                "sensorType": "Voltage",
                "statesAsserted": [
                  "State Deasserted"
                ],
                "uniqueSensorID": "7.1:0x19"
              },
              {
                "assertionEvents": [
                  "State Deasserted"
                ],
                "assertionsEnabled": [
                  "State Deasserted",
                  "State Asserted"
                ],
                "entityID": "7.1 (System Board)",
                "sensorID": "0x1a",
                "sensorName": "5V PG",
                "sensorType": "Voltage",
                "statesAsserted": [
                  "State Deasserted"
                ],
                "uniqueSensorID": "7.1:0x1a"
              },
              {
                "assertionEvents": [
                  "Connected"
                ],
                "assertionsEnabled": [
                  "Config Error"
                ],
                "deassertionsEnabled": [
                  "Config Error"
                ],
                "entityID": "7.1 (System Board)",
                "sensorID": "0x50",
                "sensorName": "USB Cable Pres",
                "sensorType": "Cable / Interconnect",
                "statesAsserted": [
                  "Connected"
                ],
                "uniqueSensorID": "7.1:0x50"
              },
              {
                "assertionsEnabled": [
                  "Config Error"
                ],
                "deassertionsEnabled": [
                  "Config Error"
                ],
                "entityID": "7.1 (System Board)",
                "sensorID": "0x51",
                "sensorName": "VGA Cable Pres",
                "sensorType": "Cable / Interconnect",
                "uniqueSensorID": "7.1:0x51"
              },
              {
                "assertionEvents": [
                  "Present"
                ],
                "entityID": "7.1 (System Board)",
                "sensorID": "0x70",
                "sensorName": "Dedicated NIC",
                "sensorType": "Entity Presence",
                "statesAsserted": [
                  "Present"
                ],
                "uniqueSensorID": "7.1:0x70"
              },
              {
                "assertionEvents": [
                  "Absent"
                ],
                "entityID": "11.2 (Add-in Card)",
                "sensorID": "0x49",
                "sensorName": "Presence",
                "sensorType": "Entity Presence",
                "statesAsserted": [
                  "Absent"
                ],
                "uniqueSensorID": "11.2:0x49"
              },
              {
                "assertionEvents": [
                  "Present"
                ],
                "entityID": "3.1 (Processor)",
                "sensorID": "0x40",
                "sensorName": "Presence",
                "sensorType": "Entity Presence",
                "statesAsserted": [
                  "Present"
                ],
                "uniqueSensorID": "3.1:0x40"
              },
              {
                "assertionEvents": [
                  "Present"
                ],
                "entityID": "3.2 (Processor)",
                "sensorID": "0x41",
                "sensorName": "Presence",
                "sensorType": "Entity Presence",
                "statesAsserted": [
                  "Present"
                ],
                "uniqueSensorID": "3.2:0x41"
              },
              {
                "assertionEvents": [
                  "State Deasserted"
                ],
                "assertionsEnabled": [
                  "State Deasserted",
                  "State Asserted"
                ],
                "entityID": "3.2 (Processor)",
                "sensorID": "0x22",
                "sensorName": "PLL PG",
                "sensorType": "Voltage",
                "statesAsserted": [
                  "State Deasserted"
                ],
                "uniqueSensorID": "3.2:0x22"
              },
              {
                "assertionEvents": [
                  "State Deasserted"
                ],
                "assertionsEnabled": [
                  "State Deasserted",
                  "State Asserted"
                ],
                "entityID": "3.1 (Processor)",
                "sensorID": "0x25",
                "sensorName": "PLL PG",
                "sensorType": "Voltage",
                "statesAsserted": [
                  "State Deasserted"
                ],
                "uniqueSensorID": "3.1:0x25"
              },
              {
                "assertionEvents": [
                  "State Deasserted"
                ],
                "assertionsEnabled": [
                  "State Deasserted",
                  "State Asserted"
                ],
                "entityID": "7.1 (System Board)",
                "sensorID": "0x27",
                "sensorName": "1.1V PG",
                "sensorType": "Voltage",
                "statesAsserted": [
                  "State Deasserted"
                ],
                "uniqueSensorID": "7.1:0x27"
              },
              {
                "assertionEvents": [
                  "State Deasserted"
                ],
                "assertionsEnabled": [
                  "State Deasserted",
                  "State Asserted"
                ],
                "entityID": "3.1 (Processor)",
                "sensorID": "0x15",
                "sensorName": "M23 VDDQ PG",
                "sensorType": "Voltage",
                "statesAsserted": [
                  "State Deasserted"
                ],
                "uniqueSensorID": "3.1:0x15"
              },
              {
                "assertionEvents": [
                  "State Deasserted"
                ],
                "assertionsEnabled": [
                  "State Deasserted",
                  "State Asserted"
                ],
                "entityID": "3.1 (Processor)",
                "sensorID": "0x16",
                "sensorName": "M23 VTT PG",
                "sensorType": "Voltage",
                "statesAsserted": [
                  "State Deasserted"
                ],
                "uniqueSensorID": "3.1:0x16"
              },
              {
                "assertionEvents": [
                  "State Deasserted"
                ],
                "assertionsEnabled": [
                  "State Deasserted",
                  "State Asserted"
                ],
                "entityID": "7.1 (System Board)",
                "sensorID": "0x21",
                "sensorName": "FETDRV PG",
                "sensorType": "Voltage",
                "statesAsserted": [
                  "State Deasserted"
                ],
                "uniqueSensorID": "7.1:0x21"
              },
              {
                "assertionEvents": [
                  "Present"
                ],
                "entityID": "10.2 (Power Supply)",
                "sensorID": "0x43",
                "sensorName": "Presence",
                "sensorType": "Entity Presence",
                "statesAsserted": [
                  "Present"
                ],
                "uniqueSensorID": "10.2:0x43"
              },
              {
                "assertionEvents": [
                  "State Deasserted"
                ],
                "assertionsEnabled": [
                  "State Deasserted",
                  "State Asserted"
                ],
                "entityID": "3.2 (Processor)",
                "sensorID": "0x29",
                "sensorName": "VSA PG",
                "sensorType": "Voltage",
                "statesAsserted": [
                  "State Deasserted"
                ],
                "uniqueSensorID": "3.2:0x29"
              },
              {
                "assertionEvents": [
                  "State Deasserted"
                ],
                "assertionsEnabled": [
                  "State Deasserted",
                  "State Asserted"
                ],
                "entityID": "3.1 (Processor)",
                "sensorID": "0x2b",
                "sensorName": "VSA PG",
                "sensorType": "Voltage",
                "statesAsserted": [
                  "State Deasserted"
                ],
                "uniqueSensorID": "3.1:0x2b"
              },
              {
                "assertionEvents": [
                  "State Deasserted"
                ],
                "assertionsEnabled": [
                  "State Deasserted",
                  "State Asserted"
                ],
                "entityID": "3.2 (Processor)",
                "sensorID": "0x1b",
                "sensorName": "M01 VDDQ PG",
                "sensorType": "Voltage",
                "statesAsserted": [
                  "State Deasserted"
                ],
                "uniqueSensorID": "3.2:0x1b"
              },
              {
                "assertionEvents": [
                  "State Deasserted"
                ],
                "assertionsEnabled": [
                  "State Deasserted",
                  "State Asserted"
                ],
                "entityID": "3.1 (Processor)",
                "sensorID": "0x1e",
                "sensorName": "M01 VDDQ PG",
                "sensorType": "Voltage",
                "statesAsserted": [
                  "State Deasserted"
                ],
                "uniqueSensorID": "3.1:0x1e"
              },
              {
                "assertionEvents": [
                  "State Deasserted"
                ],
                "assertionsEnabled": [
                  "State Deasserted",
                  "State Asserted"
                ],
                "entityID": "3.2 (Processor)",
                "sensorID": "0x2e",
                "sensorName": "M23 VTT PG",
                "sensorType": "Voltage",
                "statesAsserted": [
                  "State Deasserted"
                ],
                "uniqueSensorID": "3.2:0x2e"
              },
              {
                "assertionEvents": [
                  "State Deasserted"
                ],
                "assertionsEnabled": [
                  "State Deasserted",
                  "State Asserted"
                ],
                "entityID": "3.2 (Processor)",
                "sensorID": "0x1c",
                "sensorName": "M01 VTT PG",
                "sensorType": "Voltage",
                "statesAsserted": [
                  "State Deasserted"
                ],
                "uniqueSensorID": "3.2:0x1c"
              },
              {
                "assertionEvents": [
                  "State Deasserted"
                ],
                "assertionsEnabled": [
                  "State Deasserted",
                  "State Asserted"
                ],
                "entityID": "7.1 (System Board)",
                "sensorID": "0x2f",
                "sensorName": "NDC PG",
                "sensorType": "Voltage",
                "statesAsserted": [
                  "State Deasserted"
                ],
                "uniqueSensorID": "7.1:0x2f"
              },
              {
                "entityID": "7.1 (System Board)",
                "sensorID": "0x4c",
                "sensorName": "LCD Cable Pres",
                "sensorType": "Cable / Interconnect",
                "uniqueSensorID": "7.1:0x4c"
              },
              {
                "assertionEvents": [
                  "State Deasserted"
                ],
                "assertionsEnabled": [
                  "State Deasserted",
                  "State Asserted"
                ],
                "entityID": "3.2 (Processor)",
                "sensorID": "0x1f",
                "sensorName": "VTT PG",
                "sensorType": "Voltage",
                "statesAsserted": [
                  "State Deasserted"
                ],
                "uniqueSensorID": "3.2:0x1f"
              },
              {
                "assertionEvents": [
                  "State Deasserted"
                ],
                "assertionsEnabled": [
                  "State Deasserted",
                  "State Asserted"
                ],
                "entityID": "3.1 (Processor)",
                "sensorID": "0x20",
                "sensorName": "VTT PG",
                "sensorType": "Voltage",
                "statesAsserted": [
                  "State Deasserted"
                ],
                "uniqueSensorID": "3.1:0x20"
              },
              {
                "assertionEvents": [
                  "State Deasserted"
                ],
                "assertionsEnabled": [
                  "State Deasserted",
                  "State Asserted"
                ],
                "entityID": "3.2 (Processor)",
                "sensorID": "0x1d",
                "sensorName": "M23 VDDQ PG",
                "sensorType": "Voltage",
                "statesAsserted": [
                  "State Deasserted"
                ],
                "uniqueSensorID": "3.2:0x1d"
              },
              {
                "assertionEvents": [
                  "Present"
                ],
                "assertionsEnabled": [
                  "Present",
                  "Absent"
                ],
                "entityID": "11.1 (Add-in Card)",
                "sensorID": "0x4a",
                "sensorName": "Presence",
                "sensorType": "Entity Presence",
                "statesAsserted": [
                  "Present"
                ],
                "uniqueSensorID": "11.1:0x4a"
              },
              {
                "assertionEvents": [
                  "Absent"
                ],
                "entityID": "11.3 (Add-in Card)",
                "sensorID": "0x48",
                "sensorName": "Presence",
                "sensorType": "Entity Presence",
                "statesAsserted": [
                  "Absent"
                ],
                "uniqueSensorID": "11.3:0x48"
              },
              {
                "assertionEvents": [
                  "Presence detected"
                ],
                "assertionsEnabled": [
                  "IERR",
                  "Thermal Trip",
                  "Configuration Error",
                  "Presence detected",
                  "Throttled"
                ],
                "deassertionsEnabled": [
                  "IERR",
                  "Thermal Trip",
                  "Configuration Error",
                  "Presence detected",
                  "Throttled"
                ],
                "entityID": "3.1 (Processor)",
                "sensorID": "0x60",
                "sensorName": "Status",
                "sensorType": "Processor",
                "statesAsserted": [
                  "Presence detected"
                ],
                "uniqueSensorID": "3.1:0x60"
              },
              {
                "assertionEvents": [
                  "Presence detected"
                ],
                "assertionsEnabled": [
                  "IERR",
                  "Thermal Trip",
                  "Configuration Error",
                  "Throttled"
                ],
                "deassertionsEnabled": [
                  "IERR",
                  "Thermal Trip",
                  "Configuration Error",
                  "Throttled"
                ],
                "entityID": "3.2 (Processor)",
                "sensorID": "0x61",
                "sensorName": "Status",
                "sensorType": "Processor",
                "statesAsserted": [
                  "Presence detected"
                ],
                "uniqueSensorID": "3.2:0x61"
              },
              {
                "assertionEvents": [
                  "Fully Redundant"
                ],
                "assertionsEnabled": [
                  "Fully Redundant",
                  "Redundancy Lost"
                ],
                "entityID": "7.1 (System Board)",
                "sensorID": "0x75",
                "sensorName": "Fan Redundancy",
                "sensorType": "Fan",
                "statesAsserted": [
                  "Fully Redundant"
                ],
                "uniqueSensorID": "7.1:0x75"
              },
              {
                "assertionEvents": [
                  "Connected"
                ],
                "assertionsEnabled": [
                  "Config Error"
                ],
                "deassertionsEnabled": [
                  "Config Error"
                ],
                "entityID": "7.1 (System Board)",
                "sensorID": "0x64",
                "sensorName": "Riser Config Err",
                "sensorType": "Cable / Interconnect",
                "statesAsserted": [
                  "Connected"
                ],
                "uniqueSensorID": "7.1:0x64"
              },
              {
                "assertionEvents": [
                  "Connected"
                ],
                "assertionsEnabled": [
                  "Config Error"
                ],
                "deassertionsEnabled": [
                  "Config Error"
                ],
                "entityID": "7.1 (System Board)",
                "sensorID": "0x4f",
                "sensorName": "Riser 3 Presence",
                "sensorType": "Cable / Interconnect",
                "statesAsserted": [
                  "Connected"
                ],
                "uniqueSensorID": "7.1:0x4f"
              },
              {
                "assertionEvents": [
                  "State Deasserted"
                ],
                "assertionsEnabled": [
                  "State Deasserted",
                  "State Asserted"
                ],
                "entityID": "7.1 (System Board)",
                "sensorID": "0x28",
                "sensorName": "1.5V PG",
                "sensorType": "Voltage",
                "statesAsserted": [
                  "State Deasserted"
                ],
                "uniqueSensorID": "7.1:0x28"
              },
              {
                "assertionEvents": [
                  "State Deasserted"
                ],
                "assertionsEnabled": [
                  "State Deasserted",
                  "State Asserted"
                ],
                "entityID": "7.1 (System Board)",
                "sensorID": "0x2c",
                "sensorName": "PS2 PG Fail",
                "sensorType": "Voltage",
                "statesAsserted": [
                  "State Deasserted"
                ],
                "uniqueSensorID": "7.1:0x2c"
              },
              {
                "assertionEvents": [
                  "State Deasserted"
                ],
                "assertionsEnabled": [
                  "State Deasserted",
                  "State Asserted"
                ],
                "entityID": "7.1 (System Board)",
                "sensorID": "0x2d",
                "sensorName": "PS1 PG Fail",
                "sensorType": "Voltage",
                "statesAsserted": [
                  "State Deasserted"
                ],
                "uniqueSensorID": "7.1:0x2d"
              },
              {
                "assertionEvents": [
                  "State Deasserted"
                ],
                "assertionsEnabled": [
                  "State Deasserted",
                  "State Asserted"
                ],
                "entityID": "7.1 (System Board)",
                "sensorID": "0xf6",
                "sensorName": "BP1 5V PG",
                "sensorType": "Voltage",
                "statesAsserted": [
                  "State Deasserted"
                ],
                "uniqueSensorID": "7.1:0xf6"
              },
              {
                "assertionEvents": [
                  "State Deasserted"
                ],
                "assertionsEnabled": [
                  "State Deasserted",
                  "State Asserted"
                ],
                "entityID": "7.1 (System Board)",
                "sensorID": "0xf7",
                "sensorName": "BP2 5V PG",
                "sensorType": "Voltage",
                "uniqueSensorID": "7.1:0xf7"
              },
              {
                "assertionEvents": [
                  "State Deasserted"
                ],
                "assertionsEnabled": [
                  "State Deasserted",
                  "State Asserted"
                ],
                "entityID": "3.1 (Processor)",
                "sensorID": "0x14",
                "sensorName": "M01 VTT PG",
                "sensorType": "Voltage",
                "statesAsserted": [
                  "State Deasserted"
                ],
                "uniqueSensorID": "3.1:0x14"
              },
              {
                "assertionEvents": [
                  "Present"
                ],
                "entityID": "10.1 (Power Supply)",
                "sensorID": "0x42",
                "sensorName": "Presence",
                "sensorType": "Entity Presence",
                "statesAsserted": [
                  "Present"
                ],
                "uniqueSensorID": "10.1:0x42"
              },
              {
                "assertionsEnabled": [
                  "NMI/Diag Interrupt",
                  "Bus Timeout"
                ],
                "deassertionsEnabled": [
                  "NMI/Diag Interrupt",
                  "Bus Timeout"
                ],
                "entityID": "7.1 (System Board)",
                "sensorID": "0x90",
                "sensorName": "PCIe Slot1",
                "sensorType": "Critical Interrupt",
                "uniqueSensorID": "7.1:0x90"
              },
              {
                "assertionsEnabled": [
                  "NMI/Diag Interrupt",
                  "Bus Timeout"
                ],
                "deassertionsEnabled": [
                  "NMI/Diag Interrupt",
                  "Bus Timeout"
                ],
                "entityID": "7.1 (System Board)",
                "sensorID": "0x91",
                "sensorName": "PCIe Slot2",
                "sensorType": "Critical Interrupt",
                "uniqueSensorID": "7.1:0x91"
              },
              {
                "assertionsEnabled": [
                  "NMI/Diag Interrupt",
                  "Bus Timeout"
                ],
                "deassertionsEnabled": [
                  "NMI/Diag Interrupt",
                  "Bus Timeout"
                ],
                "entityID": "7.1 (System Board)",
                "sensorID": "0x92",
                "sensorName": "PCIe Slot3",
                "sensorType": "Critical Interrupt",
                "uniqueSensorID": "7.1:0x92"
              },
              {
                "assertionsEnabled": [
                  "NMI/Diag Interrupt",
                  "Bus Timeout"
                ],
                "deassertionsEnabled": [
                  "NMI/Diag Interrupt",
                  "Bus Timeout"
                ],
                "entityID": "7.1 (System Board)",
                "sensorID": "0x93",
                "sensorName": "PCIe Slot4",
                "sensorType": "Critical Interrupt",
                "uniqueSensorID": "7.1:0x93"
              },
              {
                "assertionsEnabled": [
                  "NMI/Diag Interrupt",
                  "Bus Timeout"
                ],
                "deassertionsEnabled": [
                  "NMI/Diag Interrupt",
                  "Bus Timeout"
                ],
                "entityID": "7.1 (System Board)",
                "sensorID": "0x94",
                "sensorName": "PCIe Slot5",
                "sensorType": "Critical Interrupt",
                "uniqueSensorID": "7.1:0x94"
              },
              {
                "assertionsEnabled": [
                  "NMI/Diag Interrupt",
                  "Bus Timeout"
                ],
                "deassertionsEnabled": [
                  "NMI/Diag Interrupt",
                  "Bus Timeout"
                ],
                "entityID": "7.1 (System Board)",
                "sensorID": "0x95",
                "sensorName": "PCIe Slot6",
                "sensorType": "Critical Interrupt",
                "uniqueSensorID": "7.1:0x95"
              },
              {
                "assertionsEnabled": [
                  "NMI/Diag Interrupt",
                  "Bus Timeout"
                ],
                "deassertionsEnabled": [
                  "NMI/Diag Interrupt",
                  "Bus Timeout"
                ],
                "entityID": "7.1 (System Board)",
                "sensorID": "0x96",
                "sensorName": "PCIe Slot7",
                "sensorType": "Critical Interrupt",
                "uniqueSensorID": "7.1:0x96"
              },
              {
                "entityID": "0.1 (Unspecified)",
                "sensorID": "0xfa",
                "sensorName": "vFlash",
                "sensorType": "Module / Board",
                "uniqueSensorID": "0.1:0xfa"
              },
              {
                "assertionsEnabled": [
                  "Failed"
                ],
                "deassertionsEnabled": [
                  "Failed"
                ],
                "entityID": "7.1 (System Board)",
                "sensorID": "0x65",
                "sensorName": "CMOS Battery",
                "sensorType": "Battery",
                "uniqueSensorID": "7.1:0x65"
              },
              {
                "assertionsEnabled": [
                  "Failed"
                ],
                "deassertionsEnabled": [
                  "Failed"
                ],
                "entityID": "11.2 (Add-in Card)",
                "eventStatus": "Unavailable",
                "sensorID": "0x68",
                "sensorName": "ROMB Battery",
                "sensorType": "Battery",
                "uniqueSensorID": "11.2:0x68"
              },
              {
                "assertionsEnabled": [
                  "Failed"
                ],
                "deassertionsEnabled": [
                  "Failed"
                ],
                "entityID": "11.4 (Add-in Card)",
                "eventStatus": "Unavailable",
                "sensorID": "0x69",
                "sensorName": "ROMB Battery",
                "sensorType": "Battery",
                "uniqueSensorID": "11.4:0x69"
              },
              {
                "assertionEvents": [
                  "Present"
                ],
                "entityID": "26.1 (Disk Drive Bay)",
                "sensorID": "0x54",
                "sensorName": "Presence",
                "sensorType": "Entity Presence",
                "statesAsserted": [
                  "Present"
                ],
                "uniqueSensorID": "26.1:0x54"
              },
              {
                "assertionEvents": [
                  "Absent"
                ],
                "entityID": "26.2 (Disk Drive Bay)",
                "sensorID": "0x55",
                "sensorName": "Presence",
                "sensorType": "Entity Presence",
                "statesAsserted": [
                  "Absent"
                ],
                "uniqueSensorID": "26.2:0x55"
              },
              {
                "assertionEvents": [],
                "assertionsEnabled": [],
                "entityID": "10.1 (Power Supply)",
                "eventMessageControl": "Per-threshold",
                "maximumSensorRange": "Unspecified",
                "minimumSensorRange": "Unspecified",
                "negativeHysteresis": "Unspecified",
                "nominalReading": "0.000",
                "normalMaximum": "0.000",
                "positiveHysteresis": "Unspecified",
                "readableThresholds": "No Thresholds",
                "sensorID": "0x6a",
                "sensorName": "Current 1",
                "sensorReading": "0.600 (+/- 0) Amps",
                "sensorType": "Current",
                "settableThresholds": "No Thresholds",
                "status": "ok",
                "uniqueSensorID": "10.1:0x6a"
              },
              {
                "assertionEvents": [],
                "assertionsEnabled": [],
                "entityID": "10.2 (Power Supply)",
                "eventMessageControl": "Per-threshold",
                "maximumSensorRange": "Unspecified",
                "minimumSensorRange": "Unspecified",
                "negativeHysteresis": "Unspecified",
                "nominalReading": "0.000",
                "normalMaximum": "0.000",
                "positiveHysteresis": "Unspecified",
                "readableThresholds": "No Thresholds",
                "sensorID": "0x6b",
                "sensorName": "Current 2",
                "sensorReading": "0.400 (+/- 0) Amps",
                "sensorType": "Current",
                "settableThresholds": "No Thresholds",
                "status": "ok",
                "uniqueSensorID": "10.2:0x6b"
              },
              {
                "assertionEvents": [],
                "assertionsEnabled": [],
                "entityID": "10.1 (Power Supply)",
                "eventMessageControl": "Per-threshold",
                "maximumSensorRange": "Unspecified",
                "minimumSensorRange": "Unspecified",
                "negativeHysteresis": "Unspecified",
                "nominalReading": "0.000",
                "normalMaximum": "0.000",
                "positiveHysteresis": "Unspecified",
                "readableThresholds": "No Thresholds",
                "sensorID": "0x6c",
                "sensorName": "Voltage 1",
                "sensorReading": "118 (+/- 0) Volts",
                "sensorType": "Voltage",
                "settableThresholds": "No Thresholds",
                "status": "ok",
                "uniqueSensorID": "10.1:0x6c"
              },
              {
                "assertionEvents": [],
                "assertionsEnabled": [],
                "entityID": "10.2 (Power Supply)",
                "eventMessageControl": "Per-threshold",
                "maximumSensorRange": "Unspecified",
                "minimumSensorRange": "Unspecified",
                "negativeHysteresis": "Unspecified",
                "nominalReading": "0.000",
                "normalMaximum": "0.000",
                "positiveHysteresis": "Unspecified",
                "readableThresholds": "No Thresholds",
                "sensorID": "0x6d",
                "sensorName": "Voltage 2",
                "sensorReading": "118 (+/- 0) Volts",
                "sensorType": "Voltage",
                "settableThresholds": "No Thresholds",
                "status": "ok",
                "uniqueSensorID": "10.2:0x6d"
              },
              {
                "assertionsEnabled": [
                  "Fully Redundant",
                  "Redundancy Lost"
                ],
                "entityID": "7.1 (System Board)",
                "eventStatus": "Unavailable",
                "sensorID": "0x74",
                "sensorName": "PS Redundancy",
                "sensorType": "Power Supply",
                "uniqueSensorID": "7.1:0x74"
              },
              {
                "assertionEvents": [
                  "Presence detected"
                ],
                "assertionsEnabled": [
                  "Presence detected",
                  "Failure detected",
                  "Predictive failure",
                  "Power Supply AC lost",
                  "Config Error: Vendor Mismatch",
                  "Config Error: Revision Mismatch",
                  "Config Error: Processor Missing",
                  "Config Error"
                ],
                "deassertionsEnabled": [
                  "Presence detected",
                  "Failure detected",
                  "Predictive failure",
                  "Power Supply AC lost",
                  "Config Error: Vendor Mismatch",
                  "Config Error: Revision Mismatch",
                  "Config Error: Processor Missing",
                  "Config Error"
                ],
                "entityID": "10.1 (Power Supply)",
                "sensorID": "0x62",
                "sensorName": "Status",
                "sensorType": "Power Supply",
                "statesAsserted": [
                  "Presence detected"
                ],
                "uniqueSensorID": "10.1:0x62"
              },
              {
                "assertionEvents": [
                  "Presence detected"
                ],
                "assertionsEnabled": [
                  "Presence detected",
                  "Failure detected",
                  "Predictive failure",
                  "Power Supply AC lost",
                  "Config Error: Vendor Mismatch",
                  "Config Error: Revision Mismatch",
                  "Config Error: Processor Missing",
                  "Config Error"
                ],
                "deassertionsEnabled": [
                  "Presence detected",
                  "Failure detected",
                  "Predictive failure",
                  "Power Supply AC lost",
                  "Config Error: Vendor Mismatch",
                  "Config Error: Revision Mismatch",
                  "Config Error: Processor Missing",
                  "Config Error"
                ],
                "entityID": "10.2 (Power Supply)",
                "sensorID": "0x63",
                "sensorName": "Status",
                "sensorType": "Power Supply",
                "statesAsserted": [
                  "Presence detected"
                ],
                "uniqueSensorID": "10.2:0x63"
              },
              {
                "assertionEvents": [],
                "assertionsEnabled": [],
                "deassertionsEnabled": [],
                "entityID": "7.1 (System Board)",
                "eventMessageControl": "Per-threshold",
                "maximumSensorRange": "3556.000",
                "minimumSensorRange": "Unspecified",
                "negativeHysteresis": "Unspecified",
                "nominalReading": "658.000",
                "normalMaximum": "672.000",
                "positiveHysteresis": "Unspecified",
                "readableThresholds": "unc ucr",
                "sensorID": "0x77",
                "sensorName": "Pwr Consumption",
                "sensorReading": "126 (+/- 0) Watts",
                "sensorType": "Current",
                "settableThresholds": "unc",
                "status": "ok",
                "uniqueSensorID": "7.1:0x77",
                "upperCritical": "1218.000",
                "upperNonCritical": "1106.000"
              },
              {
                "assertionEvents": [
                  "OEM Specific"
                ],
                "assertionsEnabled": [],
                "deassertionsEnabled": [],
                "entityID": "7.1 (System Board)",
                "sensorID": "0x76",
                "sensorName": "Power Optimized",
                "sensorType": "Unknown (0xC0)",
                "statesAsserted": [
                  "OEM Specific"
                ],
                "uniqueSensorID": "7.1:0x76"
              },
              {
                "entityID": "11.3 (Add-in Card)",
                "sensorID": "0xf4",
                "sensorName": "SD1",
                "sensorType": "Unknown (0xC9)",
                "uniqueSensorID": "11.3:0xf4"
              },
              {
                "entityID": "11.3 (Add-in Card)",
                "sensorID": "0xf5",
                "sensorName": "SD2",
                "sensorType": "Unknown (0xC9)",
                "uniqueSensorID": "11.3:0xf5"
              },
              {
                "assertionEvents": [
                  "Fully Redundant"
                ],
                "assertionsEnabled": [
                  "Fully Redundant",
                  "Redundancy Lost"
                ],
                "entityID": "11.3 (Add-in Card)",
                "sensorID": "0x78",
                "sensorName": "Redundancy",
                "sensorType": "Unknown (0xC9)",
                "uniqueSensorID": "11.3:0x78"
              },
              {
                "entityID": "34.1 (BIOS)",
                "sensorID": "0x1",
                "sensorName": "ECC Corr Err",
                "sensorType": "Memory",
                "uniqueSensorID": "34.1:0x1"
              },
              {
                "entityID": "34.1 (BIOS)",
                "sensorID": "0x2",
                "sensorName": "ECC Uncorr Err",
                "sensorType": "Memory",
                "uniqueSensorID": "34.1:0x2"
              },
              {
                "entityID": "34.1 (BIOS)",
                "sensorID": "0x3",
                "sensorName": "I/O Channel Chk",
                "sensorType": "Critical Interrupt",
                "uniqueSensorID": "34.1:0x3"
              },
              {
                "entityID": "34.1 (BIOS)",
                "sensorID": "0x4",
                "sensorName": "PCI Parity Err",
                "sensorType": "Critical Interrupt",
                "uniqueSensorID": "34.1:0x4"
              },
              {
                "entityID": "34.1 (BIOS)",
                "sensorID": "0x5",
                "sensorName": "PCI System Err",
                "sensorType": "Critical Interrupt",
                "uniqueSensorID": "34.1:0x5"
              },
              {
                "entityID": "34.1 (BIOS)",
                "sensorID": "0x6",
                "sensorName": "SBE Log Disabled",
                "sensorType": "Event Logging Disabled",
                "uniqueSensorID": "34.1:0x6"
              },
              {
                "entityID": "34.1 (BIOS)",
                "sensorID": "0x7",
                "sensorName": "Logging Disabled",
                "sensorType": "Event Logging Disabled",
                "uniqueSensorID": "34.1:0x7"
              },
              {
                "entityID": "34.1 (BIOS)",
                "sensorID": "0x8",
                "sensorName": "Unknown",
                "sensorType": "System Event",
                "uniqueSensorID": "34.1:0x8"
              },
              {
                "entityID": "34.1 (BIOS)",
                "sensorID": "0xa",
                "sensorName": "CPU Protocol Err",
                "sensorType": "Processor",
                "uniqueSensorID": "34.1:0xa"
              },
              {
                "entityID": "34.1 (BIOS)",
                "sensorID": "0xb",
                "sensorName": "CPU Bus PERR",
                "sensorType": "Processor",
                "uniqueSensorID": "34.1:0xb"
              },
              {
                "entityID": "34.1 (BIOS)",
                "sensorID": "0xc",
                "sensorName": "CPU Init Err",
                "sensorType": "Processor",
                "uniqueSensorID": "34.1:0xc"
              },
              {
                "entityID": "34.1 (BIOS)",
                "sensorID": "0xd",
                "sensorName": "CPU Machine Chk",
                "sensorType": "Processor",
                "uniqueSensorID": "34.1:0xd"
              },
              {
                "entityID": "34.1 (BIOS)",
                "sensorID": "0x11",
                "sensorName": "Memory Spared",
                "sensorType": "Memory",
                "uniqueSensorID": "34.1:0x11"
              },
              {
                "entityID": "34.1 (BIOS)",
                "sensorID": "0x12",
                "sensorName": "Memory Mirrored",
                "sensorType": "Memory",
                "uniqueSensorID": "34.1:0x12"
              },
              {
                "entityID": "34.1 (BIOS)",
                "sensorID": "0x13",
                "sensorName": "Memory RAID",
                "sensorType": "Memory",
                "uniqueSensorID": "34.1:0x13"
              },
              {
                "entityID": "34.1 (BIOS)",
                "sensorID": "0x14",
                "sensorName": "Memory Added",
                "sensorType": "Memory",
                "uniqueSensorID": "34.1:0x14"
              },
              {
                "entityID": "34.1 (BIOS)",
                "sensorID": "0x15",
                "sensorName": "Memory Removed",
                "sensorType": "Memory",
                "uniqueSensorID": "34.1:0x15"
              },
              {
                "entityID": "34.1 (BIOS)",
                "sensorID": "0x16",
                "sensorName": "Memory Cfg Err",
                "sensorType": "Memory",
                "uniqueSensorID": "34.1:0x16"
              },
              {
                "entityID": "34.1 (BIOS)",
                "sensorID": "0x17",
                "sensorName": "Mem Redun Gain",
                "sensorType": "Memory",
                "uniqueSensorID": "34.1:0x17"
              },
              {
                "entityID": "34.1 (BIOS)",
                "sensorID": "0x18",
                "sensorName": "PCIE Fatal Err",
                "sensorType": "Critical Interrupt",
                "uniqueSensorID": "34.1:0x18"
              },
              {
                "entityID": "34.1 (BIOS)",
                "sensorID": "0x19",
                "sensorName": "Chipset Err",
                "sensorType": "Critical Interrupt",
                "uniqueSensorID": "34.1:0x19"
              },
              {
                "entityID": "34.1 (BIOS)",
                "sensorID": "0x1a",
                "sensorName": "Err Reg Pointer",
                "sensorType": "Unknown (0xC1)",
                "uniqueSensorID": "34.1:0x1a"
              },
              {
                "entityID": "34.1 (BIOS)",
                "sensorID": "0x1b",
                "sensorName": "Mem ECC Warning",
                "sensorType": "Memory",
                "uniqueSensorID": "34.1:0x1b"
              },
              {
                "entityID": "34.1 (BIOS)",
                "sensorID": "0x1c",
                "sensorName": "Mem CRC Err",
                "sensorType": "Memory",
                "uniqueSensorID": "34.1:0x1c"
              },
              {
                "entityID": "34.1 (BIOS)",
                "sensorID": "0x1d",
                "sensorName": "USB Over-current",
                "sensorType": "Memory",
                "uniqueSensorID": "34.1:0x1d"
              },
              {
                "entityID": "34.1 (BIOS)",
                "sensorID": "0x1e",
                "sensorName": "POST Err",
                "sensorType": "System Firmwares",
                "uniqueSensorID": "34.1:0x1e"
              },
              {
                "entityID": "34.1 (BIOS)",
                "sensorID": "0x1f",
                "sensorName": "Hdwr version err",
                "sensorType": "Version Change",
                "uniqueSensorID": "34.1:0x1f"
              },
              {
                "entityID": "34.1 (BIOS)",
                "sensorID": "0x20",
                "sensorName": "Mem Overtemp",
                "sensorType": "Memory",
                "uniqueSensorID": "34.1:0x20"
              },
              {
                "entityID": "34.1 (BIOS)",
                "sensorID": "0x21",
                "sensorName": "Mem Fatal SB CRC",
                "sensorType": "Memory",
                "uniqueSensorID": "34.1:0x21"
              },
              {
                "entityID": "34.1 (BIOS)",
                "sensorID": "0x22",
                "sensorName": "Mem Fatal NB CRC",
                "sensorType": "Memory",
                "uniqueSensorID": "34.1:0x22"
              },
              {
                "entityID": "34.1 (BIOS)",
                "sensorID": "0x71",
                "sensorName": "OS Watchdog Time",
                "sensorType": "Watchdog",
                "uniqueSensorID": "34.1:0x71"
              },
              {
                "entityID": "34.1 (BIOS)",
                "sensorID": "0x26",
                "sensorName": "Non Fatal PCI Er",
                "sensorType": "Unknown (0xC2)",
                "uniqueSensorID": "34.1:0x26"
              },
              {
                "entityID": "34.1 (BIOS)",
                "sensorID": "0x27",
                "sensorName": "Fatal IO Error",
                "sensorType": "Unknown (0xC3)",
                "uniqueSensorID": "34.1:0x27"
              },
              {
                "entityID": "34.1 (BIOS)",
                "sensorID": "0x28",
                "sensorName": "MSR Info Log",
                "sensorType": "Unknown (0xC1)",
                "uniqueSensorID": "34.1:0x28"
              },
              {
                "entityID": "34.1 (BIOS)",
                "sensorID": "0x2a",
                "sensorName": "TXT Status",
                "sensorType": "OS Critical Stop",
                "uniqueSensorID": "34.1:0x2a"
              },
              {
                "assertionsEnabled": [
                  "Drive Present",
                  "Drive Fault"
                ],
                "deassertionsEnabled": [
                  "Drive Present",
                  "Drive Fault"
                ],
                "entityID": "7.1 (System Board)",
                "sensorID": "0xa0",
                "sensorName": "Drive 0",
                "sensorType": "Drive Slot / Bay",
                "uniqueSensorID": "7.1:0xa0"
              },
              {
                "assertionEvents": [
                  "Connected"
                ],
                "assertionsEnabled": [
                  "Config Error"
                ],
                "deassertionsEnabled": [
                  "Config Error"
                ],
                "entityID": "26.1 (Disk Drive Bay)",
                "sensorID": "0xe0",
                "sensorName": "Cable SAS A",
                "sensorType": "Cable / Interconnect",
                "statesAsserted": [
                  "Connected"
                ],
                "uniqueSensorID": "26.1:0xe0"
              },
              {
                "assertionEvents": [
                  "Connected"
                ],
                "assertionsEnabled": [
                  "Config Error"
                ],
                "deassertionsEnabled": [
                  "Config Error"
                ],
                "entityID": "26.1 (Disk Drive Bay)",
                "sensorID": "0xe1",
                "sensorName": "Cable SAS B",
                "sensorType": "Cable / Interconnect",
                "statesAsserted": [
                  "Connected"
                ],
                "uniqueSensorID": "26.1:0xe1"
              },
              {
                "assertionsEnabled": [
                  "Config Error"
                ],
                "deassertionsEnabled": [
                  "Config Error"
                ],
                "entityID": "26.1 (Disk Drive Bay)",
                "sensorID": "0xe2",
                "sensorName": "Cable SAS C",
                "sensorType": "Cable / Interconnect",
                "uniqueSensorID": "26.1:0xe2"
              },
              {
                "assertionsEnabled": [
                  "Config Error"
                ],
                "deassertionsEnabled": [
                  "Config Error"
                ],
                "entityID": "26.1 (Disk Drive Bay)",
                "sensorID": "0xe3",
                "sensorName": "Cable SAS D",
                "sensorType": "Cable / Interconnect",
                "uniqueSensorID": "26.1:0xe3"
              },
              {
                "assertionsEnabled": [
                  "Config Error"
                ],
                "deassertionsEnabled": [
                  "Config Error"
                ],
                "entityID": "26.2 (Disk Drive Bay)",
                "sensorID": "0xe4",
                "sensorName": "Cable SAS A",
                "sensorType": "Cable / Interconnect",
                "uniqueSensorID": "26.2:0xe4"
              },
              {
                "assertionsEnabled": [
                  "Config Error"
                ],
                "deassertionsEnabled": [
                  "Config Error"
                ],
                "entityID": "26.2 (Disk Drive Bay)",
                "sensorID": "0xe5",
                "sensorName": "Cable SAS B",
                "sensorType": "Cable / Interconnect",
                "uniqueSensorID": "26.2:0xe5"
              },
              {
                "assertionsEnabled": [
                  "Config Error"
                ],
                "deassertionsEnabled": [
                  "Config Error"
                ],
                "entityID": "26.2 (Disk Drive Bay)",
                "sensorID": "0xe6",
                "sensorName": "Cable SAS C",
                "sensorType": "Cable / Interconnect",
                "uniqueSensorID": "26.2:0xe6"
              },
              {
                "assertionsEnabled": [
                  "Config Error"
                ],
                "deassertionsEnabled": [
                  "Config Error"
                ],
                "entityID": "26.2 (Disk Drive Bay)",
                "sensorID": "0xe7",
                "sensorName": "Cable SAS D",
                "sensorType": "Cable / Interconnect",
                "uniqueSensorID": "26.2:0xe7"
              },
              {
                "assertionEvents": [
                  "Connected"
                ],
                "assertionsEnabled": [
                  "Config Error"
                ],
                "deassertionsEnabled": [
                  "Config Error"
                ],
                "entityID": "26.1 (Disk Drive Bay)",
                "sensorID": "0x58",
                "sensorName": "Power Cable",
                "sensorType": "Cable / Interconnect",
                "statesAsserted": [
                  "Connected"
                ],
                "uniqueSensorID": "26.1:0x58"
              },
              {
                "assertionEvents": [
                  "Connected"
                ],
                "assertionsEnabled": [
                  "Config Error"
                ],
                "deassertionsEnabled": [
                  "Config Error"
                ],
                "entityID": "26.1 (Disk Drive Bay)",
                "sensorID": "0x59",
                "sensorName": "Signal Cable",
                "sensorType": "Cable / Interconnect",
                "statesAsserted": [
                  "Connected"
                ],
                "uniqueSensorID": "26.1:0x59"
              },
              {
                "assertionsEnabled": [
                  "Config Error"
                ],
                "deassertionsEnabled": [
                  "Config Error"
                ],
                "entityID": "26.2 (Disk Drive Bay)",
                "sensorID": "0x5a",
                "sensorName": "Power Cable",
                "sensorType": "Cable / Interconnect",
                "uniqueSensorID": "26.2:0x5a"
              },
              {
                "assertionsEnabled": [
                  "Config Error"
                ],
                "deassertionsEnabled": [
                  "Config Error"
                ],
                "entityID": "26.2 (Disk Drive Bay)",
                "sensorID": "0x5b",
                "sensorName": "Signal Cable",
                "sensorType": "Cable / Interconnect",
                "uniqueSensorID": "26.2:0x5b"
              },
              {
                "assertionEvents": [],
                "assertionsEnabled": [],
                "deassertionsEnabled": [],
                "entityID": "7.1 (System Board)",
                "eventMessageControl": "Per-threshold",
                "lowerCritical": "720.000",
                "lowerNonCritical": "840.000",
                "maximumSensorRange": "Unspecified",
                "minimumSensorRange": "Unspecified",
                "negativeHysteresis": "120.000",
                "nominalReading": "6720.000",
                "normalMaximum": "23640.000",
                "normalMinimum": "16680.000",
                "positiveHysteresis": "120.000",
                "readableThresholds": "lcr lnc",
                "sensorID": "0x3c",
                "sensorName": "Fan7A RPM",
                "sensorReading": "4800 (+/- 120) RPM",
                "sensorType": "Fan",
                "settableThresholds": "",
                "status": "ok",
                "thresholdReadMask": "lcr lnc",
                "uniqueSensorID": "7.1:0x3c"
              },
              {
                "assertionEvents": [],
                "assertionsEnabled": [],
                "deassertionsEnabled": [],
                "entityID": "7.1 (System Board)",
                "eventMessageControl": "Per-threshold",
                "lowerCritical": "720.000",
                "lowerNonCritical": "840.000",
                "maximumSensorRange": "Unspecified",
                "minimumSensorRange": "Unspecified",
                "negativeHysteresis": "120.000",
                "nominalReading": "6720.000",
                "normalMaximum": "23640.000",
                "normalMinimum": "16680.000",
                "positiveHysteresis": "120.000",
                "readableThresholds": "lcr lnc",
                "sensorID": "0x31",
                "sensorName": "Fan1B RPM",
                "sensorReading": "4320 (+/- 120) RPM",
                "sensorType": "Fan",
                "settableThresholds": "",
                "status": "ok",
                "thresholdReadMask": "lcr lnc",
                "uniqueSensorID": "7.1:0x31"
              },
              {
                "assertionEvents": [],
                "assertionsEnabled": [],
                "deassertionsEnabled": [],
                "entityID": "7.1 (System Board)",
                "eventMessageControl": "Per-threshold",
                "lowerCritical": "720.000",
                "lowerNonCritical": "840.000",
                "maximumSensorRange": "Unspecified",
                "minimumSensorRange": "Unspecified",
                "negativeHysteresis": "120.000",
                "nominalReading": "6720.000",
                "normalMaximum": "23640.000",
                "normalMinimum": "16680.000",
                "positiveHysteresis": "120.000",
                "readableThresholds": "lcr lnc",
                "sensorID": "0x33",
                "sensorName": "Fan2B RPM",
                "sensorReading": "4320 (+/- 120) RPM",
                "sensorType": "Fan",
                "settableThresholds": "",
                "status": "ok",
                "thresholdReadMask": "lcr lnc",
                "uniqueSensorID": "7.1:0x33"
              },
              {
                "assertionEvents": [],
                "assertionsEnabled": [],
                "deassertionsEnabled": [],
                "entityID": "7.1 (System Board)",
                "eventMessageControl": "Per-threshold",
                "lowerCritical": "720.000",
                "lowerNonCritical": "840.000",
                "maximumSensorRange": "Unspecified",
                "minimumSensorRange": "Unspecified",
                "negativeHysteresis": "120.000",
                "nominalReading": "6720.000",
                "normalMaximum": "23640.000",
                "normalMinimum": "16680.000",
                "positiveHysteresis": "120.000",
                "readableThresholds": "lcr lnc",
                "sensorID": "0x35",
                "sensorName": "Fan3B RPM",
                "sensorReading": "4320 (+/- 120) RPM",
                "sensorType": "Fan",
                "settableThresholds": "",
                "status": "ok",
                "thresholdReadMask": "lcr lnc",
                "uniqueSensorID": "7.1:0x35"
              },
              {
                "assertionEvents": [],
                "assertionsEnabled": [],
                "deassertionsEnabled": [],
                "entityID": "7.1 (System Board)",
                "eventMessageControl": "Per-threshold",
                "lowerCritical": "720.000",
                "lowerNonCritical": "840.000",
                "maximumSensorRange": "Unspecified",
                "minimumSensorRange": "Unspecified",
                "negativeHysteresis": "120.000",
                "nominalReading": "6720.000",
                "normalMaximum": "23640.000",
                "normalMinimum": "16680.000",
                "positiveHysteresis": "120.000",
                "readableThresholds": "lcr lnc",
                "sensorID": "0x37",
                "sensorName": "Fan4B RPM",
                "sensorReading": "4320 (+/- 120) RPM",
                "sensorType": "Fan",
                "settableThresholds": "",
                "status": "ok",
                "thresholdReadMask": "lcr lnc",
                "uniqueSensorID": "7.1:0x37"
              },
              {
                "assertionEvents": [],
                "assertionsEnabled": [],
                "deassertionsEnabled": [],
                "entityID": "7.1 (System Board)",
                "eventMessageControl": "Per-threshold",
                "lowerCritical": "720.000",
                "lowerNonCritical": "840.000",
                "maximumSensorRange": "Unspecified",
                "minimumSensorRange": "Unspecified",
                "negativeHysteresis": "120.000",
                "nominalReading": "6720.000",
                "normalMaximum": "23640.000",
                "normalMinimum": "16680.000",
                "positiveHysteresis": "120.000",
                "readableThresholds": "lcr lnc",
                "sensorID": "0x39",
                "sensorName": "Fan5B RPM",
                "sensorReading": "4320 (+/- 120) RPM",
                "sensorType": "Fan",
                "settableThresholds": "",
                "status": "ok",
                "thresholdReadMask": "lcr lnc",
                "uniqueSensorID": "7.1:0x39"
              },
              {
                "assertionEvents": [],
                "assertionsEnabled": [],
                "deassertionsEnabled": [],
                "entityID": "7.1 (System Board)",
                "eventMessageControl": "Per-threshold",
                "lowerCritical": "720.000",
                "lowerNonCritical": "840.000",
                "maximumSensorRange": "Unspecified",
                "minimumSensorRange": "Unspecified",
                "negativeHysteresis": "120.000",
                "nominalReading": "6720.000",
                "normalMaximum": "23640.000",
                "normalMinimum": "16680.000",
                "positiveHysteresis": "120.000",
                "readableThresholds": "lcr lnc",
                "sensorID": "0x3b",
                "sensorName": "Fan6B RPM",
                "sensorReading": "4320 (+/- 120) RPM",
                "sensorType": "Fan",
                "settableThresholds": "",
                "status": "ok",
                "thresholdReadMask": "lcr lnc",
                "uniqueSensorID": "7.1:0x3b"
              },
              {
                "assertionEvents": [],
                "assertionsEnabled": [],
                "deassertionsEnabled": [],
                "entityID": "7.1 (System Board)",
                "eventMessageControl": "Per-threshold",
                "lowerCritical": "720.000",
                "lowerNonCritical": "840.000",
                "maximumSensorRange": "Unspecified",
                "minimumSensorRange": "Unspecified",
                "negativeHysteresis": "120.000",
                "nominalReading": "6720.000",
                "normalMaximum": "23640.000",
                "normalMinimum": "16680.000",
                "positiveHysteresis": "120.000",
                "readableThresholds": "lcr lnc",
                "sensorID": "0x3d",
                "sensorName": "Fan7B RPM",
                "sensorReading": "4320 (+/- 120) RPM",
                "sensorType": "Fan",
                "settableThresholds": "",
                "status": "ok",
                "thresholdReadMask": "lcr lnc",
                "uniqueSensorID": "7.1:0x3d"
              },
              {
                "entityID": "7.1 (System Board)",
                "sensorID": "0x66",
                "sensorName": "PFault Fail Safe",
                "sensorType": "Voltage",
                "uniqueSensorID": "7.1:0x66"
              },
              {
                "assertionEvents": [
                  "Presence Detected"
                ],
                "entityID": "32.1 (Memory Device)",
                "sensorID": "0xc0",
                "sensorName": "A",
                "sensorType": "Memory",
                "statesAsserted": [
                  "Presence Detected"
                ],
                "uniqueSensorID": "32.1:0xc0"
              },
              {
                "assertionEvents": [
                  "Presence Detected"
                ],
                "entityID": "32.1 (Memory Device)",
                "sensorID": "0xcc",
                "sensorName": "B",
                "sensorType": "Memory",
                "statesAsserted": [
                  "Presence Detected"
                ],
                "uniqueSensorID": "32.1:0xcc"
              }
            ]
          }
        }
      },
      {
        "nodeID": 3,
        "result": {
          "ipmiInfo": {
            "sensors": [
              {
                "entityID": "7.1 (System Board)",
                "sensorID": "0x72",
                "sensorName": "SEL",
                "sensorType": "Event Logging Disabled",
                "uniqueSensorID": "7.1:0x72"
              },
              {
                "assertionsEnabled": [
                  "General Chassis intrusion"
                ],
                "deassertionsEnabled": [
                  "General Chassis intrusion"
                ],
                "entityID": "7.1 (System Board)",
                "sensorID": "0x73",
                "sensorName": "Intrusion",
                "sensorType": "Physical Security",
                "uniqueSensorID": "7.1:0x73"
              },
              {
                "assertionEvents": [],
                "assertionsEnabled": [],
                "deassertionsEnabled": [],
                "entityID": "7.1 (System Board)",
                "eventMessageControl": "Per-threshold",
                "lowerCritical": "720.000",
                "lowerNonCritical": "840.000",
                "maximumSensorRange": "Unspecified",
                "minimumSensorRange": "Unspecified",
                "negativeHysteresis": "600.000",
                "nominalReading": "10080.000",
                "normalMaximum": "23640.000",
                "normalMinimum": "16680.000",
                "positiveHysteresis": "600.000",
                "readableThresholds": "lcr lnc",
                "sensorID": "0x30",
                "sensorName": "Fan1A RPM",
                "sensorReading": "4320 (+/- 120) RPM",
                "sensorType": "Fan",
                "settableThresholds": "",
                "status": "ok",
                "thresholdReadMask": "lcr lnc",
                "uniqueSensorID": "7.1:0x30"
              },
              {
                "assertionEvents": [],
                "assertionsEnabled": [],
                "deassertionsEnabled": [],
                "entityID": "7.1 (System Board)",
                "eventMessageControl": "Per-threshold",
                "lowerCritical": "720.000",
                "lowerNonCritical": "840.000",
                "maximumSensorRange": "Unspecified",
                "minimumSensorRange": "Unspecified",
                "negativeHysteresis": "600.000",
                "nominalReading": "10080.000",
                "normalMaximum": "23640.000",
                "normalMinimum": "16680.000",
                "positiveHysteresis": "600.000",
                "readableThresholds": "lcr lnc",
                "sensorID": "0x32",
                "sensorName": "Fan2A RPM",
                "sensorReading": "4440 (+/- 120) RPM",
                "sensorType": "Fan",
                "settableThresholds": "",
                "status": "ok",
                "thresholdReadMask": "lcr lnc",
                "uniqueSensorID": "7.1:0x32"
              },
              {
                "assertionEvents": [],
                "assertionsEnabled": [],
                "deassertionsEnabled": [],
                "entityID": "7.1 (System Board)",
                "eventMessageControl": "Per-threshold",
                "lowerCritical": "720.000",
                "lowerNonCritical": "840.000",
                "maximumSensorRange": "Unspecified",
                "minimumSensorRange": "Unspecified",
                "negativeHysteresis": "600.000",
                "nominalReading": "10080.000",
                "normalMaximum": "23640.000",
                "normalMinimum": "16680.000",
                "positiveHysteresis": "600.000",
                "readableThresholds": "lcr lnc",
                "sensorID": "0x34",
                "sensorName": "Fan3A RPM",
                "sensorReading": "4320 (+/- 120) RPM",
                "sensorType": "Fan",
                "settableThresholds": "",
                "status": "ok",
                "thresholdReadMask": "lcr lnc",
                "uniqueSensorID": "7.1:0x34"
              },
              {
                "assertionEvents": [],
                "assertionsEnabled": [],
                "deassertionsEnabled": [],
                "entityID": "7.1 (System Board)",
                "eventMessageControl": "Per-threshold",
                "lowerCritical": "720.000",
                "lowerNonCritical": "840.000",
                "maximumSensorRange": "Unspecified",
                "minimumSensorRange": "Unspecified",
                "negativeHysteresis": "600.000",
                "nominalReading": "10080.000",
                "normalMaximum": "23640.000",
                "normalMinimum": "16680.000",
                "positiveHysteresis": "600.000",
                "readableThresholds": "lcr lnc",
                "sensorID": "0x36",
                "sensorName": "Fan4A RPM",
                "sensorReading": "4200 (+/- 120) RPM",
                "sensorType": "Fan",
                "settableThresholds": "",
                "status": "ok",
                "thresholdReadMask": "lcr lnc",
                "uniqueSensorID": "7.1:0x36"
              },
              {
                "assertionEvents": [],
                "assertionsEnabled": [],
                "deassertionsEnabled": [],
                "entityID": "7.1 (System Board)",
                "eventMessageControl": "Per-threshold",
                "lowerCritical": "720.000",
                "lowerNonCritical": "840.000",
                "maximumSensorRange": "Unspecified",
                "minimumSensorRange": "Unspecified",
                "negativeHysteresis": "600.000",
                "nominalReading": "6720.000",
                "normalMaximum": "23640.000",
                "normalMinimum": "16680.000",
                "positiveHysteresis": "600.000",
                "readableThresholds": "lcr lnc",
                "sensorID": "0x38",
                "sensorName": "Fan5A RPM",
                "sensorReading": "4320 (+/- 120) RPM",
                "sensorType": "Fan",
                "settableThresholds": "",
                "status": "ok",
                "thresholdReadMask": "lcr lnc",
                "uniqueSensorID": "7.1:0x38"
              },
              {
                "assertionEvents": [],
                "assertionsEnabled": [],
                "deassertionsEnabled": [],
                "entityID": "7.1 (System Board)",
                "eventMessageControl": "Per-threshold",
                "lowerCritical": "720.000",
                "lowerNonCritical": "840.000",
                "maximumSensorRange": "Unspecified",
                "minimumSensorRange": "Unspecified",
                "negativeHysteresis": "600.000",
                "nominalReading": "6720.000",
                "normalMaximum": "23640.000",
                "normalMinimum": "16680.000",
                "positiveHysteresis": "600.000",
                "readableThresholds": "lcr lnc",
                "sensorID": "0x3a",
                "sensorName": "Fan6A RPM",
                "sensorReading": "4320 (+/- 120) RPM",
                "sensorType": "Fan",
                "settableThresholds": "",
                "status": "ok",
                "thresholdReadMask": "lcr lnc",
                "uniqueSensorID": "7.1:0x3a"
              },
              {
                "assertionEvents": [],
                "assertionsEnabled": [],
                "deassertionsEnabled": [],
                "entityID": "7.1 (System Board)",
                "eventMessageControl": "Per-threshold",
                "lowerCritical": "-7.000",
                "lowerNonCritical": "3.000",
                "maximumSensorRange": "Unspecified",
                "minimumSensorRange": "Unspecified",
                "negativeHysteresis": "1.000",
                "nominalReading": "23.000",
                "normalMaximum": "69.000",
                "normalMinimum": "11.000",
                "positiveHysteresis": "1.000",
                "readableThresholds": "lcr lnc unc ucr",
                "sensorID": "0x4",
                "sensorName": "Inlet Temp",
                "sensorReading": "21 (+/- 1) degrees C",
                "sensorType": "Temperature",
                "settableThresholds": "lcr lnc unc ucr",
                "status": "ok",
                "thresholdReadMask": "lcr lnc unc ucr",
                "uniqueSensorID": "7.1:0x4",
                "upperCritical": "47.000",
                "upperNonCritical": "42.000"
              },
              {
                "assertionEvents": [],
                "assertionsEnabled": [],
                "entityID": "7.1 (System Board)",
                "eventMessageControl": "Per-threshold",
                "lowerCritical": "3.000",
                "lowerNonCritical": "8.000",
                "maximumSensorRange": "Unspecified",
                "minimumSensorRange": "Unspecified",
                "negativeHysteresis": "1.000",
                "nominalReading": "23.000",
                "normalMaximum": "69.000",
                "normalMinimum": "11.000",
                "positiveHysteresis": "1.000",
                "readableThresholds": "lcr lnc unc ucr",
                "sensorID": "0x1",
                "sensorName": "Exhaust Temp",
                "sensorReading": "38 (+/- 1) degrees C",
                "sensorType": "Temperature",
                "settableThresholds": "",
                "status": "ok",
                "uniqueSensorID": "7.1:0x1",
                "upperCritical": "75.000",
                "upperNonCritical": "70.000"
              },
              {
                "assertionEvents": [],
                "assertionsEnabled": [],
                "entityID": "3.1 (Processor)",
                "eventMessageControl": "Per-threshold",
                "maximumSensorRange": "Unspecified",
                "minimumSensorRange": "Unspecified",
                "negativeHysteresis": "1.000",
                "nominalReading": "23.000",
                "normalMaximum": "69.000",
                "normalMinimum": "11.000",
                "positiveHysteresis": "1.000",
                "readableThresholds": "unc",
                "sensorID": "0xe",
                "sensorName": "Temp",
                "sensorReading": "-80 (+/- 1) unspecified",
                "sensorType": "Temperature",
                "settableThresholds": "",
                "status": "ok",
                "uniqueSensorID": "3.1:0xe",
                "upperNonCritical": "0.000"
              },
              {
                "assertionEvents": [],
                "assertionsEnabled": [],
                "entityID": "3.2 (Processor)",
                "eventMessageControl": "Per-threshold",
                "maximumSensorRange": "Unspecified",
                "minimumSensorRange": "Unspecified",
                "negativeHysteresis": "1.000",
                "nominalReading": "23.000",
                "normalMaximum": "69.000",
                "normalMinimum": "11.000",
                "positiveHysteresis": "1.000",
                "readableThresholds": "unc",
                "sensorID": "0xf",
                "sensorName": "Temp",
                "sensorReading": "-80 (+/- 1) unspecified",
                "sensorType": "Temperature",
                "settableThresholds": "",
                "status": "ok",
                "uniqueSensorID": "3.2:0xf",
                "upperNonCritical": "0.000"
              },
              {
                "assertionsEnabled": [
                  "Timer expired",
                  "Hard reset",
                  "Power down",
                  "Power cycle"
                ],
                "deassertionsEnabled": [
                  "Timer expired",
                  "Hard reset",
                  "Power down",
                  "Power cycle"
                ],
                "entityID": "7.1 (System Board)",
                "sensorID": "0x71",
                "sensorName": "OS Watchdog",
                "sensorType": "Watchdog",
                "uniqueSensorID": "7.1:0x71"
              },
              {
                "assertionEvents": [
                  "State Deasserted"
                ],
                "assertionsEnabled": [
                  "State Deasserted",
                  "State Asserted"
                ],
                "deassertionsEnabled": [
                  "State Deasserted",
                  "State Asserted"
                ],
                "entityID": "3.1 (Processor)",
                "sensorID": "0x23",
                "sensorName": "VCORE PG",
                "sensorType": "Voltage",
                "statesAsserted": [
                  "State Deasserted"
                ],
                "uniqueSensorID": "3.1:0x23"
              },
              {
                "assertionEvents": [
                  "State Deasserted"
                ],
                "assertionsEnabled": [
                  "State Deasserted",
                  "State Asserted"
                ],
                "entityID": "3.2 (Processor)",
                "sensorID": "0x24",
                "sensorName": "VCORE PG",
                "sensorType": "Voltage",
                "statesAsserted": [
                  "State Deasserted"
                ],
                "uniqueSensorID": "3.2:0x24"
              },
              {
                "assertionEvents": [
                  "State Deasserted"
                ],
                "assertionsEnabled": [
                  "State Deasserted",
                  "State Asserted"
                ],
                "entityID": "7.1 (System Board)",
                "sensorID": "0x19",
                "sensorName": "3.3V PG",
                "sensorType": "Voltage",
                "statesAsserted": [
                  "State Deasserted"
                ],
                "uniqueSensorID": "7.1:0x19"
              },
              {
                "assertionEvents": [
                  "State Deasserted"
                ],
                "assertionsEnabled": [
                  "State Deasserted",
                  "State Asserted"
                ],
                "entityID": "7.1 (System Board)",
                "sensorID": "0x1a",
                "sensorName": "5V PG",
                "sensorType": "Voltage",
                "statesAsserted": [
                  "State Deasserted"
                ],
                "uniqueSensorID": "7.1:0x1a"
              },
              {
                "assertionEvents": [
                  "Connected"
                ],
                "assertionsEnabled": [
                  "Config Error"
                ],
                "deassertionsEnabled": [
                  "Config Error"
                ],
                "entityID": "7.1 (System Board)",
                "sensorID": "0x50",
                "sensorName": "USB Cable Pres",
                "sensorType": "Cable / Interconnect",
                "statesAsserted": [
                  "Connected"
                ],
                "uniqueSensorID": "7.1:0x50"
              },
              {
                "assertionsEnabled": [
                  "Config Error"
                ],
                "deassertionsEnabled": [
                  "Config Error"
                ],
                "entityID": "7.1 (System Board)",
                "sensorID": "0x51",
                "sensorName": "VGA Cable Pres",
                "sensorType": "Cable / Interconnect",
                "uniqueSensorID": "7.1:0x51"
              },
              {
                "assertionEvents": [
                  "Present"
                ],
                "entityID": "7.1 (System Board)",
                "sensorID": "0x70",
                "sensorName": "Dedicated NIC",
                "sensorType": "Entity Presence",
                "statesAsserted": [
                  "Present"
                ],
                "uniqueSensorID": "7.1:0x70"
              },
              {
                "assertionEvents": [
                  "Absent"
                ],
                "entityID": "11.2 (Add-in Card)",
                "sensorID": "0x49",
                "sensorName": "Presence",
                "sensorType": "Entity Presence",
                "statesAsserted": [
                  "Absent"
                ],
                "uniqueSensorID": "11.2:0x49"
              },
              {
                "assertionEvents": [
                  "Present"
                ],
                "entityID": "3.1 (Processor)",
                "sensorID": "0x40",
                "sensorName": "Presence",
                "sensorType": "Entity Presence",
                "statesAsserted": [
                  "Present"
                ],
                "uniqueSensorID": "3.1:0x40"
              },
              {
                "assertionEvents": [
                  "Present"
                ],
                "entityID": "3.2 (Processor)",
                "sensorID": "0x41",
                "sensorName": "Presence",
                "sensorType": "Entity Presence",
                "statesAsserted": [
                  "Present"
                ],
                "uniqueSensorID": "3.2:0x41"
              },
              {
                "assertionEvents": [
                  "State Deasserted"
                ],
                "assertionsEnabled": [
                  "State Deasserted",
                  "State Asserted"
                ],
                "entityID": "3.2 (Processor)",
                "sensorID": "0x22",
                "sensorName": "PLL PG",
                "sensorType": "Voltage",
                "statesAsserted": [
                  "State Deasserted"
                ],
                "uniqueSensorID": "3.2:0x22"
              },
              {
                "assertionEvents": [
                  "State Deasserted"
                ],
                "assertionsEnabled": [
                  "State Deasserted",
                  "State Asserted"
                ],
                "entityID": "3.1 (Processor)",
                "sensorID": "0x25",
                "sensorName": "PLL PG",
                "sensorType": "Voltage",
                "statesAsserted": [
                  "State Deasserted"
                ],
                "uniqueSensorID": "3.1:0x25"
              },
              {
                "assertionEvents": [
                  "State Deasserted"
                ],
                "assertionsEnabled": [
                  "State Deasserted",
                  "State Asserted"
                ],
                "entityID": "7.1 (System Board)",
                "sensorID": "0x27",
                "sensorName": "1.1V PG",
                "sensorType": "Voltage",
                "statesAsserted": [
                  "State Deasserted"
                ],
                "uniqueSensorID": "7.1:0x27"
              },
              {
                "assertionEvents": [
                  "State Deasserted"
                ],
                "assertionsEnabled": [
                  "State Deasserted",
                  "State Asserted"
                ],
                "entityID": "3.1 (Processor)",
                "sensorID": "0x15",
                "sensorName": "M23 VDDQ PG",
                "sensorType": "Voltage",
                "statesAsserted": [
                  "State Deasserted"
                ],
                "uniqueSensorID": "3.1:0x15"
              },
              {
                "assertionEvents": [
                  "State Deasserted"
                ],
                "assertionsEnabled": [
                  "State Deasserted",
                  "State Asserted"
                ],
                "entityID": "3.1 (Processor)",
                "sensorID": "0x16",
                "sensorName": "M23 VTT PG",
                "sensorType": "Voltage",
                "statesAsserted": [
                  "State Deasserted"
                ],
                "uniqueSensorID": "3.1:0x16"
              },
              {
                "assertionEvents": [
                  "State Deasserted"
                ],
                "assertionsEnabled": [
                  "State Deasserted",
                  "State Asserted"
                ],
                "entityID": "7.1 (System Board)",
                "sensorID": "0x21",
                "sensorName": "FETDRV PG",
                "sensorType": "Voltage",
                "statesAsserted": [
                  "State Deasserted"
                ],
                "uniqueSensorID": "7.1:0x21"
              },
              {
                "assertionEvents": [
                  "Present"
                ],
                "entityID": "10.2 (Power Supply)",
                "sensorID": "0x43",
                "sensorName": "Presence",
                "sensorType": "Entity Presence",
                "statesAsserted": [
                  "Present"
                ],
                "uniqueSensorID": "10.2:0x43"
              },
              {
                "assertionEvents": [
                  "State Deasserted"
                ],
                "assertionsEnabled": [
                  "State Deasserted",
                  "State Asserted"
                ],
                "entityID": "3.2 (Processor)",
                "sensorID": "0x29",
                "sensorName": "VSA PG",
                "sensorType": "Voltage",
                "statesAsserted": [
                  "State Deasserted"
                ],
                "uniqueSensorID": "3.2:0x29"
              },
              {
                "assertionEvents": [
                  "State Deasserted"
                ],
                "assertionsEnabled": [
                  "State Deasserted",
                  "State Asserted"
                ],
                "entityID": "3.1 (Processor)",
                "sensorID": "0x2b",
                "sensorName": "VSA PG",
                "sensorType": "Voltage",
                "statesAsserted": [
                  "State Deasserted"
                ],
                "uniqueSensorID": "3.1:0x2b"
              },
              {
                "assertionEvents": [
                  "State Deasserted"
                ],
                "assertionsEnabled": [
                  "State Deasserted",
                  "State Asserted"
                ],
                "entityID": "3.2 (Processor)",
                "sensorID": "0x1b",
                "sensorName": "M01 VDDQ PG",
                "sensorType": "Voltage",
                "statesAsserted": [
                  "State Deasserted"
                ],
                "uniqueSensorID": "3.2:0x1b"
              },
              {
                "assertionEvents": [
                  "State Deasserted"
                ],
                "assertionsEnabled": [
                  "State Deasserted",
                  "State Asserted"
                ],
                "entityID": "3.1 (Processor)",
                "sensorID": "0x1e",
                "sensorName": "M01 VDDQ PG",
                "sensorType": "Voltage",
                "statesAsserted": [
                  "State Deasserted"
                ],
                "uniqueSensorID": "3.1:0x1e"
              },
              {
                "assertionEvents": [
                  "State Deasserted"
                ],
                "assertionsEnabled": [
                  "State Deasserted",
                  "State Asserted"
                ],
                "entityID": "3.2 (Processor)",
                "sensorID": "0x2e",
                "sensorName": "M23 VTT PG",
                "sensorType": "Voltage",
                "statesAsserted": [
                  "State Deasserted"
                ],
                "uniqueSensorID": "3.2:0x2e"
              },
              {
                "assertionEvents": [
                  "State Deasserted"
                ],
                "assertionsEnabled": [
                  "State Deasserted",
                  "State Asserted"
                ],
                "entityID": "3.2 (Processor)",
                "sensorID": "0x1c",
                "sensorName": "M01 VTT PG",
                "sensorType": "Voltage",
                "statesAsserted": [
                  "State Deasserted"
                ],
                "uniqueSensorID": "3.2:0x1c"
              },
              {
                "assertionEvents": [
                  "State Deasserted"
                ],
                "assertionsEnabled": [
                  "State Deasserted",
                  "State Asserted"
                ],
                "entityID": "7.1 (System Board)",
                "sensorID": "0x2f",
                "sensorName": "NDC PG",
                "sensorType": "Voltage",
                "statesAsserted": [
                  "State Deasserted"
                ],
                "uniqueSensorID": "7.1:0x2f"
              },
              {
                "entityID": "7.1 (System Board)",
                "sensorID": "0x4c",
                "sensorName": "LCD Cable Pres",
                "sensorType": "Cable / Interconnect",
                "uniqueSensorID": "7.1:0x4c"
              },
              {
                "assertionEvents": [
                  "State Deasserted"
                ],
                "assertionsEnabled": [
                  "State Deasserted",
                  "State Asserted"
                ],
                "entityID": "3.2 (Processor)",
                "sensorID": "0x1f",
                "sensorName": "VTT PG",
                "sensorType": "Voltage",
                "statesAsserted": [
                  "State Deasserted"
                ],
                "uniqueSensorID": "3.2:0x1f"
              },
              {
                "assertionEvents": [
                  "State Deasserted"
                ],
                "assertionsEnabled": [
                  "State Deasserted",
                  "State Asserted"
                ],
                "entityID": "3.1 (Processor)",
                "sensorID": "0x20",
                "sensorName": "VTT PG",
                "sensorType": "Voltage",
                "statesAsserted": [
                  "State Deasserted"
                ],
                "uniqueSensorID": "3.1:0x20"
              },
              {
                "assertionEvents": [
                  "State Deasserted"
                ],
                "assertionsEnabled": [
                  "State Deasserted",
                  "State Asserted"
                ],
                "entityID": "3.2 (Processor)",
                "sensorID": "0x1d",
                "sensorName": "M23 VDDQ PG",
                "sensorType": "Voltage",
                "statesAsserted": [
                  "State Deasserted"
                ],
                "uniqueSensorID": "3.2:0x1d"
              },
              {
                "assertionEvents": [
                  "Present"
                ],
                "assertionsEnabled": [
                  "Present",
                  "Absent"
                ],
                "entityID": "11.1 (Add-in Card)",
                "sensorID": "0x4a",
                "sensorName": "Presence",
                "sensorType": "Entity Presence",
                "statesAsserted": [
                  "Present"
                ],
                "uniqueSensorID": "11.1:0x4a"
              },
              {
                "assertionEvents": [
                  "Absent"
                ],
                "entityID": "11.3 (Add-in Card)",
                "sensorID": "0x48",
                "sensorName": "Presence",
                "sensorType": "Entity Presence",
                "statesAsserted": [
                  "Absent"
                ],
                "uniqueSensorID": "11.3:0x48"
              },
              {
                "assertionEvents": [
                  "Presence detected"
                ],
                "assertionsEnabled": [
                  "IERR",
                  "Thermal Trip",
                  "Configuration Error",
                  "Presence detected",
                  "Throttled"
                ],
                "deassertionsEnabled": [
                  "IERR",
                  "Thermal Trip",
                  "Configuration Error",
                  "Presence detected",
                  "Throttled"
                ],
                "entityID": "3.1 (Processor)",
                "sensorID": "0x60",
                "sensorName": "Status",
                "sensorType": "Processor",
                "statesAsserted": [
                  "Presence detected"
                ],
                "uniqueSensorID": "3.1:0x60"
              },
              {
                "assertionEvents": [
                  "Presence detected"
                ],
                "assertionsEnabled": [
                  "IERR",
                  "Thermal Trip",
                  "Configuration Error",
                  "Throttled"
                ],
                "deassertionsEnabled": [
                  "IERR",
                  "Thermal Trip",
                  "Configuration Error",
                  "Throttled"
                ],
                "entityID": "3.2 (Processor)",
                "sensorID": "0x61",
                "sensorName": "Status",
                "sensorType": "Processor",
                "statesAsserted": [
                  "Presence detected"
                ],
                "uniqueSensorID": "3.2:0x61"
              },
              {
                "assertionEvents": [
                  "Fully Redundant"
                ],
                "assertionsEnabled": [
                  "Fully Redundant",
                  "Redundancy Lost"
                ],
                "entityID": "7.1 (System Board)",
                "sensorID": "0x75",
                "sensorName": "Fan Redundancy",
                "sensorType": "Fan",
                "statesAsserted": [
                  "Fully Redundant"
                ],
                "uniqueSensorID": "7.1:0x75"
              },
              {
                "assertionsEnabled": [
                  "Config Error"
                ],
                "deassertionsEnabled": [
                  "Config Error"
                ],
                "entityID": "7.1 (System Board)",
                "sensorID": "0x64",
                "sensorName": "Riser Config Err",
                "sensorType": "Cable / Interconnect",
                "uniqueSensorID": "7.1:0x64"
              },
              {
                "assertionEvents": [
                  "Connected"
                ],
                "assertionsEnabled": [
                  "Config Error"
                ],
                "deassertionsEnabled": [
                  "Config Error"
                ],
                "entityID": "7.1 (System Board)",
                "sensorID": "0x4f",
                "sensorName": "Riser 3 Presence",
                "sensorType": "Cable / Interconnect",
                "statesAsserted": [
                  "Connected"
                ],
                "uniqueSensorID": "7.1:0x4f"
              },
              {
                "assertionEvents": [
                  "State Deasserted"
                ],
                "assertionsEnabled": [
                  "State Deasserted",
                  "State Asserted"
                ],
                "entityID": "7.1 (System Board)",
                "sensorID": "0x28",
                "sensorName": "1.5V PG",
                "sensorType": "Voltage",
                "statesAsserted": [
                  "State Deasserted"
                ],
                "uniqueSensorID": "7.1:0x28"
              },
              {
                "assertionEvents": [
                  "State Deasserted"
                ],
                "assertionsEnabled": [
                  "State Deasserted",
                  "State Asserted"
                ],
                "entityID": "7.1 (System Board)",
                "sensorID": "0xf6",
                "sensorName": "BP1 5V PG",
                "sensorType": "Voltage",
                "statesAsserted": [
                  "State Deasserted"
                ],
                "uniqueSensorID": "7.1:0xf6"
              },
              {
                "assertionEvents": [
                  "State Deasserted"
                ],
                "assertionsEnabled": [
                  "State Deasserted",
                  "State Asserted"
                ],
                "entityID": "7.1 (System Board)",
                "sensorID": "0xf7",
                "sensorName": "BP2 5V PG",
                "sensorType": "Voltage",
                "uniqueSensorID": "7.1:0xf7"
              },
              {
                "assertionEvents": [
                  "State Deasserted"
                ],
                "assertionsEnabled": [
                  "State Deasserted",
                  "State Asserted"
                ],
                "entityID": "3.1 (Processor)",
                "sensorID": "0x14",
                "sensorName": "M01 VTT PG",
                "sensorType": "Voltage",
                "statesAsserted": [
                  "State Deasserted"
                ],
                "uniqueSensorID": "3.1:0x14"
              },
              {
                "assertionEvents": [
                  "Present"
                ],
                "entityID": "10.1 (Power Supply)",
                "sensorID": "0x42",
                "sensorName": "Presence",
                "sensorType": "Entity Presence",
                "statesAsserted": [
                  "Present"
                ],
                "uniqueSensorID": "10.1:0x42"
              },
              {
                "assertionsEnabled": [
                  "NMI/Diag Interrupt",
                  "Bus Timeout"
                ],
                "deassertionsEnabled": [
                  "NMI/Diag Interrupt",
                  "Bus Timeout"
                ],
                "entityID": "7.1 (System Board)",
                "sensorID": "0x90",
                "sensorName": "PCIe Slot1",
                "sensorType": "Critical Interrupt",
                "uniqueSensorID": "7.1:0x90"
              },
              {
                "assertionsEnabled": [
                  "NMI/Diag Interrupt",
                  "Bus Timeout"
                ],
                "deassertionsEnabled": [
                  "NMI/Diag Interrupt",
                  "Bus Timeout"
                ],
                "entityID": "7.1 (System Board)",
                "sensorID": "0x91",
                "sensorName": "PCIe Slot2",
                "sensorType": "Critical Interrupt",
                "uniqueSensorID": "7.1:0x91"
              },
              {
                "assertionsEnabled": [
                  "NMI/Diag Interrupt",
                  "Bus Timeout"
                ],
                "deassertionsEnabled": [
                  "NMI/Diag Interrupt",
                  "Bus Timeout"
                ],
                "entityID": "7.1 (System Board)",
                "sensorID": "0x92",
                "sensorName": "PCIe Slot3",
                "sensorType": "Critical Interrupt",
                "uniqueSensorID": "7.1:0x92"
              },
              {
                "assertionsEnabled": [
                  "NMI/Diag Interrupt",
                  "Bus Timeout"
                ],
                "deassertionsEnabled": [
                  "NMI/Diag Interrupt",
                  "Bus Timeout"
                ],
                "entityID": "7.1 (System Board)",
                "sensorID": "0x93",
                "sensorName": "PCIe Slot4",
                "sensorType": "Critical Interrupt",
                "uniqueSensorID": "7.1:0x93"
              },
              {
                "assertionsEnabled": [
                  "NMI/Diag Interrupt",
                  "Bus Timeout"
                ],
                "deassertionsEnabled": [
                  "NMI/Diag Interrupt",
                  "Bus Timeout"
                ],
                "entityID": "7.1 (System Board)",
                "sensorID": "0x94",
                "sensorName": "PCIe Slot5",
                "sensorType": "Critical Interrupt",
                "uniqueSensorID": "7.1:0x94"
              },
              {
                "assertionsEnabled": [
                  "NMI/Diag Interrupt",
                  "Bus Timeout"
                ],
                "deassertionsEnabled": [
                  "NMI/Diag Interrupt",
                  "Bus Timeout"
                ],
                "entityID": "7.1 (System Board)",
                "sensorID": "0x95",
                "sensorName": "PCIe Slot6",
                "sensorType": "Critical Interrupt",
                "uniqueSensorID": "7.1:0x95"
              },
              {
                "assertionsEnabled": [
                  "NMI/Diag Interrupt",
                  "Bus Timeout"
                ],
                "deassertionsEnabled": [
                  "NMI/Diag Interrupt",
                  "Bus Timeout"
                ],
                "entityID": "7.1 (System Board)",
                "sensorID": "0x96",
                "sensorName": "PCIe Slot7",
                "sensorType": "Critical Interrupt",
                "uniqueSensorID": "7.1:0x96"
              },
              {
                "entityID": "7.1 (System Board)",
                "sensorID": "0xfa",
                "sensorName": "vFlash",
                "sensorType": "Module / Board",
                "uniqueSensorID": "7.1:0xfa"
              },
              {
                "assertionsEnabled": [
                  "Failed"
                ],
                "deassertionsEnabled": [
                  "Failed"
                ],
                "entityID": "7.1 (System Board)",
                "sensorID": "0x65",
                "sensorName": "CMOS Battery",
                "sensorType": "Battery",
                "uniqueSensorID": "7.1:0x65"
              },
              {
                "assertionsEnabled": [
                  "Failed"
                ],
                "deassertionsEnabled": [
                  "Failed"
                ],
                "entityID": "11.2 (Add-in Card)",
                "eventStatus": "Unavailable",
                "sensorID": "0x68",
                "sensorName": "ROMB Battery",
                "sensorType": "Battery",
                "uniqueSensorID": "11.2:0x68"
              },
              {
                "assertionsEnabled": [
                  "Failed"
                ],
                "deassertionsEnabled": [
                  "Failed"
                ],
                "entityID": "11.4 (Add-in Card)",
                "eventStatus": "Unavailable",
                "sensorID": "0x69",
                "sensorName": "ROMB Battery",
                "sensorType": "Battery",
                "uniqueSensorID": "11.4:0x69"
              },
              {
                "assertionEvents": [
                  "Present"
                ],
                "entityID": "26.1 (Disk Drive Bay)",
                "sensorID": "0x54",
                "sensorName": "Presence",
                "sensorType": "Entity Presence",
                "statesAsserted": [
                  "Present"
                ],
                "uniqueSensorID": "26.1:0x54"
              },
              {
                "assertionEvents": [
                  "Absent"
                ],
                "entityID": "26.2 (Disk Drive Bay)",
                "sensorID": "0x55",
                "sensorName": "Presence",
                "sensorType": "Entity Presence",
                "statesAsserted": [
                  "Absent"
                ],
                "uniqueSensorID": "26.2:0x55"
              },
              {
                "assertionEvents": [],
                "assertionsEnabled": [],
                "entityID": "10.1 (Power Supply)",
                "eventMessageControl": "Per-threshold",
                "maximumSensorRange": "Unspecified",
                "minimumSensorRange": "Unspecified",
                "negativeHysteresis": "Unspecified",
                "nominalReading": "0.000",
                "normalMaximum": "0.000",
                "positiveHysteresis": "Unspecified",
                "readableThresholds": "No Thresholds",
                "sensorID": "0x6a",
                "sensorName": "Current 1",
                "sensorReading": "1.200 (+/- 0) Amps",
                "sensorType": "Current",
                "settableThresholds": "No Thresholds",
                "status": "ok",
                "uniqueSensorID": "10.1:0x6a"
              },
              {
                "assertionEvents": [],
                "assertionsEnabled": [],
                "entityID": "10.2 (Power Supply)",
                "eventMessageControl": "Per-threshold",
                "maximumSensorRange": "Unspecified",
                "minimumSensorRange": "Unspecified",
                "negativeHysteresis": "Unspecified",
                "nominalReading": "0.000",
                "normalMaximum": "0.000",
                "positiveHysteresis": "Unspecified",
                "readableThresholds": "No Thresholds",
                "sensorID": "0x6b",
                "sensorName": "Current 2",
                "sensorReading": "0.200 (+/- 0) Amps",
                "sensorType": "Current",
                "settableThresholds": "No Thresholds",
                "status": "ok",
                "uniqueSensorID": "10.2:0x6b"
              },
              {
                "assertionEvents": [],
                "assertionsEnabled": [],
                "entityID": "10.1 (Power Supply)",
                "eventMessageControl": "Per-threshold",
                "maximumSensorRange": "Unspecified",
                "minimumSensorRange": "Unspecified",
                "negativeHysteresis": "Unspecified",
                "nominalReading": "0.000",
                "normalMaximum": "0.000",
                "positiveHysteresis": "Unspecified",
                "readableThresholds": "No Thresholds",
                "sensorID": "0x6c",
                "sensorName": "Voltage 1",
                "sensorReading": "118 (+/- 0) Volts",
                "sensorType": "Voltage",
                "settableThresholds": "No Thresholds",
                "status": "ok",
                "uniqueSensorID": "10.1:0x6c"
              },
              {
                "assertionEvents": [],
                "assertionsEnabled": [],
                "entityID": "10.2 (Power Supply)",
                "eventMessageControl": "Per-threshold",
                "maximumSensorRange": "Unspecified",
                "minimumSensorRange": "Unspecified",
                "negativeHysteresis": "Unspecified",
                "nominalReading": "0.000",
                "normalMaximum": "0.000",
                "positiveHysteresis": "Unspecified",
                "readableThresholds": "No Thresholds",
                "sensorID": "0x6d",
                "sensorName": "Voltage 2",
                "sensorReading": "118 (+/- 0) Volts",
                "sensorType": "Voltage",
                "settableThresholds": "No Thresholds",
                "status": "ok",
                "uniqueSensorID": "10.2:0x6d"
              },
              {
                "assertionEvents": [
                  "Fully Redundant"
                ],
                "assertionsEnabled": [
                  "Fully Redundant",
                  "Redundancy Lost"
                ],
                "entityID": "7.1 (System Board)",
                "sensorID": "0x74",
                "sensorName": "PS Redundancy",
                "sensorType": "Power Supply",
                "statesAsserted": [
                  "Fully Redundant"
                ],
                "uniqueSensorID": "7.1:0x74"
              },
              {
                "assertionEvents": [
                  "Presence detected"
                ],
                "assertionsEnabled": [
                  "Presence detected",
                  "Failure detected",
                  "Predictive failure",
                  "Power Supply AC lost",
                  "Config Error: Vendor Mismatch",
                  "Config Error: Revision Mismatch",
                  "Config Error: Processor Missing",
                  "Config Error"
                ],
                "deassertionsEnabled": [
                  "Presence detected",
                  "Failure detected",
                  "Predictive failure",
                  "Power Supply AC lost",
                  "Config Error: Vendor Mismatch",
                  "Config Error: Revision Mismatch",
                  "Config Error: Processor Missing",
                  "Config Error"
                ],
                "entityID": "10.1 (Power Supply)",
                "sensorID": "0x62",
                "sensorName": "Status",
                "sensorType": "Power Supply",
                "statesAsserted": [
                  "Presence detected"
                ],
                "uniqueSensorID": "10.1:0x62"
              },
              {
                "assertionEvents": [
                  "Presence detected"
                ],
                "assertionsEnabled": [
                  "Presence detected",
                  "Failure detected",
                  "Predictive failure",
                  "Power Supply AC lost",
                  "Config Error: Vendor Mismatch",
                  "Config Error: Revision Mismatch",
                  "Config Error: Processor Missing",
                  "Config Error"
                ],
                "deassertionsEnabled": [
                  "Presence detected",
                  "Failure detected",
                  "Predictive failure",
                  "Power Supply AC lost",
                  "Config Error: Vendor Mismatch",
                  "Config Error: Revision Mismatch",
                  "Config Error: Processor Missing",
                  "Config Error"
                ],
                "entityID": "10.2 (Power Supply)",
                "sensorID": "0x63",
                "sensorName": "Status",
                "sensorType": "Power Supply",
                "statesAsserted": [
                  "Presence detected"
                ],
                "uniqueSensorID": "10.2:0x63"
              },
              {
                "assertionEvents": [],
                "assertionsEnabled": [],
                "deassertionsEnabled": [],
                "entityID": "7.1 (System Board)",
                "eventMessageControl": "Per-threshold",
                "maximumSensorRange": "3556.000",
                "minimumSensorRange": "Unspecified",
                "negativeHysteresis": "Unspecified",
                "nominalReading": "658.000",
                "normalMaximum": "672.000",
                "positiveHysteresis": "Unspecified",
                "readableThresholds": "unc ucr",
                "sensorID": "0x77",
                "sensorName": "Pwr Consumption",
                "sensorReading": "140 (+/- 0) Watts",
                "sensorType": "Current",
                "settableThresholds": "unc",
                "status": "ok",
                "uniqueSensorID": "7.1:0x77",
                "upperCritical": "1218.000",
                "upperNonCritical": "1106.000"
              },
              {
                "assertionEvents": [
                  "OEM Specific"
                ],
                "assertionsEnabled": [],
                "deassertionsEnabled": [],
                "entityID": "7.1 (System Board)",
                "sensorID": "0x76",
                "sensorName": "Power Optimized",
                "sensorType": "Unknown (0xC0)",
                "statesAsserted": [
                  "OEM Specific"
                ],
                "uniqueSensorID": "7.1:0x76"
              },
              {
                "entityID": "11.3 (Add-in Card)",
                "sensorID": "0xf4",
                "sensorName": "SD1",
                "sensorType": "Unknown (0xC9)",
                "uniqueSensorID": "11.3:0xf4"
              },
              {
                "entityID": "11.3 (Add-in Card)",
                "sensorID": "0xf5",
                "sensorName": "SD2",
                "sensorType": "Unknown (0xC9)",
                "uniqueSensorID": "11.3:0xf5"
              },
              {
                "assertionEvents": [
                  "Fully Redundant"
                ],
                "assertionsEnabled": [
                  "Fully Redundant",
                  "Redundancy Lost"
                ],
                "entityID": "11.3 (Add-in Card)",
                "sensorID": "0x78",
                "sensorName": "Redundancy",
                "sensorType": "Unknown (0xC9)",
                "uniqueSensorID": "11.3:0x78"
              },
              {
                "entityID": "34.1 (BIOS)",
                "sensorID": "0x1",
                "sensorName": "ECC Corr Err",
                "sensorType": "Memory",
                "uniqueSensorID": "34.1:0x1"
              },
              {
                "entityID": "34.1 (BIOS)",
                "sensorID": "0x2",
                "sensorName": "ECC Uncorr Err",
                "sensorType": "Memory",
                "uniqueSensorID": "34.1:0x2"
              },
              {
                "entityID": "34.1 (BIOS)",
                "sensorID": "0x3",
                "sensorName": "I/O Channel Chk",
                "sensorType": "Critical Interrupt",
                "uniqueSensorID": "34.1:0x3"
              },
              {
                "entityID": "34.1 (BIOS)",
                "sensorID": "0x4",
                "sensorName": "PCI Parity Err",
                "sensorType": "Critical Interrupt",
                "uniqueSensorID": "34.1:0x4"
              },
              {
                "entityID": "34.1 (BIOS)",
                "sensorID": "0x5",
                "sensorName": "PCI System Err",
                "sensorType": "Critical Interrupt",
                "uniqueSensorID": "34.1:0x5"
              },
              {
                "entityID": "34.1 (BIOS)",
                "sensorID": "0x6",
                "sensorName": "SBE Log Disabled",
                "sensorType": "Event Logging Disabled",
                "uniqueSensorID": "34.1:0x6"
              },
              {
                "entityID": "34.1 (BIOS)",
                "sensorID": "0x7",
                "sensorName": "Logging Disabled",
                "sensorType": "Event Logging Disabled",
                "uniqueSensorID": "34.1:0x7"
              },
              {
                "entityID": "34.1 (BIOS)",
                "sensorID": "0x8",
                "sensorName": "Unknown",
                "sensorType": "System Event",
                "uniqueSensorID": "34.1:0x8"
              },
              {
                "entityID": "34.1 (BIOS)",
                "sensorID": "0xa",
                "sensorName": "CPU Protocol Err",
                "sensorType": "Processor",
                "uniqueSensorID": "34.1:0xa"
              },
              {
                "entityID": "34.1 (BIOS)",
                "sensorID": "0xb",
                "sensorName": "CPU Bus PERR",
                "sensorType": "Processor",
                "uniqueSensorID": "34.1:0xb"
              },
              {
                "entityID": "34.1 (BIOS)",
                "sensorID": "0xc",
                "sensorName": "CPU Init Err",
                "sensorType": "Processor",
                "uniqueSensorID": "34.1:0xc"
              },
              {
                "entityID": "34.1 (BIOS)",
                "sensorID": "0xd",
                "sensorName": "CPU Machine Chk",
                "sensorType": "Processor",
                "uniqueSensorID": "34.1:0xd"
              },
              {
                "entityID": "34.1 (BIOS)",
                "sensorID": "0x11",
                "sensorName": "Memory Spared",
                "sensorType": "Memory",
                "uniqueSensorID": "34.1:0x11"
              },
              {
                "entityID": "34.1 (BIOS)",
                "sensorID": "0x12",
                "sensorName": "Memory Mirrored",
                "sensorType": "Memory",
                "uniqueSensorID": "34.1:0x12"
              },
              {
                "entityID": "34.1 (BIOS)",
                "sensorID": "0x13",
                "sensorName": "Memory RAID",
                "sensorType": "Memory",
                "uniqueSensorID": "34.1:0x13"
              },
              {
                "entityID": "34.1 (BIOS)",
                "sensorID": "0x14",
                "sensorName": "Memory Added",
                "sensorType": "Memory",
                "uniqueSensorID": "34.1:0x14"
              },
              {
                "entityID": "34.1 (BIOS)",
                "sensorID": "0x15",
                "sensorName": "Memory Removed",
                "sensorType": "Memory",
                "uniqueSensorID": "34.1:0x15"
              },
              {
                "entityID": "34.1 (BIOS)",
                "sensorID": "0x16",
                "sensorName": "Memory Cfg Err",
                "sensorType": "Memory",
                "uniqueSensorID": "34.1:0x16"
              },
              {
                "entityID": "34.1 (BIOS)",
                "sensorID": "0x17",
                "sensorName": "Mem Redun Gain",
                "sensorType": "Memory",
                "uniqueSensorID": "34.1:0x17"
              },
              {
                "entityID": "34.1 (BIOS)",
                "sensorID": "0x18",
                "sensorName": "PCIE Fatal Err",
                "sensorType": "Critical Interrupt",
                "uniqueSensorID": "34.1:0x18"
              },
              {
                "entityID": "34.1 (BIOS)",
                "sensorID": "0x19",
                "sensorName": "Chipset Err",
                "sensorType": "Critical Interrupt",
                "uniqueSensorID": "34.1:0x19"
              },
              {
                "entityID": "34.1 (BIOS)",
                "sensorID": "0x1a",
                "sensorName": "Err Reg Pointer",
                "sensorType": "Unknown (0xC1)",
                "uniqueSensorID": "34.1:0x1a"
              },
              {
                "entityID": "34.1 (BIOS)",
                "sensorID": "0x1b",
                "sensorName": "Mem ECC Warning",
                "sensorType": "Memory",
                "uniqueSensorID": "34.1:0x1b"
              },
              {
                "entityID": "34.1 (BIOS)",
                "sensorID": "0x1c",
                "sensorName": "Mem CRC Err",
                "sensorType": "Memory",
                "uniqueSensorID": "34.1:0x1c"
              },
              {
                "entityID": "34.1 (BIOS)",
                "sensorID": "0x1d",
                "sensorName": "USB Over-current",
                "sensorType": "Memory",
                "uniqueSensorID": "34.1:0x1d"
              },
              {
                "entityID": "34.1 (BIOS)",
                "sensorID": "0x1e",
                "sensorName": "POST Err",
                "sensorType": "System Firmwares",
                "uniqueSensorID": "34.1:0x1e"
              },
              {
                "entityID": "34.1 (BIOS)",
                "sensorID": "0x1f",
                "sensorName": "Hdwr version err",
                "sensorType": "Version Change",
                "uniqueSensorID": "34.1:0x1f"
              },
              {
                "entityID": "34.1 (BIOS)",
                "sensorID": "0x20",
                "sensorName": "Mem Overtemp",
                "sensorType": "Memory",
                "uniqueSensorID": "34.1:0x20"
              },
              {
                "entityID": "34.1 (BIOS)",
                "sensorID": "0x21",
                "sensorName": "Mem Fatal SB CRC",
                "sensorType": "Memory",
                "uniqueSensorID": "34.1:0x21"
              },
              {
                "entityID": "34.1 (BIOS)",
                "sensorID": "0x22",
                "sensorName": "Mem Fatal NB CRC",
                "sensorType": "Memory",
                "uniqueSensorID": "34.1:0x22"
              },
              {
                "entityID": "34.1 (BIOS)",
                "sensorID": "0x71",
                "sensorName": "OS Watchdog Time",
                "sensorType": "Watchdog",
                "uniqueSensorID": "34.1:0x71"
              },
              {
                "entityID": "34.1 (BIOS)",
                "sensorID": "0x26",
                "sensorName": "Non Fatal PCI Er",
                "sensorType": "Unknown (0xC2)",
                "uniqueSensorID": "34.1:0x26"
              },
              {
                "entityID": "34.1 (BIOS)",
                "sensorID": "0x27",
                "sensorName": "Fatal IO Error",
                "sensorType": "Unknown (0xC3)",
                "uniqueSensorID": "34.1:0x27"
              },
              {
                "entityID": "34.1 (BIOS)",
                "sensorID": "0x28",
                "sensorName": "MSR Info Log",
                "sensorType": "Unknown (0xC1)",
                "uniqueSensorID": "34.1:0x28"
              },
              {
                "entityID": "34.1 (BIOS)",
                "sensorID": "0x2a",
                "sensorName": "TXT Status",
                "sensorType": "OS Critical Stop",
                "uniqueSensorID": "34.1:0x2a"
              },
              {
                "assertionEvents": [
                  "Drive Present"
                ],
                "assertionsEnabled": [
                  "Drive Present",
                  "Drive Fault"
                ],
                "deassertionsEnabled": [
                  "Drive Present",
                  "Drive Fault"
                ],
                "entityID": "7.1 (System Board)",
                "sensorID": "0xa0",
                "sensorName": "Drive 0",
                "sensorType": "Drive Slot / Bay",
                "uniqueSensorID": "7.1:0xa0"
              },
              {
                "assertionsEnabled": [
                  "Config Error"
                ],
                "deassertionsEnabled": [
                  "Config Error"
                ],
                "entityID": "26.1 (Disk Drive Bay)",
                "eventStatus": "Unavailable",
                "sensorID": "0xe0",
                "sensorName": "Cable SAS A",
                "sensorType": "Cable / Interconnect",
                "uniqueSensorID": "26.1:0xe0"
              },
              {
                "assertionsEnabled": [
                  "Config Error"
                ],
                "deassertionsEnabled": [
                  "Config Error"
                ],
                "entityID": "26.1 (Disk Drive Bay)",
                "eventStatus": "Unavailable",
                "sensorID": "0xe1",
                "sensorName": "Cable SAS B",
                "sensorType": "Cable / Interconnect",
                "uniqueSensorID": "26.1:0xe1"
              },
              {
                "assertionsEnabled": [
                  "Config Error"
                ],
                "deassertionsEnabled": [
                  "Config Error"
                ],
                "entityID": "26.1 (Disk Drive Bay)",
                "eventStatus": "Unavailable",
                "sensorID": "0xe2",
                "sensorName": "Cable SAS C",
                "sensorType": "Cable / Interconnect",
                "uniqueSensorID": "26.1:0xe2"
              },
              {
                "assertionsEnabled": [
                  "Config Error"
                ],
                "deassertionsEnabled": [
                  "Config Error"
                ],
                "entityID": "26.1 (Disk Drive Bay)",
                "eventStatus": "Unavailable",
                "sensorID": "0xe3",
                "sensorName": "Cable SAS D",
                "sensorType": "Cable / Interconnect",
                "uniqueSensorID": "26.1:0xe3"
              },
              {
                "assertionsEnabled": [
                  "Config Error"
                ],
                "deassertionsEnabled": [
                  "Config Error"
                ],
                "entityID": "26.2 (Disk Drive Bay)",
                "sensorID": "0xe4",
                "sensorName": "Cable SAS A",
                "sensorType": "Cable / Interconnect",
                "uniqueSensorID": "26.2:0xe4"
              },
              {
                "assertionsEnabled": [
                  "Config Error"
                ],
                "deassertionsEnabled": [
                  "Config Error"
                ],
                "entityID": "26.2 (Disk Drive Bay)",
                "sensorID": "0xe5",
                "sensorName": "Cable SAS B",
                "sensorType": "Cable / Interconnect",
                "uniqueSensorID": "26.2:0xe5"
              },
              {
                "assertionsEnabled": [
                  "Config Error"
                ],
                "deassertionsEnabled": [
                  "Config Error"
                ],
                "entityID": "26.2 (Disk Drive Bay)",
                "sensorID": "0xe6",
                "sensorName": "Cable SAS C",
                "sensorType": "Cable / Interconnect",
                "uniqueSensorID": "26.2:0xe6"
              },
              {
                "assertionsEnabled": [
                  "Config Error"
                ],
                "deassertionsEnabled": [
                  "Config Error"
                ],
                "entityID": "26.2 (Disk Drive Bay)",
                "sensorID": "0xe7",
                "sensorName": "Cable SAS D",
                "sensorType": "Cable / Interconnect",
                "uniqueSensorID": "26.2:0xe7"
              },
              {
                "assertionEvents": [
                  "Connected"
                ],
                "assertionsEnabled": [
                  "Config Error"
                ],
                "deassertionsEnabled": [
                  "Config Error"
                ],
                "entityID": "26.1 (Disk Drive Bay)",
                "sensorID": "0x58",
                "sensorName": "Power Cable",
                "sensorType": "Cable / Interconnect",
                "statesAsserted": [
                  "Connected"
                ],
                "uniqueSensorID": "26.1:0x58"
              },
              {
                "assertionEvents": [
                  "Connected"
                ],
                "assertionsEnabled": [
                  "Config Error"
                ],
                "deassertionsEnabled": [
                  "Config Error"
                ],
                "entityID": "26.1 (Disk Drive Bay)",
                "sensorID": "0x59",
                "sensorName": "Signal Cable",
                "sensorType": "Cable / Interconnect",
                "statesAsserted": [
                  "Connected"
                ],
                "uniqueSensorID": "26.1:0x59"
              },
              {
                "assertionsEnabled": [
                  "Config Error"
                ],
                "deassertionsEnabled": [
                  "Config Error"
                ],
                "entityID": "26.2 (Disk Drive Bay)",
                "sensorID": "0x5a",
                "sensorName": "Power Cable",
                "sensorType": "Cable / Interconnect",
                "uniqueSensorID": "26.2:0x5a"
              },
              {
                "assertionsEnabled": [
                  "Config Error"
                ],
                "deassertionsEnabled": [
                  "Config Error"
                ],
                "entityID": "26.2 (Disk Drive Bay)",
                "sensorID": "0x5b",
                "sensorName": "Signal Cable",
                "sensorType": "Cable / Interconnect",
                "uniqueSensorID": "26.2:0x5b"
              },
              {
                "assertionEvents": [],
                "assertionsEnabled": [],
                "deassertionsEnabled": [],
                "entityID": "7.1 (System Board)",
                "eventMessageControl": "Per-threshold",
                "lowerCritical": "720.000",
                "lowerNonCritical": "840.000",
                "maximumSensorRange": "Unspecified",
                "minimumSensorRange": "Unspecified",
                "negativeHysteresis": "600.000",
                "nominalReading": "6720.000",
                "normalMaximum": "23640.000",
                "normalMinimum": "16680.000",
                "positiveHysteresis": "600.000",
                "readableThresholds": "lcr lnc",
                "sensorID": "0x3c",
                "sensorName": "Fan7A RPM",
                "sensorReading": "4320 (+/- 120) RPM",
                "sensorType": "Fan",
                "settableThresholds": "",
                "status": "ok",
                "thresholdReadMask": "lcr lnc",
                "uniqueSensorID": "7.1:0x3c"
              },
              {
                "assertionEvents": [],
                "assertionsEnabled": [],
                "deassertionsEnabled": [],
                "entityID": "7.1 (System Board)",
                "eventMessageControl": "Per-threshold",
                "lowerCritical": "720.000",
                "lowerNonCritical": "840.000",
                "maximumSensorRange": "Unspecified",
                "minimumSensorRange": "Unspecified",
                "negativeHysteresis": "600.000",
                "nominalReading": "6720.000",
                "normalMaximum": "23640.000",
                "normalMinimum": "16680.000",
                "positiveHysteresis": "600.000",
                "readableThresholds": "lcr lnc",
                "sensorID": "0x31",
                "sensorName": "Fan1B RPM",
                "sensorReading": "4080 (+/- 120) RPM",
                "sensorType": "Fan",
                "settableThresholds": "",
                "status": "ok",
                "thresholdReadMask": "lcr lnc",
                "uniqueSensorID": "7.1:0x31"
              },
              {
                "assertionEvents": [],
                "assertionsEnabled": [],
                "deassertionsEnabled": [],
                "entityID": "7.1 (System Board)",
                "eventMessageControl": "Per-threshold",
                "lowerCritical": "720.000",
                "lowerNonCritical": "840.000",
                "maximumSensorRange": "Unspecified",
                "minimumSensorRange": "Unspecified",
                "negativeHysteresis": "600.000",
                "nominalReading": "6720.000",
                "normalMaximum": "23640.000",
                "normalMinimum": "16680.000",
                "positiveHysteresis": "600.000",
                "readableThresholds": "lcr lnc",
                "sensorID": "0x33",
                "sensorName": "Fan2B RPM",
                "sensorReading": "4080 (+/- 120) RPM",
                "sensorType": "Fan",
                "settableThresholds": "",
                "status": "ok",
                "thresholdReadMask": "lcr lnc",
                "uniqueSensorID": "7.1:0x33"
              },
              {
                "assertionEvents": [],
                "assertionsEnabled": [],
                "deassertionsEnabled": [],
                "entityID": "7.1 (System Board)",
                "eventMessageControl": "Per-threshold",
                "lowerCritical": "720.000",
                "lowerNonCritical": "840.000",
                "maximumSensorRange": "Unspecified",
                "minimumSensorRange": "Unspecified",
                "negativeHysteresis": "600.000",
                "nominalReading": "6720.000",
                "normalMaximum": "23640.000",
                "normalMinimum": "16680.000",
                "positiveHysteresis": "600.000",
                "readableThresholds": "lcr lnc",
                "sensorID": "0x35",
                "sensorName": "Fan3B RPM",
                "sensorReading": "4080 (+/- 120) RPM",
                "sensorType": "Fan",
                "settableThresholds": "",
                "status": "ok",
                "thresholdReadMask": "lcr lnc",
                "uniqueSensorID": "7.1:0x35"
              },
              {
                "assertionEvents": [],
                "assertionsEnabled": [],
                "deassertionsEnabled": [],
                "entityID": "7.1 (System Board)",
                "eventMessageControl": "Per-threshold",
                "lowerCritical": "720.000",
                "lowerNonCritical": "840.000",
                "maximumSensorRange": "Unspecified",
                "minimumSensorRange": "Unspecified",
                "negativeHysteresis": "600.000",
                "nominalReading": "6720.000",
                "normalMaximum": "23640.000",
                "normalMinimum": "16680.000",
                "positiveHysteresis": "600.000",
                "readableThresholds": "lcr lnc",
                "sensorID": "0x37",
                "sensorName": "Fan4B RPM",
                "sensorReading": "3960 (+/- 120) RPM",
                "sensorType": "Fan",
                "settableThresholds": "",
                "status": "ok",
                "thresholdReadMask": "lcr lnc",
                "uniqueSensorID": "7.1:0x37"
              },
              {
                "assertionEvents": [],
                "assertionsEnabled": [],
                "deassertionsEnabled": [],
                "entityID": "7.1 (System Board)",
                "eventMessageControl": "Per-threshold",
                "lowerCritical": "720.000",
                "lowerNonCritical": "840.000",
                "maximumSensorRange": "Unspecified",
                "minimumSensorRange": "Unspecified",
                "negativeHysteresis": "600.000",
                "nominalReading": "6720.000",
                "normalMaximum": "23640.000",
                "normalMinimum": "16680.000",
                "positiveHysteresis": "600.000",
                "readableThresholds": "lcr lnc",
                "sensorID": "0x39",
                "sensorName": "Fan5B RPM",
                "sensorReading": "4080 (+/- 120) RPM",
                "sensorType": "Fan",
                "settableThresholds": "",
                "status": "ok",
                "thresholdReadMask": "lcr lnc",
                "uniqueSensorID": "7.1:0x39"
              },
              {
                "assertionEvents": [],
                "assertionsEnabled": [],
                "deassertionsEnabled": [],
                "entityID": "7.1 (System Board)",
                "eventMessageControl": "Per-threshold",
                "lowerCritical": "720.000",
                "lowerNonCritical": "840.000",
                "maximumSensorRange": "Unspecified",
                "minimumSensorRange": "Unspecified",
                "negativeHysteresis": "600.000",
                "nominalReading": "6720.000",
                "normalMaximum": "23640.000",
                "normalMinimum": "16680.000",
                "positiveHysteresis": "600.000",
                "readableThresholds": "lcr lnc",
                "sensorID": "0x3b",
                "sensorName": "Fan6B RPM",
                "sensorReading": "4080 (+/- 120) RPM",
                "sensorType": "Fan",
                "settableThresholds": "",
                "status": "ok",
                "thresholdReadMask": "lcr lnc",
                "uniqueSensorID": "7.1:0x3b"
              },
              {
                "assertionEvents": [],
                "assertionsEnabled": [],
                "deassertionsEnabled": [],
                "entityID": "7.1 (System Board)",
                "eventMessageControl": "Per-threshold",
                "lowerCritical": "720.000",
                "lowerNonCritical": "840.000",
                "maximumSensorRange": "Unspecified",
                "minimumSensorRange": "Unspecified",
                "negativeHysteresis": "600.000",
                "nominalReading": "6720.000",
                "normalMaximum": "23640.000",
                "normalMinimum": "16680.000",
                "positiveHysteresis": "600.000",
                "readableThresholds": "lcr lnc",
                "sensorID": "0x3d",
                "sensorName": "Fan7B RPM",
                "sensorReading": "4080 (+/- 120) RPM",
                "sensorType": "Fan",
                "settableThresholds": "",
                "status": "ok",
                "thresholdReadMask": "lcr lnc",
                "uniqueSensorID": "7.1:0x3d"
              },
              {
                "entityID": "7.1 (System Board)",
                "sensorID": "0x66",
                "sensorName": "PFault Fail Safe",
                "sensorType": "Voltage",
                "uniqueSensorID": "7.1:0x66"
              }
            ]
          }
        }
      },
      {
        "nodeID": 4,
        "result": {
          "ipmiInfo": {
            "sensors": [
              {
                "entityID": "7.1 (System Board)",
                "sensorID": "0x72",
                "sensorName": "SEL",
                "sensorType": "Event Logging Disabled",
                "uniqueSensorID": "7.1:0x72"
              },
              {
                "assertionsEnabled": [
                  "General Chassis intrusion"
                ],
                "deassertionsEnabled": [
                  "General Chassis intrusion"
                ],
                "entityID": "7.1 (System Board)",
                "sensorID": "0x73",
                "sensorName": "Intrusion",
                "sensorType": "Physical Security",
                "uniqueSensorID": "7.1:0x73"
              },
              {
                "assertionEvents": [],
                "assertionsEnabled": [],
                "deassertionsEnabled": [],
                "entityID": "7.1 (System Board)",
                "eventMessageControl": "Per-threshold",
                "lowerCritical": "720.000",
                "lowerNonCritical": "840.000",
                "maximumSensorRange": "Unspecified",
                "minimumSensorRange": "Unspecified",
                "negativeHysteresis": "120.000",
                "nominalReading": "10080.000",
                "normalMaximum": "23640.000",
                "normalMinimum": "16680.000",
                "positiveHysteresis": "120.000",
                "readableThresholds": "lcr lnc",
                "sensorID": "0x30",
                "sensorName": "Fan1A RPM",
                "sensorReading": "5640 (+/- 120) RPM",
                "sensorType": "Fan",
                "settableThresholds": "",
                "status": "ok",
                "thresholdReadMask": "lcr lnc",
                "uniqueSensorID": "7.1:0x30"
              },
              {
                "assertionEvents": [],
                "assertionsEnabled": [],
                "deassertionsEnabled": [],
                "entityID": "7.1 (System Board)",
                "eventMessageControl": "Per-threshold",
                "lowerCritical": "720.000",
                "lowerNonCritical": "840.000",
                "maximumSensorRange": "Unspecified",
                "minimumSensorRange": "Unspecified",
                "negativeHysteresis": "120.000",
                "nominalReading": "10080.000",
                "normalMaximum": "23640.000",
                "normalMinimum": "16680.000",
                "positiveHysteresis": "120.000",
                "readableThresholds": "lcr lnc",
                "sensorID": "0x32",
                "sensorName": "Fan2A RPM",
                "sensorReading": "5760 (+/- 120) RPM",
                "sensorType": "Fan",
                "settableThresholds": "",
                "status": "ok",
                "thresholdReadMask": "lcr lnc",
                "uniqueSensorID": "7.1:0x32"
              },
              {
                "assertionEvents": [],
                "assertionsEnabled": [],
                "deassertionsEnabled": [],
                "entityID": "7.1 (System Board)",
                "eventMessageControl": "Per-threshold",
                "lowerCritical": "720.000",
                "lowerNonCritical": "840.000",
                "maximumSensorRange": "Unspecified",
                "minimumSensorRange": "Unspecified",
                "negativeHysteresis": "120.000",
                "nominalReading": "10080.000",
                "normalMaximum": "23640.000",
                "normalMinimum": "16680.000",
                "positiveHysteresis": "120.000",
                "readableThresholds": "lcr lnc",
                "sensorID": "0x34",
                "sensorName": "Fan3A RPM",
                "sensorReading": "5760 (+/- 120) RPM",
                "sensorType": "Fan",
                "settableThresholds": "",
                "status": "ok",
                "thresholdReadMask": "lcr lnc",
                "uniqueSensorID": "7.1:0x34"
              },
              {
                "assertionEvents": [],
                "assertionsEnabled": [],
                "deassertionsEnabled": [],
                "entityID": "7.1 (System Board)",
                "eventMessageControl": "Per-threshold",
                "lowerCritical": "720.000",
                "lowerNonCritical": "840.000",
                "maximumSensorRange": "Unspecified",
                "minimumSensorRange": "Unspecified",
                "negativeHysteresis": "120.000",
                "nominalReading": "10080.000",
                "normalMaximum": "23640.000",
                "normalMinimum": "16680.000",
                "positiveHysteresis": "120.000",
                "readableThresholds": "lcr lnc",
                "sensorID": "0x36",
                "sensorName": "Fan4A RPM",
                "sensorReading": "5760 (+/- 120) RPM",
                "sensorType": "Fan",
                "settableThresholds": "",
                "status": "ok",
                "thresholdReadMask": "lcr lnc",
                "uniqueSensorID": "7.1:0x36"
              },
              {
                "assertionEvents": [],
                "assertionsEnabled": [],
                "deassertionsEnabled": [],
                "entityID": "7.1 (System Board)",
                "eventMessageControl": "Per-threshold",
                "lowerCritical": "720.000",
                "lowerNonCritical": "840.000",
                "maximumSensorRange": "Unspecified",
                "minimumSensorRange": "Unspecified",
                "negativeHysteresis": "120.000",
                "nominalReading": "6720.000",
                "normalMaximum": "23640.000",
                "normalMinimum": "16680.000",
                "positiveHysteresis": "120.000",
                "readableThresholds": "lcr lnc",
                "sensorID": "0x38",
                "sensorName": "Fan5A RPM",
                "sensorReading": "5760 (+/- 120) RPM",
                "sensorType": "Fan",
                "settableThresholds": "",
                "status": "ok",
                "thresholdReadMask": "lcr lnc",
                "uniqueSensorID": "7.1:0x38"
              },
              {
                "assertionEvents": [],
                "assertionsEnabled": [],
                "deassertionsEnabled": [],
                "entityID": "7.1 (System Board)",
                "eventMessageControl": "Per-threshold",
                "lowerCritical": "720.000",
                "lowerNonCritical": "840.000",
                "maximumSensorRange": "Unspecified",
                "minimumSensorRange": "Unspecified",
                "negativeHysteresis": "120.000",
                "nominalReading": "6720.000",
                "normalMaximum": "23640.000",
                "normalMinimum": "16680.000",
                "positiveHysteresis": "120.000",
                "readableThresholds": "lcr lnc",
                "sensorID": "0x3a",
                "sensorName": "Fan6A RPM",
                "sensorReading": "5760 (+/- 120) RPM",
                "sensorType": "Fan",
                "settableThresholds": "",
                "status": "ok",
                "thresholdReadMask": "lcr lnc",
                "uniqueSensorID": "7.1:0x3a"
              },
              {
                "assertionEvents": [],
                "assertionsEnabled": [],
                "deassertionsEnabled": [],
                "entityID": "7.1 (System Board)",
                "eventMessageControl": "Per-threshold",
                "lowerCritical": "-7.000",
                "lowerNonCritical": "3.000",
                "maximumSensorRange": "Unspecified",
                "minimumSensorRange": "Unspecified",
                "negativeHysteresis": "1.000",
                "nominalReading": "23.000",
                "normalMaximum": "69.000",
                "normalMinimum": "11.000",
                "positiveHysteresis": "1.000",
                "readableThresholds": "lcr lnc unc ucr",
                "sensorID": "0x4",
                "sensorName": "Inlet Temp",
                "sensorReading": "21 (+/- 1) degrees C",
                "sensorType": "Temperature",
                "settableThresholds": "lcr lnc unc ucr",
                "status": "ok",
                "thresholdReadMask": "lcr lnc unc ucr",
                "uniqueSensorID": "7.1:0x4",
                "upperCritical": "47.000",
                "upperNonCritical": "42.000"
              },
              {
                "assertionEvents": [],
                "assertionsEnabled": [],
                "entityID": "7.1 (System Board)",
                "eventMessageControl": "Per-threshold",
                "lowerCritical": "3.000",
                "lowerNonCritical": "8.000",
                "maximumSensorRange": "Unspecified",
                "minimumSensorRange": "Unspecified",
                "negativeHysteresis": "1.000",
                "nominalReading": "23.000",
                "normalMaximum": "69.000",
                "normalMinimum": "11.000",
                "positiveHysteresis": "1.000",
                "readableThresholds": "lcr lnc unc ucr",
                "sensorID": "0x1",
                "sensorName": "Exhaust Temp",
                "sensorReading": "33 (+/- 1) degrees C",
                "sensorType": "Temperature",
                "settableThresholds": "",
                "status": "ok",
                "uniqueSensorID": "7.1:0x1",
                "upperCritical": "75.000",
                "upperNonCritical": "70.000"
              },
              {
                "assertionEvents": [],
                "assertionsEnabled": [],
                "entityID": "3.1 (Processor)",
                "eventMessageControl": "Per-threshold",
                "lowerCritical": "3.000",
                "lowerNonCritical": "8.000",
                "maximumSensorRange": "Unspecified",
                "minimumSensorRange": "Unspecified",
                "negativeHysteresis": "1.000",
                "nominalReading": "23.000",
                "normalMaximum": "69.000",
                "normalMinimum": "11.000",
                "positiveHysteresis": "1.000",
                "readableThresholds": "No Thresholds",
                "sensorID": "0xe",
                "sensorName": "Temp",
                "sensorReading": "42 (+/- 1) degrees C",
                "sensorType": "Temperature",
                "settableThresholds": "No Thresholds",
                "status": "ok",
                "uniqueSensorID": "3.1:0xe",
                "upperCritical": "83.000",
                "upperNonCritical": "77.000"
              },
              {
                "assertionEvents": [],
                "assertionsEnabled": [],
                "entityID": "3.2 (Processor)",
                "eventMessageControl": "Per-threshold",
                "lowerCritical": "3.000",
                "lowerNonCritical": "8.000",
                "maximumSensorRange": "Unspecified",
                "minimumSensorRange": "Unspecified",
                "negativeHysteresis": "1.000",
                "nominalReading": "23.000",
                "normalMaximum": "69.000",
                "normalMinimum": "11.000",
                "positiveHysteresis": "1.000",
                "readableThresholds": "No Thresholds",
                "sensorID": "0xf",
                "sensorName": "Temp",
                "sensorReading": "41 (+/- 1) degrees C",
                "sensorType": "Temperature",
                "settableThresholds": "No Thresholds",
                "status": "ok",
                "uniqueSensorID": "3.2:0xf",
                "upperCritical": "83.000",
                "upperNonCritical": "77.000"
              },
              {
                "assertionsEnabled": [
                  "Timer expired",
                  "Hard reset",
                  "Power down",
                  "Power cycle"
                ],
                "deassertionsEnabled": [
                  "Timer expired",
                  "Hard reset",
                  "Power down",
                  "Power cycle"
                ],
                "entityID": "7.1 (System Board)",
                "sensorID": "0x71",
                "sensorName": "OS Watchdog",
                "sensorType": "Watchdog",
                "uniqueSensorID": "7.1:0x71"
              },
              {
                "assertionEvents": [
                  "State Deasserted"
                ],
                "assertionsEnabled": [
                  "State Deasserted",
                  "State Asserted"
                ],
                "deassertionsEnabled": [
                  "State Deasserted",
                  "State Asserted"
                ],
                "entityID": "3.1 (Processor)",
                "sensorID": "0x23",
                "sensorName": "VCORE PG",
                "sensorType": "Voltage",
                "statesAsserted": [
                  "State Deasserted"
                ],
                "uniqueSensorID": "3.1:0x23"
              },
              {
                "assertionEvents": [
                  "State Deasserted"
                ],
                "assertionsEnabled": [
                  "State Deasserted",
                  "State Asserted"
                ],
                "entityID": "3.2 (Processor)",
                "sensorID": "0x24",
                "sensorName": "VCORE PG",
                "sensorType": "Voltage",
                "statesAsserted": [
                  "State Deasserted"
                ],
                "uniqueSensorID": "3.2:0x24"
              },
              {
                "assertionEvents": [
                  "State Deasserted"
                ],
                "assertionsEnabled": [
                  "State Deasserted",
                  "State Asserted"
                ],
                "entityID": "7.1 (System Board)",
                "sensorID": "0x19",
                "sensorName": "3.3V PG",
                "sensorType": "Voltage",
                "statesAsserted": [
                  "State Deasserted"
                ],
                "uniqueSensorID": "7.1:0x19"
              },
              {
                "assertionEvents": [
                  "State Deasserted"
                ],
                "assertionsEnabled": [
                  "State Deasserted",
                  "State Asserted"
                ],
                "entityID": "7.1 (System Board)",
                "sensorID": "0x1a",
                "sensorName": "5V PG",
                "sensorType": "Voltage",
                "statesAsserted": [
                  "State Deasserted"
                ],
                "uniqueSensorID": "7.1:0x1a"
              },
              {
                "assertionEvents": [
                  "Connected"
                ],
                "assertionsEnabled": [
                  "Config Error"
                ],
                "deassertionsEnabled": [
                  "Config Error"
                ],
                "entityID": "7.1 (System Board)",
                "sensorID": "0x50",
                "sensorName": "USB Cable Pres",
                "sensorType": "Cable / Interconnect",
                "statesAsserted": [
                  "Connected"
                ],
                "uniqueSensorID": "7.1:0x50"
              },
              {
                "assertionsEnabled": [
                  "Config Error"
                ],
                "deassertionsEnabled": [
                  "Config Error"
                ],
                "entityID": "7.1 (System Board)",
                "sensorID": "0x51",
                "sensorName": "VGA Cable Pres",
                "sensorType": "Cable / Interconnect",
                "uniqueSensorID": "7.1:0x51"
              },
              {
                "assertionEvents": [
                  "Present"
                ],
                "entityID": "7.1 (System Board)",
                "sensorID": "0x70",
                "sensorName": "Dedicated NIC",
                "sensorType": "Entity Presence",
                "statesAsserted": [
                  "Present"
                ],
                "uniqueSensorID": "7.1:0x70"
              },
              {
                "assertionEvents": [
                  "Absent"
                ],
                "entityID": "11.2 (Add-in Card)",
                "sensorID": "0x49",
                "sensorName": "Presence",
                "sensorType": "Entity Presence",
                "statesAsserted": [
                  "Absent"
                ],
                "uniqueSensorID": "11.2:0x49"
              },
              {
                "assertionEvents": [
                  "Present"
                ],
                "entityID": "3.1 (Processor)",
                "sensorID": "0x40",
                "sensorName": "Presence",
                "sensorType": "Entity Presence",
                "statesAsserted": [
                  "Present"
                ],
                "uniqueSensorID": "3.1:0x40"
              },
              {
                "assertionEvents": [
                  "Present"
                ],
                "entityID": "3.2 (Processor)",
                "sensorID": "0x41",
                "sensorName": "Presence",
                "sensorType": "Entity Presence",
                "statesAsserted": [
                  "Present"
                ],
                "uniqueSensorID": "3.2:0x41"
              },
              {
                "assertionEvents": [
                  "State Deasserted"
                ],
                "assertionsEnabled": [
                  "State Deasserted",
                  "State Asserted"
                ],
                "entityID": "3.2 (Processor)",
                "sensorID": "0x22",
                "sensorName": "PLL PG",
                "sensorType": "Voltage",
                "statesAsserted": [
                  "State Deasserted"
                ],
                "uniqueSensorID": "3.2:0x22"
              },
              {
                "assertionEvents": [
                  "State Deasserted"
                ],
                "assertionsEnabled": [
                  "State Deasserted",
                  "State Asserted"
                ],
                "entityID": "3.1 (Processor)",
                "sensorID": "0x25",
                "sensorName": "PLL PG",
                "sensorType": "Voltage",
                "statesAsserted": [
                  "State Deasserted"
                ],
                "uniqueSensorID": "3.1:0x25"
              },
              {
                "assertionEvents": [
                  "State Deasserted"
                ],
                "assertionsEnabled": [
                  "State Deasserted",
                  "State Asserted"
                ],
                "entityID": "7.1 (System Board)",
                "sensorID": "0x27",
                "sensorName": "1.1V PG",
                "sensorType": "Voltage",
                "statesAsserted": [
                  "State Deasserted"
                ],
                "uniqueSensorID": "7.1:0x27"
              },
              {
                "assertionEvents": [
                  "State Deasserted"
                ],
                "assertionsEnabled": [
                  "State Deasserted",
                  "State Asserted"
                ],
                "entityID": "3.1 (Processor)",
                "sensorID": "0x15",
                "sensorName": "M23 VDDQ PG",
                "sensorType": "Voltage",
                "statesAsserted": [
                  "State Deasserted"
                ],
                "uniqueSensorID": "3.1:0x15"
              },
              {
                "assertionEvents": [
                  "State Deasserted"
                ],
                "assertionsEnabled": [
                  "State Deasserted",
                  "State Asserted"
                ],
                "entityID": "3.1 (Processor)",
                "sensorID": "0x16",
                "sensorName": "M23 VTT PG",
                "sensorType": "Voltage",
                "statesAsserted": [
                  "State Deasserted"
                ],
                "uniqueSensorID": "3.1:0x16"
              },
              {
                "assertionEvents": [
                  "State Deasserted"
                ],
                "assertionsEnabled": [
                  "State Deasserted",
                  "State Asserted"
                ],
                "entityID": "7.1 (System Board)",
                "sensorID": "0x21",
                "sensorName": "FETDRV PG",
                "sensorType": "Voltage",
                "statesAsserted": [
                  "State Deasserted"
                ],
                "uniqueSensorID": "7.1:0x21"
              },
              {
                "assertionEvents": [
                  "Present"
                ],
                "entityID": "10.2 (Power Supply)",
                "sensorID": "0x43",
                "sensorName": "Presence",
                "sensorType": "Entity Presence",
                "statesAsserted": [
                  "Present"
                ],
                "uniqueSensorID": "10.2:0x43"
              },
              {
                "assertionEvents": [
                  "State Deasserted"
                ],
                "assertionsEnabled": [
                  "State Deasserted",
                  "State Asserted"
                ],
                "entityID": "3.2 (Processor)",
                "sensorID": "0x29",
                "sensorName": "VSA PG",
                "sensorType": "Voltage",
                "statesAsserted": [
                  "State Deasserted"
                ],
                "uniqueSensorID": "3.2:0x29"
              },
              {
                "assertionEvents": [
                  "State Deasserted"
                ],
                "assertionsEnabled": [
                  "State Deasserted",
                  "State Asserted"
                ],
                "entityID": "3.1 (Processor)",
                "sensorID": "0x2b",
                "sensorName": "VSA PG",
                "sensorType": "Voltage",
                "statesAsserted": [
                  "State Deasserted"
                ],
                "uniqueSensorID": "3.1:0x2b"
              },
              {
                "assertionEvents": [
                  "State Deasserted"
                ],
                "assertionsEnabled": [
                  "State Deasserted",
                  "State Asserted"
                ],
                "entityID": "3.2 (Processor)",
                "sensorID": "0x1b",
                "sensorName": "M01 VDDQ PG",
                "sensorType": "Voltage",
                "statesAsserted": [
                  "State Deasserted"
                ],
                "uniqueSensorID": "3.2:0x1b"
              },
              {
                "assertionEvents": [
                  "State Deasserted"
                ],
                "assertionsEnabled": [
                  "State Deasserted",
                  "State Asserted"
                ],
                "entityID": "3.1 (Processor)",
                "sensorID": "0x1e",
                "sensorName": "M01 VDDQ PG",
                "sensorType": "Voltage",
                "statesAsserted": [
                  "State Deasserted"
                ],
                "uniqueSensorID": "3.1:0x1e"
              },
              {
                "assertionEvents": [
                  "State Deasserted"
                ],
                "assertionsEnabled": [
                  "State Deasserted",
                  "State Asserted"
                ],
                "entityID": "3.2 (Processor)",
                "sensorID": "0x2e",
                "sensorName": "M23 VTT PG",
                "sensorType": "Voltage",
                "statesAsserted": [
                  "State Deasserted"
                ],
                "uniqueSensorID": "3.2:0x2e"
              },
              {
                "assertionEvents": [
                  "State Deasserted"
                ],
                "assertionsEnabled": [
                  "State Deasserted",
                  "State Asserted"
                ],
                "entityID": "3.2 (Processor)",
                "sensorID": "0x1c",
                "sensorName": "M01 VTT PG",
                "sensorType": "Voltage",
                "statesAsserted": [
                  "State Deasserted"
                ],
                "uniqueSensorID": "3.2:0x1c"
              },
              {
                "assertionEvents": [
                  "State Deasserted"
                ],
                "assertionsEnabled": [
                  "State Deasserted",
                  "State Asserted"
                ],
                "entityID": "7.1 (System Board)",
                "sensorID": "0x2f",
                "sensorName": "NDC PG",
                "sensorType": "Voltage",
                "statesAsserted": [
                  "State Deasserted"
                ],
                "uniqueSensorID": "7.1:0x2f"
              },
              {
                "entityID": "7.1 (System Board)",
                "sensorID": "0x4c",
                "sensorName": "LCD Cable Pres",
                "sensorType": "Cable / Interconnect",
                "uniqueSensorID": "7.1:0x4c"
              },
              {
                "assertionEvents": [
                  "State Deasserted"
                ],
                "assertionsEnabled": [
                  "State Deasserted",
                  "State Asserted"
                ],
                "entityID": "3.2 (Processor)",
                "sensorID": "0x1f",
                "sensorName": "VTT PG",
                "sensorType": "Voltage",
                "statesAsserted": [
                  "State Deasserted"
                ],
                "uniqueSensorID": "3.2:0x1f"
              },
              {
                "assertionEvents": [
                  "State Deasserted"
                ],
                "assertionsEnabled": [
                  "State Deasserted",
                  "State Asserted"
                ],
                "entityID": "3.1 (Processor)",
                "sensorID": "0x20",
                "sensorName": "VTT PG",
                "sensorType": "Voltage",
                "statesAsserted": [
                  "State Deasserted"
                ],
                "uniqueSensorID": "3.1:0x20"
              },
              {
                "assertionEvents": [
                  "State Deasserted"
                ],
                "assertionsEnabled": [
                  "State Deasserted",
                  "State Asserted"
                ],
                "entityID": "3.2 (Processor)",
                "sensorID": "0x1d",
                "sensorName": "M23 VDDQ PG",
                "sensorType": "Voltage",
                "statesAsserted": [
                  "State Deasserted"
                ],
                "uniqueSensorID": "3.2:0x1d"
              },
              {
                "assertionEvents": [
                  "Present"
                ],
                "assertionsEnabled": [
                  "Present",
                  "Absent"
                ],
                "entityID": "11.1 (Add-in Card)",
                "sensorID": "0x4a",
                "sensorName": "Presence",
                "sensorType": "Entity Presence",
                "statesAsserted": [
                  "Present"
                ],
                "uniqueSensorID": "11.1:0x4a"
              },
              {
                "assertionEvents": [
                  "Absent"
                ],
                "entityID": "11.3 (Add-in Card)",
                "sensorID": "0x48",
                "sensorName": "Presence",
                "sensorType": "Entity Presence",
                "statesAsserted": [
                  "Absent"
                ],
                "uniqueSensorID": "11.3:0x48"
              },
              {
                "assertionEvents": [
                  "Presence detected"
                ],
                "assertionsEnabled": [
                  "IERR",
                  "Thermal Trip",
                  "Configuration Error",
                  "Presence detected",
                  "Throttled"
                ],
                "deassertionsEnabled": [
                  "IERR",
                  "Thermal Trip",
                  "Configuration Error",
                  "Presence detected",
                  "Throttled"
                ],
                "entityID": "3.1 (Processor)",
                "sensorID": "0x60",
                "sensorName": "Status",
                "sensorType": "Processor",
                "statesAsserted": [
                  "Presence detected"
                ],
                "uniqueSensorID": "3.1:0x60"
              },
              {
                "assertionEvents": [
                  "Presence detected"
                ],
                "assertionsEnabled": [
                  "IERR",
                  "Thermal Trip",
                  "Configuration Error",
                  "Throttled"
                ],
                "deassertionsEnabled": [
                  "IERR",
                  "Thermal Trip",
                  "Configuration Error",
                  "Throttled"
                ],
                "entityID": "3.2 (Processor)",
                "sensorID": "0x61",
                "sensorName": "Status",
                "sensorType": "Processor",
                "statesAsserted": [
                  "Presence detected"
                ],
                "uniqueSensorID": "3.2:0x61"
              },
              {
                "assertionEvents": [
                  "Fully Redundant"
                ],
                "assertionsEnabled": [
                  "Fully Redundant",
                  "Redundancy Lost"
                ],
                "entityID": "7.1 (System Board)",
                "sensorID": "0x75",
                "sensorName": "Fan Redundancy",
                "sensorType": "Fan",
                "statesAsserted": [
                  "Fully Redundant"
                ],
                "uniqueSensorID": "7.1:0x75"
              },
              {
                "assertionEvents": [
                  "Connected"
                ],
                "assertionsEnabled": [
                  "Config Error"
                ],
                "deassertionsEnabled": [
                  "Config Error"
                ],
                "entityID": "7.1 (System Board)",
                "sensorID": "0x64",
                "sensorName": "Riser Config Err",
                "sensorType": "Cable / Interconnect",
                "statesAsserted": [
                  "Connected"
                ],
                "uniqueSensorID": "7.1:0x64"
              },
              {
                "assertionEvents": [
                  "Connected"
                ],
                "assertionsEnabled": [
                  "Config Error"
                ],
                "deassertionsEnabled": [
                  "Config Error"
                ],
                "entityID": "7.1 (System Board)",
                "sensorID": "0x4f",
                "sensorName": "Riser 3 Presence",
                "sensorType": "Cable / Interconnect",
                "statesAsserted": [
                  "Connected"
                ],
                "uniqueSensorID": "7.1:0x4f"
              },
              {
                "assertionEvents": [
                  "State Deasserted"
                ],
                "assertionsEnabled": [
                  "State Deasserted",
                  "State Asserted"
                ],
                "entityID": "7.1 (System Board)",
                "sensorID": "0x28",
                "sensorName": "1.5V PG",
                "sensorType": "Voltage",
                "statesAsserted": [
                  "State Deasserted"
                ],
                "uniqueSensorID": "7.1:0x28"
              },
              {
                "assertionEvents": [
                  "State Deasserted"
                ],
                "assertionsEnabled": [
                  "State Deasserted",
                  "State Asserted"
                ],
                "entityID": "7.1 (System Board)",
                "sensorID": "0x2c",
                "sensorName": "PS2 PG Fail",
                "sensorType": "Voltage",
                "statesAsserted": [
                  "State Deasserted"
                ],
                "uniqueSensorID": "7.1:0x2c"
              },
              {
                "assertionEvents": [
                  "State Deasserted"
                ],
                "assertionsEnabled": [
                  "State Deasserted",
                  "State Asserted"
                ],
                "entityID": "7.1 (System Board)",
                "sensorID": "0x2d",
                "sensorName": "PS1 PG Fail",
                "sensorType": "Voltage",
                "statesAsserted": [
                  "State Deasserted"
                ],
                "uniqueSensorID": "7.1:0x2d"
              },
              {
                "assertionEvents": [
                  "State Deasserted"
                ],
                "assertionsEnabled": [
                  "State Deasserted",
                  "State Asserted"
                ],
                "entityID": "7.1 (System Board)",
                "sensorID": "0xf6",
                "sensorName": "BP1 5V PG",
                "sensorType": "Voltage",
                "statesAsserted": [
                  "State Deasserted"
                ],
                "uniqueSensorID": "7.1:0xf6"
              },
              {
                "assertionEvents": [
                  "State Deasserted"
                ],
                "assertionsEnabled": [
                  "State Deasserted",
                  "State Asserted"
                ],
                "entityID": "7.1 (System Board)",
                "sensorID": "0xf7",
                "sensorName": "BP2 5V PG",
                "sensorType": "Voltage",
                "uniqueSensorID": "7.1:0xf7"
              },
              {
                "assertionEvents": [
                  "State Deasserted"
                ],
                "assertionsEnabled": [
                  "State Deasserted",
                  "State Asserted"
                ],
                "entityID": "3.1 (Processor)",
                "sensorID": "0x14",
                "sensorName": "M01 VTT PG",
                "sensorType": "Voltage",
                "statesAsserted": [
                  "State Deasserted"
                ],
                "uniqueSensorID": "3.1:0x14"
              },
              {
                "assertionEvents": [
                  "Present"
                ],
                "entityID": "10.1 (Power Supply)",
                "sensorID": "0x42",
                "sensorName": "Presence",
                "sensorType": "Entity Presence",
                "statesAsserted": [
                  "Present"
                ],
                "uniqueSensorID": "10.1:0x42"
              },
              {
                "assertionsEnabled": [
                  "NMI/Diag Interrupt",
                  "Bus Timeout"
                ],
                "deassertionsEnabled": [
                  "NMI/Diag Interrupt",
                  "Bus Timeout"
                ],
                "entityID": "7.1 (System Board)",
                "sensorID": "0x90",
                "sensorName": "PCIe Slot1",
                "sensorType": "Critical Interrupt",
                "uniqueSensorID": "7.1:0x90"
              },
              {
                "assertionsEnabled": [
                  "NMI/Diag Interrupt",
                  "Bus Timeout"
                ],
                "deassertionsEnabled": [
                  "NMI/Diag Interrupt",
                  "Bus Timeout"
                ],
                "entityID": "7.1 (System Board)",
                "sensorID": "0x91",
                "sensorName": "PCIe Slot2",
                "sensorType": "Critical Interrupt",
                "uniqueSensorID": "7.1:0x91"
              },
              {
                "assertionsEnabled": [
                  "NMI/Diag Interrupt",
                  "Bus Timeout"
                ],
                "deassertionsEnabled": [
                  "NMI/Diag Interrupt",
                  "Bus Timeout"
                ],
                "entityID": "7.1 (System Board)",
                "sensorID": "0x92",
                "sensorName": "PCIe Slot3",
                "sensorType": "Critical Interrupt",
                "uniqueSensorID": "7.1:0x92"
              },
              {
                "assertionsEnabled": [
                  "NMI/Diag Interrupt",
                  "Bus Timeout"
                ],
                "deassertionsEnabled": [
                  "NMI/Diag Interrupt",
                  "Bus Timeout"
                ],
                "entityID": "7.1 (System Board)",
                "sensorID": "0x93",
                "sensorName": "PCIe Slot4",
                "sensorType": "Critical Interrupt",
                "uniqueSensorID": "7.1:0x93"
              },
              {
                "assertionsEnabled": [
                  "NMI/Diag Interrupt",
                  "Bus Timeout"
                ],
                "deassertionsEnabled": [
                  "NMI/Diag Interrupt",
                  "Bus Timeout"
                ],
                "entityID": "7.1 (System Board)",
                "sensorID": "0x94",
                "sensorName": "PCIe Slot5",
                "sensorType": "Critical Interrupt",
                "uniqueSensorID": "7.1:0x94"
              },
              {
                "assertionsEnabled": [
                  "NMI/Diag Interrupt",
                  "Bus Timeout"
                ],
                "deassertionsEnabled": [
                  "NMI/Diag Interrupt",
                  "Bus Timeout"
                ],
                "entityID": "7.1 (System Board)",
                "sensorID": "0x95",
                "sensorName": "PCIe Slot6",
                "sensorType": "Critical Interrupt",
                "uniqueSensorID": "7.1:0x95"
              },
              {
                "assertionsEnabled": [
                  "NMI/Diag Interrupt",
                  "Bus Timeout"
                ],
                "deassertionsEnabled": [
                  "NMI/Diag Interrupt",
                  "Bus Timeout"
                ],
                "entityID": "7.1 (System Board)",
                "sensorID": "0x96",
                "sensorName": "PCIe Slot7",
                "sensorType": "Critical Interrupt",
                "uniqueSensorID": "7.1:0x96"
              },
              {
                "entityID": "0.1 (Unspecified)",
                "sensorID": "0xfa",
                "sensorName": "vFlash",
                "sensorType": "Module / Board",
                "uniqueSensorID": "0.1:0xfa"
              },
              {
                "assertionsEnabled": [
                  "Failed"
                ],
                "deassertionsEnabled": [
                  "Failed"
                ],
                "entityID": "7.1 (System Board)",
                "sensorID": "0x65",
                "sensorName": "CMOS Battery",
                "sensorType": "Battery",
                "uniqueSensorID": "7.1:0x65"
              },
              {
                "assertionsEnabled": [
                  "Failed"
                ],
                "deassertionsEnabled": [
                  "Failed"
                ],
                "entityID": "11.2 (Add-in Card)",
                "eventStatus": "Unavailable",
                "sensorID": "0x68",
                "sensorName": "ROMB Battery",
                "sensorType": "Battery",
                "uniqueSensorID": "11.2:0x68"
              },
              {
                "assertionsEnabled": [
                  "Failed"
                ],
                "deassertionsEnabled": [
                  "Failed"
                ],
                "entityID": "11.4 (Add-in Card)",
                "eventStatus": "Unavailable",
                "sensorID": "0x69",
                "sensorName": "ROMB Battery",
                "sensorType": "Battery",
                "uniqueSensorID": "11.4:0x69"
              },
              {
                "assertionEvents": [
                  "Present"
                ],
                "entityID": "26.1 (Disk Drive Bay)",
                "sensorID": "0x54",
                "sensorName": "Presence",
                "sensorType": "Entity Presence",
                "statesAsserted": [
                  "Present"
                ],
                "uniqueSensorID": "26.1:0x54"
              },
              {
                "assertionEvents": [
                  "Absent"
                ],
                "entityID": "26.2 (Disk Drive Bay)",
                "sensorID": "0x55",
                "sensorName": "Presence",
                "sensorType": "Entity Presence",
                "statesAsserted": [
                  "Absent"
                ],
                "uniqueSensorID": "26.2:0x55"
              },
              {
                "assertionEvents": [],
                "assertionsEnabled": [],
                "entityID": "10.1 (Power Supply)",
                "eventMessageControl": "Per-threshold",
                "maximumSensorRange": "Unspecified",
                "minimumSensorRange": "Unspecified",
                "negativeHysteresis": "Unspecified",
                "nominalReading": "0.000",
                "normalMaximum": "0.000",
                "positiveHysteresis": "Unspecified",
                "readableThresholds": "No Thresholds",
                "sensorID": "0x6a",
                "sensorName": "Current 1",
                "sensorReading": "1.200 (+/- 0) Amps",
                "sensorType": "Current",
                "settableThresholds": "No Thresholds",
                "status": "ok",
                "uniqueSensorID": "10.1:0x6a"
              },
              {
                "assertionEvents": [],
                "assertionsEnabled": [],
                "entityID": "10.2 (Power Supply)",
                "eventMessageControl": "Per-threshold",
                "maximumSensorRange": "Unspecified",
                "minimumSensorRange": "Unspecified",
                "negativeHysteresis": "Unspecified",
                "nominalReading": "0.000",
                "normalMaximum": "0.000",
                "positiveHysteresis": "Unspecified",
                "readableThresholds": "No Thresholds",
                "sensorID": "0x6b",
                "sensorName": "Current 2",
                "sensorReading": "0.200 (+/- 0) Amps",
                "sensorType": "Current",
                "settableThresholds": "No Thresholds",
                "status": "ok",
                "uniqueSensorID": "10.2:0x6b"
              },
              {
                "assertionEvents": [],
                "assertionsEnabled": [],
                "entityID": "10.1 (Power Supply)",
                "eventMessageControl": "Per-threshold",
                "maximumSensorRange": "Unspecified",
                "minimumSensorRange": "Unspecified",
                "negativeHysteresis": "Unspecified",
                "nominalReading": "0.000",
                "normalMaximum": "0.000",
                "positiveHysteresis": "Unspecified",
                "readableThresholds": "No Thresholds",
                "sensorID": "0x6c",
                "sensorName": "Voltage 1",
                "sensorReading": "118 (+/- 0) Volts",
                "sensorType": "Voltage",
                "settableThresholds": "No Thresholds",
                "status": "ok",
                "uniqueSensorID": "10.1:0x6c"
              },
              {
                "assertionEvents": [],
                "assertionsEnabled": [],
                "entityID": "10.2 (Power Supply)",
                "eventMessageControl": "Per-threshold",
                "maximumSensorRange": "Unspecified",
                "minimumSensorRange": "Unspecified",
                "negativeHysteresis": "Unspecified",
                "nominalReading": "0.000",
                "normalMaximum": "0.000",
                "positiveHysteresis": "Unspecified",
                "readableThresholds": "No Thresholds",
                "sensorID": "0x6d",
                "sensorName": "Voltage 2",
                "sensorReading": "118 (+/- 0) Volts",
                "sensorType": "Voltage",
                "settableThresholds": "No Thresholds",
                "status": "ok",
                "uniqueSensorID": "10.2:0x6d"
              },
              {
                "assertionEvents": [
                  "Fully Redundant"
                ],
                "assertionsEnabled": [
                  "Fully Redundant",
                  "Redundancy Lost"
                ],
                "entityID": "7.1 (System Board)",
                "sensorID": "0x74",
                "sensorName": "PS Redundancy",
                "sensorType": "Power Supply",
                "statesAsserted": [
                  "Fully Redundant"
                ],
                "uniqueSensorID": "7.1:0x74"
              },
              {
                "assertionEvents": [
                  "Presence detected"
                ],
                "assertionsEnabled": [
                  "Presence detected",
                  "Failure detected",
                  "Predictive failure",
                  "Power Supply AC lost",
                  "Config Error: Vendor Mismatch",
                  "Config Error: Revision Mismatch",
                  "Config Error: Processor Missing",
                  "Config Error"
                ],
                "deassertionsEnabled": [
                  "Presence detected",
                  "Failure detected",
                  "Predictive failure",
                  "Power Supply AC lost",
                  "Config Error: Vendor Mismatch",
                  "Config Error: Revision Mismatch",
                  "Config Error: Processor Missing",
                  "Config Error"
                ],
                "entityID": "10.1 (Power Supply)",
                "sensorID": "0x62",
                "sensorName": "Status",
                "sensorType": "Power Supply",
                "statesAsserted": [
                  "Presence detected"
                ],
                "uniqueSensorID": "10.1:0x62"
              },
              {
                "assertionEvents": [
                  "Presence detected"
                ],
                "assertionsEnabled": [
                  "Presence detected",
                  "Failure detected",
                  "Predictive failure",
                  "Power Supply AC lost",
                  "Config Error: Vendor Mismatch",
                  "Config Error: Revision Mismatch",
                  "Config Error: Processor Missing",
                  "Config Error"
                ],
                "deassertionsEnabled": [
                  "Presence detected",
                  "Failure detected",
                  "Predictive failure",
                  "Power Supply AC lost",
                  "Config Error: Vendor Mismatch",
                  "Config Error: Revision Mismatch",
                  "Config Error: Processor Missing",
                  "Config Error"
                ],
                "entityID": "10.2 (Power Supply)",
                "sensorID": "0x63",
                "sensorName": "Status",
                "sensorType": "Power Supply",
                "statesAsserted": [
                  "Presence detected"
                ],
                "uniqueSensorID": "10.2:0x63"
              },
              {
                "assertionEvents": [],
                "assertionsEnabled": [],
                "deassertionsEnabled": [],
                "entityID": "7.1 (System Board)",
                "eventMessageControl": "Per-threshold",
                "maximumSensorRange": "3556.000",
                "minimumSensorRange": "Unspecified",
                "negativeHysteresis": "Unspecified",
                "nominalReading": "658.000",
                "normalMaximum": "672.000",
                "positiveHysteresis": "Unspecified",
                "readableThresholds": "unc ucr",
                "sensorID": "0x77",
                "sensorName": "Pwr Consumption",
                "sensorReading": "140 (+/- 0) Watts",
                "sensorType": "Current",
                "settableThresholds": "unc",
                "status": "ok",
                "uniqueSensorID": "7.1:0x77",
                "upperCritical": "1218.000",
                "upperNonCritical": "1106.000"
              },
              {
                "assertionEvents": [
                  "OEM Specific"
                ],
                "assertionsEnabled": [],
                "deassertionsEnabled": [],
                "entityID": "7.1 (System Board)",
                "sensorID": "0x76",
                "sensorName": "Power Optimized",
                "sensorType": "Unknown (0xC0)",
                "statesAsserted": [
                  "OEM Specific"
                ],
                "uniqueSensorID": "7.1:0x76"
              },
              {
                "entityID": "11.3 (Add-in Card)",
                "sensorID": "0xf4",
                "sensorName": "SD1",
                "sensorType": "Unknown (0xC9)",
                "uniqueSensorID": "11.3:0xf4"
              },
              {
                "entityID": "11.3 (Add-in Card)",
                "sensorID": "0xf5",
                "sensorName": "SD2",
                "sensorType": "Unknown (0xC9)",
                "uniqueSensorID": "11.3:0xf5"
              },
              {
                "assertionEvents": [
                  "Fully Redundant"
                ],
                "assertionsEnabled": [
                  "Fully Redundant",
                  "Redundancy Lost"
                ],
                "entityID": "11.3 (Add-in Card)",
                "sensorID": "0x78",
                "sensorName": "Redundancy",
                "sensorType": "Unknown (0xC9)",
                "uniqueSensorID": "11.3:0x78"
              },
              {
                "entityID": "34.1 (BIOS)",
                "sensorID": "0x1",
                "sensorName": "ECC Corr Err",
                "sensorType": "Memory",
                "uniqueSensorID": "34.1:0x1"
              },
              {
                "entityID": "34.1 (BIOS)",
                "sensorID": "0x2",
                "sensorName": "ECC Uncorr Err",
                "sensorType": "Memory",
                "uniqueSensorID": "34.1:0x2"
              },
              {
                "entityID": "34.1 (BIOS)",
                "sensorID": "0x3",
                "sensorName": "I/O Channel Chk",
                "sensorType": "Critical Interrupt",
                "uniqueSensorID": "34.1:0x3"
              },
              {
                "entityID": "34.1 (BIOS)",
                "sensorID": "0x4",
                "sensorName": "PCI Parity Err",
                "sensorType": "Critical Interrupt",
                "uniqueSensorID": "34.1:0x4"
              },
              {
                "entityID": "34.1 (BIOS)",
                "sensorID": "0x5",
                "sensorName": "PCI System Err",
                "sensorType": "Critical Interrupt",
                "uniqueSensorID": "34.1:0x5"
              },
              {
                "entityID": "34.1 (BIOS)",
                "sensorID": "0x6",
                "sensorName": "SBE Log Disabled",
                "sensorType": "Event Logging Disabled",
                "uniqueSensorID": "34.1:0x6"
              },
              {
                "entityID": "34.1 (BIOS)",
                "sensorID": "0x7",
                "sensorName": "Logging Disabled",
                "sensorType": "Event Logging Disabled",
                "uniqueSensorID": "34.1:0x7"
              },
              {
                "entityID": "34.1 (BIOS)",
                "sensorID": "0x8",
                "sensorName": "Unknown",
                "sensorType": "System Event",
                "uniqueSensorID": "34.1:0x8"
              },
              {
                "entityID": "34.1 (BIOS)",
                "sensorID": "0xa",
                "sensorName": "CPU Protocol Err",
                "sensorType": "Processor",
                "uniqueSensorID": "34.1:0xa"
              },
              {
                "entityID": "34.1 (BIOS)",
                "sensorID": "0xb",
                "sensorName": "CPU Bus PERR",
                "sensorType": "Processor",
                "uniqueSensorID": "34.1:0xb"
              },
              {
                "entityID": "34.1 (BIOS)",
                "sensorID": "0xc",
                "sensorName": "CPU Init Err",
                "sensorType": "Processor",
                "uniqueSensorID": "34.1:0xc"
              },
              {
                "entityID": "34.1 (BIOS)",
                "sensorID": "0xd",
                "sensorName": "CPU Machine Chk",
                "sensorType": "Processor",
                "uniqueSensorID": "34.1:0xd"
              },
              {
                "entityID": "34.1 (BIOS)",
                "sensorID": "0x11",
                "sensorName": "Memory Spared",
                "sensorType": "Memory",
                "uniqueSensorID": "34.1:0x11"
              },
              {
                "entityID": "34.1 (BIOS)",
                "sensorID": "0x12",
                "sensorName": "Memory Mirrored",
                "sensorType": "Memory",
                "uniqueSensorID": "34.1:0x12"
              },
              {
                "entityID": "34.1 (BIOS)",
                "sensorID": "0x13",
                "sensorName": "Memory RAID",
                "sensorType": "Memory",
                "uniqueSensorID": "34.1:0x13"
              },
              {
                "entityID": "34.1 (BIOS)",
                "sensorID": "0x14",
                "sensorName": "Memory Added",
                "sensorType": "Memory",
                "uniqueSensorID": "34.1:0x14"
              },
              {
                "entityID": "34.1 (BIOS)",
                "sensorID": "0x15",
                "sensorName": "Memory Removed",
                "sensorType": "Memory",
                "uniqueSensorID": "34.1:0x15"
              },
              {
                "entityID": "34.1 (BIOS)",
                "sensorID": "0x16",
                "sensorName": "Memory Cfg Err",
                "sensorType": "Memory",
                "uniqueSensorID": "34.1:0x16"
              },
              {
                "entityID": "34.1 (BIOS)",
                "sensorID": "0x17",
                "sensorName": "Mem Redun Gain",
                "sensorType": "Memory",
                "uniqueSensorID": "34.1:0x17"
              },
              {
                "entityID": "34.1 (BIOS)",
                "sensorID": "0x18",
                "sensorName": "PCIE Fatal Err",
                "sensorType": "Critical Interrupt",
                "uniqueSensorID": "34.1:0x18"
              },
              {
                "entityID": "34.1 (BIOS)",
                "sensorID": "0x19",
                "sensorName": "Chipset Err",
                "sensorType": "Critical Interrupt",
                "uniqueSensorID": "34.1:0x19"
              },
              {
                "entityID": "34.1 (BIOS)",
                "sensorID": "0x1a",
                "sensorName": "Err Reg Pointer",
                "sensorType": "Unknown (0xC1)",
                "uniqueSensorID": "34.1:0x1a"
              },
              {
                "entityID": "34.1 (BIOS)",
                "sensorID": "0x1b",
                "sensorName": "Mem ECC Warning",
                "sensorType": "Memory",
                "uniqueSensorID": "34.1:0x1b"
              },
              {
                "entityID": "34.1 (BIOS)",
                "sensorID": "0x1c",
                "sensorName": "Mem CRC Err",
                "sensorType": "Memory",
                "uniqueSensorID": "34.1:0x1c"
              },
              {
                "entityID": "34.1 (BIOS)",
                "sensorID": "0x1d",
                "sensorName": "USB Over-current",
                "sensorType": "Memory",
                "uniqueSensorID": "34.1:0x1d"
              },
              {
                "entityID": "34.1 (BIOS)",
                "sensorID": "0x1e",
                "sensorName": "POST Err",
                "sensorType": "System Firmwares",
                "uniqueSensorID": "34.1:0x1e"
              },
              {
                "entityID": "34.1 (BIOS)",
                "sensorID": "0x1f",
                "sensorName": "Hdwr version err",
                "sensorType": "Version Change",
                "uniqueSensorID": "34.1:0x1f"
              },
              {
                "entityID": "34.1 (BIOS)",
                "sensorID": "0x20",
                "sensorName": "Mem Overtemp",
                "sensorType": "Memory",
                "uniqueSensorID": "34.1:0x20"
              },
              {
                "entityID": "34.1 (BIOS)",
                "sensorID": "0x21",
                "sensorName": "Mem Fatal SB CRC",
                "sensorType": "Memory",
                "uniqueSensorID": "34.1:0x21"
              },
              {
                "entityID": "34.1 (BIOS)",
                "sensorID": "0x22",
                "sensorName": "Mem Fatal NB CRC",
                "sensorType": "Memory",
                "uniqueSensorID": "34.1:0x22"
              },
              {
                "entityID": "34.1 (BIOS)",
                "sensorID": "0x71",
                "sensorName": "OS Watchdog Time",
                "sensorType": "Watchdog",
                "uniqueSensorID": "34.1:0x71"
              },
              {
                "entityID": "34.1 (BIOS)",
                "sensorID": "0x26",
                "sensorName": "Non Fatal PCI Er",
                "sensorType": "Unknown (0xC2)",
                "uniqueSensorID": "34.1:0x26"
              },
              {
                "entityID": "34.1 (BIOS)",
                "sensorID": "0x27",
                "sensorName": "Fatal IO Error",
                "sensorType": "Unknown (0xC3)",
                "uniqueSensorID": "34.1:0x27"
              },
              {
                "entityID": "34.1 (BIOS)",
                "sensorID": "0x28",
                "sensorName": "MSR Info Log",
                "sensorType": "Unknown (0xC1)",
                "uniqueSensorID": "34.1:0x28"
              },
              {
                "entityID": "34.1 (BIOS)",
                "sensorID": "0x2a",
                "sensorName": "TXT Status",
                "sensorType": "OS Critical Stop",
                "uniqueSensorID": "34.1:0x2a"
              },
              {
                "assertionEvents": [
                  "Drive Present"
                ],
                "assertionsEnabled": [
                  "Drive Present",
                  "Drive Fault"
                ],
                "deassertionsEnabled": [
                  "Drive Present",
                  "Drive Fault"
                ],
                "entityID": "7.1 (System Board)",
                "sensorID": "0xa0",
                "sensorName": "Drive 0",
                "sensorType": "Drive Slot / Bay",
                "uniqueSensorID": "7.1:0xa0"
              },
              {
                "assertionsEnabled": [
                  "Config Error"
                ],
                "deassertionsEnabled": [
                  "Config Error"
                ],
                "entityID": "26.1 (Disk Drive Bay)",
                "eventStatus": "Unavailable",
                "sensorID": "0xe0",
                "sensorName": "Cable SAS A",
                "sensorType": "Cable / Interconnect",
                "uniqueSensorID": "26.1:0xe0"
              },
              {
                "assertionsEnabled": [
                  "Config Error"
                ],
                "deassertionsEnabled": [
                  "Config Error"
                ],
                "entityID": "26.1 (Disk Drive Bay)",
                "eventStatus": "Unavailable",
                "sensorID": "0xe1",
                "sensorName": "Cable SAS B",
                "sensorType": "Cable / Interconnect",
                "uniqueSensorID": "26.1:0xe1"
              },
              {
                "assertionsEnabled": [
                  "Config Error"
                ],
                "deassertionsEnabled": [
                  "Config Error"
                ],
                "entityID": "26.1 (Disk Drive Bay)",
                "eventStatus": "Unavailable",
                "sensorID": "0xe2",
                "sensorName": "Cable SAS C",
                "sensorType": "Cable / Interconnect",
                "uniqueSensorID": "26.1:0xe2"
              },
              {
                "assertionsEnabled": [
                  "Config Error"
                ],
                "deassertionsEnabled": [
                  "Config Error"
                ],
                "entityID": "26.1 (Disk Drive Bay)",
                "eventStatus": "Unavailable",
                "sensorID": "0xe3",
                "sensorName": "Cable SAS D",
                "sensorType": "Cable / Interconnect",
                "uniqueSensorID": "26.1:0xe3"
              },
              {
                "assertionsEnabled": [
                  "Config Error"
                ],
                "deassertionsEnabled": [
                  "Config Error"
                ],
                "entityID": "26.2 (Disk Drive Bay)",
                "sensorID": "0xe4",
                "sensorName": "Cable SAS A",
                "sensorType": "Cable / Interconnect",
                "uniqueSensorID": "26.2:0xe4"
              },
              {
                "assertionsEnabled": [
                  "Config Error"
                ],
                "deassertionsEnabled": [
                  "Config Error"
                ],
                "entityID": "26.2 (Disk Drive Bay)",
                "sensorID": "0xe5",
                "sensorName": "Cable SAS B",
                "sensorType": "Cable / Interconnect",
                "uniqueSensorID": "26.2:0xe5"
              },
              {
                "assertionsEnabled": [
                  "Config Error"
                ],
                "deassertionsEnabled": [
                  "Config Error"
                ],
                "entityID": "26.2 (Disk Drive Bay)",
                "sensorID": "0xe6",
                "sensorName": "Cable SAS C",
                "sensorType": "Cable / Interconnect",
                "uniqueSensorID": "26.2:0xe6"
              },
              {
                "assertionsEnabled": [
                  "Config Error"
                ],
                "deassertionsEnabled": [
                  "Config Error"
                ],
                "entityID": "26.2 (Disk Drive Bay)",
                "sensorID": "0xe7",
                "sensorName": "Cable SAS D",
                "sensorType": "Cable / Interconnect",
                "uniqueSensorID": "26.2:0xe7"
              },
              {
                "assertionEvents": [
                  "Connected"
                ],
                "assertionsEnabled": [
                  "Config Error"
                ],
                "deassertionsEnabled": [
                  "Config Error"
                ],
                "entityID": "26.1 (Disk Drive Bay)",
                "sensorID": "0x58",
                "sensorName": "Power Cable",
                "sensorType": "Cable / Interconnect",
                "statesAsserted": [
                  "Connected"
                ],
                "uniqueSensorID": "26.1:0x58"
              },
              {
                "assertionEvents": [
                  "Connected"
                ],
                "assertionsEnabled": [
                  "Config Error"
                ],
                "deassertionsEnabled": [
                  "Config Error"
                ],
                "entityID": "26.1 (Disk Drive Bay)",
                "sensorID": "0x59",
                "sensorName": "Signal Cable",
                "sensorType": "Cable / Interconnect",
                "statesAsserted": [
                  "Connected"
                ],
                "uniqueSensorID": "26.1:0x59"
              },
              {
                "assertionsEnabled": [
                  "Config Error"
                ],
                "deassertionsEnabled": [
                  "Config Error"
                ],
                "entityID": "26.2 (Disk Drive Bay)",
                "sensorID": "0x5a",
                "sensorName": "Power Cable",
                "sensorType": "Cable / Interconnect",
                "uniqueSensorID": "26.2:0x5a"
              },
              {
                "assertionsEnabled": [
                  "Config Error"
                ],
                "deassertionsEnabled": [
                  "Config Error"
                ],
                "entityID": "26.2 (Disk Drive Bay)",
                "sensorID": "0x5b",
                "sensorName": "Signal Cable",
                "sensorType": "Cable / Interconnect",
                "uniqueSensorID": "26.2:0x5b"
              },
              {
                "assertionEvents": [],
                "assertionsEnabled": [],
                "deassertionsEnabled": [],
                "entityID": "7.1 (System Board)",
                "eventMessageControl": "Per-threshold",
                "lowerCritical": "720.000",
                "lowerNonCritical": "840.000",
                "maximumSensorRange": "Unspecified",
                "minimumSensorRange": "Unspecified",
                "negativeHysteresis": "120.000",
                "nominalReading": "6720.000",
                "normalMaximum": "23640.000",
                "normalMinimum": "16680.000",
                "positiveHysteresis": "120.000",
                "readableThresholds": "lcr lnc",
                "sensorID": "0x3c",
                "sensorName": "Fan7A RPM",
                "sensorReading": "5880 (+/- 120) RPM",
                "sensorType": "Fan",
                "settableThresholds": "",
                "status": "ok",
                "thresholdReadMask": "lcr lnc",
                "uniqueSensorID": "7.1:0x3c"
              },
              {
                "assertionEvents": [],
                "assertionsEnabled": [],
                "deassertionsEnabled": [],
                "entityID": "7.1 (System Board)",
                "eventMessageControl": "Per-threshold",
                "lowerCritical": "720.000",
                "lowerNonCritical": "840.000",
                "maximumSensorRange": "Unspecified",
                "minimumSensorRange": "Unspecified",
                "negativeHysteresis": "120.000",
                "nominalReading": "6720.000",
                "normalMaximum": "23640.000",
                "normalMinimum": "16680.000",
                "positiveHysteresis": "120.000",
                "readableThresholds": "lcr lnc",
                "sensorID": "0x31",
                "sensorName": "Fan1B RPM",
                "sensorReading": "5400 (+/- 120) RPM",
                "sensorType": "Fan",
                "settableThresholds": "",
                "status": "ok",
                "thresholdReadMask": "lcr lnc",
                "uniqueSensorID": "7.1:0x31"
              },
              {
                "assertionEvents": [],
                "assertionsEnabled": [],
                "deassertionsEnabled": [],
                "entityID": "7.1 (System Board)",
                "eventMessageControl": "Per-threshold",
                "lowerCritical": "720.000",
                "lowerNonCritical": "840.000",
                "maximumSensorRange": "Unspecified",
                "minimumSensorRange": "Unspecified",
                "negativeHysteresis": "120.000",
                "nominalReading": "6720.000",
                "normalMaximum": "23640.000",
                "normalMinimum": "16680.000",
                "positiveHysteresis": "120.000",
                "readableThresholds": "lcr lnc",
                "sensorID": "0x33",
                "sensorName": "Fan2B RPM",
                "sensorReading": "5400 (+/- 120) RPM",
                "sensorType": "Fan",
                "settableThresholds": "",
                "status": "ok",
                "thresholdReadMask": "lcr lnc",
                "uniqueSensorID": "7.1:0x33"
              },
              {
                "assertionEvents": [],
                "assertionsEnabled": [],
                "deassertionsEnabled": [],
                "entityID": "7.1 (System Board)",
                "eventMessageControl": "Per-threshold",
                "lowerCritical": "720.000",
                "lowerNonCritical": "840.000",
                "maximumSensorRange": "Unspecified",
                "minimumSensorRange": "Unspecified",
                "negativeHysteresis": "120.000",
                "nominalReading": "6720.000",
                "normalMaximum": "23640.000",
                "normalMinimum": "16680.000",
                "positiveHysteresis": "120.000",
                "readableThresholds": "lcr lnc",
                "sensorID": "0x35",
                "sensorName": "Fan3B RPM",
                "sensorReading": "5520 (+/- 120) RPM",
                "sensorType": "Fan",
                "settableThresholds": "",
                "status": "ok",
                "thresholdReadMask": "lcr lnc",
                "uniqueSensorID": "7.1:0x35"
              },
              {
                "assertionEvents": [],
                "assertionsEnabled": [],
                "deassertionsEnabled": [],
                "entityID": "7.1 (System Board)",
                "eventMessageControl": "Per-threshold",
                "lowerCritical": "720.000",
                "lowerNonCritical": "840.000",
                "maximumSensorRange": "Unspecified",
                "minimumSensorRange": "Unspecified",
                "negativeHysteresis": "120.000",
                "nominalReading": "6720.000",
                "normalMaximum": "23640.000",
                "normalMinimum": "16680.000",
                "positiveHysteresis": "120.000",
                "readableThresholds": "lcr lnc",
                "sensorID": "0x37",
                "sensorName": "Fan4B RPM",
                "sensorReading": "5280 (+/- 120) RPM",
                "sensorType": "Fan",
                "settableThresholds": "",
                "status": "ok",
                "thresholdReadMask": "lcr lnc",
                "uniqueSensorID": "7.1:0x37"
              },
              {
                "assertionEvents": [],
                "assertionsEnabled": [],
                "deassertionsEnabled": [],
                "entityID": "7.1 (System Board)",
                "eventMessageControl": "Per-threshold",
                "lowerCritical": "720.000",
                "lowerNonCritical": "840.000",
                "maximumSensorRange": "Unspecified",
                "minimumSensorRange": "Unspecified",
                "negativeHysteresis": "120.000",
                "nominalReading": "6720.000",
                "normalMaximum": "23640.000",
                "normalMinimum": "16680.000",
                "positiveHysteresis": "120.000",
                "readableThresholds": "lcr lnc",
                "sensorID": "0x39",
                "sensorName": "Fan5B RPM",
                "sensorReading": "5280 (+/- 120) RPM",
                "sensorType": "Fan",
                "settableThresholds": "",
                "status": "ok",
                "thresholdReadMask": "lcr lnc",
                "uniqueSensorID": "7.1:0x39"
              },
              {
                "assertionEvents": [],
                "assertionsEnabled": [],
                "deassertionsEnabled": [],
                "entityID": "7.1 (System Board)",
                "eventMessageControl": "Per-threshold",
                "lowerCritical": "720.000",
                "lowerNonCritical": "840.000",
                "maximumSensorRange": "Unspecified",
                "minimumSensorRange": "Unspecified",
                "negativeHysteresis": "120.000",
                "nominalReading": "6720.000",
                "normalMaximum": "23640.000",
                "normalMinimum": "16680.000",
                "positiveHysteresis": "120.000",
                "readableThresholds": "lcr lnc",
                "sensorID": "0x3b",
                "sensorName": "Fan6B RPM",
                "sensorReading": "5640 (+/- 120) RPM",
                "sensorType": "Fan",
                "settableThresholds": "",
                "status": "ok",
                "thresholdReadMask": "lcr lnc",
                "uniqueSensorID": "7.1:0x3b"
              },
              {
                "assertionEvents": [],
                "assertionsEnabled": [],
                "deassertionsEnabled": [],
                "entityID": "7.1 (System Board)",
                "eventMessageControl": "Per-threshold",
                "lowerCritical": "720.000",
                "lowerNonCritical": "840.000",
                "maximumSensorRange": "Unspecified",
                "minimumSensorRange": "Unspecified",
                "negativeHysteresis": "120.000",
                "nominalReading": "6720.000",
                "normalMaximum": "23640.000",
                "normalMinimum": "16680.000",
                "positiveHysteresis": "120.000",
                "readableThresholds": "lcr lnc",
                "sensorID": "0x3d",
                "sensorName": "Fan7B RPM",
                "sensorReading": "5520 (+/- 120) RPM",
                "sensorType": "Fan",
                "settableThresholds": "",
                "status": "ok",
                "thresholdReadMask": "lcr lnc",
                "uniqueSensorID": "7.1:0x3d"
              },
              {
                "entityID": "7.1 (System Board)",
                "sensorID": "0x66",
                "sensorName": "PFault Fail Safe",
                "sensorType": "Voltage",
                "uniqueSensorID": "7.1:0x66"
              },
              {
                "assertionEvents": [
                  "Presence Detected"
                ],
                "entityID": "32.1 (Memory Device)",
                "sensorID": "0xc0",
                "sensorName": "A",
                "sensorType": "Memory",
                "statesAsserted": [
                  "Presence Detected"
                ],
                "uniqueSensorID": "32.1:0xc0"
              },
              {
                "assertionEvents": [
                  "Presence Detected"
                ],
                "entityID": "32.1 (Memory Device)",
                "sensorID": "0xcc",
                "sensorName": "B",
                "sensorType": "Memory",
                "statesAsserted": [
                  "Presence Detected"
                ],
                "uniqueSensorID": "32.1:0xcc"
              }
            ]
          }
        }
      }
    ]
  }
}"""

RESP_GetLimits_v9_0 = """{
  "id": 1,
  "result": {
    "accountCountMax": 5000,
    "accountNameLengthMax": 64,
    "accountNameLengthMin": 1,
    "bulkVolumeJobsPerNodeMax": 8,
    "bulkVolumeJobsPerVolumeMax": 2,
    "cloneJobsPerVolumeMax": 2,
    "clusterPairsCountMax": 4,
    "initiatorAliasLengthMax": 224,
    "initiatorCountMax": 0,
    "initiatorNameLengthMax": 224,
    "initiatorsPerVolumeAccessGroupCountMax": 64,
    "iscsiSessionsFromFibreChannelNodesMax": 4096,
    "secretLengthMax": 16,
    "secretLengthMin": 12,
    "snapshotNameLengthMax": 64,
    "snapshotsPerVolumeMax": 32,
    "volumeAccessGroupCountMax": 1000,
    "volumeAccessGroupLunMax": 16383,
    "volumeAccessGroupNameLengthMax": 64,
    "volumeAccessGroupNameLengthMin": 1,
    "volumeAccessGroupsPerInitiatorCountMax": 1,
    "volumeAccessGroupsPerVolumeCountMax": 4,
    "volumeBurstIOPSMax": 100000,
    "volumeBurstIOPSMin": 100,
    "volumeCountMax": 4000,
    "volumeMaxIOPSMax": 100000,
    "volumeMaxIOPSMin": 100,
    "volumeMinIOPSMax": 15000,
    "volumeMinIOPSMin": 50,
    "volumeNameLengthMax": 64,
    "volumeNameLengthMin": 1,
    "volumeSizeMax": 8000000491520,
    "volumeSizeMin": 1000000000,
    "volumesPerAccountCountMax": 2000,
    "volumesPerGroupSnapshotMax": 32,
    "volumesPerVolumeAccessGroupCountMax": 2000
  }
}"""

RESP_GetNetworkConfig_v9_0 = """{
  "id": null,
  "result":
  {
    "network":
    {
      "Bond10G":
      {
        "#default": false,
        "address": "192.168.65.161",
        "auto": true,
        "bond-downdelay": "200",
        "bond-fail_over_mac": "None",
        "bond-miimon": "100",
        "bond-mode": "ActivePassive",
        "bond-primary_reselect": "Failure",
        "bond-slaves": "eth0 eth1",
        "bond-updelay": "200",
        "dns-nameservers": "",
        "dns-search": "",
        "family": "inet",
        "gateway": "192.168.95.254",
        "macAddress": "d4:ae:52:8a:6c:77",
        "macAddressPermanent": "00:00:00:00:00:00",
        "method": "static",
        "mtu": "9000",
        "netmask": "255.255.224.0",
        "network": "192.168.64.0",
        "physical":
        {
          "address": "192.168.65.161",
          "macAddress": "d4:ae:52:8a:6c:77",
          "macAddressPermanent": "00:00:00:00:00:00",
          "mtu": "9000",
          "netmask": "255.255.224.0",
          "network": "192.168.64.0",
          "upAndRunning": true
        },
        "routes": [],
        "status": "UpAndRunning",
        "symmetricRouteRules":
        [
          "ip route add 192.168.64.0/19 dev Bond10G src 192.168.65.161 table Bond10G",
          "ip route add default via 192.168.95.254 dev Bond10G src 192.168.65.161 table Bond10G",
          "ip rule add from 192.168.65.161 table Bond10G"
        ],
        "upAndRunning": true,
        "virtualNetworkTag": "2064"
      },
      "Bond1G":
      {
        "#default": true,
        "address": "10.30.65.161",
        "auto": true,
        "bond-downdelay": "200",
        "bond-fail_over_mac": "None",
        "bond-miimon": "100",
        "bond-mode": "ActivePassive",
        "bond-primary_reselect": "Failure",
        "bond-slaves": "eth2 eth3",
        "bond-updelay": "200",
        "dns-nameservers": "",
        "dns-search": "",
        "family": "inet",
        "gateway": "10.30.95.254",
        "macAddress": "d4:ae:52:8a:6c:7b",
        "macAddressPermanent": "00:00:00:00:00:00",
        "method": "static",
        "mtu": "1500",
        "netmask": "255.255.224.0",
        "network": "10.30.64.0",
        "physical":
        {
          "address": "10.30.65.161",
          "macAddress": "d4:ae:52:8a:6c:7b",
          "macAddressPermanent": "00:00:00:00:00:00",
          "mtu": "1500",
          "netmask": "255.255.224.0",
          "network": "10.30.64.0",
          "upAndRunning": true
        },
        "routes": [],
        "status": "UpAndRunning",
        "symmetricRouteRules":
        [
          "ip route add 10.30.64.0/19 dev Bond1G src 10.30.65.161 table Bond1G",
          "ip route add default via 10.30.95.254 dev Bond1G src 10.30.65.161 table Bond1G",
          "ip rule add from 10.30.65.161 table Bond1G",
          "ip route add default via 10.30.95.254"
        ],
        "upAndRunning": true,
        "virtualNetworkTag": "1064"
      },
      "eth0":
      {
        "auto": true,
        "bond-master": "Bond10G",
        "family": "inet",
        "macAddress": "d4:ae:52:8a:6c:77",
        "macAddressPermanent": "d4:ae:52:8a:6c:77",
        "method": "bond",
        "physical":
        {
          "address": "0.0.0.0",
          "macAddress": "d4:ae:52:8a:6c:77",
          "macAddressPermanent": "d4:ae:52:8a:6c:77",
          "netmask": "N/A",
          "network": "N/A",
          "upAndRunning": true
        },
        "status": "UpAndRunning",
        "upAndRunning": true
      },
      "eth1":
      {
        "auto": true,
        "bond-master": "Bond10G",
        "family": "inet",
        "macAddress": "d4:ae:52:8a:6c:77",
        "macAddressPermanent": "d4:ae:52:8a:6c:79",
        "method": "bond",
        "physical":
        {
          "address": "0.0.0.0",
          "macAddress": "d4:ae:52:8a:6c:77",
          "macAddressPermanent": "d4:ae:52:8a:6c:79",
          "netmask": "N/A",
          "network": "N/A",
          "upAndRunning": true
        },
        "status": "UpAndRunning",
        "upAndRunning": true
      },
      "eth2":
      {
        "auto": true,
        "bond-master": "Bond1G",
        "family": "inet",
        "macAddress": "d4:ae:52:8a:6c:7b",
        "macAddressPermanent": "d4:ae:52:8a:6c:7b",
        "method": "bond",
        "physical":
        {
          "address": "0.0.0.0",
          "macAddress": "d4:ae:52:8a:6c:7b",
          "macAddressPermanent": "d4:ae:52:8a:6c:7b",
          "netmask": "N/A",
          "network": "N/A",
          "upAndRunning": true
        },
        "status": "UpAndRunning",
        "upAndRunning": true
      },
      "eth3":
      {
        "auto": true,
        "bond-master": "Bond1G",
        "family": "inet",
        "macAddress": "d4:ae:52:8a:6c:7b",
        "macAddressPermanent": "d4:ae:52:8a:6c:7d",
        "method": "bond",
        "physical":
        {
          "address": "0.0.0.0",
          "macAddress": "d4:ae:52:8a:6c:7b",
          "macAddressPermanent": "d4:ae:52:8a:6c:7d",
          "netmask": "N/A",
          "network": "N/A",
          "upAndRunning": true
        },
        "status": "UpAndRunning",
        "upAndRunning": true
      },
      "lo":
      {
        "auto": true,
        "family": "inet",
        "macAddress": "00:00:00:00:00:00",
        "macAddressPermanent": "00:00:00:00:00:00",
        "method": "loopback",
        "physical":
        {
          "address": "0.0.0.0",
          "macAddress": "00:00:00:00:00:00",
          "macAddressPermanent": "00:00:00:00:00:00",
          "netmask": "N/A",
          "network": "N/A",
          "upAndRunning": true
        },
        "status": "UpAndRunning",
        "upAndRunning": true
      }
    }
  }
}"""

RESP_GetNodeHardwareInfo_v9_0 = """{
  "id": null,
  "result": {
    "nodeHardwareInfo": {
      "bus": {
        "core_DMI:0200": {
          "description": "Motherboard",
          "physid": "0",
          "product": "0H47HH",
          "serial": "..CN7475122J0059.",
          "vendor": "SolidFire",
          "version": "A00"
        }
      },
      "driveHardware": [
        {
          "canonicalName": "sda",
          "connected": true,
          "dev": 2052,
          "devPath": "/dev/sdimm0p4",
          "driveType": "Slice",
          "lifeRemainingPercent": 100,
          "lifetimeReadBytes": 1471026298880,
          "lifetimeWriteBytes": 657129996288,
          "name": "scsi-SATA_VRFSD3400GBCTMM203529284-part4",
          "path": "/dev/sda4",
          "pathLink": "/dev/sdimm0p4",
          "powerOnHours": 21889,
          "product": "VRFSD3400GBCTMMAS1",
          "reallocatedSectors": 0,
          "reserveCapacityPercent": 100,
          "scsiCompatId": "scsi-SATA_VRFSD3400GBCTMM203529284-part4",
          "scsiState": "Running",
          "securityAtMaximum": false,
          "securityEnabled": false,
          "securityFrozen": true,
          "securityLocked": false,
          "securitySupported": true,
          "serial": "203529284",
          "size": 299988156416,
          "slot": -1,
          "uuid": "f0b19a4b-c9a2-2e58-335f-cceb20c306cd",
          "vendor": "Viking",
          "version": "365A13F0"
        },
        {
          "canonicalName": "sdb",
          "connected": true,
          "dev": 2064,
          "devPath": "/dev/slot0",
          "driveType": "Block",
          "lifeRemainingPercent": 67,
          "lifetimeReadBytes": 21367697178624,
          "lifetimeWriteBytes": 28688770924544,
          "name": "scsi-SATA_INTEL_SSDSA2CW3CVPR14620193300EGN",
          "path": "/dev/sdb",
          "pathLink": "/dev/slot0",
          "powerOnHours": 37461,
          "product": "INTEL SSDSA2CW300G3",
          "reallocatedSectors": 0,
          "reserveCapacityPercent": 100,
          "scsiCompatId": "scsi-SATA_INTEL_SSDSA2CW3CVPR14620193300EGN",
          "scsiState": "Running",
          "securityAtMaximum": false,
          "securityEnabled": false,
          "securityFrozen": false,
          "securityLocked": false,
          "securitySupported": true,
          "serial": "CVPR14620193300EGN",
          "size": 300069052416,
          "slot": 0,
          "uuid": "b198c917-5ffe-ae63-0940-8765f786ed64",
          "vendor": "Intel",
          "version": "4PC10362"
        },
        {
          "canonicalName": "sdh",
          "connected": true,
          "dev": 2160,
          "devPath": "/dev/slot1",
          "driveType": "Block",
          "lifeRemainingPercent": 68,
          "lifetimeReadBytes": 21356489998336,
          "lifetimeWriteBytes": 28929087766528,
          "name": "scsi-SATA_INTEL_SSDSA2CW3CVPR1461053H300EGN",
          "path": "/dev/sdh",
          "pathLink": "/dev/slot1",
          "powerOnHours": 37345,
          "product": "INTEL SSDSA2CW300G3",
          "reallocatedSectors": 0,
          "reserveCapacityPercent": 100,
          "scsiCompatId": "scsi-SATA_INTEL_SSDSA2CW3CVPR1461053H300EGN",
          "scsiState": "Running",
          "securityAtMaximum": false,
          "securityEnabled": false,
          "securityFrozen": false,
          "securityLocked": false,
          "securitySupported": true,
          "serial": "CVPR1461053H300EGN",
          "size": 300069052416,
          "slot": 1,
          "uuid": "355b7f51-e861-97f3-48f5-0b9bb4bb86b6",
          "vendor": "Intel",
          "version": "4PC10362"
        },
        {
          "canonicalName": "sdj",
          "connected": true,
          "dev": 2192,
          "devPath": "/dev/slot2",
          "driveType": "Block",
          "lifeRemainingPercent": 68,
          "lifetimeReadBytes": 21170531336192,
          "lifetimeWriteBytes": 28565223505920,
          "name": "scsi-SATA_INTEL_SSDSA2CW3CVPR146101TT300EGN",
          "path": "/dev/sdj",
          "pathLink": "/dev/slot2",
          "powerOnHours": 37457,
          "product": "INTEL SSDSA2CW300G3",
          "reallocatedSectors": 0,
          "reserveCapacityPercent": 100,
          "scsiCompatId": "scsi-SATA_INTEL_SSDSA2CW3CVPR146101TT300EGN",
          "scsiState": "Running",
          "securityAtMaximum": false,
          "securityEnabled": false,
          "securityFrozen": false,
          "securityLocked": false,
          "securitySupported": true,
          "serial": "CVPR146101TT300EGN",
          "size": 300069052416,
          "slot": 2,
          "uuid": "b62dbadf-e62e-894e-37df-ac9dce6594ff",
          "vendor": "Intel",
          "version": "4PC10362"
        },
        {
          "canonicalName": "sdg",
          "connected": true,
          "dev": 2144,
          "devPath": "/dev/slot3",
          "driveType": "Block",
          "lifeRemainingPercent": 68,
          "lifetimeReadBytes": 21286562562048,
          "lifetimeWriteBytes": 28216995610624,
          "name": "scsi-SATA_INTEL_SSDSA2CW3CVPR14620AP5300EGN",
          "path": "/dev/sdg",
          "pathLink": "/dev/slot3",
          "powerOnHours": 37344,
          "product": "INTEL SSDSA2CW300G3",
          "reallocatedSectors": 0,
          "reserveCapacityPercent": 100,
          "scsiCompatId": "scsi-SATA_INTEL_SSDSA2CW3CVPR14620AP5300EGN",
          "scsiState": "Running",
          "securityAtMaximum": false,
          "securityEnabled": false,
          "securityFrozen": false,
          "securityLocked": false,
          "securitySupported": true,
          "serial": "CVPR14620AP5300EGN",
          "size": 300069052416,
          "slot": 3,
          "uuid": "c5d7a7ee-7cdf-494a-76e3-72f2284023d4",
          "vendor": "Intel",
          "version": "4PC10362"
        },
        {
          "canonicalName": "sdi",
          "connected": true,
          "dev": 2176,
          "devPath": "/dev/slot4",
          "driveType": "Block",
          "lifeRemainingPercent": 68,
          "lifetimeReadBytes": 16556394283008,
          "lifetimeWriteBytes": 24971912937472,
          "name": "scsi-SATA_INTEL_SSDSA2CW3CVPR142108T5300EGN",
          "path": "/dev/sdi",
          "pathLink": "/dev/slot4",
          "powerOnHours": 37495,
          "product": "INTEL SSDSA2CW300G3",
          "reallocatedSectors": 0,
          "reserveCapacityPercent": 100,
          "scsiCompatId": "scsi-SATA_INTEL_SSDSA2CW3CVPR142108T5300EGN",
          "scsiState": "Running",
          "securityAtMaximum": false,
          "securityEnabled": false,
          "securityFrozen": false,
          "securityLocked": false,
          "securitySupported": true,
          "serial": "CVPR142108T5300EGN",
          "size": 300069052416,
          "slot": 4,
          "uuid": "545dd40d-8344-dda5-2e3d-c2ad4005283b",
          "vendor": "Intel",
          "version": "4PC10362"
        },
        {
          "canonicalName": "sdk",
          "connected": true,
          "dev": 2208,
          "devPath": "/dev/slot5",
          "driveType": "Block",
          "lifeRemainingPercent": 68,
          "lifetimeReadBytes": 21341323395072,
          "lifetimeWriteBytes": 28911270363136,
          "name": "scsi-SATA_INTEL_SSDSA2CW3CVPR146401ZY300EGN",
          "path": "/dev/sdk",
          "pathLink": "/dev/slot5",
          "powerOnHours": 37458,
          "product": "INTEL SSDSA2CW300G3",
          "reallocatedSectors": 0,
          "reserveCapacityPercent": 100,
          "scsiCompatId": "scsi-SATA_INTEL_SSDSA2CW3CVPR146401ZY300EGN",
          "scsiState": "Running",
          "securityAtMaximum": false,
          "securityEnabled": false,
          "securityFrozen": false,
          "securityLocked": false,
          "securitySupported": true,
          "serial": "CVPR146401ZY300EGN",
          "size": 300069052416,
          "slot": 5,
          "uuid": "47175675-a5e0-267b-4288-015ca5e9ef1b",
          "vendor": "Intel",
          "version": "4PC10362"
        },
        {
          "canonicalName": "sdc",
          "connected": true,
          "dev": 2080,
          "devPath": "/dev/slot6",
          "driveType": "Block",
          "lifeRemainingPercent": 68,
          "lifetimeReadBytes": 21032555511808,
          "lifetimeWriteBytes": 28401511432192,
          "name": "scsi-SATA_INTEL_SSDSA2CW3CVPR146007NL300EGN",
          "path": "/dev/sdc",
          "pathLink": "/dev/slot6",
          "powerOnHours": 37261,
          "product": "INTEL SSDSA2CW300G3",
          "reallocatedSectors": 0,
          "reserveCapacityPercent": 100,
          "scsiCompatId": "scsi-SATA_INTEL_SSDSA2CW3CVPR146007NL300EGN",
          "scsiState": "Running",
          "securityAtMaximum": false,
          "securityEnabled": false,
          "securityFrozen": false,
          "securityLocked": false,
          "securitySupported": true,
          "serial": "CVPR146007NL300EGN",
          "size": 300069052416,
          "slot": 6,
          "uuid": "7524866c-4a31-1a4a-7aad-32b4cf83d176",
          "vendor": "Intel",
          "version": "4PC10362"
        },
        {
          "canonicalName": "sde",
          "connected": true,
          "dev": 2112,
          "devPath": "/dev/slot7",
          "driveType": "Block",
          "lifeRemainingPercent": 68,
          "lifetimeReadBytes": 21204454866944,
          "lifetimeWriteBytes": 28637466198016,
          "name": "scsi-SATA_INTEL_SSDSA2CW3CVPR146007NE300EGN",
          "path": "/dev/sde",
          "pathLink": "/dev/slot7",
          "powerOnHours": 37460,
          "product": "INTEL SSDSA2CW300G3",
          "reallocatedSectors": 0,
          "reserveCapacityPercent": 100,
          "scsiCompatId": "scsi-SATA_INTEL_SSDSA2CW3CVPR146007NE300EGN",
          "scsiState": "Running",
          "securityAtMaximum": false,
          "securityEnabled": false,
          "securityFrozen": false,
          "securityLocked": false,
          "securitySupported": true,
          "serial": "CVPR146007NE300EGN",
          "size": 300069052416,
          "slot": 7,
          "uuid": "e498c538-5798-22e7-5933-48e1e0ef9960",
          "vendor": "Intel",
          "version": "4PC10362"
        },
        {
          "canonicalName": "sdf",
          "connected": true,
          "dev": 2128,
          "devPath": "/dev/slot8",
          "driveType": "Block",
          "lifeRemainingPercent": 100,
          "lifetimeReadBytes": 201326592,
          "lifetimeWriteBytes": 167772160,
          "name": "scsi-SATA_INTEL_SSDSA2CW3CVPR146104SF300EGN",
          "path": "/dev/sdf",
          "pathLink": "/dev/slot8",
          "powerOnHours": 1843,
          "product": "INTEL SSDSA2CW300G3",
          "reallocatedSectors": 0,
          "reserveCapacityPercent": 100,
          "scsiCompatId": "scsi-SATA_INTEL_SSDSA2CW3CVPR146104SF300EGN",
          "scsiState": "Running",
          "securityAtMaximum": false,
          "securityEnabled": false,
          "securityFrozen": false,
          "securityLocked": false,
          "securitySupported": true,
          "serial": "CVPR146104SF300EGN",
          "size": 300069052416,
          "slot": 8,
          "uuid": "9cc657ad-b162-6a56-b3ae-2d5c4f85bf1e",
          "vendor": "Intel",
          "version": "4PC10362"
        },
        {
          "canonicalName": "sdd",
          "connected": true,
          "dev": 2096,
          "devPath": "/dev/slot9",
          "driveType": "Block",
          "lifeRemainingPercent": 68,
          "lifetimeReadBytes": 21338504822784,
          "lifetimeWriteBytes": 28405235974144,
          "name": "scsi-SATA_INTEL_SSDSA2CW3CVPR1462045W300EGN",
          "path": "/dev/sdd",
          "pathLink": "/dev/slot9",
          "powerOnHours": 37464,
          "product": "INTEL SSDSA2CW300G3",
          "reallocatedSectors": 0,
          "reserveCapacityPercent": 100,
          "scsiCompatId": "scsi-SATA_INTEL_SSDSA2CW3CVPR1462045W300EGN",
          "scsiState": "Running",
          "securityAtMaximum": false,
          "securityEnabled": false,
          "securityFrozen": false,
          "securityLocked": false,
          "securitySupported": true,
          "serial": "CVPR1462045W300EGN",
          "size": 300069052416,
          "slot": 9,
          "uuid": "caa5012e-c5ce-f2c7-a02c-0f0e6e986c3a",
          "vendor": "Intel",
          "version": "4PC10362"
        }
      ],
      "fibreChannelPorts": [],
      "fileSystemUsage": {},
      "hardwareConfig": {
        "BIOS_REVISION": {
          "Passed": true,
          "actual": "1.1",
          "comparator": ">=",
          "expected": "1.0.0.0"
        },
        "BIOS_VENDOR": {
          "Passed": true,
          "actual": "SolidFire",
          "comparator": "==",
          "expected": "SolidFire"
        },
        "BIOS_VERSION": {
          "Passed": true,
          "actual": "1.1.2",
          "comparator": ">=",
          "expected": "1.1.2"
        },
        "CPU_CORES_00": {
          "Passed": true,
          "actual": "6",
          "comparator": "==",
          "expected": "6"
        },
        "CPU_CORES_01": {
          "Passed": true,
          "actual": "6",
          "comparator": "==",
          "expected": "6"
        },
        "CPU_CORES_ENABLED_00": {
          "Passed": true,
          "actual": "6",
          "comparator": "==",
          "expected": "6"
        },
        "CPU_CORES_ENABLED_01": {
          "Passed": true,
          "actual": "6",
          "comparator": "==",
          "expected": "6"
        },
        "CPU_MODEL_00": {
          "Passed": true,
          "actual": "Intel(R) Xeon(R) CPU E5-2640 0 @ 2.50GHz",
          "comparator": "==",
          "expected": "Intel(R) Xeon(R) CPU E5-2640 0 @ 2.50GHz"
        },
        "CPU_MODEL_01": {
          "Passed": true,
          "actual": "Intel(R) Xeon(R) CPU E5-2640 0 @ 2.50GHz",
          "comparator": "==",
          "expected": "Intel(R) Xeon(R) CPU E5-2640 0 @ 2.50GHz"
        },
        "CPU_THREADS_00": {
          "Passed": true,
          "actual": "12",
          "comparator": "==",
          "expected": "12"
        },
        "CPU_THREADS_01": {
          "Passed": true,
          "actual": "12",
          "comparator": "==",
          "expected": "12"
        },
        "CPU_THREADS_ENABLED": {
          "Passed": true,
          "actual": "24",
          "comparator": "==",
          "expected": "24"
        },
        "IDRAC_VERSION": {
          "Passed": true,
          "actual": "1.06.06",
          "comparator": ">=",
          "expected": "1.06.06"
        },
        "LIFECYCLE_VERSION": {
          "Passed": true,
          "actual": "1.0.0.5747",
          "comparator": ">=",
          "expected": "1.0.0.5747"
        },
        "MEMORY_GB": {
          "Passed": true,
          "actual": "72",
          "comparator": ">=",
          "expected": "72"
        },
        "MEMORY_MHZ_00": {
          "Passed": true,
          "actual": "1333",
          "comparator": ">=",
          "expected": "1333"
        },
        "MEMORY_MHZ_01": {
          "Passed": true,
          "actual": "1333",
          "comparator": ">=",
          "expected": "1333"
        },
        "MEMORY_MHZ_02": {
          "Passed": true,
          "actual": "1333",
          "comparator": ">=",
          "expected": "1333"
        },
        "MEMORY_MHZ_03": {
          "Passed": true,
          "actual": "1333",
          "comparator": ">=",
          "expected": "1333"
        },
        "MEMORY_MHZ_04": {
          "Passed": true,
          "actual": "1333",
          "comparator": ">=",
          "expected": "1333"
        },
        "MEMORY_MHZ_05": {
          "Passed": true,
          "actual": "1333",
          "comparator": ">=",
          "expected": "1333"
        },
        "MEMORY_MHZ_06": {
          "Passed": true,
          "actual": "1333",
          "comparator": ">=",
          "expected": "1333"
        },
        "MEMORY_MHZ_07": {
          "Passed": true,
          "actual": "1333",
          "comparator": ">=",
          "expected": "1333"
        },
        "MEMORY_MHZ_08": {
          "Passed": true,
          "actual": "1333",
          "comparator": ">=",
          "expected": "1333"
        },
        "MEMORY_MHZ_09": {
          "Passed": true,
          "actual": "1333",
          "comparator": ">=",
          "expected": "1333"
        },
        "MEMORY_MHZ_10": {
          "Passed": true,
          "actual": "1333",
          "comparator": ">=",
          "expected": "1333"
        },
        "MEMORY_MHZ_11": {
          "Passed": true,
          "actual": "1333",
          "comparator": ">=",
          "expected": "1333"
        },
        "MPTSAS_BIOS_VERSION": {
          "Passed": true,
          "actual": "07.25.00.00",
          "comparator": "==",
          "expected": "7.25.0.0"
        },
        "MPTSAS_FIRMWARE_VERSION": {
          "Passed": true,
          "actual": "13.00.57.00",
          "comparator": "==",
          "expected": "13.0.57.0"
        },
        "NETWORK_DRIVER_ETH0": {
          "Passed": true,
          "actual": "bnx2x",
          "comparator": "==",
          "expected": "bnx2x"
        },
        "NETWORK_DRIVER_ETH1": {
          "Passed": true,
          "actual": "bnx2x",
          "comparator": "==",
          "expected": "bnx2x"
        },
        "NETWORK_DRIVER_ETH2": {
          "Passed": true,
          "actual": "bnx2x",
          "comparator": "==",
          "expected": "bnx2x"
        },
        "NETWORK_DRIVER_ETH3": {
          "Passed": true,
          "actual": "bnx2x",
          "comparator": "==",
          "expected": "bnx2x"
        },
        "NETWORK_FIRMWARE_VERSION_ETH0": {
          "Passed": true,
          "actual": "7.10.18-solidfire-386560b9d0e3.",
          "comparator": "==",
          "expected": "7.10.18-solidfire-386560b9d0e3."
        },
        "NETWORK_FIRMWARE_VERSION_ETH1": {
          "Passed": true,
          "actual": "7.10.18-solidfire-386560b9d0e3.",
          "comparator": "==",
          "expected": "7.10.18-solidfire-386560b9d0e3."
        },
        "NETWORK_FIRMWARE_VERSION_ETH2": {
          "Passed": true,
          "actual": "7.10.18-solidfire-386560b9d0e3.",
          "comparator": "==",
          "expected": "7.10.18-solidfire-386560b9d0e3."
        },
        "NETWORK_FIRMWARE_VERSION_ETH3": {
          "Passed": true,
          "actual": "7.10.18-solidfire-386560b9d0e3.",
          "comparator": "==",
          "expected": "7.10.18-solidfire-386560b9d0e3."
        },
        "NUM_CPU": {
          "Passed": true,
          "actual": "2",
          "comparator": "==",
          "expected": "2"
        }
      },
      "kernelCrashDumpState": "EnabledByDefault",
      "memory": {
        "firmware_": {
          "capacity": "8323072",
          "date": "03/08/2012",
          "description": "BIOS",
          "physid": "0",
          "size": "65536",
          "vendor": "SolidFire",
          "version": "1.1.2"
        },
        "memory_DMI:1000": {
          "description": "System Memory",
          "physid": "1000",
          "size": "77309411328",
          "slot": "System board or motherboard"
        }
      },
      "network": {
        "network:0_": {
          "description": "Ethernet interface",
          "logicalname": "Bond1G",
          "physid": "1",
          "serial": "d4:ae:52:7a:bb:b1"
        },
        "network:0_PCI:0000:01:00.0": {
          "businfo": "pci@0000:01:00.0",
          "capacity": "1000000000",
          "clock": "33000000",
          "description": "Ethernet interface",
          "logicalname": "eth0",
          "physid": "0",
          "product": "NetXtreme II BCM57800 1/10 Gigabit Ethernet",
          "serial": "d4:ae:52:7a:bb:ad",
          "vendor": "Broadcom Corporation",
          "version": "10",
          "width": "64"
        },
        "network:1_": {
          "description": "Ethernet interface",
          "logicalname": "Bond10G",
          "physid": "2",
          "serial": "d4:ae:52:7a:bb:ad"
        },
        "network:1_PCI:0000:01:00.1": {
          "businfo": "pci@0000:01:00.1",
          "capacity": "1000000000",
          "clock": "33000000",
          "description": "Ethernet interface",
          "logicalname": "eth1",
          "physid": "0.1",
          "product": "NetXtreme II BCM57800 1/10 Gigabit Ethernet",
          "serial": "d4:ae:52:7a:bb:ad",
          "vendor": "Broadcom Corporation",
          "version": "10",
          "width": "64"
        },
        "network:2_PCI:0000:01:00.2": {
          "businfo": "pci@0000:01:00.2",
          "capacity": "1000000000",
          "clock": "33000000",
          "description": "Ethernet interface",
          "logicalname": "eth2",
          "physid": "0.2",
          "product": "NetXtreme II BCM57800 1/10 Gigabit Ethernet",
          "serial": "d4:ae:52:7a:bb:b1",
          "size": "1000000000",
          "vendor": "Broadcom Corporation",
          "version": "10",
          "width": "64"
        },
        "network:3_PCI:0000:01:00.3": {
          "businfo": "pci@0000:01:00.3",
          "capacity": "1000000000",
          "clock": "33000000",
          "description": "Ethernet interface",
          "logicalname": "eth3",
          "physid": "0.3",
          "product": "NetXtreme II BCM57800 1/10 Gigabit Ethernet",
          "serial": "d4:ae:52:7a:bb:b1",
          "size": "1000000000",
          "vendor": "Broadcom Corporation",
          "version": "10",
          "width": "64"
        }
      },
      "networkInterfaces": {
        "Bond10G": {
          "isConfigured": true,
          "isUp": true
        },
        "Bond1G": {
          "isConfigured": true,
          "isUp": true
        },
        "eth0": {
          "isConfigured": true,
          "isUp": true
        },
        "eth1": {
          "isConfigured": true,
          "isUp": true
        },
        "eth2": {
          "isConfigured": true,
          "isUp": true
        },
        "eth3": {
          "isConfigured": true,
          "isUp": true
        }
      },
      "nvram": {
        "errors": {
          "numOfErrorLogEntries": "0"
        },
        "extended": {
          "dialogVersion": "4",
          "event": [
            {
              "name": "flushToFlash",
              "time": "2016-07-28 17:43:56",
              "value": "0"
            },
            {
              "name": "flushToFlash",
              "time": "2016-07-28 17:59:28",
              "value": "0"
            },
            {
              "name": "flushToFlash",
              "time": "1948-07-10 14:45:43",
              "value": "0"
            },
            {
              "name": "flushToFlash",
              "time": "2016-07-28 18:37:02",
              "value": "0"
            },
            {
              "name": "flushToFlash",
              "time": "1948-07-10 15:23:17",
              "value": "0"
            },
            {
              "name": "flushToFlash",
              "time": "2016-07-28 20:28:01",
              "value": "0"
            },
            {
              "name": "flushToFlash",
              "time": "2016-08-10 20:11:31",
              "value": "0"
            },
            {
              "name": "flushToFlash",
              "time": "2016-08-10 20:31:47",
              "value": "0"
            },
            {
              "name": "excessiveCurrent",
              "time": "2014-07-31 21:12:08",
              "value": "244"
            }
          ],
          "eventOccurrences": [
            {
              "count": "143",
              "name": "flushToFlash"
            },
            {
              "count": "1",
              "name": "excessiveCurrent"
            }
          ],
          "initialCapacitance": "7.126 F",
          "initialEsr": "0.097 Ohm",
          "measurement": [
            {
              "level_0": " 0",
              "level_1": " 387",
              "level_2": " 4235656",
              "level_3": " 156318",
              "level_4": " 18423319",
              "level_5": " 11903",
              "level_6": " 0",
              "level_7": " 0",
              "level_8": " 0",
              "level_9": " 0",
              "name": "enterpriseFlashControllerTemperature",
              "recent": "72 C"
            },
            {
              "level_0": " 0",
              "level_1": " 428",
              "level_2": " 318053",
              "level_3": " 4069249",
              "level_4": " 17460810",
              "level_5": " 973002",
              "level_6": " 1977",
              "level_7": " 3919",
              "level_8": " 145",
              "level_9": " 0",
              "name": "capacitor1And2Temperature",
              "recent": "36.79 C"
            },
            {
              "level_0": " 0",
              "level_1": " 582",
              "level_2": " 4137227",
              "level_3": " 15410736",
              "level_4": " 3267522",
              "level_5": " 6589",
              "level_6": " 1051",
              "level_7": " 3876",
              "level_8": " 0",
              "level_9": " 0",
              "name": "capacitor3And4Temperature",
              "recent": "33.22 C"
            },
            {
              "errorPeriod": [
                {
                  "duration": "18",
                  "startTime": "2015-08-05 21:08:44",
                  "worst": "8"
                },
                {
                  "duration": "60",
                  "startTime": "2015-08-05 21:09:08",
                  "worst": "8"
                },
                {
                  "duration": "1238",
                  "startTime": "2015-08-05 21:10:21",
                  "worst": "8"
                },
                {
                  "duration": "48",
                  "startTime": "2015-08-05 21:31:29",
                  "worst": "8"
                }
              ],
              "level_0": " 0",
              "level_1": " 517",
              "level_2": " 23121",
              "level_3": " 949227",
              "level_4": " 3418492",
              "level_5": " 111906",
              "level_6": " 16026790",
              "level_7": " 2297078",
              "level_8": " 452",
              "level_9": " 0",
              "name": "rearVentAmbientTemperature",
              "recent": "52.56 C"
            },
            {
              "level_0": " 0",
              "level_1": " 4260284",
              "level_2": " 16817032",
              "level_3": " 1750179",
              "level_4": " 88",
              "level_5": " 0",
              "level_6": " 0",
              "level_7": " 0",
              "level_8": " 0",
              "level_9": " 0",
              "name": "rms200BoardTemperature",
              "recent": "57.88 C"
            },
            {
              "name": "voltageOfCapacitor1",
              "recent": "2.256 V"
            },
            {
              "name": "voltageOfCapacitor2",
              "recent": "2.265 V"
            },
            {
              "name": "voltageOfCapacitor3",
              "recent": "2.228 V"
            },
            {
              "name": "voltageOfCapacitor4",
              "recent": "2.209 V"
            },
            {
              "level_0": " 4650290",
              "level_1": " 16740451",
              "level_2": " 1048777",
              "level_3": " 123763",
              "level_4": " 93659",
              "level_5": " 80709",
              "level_6": " 62446",
              "level_7": " 27488",
              "level_8": " 0",
              "level_9": " 0",
              "name": "capacitorPackVoltage",
              "recent": "8.958 V"
            },
            {
              "level_0": " 0",
              "level_1": " 0",
              "level_2": " 0",
              "level_3": " 19",
              "level_4": " 38",
              "level_5": " 18",
              "level_6": " 0",
              "level_7": " 0",
              "level_8": " 2",
              "level_9": " 66",
              "name": "capacitorPackVoltageAtEndOfFlushToFlash",
              "recent": "4.470 V"
            },
            {
              "name": "currentDerivedFromV3V4",
              "recent": "0.002 A"
            },
            {
              "level_0": " 8",
              "level_1": " 6",
              "level_2": " 4",
              "level_3": " 106",
              "level_4": " 17",
              "level_5": " 2",
              "level_6": " 0",
              "level_7": " 0",
              "level_8": " 0",
              "level_9": " 0",
              "name": "derivedEnergy",
              "recent": "190 Joules"
            },
            {
              "level_0": " 0",
              "level_1": " 0",
              "level_2": " 0",
              "level_3": " 0",
              "level_4": " 0",
              "level_5": " 0",
              "level_6": " 0",
              "level_7": " 0",
              "level_8": " 18",
              "level_9": " 230",
              "name": "derivedCapacitanceOfThePack",
              "recent": "7.322 F"
            },
            {
              "level_0": " 0",
              "level_1": " 248",
              "level_2": " 0",
              "level_3": " 0",
              "level_4": " 0",
              "level_5": " 0",
              "level_6": " 0",
              "level_7": " 0",
              "level_8": " 0",
              "level_9": " 0",
              "name": "derivedEsrOfCapacitorPack",
              "recent": "0.096 Ohm"
            },
            {
              "level_0": " 0",
              "level_1": " 0",
              "level_2": " 0",
              "level_3": " 0",
              "level_4": " 124",
              "level_5": " 19",
              "level_6": " 0",
              "level_7": " 0",
              "level_8": " 0",
              "level_9": " 0",
              "name": "timeToRunFlushToFlash",
              "recent": "22.39 Seconds"
            },
            {
              "level_0": " 0",
              "level_1": " 0",
              "level_2": " 77",
              "level_3": " 0",
              "level_4": " 0",
              "level_5": " 0",
              "level_6": " 0",
              "level_7": " 0",
              "level_8": " 0",
              "level_9": " 0",
              "name": "timeToRunRestore",
              "recent": "20.49 Seconds"
            },
            {
              "level_0": " 0",
              "level_1": " 54",
              "level_2": " 17",
              "level_3": " 6",
              "level_4": " 0",
              "level_5": " 0",
              "level_6": " 0",
              "level_7": " 0",
              "level_8": " 0",
              "level_9": " 1",
              "name": "timeToChargeCapacitors",
              "recent": "42 Seconds"
            },
            {
              "level_0": " 4945370",
              "level_1": " 22054",
              "level_2": " 0",
              "level_3": " 0",
              "level_4": " 0",
              "level_5": " 0",
              "level_6": " 0",
              "level_7": " 0",
              "level_8": " 0",
              "level_9": " 0",
              "name": "correctableBitsInErrorOnReadingAPage"
            },
            {
              "level_0": " 22054",
              "level_1": " 0",
              "level_2": " 0",
              "level_3": " 0",
              "level_4": " 0",
              "level_5": " 0",
              "level_6": " 0",
              "level_7": " 0",
              "level_8": " 0",
              "level_9": " 0",
              "name": "correctableBitsInErrorOnReadingTheWorstBchRegionOfAPage"
            },
            {
              "errorPeriod": [
                {
                  "duration": "9",
                  "startTime": "2015-11-26 16:29:51",
                  "worst": "8"
                },
                {
                  "duration": "6",
                  "startTime": "2015-11-26 16:30:06",
                  "worst": "8"
                },
                {
                  "duration": "15",
                  "startTime": "2015-11-26 16:30:36",
                  "worst": "8"
                }
              ],
              "level_0": " 0",
              "level_1": " 3924463",
              "level_2": " 337357",
              "level_3": " 5942",
              "level_4": " 451546",
              "level_5": " 17237871",
              "level_6": " 865372",
              "level_7": " 5022",
              "level_8": " 10",
              "level_9": " 0",
              "name": "fanInletAmbientTemperature",
              "recent": "46.33 C"
            }
          ],
          "smartCounters": [
            {
              "name": "numberOf512ByteBlocksReadFromDdr",
              "value": "141895819"
            },
            {
              "name": "numberOf512ByteBlocksWrittenToDdr",
              "value": "89867121104"
            },
            {
              "name": "numberOfHostReadCommands",
              "value": "9326735"
            },
            {
              "name": "numberOfHostWriteCommands",
              "value": "12090520050"
            },
            {
              "name": "controllerBusyTimeMinutes",
              "value": "37318"
            },
            {
              "name": "numberOfPowerCycles",
              "value": "133"
            },
            {
              "name": "powerOnHours",
              "value": "18611"
            },
            {
              "name": "unsafeShutdowns",
              "value": "56"
            },
            {
              "name": "mediaErrors",
              "value": "0"
            },
            {
              "name": "numberOfErrorLogs",
              "value": "13"
            }
          ],
          "snapshotTime": "2016-10-13 16:37:39"
        },
        "firmware": {
          "activeSlotNumber": "2",
          "slot1Version": "1e5817bc",
          "slot2Version": "5fb7565c",
          "slot3Version": "1e5817bc",
          "slot4Version": "1e5817bc"
        },
        "identify": {
          "firmwareVersion": "5fb7565c on slot 2",
          "hardwareRevision": "B04",
          "modelNumber": "RMS-200",
          "serialNumber": "0000866"
        },
        "smart": {
          "availableSpace": "0%",
          "availableSpaceThreshold": "0%",
          "controllerBusyTimeMinutes": "37318",
          "criticalErrorVector": "0x0",
          "mediaErrors": "0",
          "numberOf512ByteBlocksRead": "141895819",
          "numberOf512ByteBlocksWritten": "89867121104",
          "numberOfErrorInfoLogs": "13",
          "numberOfHostReadCommands": "9326735",
          "numberOfHostWriteCommands": "12090520050",
          "numberOfPowerCycles": "133",
          "powerOnHours": "18611",
          "temperature": "330 Kelvin",
          "unsafeShutdowns": "56"
        }
      },
      "origin": null,
      "platform": {
        "chassisType": "R620",
        "cpuModel": "Intel(R) Xeon(R) CPU E5-2640 0 @ 2.50GHz",
        "nodeMemoryGB": 72,
        "nodeType": "SF3010"
      },
      "serial": "4QSR3T1",
      "storage": {
        "storage_PCI:0000:00:1f.2": {
          "businfo": "pci@0000:00:1f.2",
          "clock": "66000000",
          "description": "SATA controller",
          "physid": "1f.2",
          "product": "C600/X79 series chipset 6-Port SATA AHCI Controller",
          "vendor": "Intel Corporation",
          "version": "05",
          "width": "32"
        },
        "storage_PCI:0000:04:00.0": {
          "businfo": "pci@0000:04:00.0",
          "clock": "33000000",
          "description": "Non-Volatile memory controller",
          "physid": "0",
          "version": "03",
          "width": "64"
        },
        "storage_PCI:0000:41:00.0": {
          "businfo": "pci@0000:41:00.0",
          "clock": "33000000",
          "description": "Serial Attached SCSI controller",
          "physid": "0",
          "product": "SAS2008 PCI-Express Fusion-MPT SAS-2 [Falcon]",
          "vendor": "LSI Logic / Symbios Logic",
          "version": "03",
          "width": "64"
        }
      },
      "system": {
        "bdr-en92_DMI:0100": {
          "description": "Rack Mount Chassis",
          "product": "SFx010 ()",
          "serial": "4QSR3T1",
          "vendor": "SolidFire",
          "width": "64"
        }
      },
      "systemMemory": {
        "free": 47105552384,
        "total": 75566792704,
        "used": 28461240320
      },
      "uuid": "4C4C4544-0051-5310-8052-B4C04F335431"
    }
  }
}"""

RESP_GetNvramInfo_v9_0 = """{
  "id": null,
  "result": {
    "nvramInfo": {
      "details": {
        "errors": {
          "numOfErrorLogEntries": "0"
        },
        "extended": {
          "dialogVersion": "4",
          "event": [
            {
              "name": "flushToFlash",
              "time": "2016-07-28 17:43:56",
              "value": "0"
            },
            {
              "name": "flushToFlash",
              "time": "2016-07-28 17:59:28",
              "value": "0"
            },
            {
              "name": "flushToFlash",
              "time": "1948-07-10 14:45:43",
              "value": "0"
            },
            {
              "name": "flushToFlash",
              "time": "2016-07-28 18:37:02",
              "value": "0"
            },
            {
              "name": "flushToFlash",
              "time": "1948-07-10 15:23:17",
              "value": "0"
            },
            {
              "name": "flushToFlash",
              "time": "2016-07-28 20:28:01",
              "value": "0"
            },
            {
              "name": "flushToFlash",
              "time": "2016-08-10 20:11:31",
              "value": "0"
            },
            {
              "name": "flushToFlash",
              "time": "2016-08-10 20:31:47",
              "value": "0"
            },
            {
              "name": "excessiveCurrent",
              "time": "2014-07-31 21:12:08",
              "value": "244"
            }
          ],
          "eventOccurrences": [
            {
              "count": "143",
              "name": "flushToFlash"
            },
            {
              "count": "1",
              "name": "excessiveCurrent"
            }
          ],
          "initialCapacitance": "7.126 F",
          "initialEsr": "0.097 Ohm",
          "measurement": [
            {
              "level_0": " 0",
              "level_1": " 387",
              "level_2": " 4235656",
              "level_3": " 156318",
              "level_4": " 18423212",
              "level_5": " 11903",
              "level_6": " 0",
              "level_7": " 0",
              "level_8": " 0",
              "level_9": " 0",
              "name": "enterpriseFlashControllerTemperature",
              "recent": "72 C"
            },
            {
              "level_0": " 0",
              "level_1": " 428",
              "level_2": " 318053",
              "level_3": " 4069249",
              "level_4": " 17460703",
              "level_5": " 973002",
              "level_6": " 1977",
              "level_7": " 3919",
              "level_8": " 145",
              "level_9": " 0",
              "name": "capacitor1And2Temperature",
              "recent": "36.67 C"
            },
            {
              "level_0": " 0",
              "level_1": " 582",
              "level_2": " 4137227",
              "level_3": " 15410629",
              "level_4": " 3267522",
              "level_5": " 6589",
              "level_6": " 1051",
              "level_7": " 3876",
              "level_8": " 0",
              "level_9": " 0",
              "name": "capacitor3And4Temperature",
              "recent": "33.15 C"
            },
            {
              "errorPeriod": [
                {
                  "duration": "18",
                  "startTime": "2015-08-05 21:08:44",
                  "worst": "8"
                },
                {
                  "duration": "60",
                  "startTime": "2015-08-05 21:09:08",
                  "worst": "8"
                },
                {
                  "duration": "1238",
                  "startTime": "2015-08-05 21:10:21",
                  "worst": "8"
                },
                {
                  "duration": "48",
                  "startTime": "2015-08-05 21:31:29",
                  "worst": "8"
                }
              ],
              "level_0": " 0",
              "level_1": " 517",
              "level_2": " 23121",
              "level_3": " 949227",
              "level_4": " 3418492",
              "level_5": " 111906",
              "level_6": " 16026683",
              "level_7": " 2297078",
              "level_8": " 452",
              "level_9": " 0",
              "name": "rearVentAmbientTemperature",
              "recent": "52.71 C"
            },
            {
              "level_0": " 0",
              "level_1": " 4260284",
              "level_2": " 16816925",
              "level_3": " 1750179",
              "level_4": " 88",
              "level_5": " 0",
              "level_6": " 0",
              "level_7": " 0",
              "level_8": " 0",
              "level_9": " 0",
              "name": "rms200BoardTemperature",
              "recent": "57.75 C"
            },
            {
              "name": "voltageOfCapacitor1",
              "recent": "2.254 V"
            },
            {
              "name": "voltageOfCapacitor2",
              "recent": "2.262 V"
            },
            {
              "name": "voltageOfCapacitor3",
              "recent": "2.226 V"
            },
            {
              "name": "voltageOfCapacitor4",
              "recent": "2.207 V"
            },
            {
              "level_0": " 4650290",
              "level_1": " 16740344",
              "level_2": " 1048777",
              "level_3": " 123763",
              "level_4": " 93659",
              "level_5": " 80709",
              "level_6": " 62446",
              "level_7": " 27488",
              "level_8": " 0",
              "level_9": " 0",
              "name": "capacitorPackVoltage",
              "recent": "8.949 V"
            },
            {
              "level_0": " 0",
              "level_1": " 0",
              "level_2": " 0",
              "level_3": " 19",
              "level_4": " 38",
              "level_5": " 18",
              "level_6": " 0",
              "level_7": " 0",
              "level_8": " 2",
              "level_9": " 66",
              "name": "capacitorPackVoltageAtEndOfFlushToFlash",
              "recent": "4.470 V"
            },
            {
              "name": "currentDerivedFromV3V4",
              "recent": "0.002 A"
            },
            {
              "level_0": " 8",
              "level_1": " 6",
              "level_2": " 4",
              "level_3": " 106",
              "level_4": " 17",
              "level_5": " 2",
              "level_6": " 0",
              "level_7": " 0",
              "level_8": " 0",
              "level_9": " 0",
              "name": "derivedEnergy",
              "recent": "190 Joules"
            },
            {
              "level_0": " 0",
              "level_1": " 0",
              "level_2": " 0",
              "level_3": " 0",
              "level_4": " 0",
              "level_5": " 0",
              "level_6": " 0",
              "level_7": " 0",
              "level_8": " 18",
              "level_9": " 230",
              "name": "derivedCapacitanceOfThePack",
              "recent": "7.322 F"
            },
            {
              "level_0": " 0",
              "level_1": " 248",
              "level_2": " 0",
              "level_3": " 0",
              "level_4": " 0",
              "level_5": " 0",
              "level_6": " 0",
              "level_7": " 0",
              "level_8": " 0",
              "level_9": " 0",
              "name": "derivedEsrOfCapacitorPack",
              "recent": "0.096 Ohm"
            },
            {
              "level_0": " 0",
              "level_1": " 0",
              "level_2": " 0",
              "level_3": " 0",
              "level_4": " 124",
              "level_5": " 19",
              "level_6": " 0",
              "level_7": " 0",
              "level_8": " 0",
              "level_9": " 0",
              "name": "timeToRunFlushToFlash",
              "recent": "22.39 Seconds"
            },
            {
              "level_0": " 0",
              "level_1": " 0",
              "level_2": " 77",
              "level_3": " 0",
              "level_4": " 0",
              "level_5": " 0",
              "level_6": " 0",
              "level_7": " 0",
              "level_8": " 0",
              "level_9": " 0",
              "name": "timeToRunRestore",
              "recent": "20.49 Seconds"
            },
            {
              "level_0": " 0",
              "level_1": " 54",
              "level_2": " 17",
              "level_3": " 6",
              "level_4": " 0",
              "level_5": " 0",
              "level_6": " 0",
              "level_7": " 0",
              "level_8": " 0",
              "level_9": " 1",
              "name": "timeToChargeCapacitors",
              "recent": "42 Seconds"
            },
            {
              "level_0": " 4945370",
              "level_1": " 22054",
              "level_2": " 0",
              "level_3": " 0",
              "level_4": " 0",
              "level_5": " 0",
              "level_6": " 0",
              "level_7": " 0",
              "level_8": " 0",
              "level_9": " 0",
              "name": "correctableBitsInErrorOnReadingAPage"
            },
            {
              "level_0": " 22054",
              "level_1": " 0",
              "level_2": " 0",
              "level_3": " 0",
              "level_4": " 0",
              "level_5": " 0",
              "level_6": " 0",
              "level_7": " 0",
              "level_8": " 0",
              "level_9": " 0",
              "name": "correctableBitsInErrorOnReadingTheWorstBchRegionOfAPage"
            },
            {
              "errorPeriod": [
                {
                  "duration": "9",
                  "startTime": "2015-11-26 16:29:51",
                  "worst": "8"
                },
                {
                  "duration": "6",
                  "startTime": "2015-11-26 16:30:06",
                  "worst": "8"
                },
                {
                  "duration": "15",
                  "startTime": "2015-11-26 16:30:36",
                  "worst": "8"
                }
              ],
              "level_0": " 0",
              "level_1": " 3924463",
              "level_2": " 337357",
              "level_3": " 5942",
              "level_4": " 451546",
              "level_5": " 17237764",
              "level_6": " 865372",
              "level_7": " 5022",
              "level_8": " 10",
              "level_9": " 0",
              "name": "fanInletAmbientTemperature",
              "recent": "46.47 C"
            }
          ],
          "smartCounters": [
            {
              "name": "numberOf512ByteBlocksReadFromDdr",
              "value": "141895819"
            },
            {
              "name": "numberOf512ByteBlocksWrittenToDdr",
              "value": "89867121104"
            },
            {
              "name": "numberOfHostReadCommands",
              "value": "9326735"
            },
            {
              "name": "numberOfHostWriteCommands",
              "value": "12090520050"
            },
            {
              "name": "controllerBusyTimeMinutes",
              "value": "37318"
            },
            {
              "name": "numberOfPowerCycles",
              "value": "133"
            },
            {
              "name": "powerOnHours",
              "value": "18611"
            },
            {
              "name": "unsafeShutdowns",
              "value": "56"
            },
            {
              "name": "mediaErrors",
              "value": "0"
            },
            {
              "name": "numberOfErrorLogs",
              "value": "13"
            }
          ],
          "snapshotTime": "2016-10-13 16:32:13"
        },
        "firmware": {
          "activeSlotNumber": "2",
          "slot1Version": "1e5817bc",
          "slot2Version": "5fb7565c",
          "slot3Version": "1e5817bc",
          "slot4Version": "1e5817bc"
        },
        "identify": {
          "firmwareVersion": "5fb7565c on slot 2",
          "hardwareRevision": "B04",
          "modelNumber": "RMS-200",
          "serialNumber": "0000866"
        },
        "smart": {
          "availableSpace": "0%",
          "availableSpaceThreshold": "0%",
          "controllerBusyTimeMinutes": "37318",
          "criticalErrorVector": "0x0",
          "mediaErrors": "0",
          "numberOf512ByteBlocksRead": "141895819",
          "numberOf512ByteBlocksWritten": "89867121104",
          "numberOfErrorInfoLogs": "13",
          "numberOfHostReadCommands": "9326735",
          "numberOfHostWriteCommands": "12090520050",
          "numberOfPowerCycles": "133",
          "powerOnHours": "18611",
          "temperature": "330 Kelvin",
          "unsafeShutdowns": "56"
        }
      },
      "status": "Warning",
      "statusInfo": {
        "warning": [
          "excessiveCurrent (1x)"
        ]
      },
      "type": "RMS-200"
    }
  }
}"""

RESP_GetOrigin_v9_0 = """{
  "id": null,
  "result": {
    "nodes": [
      {
        "nodeID": 1,
        "result": {
          "origin": {
            "<signature>": {
              "data": "eiPNNA3TpfgO0bl+SnhjaO1ZEKJUPZJDG1PFZrbOmUu5JXfQ012Aq0RzhMSKIb8MVTgesZ/+urfzuVD9Zf1JKwnfv7h3UZLMzE7eC6rJnLNi+AgHEYvqBLLKMJ39HNj+xEOogpQmBIn5jKv7U05pk4tsQwbxv4HtoQNMEl+PdQuVdDGLD9ipU3jgAw5sHFFZ+hLq8Uk3fzUiiR7LcW2b9aAw4KEQdSj/OhCNB4/7IcKOq8YBpP3ONWb+N6jrqSfMtnD4sa7vzSX7vI0z++zBeUd6E0hJz7atonS6oAqtyT4F48giO6hBSfkqt0KLvvC1Mcgh0LQrQG+XZnQ5KWBIuQ==",
              "pubkey": "MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAxmKgEBzyZv2jFZpucao7HT9lYuR3g/18thP/7arwflrtDauIaPaIbnsuDVWgbPKHsqBkth9XCnDF16yBOFYoJLZ+vW0kNS7Z/CiCiLlmAXIa4voeEqLsQ55IbAhjMXfrGauyUHZYunMBhUG3xDJxdrs4Rgp24VqB/oBxihleyotIX+dLpv7nd7qbVA3juLMAy7cfgxUX7mAEmPAcx3gNiNw7SBBZaeFVrNSiXv3+Zrw5wLkLH1QDWwuBRK+3yGTkzVwD5QgLw0qkRMkFobBhk96Z7CQbf4B/8zi3bhvowoyaK+4Cv/jmEjs2TS0QFW0PQHKIjyC3ckkcLaZZ2DQcLQIDAQAB",
              "version": 1
            },
            "contract-date": "10/1/2015",
            "contract-name": "00002265",
            "contract-quantity": 0,
            "contract-type": "Master",
            "integrator": "StackVelocity",
            "location": "Memphis, Tennessee",
            "organization": "none",
            "type": "appliance"
          }
        }
      },
      {
        "nodeID": 2,
        "result": {
          "origin": {
            "<signature>": {
              "data": "eiPNNA3TpfgO0bl+SnhjaO1ZEKJUPZJDG1PFZrbOmUu5JXfQ012Aq0RzhMSKIb8MVTgesZ/+urfzuVD9Zf1JKwnfv7h3UZLMzE7eC6rJnLNi+AgHEYvqBLLKMJ39HNj+xEOogpQmBIn5jKv7U05pk4tsQwbxv4HtoQNMEl+PdQuVdDGLD9ipU3jgAw5sHFFZ+hLq8Uk3fzUiiR7LcW2b9aAw4KEQdSj/OhCNB4/7IcKOq8YBpP3ONWb+N6jrqSfMtnD4sa7vzSX7vI0z++zBeUd6E0hJz7atonS6oAqtyT4F48giO6hBSfkqt0KLvvC1Mcgh0LQrQG+XZnQ5KWBIuQ==",
              "pubkey": "MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAxmKgEBzyZv2jFZpucao7HT9lYuR3g/18thP/7arwflrtDauIaPaIbnsuDVWgbPKHsqBkth9XCnDF16yBOFYoJLZ+vW0kNS7Z/CiCiLlmAXIa4voeEqLsQ55IbAhjMXfrGauyUHZYunMBhUG3xDJxdrs4Rgp24VqB/oBxihleyotIX+dLpv7nd7qbVA3juLMAy7cfgxUX7mAEmPAcx3gNiNw7SBBZaeFVrNSiXv3+Zrw5wLkLH1QDWwuBRK+3yGTkzVwD5QgLw0qkRMkFobBhk96Z7CQbf4B/8zi3bhvowoyaK+4Cv/jmEjs2TS0QFW0PQHKIjyC3ckkcLaZZ2DQcLQIDAQAB",
              "version": 1
            },
            "contract-date": "10/1/2015",
            "contract-name": "00002265",
            "contract-quantity": 0,
            "contract-type": "Master",
            "integrator": "StackVelocity",
            "location": "Memphis, Tennessee",
            "organization": "none",
            "type": "appliance"
          }
        }
      },
      {
        "nodeID": 3,
        "result": {
          "origin": {
            "<signature>": {
              "data": "eiPNNA3TpfgO0bl+SnhjaO1ZEKJUPZJDG1PFZrbOmUu5JXfQ012Aq0RzhMSKIb8MVTgesZ/+urfzuVD9Zf1JKwnfv7h3UZLMzE7eC6rJnLNi+AgHEYvqBLLKMJ39HNj+xEOogpQmBIn5jKv7U05pk4tsQwbxv4HtoQNMEl+PdQuVdDGLD9ipU3jgAw5sHFFZ+hLq8Uk3fzUiiR7LcW2b9aAw4KEQdSj/OhCNB4/7IcKOq8YBpP3ONWb+N6jrqSfMtnD4sa7vzSX7vI0z++zBeUd6E0hJz7atonS6oAqtyT4F48giO6hBSfkqt0KLvvC1Mcgh0LQrQG+XZnQ5KWBIuQ==",
              "pubkey": "MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAxmKgEBzyZv2jFZpucao7HT9lYuR3g/18thP/7arwflrtDauIaPaIbnsuDVWgbPKHsqBkth9XCnDF16yBOFYoJLZ+vW0kNS7Z/CiCiLlmAXIa4voeEqLsQ55IbAhjMXfrGauyUHZYunMBhUG3xDJxdrs4Rgp24VqB/oBxihleyotIX+dLpv7nd7qbVA3juLMAy7cfgxUX7mAEmPAcx3gNiNw7SBBZaeFVrNSiXv3+Zrw5wLkLH1QDWwuBRK+3yGTkzVwD5QgLw0qkRMkFobBhk96Z7CQbf4B/8zi3bhvowoyaK+4Cv/jmEjs2TS0QFW0PQHKIjyC3ckkcLaZZ2DQcLQIDAQAB",
              "version": 1
            },
            "contract-date": "10/1/2015",
            "contract-name": "00002265",
            "contract-quantity": 0,
            "contract-type": "Master",
            "integrator": "StackVelocity",
            "location": "Memphis, Tennessee",
            "organization": "none",
            "type": "appliance"
          }
        }
      },
      {
        "nodeID": 4,
        "result": {
          "origin": null
        }
      }
    ]
  }
}"""

RESP_GetStorageContainerEfficiency_v9_0 = """{
  "id": null,
  "result": {
    "compression": 1,
    "deduplication": 1,
    "missingVolumes": [],
    "thinProvisioning": 1,
    "timestamp": "2016-10-14T22:41:24Z"
  }
}"""

RESP_GetVirtualVolumeCount_v9_0 = """{
  "id": null,
  "result": {
    "count": 0
  }
}"""

RESP_GetVolumeCount_v9_0 = """{
  "id": null,
  "result": {
    "count": 736
  }
}"""

RESP_ListAllNodes_v8_0 = """{
   "id":749,
   "result":{
      "nodes":[
         {
            "associatedFServiceID":0,
            "associatedMasterServiceID":1,
            "attributes":{

            },
            "cip":"10.117.62.22",
            "cipi":"Bond10G",
            "fibreChannelTargetPortGroup":null,
            "mip":"10.117.60.22",
            "mipi":"Bond1G",
            "name":"node4",
            "nodeID":1,
            "platformInfo":{
               "chassisType":"R620",
               "cpuModel":"Intel(R) Xeon(R) CPU E5-2640 0 @ 2.50GHz",
               "nodeMemoryGB":72,
               "nodeType":"SF3010"
            },
            "sip":"10.117.62.22",
            "sipi":"Bond10G",
            "softwareVersion":"8.7.0.15",
            "uuid":"4C4C4544-0032-3810-8036-B3C04F585631",
            "virtualNetworks":[
               {
                  "address":"10.117.41.130",
                  "virtualNetworkID":16
               }
            ]
         }
      ],
      "pendingNodes":[

      ]
   }
}"""

RESP_ListAsyncResults_v9_0 = """{
  "id": 1,
  "result": {
    "asyncHandles": [
      {
        "asyncResultID": 1,
        "completed": true,
        "createTime": "2016-10-27T16:09:29Z",
        "data": {
          "abortedDrives": [],
          "addedDrives": [
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20,
            21,
            22
          ],
          "pendingDrives": []
        },
        "lastUpdateTime": "2016-10-27T16:09:49Z",
        "resultType": "DriveAdd",
        "success": true
      }
    ]
  }
}"""

RESP_ListDriveStats_v9_0 = """{
  "id": 1,
  "result": {
    "driveStats": [
      {
        "driveID": 22,
        "failedDieCount": 0,
        "lifeRemainingPercent": 84,
        "lifetimeReadBytes": 30171004403712,
        "lifetimeWriteBytes": 103464755527680,
        "powerOnHours": 17736,
        "readBytes": 14656542,
         "readOps": 3624,
        "reallocatedSectors": 0,
        "reserveCapacityPercent": 100,
        "timestamp": "2016-03-01T00:19:24.782735Z",
        "totalCapacity": 300069052416,
        "usedCapacity": 1783735635,
        "usedMemory": 879165440,
        "writeBytes": 2462169894,
        "writeOps": 608802
      }
    ],
    "errors": [
      {
        "driveID": 23,
        "exception": {
          "message": "xStatCheckpointDoesNotExist",
          "name": "xStatCheckpointDoesNotExist"
        }
      }
    ]
  }
}"""

RESP_ListFibreChannelSessions_v9_0 = """{
  "id" : 1,
  "result" : {
     "sessions" : [
    {
       "initiatorWWPN" : "21:00:00:0e:1e:14:af:40",
       "nodeID" : 5,
       "serviceID" : 21,
       "targetWWPN": "5f:47:ac:c0:00:00:00:10",
       "volumeAccessGroupID": 7
    },
    {
       "initiatorWWPN" : "21:00:00:0e:1e:14:af:40",
       "nodeID" : 1,
       "serviceID" : 22,
       "targetWWPN": "5f:47:ac:c0:00:00:00:11",
       "volumeAccessGroupID": 7
    }
    ]
  }
}"""

RESP_ListISCSISessions_v9_0 = """{
  "id": 7,
  "result": {
    "sessions": [
      {
        "accountID": 1,
        "accountName": "myaccount",
        "createTime": "2016-08-12T16:40:04.827786Z",
        "driveID": 1,
        "initiator": {
          "alias": "",
          "attributes": {},
          "initiatorID": 2,
          "initiatorName": "iqn.2010-01.net.solidfire.eng:zdc-3",
          "volumeAccessGroups": [
            1
          ]
        },
        "initiatorIP": "10.30.76.3:33994",
        "initiatorName": "iqn.2010-01.net.solidfire.eng:zdc-3",
        "initiatorPortName": "iqn.2010-01.net.solidfire.eng:zdc-3,i,0x23d070000",
        "initiatorSessionID": 9613803520,
        "nodeID": 1,
        "serviceID": 4,
        "sessionID": 17179882017,
        "targetIP": "10.30.65.134:3260",
        "targetName": "iqn.2010-01.com.solidfire:dvmj.aawuanfmxukfnffl.3",
        "targetPortName": "iqn.2010-01.com.solidfire:dvmj.aawuanfmxukfnffl.3,t,0x1",
        "virtualNetworkID": 0,
        "volumeID": 3,
        "volumeInstance": 139922648856576
      },
      {
        "accountID": 1,
        "accountName": "myaccount",
        "createTime": "2016-08-12T16:40:04.827831Z",
        "driveID": 1,
        "initiator": {
          "alias": "",
          "attributes": {},
          "initiatorID": 2,
          "initiatorName": "iqn.2010-01.net.solidfire.eng:zdc-3",
          "volumeAccessGroups": [
            1
          ]
        },
        "initiatorIP": "10.30.76.3:33995",
        "initiatorName": "iqn.2010-01.net.solidfire.eng:zdc-3",
        "initiatorPortName": "iqn.2010-01.net.solidfire.eng:zdc-3,i,0x23d080000",
        "initiatorSessionID": 9613869056,
        "nodeID": 1,
        "serviceID": 4,
        "sessionID": 17179882018,
        "targetIP": "10.30.65.134:3260",
        "targetName": "iqn.2010-01.com.solidfire:dvmj.trruw982e4vr2cgf.9",
        "targetPortName": "iqn.2010-01.com.solidfire:dvmj.trruw982e4vr2cgf.9,t,0x1",
        "virtualNetworkID": 0,
        "volumeID": 9,
        "volumeInstance": 139922531221504
      }
    ]
  }
}"""

RESP_ListPendingActiveNodes_v9_0 = """{
  "id": null,
  "result": {
    "pendingActiveNodes": [
		{
		  "activeNodeKey": "5rPHP3lTAO",
		  "assignedNodeID": 5,
		  "asyncHandle": 2,
		  "cip": "10.10.5.106",
		  "mip": "192.168.133.106",
		  "pendingNodeID": 1,
		  "platformInfo": {
			"chassisType": "R620",
			"cpuModel": "Intel(R) Xeon(R) CPU E5-2640 0 @ 2.50GHz",
			"nodeMemoryGB": 72,
			"nodeType": "SF3010"
		  },
		 "sip": "10.10.5.106",
		 "softwareVersion": "9.0.0.1077"
		}
    ]
  }
}"""

RESP_ListProtocolEndpoints_v9_0 = """{
  "id": 1,
  "result": {
    "protocolEndpoints": [
      {
        "primaryProviderID": 1,
        "protocolEndpointID": "1387e257-d2e3-4446-be6d-39db71583e7b",
        "protocolEndpointState": "Active",
        "providerType": "Primary",
        "scsiNAADeviceID": "6f47acc2000000016970687200000000",
        "secondaryProviderID": 2
      },
      {
        "primaryProviderID": 2,
        "protocolEndpointID": "1f16ed86-3f31-4c76-b004-a1251187700b",
        "protocolEndpointState": "Active",
        "providerType": "Primary",
        "scsiNAADeviceID": "6f47acc2000000026970687200000000",
        "secondaryProviderID": 3
      },
      {
        "primaryProviderID": 4,
        "protocolEndpointID": "c6458dfe-9803-4350-bb4e-68a3feb7e830",
        "protocolEndpointState": "Active",
        "providerType": "Primary",
        "scsiNAADeviceID": "6f47acc2000000046970687200000000",
        "secondaryProviderID": 1
      },
      {
        "primaryProviderID": 3,
        "protocolEndpointID": "f3e7911d-0e86-4776-97db-7468c272213f",
        "protocolEndpointState": "Active",
        "providerType": "Primary",
        "scsiNAADeviceID": "6f47acc2000000036970687200000000",
        "secondaryProviderID": 4
      }
    ]
  }
}"""

RESP_ListServices_v9_0 = """{
  "id": null,
  "result": {
    "services": [
      {
        "drive": {
          "assignedService": 22,
          "asyncResultIDs": [],
          "attributes": {},
          "capacity": 300069052416,
          "customerSliceFileCapacity": 0,
          "driveID": 5,
          "driveStatus": "assigned",
          "driveType": "block",
          "nodeID": 4,
          "reservedSliceFileCapacity": 0,
          "serial": "scsi-SATA_INTEL_SSDSA2CW3CVPR132402D3300EGN",
          "slot": 3
        },
        "drives": [
          {
            "assignedService": 22,
            "asyncResultIDs": [],
            "attributes": {},
            "capacity": 300069052416,
            "customerSliceFileCapacity": 0,
            "driveID": 5,
            "driveStatus": "assigned",
            "driveType": "Block",
            "nodeID": 4,
            "reservedSliceFileCapacity": 0,
            "serial": "scsi-SATA_INTEL_SSDSA2CW3CVPR132402D3300EGN",
            "slot": 3
          }
        ],
        "node": {
          "associatedFServiceID": 0,
          "associatedMasterServiceID": 3,
          "attributes": {},
          "cip": "10.117.62.26",
          "cipi": "Bond10G",
          "fibreChannelTargetPortGroup": null,
          "mip": "10.117.60.26",
          "mipi": "Bond1G",
          "name": "SF-1713",
          "nodeID": 4,
          "platformInfo": {
            "chassisType": "R620",
            "cpuModel": "Intel(R) Xeon(R) CPU E5-2640 0 @ 2.50GHz",
            "nodeMemoryGB": 72,
            "nodeType": "SF3010"
          },
          "sip": "10.117.62.26",
          "sipi": "Bond10G",
          "softwareVersion": "9.0.0.1554",
          "uuid": "4C4C4544-0053-3210-8054-B6C04F435831",
          "virtualNetworks": []
        },
        "service": {
          "associatedBV": 0,
          "associatedTS": 0,
          "associatedVS": 0,
          "asyncResultIDs": [],
          "driveID": 5,
          "driveIDs": [
            5
          ],
          "firstTimeStartup": false,
          "ipcPort": 4008,
          "iscsiPort": 0,
          "nodeID": 4,
          "serviceID": 22,
          "serviceType": "block",
          "startedDriveIDs": [
            5
          ],
          "status": "healthy"
        }
      },
      {
        "drive": {
          "assignedService": 23,
          "asyncResultIDs": [],
          "attributes": {},
          "capacity": 300069052416,
          "customerSliceFileCapacity": 0,
          "driveID": 17,
          "driveStatus": "assigned",
          "driveType": "block",
          "nodeID": 3,
          "reservedSliceFileCapacity": 0,
          "serial": "scsi-SATA_INTEL_SSDSC2BB3BTWL311300X7300PGN",
          "slot": 4
        },
        "drives": [
          {
            "assignedService": 23,
            "asyncResultIDs": [],
            "attributes": {},
            "capacity": 300069052416,
            "customerSliceFileCapacity": 0,
            "driveID": 17,
            "driveStatus": "assigned",
            "driveType": "Block",
            "nodeID": 3,
            "reservedSliceFileCapacity": 0,
            "serial": "scsi-SATA_INTEL_SSDSC2BB3BTWL311300X7300PGN",
            "slot": 4
          }
        ],
        "node": {
          "associatedFServiceID": 0,
          "associatedMasterServiceID": 4,
          "attributes": {},
          "cip": "10.117.62.25",
          "cipi": "Bond10G",
          "fibreChannelTargetPortGroup": null,
          "mip": "10.117.60.25",
          "mipi": "Bond1G",
          "name": "SF-F2A3",
          "nodeID": 3,
          "platformInfo": {
            "chassisType": "R620",
            "cpuModel": "Intel(R) Xeon(R) CPU E5-2640 0 @ 2.50GHz",
            "nodeMemoryGB": 72,
            "nodeType": "SF3010"
          },
          "sip": "10.117.62.25",
          "sipi": "Bond10G",
          "softwareVersion": "9.0.0.1554",
          "uuid": "4C4C4544-0053-3310-8053-B6C04F435831",
          "virtualNetworks": []
        },
        "service": {
          "associatedBV": 0,
          "associatedTS": 0,
          "associatedVS": 0,
          "asyncResultIDs": [],
          "driveID": 17,
          "driveIDs": [
            17
          ],
          "firstTimeStartup": false,
          "ipcPort": 4009,
          "iscsiPort": 0,
          "nodeID": 3,
          "serviceID": 23,
          "serviceType": "block",
          "startedDriveIDs": [
            17
          ],
          "status": "healthy"
        }
      },
      {
        "drive": {
          "assignedService": 24,
          "asyncResultIDs": [],
          "attributes": {},
          "capacity": 300069052416,
          "customerSliceFileCapacity": 0,
          "driveID": 6,
          "driveStatus": "assigned",
          "driveType": "block",
          "nodeID": 4,
          "reservedSliceFileCapacity": 0,
          "serial": "scsi-SATA_INTEL_SSDSA2CW3BTPR227401VN300EGN",
          "slot": 4
        },
        "drives": [
          {
            "assignedService": 24,
            "asyncResultIDs": [],
            "attributes": {},
            "capacity": 300069052416,
            "customerSliceFileCapacity": 0,
            "driveID": 6,
            "driveStatus": "assigned",
            "driveType": "Block",
            "nodeID": 4,
            "reservedSliceFileCapacity": 0,
            "serial": "scsi-SATA_INTEL_SSDSA2CW3BTPR227401VN300EGN",
            "slot": 4
          }
        ],
        "node": {
          "associatedFServiceID": 0,
          "associatedMasterServiceID": 3,
          "attributes": {},
          "cip": "10.117.62.26",
          "cipi": "Bond10G",
          "fibreChannelTargetPortGroup": null,
          "mip": "10.117.60.26",
          "mipi": "Bond1G",
          "name": "SF-1713",
          "nodeID": 4,
          "platformInfo": {
            "chassisType": "R620",
            "cpuModel": "Intel(R) Xeon(R) CPU E5-2640 0 @ 2.50GHz",
            "nodeMemoryGB": 72,
            "nodeType": "SF3010"
          },
          "sip": "10.117.62.26",
          "sipi": "Bond10G",
          "softwareVersion": "9.0.0.1554",
          "uuid": "4C4C4544-0053-3210-8054-B6C04F435831",
          "virtualNetworks": []
        },
        "service": {
          "associatedBV": 0,
          "associatedTS": 0,
          "associatedVS": 0,
          "asyncResultIDs": [],
          "driveID": 6,
          "driveIDs": [
            6
          ],
          "firstTimeStartup": false,
          "ipcPort": 4009,
          "iscsiPort": 0,
          "nodeID": 4,
          "serviceID": 24,
          "serviceType": "block",
          "startedDriveIDs": [
            6
          ],
          "status": "healthy"
        }
      },
      {
        "drive": {
          "assignedService": 25,
          "asyncResultIDs": [],
          "attributes": {},
          "capacity": 300069052416,
          "customerSliceFileCapacity": 0,
          "driveID": 18,
          "driveStatus": "assigned",
          "driveType": "block",
          "nodeID": 3,
          "reservedSliceFileCapacity": 0,
          "serial": "scsi-SATA_INTEL_SSDSC2BB3BTWL31130138300PGN",
          "slot": 5
        },
        "drives": [
          {
            "assignedService": 25,
            "asyncResultIDs": [],
            "attributes": {},
            "capacity": 300069052416,
            "customerSliceFileCapacity": 0,
            "driveID": 18,
            "driveStatus": "assigned",
            "driveType": "Block",
            "nodeID": 3,
            "reservedSliceFileCapacity": 0,
            "serial": "scsi-SATA_INTEL_SSDSC2BB3BTWL31130138300PGN",
            "slot": 5
          }
        ],
        "node": {
          "associatedFServiceID": 0,
          "associatedMasterServiceID": 4,
          "attributes": {},
          "cip": "10.117.62.25",
          "cipi": "Bond10G",
          "fibreChannelTargetPortGroup": null,
          "mip": "10.117.60.25",
          "mipi": "Bond1G",
          "name": "SF-F2A3",
          "nodeID": 3,
          "platformInfo": {
            "chassisType": "R620",
            "cpuModel": "Intel(R) Xeon(R) CPU E5-2640 0 @ 2.50GHz",
            "nodeMemoryGB": 72,
            "nodeType": "SF3010"
          },
          "sip": "10.117.62.25",
          "sipi": "Bond10G",
          "softwareVersion": "9.0.0.1554",
          "uuid": "4C4C4544-0053-3310-8053-B6C04F435831",
          "virtualNetworks": []
        },
        "service": {
          "associatedBV": 0,
          "associatedTS": 0,
          "associatedVS": 0,
          "asyncResultIDs": [],
          "driveID": 18,
          "driveIDs": [
            18
          ],
          "firstTimeStartup": false,
          "ipcPort": 4010,
          "iscsiPort": 0,
          "nodeID": 3,
          "serviceID": 25,
          "serviceType": "block",
          "startedDriveIDs": [
            18
          ],
          "status": "healthy"
        }
      },
      {
        "drive": {
          "assignedService": 26,
          "asyncResultIDs": [],
          "attributes": {},
          "capacity": 300069052416,
          "customerSliceFileCapacity": 0,
          "driveID": 7,
          "driveStatus": "assigned",
          "driveType": "block",
          "nodeID": 4,
          "reservedSliceFileCapacity": 0,
          "serial": "scsi-SATA_INTEL_SSDSA2BW3CVPR120504CK300EGN",
          "slot": 5
        },
        "drives": [
          {
            "assignedService": 26,
            "asyncResultIDs": [],
            "attributes": {},
            "capacity": 300069052416,
            "customerSliceFileCapacity": 0,
            "driveID": 7,
            "driveStatus": "assigned",
            "driveType": "Block",
            "nodeID": 4,
            "reservedSliceFileCapacity": 0,
            "serial": "scsi-SATA_INTEL_SSDSA2BW3CVPR120504CK300EGN",
            "slot": 5
          }
        ],
        "node": {
          "associatedFServiceID": 0,
          "associatedMasterServiceID": 3,
          "attributes": {},
          "cip": "10.117.62.26",
          "cipi": "Bond10G",
          "fibreChannelTargetPortGroup": null,
          "mip": "10.117.60.26",
          "mipi": "Bond1G",
          "name": "SF-1713",
          "nodeID": 4,
          "platformInfo": {
            "chassisType": "R620",
            "cpuModel": "Intel(R) Xeon(R) CPU E5-2640 0 @ 2.50GHz",
            "nodeMemoryGB": 72,
            "nodeType": "SF3010"
          },
          "sip": "10.117.62.26",
          "sipi": "Bond10G",
          "softwareVersion": "9.0.0.1554",
          "uuid": "4C4C4544-0053-3210-8054-B6C04F435831",
          "virtualNetworks": []
        },
        "service": {
          "associatedBV": 0,
          "associatedTS": 0,
          "associatedVS": 0,
          "asyncResultIDs": [],
          "driveID": 7,
          "driveIDs": [
            7
          ],
          "firstTimeStartup": false,
          "ipcPort": 4010,
          "iscsiPort": 0,
          "nodeID": 4,
          "serviceID": 26,
          "serviceType": "block",
          "startedDriveIDs": [
            7
          ],
          "status": "healthy"
        }
      },
      {
        "drive": {
          "assignedService": 27,
          "asyncResultIDs": [],
          "attributes": {},
          "capacity": 300069052416,
          "customerSliceFileCapacity": 0,
          "driveID": 19,
          "driveStatus": "assigned",
          "driveType": "block",
          "nodeID": 3,
          "reservedSliceFileCapacity": 0,
          "serial": "scsi-SATA_INTEL_SSDSC2BB3BTWL307103KD300PGN",
          "slot": 6
        },
        "drives": [
          {
            "assignedService": 27,
            "asyncResultIDs": [],
            "attributes": {},
            "capacity": 300069052416,
            "customerSliceFileCapacity": 0,
            "driveID": 19,
            "driveStatus": "assigned",
            "driveType": "Block",
            "nodeID": 3,
            "reservedSliceFileCapacity": 0,
            "serial": "scsi-SATA_INTEL_SSDSC2BB3BTWL307103KD300PGN",
            "slot": 6
          }
        ],
        "node": {
          "associatedFServiceID": 0,
          "associatedMasterServiceID": 4,
          "attributes": {},
          "cip": "10.117.62.25",
          "cipi": "Bond10G",
          "fibreChannelTargetPortGroup": null,
          "mip": "10.117.60.25",
          "mipi": "Bond1G",
          "name": "SF-F2A3",
          "nodeID": 3,
          "platformInfo": {
            "chassisType": "R620",
            "cpuModel": "Intel(R) Xeon(R) CPU E5-2640 0 @ 2.50GHz",
            "nodeMemoryGB": 72,
            "nodeType": "SF3010"
          },
          "sip": "10.117.62.25",
          "sipi": "Bond10G",
          "softwareVersion": "9.0.0.1554",
          "uuid": "4C4C4544-0053-3310-8053-B6C04F435831",
          "virtualNetworks": []
        },
        "service": {
          "associatedBV": 0,
          "associatedTS": 0,
          "associatedVS": 0,
          "asyncResultIDs": [],
          "driveID": 19,
          "driveIDs": [
            19
          ],
          "firstTimeStartup": false,
          "ipcPort": 4011,
          "iscsiPort": 0,
          "nodeID": 3,
          "serviceID": 27,
          "serviceType": "block",
          "startedDriveIDs": [
            19
          ],
          "status": "healthy"
        }
      },
      {
        "drive": {
          "assignedService": 28,
          "asyncResultIDs": [],
          "attributes": {},
          "capacity": 300069052416,
          "customerSliceFileCapacity": 0,
          "driveID": 8,
          "driveStatus": "assigned",
          "driveType": "block",
          "nodeID": 4,
          "reservedSliceFileCapacity": 0,
          "serial": "scsi-SATA_INTEL_SSDSA2CW3BTPR227401S0300EGN",
          "slot": 6
        },
        "drives": [
          {
            "assignedService": 28,
            "asyncResultIDs": [],
            "attributes": {},
            "capacity": 300069052416,
            "customerSliceFileCapacity": 0,
            "driveID": 8,
            "driveStatus": "assigned",
            "driveType": "Block",
            "nodeID": 4,
            "reservedSliceFileCapacity": 0,
            "serial": "scsi-SATA_INTEL_SSDSA2CW3BTPR227401S0300EGN",
            "slot": 6
          }
        ],
        "node": {
          "associatedFServiceID": 0,
          "associatedMasterServiceID": 3,
          "attributes": {},
          "cip": "10.117.62.26",
          "cipi": "Bond10G",
          "fibreChannelTargetPortGroup": null,
          "mip": "10.117.60.26",
          "mipi": "Bond1G",
          "name": "SF-1713",
          "nodeID": 4,
          "platformInfo": {
            "chassisType": "R620",
            "cpuModel": "Intel(R) Xeon(R) CPU E5-2640 0 @ 2.50GHz",
            "nodeMemoryGB": 72,
            "nodeType": "SF3010"
          },
          "sip": "10.117.62.26",
          "sipi": "Bond10G",
          "softwareVersion": "9.0.0.1554",
          "uuid": "4C4C4544-0053-3210-8054-B6C04F435831",
          "virtualNetworks": []
        },
        "service": {
          "associatedBV": 0,
          "associatedTS": 0,
          "associatedVS": 0,
          "asyncResultIDs": [],
          "driveID": 8,
          "driveIDs": [
            8
          ],
          "firstTimeStartup": false,
          "ipcPort": 4011,
          "iscsiPort": 0,
          "nodeID": 4,
          "serviceID": 28,
          "serviceType": "block",
          "startedDriveIDs": [
            8
          ],
          "status": "healthy"
        }
      },
      {
        "drive": {
          "assignedService": 29,
          "asyncResultIDs": [],
          "attributes": {},
          "capacity": 300069052416,
          "customerSliceFileCapacity": 0,
          "driveID": 20,
          "driveStatus": "assigned",
          "driveType": "block",
          "nodeID": 3,
          "reservedSliceFileCapacity": 0,
          "serial": "scsi-SATA_INTEL_SSDSC2BB3BTWL305101U0300JGN",
          "slot": 7
        },
        "drives": [
          {
            "assignedService": 29,
            "asyncResultIDs": [],
            "attributes": {},
            "capacity": 300069052416,
            "customerSliceFileCapacity": 0,
            "driveID": 20,
            "driveStatus": "assigned",
            "driveType": "Block",
            "nodeID": 3,
            "reservedSliceFileCapacity": 0,
            "serial": "scsi-SATA_INTEL_SSDSC2BB3BTWL305101U0300JGN",
            "slot": 7
          }
        ],
        "node": {
          "associatedFServiceID": 0,
          "associatedMasterServiceID": 4,
          "attributes": {},
          "cip": "10.117.62.25",
          "cipi": "Bond10G",
          "fibreChannelTargetPortGroup": null,
          "mip": "10.117.60.25",
          "mipi": "Bond1G",
          "name": "SF-F2A3",
          "nodeID": 3,
          "platformInfo": {
            "chassisType": "R620",
            "cpuModel": "Intel(R) Xeon(R) CPU E5-2640 0 @ 2.50GHz",
            "nodeMemoryGB": 72,
            "nodeType": "SF3010"
          },
          "sip": "10.117.62.25",
          "sipi": "Bond10G",
          "softwareVersion": "9.0.0.1554",
          "uuid": "4C4C4544-0053-3310-8053-B6C04F435831",
          "virtualNetworks": []
        },
        "service": {
          "associatedBV": 0,
          "associatedTS": 0,
          "associatedVS": 0,
          "asyncResultIDs": [],
          "driveID": 20,
          "driveIDs": [
            20
          ],
          "firstTimeStartup": false,
          "ipcPort": 4012,
          "iscsiPort": 0,
          "nodeID": 3,
          "serviceID": 29,
          "serviceType": "block",
          "startedDriveIDs": [
            20
          ],
          "status": "healthy"
        }
      },
      {
        "drive": {
          "assignedService": 30,
          "asyncResultIDs": [],
          "attributes": {},
          "capacity": 300069052416,
          "customerSliceFileCapacity": 0,
          "driveID": 9,
          "driveStatus": "assigned",
          "driveType": "block",
          "nodeID": 4,
          "reservedSliceFileCapacity": 0,
          "serial": "scsi-SATA_INTEL_SSDSA2CW3BTPR227400QG300EGN",
          "slot": 7
        },
        "drives": [
          {
            "assignedService": 30,
            "asyncResultIDs": [],
            "attributes": {},
            "capacity": 300069052416,
            "customerSliceFileCapacity": 0,
            "driveID": 9,
            "driveStatus": "assigned",
            "driveType": "Block",
            "nodeID": 4,
            "reservedSliceFileCapacity": 0,
            "serial": "scsi-SATA_INTEL_SSDSA2CW3BTPR227400QG300EGN",
            "slot": 7
          }
        ],
        "node": {
          "associatedFServiceID": 0,
          "associatedMasterServiceID": 3,
          "attributes": {},
          "cip": "10.117.62.26",
          "cipi": "Bond10G",
          "fibreChannelTargetPortGroup": null,
          "mip": "10.117.60.26",
          "mipi": "Bond1G",
          "name": "SF-1713",
          "nodeID": 4,
          "platformInfo": {
            "chassisType": "R620",
            "cpuModel": "Intel(R) Xeon(R) CPU E5-2640 0 @ 2.50GHz",
            "nodeMemoryGB": 72,
            "nodeType": "SF3010"
          },
          "sip": "10.117.62.26",
          "sipi": "Bond10G",
          "softwareVersion": "9.0.0.1554",
          "uuid": "4C4C4544-0053-3210-8054-B6C04F435831",
          "virtualNetworks": []
        },
        "service": {
          "associatedBV": 0,
          "associatedTS": 0,
          "associatedVS": 0,
          "asyncResultIDs": [],
          "driveID": 9,
          "driveIDs": [
            9
          ],
          "firstTimeStartup": false,
          "ipcPort": 4012,
          "iscsiPort": 0,
          "nodeID": 4,
          "serviceID": 30,
          "serviceType": "block",
          "startedDriveIDs": [
            9
          ],
          "status": "healthy"
        }
      },
      {
        "drive": {
          "assignedService": 31,
          "asyncResultIDs": [],
          "attributes": {},
          "capacity": 300069052416,
          "customerSliceFileCapacity": 0,
          "driveID": 10,
          "driveStatus": "assigned",
          "driveType": "block",
          "nodeID": 4,
          "reservedSliceFileCapacity": 0,
          "serial": "scsi-SATA_INTEL_SSDSA2CW3BTPR2275018Z300EGN",
          "slot": 8
        },
        "drives": [
          {
            "assignedService": 31,
            "asyncResultIDs": [],
            "attributes": {},
            "capacity": 300069052416,
            "customerSliceFileCapacity": 0,
            "driveID": 10,
            "driveStatus": "assigned",
            "driveType": "Block",
            "nodeID": 4,
            "reservedSliceFileCapacity": 0,
            "serial": "scsi-SATA_INTEL_SSDSA2CW3BTPR2275018Z300EGN",
            "slot": 8
          }
        ],
        "node": {
          "associatedFServiceID": 0,
          "associatedMasterServiceID": 3,
          "attributes": {},
          "cip": "10.117.62.26",
          "cipi": "Bond10G",
          "fibreChannelTargetPortGroup": null,
          "mip": "10.117.60.26",
          "mipi": "Bond1G",
          "name": "SF-1713",
          "nodeID": 4,
          "platformInfo": {
            "chassisType": "R620",
            "cpuModel": "Intel(R) Xeon(R) CPU E5-2640 0 @ 2.50GHz",
            "nodeMemoryGB": 72,
            "nodeType": "SF3010"
          },
          "sip": "10.117.62.26",
          "sipi": "Bond10G",
          "softwareVersion": "9.0.0.1554",
          "uuid": "4C4C4544-0053-3210-8054-B6C04F435831",
          "virtualNetworks": []
        },
        "service": {
          "associatedBV": 0,
          "associatedTS": 0,
          "associatedVS": 0,
          "asyncResultIDs": [],
          "driveID": 10,
          "driveIDs": [
            10
          ],
          "firstTimeStartup": false,
          "ipcPort": 4013,
          "iscsiPort": 0,
          "nodeID": 4,
          "serviceID": 31,
          "serviceType": "block",
          "startedDriveIDs": [
            10
          ],
          "status": "healthy"
        }
      },
      {
        "drive": {
          "assignedService": 10,
          "asyncResultIDs": [],
          "attributes": {},
          "capacity": 299988156416,
          "customerSliceFileCapacity": 134994670387,
          "driveID": 1,
          "driveStatus": "assigned",
          "driveType": "volume",
          "nodeID": 4,
          "reservedSliceFileCapacity": 67497335193,
          "serial": "scsi-SATA_VRFSD3400GNCVMT205121574-part4",
          "slot": -1
        },
        "drives": [
          {
            "assignedService": 10,
            "asyncResultIDs": [],
            "attributes": {},
            "capacity": 299988156416,
            "customerSliceFileCapacity": 134994670387,
            "driveID": 1,
            "driveStatus": "assigned",
            "driveType": "Slice",
            "nodeID": 4,
            "reservedSliceFileCapacity": 67497335193,
            "serial": "scsi-SATA_VRFSD3400GNCVMT205121574-part4",
            "slot": -1
          }
        ],
        "node": {
          "associatedFServiceID": 0,
          "associatedMasterServiceID": 3,
          "attributes": {},
          "cip": "10.117.62.26",
          "cipi": "Bond10G",
          "fibreChannelTargetPortGroup": null,
          "mip": "10.117.60.26",
          "mipi": "Bond1G",
          "name": "SF-1713",
          "nodeID": 4,
          "platformInfo": {
            "chassisType": "R620",
            "cpuModel": "Intel(R) Xeon(R) CPU E5-2640 0 @ 2.50GHz",
            "nodeMemoryGB": 72,
            "nodeType": "SF3010"
          },
          "sip": "10.117.62.26",
          "sipi": "Bond10G",
          "softwareVersion": "9.0.0.1554",
          "uuid": "4C4C4544-0053-3210-8054-B6C04F435831",
          "virtualNetworks": []
        },
        "service": {
          "associatedBV": 7,
          "associatedTS": 9,
          "associatedVS": 8,
          "asyncResultIDs": [],
          "driveID": 1,
          "driveIDs": [
            1
          ],
          "firstTimeStartup": false,
          "ipcPort": 4002,
          "iscsiPort": 0,
          "nodeID": 4,
          "serviceID": 10,
          "serviceType": "slice",
          "startedDriveIDs": [
            1
          ],
          "status": "healthy"
        }
      },
      {
        "drive": {
          "assignedService": 32,
          "asyncResultIDs": [],
          "attributes": {},
          "capacity": 300069052416,
          "customerSliceFileCapacity": 0,
          "driveID": 21,
          "driveStatus": "assigned",
          "driveType": "block",
          "nodeID": 3,
          "reservedSliceFileCapacity": 0,
          "serial": "scsi-SATA_INTEL_SSDSC2BB3BTWL3072006A300PGN",
          "slot": 8
        },
        "drives": [
          {
            "assignedService": 32,
            "asyncResultIDs": [],
            "attributes": {},
            "capacity": 300069052416,
            "customerSliceFileCapacity": 0,
            "driveID": 21,
            "driveStatus": "assigned",
            "driveType": "Block",
            "nodeID": 3,
            "reservedSliceFileCapacity": 0,
            "serial": "scsi-SATA_INTEL_SSDSC2BB3BTWL3072006A300PGN",
            "slot": 8
          }
        ],
        "node": {
          "associatedFServiceID": 0,
          "associatedMasterServiceID": 4,
          "attributes": {},
          "cip": "10.117.62.25",
          "cipi": "Bond10G",
          "fibreChannelTargetPortGroup": null,
          "mip": "10.117.60.25",
          "mipi": "Bond1G",
          "name": "SF-F2A3",
          "nodeID": 3,
          "platformInfo": {
            "chassisType": "R620",
            "cpuModel": "Intel(R) Xeon(R) CPU E5-2640 0 @ 2.50GHz",
            "nodeMemoryGB": 72,
            "nodeType": "SF3010"
          },
          "sip": "10.117.62.25",
          "sipi": "Bond10G",
          "softwareVersion": "9.0.0.1554",
          "uuid": "4C4C4544-0053-3310-8053-B6C04F435831",
          "virtualNetworks": []
        },
        "service": {
          "associatedBV": 0,
          "associatedTS": 0,
          "associatedVS": 0,
          "asyncResultIDs": [],
          "driveID": 21,
          "driveIDs": [
            21
          ],
          "firstTimeStartup": false,
          "ipcPort": 4013,
          "iscsiPort": 0,
          "nodeID": 3,
          "serviceID": 32,
          "serviceType": "block",
          "startedDriveIDs": [
            21
          ],
          "status": "healthy"
        }
      },
      {
        "drives": [],
        "node": {
          "associatedFServiceID": 0,
          "associatedMasterServiceID": 4,
          "attributes": {},
          "cip": "10.117.62.25",
          "cipi": "Bond10G",
          "fibreChannelTargetPortGroup": null,
          "mip": "10.117.60.25",
          "mipi": "Bond1G",
          "name": "SF-F2A3",
          "nodeID": 3,
          "platformInfo": {
            "chassisType": "R620",
            "cpuModel": "Intel(R) Xeon(R) CPU E5-2640 0 @ 2.50GHz",
            "nodeMemoryGB": 72,
            "nodeType": "SF3010"
          },
          "sip": "10.117.62.25",
          "sipi": "Bond10G",
          "softwareVersion": "9.0.0.1554",
          "uuid": "4C4C4544-0053-3310-8053-B6C04F435831",
          "virtualNetworks": []
        },
        "service": {
          "associatedBV": 0,
          "associatedTS": 0,
          "associatedVS": 0,
          "asyncResultIDs": [],
          "driveID": 0,
          "driveIDs": [],
          "firstTimeStartup": true,
          "ipcPort": 4001,
          "iscsiPort": 0,
          "nodeID": 3,
          "serviceID": 11,
          "serviceType": "bulkvolume",
          "startedDriveIDs": [],
          "status": "healthy"
        }
      },
      {
        "drive": {
          "assignedService": 33,
          "asyncResultIDs": [],
          "attributes": {},
          "capacity": 300069052416,
          "customerSliceFileCapacity": 0,
          "driveID": 11,
          "driveStatus": "assigned",
          "driveType": "block",
          "nodeID": 4,
          "reservedSliceFileCapacity": 0,
          "serial": "scsi-SATA_INTEL_SSDSA2CW3BTPR227500TS300EGN",
          "slot": 9
        },
        "drives": [
          {
            "assignedService": 33,
            "asyncResultIDs": [],
            "attributes": {},
            "capacity": 300069052416,
            "customerSliceFileCapacity": 0,
            "driveID": 11,
            "driveStatus": "assigned",
            "driveType": "Block",
            "nodeID": 4,
            "reservedSliceFileCapacity": 0,
            "serial": "scsi-SATA_INTEL_SSDSA2CW3BTPR227500TS300EGN",
            "slot": 9
          }
        ],
        "node": {
          "associatedFServiceID": 0,
          "associatedMasterServiceID": 3,
          "attributes": {},
          "cip": "10.117.62.26",
          "cipi": "Bond10G",
          "fibreChannelTargetPortGroup": null,
          "mip": "10.117.60.26",
          "mipi": "Bond1G",
          "name": "SF-1713",
          "nodeID": 4,
          "platformInfo": {
            "chassisType": "R620",
            "cpuModel": "Intel(R) Xeon(R) CPU E5-2640 0 @ 2.50GHz",
            "nodeMemoryGB": 72,
            "nodeType": "SF3010"
          },
          "sip": "10.117.62.26",
          "sipi": "Bond10G",
          "softwareVersion": "9.0.0.1554",
          "uuid": "4C4C4544-0053-3210-8054-B6C04F435831",
          "virtualNetworks": []
        },
        "service": {
          "associatedBV": 0,
          "associatedTS": 0,
          "associatedVS": 0,
          "asyncResultIDs": [],
          "driveID": 11,
          "driveIDs": [
            11
          ],
          "firstTimeStartup": false,
          "ipcPort": 4014,
          "iscsiPort": 0,
          "nodeID": 4,
          "serviceID": 33,
          "serviceType": "block",
          "startedDriveIDs": [
            11
          ],
          "status": "healthy"
        }
      },
      {
        "drives": [],
        "node": {
          "associatedFServiceID": 0,
          "associatedMasterServiceID": 4,
          "attributes": {},
          "cip": "10.117.62.25",
          "cipi": "Bond10G",
          "fibreChannelTargetPortGroup": null,
          "mip": "10.117.60.25",
          "mipi": "Bond1G",
          "name": "SF-F2A3",
          "nodeID": 3,
          "platformInfo": {
            "chassisType": "R620",
            "cpuModel": "Intel(R) Xeon(R) CPU E5-2640 0 @ 2.50GHz",
            "nodeMemoryGB": 72,
            "nodeType": "SF3010"
          },
          "sip": "10.117.62.25",
          "sipi": "Bond10G",
          "softwareVersion": "9.0.0.1554",
          "uuid": "4C4C4544-0053-3310-8053-B6C04F435831",
          "virtualNetworks": []
        },
        "service": {
          "associatedBV": 0,
          "associatedTS": 0,
          "associatedVS": 0,
          "asyncResultIDs": [],
          "driveID": 0,
          "driveIDs": [],
          "firstTimeStartup": true,
          "ipcPort": 4003,
          "iscsiPort": 0,
          "nodeID": 3,
          "serviceID": 12,
          "serviceType": "volume",
          "startedDriveIDs": [],
          "status": "healthy"
        }
      },
      {
        "drive": {
          "assignedService": 34,
          "asyncResultIDs": [],
          "attributes": {},
          "capacity": 300069052416,
          "customerSliceFileCapacity": 0,
          "driveID": 22,
          "driveStatus": "assigned",
          "driveType": "block",
          "nodeID": 3,
          "reservedSliceFileCapacity": 0,
          "serial": "scsi-SATA_INTEL_SSDSC2BB3BTWL3071045B300PGN",
          "slot": 9
        },
        "drives": [
          {
            "assignedService": 34,
            "asyncResultIDs": [],
            "attributes": {},
            "capacity": 300069052416,
            "customerSliceFileCapacity": 0,
            "driveID": 22,
            "driveStatus": "assigned",
            "driveType": "Block",
            "nodeID": 3,
            "reservedSliceFileCapacity": 0,
            "serial": "scsi-SATA_INTEL_SSDSC2BB3BTWL3071045B300PGN",
            "slot": 9
          }
        ],
        "node": {
          "associatedFServiceID": 0,
          "associatedMasterServiceID": 4,
          "attributes": {},
          "cip": "10.117.62.25",
          "cipi": "Bond10G",
          "fibreChannelTargetPortGroup": null,
          "mip": "10.117.60.25",
          "mipi": "Bond1G",
          "name": "SF-F2A3",
          "nodeID": 3,
          "platformInfo": {
            "chassisType": "R620",
            "cpuModel": "Intel(R) Xeon(R) CPU E5-2640 0 @ 2.50GHz",
            "nodeMemoryGB": 72,
            "nodeType": "SF3010"
          },
          "sip": "10.117.62.25",
          "sipi": "Bond10G",
          "softwareVersion": "9.0.0.1554",
          "uuid": "4C4C4544-0053-3310-8053-B6C04F435831",
          "virtualNetworks": []
        },
        "service": {
          "associatedBV": 0,
          "associatedTS": 0,
          "associatedVS": 0,
          "asyncResultIDs": [],
          "driveID": 22,
          "driveIDs": [
            22
          ],
          "firstTimeStartup": false,
          "ipcPort": 4014,
          "iscsiPort": 0,
          "nodeID": 3,
          "serviceID": 34,
          "serviceType": "block",
          "startedDriveIDs": [
            22
          ],
          "status": "healthy"
        }
      },
      {
        "drives": [],
        "node": {
          "associatedFServiceID": 0,
          "associatedMasterServiceID": 4,
          "attributes": {},
          "cip": "10.117.62.25",
          "cipi": "Bond10G",
          "fibreChannelTargetPortGroup": null,
          "mip": "10.117.60.25",
          "mipi": "Bond1G",
          "name": "SF-F2A3",
          "nodeID": 3,
          "platformInfo": {
            "chassisType": "R620",
            "cpuModel": "Intel(R) Xeon(R) CPU E5-2640 0 @ 2.50GHz",
            "nodeMemoryGB": 72,
            "nodeType": "SF3010"
          },
          "sip": "10.117.62.25",
          "sipi": "Bond10G",
          "softwareVersion": "9.0.0.1554",
          "uuid": "4C4C4544-0053-3310-8053-B6C04F435831",
          "virtualNetworks": []
        },
        "service": {
          "associatedBV": 0,
          "associatedTS": 0,
          "associatedVS": 0,
          "asyncResultIDs": [],
          "driveID": 0,
          "driveIDs": [],
          "firstTimeStartup": true,
          "ipcPort": 4004,
          "iscsiPort": 3260,
          "nodeID": 3,
          "serviceID": 13,
          "serviceType": "transport",
          "startedDriveIDs": [],
          "status": "healthy"
        }
      },
      {
        "drive": {
          "assignedService": 14,
          "asyncResultIDs": [],
          "attributes": {},
          "capacity": 299988156416,
          "customerSliceFileCapacity": 134994670387,
          "driveID": 12,
          "driveStatus": "assigned",
          "driveType": "volume",
          "nodeID": 3,
          "reservedSliceFileCapacity": 67497335193,
          "serial": "scsi-SATA_VRFSD3400GNCVMT205121578-part4",
          "slot": -1
        },
        "drives": [
          {
            "assignedService": 14,
            "asyncResultIDs": [],
            "attributes": {},
            "capacity": 299988156416,
            "customerSliceFileCapacity": 134994670387,
            "driveID": 12,
            "driveStatus": "assigned",
            "driveType": "Slice",
            "nodeID": 3,
            "reservedSliceFileCapacity": 67497335193,
            "serial": "scsi-SATA_VRFSD3400GNCVMT205121578-part4",
            "slot": -1
          }
        ],
        "node": {
          "associatedFServiceID": 0,
          "associatedMasterServiceID": 4,
          "attributes": {},
          "cip": "10.117.62.25",
          "cipi": "Bond10G",
          "fibreChannelTargetPortGroup": null,
          "mip": "10.117.60.25",
          "mipi": "Bond1G",
          "name": "SF-F2A3",
          "nodeID": 3,
          "platformInfo": {
            "chassisType": "R620",
            "cpuModel": "Intel(R) Xeon(R) CPU E5-2640 0 @ 2.50GHz",
            "nodeMemoryGB": 72,
            "nodeType": "SF3010"
          },
          "sip": "10.117.62.25",
          "sipi": "Bond10G",
          "softwareVersion": "9.0.0.1554",
          "uuid": "4C4C4544-0053-3310-8053-B6C04F435831",
          "virtualNetworks": []
        },
        "service": {
          "associatedBV": 11,
          "associatedTS": 13,
          "associatedVS": 12,
          "asyncResultIDs": [],
          "driveID": 12,
          "driveIDs": [
            12
          ],
          "firstTimeStartup": false,
          "ipcPort": 4002,
          "iscsiPort": 0,
          "nodeID": 3,
          "serviceID": 14,
          "serviceType": "slice",
          "startedDriveIDs": [
            12
          ],
          "status": "healthy"
        }
      },
      {
        "drive": {
          "assignedService": 15,
          "asyncResultIDs": [],
          "attributes": {},
          "capacity": 300069052416,
          "customerSliceFileCapacity": 0,
          "driveID": 2,
          "driveStatus": "assigned",
          "driveType": "block",
          "nodeID": 4,
          "reservedSliceFileCapacity": 0,
          "serial": "scsi-SATA_INTEL_SSDSA2CW3CVPR121400NA300EGN",
          "slot": 0
        },
        "drives": [
          {
            "assignedService": 15,
            "asyncResultIDs": [],
            "attributes": {},
            "capacity": 300069052416,
            "customerSliceFileCapacity": 0,
            "driveID": 2,
            "driveStatus": "assigned",
            "driveType": "Block",
            "nodeID": 4,
            "reservedSliceFileCapacity": 0,
            "serial": "scsi-SATA_INTEL_SSDSA2CW3CVPR121400NA300EGN",
            "slot": 0
          }
        ],
        "node": {
          "associatedFServiceID": 0,
          "associatedMasterServiceID": 3,
          "attributes": {},
          "cip": "10.117.62.26",
          "cipi": "Bond10G",
          "fibreChannelTargetPortGroup": null,
          "mip": "10.117.60.26",
          "mipi": "Bond1G",
          "name": "SF-1713",
          "nodeID": 4,
          "platformInfo": {
            "chassisType": "R620",
            "cpuModel": "Intel(R) Xeon(R) CPU E5-2640 0 @ 2.50GHz",
            "nodeMemoryGB": 72,
            "nodeType": "SF3010"
          },
          "sip": "10.117.62.26",
          "sipi": "Bond10G",
          "softwareVersion": "9.0.0.1554",
          "uuid": "4C4C4544-0053-3210-8054-B6C04F435831",
          "virtualNetworks": []
        },
        "service": {
          "associatedBV": 0,
          "associatedTS": 0,
          "associatedVS": 0,
          "asyncResultIDs": [],
          "driveID": 2,
          "driveIDs": [
            2
          ],
          "firstTimeStartup": false,
          "ipcPort": 4005,
          "iscsiPort": 0,
          "nodeID": 4,
          "serviceID": 15,
          "serviceType": "block",
          "startedDriveIDs": [
            2
          ],
          "status": "healthy"
        }
      },
      {
        "drive": {
          "assignedService": 16,
          "asyncResultIDs": [],
          "attributes": {},
          "capacity": 300069052416,
          "customerSliceFileCapacity": 0,
          "driveID": 13,
          "driveStatus": "assigned",
          "driveType": "block",
          "nodeID": 3,
          "reservedSliceFileCapacity": 0,
          "serial": "scsi-SATA_INTEL_SSDSA2CW3CVPR1214002J300EGN",
          "slot": 0
        },
        "drives": [
          {
            "assignedService": 16,
            "asyncResultIDs": [],
            "attributes": {},
            "capacity": 300069052416,
            "customerSliceFileCapacity": 0,
            "driveID": 13,
            "driveStatus": "assigned",
            "driveType": "Block",
            "nodeID": 3,
            "reservedSliceFileCapacity": 0,
            "serial": "scsi-SATA_INTEL_SSDSA2CW3CVPR1214002J300EGN",
            "slot": 0
          }
        ],
        "node": {
          "associatedFServiceID": 0,
          "associatedMasterServiceID": 4,
          "attributes": {},
          "cip": "10.117.62.25",
          "cipi": "Bond10G",
          "fibreChannelTargetPortGroup": null,
          "mip": "10.117.60.25",
          "mipi": "Bond1G",
          "name": "SF-F2A3",
          "nodeID": 3,
          "platformInfo": {
            "chassisType": "R620",
            "cpuModel": "Intel(R) Xeon(R) CPU E5-2640 0 @ 2.50GHz",
            "nodeMemoryGB": 72,
            "nodeType": "SF3010"
          },
          "sip": "10.117.62.25",
          "sipi": "Bond10G",
          "softwareVersion": "9.0.0.1554",
          "uuid": "4C4C4544-0053-3310-8053-B6C04F435831",
          "virtualNetworks": []
        },
        "service": {
          "associatedBV": 0,
          "associatedTS": 0,
          "associatedVS": 0,
          "asyncResultIDs": [],
          "driveID": 13,
          "driveIDs": [
            13
          ],
          "firstTimeStartup": false,
          "ipcPort": 4005,
          "iscsiPort": 0,
          "nodeID": 3,
          "serviceID": 16,
          "serviceType": "block",
          "startedDriveIDs": [
            13
          ],
          "status": "healthy"
        }
      },
      {
        "drive": {
          "assignedService": 17,
          "asyncResultIDs": [],
          "attributes": {},
          "capacity": 300069052416,
          "customerSliceFileCapacity": 0,
          "driveID": 14,
          "driveStatus": "assigned",
          "driveType": "block",
          "nodeID": 3,
          "reservedSliceFileCapacity": 0,
          "serial": "scsi-SATA_INTEL_SSDSC2BB3BTWL311301EL300PGN",
          "slot": 1
        },
        "drives": [
          {
            "assignedService": 17,
            "asyncResultIDs": [],
            "attributes": {},
            "capacity": 300069052416,
            "customerSliceFileCapacity": 0,
            "driveID": 14,
            "driveStatus": "assigned",
            "driveType": "Block",
            "nodeID": 3,
            "reservedSliceFileCapacity": 0,
            "serial": "scsi-SATA_INTEL_SSDSC2BB3BTWL311301EL300PGN",
            "slot": 1
          }
        ],
        "node": {
          "associatedFServiceID": 0,
          "associatedMasterServiceID": 4,
          "attributes": {},
          "cip": "10.117.62.25",
          "cipi": "Bond10G",
          "fibreChannelTargetPortGroup": null,
          "mip": "10.117.60.25",
          "mipi": "Bond1G",
          "name": "SF-F2A3",
          "nodeID": 3,
          "platformInfo": {
            "chassisType": "R620",
            "cpuModel": "Intel(R) Xeon(R) CPU E5-2640 0 @ 2.50GHz",
            "nodeMemoryGB": 72,
            "nodeType": "SF3010"
          },
          "sip": "10.117.62.25",
          "sipi": "Bond10G",
          "softwareVersion": "9.0.0.1554",
          "uuid": "4C4C4544-0053-3310-8053-B6C04F435831",
          "virtualNetworks": []
        },
        "service": {
          "associatedBV": 0,
          "associatedTS": 0,
          "associatedVS": 0,
          "asyncResultIDs": [],
          "driveID": 14,
          "driveIDs": [
            14
          ],
          "firstTimeStartup": false,
          "ipcPort": 4006,
          "iscsiPort": 0,
          "nodeID": 3,
          "serviceID": 17,
          "serviceType": "block",
          "startedDriveIDs": [
            14
          ],
          "status": "healthy"
        }
      },
      {
        "drive": {
          "assignedService": 18,
          "asyncResultIDs": [],
          "attributes": {},
          "capacity": 300069052416,
          "customerSliceFileCapacity": 0,
          "driveID": 3,
          "driveStatus": "assigned",
          "driveType": "block",
          "nodeID": 4,
          "reservedSliceFileCapacity": 0,
          "serial": "scsi-SATA_INTEL_SSDSA2CW3CVPR1214010M300EGN",
          "slot": 1
        },
        "drives": [
          {
            "assignedService": 18,
            "asyncResultIDs": [],
            "attributes": {},
            "capacity": 300069052416,
            "customerSliceFileCapacity": 0,
            "driveID": 3,
            "driveStatus": "assigned",
            "driveType": "Block",
            "nodeID": 4,
            "reservedSliceFileCapacity": 0,
            "serial": "scsi-SATA_INTEL_SSDSA2CW3CVPR1214010M300EGN",
            "slot": 1
          }
        ],
        "node": {
          "associatedFServiceID": 0,
          "associatedMasterServiceID": 3,
          "attributes": {},
          "cip": "10.117.62.26",
          "cipi": "Bond10G",
          "fibreChannelTargetPortGroup": null,
          "mip": "10.117.60.26",
          "mipi": "Bond1G",
          "name": "SF-1713",
          "nodeID": 4,
          "platformInfo": {
            "chassisType": "R620",
            "cpuModel": "Intel(R) Xeon(R) CPU E5-2640 0 @ 2.50GHz",
            "nodeMemoryGB": 72,
            "nodeType": "SF3010"
          },
          "sip": "10.117.62.26",
          "sipi": "Bond10G",
          "softwareVersion": "9.0.0.1554",
          "uuid": "4C4C4544-0053-3210-8054-B6C04F435831",
          "virtualNetworks": []
        },
        "service": {
          "associatedBV": 0,
          "associatedTS": 0,
          "associatedVS": 0,
          "asyncResultIDs": [],
          "driveID": 3,
          "driveIDs": [
            3
          ],
          "firstTimeStartup": false,
          "ipcPort": 4006,
          "iscsiPort": 0,
          "nodeID": 4,
          "serviceID": 18,
          "serviceType": "block",
          "startedDriveIDs": [
            3
          ],
          "status": "healthy"
        }
      },
      {
        "drive": {
          "assignedService": 19,
          "asyncResultIDs": [],
          "attributes": {},
          "capacity": 300069052416,
          "customerSliceFileCapacity": 0,
          "driveID": 15,
          "driveStatus": "assigned",
          "driveType": "block",
          "nodeID": 3,
          "reservedSliceFileCapacity": 0,
          "serial": "scsi-SATA_INTEL_SSDSC2BB3BTWL3113015C300PGN",
          "slot": 2
        },
        "drives": [
          {
            "assignedService": 19,
            "asyncResultIDs": [],
            "attributes": {},
            "capacity": 300069052416,
            "customerSliceFileCapacity": 0,
            "driveID": 15,
            "driveStatus": "assigned",
            "driveType": "Block",
            "nodeID": 3,
            "reservedSliceFileCapacity": 0,
            "serial": "scsi-SATA_INTEL_SSDSC2BB3BTWL3113015C300PGN",
            "slot": 2
          }
        ],
        "node": {
          "associatedFServiceID": 0,
          "associatedMasterServiceID": 4,
          "attributes": {},
          "cip": "10.117.62.25",
          "cipi": "Bond10G",
          "fibreChannelTargetPortGroup": null,
          "mip": "10.117.60.25",
          "mipi": "Bond1G",
          "name": "SF-F2A3",
          "nodeID": 3,
          "platformInfo": {
            "chassisType": "R620",
            "cpuModel": "Intel(R) Xeon(R) CPU E5-2640 0 @ 2.50GHz",
            "nodeMemoryGB": 72,
            "nodeType": "SF3010"
          },
          "sip": "10.117.62.25",
          "sipi": "Bond10G",
          "softwareVersion": "9.0.0.1554",
          "uuid": "4C4C4544-0053-3310-8053-B6C04F435831",
          "virtualNetworks": []
        },
        "service": {
          "associatedBV": 0,
          "associatedTS": 0,
          "associatedVS": 0,
          "asyncResultIDs": [],
          "driveID": 15,
          "driveIDs": [
            15
          ],
          "firstTimeStartup": false,
          "ipcPort": 4007,
          "iscsiPort": 0,
          "nodeID": 3,
          "serviceID": 19,
          "serviceType": "block",
          "startedDriveIDs": [
            15
          ],
          "status": "healthy"
        }
      },
      {
        "drives": [],
        "node": {
          "associatedFServiceID": 2,
          "associatedMasterServiceID": 1,
          "attributes": {},
          "cip": "10.117.62.23",
          "cipi": "Bond10G",
          "fibreChannelTargetPortGroup": 0,
          "mip": "10.117.60.23",
          "mipi": "Bond1G",
          "name": "SF-5391",
          "nodeID": 1,
          "platformInfo": {
            "chassisType": "R620",
            "cpuModel": "Intel(R) Xeon(R) CPU E5-2640 0 @ 2.50GHz",
            "nodeMemoryGB": 32,
            "nodeType": "FC0025"
          },
          "sip": "10.117.62.23",
          "sipi": "Bond10G",
          "softwareVersion": "9.0.0.1554",
          "uuid": "4C4C4544-0032-4B10-8038-C2C04F513232",
          "virtualNetworks": []
        },
        "service": {
          "associatedBV": 0,
          "associatedTS": 0,
          "associatedVS": 8000,
          "asyncResultIDs": [],
          "driveID": 0,
          "driveIDs": [],
          "firstTimeStartup": true,
          "ipcPort": 4000,
          "iscsiPort": 0,
          "nodeID": 1,
          "serviceID": 1,
          "serviceType": "master",
          "startedDriveIDs": [],
          "status": "healthy"
        }
      },
      {
        "drives": [],
        "node": {
          "associatedFServiceID": 2,
          "associatedMasterServiceID": 1,
          "attributes": {},
          "cip": "10.117.62.23",
          "cipi": "Bond10G",
          "fibreChannelTargetPortGroup": 0,
          "mip": "10.117.60.23",
          "mipi": "Bond1G",
          "name": "SF-5391",
          "nodeID": 1,
          "platformInfo": {
            "chassisType": "R620",
            "cpuModel": "Intel(R) Xeon(R) CPU E5-2640 0 @ 2.50GHz",
            "nodeMemoryGB": 32,
            "nodeType": "FC0025"
          },
          "sip": "10.117.62.23",
          "sipi": "Bond10G",
          "softwareVersion": "9.0.0.1554",
          "uuid": "4C4C4544-0032-4B10-8038-C2C04F513232",
          "virtualNetworks": []
        },
        "service": {
          "associatedBV": 0,
          "associatedTS": 0,
          "associatedVS": 0,
          "asyncResultIDs": [],
          "driveID": 0,
          "driveIDs": [],
          "firstTimeStartup": true,
          "ipcPort": 4001,
          "iscsiPort": 0,
          "nodeID": 1,
          "serviceID": 2,
          "serviceType": "fibre",
          "startedDriveIDs": [],
          "status": "healthy"
        }
      },
      {
        "drives": [],
        "node": {
          "associatedFServiceID": 0,
          "associatedMasterServiceID": 3,
          "attributes": {},
          "cip": "10.117.62.26",
          "cipi": "Bond10G",
          "fibreChannelTargetPortGroup": null,
          "mip": "10.117.60.26",
          "mipi": "Bond1G",
          "name": "SF-1713",
          "nodeID": 4,
          "platformInfo": {
            "chassisType": "R620",
            "cpuModel": "Intel(R) Xeon(R) CPU E5-2640 0 @ 2.50GHz",
            "nodeMemoryGB": 72,
            "nodeType": "SF3010"
          },
          "sip": "10.117.62.26",
          "sipi": "Bond10G",
          "softwareVersion": "9.0.0.1554",
          "uuid": "4C4C4544-0053-3210-8054-B6C04F435831",
          "virtualNetworks": []
        },
        "service": {
          "associatedBV": 0,
          "associatedTS": 0,
          "associatedVS": 8000,
          "asyncResultIDs": [],
          "driveID": 0,
          "driveIDs": [],
          "firstTimeStartup": true,
          "ipcPort": 4000,
          "iscsiPort": 0,
          "nodeID": 4,
          "serviceID": 3,
          "serviceType": "master",
          "startedDriveIDs": [],
          "status": "healthy"
        }
      },
      {
        "drives": [],
        "node": {
          "associatedFServiceID": 0,
          "associatedMasterServiceID": 4,
          "attributes": {},
          "cip": "10.117.62.25",
          "cipi": "Bond10G",
          "fibreChannelTargetPortGroup": null,
          "mip": "10.117.60.25",
          "mipi": "Bond1G",
          "name": "SF-F2A3",
          "nodeID": 3,
          "platformInfo": {
            "chassisType": "R620",
            "cpuModel": "Intel(R) Xeon(R) CPU E5-2640 0 @ 2.50GHz",
            "nodeMemoryGB": 72,
            "nodeType": "SF3010"
          },
          "sip": "10.117.62.25",
          "sipi": "Bond10G",
          "softwareVersion": "9.0.0.1554",
          "uuid": "4C4C4544-0053-3310-8053-B6C04F435831",
          "virtualNetworks": []
        },
        "service": {
          "associatedBV": 0,
          "associatedTS": 0,
          "associatedVS": 8000,
          "asyncResultIDs": [],
          "driveID": 0,
          "driveIDs": [],
          "firstTimeStartup": true,
          "ipcPort": 4000,
          "iscsiPort": 0,
          "nodeID": 3,
          "serviceID": 4,
          "serviceType": "master",
          "startedDriveIDs": [],
          "status": "healthy"
        }
      },
      {
        "drives": [],
        "node": {
          "associatedFServiceID": 6,
          "associatedMasterServiceID": 5,
          "attributes": {},
          "cip": "10.117.62.24",
          "cipi": "Bond10G",
          "fibreChannelTargetPortGroup": 1,
          "mip": "10.117.60.24",
          "mipi": "Bond1G",
          "name": "SF-918D",
          "nodeID": 2,
          "platformInfo": {
            "chassisType": "R620",
            "cpuModel": "Intel(R) Xeon(R) CPU E5-2640 0 @ 2.50GHz",
            "nodeMemoryGB": 32,
            "nodeType": "FC0025"
          },
          "sip": "10.117.62.24",
          "sipi": "Bond10G",
          "softwareVersion": "9.0.0.1554",
          "uuid": "4C4C4544-0034-5910-8033-B1C04F503232",
          "virtualNetworks": []
        },
        "service": {
          "associatedBV": 0,
          "associatedTS": 0,
          "associatedVS": 8000,
          "asyncResultIDs": [],
          "driveID": 0,
          "driveIDs": [],
          "firstTimeStartup": true,
          "ipcPort": 4000,
          "iscsiPort": 0,
          "nodeID": 2,
          "serviceID": 5,
          "serviceType": "master",
          "startedDriveIDs": [],
          "status": "healthy"
        }
      },
      {
        "drives": [],
        "node": {
          "associatedFServiceID": 6,
          "associatedMasterServiceID": 5,
          "attributes": {},
          "cip": "10.117.62.24",
          "cipi": "Bond10G",
          "fibreChannelTargetPortGroup": 1,
          "mip": "10.117.60.24",
          "mipi": "Bond1G",
          "name": "SF-918D",
          "nodeID": 2,
          "platformInfo": {
            "chassisType": "R620",
            "cpuModel": "Intel(R) Xeon(R) CPU E5-2640 0 @ 2.50GHz",
            "nodeMemoryGB": 32,
            "nodeType": "FC0025"
          },
          "sip": "10.117.62.24",
          "sipi": "Bond10G",
          "softwareVersion": "9.0.0.1554",
          "uuid": "4C4C4544-0034-5910-8033-B1C04F503232",
          "virtualNetworks": []
        },
        "service": {
          "associatedBV": 0,
          "associatedTS": 0,
          "associatedVS": 0,
          "asyncResultIDs": [],
          "driveID": 0,
          "driveIDs": [],
          "firstTimeStartup": true,
          "ipcPort": 4001,
          "iscsiPort": 0,
          "nodeID": 2,
          "serviceID": 6,
          "serviceType": "fibre",
          "startedDriveIDs": [],
          "status": "healthy"
        }
      },
      {
        "drives": [],
        "node": {
          "associatedFServiceID": 0,
          "associatedMasterServiceID": 3,
          "attributes": {},
          "cip": "10.117.62.26",
          "cipi": "Bond10G",
          "fibreChannelTargetPortGroup": null,
          "mip": "10.117.60.26",
          "mipi": "Bond1G",
          "name": "SF-1713",
          "nodeID": 4,
          "platformInfo": {
            "chassisType": "R620",
            "cpuModel": "Intel(R) Xeon(R) CPU E5-2640 0 @ 2.50GHz",
            "nodeMemoryGB": 72,
            "nodeType": "SF3010"
          },
          "sip": "10.117.62.26",
          "sipi": "Bond10G",
          "softwareVersion": "9.0.0.1554",
          "uuid": "4C4C4544-0053-3210-8054-B6C04F435831",
          "virtualNetworks": []
        },
        "service": {
          "associatedBV": 0,
          "associatedTS": 0,
          "associatedVS": 0,
          "asyncResultIDs": [],
          "driveID": 0,
          "driveIDs": [],
          "firstTimeStartup": true,
          "ipcPort": 4001,
          "iscsiPort": 0,
          "nodeID": 4,
          "serviceID": 7,
          "serviceType": "bulkvolume",
          "startedDriveIDs": [],
          "status": "healthy"
        }
      },
      {
        "drives": [],
        "node": {
          "associatedFServiceID": 0,
          "associatedMasterServiceID": 3,
          "attributes": {},
          "cip": "10.117.62.26",
          "cipi": "Bond10G",
          "fibreChannelTargetPortGroup": null,
          "mip": "10.117.60.26",
          "mipi": "Bond1G",
          "name": "SF-1713",
          "nodeID": 4,
          "platformInfo": {
            "chassisType": "R620",
            "cpuModel": "Intel(R) Xeon(R) CPU E5-2640 0 @ 2.50GHz",
            "nodeMemoryGB": 72,
            "nodeType": "SF3010"
          },
          "sip": "10.117.62.26",
          "sipi": "Bond10G",
          "softwareVersion": "9.0.0.1554",
          "uuid": "4C4C4544-0053-3210-8054-B6C04F435831",
          "virtualNetworks": []
        },
        "service": {
          "associatedBV": 0,
          "associatedTS": 0,
          "associatedVS": 0,
          "asyncResultIDs": [],
          "driveID": 0,
          "driveIDs": [],
          "firstTimeStartup": true,
          "ipcPort": 4003,
          "iscsiPort": 0,
          "nodeID": 4,
          "serviceID": 8,
          "serviceType": "volume",
          "startedDriveIDs": [],
          "status": "healthy"
        }
      },
      {
        "drives": [],
        "node": {
          "associatedFServiceID": 0,
          "associatedMasterServiceID": 3,
          "attributes": {},
          "cip": "10.117.62.26",
          "cipi": "Bond10G",
          "fibreChannelTargetPortGroup": null,
          "mip": "10.117.60.26",
          "mipi": "Bond1G",
          "name": "SF-1713",
          "nodeID": 4,
          "platformInfo": {
            "chassisType": "R620",
            "cpuModel": "Intel(R) Xeon(R) CPU E5-2640 0 @ 2.50GHz",
            "nodeMemoryGB": 72,
            "nodeType": "SF3010"
          },
          "sip": "10.117.62.26",
          "sipi": "Bond10G",
          "softwareVersion": "9.0.0.1554",
          "uuid": "4C4C4544-0053-3210-8054-B6C04F435831",
          "virtualNetworks": []
        },
        "service": {
          "associatedBV": 0,
          "associatedTS": 0,
          "associatedVS": 0,
          "asyncResultIDs": [],
          "driveID": 0,
          "driveIDs": [],
          "firstTimeStartup": true,
          "ipcPort": 4004,
          "iscsiPort": 3260,
          "nodeID": 4,
          "serviceID": 9,
          "serviceType": "transport",
          "startedDriveIDs": [],
          "status": "healthy"
        }
      },
      {
        "drive": {
          "assignedService": 20,
          "asyncResultIDs": [],
          "attributes": {},
          "capacity": 300069052416,
          "customerSliceFileCapacity": 0,
          "driveID": 4,
          "driveStatus": "assigned",
          "driveType": "block",
          "nodeID": 4,
          "reservedSliceFileCapacity": 0,
          "serial": "scsi-SATA_INTEL_SSDSA2BW3CVPR120504U8300EGN",
          "slot": 2
        },
        "drives": [
          {
            "assignedService": 20,
            "asyncResultIDs": [],
            "attributes": {},
            "capacity": 300069052416,
            "customerSliceFileCapacity": 0,
            "driveID": 4,
            "driveStatus": "assigned",
            "driveType": "Block",
            "nodeID": 4,
            "reservedSliceFileCapacity": 0,
            "serial": "scsi-SATA_INTEL_SSDSA2BW3CVPR120504U8300EGN",
            "slot": 2
          }
        ],
        "node": {
          "associatedFServiceID": 0,
          "associatedMasterServiceID": 3,
          "attributes": {},
          "cip": "10.117.62.26",
          "cipi": "Bond10G",
          "fibreChannelTargetPortGroup": null,
          "mip": "10.117.60.26",
          "mipi": "Bond1G",
          "name": "SF-1713",
          "nodeID": 4,
          "platformInfo": {
            "chassisType": "R620",
            "cpuModel": "Intel(R) Xeon(R) CPU E5-2640 0 @ 2.50GHz",
            "nodeMemoryGB": 72,
            "nodeType": "SF3010"
          },
          "sip": "10.117.62.26",
          "sipi": "Bond10G",
          "softwareVersion": "9.0.0.1554",
          "uuid": "4C4C4544-0053-3210-8054-B6C04F435831",
          "virtualNetworks": []
        },
        "service": {
          "associatedBV": 0,
          "associatedTS": 0,
          "associatedVS": 0,
          "asyncResultIDs": [],
          "driveID": 4,
          "driveIDs": [
            4
          ],
          "firstTimeStartup": false,
          "ipcPort": 4007,
          "iscsiPort": 0,
          "nodeID": 4,
          "serviceID": 20,
          "serviceType": "block",
          "startedDriveIDs": [
            4
          ],
          "status": "healthy"
        }
      },
      {
        "drive": {
          "assignedService": 21,
          "asyncResultIDs": [],
          "attributes": {},
          "capacity": 300069052416,
          "customerSliceFileCapacity": 0,
          "driveID": 16,
          "driveStatus": "assigned",
          "driveType": "block",
          "nodeID": 3,
          "reservedSliceFileCapacity": 0,
          "serial": "scsi-SATA_INTEL_SSDSC2BB3BTWL311604K4300PGN",
          "slot": 3
        },
        "drives": [
          {
            "assignedService": 21,
            "asyncResultIDs": [],
            "attributes": {},
            "capacity": 300069052416,
            "customerSliceFileCapacity": 0,
            "driveID": 16,
            "driveStatus": "assigned",
            "driveType": "Block",
            "nodeID": 3,
            "reservedSliceFileCapacity": 0,
            "serial": "scsi-SATA_INTEL_SSDSC2BB3BTWL311604K4300PGN",
            "slot": 3
          }
        ],
        "node": {
          "associatedFServiceID": 0,
          "associatedMasterServiceID": 4,
          "attributes": {},
          "cip": "10.117.62.25",
          "cipi": "Bond10G",
          "fibreChannelTargetPortGroup": null,
          "mip": "10.117.60.25",
          "mipi": "Bond1G",
          "name": "SF-F2A3",
          "nodeID": 3,
          "platformInfo": {
            "chassisType": "R620",
            "cpuModel": "Intel(R) Xeon(R) CPU E5-2640 0 @ 2.50GHz",
            "nodeMemoryGB": 72,
            "nodeType": "SF3010"
          },
          "sip": "10.117.62.25",
          "sipi": "Bond10G",
          "softwareVersion": "9.0.0.1554",
          "uuid": "4C4C4544-0053-3310-8053-B6C04F435831",
          "virtualNetworks": []
        },
        "service": {
          "associatedBV": 0,
          "associatedTS": 0,
          "associatedVS": 0,
          "asyncResultIDs": [],
          "driveID": 16,
          "driveIDs": [
            16
          ],
          "firstTimeStartup": false,
          "ipcPort": 4008,
          "iscsiPort": 0,
          "nodeID": 3,
          "serviceID": 21,
          "serviceType": "block",
          "startedDriveIDs": [
            16
          ],
          "status": "healthy"
        }
      }
    ]
  }
}"""

RESP_ListSnapshots_v8_0 = """{
   "result":{
      "snapshots":[
         {
            "checksum":"0x0",
            "totalSize":1000341504,
            "enableRemoteReplication":false,
            "virtualVolumeID":null,
            "snapshotUUID":"c78bf699-3b5d-4ba2-9558-72ded9a71257",
            "volumeID":6452,
            "groupID":0,
            "status":"done",
            "expirationReason":"None",
            "expirationTime":"2017-01-13T16:07:36Z",
            "snapshotID":8136,
            "attributes":{
               "I-kR4TX":[
                  10,
                  null,
                  null
               ],
               "A":0,
               "G":0,
               "iHa":false,
               "Inhs":true,
               "dlu7bRB":"c",
               "cvY":[
                  "UBENLzSc",
                  "pNYx7nqnlYfsL3qwHZ56QwhfMlyAEL"
               ],
               "UYFbeo71R":"uGv",
               "vjnqWRl8":[
                  "bQB-divhKM0gu2",
                  5,
                  "ouSU1mL5e3Rg6ECiaShhQPaou",
                  1,
                  6,
                  "pyKXI0aVu2ud"
               ],
               "KTSi":[
                  4,
                  9,
                  4,
                  2,
                  7,
                  1,
                  0
               ]
            },
            "createTime":"2017-01-13T16:06:36Z",
            "name":"haxepyBR2J5nx4-Rv-Q8Xe704OWucxrNMHmBKalCRrlzbjGu7Fri-F6A1om9l1qU",
            "groupSnapshotUUID":"00000000-0000-0000-0000-000000000000"
         }
      ]
   },
   "id":2152
}"""

RESP_ListSnapshots_v9_0 = """{
   "id":9,
   "result":{
      "snapshots":[
         {
            "attributes":{
               "SRA_SYNCONCE":"cb44f772-bb26-40f8-ab3b-8577282eb785"
            },
            "checksum":"0xc683fe2c00e085c3",
            "createTime":"2016-12-06T22:49:03Z",
            "enableRemoteReplication":true,
            "expirationReason":"None",
            "expirationTime":"2016-12-07T22:49:03Z",
            "groupID":0,
            "groupSnapshotUUID":"00000000-0000-0000-0000-000000000000",
            "name":"2016-12-06T22:49:03Z",
            "remoteStatuses":[
               {
                  "remoteStatus":"Syncing",
                  "volumePairUUID":"cb44f772-bb26-40f8-ab3b-8577282eb785"
               }
            ],
            "snapshotID":2235,
            "snapshotUUID":"db5633bc-d1e8-4674-b598-d58a3f265167",
            "status":"done",
            "totalSize":20000538624,
            "virtualVolumeID":null,
            "volumeID":4
         }
      ]
   }
}"""

RESP_ListVirtualVolumeBindings_v9_0 = """{
  "id": 1,
  "result": {
    "bindings": [
      {
        "protocolEndpointID": "5dd53da0-b9b7-43f9-9b7e-b41c2558e92b",
        "protocolEndpointInBandID": "naa.6f47acc2000000016a67746700000000",
        "protocolEndpointType": "SCSI",
        "virtualVolumeBindingID": 177,
        "virtualVolumeHostID": "564de1a4-9a99-da0f-8b7c-3a41dfd64bf1",
        "virtualVolumeID": "269d3378-1ca6-4175-a18f-6d4839e5c746",
        "virtualVolumeSecondaryID": "0xe200000000a6"
      }
    ]
  }
}"""

RESP_ListVirtualVolumeHosts_v9_0 = """{
  "id": 1,
  "result": {
    "hosts": [
      {
        "bindings": [],
        "clusterID": "5ebdb4ad-9617-4647-adfd-c1013578483b",
        "hostAddress": "172.30.89.117",
        "initiatorNames": [
          "iqn.1998-01.com.vmware:zdc-dhcp-0-c-29-d6-4b-f1-1a0cd614",
          "iqn.1998-01.com.vmware:zdc-dhcp-0-c-29-d6-4b-f1-5bcf9254"
        ],
        "virtualVolumeHostID": "564de1a4-9a99-da0f-8b7c-3a41dfd64bf1",
        "visibleProtocolEndpointIDs": [
          "5dd53da0-b9b7-43f9-9b7e-b41c2558e92b"
        ]
      }
    ]
  }
}"""

RESP_ListVirtualVolumes_v9_0 = """{
  "id": 1,
  "result": {
    "nextVirtualVolumeID": "00000000-0000-0000-0000-000000000000",
    "virtualVolumes": [
      {
        "bindings": [
          177
        ],
        "children": [],
        "metadata": {
          "SFProfileId": "f4e5bade-15a2-4805-bf8e-52318c4ce443",
          "SFgenerationId": "0",
          "VMW_ContainerId": "abaab415-bedc-44cd-98b8-f37495884db0",
          "VMW_VVolName": "asdf",
          "VMW_VVolType": "Config",
          "VMW_VmID": "502e0676-e510-ccdd-394c-667f6867fcdf",
          "VMW_VvolProfile": "f4e5bade-15a2-4805-bf8e-52318c4ce443:0"
        },
        "parentVirtualVolumeID": "00000000-0000-0000-0000-000000000000",
        "snapshotID": 0,
        "snapshotInfo": null,
        "status": "done",
        "storageContainer": {
          "accountID": 1,
          "initiatorSecret": "B5)D1y10K)8IDN58",
          "name": "test",
          "protocolEndpointType": "SCSI",
          "status": "active",
          "storageContainerID": "abaab415-bedc-44cd-98b8-f37495884db0",
          "targetSecret": "qgae@{o{~82U)U^"
        },
        "virtualVolumeID": "269d3378-1ca6-4175-a18f-6d4839e5c746",
        "virtualVolumeType": "config",
        "volumeID": 166,
        "volumeInfo": null
      }
    ]
  }
}"""

RESP_ListVirtualVolumes_v9_1 = """{"id":2,"result":{"nextVirtualVolumeID":"00000000-0000-0000-0000-000000000000","virtualVolumes":[{"bindings":[],"children":[],"metadata":{"SFGenerationId":"0","SFProfileId":"f4e5bade-15a2-4805-bf8e-52318c4ce443","VMW_ContainerId":"f8ee427e-f858-420d-bd38-762ad1cb6cc3","VMW_GosType":"windows7Server64Guest","VMW_VVolName":"VM1_3.vmdk","VMW_VVolNamespace":"/vmfs/volumes/vvol:f8ee427ef858420d-bd38762ad1cb6cc3/rfc4122.5630cccd-0bc5-4fcd-a4d7-6f5d66da295a","VMW_VVolType":"Data","VMW_VmID":"50071f6b-2c72-50c7-eec9-f7e2bfb6f2f2","VMW_VvolAllocationType":"4","VMW_VvolProfile":"f4e5bade-15a2-4805-bf8e-52318c4ce443:0"},"parentVirtualVolumeID":"00000000-0000-0000-0000-000000000000","snapshotID":0,"snapshotInfo":null,"status":"done","storageContainer":{"accountID":2,"initiatorSecret":"0&%Q2f$61(3#1TX%","name":"akcluster1","protocolEndpointType":"SCSI","status":"active","storageContainerID":"f8ee427e-f858-420d-bd38-762ad1cb6cc3","targetSecret":"[]6~98n1ltWn<cl%"},"virtualVolumeID":"10c24f95-336d-4173-a19f-93ffbd852585","virtualVolumeType":"data","volumeID":6,"volumeInfo":null},{"bindings":[38],"children":[],"metadata":{"SFGenerationId":"0","SFProfileId":"f4e5bade-15a2-4805-bf8e-52318c4ce443","VMW_ContainerId":"76bbb2b4-8936-4c98-814d-d16f9249c156","VMW_GosType":"winNetEnterpriseGuest","VMW_VVolName":"ErikVM001.vmdk","VMW_VVolNamespace":"/vmfs/volumes/vvol:76bbb2b489364c98-814dd16f9249c156/rfc4122.1e09b208-80ee-43fa-8dad-6ffc2a013072","VMW_VVolType":"Data","VMW_VmID":"5007856a-7a81-92a8-3bcf-979c4fbab711","VMW_VvolAllocationType":"4","VMW_VvolProfile":"f4e5bade-15a2-4805-bf8e-52318c4ce443:0"},"parentVirtualVolumeID":"00000000-0000-0000-0000-000000000000","snapshotID":0,"snapshotInfo":null,"status":"done","storageContainer":{"accountID":4,"initiatorSecret":"n]shaq.ju!z>5{0X","name":"ErikSC","protocolEndpointType":"SCSI","status":"active","storageContainerID":"76bbb2b4-8936-4c98-814d-d16f9249c156","targetSecret":"037<BCYs^|iB%y,b"},"virtualVolumeID":"1dfe1cb3-bdd6-4051-a92c-43a0184d483d","virtualVolumeType":"data","volumeID":13,"volumeInfo":null},{"bindings":[36],"children":[],"metadata":{"SFGenerationId":"0","SFProfileId":"f4e5bade-15a2-4805-bf8e-52318c4ce443","VMW_ContainerId":"76bbb2b4-8936-4c98-814d-d16f9249c156","VMW_VVolName":"ErikVM001","VMW_VVolType":"Config","VMW_VmID":"5007856a-7a81-92a8-3bcf-979c4fbab711","VMW_VvolProfile":"f4e5bade-15a2-4805-bf8e-52318c4ce443:0"},"parentVirtualVolumeID":"00000000-0000-0000-0000-000000000000","snapshotID":0,"snapshotInfo":null,"status":"done","storageContainer":{"accountID":4,"initiatorSecret":"n]shaq.ju!z>5{0X","name":"ErikSC","protocolEndpointType":"SCSI","status":"active","storageContainerID":"76bbb2b4-8936-4c98-814d-d16f9249c156","targetSecret":"037<BCYs^|iB%y,b"},"virtualVolumeID":"1e09b208-80ee-43fa-8dad-6ffc2a013072","virtualVolumeType":"config","volumeID":12,"volumeInfo":null},{"bindings":[],"children":[],"metadata":{"SFGenerationId":"0","SFProfileId":"f4e5bade-15a2-4805-bf8e-52318c4ce443","VMW_ContainerId":"f8ee427e-f858-420d-bd38-762ad1cb6cc3","VMW_GosType":"windows7Server64Guest","VMW_VVolName":"VM1_1.vmdk","VMW_VVolNamespace":"/vmfs/volumes/vvol:f8ee427ef858420d-bd38762ad1cb6cc3/rfc4122.5630cccd-0bc5-4fcd-a4d7-6f5d66da295a","VMW_VVolType":"Data","VMW_VmID":"50071f6b-2c72-50c7-eec9-f7e2bfb6f2f2","VMW_VvolAllocationType":"4","VMW_VvolProfile":"f4e5bade-15a2-4805-bf8e-52318c4ce443:0"},"parentVirtualVolumeID":"00000000-0000-0000-0000-000000000000","snapshotID":0,"snapshotInfo":null,"status":"done","storageContainer":{"accountID":2,"initiatorSecret":"0&%Q2f$61(3#1TX%","name":"akcluster1","protocolEndpointType":"SCSI","status":"active","storageContainerID":"f8ee427e-f858-420d-bd38-762ad1cb6cc3","targetSecret":"[]6~98n1ltWn<cl%"},"virtualVolumeID":"25081b2e-0656-428d-b4a3-6dddb0255d51","virtualVolumeType":"data","volumeID":4,"volumeInfo":null},{"bindings":[],"children":[],"metadata":{"SFGenerationId":"0","SFProfileId":"f4e5bade-15a2-4805-bf8e-52318c4ce443","VMW_ContainerId":"f8ee427e-f858-420d-bd38-762ad1cb6cc3","VMW_GosType":"windows7Server64Guest","VMW_VVolName":"VM1.vmdk","VMW_VVolNamespace":"/vmfs/volumes/vvol:f8ee427ef858420d-bd38762ad1cb6cc3/rfc4122.5630cccd-0bc5-4fcd-a4d7-6f5d66da295a","VMW_VVolType":"Data","VMW_VmID":"50071f6b-2c72-50c7-eec9-f7e2bfb6f2f2","VMW_VvolAllocationType":"4","VMW_VvolProfile":"f4e5bade-15a2-4805-bf8e-52318c4ce443:0"},"parentVirtualVolumeID":"00000000-0000-0000-0000-000000000000","snapshotID":0,"snapshotInfo":null,"status":"done","storageContainer":{"accountID":2,"initiatorSecret":"0&%Q2f$61(3#1TX%","name":"akcluster1","protocolEndpointType":"SCSI","status":"active","storageContainerID":"f8ee427e-f858-420d-bd38-762ad1cb6cc3","targetSecret":"[]6~98n1ltWn<cl%"},"virtualVolumeID":"4a2fa09f-8eb7-4151-be39-27bae2f8100f","virtualVolumeType":"data","volumeID":3,"volumeInfo":null},{"bindings":[],"children":[],"metadata":{"SFGenerationId":"0","SFProfileId":"f4e5bade-15a2-4805-bf8e-52318c4ce443","VMW_ContainerId":"f8ee427e-f858-420d-bd38-762ad1cb6cc3","VMW_VVolName":"VM1","VMW_VVolType":"Config","VMW_VmID":"50071f6b-2c72-50c7-eec9-f7e2bfb6f2f2","VMW_VvolProfile":"f4e5bade-15a2-4805-bf8e-52318c4ce443:0"},"parentVirtualVolumeID":"00000000-0000-0000-0000-000000000000","snapshotID":0,"snapshotInfo":null,"status":"done","storageContainer":{"accountID":2,"initiatorSecret":"0&%Q2f$61(3#1TX%","name":"akcluster1","protocolEndpointType":"SCSI","status":"active","storageContainerID":"f8ee427e-f858-420d-bd38-762ad1cb6cc3","targetSecret":"[]6~98n1ltWn<cl%"},"virtualVolumeID":"5630cccd-0bc5-4fcd-a4d7-6f5d66da295a","virtualVolumeType":"config","volumeID":2,"volumeInfo":null},{"bindings":[],"children":[],"metadata":{"SFGenerationId":"0","SFProfileId":"f4e5bade-15a2-4805-bf8e-52318c4ce443","VMW_ContainerId":"f8ee427e-f858-420d-bd38-762ad1cb6cc3","VMW_VVolName":"vvolVM1","VMW_VVolType":"Config","VMW_VmID":"50073c1f-e7d7-88be-4c13-8ef84026ffb1","VMW_VvolProfile":"f4e5bade-15a2-4805-bf8e-52318c4ce443:0"},"parentVirtualVolumeID":"00000000-0000-0000-0000-000000000000","snapshotID":0,"snapshotInfo":null,"status":"done","storageContainer":{"accountID":2,"initiatorSecret":"0&%Q2f$61(3#1TX%","name":"akcluster1","protocolEndpointType":"SCSI","status":"active","storageContainerID":"f8ee427e-f858-420d-bd38-762ad1cb6cc3","targetSecret":"[]6~98n1ltWn<cl%"},"virtualVolumeID":"6664a13e-a525-47a2-a58b-47231a5ecfea","virtualVolumeType":"config","volumeID":8,"volumeInfo":null},{"bindings":[37],"children":[],"metadata":{"SFGenerationId":"0","SFProfileId":"7508ed62-e4a9-4cf1-9ef9-fb1f07b72bc1","VMW_ContainerId":"76bbb2b4-8936-4c98-814d-d16f9249c156","VMW_GosType":"winNetEnterpriseGuest","VMW_VVolName":"ErikVM001-59835ac3.vswp","VMW_VVolNamespace":"/vmfs/volumes/vvol:76bbb2b489364c98-814dd16f9249c156/rfc4122.1e09b208-80ee-43fa-8dad-6ffc2a013072","VMW_VVolType":"Swap","VMW_VmID":"5007856a-7a81-92a8-3bcf-979c4fbab711","VMW_VvolAllocationType":"3","VMW_VvolProfile":"7508ed62-e4a9-4cf1-9ef9-fb1f07b72bc1:0"},"parentVirtualVolumeID":"00000000-0000-0000-0000-000000000000","snapshotID":0,"snapshotInfo":null,"status":"done","storageContainer":{"accountID":4,"initiatorSecret":"n]shaq.ju!z>5{0X","name":"ErikSC","protocolEndpointType":"SCSI","status":"active","storageContainerID":"76bbb2b4-8936-4c98-814d-d16f9249c156","targetSecret":"037<BCYs^|iB%y,b"},"virtualVolumeID":"8182ae66-7cdb-4df4-be00-e1b93a5b8364","virtualVolumeType":"swap","volumeID":14,"volumeInfo":null},{"bindings":[],"children":[],"metadata":{"SFGenerationId":"0","SFProfileId":"f4e5bade-15a2-4805-bf8e-52318c4ce443","VMW_ContainerId":"f8ee427e-f858-420d-bd38-762ad1cb6cc3","VMW_GosType":"rhel7_64Guest","VMW_VVolName":"vvolVM1.vmdk","VMW_VVolNamespace":"/vmfs/volumes/vvol:f8ee427ef858420d-bd38762ad1cb6cc3/rfc4122.6664a13e-a525-47a2-a58b-47231a5ecfea","VMW_VVolType":"Data","VMW_VmID":"50073c1f-e7d7-88be-4c13-8ef84026ffb1","VMW_VvolAllocationType":"4","VMW_VvolProfile":"f4e5bade-15a2-4805-bf8e-52318c4ce443:0"},"parentVirtualVolumeID":"00000000-0000-0000-0000-000000000000","snapshotID":0,"snapshotInfo":null,"status":"done","storageContainer":{"accountID":2,"initiatorSecret":"0&%Q2f$61(3#1TX%","name":"akcluster1","protocolEndpointType":"SCSI","status":"active","storageContainerID":"f8ee427e-f858-420d-bd38-762ad1cb6cc3","targetSecret":"[]6~98n1ltWn<cl%"},"virtualVolumeID":"83345d1c-70ab-4d99-8177-d96f67570594","virtualVolumeType":"data","volumeID":9,"volumeInfo":null},{"bindings":[],"children":[],"metadata":{"SFGenerationId":"0","SFProfileId":"f4e5bade-15a2-4805-bf8e-52318c4ce443","VMW_ContainerId":"f8ee427e-f858-420d-bd38-762ad1cb6cc3","VMW_GosType":"windows7Server64Guest","VMW_VVolName":"VM1_2.vmdk","VMW_VVolNamespace":"/vmfs/volumes/vvol:f8ee427ef858420d-bd38762ad1cb6cc3/rfc4122.5630cccd-0bc5-4fcd-a4d7-6f5d66da295a","VMW_VVolType":"Data","VMW_VmID":"50071f6b-2c72-50c7-eec9-f7e2bfb6f2f2","VMW_VvolAllocationType":"4","VMW_VvolProfile":"f4e5bade-15a2-4805-bf8e-52318c4ce443:0"},"parentVirtualVolumeID":"00000000-0000-0000-0000-000000000000","snapshotID":0,"snapshotInfo":null,"status":"done","storageContainer":{"accountID":2,"initiatorSecret":"0&%Q2f$61(3#1TX%","name":"akcluster1","protocolEndpointType":"SCSI","status":"active","storageContainerID":"f8ee427e-f858-420d-bd38-762ad1cb6cc3","targetSecret":"[]6~98n1ltWn<cl%"},"virtualVolumeID":"c983e671-23dd-45a1-9b7e-9b4f94c13534","virtualVolumeType":"data","volumeID":5,"volumeInfo":null}]}}"""

RESP_ListVirtualVolumeTasks_v9_0 = """{
  "id": 1,
  "result": {
    "tasks": [
      {
        "cancelled": false,
        "cloneVirtualVolumeID": "fafeb3a0-7dd9-4c9f-8a07-80e0bbf6f4d0",
        "operation": "clone",
        "parentMetadata": {
          "SFProfileId": "f4e5bade-15a2-4805-bf8e-52318c4ce443",
          "SFgenerationId": "0",
          "VMW_ContainerId": "abaab415-bedc-44cd-98b8-f37495884db0",
          "VMW_GosType": "windows7Server64Guest",
          "VMW_VVolName": "asdf.vmdk",
          "VMW_VVolNamespace": "/vmfs/volumes/vvol:abaab415bedc44cd-98b8f37495884db0/rfc4122.269d3378-1ca6-4175-a18f-6d4839e5c746",
          "VMW_VVolType": "Data",
          "VMW_VmID": "502e0676-e510-ccdd-394c-667f6867fcdf",
          "VMW_VvolAllocationType": "4",
          "VMW_VvolProfile": "f4e5bade-15a2-4805-bf8e-52318c4ce443:0"
        },
        "parentTotalSize": 42949672960,
        "parentUsedSize": 0,
        "status": "success",
        "virtualVolumeHostID": "564de1a4-9a99-da0f-8b7c-3a41dfd64bf1",
        "virtualVolumeTaskID": "a1b72df7-66a6-489a-86e4-538d0dbe05bf",
        "virtualvolumeID": "fafeb3a0-7dd9-4c9f-8a07-80e0bbf6f4d0"
      }
    ]
  }
}"""

RESP_ListVolumeAccessGroups_v9_0 = """{
  "id": 1,
  "result": {
    "volumeAccessGroups": [
      {
        "attributes": {},
        "deletedVolumes": [],
        "initiatorIDs": [
          1
        ],
        "initiators": [
          "iqn.1998-01.com.vmware:sra-site1-esxi"
        ],
        "name": "sra-site1-esxi",
        "volumeAccessGroupID": 1,
        "volumes": [
          2,
          4
        ]
      },
      {
        "attributes": {},
        "deletedVolumes": [],
        "initiatorIDs": [
          4,
          5
        ],
        "initiators": [
          "21:00:00:0e:1e:1b:2a:40",
          "21:00:00:0e:1e:1b:2a:41"
        ],
        "name": "loyds",
        "volumeAccessGroupID": 2,
        "volumes": [
          5
        ]
      }
    ]
  }
}"""

RESP_ListVolumeStatsByVirtualVolume_v9_0 = """{"id":1,"result":{"volumeStats":[]}}"""

RESP_ListVolumeStatsByVirtualVolume_v9_1 = """{"id":1,"result":{"volumeStats":[{"accountID":2,"actualIOPS":0,"asyncDelay":null,"averageIOPSize":0,"burstIOPSCredit":0,"clientQueueDepth":0,"desiredMetadataHosts":null,"latencyUSec":0,"metadataHosts":{"deadSecondaries":[],"liveSecondaries":[],"primary":5},"nonZeroBlocks":0,"readBytes":0,"readBytesLastSample":0,"readLatencyUSec":0,"readOps":0,"readOpsLastSample":0,"samplePeriodMSec":0,"throttle":0,"timestamp":"2016-11-22T18:06:08.851768Z","unalignedReads":0,"unalignedWrites":0,"virtualVolumeID":"10c24f95-336d-4173-a19f-93ffbd852585","volumeAccessGroups":[],"volumeID":6,"volumeSize":4294967296,"volumeUtilization":0,"writeBytes":0,"writeBytesLastSample":0,"writeLatencyUSec":0,"writeOps":0,"writeOpsLastSample":0,"zeroBlocks":1048576},{"accountID":4,"actualIOPS":0,"asyncDelay":null,"averageIOPSize":0,"burstIOPSCredit":0,"clientQueueDepth":0,"desiredMetadataHosts":null,"latencyUSec":0,"metadataHosts":{"deadSecondaries":[],"liveSecondaries":[],"primary":5},"nonZeroBlocks":0,"readBytes":512,"readBytesLastSample":0,"readLatencyUSec":0,"readOps":1,"readOpsLastSample":0,"samplePeriodMSec":0,"throttle":0,"timestamp":"2016-11-22T18:06:08.862264Z","unalignedReads":1,"unalignedWrites":0,"virtualVolumeID":"1dfe1cb3-bdd6-4051-a92c-43a0184d483d","volumeAccessGroups":[],"volumeID":13,"volumeSize":8589934592,"volumeUtilization":0,"writeBytes":0,"writeBytesLastSample":0,"writeLatencyUSec":0,"writeOps":0,"writeOpsLastSample":0,"zeroBlocks":2097152},{"accountID":4,"actualIOPS":0,"asyncDelay":null,"averageIOPSize":512,"burstIOPSCredit":0,"clientQueueDepth":0,"desiredMetadataHosts":null,"latencyUSec":0,"metadataHosts":{"deadSecondaries":[],"liveSecondaries":[],"primary":5},"nonZeroBlocks":1447,"readBytes":2517504,"readBytesLastSample":0,"readLatencyUSec":0,"readOps":587,"readOpsLastSample":0,"samplePeriodMSec":500,"throttle":0,"timestamp":"2016-11-22T18:06:08.872020Z","unalignedReads":557,"unalignedWrites":5879,"virtualVolumeID":"1e09b208-80ee-43fa-8dad-6ffc2a013072","volumeAccessGroups":[],"volumeID":12,"volumeSize":4294967296,"volumeUtilization":0,"writeBytes":15736832,"writeBytesLastSample":0,"writeLatencyUSec":0,"writeOps":6046,"writeOpsLastSample":0,"zeroBlocks":1047129},{"accountID":2,"actualIOPS":0,"asyncDelay":null,"averageIOPSize":0,"burstIOPSCredit":0,"clientQueueDepth":0,"desiredMetadataHosts":null,"latencyUSec":0,"metadataHosts":{"deadSecondaries":[],"liveSecondaries":[],"primary":5},"nonZeroBlocks":0,"readBytes":0,"readBytesLastSample":0,"readLatencyUSec":0,"readOps":0,"readOpsLastSample":0,"samplePeriodMSec":0,"throttle":0,"timestamp":"2016-11-22T18:06:08.882931Z","unalignedReads":0,"unalignedWrites":0,"virtualVolumeID":"25081b2e-0656-428d-b4a3-6dddb0255d51","volumeAccessGroups":[],"volumeID":4,"volumeSize":4294967296,"volumeUtilization":0,"writeBytes":0,"writeBytesLastSample":0,"writeLatencyUSec":0,"writeOps":0,"writeOpsLastSample":0,"zeroBlocks":1048576},{"accountID":2,"actualIOPS":0,"asyncDelay":null,"averageIOPSize":0,"burstIOPSCredit":0,"clientQueueDepth":0,"desiredMetadataHosts":null,"latencyUSec":0,"metadataHosts":{"deadSecondaries":[],"liveSecondaries":[],"primary":5},"nonZeroBlocks":0,"readBytes":0,"readBytesLastSample":0,"readLatencyUSec":0,"readOps":0,"readOpsLastSample":0,"samplePeriodMSec":0,"throttle":0,"timestamp":"2016-11-22T18:06:08.893663Z","unalignedReads":0,"unalignedWrites":0,"virtualVolumeID":"4a2fa09f-8eb7-4151-be39-27bae2f8100f","volumeAccessGroups":[],"volumeID":3,"volumeSize":5368709120,"volumeUtilization":0,"writeBytes":0,"writeBytesLastSample":0,"writeLatencyUSec":0,"writeOps":0,"writeOpsLastSample":0,"zeroBlocks":1310720},{"accountID":2,"actualIOPS":0,"asyncDelay":null,"averageIOPSize":0,"burstIOPSCredit":0,"clientQueueDepth":0,"desiredMetadataHosts":null,"latencyUSec":0,"metadataHosts":{"deadSecondaries":[],"liveSecondaries":[],"primary":5},"nonZeroBlocks":1414,"readBytes":9278464,"readBytesLastSample":0,"readLatencyUSec":0,"readOps":3667,"readOpsLastSample":0,"samplePeriodMSec":0,"throttle":0,"timestamp":"2016-11-22T18:06:08.904266Z","unalignedReads":3541,"unalignedWrites":4210,"virtualVolumeID":"5630cccd-0bc5-4fcd-a4d7-6f5d66da295a","volumeAccessGroups":[],"volumeID":2,"volumeSize":4294967296,"volumeUtilization":0,"writeBytes":12729344,"writeBytesLastSample":0,"writeLatencyUSec":0,"writeOps":4373,"writeOpsLastSample":0,"zeroBlocks":1047162},{"accountID":2,"actualIOPS":0,"asyncDelay":null,"averageIOPSize":0,"burstIOPSCredit":0,"clientQueueDepth":0,"desiredMetadataHosts":null,"latencyUSec":0,"metadataHosts":{"deadSecondaries":[],"liveSecondaries":[],"primary":5},"nonZeroBlocks":1407,"readBytes":1610752,"readBytesLastSample":0,"readLatencyUSec":0,"readOps":462,"readOpsLastSample":0,"samplePeriodMSec":0,"throttle":0,"timestamp":"2016-11-22T18:06:08.915110Z","unalignedReads":438,"unalignedWrites":1200,"virtualVolumeID":"6664a13e-a525-47a2-a58b-47231a5ecfea","volumeAccessGroups":[],"volumeID":8,"volumeSize":4294967296,"volumeUtilization":0,"writeBytes":10829824,"writeBytesLastSample":0,"writeLatencyUSec":0,"writeOps":1351,"writeOpsLastSample":0,"zeroBlocks":1047169},{"accountID":4,"actualIOPS":0,"asyncDelay":null,"averageIOPSize":0,"burstIOPSCredit":0,"clientQueueDepth":0,"desiredMetadataHosts":null,"latencyUSec":0,"metadataHosts":{"deadSecondaries":[],"liveSecondaries":[],"primary":5},"nonZeroBlocks":0,"readBytes":0,"readBytesLastSample":0,"readLatencyUSec":0,"readOps":0,"readOpsLastSample":0,"samplePeriodMSec":0,"throttle":0,"timestamp":"2016-11-22T18:06:08.925641Z","unalignedReads":0,"unalignedWrites":0,"virtualVolumeID":"8182ae66-7cdb-4df4-be00-e1b93a5b8364","volumeAccessGroups":[],"volumeID":14,"volumeSize":2147483648,"volumeUtilization":0,"writeBytes":0,"writeBytesLastSample":0,"writeLatencyUSec":0,"writeOps":0,"writeOpsLastSample":0,"zeroBlocks":524288},{"accountID":2,"actualIOPS":0,"asyncDelay":null,"averageIOPSize":0,"burstIOPSCredit":0,"clientQueueDepth":0,"desiredMetadataHosts":null,"latencyUSec":0,"metadataHosts":{"deadSecondaries":[],"liveSecondaries":[],"primary":5},"nonZeroBlocks":0,"readBytes":0,"readBytesLastSample":0,"readLatencyUSec":0,"readOps":0,"readOpsLastSample":0,"samplePeriodMSec":0,"throttle":0,"timestamp":"2016-11-22T18:06:08.935746Z","unalignedReads":0,"unalignedWrites":0,"virtualVolumeID":"83345d1c-70ab-4d99-8177-d96f67570594","volumeAccessGroups":[],"volumeID":9,"volumeSize":10737418240,"volumeUtilization":0,"writeBytes":0,"writeBytesLastSample":0,"writeLatencyUSec":0,"writeOps":0,"writeOpsLastSample":0,"zeroBlocks":2621440},{"accountID":2,"actualIOPS":0,"asyncDelay":null,"averageIOPSize":0,"burstIOPSCredit":0,"clientQueueDepth":0,"desiredMetadataHosts":null,"latencyUSec":0,"metadataHosts":{"deadSecondaries":[],"liveSecondaries":[],"primary":5},"nonZeroBlocks":0,"readBytes":0,"readBytesLastSample":0,"readLatencyUSec":0,"readOps":0,"readOpsLastSample":0,"samplePeriodMSec":0,"throttle":0,"timestamp":"2016-11-22T18:06:08.946487Z","unalignedReads":0,"unalignedWrites":0,"virtualVolumeID":"c983e671-23dd-45a1-9b7e-9b4f94c13534","volumeAccessGroups":[],"volumeID":5,"volumeSize":4294967296,"volumeUtilization":0,"writeBytes":0,"writeBytesLastSample":0,"writeLatencyUSec":0,"writeOps":0,"writeOpsLastSample":0,"zeroBlocks":1048576}]}}"""

RESP_ModifyStorageContainer_v9_0 = """{
  "id": null,
  "result": {
    "storageContainer": {
      "accountID": 114,
      "initiatorSecret": "e;~t5f4T~r8CQK9",
      "name": "ExampleName",
      "protocolEndpointType": "SCSI",
      "status": "active",
      "storageContainerID": "b4528ea8-2930-41a0-8b8e-6361e1f0a71f",
      "targetSecret": "LIU4?KW8mOlMZO^6"
    }
  }
}"""

RESP_ModifyVolumeAccessGroup_v9_0 = """{
  "id": null,
  "result": {
    "volumeAccessGroup": {
      "attributes": {},
      "deletedVolumes": [
        327
      ],
      "initiatorIDs": [
        114,
        115
      ],
      "initiators": [
        "iqn.1998-01.com.vmware:desk1-esx1-577b283a",
        "iqn.1998-01.com.vmware:donesq-esx1-421b281b"
      ],
      "name": "northbanktest",
      "volumeAccessGroupID": 96,
      "volumes": [
        346
      ]
    }
  }
}"""

RESP_ModifyVolumes_v9_0 = """{
  "id": 1,
  "result": {
    "volumes": [
      {
        "access": "replicationTarget",
        "accountID": 1,
        "attributes": {
          "name1": "value1",
          "name2": "value2",
          "name3": "value3"
        },
        "blockSize": 4096,
        "createTime": "2016-04-06T17:25:13Z",
        "deleteTime": "",
        "enable512e": false,
        "iqn": "iqn.2010-01.com.solidfire:jo73.2",
        "name": "doctest1",
        "purgeTime": "",
        "qos": {
          "burstIOPS": 150,
          "burstTime": 60,
          "curve": {
            "4096": 100,
            "8192": 160,
            "16384": 270,
            "32768": 500,
            "65536": 1000,
            "131072": 1950,
            "262144": 3900,
            "524288": 7600,
            "1048576": 15000
          },
          "maxIOPS": 100,
          "minIOPS": 50
        },
        "scsiEUIDeviceID": "6a6f373300000002f47acc0100000000",
        "scsiNAADeviceID": "6f47acc1000000006a6f373300000002",
        "sliceCount": 1,
        "status": "active",
        "totalSize": 1000341504,
        "virtualVolumeID": null,
        "volumeAccessGroups": [],
        "volumeID": 2,
        "volumePairs": []
      },
      {
        "access": "replicationTarget",
        "accountID": 1,
        "attributes": {
          "name1": "value1",
          "name2": "value2",
          "name3": "value3"
        },
        "blockSize": 4096,
        "createTime": "2016-04-06T17:26:31Z",
        "deleteTime": "",
        "enable512e": false,
        "iqn": "iqn.2010-01.com.solidfire:jo73.3",
        "name": "doctest2",
        "purgeTime": "",
        "qos": {
          "burstIOPS": 150,
          "burstTime": 60,
          "curve": {
            "4096": 100,
            "8192": 160,
            "16384": 270,
            "32768": 500,
            "65536": 1000,
            "131072": 1950,
            "262144": 3900,
            "524288": 7600,
            "1048576": 15000
          },
          "maxIOPS": 100,
          "minIOPS": 50
        },
        "scsiEUIDeviceID": "6a6f373300000003f47acc0100000000",
        "scsiNAADeviceID": "6f47acc1000000006a6f373300000003",
        "sliceCount": 1,
        "status": "active",
        "totalSize": 1000341504,
        "virtualVolumeID": null,
        "volumeAccessGroups": [],
        "volumeID": 3,
        "volumePairs": []
      }
    ]
  }
}"""

RESP_ModifyVolumes_v9_1 = """{"id":1642,"result":{"volumes":[{"access":"readWrite","accountID":8731,"attributes":{},"blockSize":4096,"createTime":"2016-11-22T15:40:16Z","deleteTime":"","enable512e":false,"iqn":"iqn.2010-01.com.solidfire:ixvl.haxecsl537c7lrxl7lrhgvduucobdg2w2e1ylcsoaxk8kdizntilduhsfp3jukbx.9980","name":"haxecsl537C7LrXL7lRHGvDuUCobdg2w2E1YLCsoAxk8KdiZNtILDuhsfP3jUKbX","purgeTime":"","qos":{"burstIOPS":15000,"burstTime":60,"curve":{"1048576":15000,"131072":1950,"16384":270,"262144":3900,"32768":500,"4096":100,"524288":7600,"65536":1000,"8192":160},"maxIOPS":15000,"minIOPS":50},"scsiEUIDeviceID":"6978766c000026fcf47acc0100000000","scsiNAADeviceID":"6f47acc1000000006978766c000026fc","sliceCount":1,"status":"active","totalSize":1000341504,"virtualVolumeID":null,"volumeAccessGroups":[],"volumeID":9980,"volumePairs":[]},{"access":"readWrite","accountID":8731,"attributes":{},"blockSize":4096,"createTime":"2016-11-22T15:40:16Z","deleteTime":"","enable512e":false,"iqn":"iqn.2010-01.com.solidfire:ixvl.haxecsksgcuvtr98nqedr-ajysgulerjep4onfwa11irehguokm-hay8r1-pbqgm.9981","name":"haxecsksGCuvTR98NqeDr-AJYSgUleRJEP4oNfWa11IrehGUOkM-hAY8r1-PbQGm","purgeTime":"","qos":{"burstIOPS":15000,"burstTime":60,"curve":{"1048576":15000,"131072":1950,"16384":270,"262144":3900,"32768":500,"4096":100,"524288":7600,"65536":1000,"8192":160},"maxIOPS":15000,"minIOPS":50},"scsiEUIDeviceID":"6978766c000026fdf47acc0100000000","scsiNAADeviceID":"6f47acc1000000006978766c000026fd","sliceCount":1,"status":"active","totalSize":1000341504,"virtualVolumeID":null,"volumeAccessGroups":[],"volumeID":9981,"volumePairs":[]},{"access":"readWrite","accountID":8731,"attributes":{},"blockSize":4096,"createTime":"2016-11-22T15:40:17Z","deleteTime":"","enable512e":false,"iqn":"iqn.2010-01.com.solidfire:ixvl.haxecsmcxwlmfmgvywbjqmkylkqu0jlzeubplb6n1egfsexlbw-af5-86g3yw2ny.9982","name":"haxecsMcXWLMFmGVYwBJQMKylKQU0jLZEubpLb6N1egfSeXLbw-aF5-86g3yW2ny","purgeTime":"","qos":{"burstIOPS":15000,"burstTime":60,"curve":{"1048576":15000,"131072":1950,"16384":270,"262144":3900,"32768":500,"4096":100,"524288":7600,"65536":1000,"8192":160},"maxIOPS":15000,"minIOPS":50},"scsiEUIDeviceID":"6978766c000026fef47acc0100000000","scsiNAADeviceID":"6f47acc1000000006978766c000026fe","sliceCount":1,"status":"active","totalSize":1000341504,"virtualVolumeID":null,"volumeAccessGroups":[],"volumeID":9982,"volumePairs":[]},{"access":"readWrite","accountID":8731,"attributes":{},"blockSize":4096,"createTime":"2016-11-22T15:40:17Z","deleteTime":"","enable512e":false,"iqn":"iqn.2010-01.com.solidfire:ixvl.haxecsmssext8u48vavvf4cglbhglepyfk-te6byasrhq2tsuu5aaqmfgtncbfho.9983","name":"haxecsmsseXt8U48VAvvF4cgLBhgLepyFk-Te6BYaSRHq2TSUU5AAQMFGtNcbFhO","purgeTime":"","qos":{"burstIOPS":15000,"burstTime":60,"curve":{"1048576":15000,"131072":1950,"16384":270,"262144":3900,"32768":500,"4096":100,"524288":7600,"65536":1000,"8192":160},"maxIOPS":15000,"minIOPS":50},"scsiEUIDeviceID":"6978766c000026fff47acc0100000000","scsiNAADeviceID":"6f47acc1000000006978766c000026ff","sliceCount":1,"status":"active","totalSize":1000341504,"virtualVolumeID":null,"volumeAccessGroups":[],"volumeID":9983,"volumePairs":[]},{"access":"readWrite","accountID":8731,"attributes":{},"blockSize":4096,"createTime":"2016-11-22T15:40:18Z","deleteTime":"","enable512e":false,"iqn":"iqn.2010-01.com.solidfire:ixvl.haxecs-ayusaaabjcugxreafnj49bb2zzvcezgsa6iuhwmn5y5ujy85zrjjp5b-8.9984","name":"haxecs-aYusaaABjCuGxReAFnJ49bb2zzvcEZGSa6iUHwmN5Y5uJy85Zrjjp5B-8","purgeTime":"","qos":{"burstIOPS":15000,"burstTime":60,"curve":{"1048576":15000,"131072":1950,"16384":270,"262144":3900,"32768":500,"4096":100,"524288":7600,"65536":1000,"8192":160},"maxIOPS":15000,"minIOPS":50},"scsiEUIDeviceID":"6978766c00002700f47acc0100000000","scsiNAADeviceID":"6f47acc1000000006978766c00002700","sliceCount":1,"status":"active","totalSize":1000341504,"virtualVolumeID":null,"volumeAccessGroups":[],"volumeID":9984,"volumePairs":[]},{"access":"readWrite","accountID":8731,"attributes":{},"blockSize":4096,"createTime":"2016-11-22T15:40:18Z","deleteTime":"","enable512e":false,"iqn":"iqn.2010-01.com.solidfire:ixvl.haxecs0gjuyyk7lxpbazniw4-4upylla6jcfgdaqr03aa67l-djyhuttrwl8alt8.9985","name":"haxecs0gjUYyK7LxpbAZnIw4-4upyllA6jcFGDAQr03aa67L-dJyhUTTrWL8ALt8","purgeTime":"","qos":{"burstIOPS":15000,"burstTime":60,"curve":{"1048576":15000,"131072":1950,"16384":270,"262144":3900,"32768":500,"4096":100,"524288":7600,"65536":1000,"8192":160},"maxIOPS":15000,"minIOPS":50},"scsiEUIDeviceID":"6978766c00002701f47acc0100000000","scsiNAADeviceID":"6f47acc1000000006978766c00002701","sliceCount":1,"status":"active","totalSize":1000341504,"virtualVolumeID":null,"volumeAccessGroups":[],"volumeID":9985,"volumePairs":[]},{"access":"readWrite","accountID":8731,"attributes":{},"blockSize":4096,"createTime":"2016-11-22T15:40:18Z","deleteTime":"","enable512e":false,"iqn":"iqn.2010-01.com.solidfire:ixvl.haxecswvs6txelqurcal1xh4zr9tfe2uczbtzshx-wl20asb1unbhzlt2njnsnqn.9986","name":"haxecsWVs6tXeLqUrcAl1xh4Zr9tFE2uCzBtZsHx-WL20ASb1unbHZlt2njNSnQn","purgeTime":"","qos":{"burstIOPS":15000,"burstTime":60,"curve":{"1048576":15000,"131072":1950,"16384":270,"262144":3900,"32768":500,"4096":100,"524288":7600,"65536":1000,"8192":160},"maxIOPS":15000,"minIOPS":50},"scsiEUIDeviceID":"6978766c00002702f47acc0100000000","scsiNAADeviceID":"6f47acc1000000006978766c00002702","sliceCount":1,"status":"active","totalSize":1000341504,"virtualVolumeID":null,"volumeAccessGroups":[],"volumeID":9986,"volumePairs":[]},{"access":"readWrite","accountID":8731,"attributes":{},"blockSize":4096,"createTime":"2016-11-22T15:40:19Z","deleteTime":"","enable512e":false,"iqn":"iqn.2010-01.com.solidfire:ixvl.haxecsd2gj0atoyd2muwrahxutzhlpmaevomwkg7kzwpzrkktduxzdduyztn4wqc.9987","name":"haxecsd2GJ0atOYD2MuwRAhxUtzHLpMAEvoMWKg7KZwpzrKktDUXZDduYZTn4Wqc","purgeTime":"","qos":{"burstIOPS":15000,"burstTime":60,"curve":{"1048576":15000,"131072":1950,"16384":270,"262144":3900,"32768":500,"4096":100,"524288":7600,"65536":1000,"8192":160},"maxIOPS":15000,"minIOPS":50},"scsiEUIDeviceID":"6978766c00002703f47acc0100000000","scsiNAADeviceID":"6f47acc1000000006978766c00002703","sliceCount":1,"status":"active","totalSize":1000341504,"virtualVolumeID":null,"volumeAccessGroups":[],"volumeID":9987,"volumePairs":[]},{"access":"readWrite","accountID":8731,"attributes":{},"blockSize":4096,"createTime":"2016-11-22T15:40:19Z","deleteTime":"","enable512e":false,"iqn":"iqn.2010-01.com.solidfire:ixvl.haxecsqrxv1xuyj6j9sxq1wrh-jsasgk0z1lmkvbgskmx52pcjwdyrygxaapv9qe.9988","name":"haxecsqrXv1xuyJ6J9SXQ1wrH-jsaSgK0Z1LMkvBgSKmx52pcjWdYrYGxaAPv9QE","purgeTime":"","qos":{"burstIOPS":15000,"burstTime":60,"curve":{"1048576":15000,"131072":1950,"16384":270,"262144":3900,"32768":500,"4096":100,"524288":7600,"65536":1000,"8192":160},"maxIOPS":15000,"minIOPS":50},"scsiEUIDeviceID":"6978766c00002704f47acc0100000000","scsiNAADeviceID":"6f47acc1000000006978766c00002704","sliceCount":1,"status":"active","totalSize":1000341504,"virtualVolumeID":null,"volumeAccessGroups":[],"volumeID":9988,"volumePairs":[]},{"access":"readWrite","accountID":8731,"attributes":{},"blockSize":4096,"createTime":"2016-11-22T15:40:20Z","deleteTime":"","enable512e":false,"iqn":"iqn.2010-01.com.solidfire:ixvl.haxecstmk7arat6lwxplmxajyptmuuqwyzzm7lokog44wihgez3uihp7z-yper21.9989","name":"haxecsTMk7ArAT6lwxPlMxAJypTmUuQwYZzm7LOKOg44wiHgez3uihp7Z-YPer21","purgeTime":"","qos":{"burstIOPS":15000,"burstTime":60,"curve":{"1048576":15000,"131072":1950,"16384":270,"262144":3900,"32768":500,"4096":100,"524288":7600,"65536":1000,"8192":160},"maxIOPS":15000,"minIOPS":50},"scsiEUIDeviceID":"6978766c00002705f47acc0100000000","scsiNAADeviceID":"6f47acc1000000006978766c00002705","sliceCount":1,"status":"active","totalSize":1000341504,"virtualVolumeID":null,"volumeAccessGroups":[],"volumeID":9989,"volumePairs":[]}]}}"""

RESP_PurgeDeletedVolumes_v9_0 = """{
  "id" : 1,
  "result": {}
}"""

RESP_ResetNode_v9_0 = """{
  "id": null,
  "result": {
    "rtfiInfo": {
      "build": "file:///sf/rtfi/image/filesystem.squashfs",
      "generation": "9",
      "options": {
        "edebug": "",
        "sf_auto": "0",
        "sf_bond_mode": "ActivePassive",
        "sf_check_hardware": "0",
        "sf_disable_otpw": "0",
        "sf_fa_host": "",
        "sf_hostname": "SF-FA18",
        "sf_inplace": "1",
        "sf_inplace_die_action": "kexec",
        "sf_inplace_safe": "0",
        "sf_keep_cluster_config": "0",
        "sf_keep_data": "0",
        "sf_keep_hostname": "0",
        "sf_keep_network_config": "0",
        "sf_keep_paths": "\"/var/log/hardware.xml\"",
        "sf_max_archives": "5",
        "sf_nvram_size": "",
        "sf_oldroot": "",
        "sf_postinst_erase_root_drive": "0",
        "sf_root_drive": "",
        "sf_rtfi_cleanup_state": "",
        "sf_secure_erase": "1",
        "sf_secure_erase_retries": "5",
        "sf_slice_size": "",
        "sf_ssh_key": "1",
        "sf_ssh_root": "1",
        "sf_start_rtfi": "1",
        "sf_status_httpserver": "1",
        "sf_status_httpserver_stop_delay": "5m",
        "sf_status_inject_failure": "",
        "sf_status_json": "0",
        "sf_support_host": "sfsupport.solidfire.com",
        "sf_test_hardware": "0",
        "sf_upgrade": "0",
        "sf_upgrade_firmware": "0",
        "sf_upload_logs_url": ""
     },
      "statusUrlAll": "http://192.168.130.20/status/all.json",
      "statusUrlCurrent": "http://192.168.130.20/status/current.json"
    }
  }
}"""

RESP_RestartNetworking_v9_0 = """{
  "id": null,
  "result": {
    "details": {},
    "duration": "00:00:02.548688",
    "result": "Passed"
  }
}"""

RESP_RestartServices_v9_0 = """{
  "id": 1,
  "result": {
      "details": {},
      "duration": "00:00:06.617292",
      "result": "Passed"
   }
}"""

RESP_RestartServices_v9_1 = """{"id":9,"result":{"details":"solidfire stop/waiting\nsolidfire start/running, process 55253\n","duration":"00:00:02.044584","result":"Passed"}}"""

RESP_SetDefaultQoS_v9_0 = """{
    "id":1,
    "result": {
        "burstIOPS":8000,
        "maxIOPS":1000,
        "minIOPS":200
    }
}"""

RESP_Shutdown_v9_0 = """{"result": {"failed": [], "successful": [1]}, "id": 5}"""

