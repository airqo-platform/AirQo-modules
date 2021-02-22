## AirQo Modules.

[![Documentation Status](https://readthedocs.org/projects/airqo-modules/badge/?version=latest)](https://airqo-modules.readthedocs.io/en/latest/?badge=latest) [![codecov](https://codecov.io/gh/airqo-platform/AirQo-modules/branch/add-data-model/graph/badge.svg?token=A7AQLMNI9R)](https://codecov.io/gh/airqo-platform/AirQo-modules) [![tests](https://github.com/airqo-platform/AirQo-modules/actions/workflows/python-app.yml/badge.svg)](https://github.com/airqo-platform/AirQo-modules/actions/workflows/python-app.yml)

Code for reproducing datasets, models and training routines for AirQo prediction models

To install the dev build, clone the repo and use

    pip install -e .

See repo [wiki](https://github.com/airqo-platform/AirQo-modules/wiki) for contributing guidelines and general FAQ.

## Currently implemented:

### data_models

Data Models contain logic for extracting, transforming and loading data

They link external data (e.g BigQuery), internal data (e.g. csv files) and dataframes which can be used by the model.
