from setuptools import setup
setup(
  name = 'simple_calibration',
  packages = ['simple_calibration'],
  version = '0.0.1',
  description = 'Performs simple calibration on network of colocated sensors.',
  author = 'AirQo',
  classifiers = [],
  install_requires=['numpy','networkx','matplotlib','scipy'],
)