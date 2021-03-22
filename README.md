# AirQo Modules

[![Documentation Status](https://readthedocs.org/projects/airqo-modules/badge/?version=latest)](https://airqo-modules.readthedocs.io/en/latest/?badge=latest) [![codecov](https://codecov.io/gh/airqo-platform/AirQo-modules/branch/add-data-model/graph/badge.svg?token=A7AQLMNI9R)](https://codecov.io/gh/airqo-platform/AirQo-modules) [![tests](https://github.com/airqo-platform/AirQo-modules/actions/workflows/python-app.yml/badge.svg)](https://github.com/airqo-platform/AirQo-modules/actions/workflows/python-app.yml)

Code for reproducing datasets, models and training routines for AirQo prediction models

## Summary

The [AirQo Platform](https://github.com/airqo-platform) consists of two main repositories ([AirQo-frontend](https://github.com/airqo-platform/AirQo-frontend) and [AirQo-api](https://github.com/airqo-platform/AirQo-api)) along with a mongodb database and various other functionality provided by the Google Cloud Platform, including BigQuery.

Current machine learning software within the platform is in the [predict](https://github.com/airqo-platform/AirQo-api/tree/staging/src/predict) and [calibrate](https://github.com/airqo-platform/AirQo-api/tree/staging/src/calibrate) microservices, built using Python and Flask. These microservices can import additional functionality from modules in this repository e.g. the calibrate microservice imports the [calibration](https://github.com/airqo-platform/AirQo-modules/tree/staging/calibration) Python package.

## Installation

Install [miniconda](https://docs.conda.io/en/latest/miniconda.html) (it also works with [anaconda](https://docs.anaconda.com/anaconda/install/), but we do not need the extra packages). With conda installed, run the following commands to create the virtual environment and activate it:

```
conda create --force -n AirQo-modules python=3.7
conda activate AirQo-modules
```

To install the dev build, clone the repo and use

    pip install -e .

See repo [wiki](https://github.com/airqo-platform/AirQo-modules/wiki) for contributing guidelines and general FAQ.

### Currently implemented:
#### [data_models](data_models/)

Data Models contain logic for extracting, transforming and loading data.

They link external data (e.g BigQuery), internal data (e.g. csv files) and dataframes which can be used by the model.

This module is under development and is planned to provide an absraction layer (unifying calls to BigQuery, mongodb and AirQo API) along with utility functions to be shared by multiple machine learning models e.g. GPS co-ordinate transforms.

### Adding Machine Learning Models

The process for adding machine learning models to the AirQo platform is summarised here.

![add-ml-process](assets/add-ml-process.svg)

Data is manually extracted from the AirQo platform (by a combination of direct access to BigQuery and mongodb, and by API calls). The data is then manually "wrangled" into a form that can be used in development of Machine Learning models. I is typically split into test and training datasets. The training dataset is used to train the model, yielding (hyper)parameters that define the fit of the model to the data. It is validated using the test dataset which provides metrics of model performance.

All or some of the code for model implementation and validation, and outputs in the form of (hyper)parameters and performance metrics may be stored in this repository. If this is the case, it facilitates direct re-use of offline model development outputs in online model imlpementation. Otherwise, models are re-implemented online entirely in the [AirQo-api repository](https://github.com/airqo-platform/AirQo-api).

Model developers are encouraged to find ways of reusing offline / research model code and outputs directly in the online platform (e.g. by installing and importing Python code). This decreases rework and increases confidence in the similarity and trustworthiness of online and offline model outputs used in descision making by end users.

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

https://airqo-modules.readthedocs.io/

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

## Contributing

## Usage

## Continuous Integration

## Static Analysis

## License