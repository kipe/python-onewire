import pytest

import onewire

def test_sensor_attrs_get_infinite_recursion(mocker):
    m = mocker.patch('onewire.Onewire.get', return_value=None)
    i = mocker.patch('onewire._ow.init', return_value=0)

    o = onewire.Onewire("Testdev")
    s = o.sensor('/test/path')
    s.read("temperature")
