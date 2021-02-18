from setuptools import setup, find_packages
setup(
    name = 'airqomodules',
    packages = find_packages(include = ['data_models', 'data_models.*']),
    version = '1.0',
    install_requires = [
    'pandas',
    'pyproj'
    ]
)
