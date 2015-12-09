# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import _ow
import os
import re


class Onewire(object):
    _path = '/uncached/'
    initialized = False

    SENSOR_REGEX = re.compile(r'[0-9A-F][0-9A-F]\.[0-9A-F]+', re.IGNORECASE | re.DOTALL)

    def __init__(self, device, cached=False):
        if _ow.init(str(device)) != 0:
            raise IOError("Initializing 1-wire failed.")

        self.initialized = True
        if cached:
            self._path = '/'

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.finish()

    def finish(self):
        _ow.finish()
        self.initialized = False

    def get(self, *path):
        return _ow.get(str(os.path.join(self._path, *path)))

    def find(self, has_all=[], has_one=[], sensor_type=[]):
        if not isinstance(has_all, list):
            has_all = [has_all]
        if not isinstance(has_one, list):
            has_one = [has_one]
        if not isinstance(sensor_type, list):
            sensor_type = [sensor_type]

        for p in self.get('').split(','):
            if not self.SENSOR_REGEX.match(p):
                continue

            s = Sensor(self, p)
            # Check if all required arguments are found
            if has_all and not set(s.attrs).issuperset(set(has_all)):
                continue
            # Check if at least one of has_one arguments is found
            if has_one and not [x for x in has_one if x in s.attrs]:
                continue
            # Check if sensor_type matches
            if sensor_type and s.sensor_type not in sensor_type:
                continue
            yield s

    def sensor(self, path):
        return Sensor(self, path)


class Sensor(object):
    def __init__(self, ow, path):
        self._ow = ow
        self.path = path.rstrip('/')
        self._sensor_type = None
        self._attrs = []

    def __str__(self):
        return '<Sensor %s - %s>' % (self.path, self.sensor_type)

    def __unicode__(self):
        return self.__str__()

    def __repr__(self):
        return self.__str__()

    def __getattr__(self, attr):
        if attr not in self.attrs:
            raise AttributeError('Attribute "%s" not found in %s.' % (attr, self.__str__()))
        return self._ow.get(self.path, attr)

    def read(self, attr):
        return self.__getattr__(attr)

    def read_float(self, attr):
        return float(self.__getattr__(attr))

    def read_int(self, attr):
        return int(self.__getattr__(attr))

    def read_boolean(self, attr):
        return int(self.__getattr__(attr)) == 1

    @property
    def sensor_type(self):
        if self._sensor_type:
            return self._sensor_type
        self._sensor_type = self._ow.get(self.path, 'type')
        return self._sensor_type

    @property
    def attrs(self):
        if self._attrs:
            return self._attrs
        self._attrs = self._ow.get(self.path).split(',')
        return self._attrs
