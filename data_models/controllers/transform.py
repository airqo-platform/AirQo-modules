'''Transform Controllers

This module contains controller functions for interacting with DataModel
transform functionality.

'''

import pandas as pd
from models.DataModels import CoordinateTransformModel

def coord_transform(*args, **kwargs)-> pd.DataFrame:
    '''Transforms DataFrame columns from one coordinate system to another, see
    models.CoordinateTransformModel for more detail.

    Args:
        *args: Variable length argument list.
        **kwargs: Arbitrary keyword arguments.

    Returns:
        output_df: Dataframe with transformed columns
    '''
    # Create transformer
    transformer = CoordinateTransformModel()
    # Transform df columns based on input arguments
    output_df = transformer.transform(*args, **kwargs)

    return output_df

def latlon_xy_transform(
    input_df: pd.DataFrame,
    input_labels = ['latitude','longitude'],
    output_labels = ['x', 'y'],
    **kwargs
)-> pd.DataFrame:
    '''Transforms DataFrame columns from EPSG:4326 (lat,lon) to EPSG:3857 (X,Y).

    Args:
        input_df: DataFrame containing values to be converted
        input_labels (optional): Names of columns containing latitude and
            longitude values
        output_labels: Names of columns to be returned containing
            transformed coordinates
        **kwargs: Arbitrary keyword arguments.

    Returns:
        output_df: Dataframe with transformed columns
    '''
    # Create transformer and crs parameter list
    transformer = CoordinateTransformModel()
    crs = ['epsg:4326','epsg:3857']
    # Transform named latitude and longitude columns to X and Y
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
    '''Transforms DataFrame columns from EPSG:3857 (X,Y) to EPSG:4326 (lat,lon).

    Args:
        input_df: DataFrame containing values to be converted
        input_labels (optional): Names of columns containing X and Y values
        output_labels: Names of columns to be returned containing
            transformed coordinates
        **kwargs: Arbitrary keyword arguments.

    Returns:
        output_df: Dataframe with transformed columns
    '''
    # Create transformer and crs parameter list
    transformer = CoordinateTransformModel()
    crs = ['epsg:3857','epsg:4326']
    # Transform named X and Y columns to latitude and longitude
    output_df = transformer.transform(
        input_df,
        crs = crs,
        input_labels = input_labels,
        output_labels = output_labels,
        **kwargs
    )

    return output_df
