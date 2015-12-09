# python-onewire
A wrapper for OWFS C-API, compatible with both Python 2.7 and Python 3.x.

## Requirements
Depends on `owcapi` from [OWFS -project](http://owfs.org/index.php?page=owcapi).
On Debian-based systems, it can be installed by running
```sh
apt-get install libow-dev
```

## Install
`pip install git+https://github.com/kipe/python-onewire.git`

## Usage
Usage is fairly similar to the original [owpython](http://owfs.sourceforge.net/owpython.html).
However, this library is class-based, so some modifications are required.

```python
from onewire import Onewire

# Use USB-adapter
with Onewire('u') as o:
    # Find all temperature sensors in the bus, and print family, id and temperature as float.
    print('\n'.join([
        '%s.%s %.02f' % (s.family, s.id, s.read_float('temperature'))
        for s in o.find(has_all=['temperature'])
    ]))
    # Read temperature from specific sensor
    # (note: when accessing values directly, the return value is always a string).
    print(o.sensor('28.D035DE060000').temperature)
```
