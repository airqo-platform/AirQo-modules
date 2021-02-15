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

def test_pytest(xydf, latlondf):
    a = latlon_xy_transform(latlondf)

    b = xydf

    assert (a.round(5) == b.round(5)).all(axis=None)
