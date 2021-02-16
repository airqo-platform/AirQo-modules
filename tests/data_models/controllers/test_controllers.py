from data_models.controllers.transform import (
    coord_transform,
    latlon_xy_transform,
    xy_latlon_transform
)

import pandas as pd
import numpy as np
import pytest

@pytest.fixture
def latlondf():
    lat = [0.3335304, 53.3813502]
    lon = [32.5675046, -1.4884229]
    name = ['makerere', 'sheffield']

    labels = ['latitude', 'longitude', 'name']

    df = pd.DataFrame([lat,lon,name]).transpose()
    df.columns = labels
    df[labels[0:2]] = df[labels[0:2]].astype(np.float64)

    return df

@pytest.fixture
def xydf():
    x = np.array([3625398.0284795, -165690.4793130])
    y = np.array([37128.6439850, 7053851.2814178])
    name = ['makerere', 'sheffield']

    labels = ['x', 'y', 'name']

    df = pd.DataFrame([x,y,name]).transpose()
    df.columns = labels
    df[labels[0:2]] = df[labels[0:2]].astype(np.float64)

    return df

def test_coord_transform(xydf):
    input = xydf
    transform = coord_transform(
        input,
        crs = ['epsg:3857','epsg:4326'],
        input_labels = ['x', 'y'],
        output_labels = ['latitude','longitude']
    )
    expected = xy_latlon_transform(input)

    assert (transform == expected).all(axis=None)

def test_latlon_to_xy(xydf, latlondf):
    input = latlondf

    transform = latlon_xy_transform(input).round(5)

    expected = xydf.round(5)

    assert (transform == expected).all(axis=None)

def test_xy_to_latlon(xydf, latlondf):
    input = xydf

    transform = xy_latlon_transform(input).round(5)

    expected = latlondf.round(5)

    assert (transform == expected).all(axis=None)

def test_latlon_to_latlon(latlondf):
    input = latlondf

    transform = latlon_xy_transform(input)

    transform = xy_latlon_transform(transform).round(5)

    expected = latlondf.round(5)

    assert (transform == expected).all(axis=None)
