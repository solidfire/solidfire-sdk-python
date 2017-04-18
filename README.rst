|sf-python-logo| SolidFire Python SDK v1.2
==========================================

Python SDK library for interacting with SolidFire Element API

|pypy| |python| |format| |downloads| |license| |build|

Current Release
---------------

Version 1.2.2.185

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
| SolidFire Element OS   | 7.0 - 9.0     |
+------------------------+---------------+

Getting Help
------------

If you have any questions or comments about this product, contact
ng-sf-host-integrations-sdk@netapp.com or reach out to the online
developer community at `ThePub <http://netapp.io>`__. Your feedback
helps us focus our efforts on new features and capabilities.

Documentation
-------------

`Latest Docs <https://pythonhosted.org/solidfire-sdk-python/>`__

`Release
Notes <https://github.com/solidfire/solidfire-sdk-python/blob/gh-pages/SolidFire_Python_SDK_Release_Notes_v1.2.pdf>`__

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

Step 1 - Build an `Element <https://pythonhosted.org/solidfire-sdk-python/solidfire.html#solidfire.Element>`__ object using the factory
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This is the preferred way to construct the
`Element <https://pythonhosted.org/solidfire-sdk-python/solidfire.html#solidfire.Element>`__
object. The factory will make a call to the SolidFire cluster using the
credentials supplied to test the connection. It will also set the
version to communicate with based on the highest number supported by the
SDK and Element OS. Optionally, you can choose to set the version
manually and whether or not to verify SSL. Read more about it in the
`ElementFactory <https://pythonhosted.org/solidfire-sdk-python/solidfire.html#solidfire.factory.ElementFactory>`__ documentation.

.. code-block:: python

    from solidfire.factory import ElementFactory

    # Use ElementFactory to get a SolidFireElement object.
    sfe = ElementFactory.create("ip-address-of-cluster", "username", "password")

Step 2 - Call the API method and retrieve the result
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

All service methods in SolidFireElement call API endpoints and they all
return result objects. The naming convention is :code:`[method_name]_result`.
For example, :code:`list_accounts` returns a :code:`list_accounts_result` object
which has a property called :code:`accounts` that can be iterated.

This example sends a request to list accounts then pulls the first account
from the :code:`add_account_result` object.

.. code-block:: python

    # Send the request and wait for the result then pull the AccountID
    list_accounts_result = sfe.list_accounts()
    account = list_accounts_result.accounts[0];   

More examples using the Python SDK
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

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

More specific examples are available `here <https://github.com/solidfire/solidfire-sdk-python/blob/v1.2/examples/examples.rst>`__

Logging
-------

To configure logging responses, execute the following:

.. code-block:: python

    import logging
    from solidfire import common
    common.setLogLevel(logging.DEBUG)

To access the logger for the Element instance:

.. code-block:: python

     from solidfire.common import LOG

Timeouts
--------

Connection timeout (useful for failing fast when a host becomes
unreachable):

.. code-block:: python

    from solidfire.factory import ElementFactory
    sfe = ElementFactory.create("ip-address-of-cluster", "username", "password")
    sfe.timeout(600)

Read timeout (useful for extending time for a service call to return):

.. code-block:: python

    from solidfire.factory import ElementFactory
    sfe = ElementFactory.create("ip-address-of-cluster", "username", "password")
    sf.read_timeout(600)

**License**
-----------

Copyright © 2016, 2017 NetApp, Inc. All rights reserved.

Licensed under the Apache License, Version 2.0 (the "License"); you may
not use this file except in compliance with the License. You may obtain
a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

.. |sf-python-logo| image:: https://raw.githubusercontent.com/solidfire/solidfire-sdk-python/release1.1/img/python-50.png
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
