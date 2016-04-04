SolidFire Element API Python SDK
================================

.. image:: https://raw.githubusercontent.com/solidfire/solidfire-sdk-python/gh-pages/_static/PythonSDK-58x58.png 


Python SDK library for interacting with the SolidFire Element API.

Minimum versions:

* Python 2: 2.7+
* Python 3: 3.3+

Dependencies
------------
**PycURL**

The Solidfire Python SDK depends on the PycURL library which depends on an installed SSL library.  If the installation fails due to PycURL, this is most likely due to a missing SSL dependency. OpenSSL is the recomended SSL backend for all linux flavors.

The following are instructions are required before installing the Solidfire SDK.  Instructions are Python 2.7 specific with examples of Python 3.3+ examples in the comments.

**Ubuntu Pre-Installation Steps**::
    
    sudo apt-get install python-pip                                  # or python3-pip
    sudo apt-get install libffi-dev libssl-dev libcurl4-openssl-dev
    sudo apt-get install python-dev                                  # or python3.3-dev python3.4-dev python3.5-dev
    pip install pyopenssl ndg-httpsclient pyasn1                     # use the correct version of pip (i.e. pip3.3)

**RHEL/CentOS Pre-Installation Steps**::
    
    yum install epel-release
    yum groupinstall 'Development Tools'
    yum -y install python-setuptools python-pip python-wheel         # or python3-setuptools python3-pip python3-wheel
    yum -y install libffi-devel openssl-devel libcurl
    yum -y install python-devel                                      # or python3.3-devel python3.4-devel python3.5-devel 
    pip install pyopenssl ndg-httpsclient pyasn1                     # use the correct version of pip (i.e. pip3.3)

Installation
============
To install globally with `pip` (requires pip 1.3 or greater installed globally)::

    pip install solidfire-sdk-python

**From Source**
---------------
*Note*: It is recommended using virtualenv <https://github.com/pypa/virtualenv> for isolating the python environment to only the required libraries.

To install the latest version of the SDK::

    pip install -e git+https://github.com/solidfire/solidfire-sdk-python.git@release/1.0.0#egg=solidfire-sdk-python

Alternatively, for development purposes or to inspect the source, the following will work::

    git clone git@github.com:solidfire/solidfire-sdk-python.git  
    cd solidfire-sdk-python  
    git checkout release/1.0.0
    pip install -e ".[dev, test, docs, release]"
    python setup.py install

Then append the location of this directory to the `PYTHONPATH` environment
variable to use the SDK in other python scripts::

    export PYTHONPATH=$PYTHONPATH:/path/to/sf-python-sdk/

That's it -- you are ready to start interacting with your SolidFire cluster using Python!

**How To Use**
--------------
Using the SolidFire Element API Python SDK is very straightforward.
Just import the module, instantiate an instance of the `solidfire.Element` class, give it admin authentication 
credentials, and start asking the SolidFire Element API for data.

*Note*: The parameter *verify_ssl=False* is useful when connecting to an IP or when ssl errors are causing the connection to fail.

**Example**::

    >>> from solidfire import Element
    >>> sf = Element('<MVIP>', '<YOUR USERNAME>', '<YOUR PASSWORD>', '<API VERSION>', verify_ssl=False)
    >>> result = sf.list_active_volumes()
    >>> for volume in result.volumes:
    ...     print('{id}, ({name}): size={vol_size} - QoS(min={min_iops}, max={max_iops}, burst={burst_iops}, burst_time={burst_time})'.format(
    ...         id=volume.volume_id, name=volume.name,  vol_size=volume.total_size,
    ...         min_iops=volume.qos.min_iops, max_iops=volume.qos.max_iops, burst_iops=volume.qos.burst_iops, burst_time=volume.qos.burst_time)
    ...     )
    ...
    1, (VOLUME1): size=1000341504 - QoS(min=50, max=15000, burst=15000, burst_time=60)
    2, (VOLUME2): size=2000683008 - QoS(min=5000, max=15000, burst=30000, burst_time=60)
    3, (VOLUME3): size=1000341504 - QoS(min=50, max=15000, burst=15000, burst_time=60)
    4, (VOLUME4): size=2000683008 - QoS(min=50, max=15000, burst=15000, burst_time=60)

That is it! For a list of available methods (and a bit of documentation), run `help(Element)`.

**Logging**
-----------
To configure logging responses, execute the following::

    >>> import logging
    >>> from solidfire import common
    >>> common.setLogLevel(logging.DEBUG)
  
To access the logger for the Element instance::

    >>> from solidfire import common
    >>> common.log

**Timeouts**
------------
Connection timeout (useful for failing fast when a host becomes unreachable)::

    >>> from solidfire import Element
    >>> sf = Element('<MVIP>', '<YOUR USERNAME>', '<YOUR PASSWORD>', '<API VERSION>', verify_ssl=False)
    >>> sf.timeout(600)

Read timeout (useful for extending time for a service call to return)::

    >>> from solidfire import Element
    >>> sf = Element('<MVIP>', '<YOUR USERNAME>', '<YOUR PASSWORD>', '<API VERSION>', verify_ssl=False)
    >>> sf.read_timeout(600)
    
**License**
-----------
Copyright © 2016 NetApp, Inc.  All rights reserved.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

<http://www.apache.org/licenses/LICENSE-2.0>

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and limitations under the License.
