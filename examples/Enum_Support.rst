Enum Support Examples
===========================


Enum Support
---------------


These examples walk through all interactions with an Enums on the
SolidFire cluster.

Examples for:

-  `List all Enums <#list/details-all-Enums>`__

List all Enums
~~~~~~~~~~~~~~~~~

AuthConfigType
~~~~~~~~~~~~~~~
AuthConfigType This type indicates the configuration data which will be accessed or modified by the element auth container.:

.. code-block:: python

	from solidfire.models import AuthConfigType
	
	#mNode authentication configuration data.
	    sfe = models.AuthConfigType("mNode")
		
	#Element authentication configuration data.
		sfe = models.AuthConfigType("element")
		
	#Returns String type values.
		value=sfe.get_value()

DriveEncryptionCapabilityType
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This specifies a drive's encryption capability.

.. code-block:: python

	from solidfire.models import DriveEncryptionCapabilityType
	
	#Drive is not a Self Encrypting Drive (SED), and therefore not FIPS.
		sfe = models.DriveEncryptionCapabilityType("none")
	 
	#Drive is a SED but not a FIPS SED.
		sfe = models.DriveEncryptionCapabilityType("sed")
		
	#Drive is a FIPS SED Drive.
		sfe = models.DriveEncryptionCapabilityType("fips")
		
	#Returns String type values.
		value=sfe.get_value()

FipsDrivesStatusType
~~~~~~~~~~~~~~~~~~~~
This specifies a node's FIPS 140-2 compliance status.

.. code-block:: python

	from solidfire.models import FipsDrivesStatusType
	
	#Node is not FIPS capable.
		sfe = models.FipsDrivesStatusType("none")
	
	#Node is FIPS capable but not all drives present are FIPS drives.
		sfe = models.FipsDrivesStatusType("partial")
		
	#Node is FIPS capable and all drives present are FIPS drives or if there are no drives present.
		sfe = models.FipsDrivesStatusType("ready")
		
	#Returns String type values.
		value=sfe.get_value()
		
ProposedNodeErrorCode
~~~~~~~~~~~~~~~~~~~~~~
This specifies error code for a proposed node addition.

.. code-block:: python

	from solidfire.models import ProposedNodeErrorCode
	
	#Nodes constitute too large a portion of cluster capacity for protectionScheme=doubleHelix.
		sfe = models.ProposedNodeErrorCode("nodesTooLarge")
	
	#Nodes failed to authenticate.
		sfe = models.ProposedNodeErrorCode("nodesAuthError")
	
	#Nodes did not respond to ping requests.
		sfe = models.ProposedNodeErrorCode("nodesUnreachable")
		
	#Unable to add a non-FIPS capable node to cluster while FipsDrives Feature is enabled.
		sfe = models.ProposedNodeErrorCode("nonFipsNodeCapable")
		
	#Unable to add a node with non-FIPS capable drive(s) to cluster while FipsDrives Feature is enabled.
		sfe = models.ProposedNodeErrorCode("nonFipsDrivesCapable")
	
	#Returns String type values.
		value=sfe.get_value()
		
ProtectionDomainType
~~~~~~~~~~~~~~~~~~~~
A Protection Domain is a set of one or more components whose simultaneous failure is protectedfrom causing data unavailability or loss.
This specifies one of the types of Protection Domains recognized by this cluster.

.. code-block:: python

	from solidfire.models import ProtectionDomainType

	#Any individual Node.
		sfe = models.ProtectionDomainType("node")
	
	#Any individual Node or all storage Nodes within an individual HCI chassis.
		sfe = models.ProtectionDomainType("chassis")
	
	#Any or all Nodes that have been assigned the same CustomProtectionDomainName.
		sfe = models.ProtectionDomainType("custom")
	
	#Returns String type values.
		value=sfe.get_value()
		
ProtectionScheme
~~~~~~~~~~~~~~~~~~~~
The method of protecting data on the cluster

.. code-block:: python

	from solidfire.models import ProtectionScheme

	
		sfe = models.ProtectionScheme("singleHelix")
		
		sfe = models.ProtectionScheme("doubleHelix")
		
		sfe = models.ProtectionScheme("tripleHelix")
		
	#Returns String type values.
		value=sfe.get_value()
		
ProtectionSchemeCategory
~~~~~~~~~~~~~~~~~~~~~~~~~~~
The category of the protection scheme.

.. code-block:: python
	
	from solidfire.models import ProtectionSchemeCategory

	#The protection scheme is replication based.
		sfe = models.ProtectionSchemeCategory("helix")
		
	#The protection scheme is erasure-coding based.
		sfe = models.ProtectionSchemeCategory("erasureCoded")
		
	#Returns String type values.
		value=sfe.get_value()

ProtectionSchemeVisibility
~~~~~~~~~~~~~~~~~~~~~~~~~~~
The public visibility of the protection scheme.

.. code-block:: python
	
	from solidfire.models import ProtectionSchemeVisibility

	#The scheme is publicly released for customer use.
		sfe = models.ProtectionSchemeVisibility("customer")
	
	#The scheme is for internal test use only.
		sfe = models.ProtectionSchemeVisibility("testOnly")
		
	#Returns String type values.
		value=sfe.get_value()


RemoteClusterSnapshotStatus
~~~~~~~~~~~~~~~~~~~~~~~~~~~
Status of the remote snapshot on the target cluster as seen on the source cluster.

.. code-block:: python

	from solidfire.models import RemoteClusterSnapshotStatus
	
	#Snapshot exists on the target cluster
		sfe = models.RemoteClusterSnapshotStatus("Present")
	
	#Snapshot does not exist on the target cluster
		sfe = models.RemoteClusterSnapshotStatus("Not Present")
	
	#Snapshot is currently replicating to the target cluster
		sfe = models.RemoteClusterSnapshotStatus("Syncing")

	#Snapshot has been deleted on the target, and it still exists on the source
		sfe = models.RemoteClusterSnapshotStatus("Deleted")
		
	#The status of snapshot on the target is not known on the source
		sfe = models.RemoteClusterSnapshotStatus("Unknown")

	#Returns String type values.
		value=sfe.get_value()

VolumeAccess
~~~~~~~~~~~~~~~~~~~~~~~~~~~
Describes host access for a volume.


.. code-block:: python
	
	from solidfire.models import VolumeAccess
	
	#No reads or writes are allowed.
		sfe = models.VolumeAccess("locked")
		
	#Only read operations are allowed.
		sfe = models.VolumeAccess("readOnly")
	
	#Reads and writes are allowed.
		sfe = models.VolumeAccess("readWrite")
	
	#Designated as a target volume in a replicated volume pair.
		sfe = models.VolumeAccess("replicationTarget")
	
	#Controlled by a SnapMirror endpoint. No reads or writes are allowed.
		sfe = models.VolumeAccess("snapMirrorTarget")
	
	#Returns String type values.
		value=sfe.get_value()
