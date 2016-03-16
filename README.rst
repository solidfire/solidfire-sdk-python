********************************
SolidFire Element API Python SDK
********************************

Python SDK library for interacting with the SolidFire Element API.


Installation
============
To install globally with `pip` (if you have pip 1.3 or greater installed globally)::

    $> pip install solidfire-sdk-python

**From Source**
+++++++++++++++
*Note*:
It is recommended using virtualenv <https://github.com/pypa/virtualenv> for isolating your python environment to only the required libraries::

    $> git clone git@github.com:solidfire/solidfire-sdk-python.git
    $> cd solidfire-sdk-python
    $> pip install -e ".[dev,test, docs, release]"
    $> python setup.py install

Then you will need to append the location of this directory to your `PYTHONPATH` environment
variable so you can use the SDK in other python scripts::

    export PYTHONPATH=$PYTHONPATH:/path/to/sf-python-sdk/

That's it -- you are ready to start interacting with your SolidFire cluster using Python!

**How To Use**
++++++++++++++
Using the SolidFire Element API Python SDK is very straightforward.
Just import the module, instantiate an instance of the `solidfire.Element` class, give it your authentication 
credentials, and start asking the SolidFire Element API for data.

    >>> from solidfire import Element
    >>> sf = Element('<MVIP>', '<YOUR USERNAME>', '<YOUR PASSWORD>', '<API VERSION>')
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
