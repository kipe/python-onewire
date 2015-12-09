from onewire import Onewire

# Use USB-adapter
with Onewire('u') as o:
    # Find all temperature sensors in the bus, and print family, id and temperature as float.
    print(['%s.%s %.02f' % (s.family, s.id, s.read_float('temperature')) for s in o.find(has_all=['temperature'])])
    # Read temperature from specific sensor (note: when accessing values directly, the return value is always a string).
    print(o.sensor('28.D035DE060000').temperature)
