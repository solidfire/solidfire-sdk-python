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

RESP_SetDefaultQoS_v9_0 = """{
    "id":1,
    "result": {
        "burstIOPS":8000,
        "maxIOPS":1000,
        "minIOPS":200
    }
}"""

