---
title: Solidfire Python SDK
layout: index
---
SolidFire Element API Python SDK
================================

Python SDK library for interacting with the SolidFire Element API.

Installation
============
To install globally with `pip` (if you have pip 1.3 or greater installed globally)::

    $> pip install solidfire-sdk-python

**From Source**
---------------
*Note*:
It is recommended using virtualenv <https://github.com/pypa/virtualenv> for isolating your python environment to only the required libraries::

    $> pip install -e git+https://github.com/solidfire/solidfire-sdk-python.git@release/1.0.0#egg=solidfire-sdk-python

Alternativly, for development purposes or to inspect the source, the following will work::

    $> git clone git@github.com:solidfire/solidfire-sdk-python.git
    $> cd solidfire-sdk-python
    $> git checkout release/1.0.0
    $> pip install -e ".[dev,test, docs, release]"
    $> python setup.py install

Then you will need to append the location of this directory to your `PYTHONPATH` environment
variable so you can use the SDK in other python scripts::

    export PYTHONPATH=$PYTHONPATH:/path/to/sf-python-sdk/

That's it -- you are ready to start interacting with your SolidFire cluster using Python!

**How To Use**
--------------
Using the SolidFire Element API Python SDK is very straightforward.
Just import the module, instantiate an instance of the `solidfire.Element` class, give it your authentication 
credentials, and start asking the SolidFire Element API for data.
*Note*:
The parameter verify_ssl=False is useful when connecting to an IP or when ssl errors are causing the connection to fail.

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
To configure logging responses, execute the following:

    >>> import logging
    >>> from solidfire import common
    >>> common.setLogLevel(logging.DEBUG)

To access the logger for the Element instance:

    >>> from solidfire import common
    >>> common.log

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
