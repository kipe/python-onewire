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
