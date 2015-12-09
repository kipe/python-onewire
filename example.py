from onewire import Onewire

with Onewire('u') as o:
    print(['%s.%s %.02f' % (s.family, s.id, s.read_float('temperature')) for s in o.find(has_all=['temperature'])])
