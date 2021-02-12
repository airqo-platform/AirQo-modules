# Controllers for DataModel transforms

import pandas as pd
from models.DataModels import CoordinateTransformModel

def coord_transform(*args, **kwargs)-> pd.DataFrame:

    transformer = CoordinateTransformModel()
    output_df = transformer.transform(*args, **kwargs)

    return output_df

def latlon_xy_transform(
    input_df: pd.DataFrame,
    input_labels = ['latitude','longitude'],
    output_labels = ['x', 'y'],
    **kwargs
)-> pd.DataFrame:

    transformer = CoordinateTransformModel()
    crs = ['epsg:4326','epsg:3857']

    output_df = transformer.transform(
        input_df,
        crs = crs,
        input_labels = input_labels,
        output_labels = output_labels,
        **kwargs
    )

    return output_df

def xy_latlon_transform(
    input_df: pd.DataFrame,
    input_labels = ['x', 'y'],
    output_labels = ['latitude','longitude'],
    **kwargs
)-> pd.DataFrame:

    transformer = CoordinateTransformModel()
    crs = ['epsg:3857','epsg:4326']

    output_df = transformer.transform(
        input_df,
        crs = crs,
        input_labels = input_labels,
        output_labels = output_labels,
        **kwargs
    )

    return output_df
