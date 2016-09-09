SolidFire Python SDK
=====================

Python SDK library for interacting with SolidFire Element API

|pypy| |python| |format| |downloads| |license| |build|

Current Release
---------------

Version 1.1.\*

Description
-----------

The SolidFire Python SDK is a collection of libraries that facilitate
integration and orchestration between proprietary systems and
third-party applications. The Python SDK allows developers to deeply
integrate SolidFire system API with the Python programming language. The
SolidFire Python SDK reduces the amount of additional coding time
required for integration.

Compatibility
-------------

+------------------------+---------------+
| Component              | Version       |
+========================+===============+
| SolidFire Element OS   | 7.x and 8.x   |
+------------------------+---------------+

Getting Help
------------

If you have any questions or comments about this product, contact
ng-sf-host-integrations-sdk@netapp.com or reach out to the online
developer community at `ThePub <http://netapp.io>`__. Your feedback
helps us focus our efforts on new features and capabilities.

Documentation (v1.1)
--------------------

`Latest Docs <https://pythonhosted.org/solidfire-sdk-python/>`__

`Release
Notes <https://github.com/solidfire/sdk-dotnet/raw/gh-pages/Dot%20NET%20SDK%20Release%20Notes_v1.0.pdf>`__

Prerequisites
-------------

The following prerequisites are required before installing the Solidfire
SDK.

+------------------------------------------------------------------+-----------+
| Component                                                        | Version   |
+==================================================================+===========+
| `PycURL <http://pycurl.io/docs/latest/install.html#install>`__   | 7.21.5+   |
+------------------------------------------------------------------+-----------+

To install globally with ``pip`` (requires pip 1.3 or greater)

PycURL
~~~~~~

**Install
`PycURL <http://pycurl.io/docs/latest/install.html#install>`__**

::

    pip install pycurl

The Solidfire Python SDK depends on the PycURL library which depends on
an installed SSL library. If the installation fails due to PycURL, this
is most likely due to a missing SSL dependency. OpenSSL is the
recomended SSL backend for all linux flavors.

Instructions are Python 2.7 specific with examples of Python 3.3+
examples in the comments.

**Ubuntu Pre-Installation Steps**:

::

    sudo apt-get install python-pip                                  # or python3-pip
    sudo apt-get install libffi-dev libssl-dev libcurl4-openssl-dev
    sudo apt-get install python-dev                                  # or python3.3-dev python3.4-dev python3.5-dev
    pip install pyopenssl ndg-httpsclient pyasn1                     # use the correct version of pip (i.e. pip3.3)

**RHEL/CentOS Pre-Installation Steps**:

::

    yum install epel-release
    yum groupinstall 'Development Tools'
    yum -y install python-setuptools python-pip python-wheel         # or python3-setuptools python3-pip python3-wheel
    yum -y install libffi-devel openssl-devel libcurl
    yum -y install python-devel                                      # or python3.3-devel python3.4-devel python3.5-devel 
    pip install pyopenssl ndg-httpsclient pyasn1                     # use the correct version of pip (i.e. pip3.3)

Installation
------------

**From PyPI**

::

    pip install solidfire-sdk-python

**From Source**

*Note*: It is recommended using
`virtualenv <https://github.com/pypa/virtualenv>`__ for isolating the
python environment to only the required libraries.

To install the latest version of the SDK:

::

    pip install -e git+https://github.com/solidfire/solidfire-sdk-python.git@develop#egg=solidfire-sdk-python

Alternatively, for development purposes or to inspect the source, the
following will work:

::

    git clone git@github.com:solidfire/solidfire-sdk-python.git  
    cd solidfire-sdk-python
    git checkout develop
    pip install -e ".[dev, test, docs, release]"
    python setup.py install

Then append the location of this directory to the ``PYTHONPATH``
environment variable to use the SDK in other python scripts:

::

    export PYTHONPATH=$PYTHONPATH:/path/to/sf-python-sdk/

That's it -- you are ready to start interacting with your SolidFire
cluster using Python!

Examples
--------

Step 1 - Build an `Element <help/v1.1/html/T_SolidFire_Element_Api_SolidFireElement.htm>`__ object using the factory
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This is the preferred way to construct the
`Element <help/v1.1/html/T_SolidFire_Element_Api_SolidFireElement.htm>`__
object. The factory will make a call to the SolidFire cluster using the
credentials supplied to test the connection. It will also set the
version to communicate with based on the highest number supported by the
SDK and Element OS. Optionally, you can choose to set the version
manually and whether or not to verify SSL. Read more about it in the
`ElementFactory <link-to-pypi-doc-for-elementfactory>`__ documentation.

.. code:: python

    from solidfire.factory import ElementFactory

    # Use ElementFactory to get a SolidFireElement object.
    sfe = ElementFactory.create("ip-address-of-cluster", "username", "password")

Step 2 - Call the API method and retrieve the result
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

All service methods in SolidFireElement call API endpoints and they all
return result objects. The naming convention is [method\_name]\_result.
For example, ``list_accounts`` returns a ``list_accounts_result`` object
which has a property called ``accounts`` that can be iterated.

*This example sends a request to create an account then pulls the new
account id from the add\_account\_result object.*

.. code:: python

    # Send the request and wait for the result then pull the AccountID
    new_account_id = sfe.add_account(username="example-account").account_id;   

More examples using the Python SDK
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

    from solidfire.factory import ElementFactory

    # Create connection to SF Cluster
    sfe = ElementFactory.create("ip-address-of-cluster", "username", "password")

    # --------- EXAMPLE 1 - CREATE AN ACCOUNT -----------
    # Send the request with required parameters and gather the result
    add_account_result = sfe.add_account(username="example-account")
    # Pull the account ID from the result object
    account_id = add_account_result.account_id

    # --------- EXAMPLE 2 - CREATE A VOLUME -------------
    # Send the request with required parameters and gather the result
    create_volume_result = sfe.create_volume(name="example-volume",
                                             account_id=account_id,
                                             total_size=1000000000,
                                             enable512e=False)
    # Pull the VolumeID off the result object
    volume_id = create_volume_result.volume_id

    # --------- EXAMPLE 3 - LIST ONE VOLUME FOR AN ACCOUNT -------------
    # Send the request with desired parameters and pull the first volume in the
    # result
    volume = sfe.list_volumes(accounts=[account_id], limit=1).volumes[0]
    # pull the iqn from the volume
    iqn = volume.iqn

    # --------- EXAMPLE 3 - MODIFY A VOLUME -------------
    # Send the request with the desired parameters
    sfe.modify_volume(volume_id=volume_id, total_size=2000000000)

More Examples
-------------

More specific examples are available `here <examples>`__

Logging
-------

To configure logging responses, execute the following::

.. code:: python

    import logging
    from solidfire import common
    common.setLogLevel(logging.DEBUG)

To access the logger for the Element instance:: :sub:`~` python from
solidfire import common common.log :sub:`~`

Timeouts
--------

Connection timeout (useful for failing fast when a host becomes
unreachable)::

.. code:: python

    from solidfire.factory import ElementFactory
    sfe = ElementFactory.create("ip-address-of-cluster", "username", "password")
    sfe.timeout(600)

Read timeout (useful for extending time for a service call to return)::

.. code:: python

    from solidfire.factory import ElementFactory
    sfe = ElementFactory.create("ip-address-of-cluster", "username", "password")
    sf.read_timeout(600)

**License**
-----------

Copyright © 2016 NetApp, Inc. All rights reserved.

Licensed under the Apache License, Version 2.0 (the "License"); you may
not use this file except in compliance with the License. You may obtain
a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

.. |pypy| image:: https://img.shields.io/pypi/v/solidfire-sdk-python.svg
   :target: https://badge.fury.io/py/solidfire-sdk-python
.. |python| image:: https://img.shields.io/pypi/pyversions/solidfire-sdk-python.svg
   :target: https://pypi.python.org/pypi/solidfire-sdk-python/
.. |format| image:: https://img.shields.io/pypi/format/solidfire-sdk-python.svg
   :target: https://pypi.python.org/pypi/solidfire-sdk-python/
.. |downloads| image:: https://img.shields.io/pypi/dm/solidfire-sdk-python.svg
   :target: https://pypi.python.org/pypi/solidfire-sdk-python/
.. |license| image:: https://img.shields.io/pypi/l/solidfire-sdk-python.svg
   :target: https://pypi.python.org/pypi/solidfire-sdk-python/
.. |build| image:: https://img.shields.io/travis/solidfire/solidfire-sdk-python/release/1.0.0.svg
   :target: https://pypi.python.org/pypi/solidfire-sdk-python/