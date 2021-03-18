# AirQo-modules

[![Documentation Status](https://readthedocs.org/projects/airqo-modules/badge/?version=latest)](https://airqo-modules.readthedocs.io/en/latest/?badge=latest)

## Summary

The [AirQo Platform](https://github.com/airqo-platform) consists of two main repositories ([AirQo-frontend](https://github.com/airqo-platform/AirQo-frontend) and [AirQo-api](https://github.com/airqo-platform/AirQo-api)) along with a mongodb database and various other functionality provided by the Google Cloud Platform, including BigQuery.

Current machine learning software within the platform is in the [predict](https://github.com/airqo-platform/AirQo-api/tree/staging/src/predict) and [calibrate](https://github.com/airqo-platform/AirQo-api/tree/staging/src/calibrate) microservices, built using Python and Flask. These microservices can import additional functionality from modules in this repository e.g. the calibrate microservice imports the [calibration](https://github.com/airqo-platform/AirQo-modules/tree/staging/calibration) Python package.

### Adding Machine Learning Models

The process for adding machine learning models to the AirQo platform is summarised here.

![add-ml-process](../assets/add-ml-process.svg)

## Contributing

## Installation

## Tests

## Usage

## Documentation

Documentation for implemented modules can be found here:

https://airqo-modules.readthedocs.io/

## Continuous Integration

## Static Analysis

## License