from setuptools import setup
from setuptools import find_packages

setup(name='image-extractor',
      version='0.5.1',
      description='simtel to HDF5 data dumper',
      url='http://github.com/',
      license='MIT',
      packages=['image-extractor'],
      dependencies=[],
      dependency_links=['git+http://github.com/cta-observatory/ctapipe'],
      zip_safe=False)
