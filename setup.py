from distutils.core import setup
from distutils.extension import Extension

setup(
    name='onewire',
    version='0.1',
    description='A wrapper for OWFS C-API, compatible with both Python 2.7 and Python 3.x.',
    author='Kimmo Huoman',
    author_email='kipenroskaposti@gmail.com',
    url='https://github.com/kipe/python-onewire',
    packages=['onewire'],
    ext_modules=[
        Extension('onewire._ow', libraries=['owcapi'], sources=['onewire/_ow.c'], extra_link_args=['-I', '/usr/include'])
    ],
)
