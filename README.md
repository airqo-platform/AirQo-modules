# AirQo Modules.

[![Documentation Status](https://readthedocs.org/projects/airqo-modules/badge/?version=latest)](https://airqo-modules.readthedocs.io/en/latest/?badge=latest) [![codecov](https://codecov.io/gh/airqo-platform/AirQo-modules/branch/add-data-model/graph/badge.svg?token=A7AQLMNI9R)](https://codecov.io/gh/airqo-platform/AirQo-modules) [![tests](https://github.com/airqo-platform/AirQo-modules/actions/workflows/python-app.yml/badge.svg)](https://github.com/airqo-platform/AirQo-modules/actions/workflows/python-app.yml)

Code for reproducing datasets, models and training routines for AirQo prediction models

To install the dev build, clone the repo and use

    pip install -e .

See repo [wiki](https://github.com/airqo-platform/AirQo-modules/wiki) for contributing guidelines and general FAQ.
## Tests

We aim to have a high level of test coverage for code in this repository. Please try and ensure new code has appropriate unit / integration / regression tests. We use the `pytest` runner. To run the tests locally, ensure you have `pytest` installed:

```
pip install pytest
```

To run the tests:

```
pytest
```
## Documentation

We used readthedocs to document this repository via `sphinx` and `autodoc`. To build the documentation locally, you must have `sphinx-build`,  `autoapi` and `sphinx_rtd_theme` installed:

```
pip install sphinx
pip install sphinx-autoapi
pip install sphinx_rtd_theme
```

To build the (html) documentation:

Windows:

```
cd docs
make html
```

Linux:

```
cd docs
make -f Makefile html
```

## Currently implemented:
### data_models

Data Models contain logic for extracting, transforming and loading data

They link external data (e.g BigQuery), internal data (e.g. csv files) and dataframes which can be used by the model.
