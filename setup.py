from distutils.core import setup
from distutils.extension import Extension

setup(
    name='onewire',
    packages=['onewire'],
    ext_modules=[
        Extension('onewire._ow', libraries=['owcapi'], sources=['onewire/_ow.c'], extra_link_args=['-I', '/usr/include'])
    ],
)
