'''**DataModels**

This module contains DataModels, which provide functionality for interacting
with remote and internal databases, building local data files and using
pd.DataFrames to interface between models and data.

'''

import pandas as pd
import pyproj
from pyproj.exceptions import CRSError
import numpy as np

class BaseDataModel():
    '''Data models are used to standardise the logic for interaction between
    external and internal databases and DataFrames that are used to build model
    inputs.

    Generic utility functions that manipulate DataFrames are defined here and
    any further functionality should be abstracted into a subclass.

    Args:
        name (str, optional): Name of data model

    '''

    def __init__(self, name = None):
        if name:
            self.name = name

    def extract(self):
        raise NotImplementedError()

    def transform(self):
        raise NotImplementedError()

    def load(self):
        raise NotImplementedError()

    def swap_df_columns(
        self,
        input_df: pd.DataFrame,
        input_columns: list,
        target_columns = None
    )-> pd.DataFrame:
        '''Swaps columns of a DataFrame given input and target orders, the
        relative order of all the columns stays the same.

        e.g. if df has columns ['x', 'y', 'z'], input_columns = ['x', 'z'] and
        target_columns = ['z', 'x'] the function returns a DataFrame with
        columns ['z', 'y' 'x']

        Args:
            input_df: DataFrame containing columns to be swapped
            input_columns: Names of columns to be swapped in the order they
                appear in df
            target_columns (optional): Names of columns to be swapped in the
                desired order. If len(input_columns) == 2, target_columns does
                not need to be specified and input_columns are swapped

        Returns:
            output_df: DataFrame with swapped columns

        '''
        # Basic assertion tests, user must specify target_columns unless passing
        # 2 columns to be swapped
        if target_columns == None:
            assert len(input_columns) == 2, (
                'Must specify target_columns if input length is > 2'
            )
            target_columns = input_columns[::-1]
        assert len(input_columns) == len(target_columns)

        # Get column names of df and make deep copy
        cols = list(input_df.columns)
        swap_cols = cols.copy()
        # Find indexes of input columns
        idx = [cols.index(col) for col in input_columns]
        # Fetch desired index order
        swap = [cols.index(col) for col in target_columns]
        # Reorder column names
        for i in range(len(idx)):
            cols[idx[i]] = swap_cols[swap[i]]
        # Reorder df
        output_df = input_df[cols]
        return output_df

class CoordinateTransformModel(BaseDataModel):
    '''The CoordinateTransformModel is used to convert columns of coordinates
    using Coordinate Reference Systems (CRS) and pyrpoj.

    Args:
        *args: Variable length argument list.
        **kwargs: Arbitrary keyword arguments.

    '''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def transform(
        self,
        input_df: pd.DataFrame,
        crs: list,
        input_labels: list,
        output_labels: list,
        replace_original = None
    )-> pd.DataFrame:
        '''Converts the coordinate values of columns specified by input_labels
        between CRS's. The order of coordinates is specified by the CRS, not the
        user. For example, EPSG:4326 expects order (lat,lon), or (Y,X) in the
        Cartesian system and EPSG:3857 expects (X,Y). Therefore if we convert
        from 4326 to 3857, the transformer takes input in format (lat, lon)
        and outputs in format (X,Y) by default.

        Args:
            input_df: DataFrame containing values to be converted
            crs: List of crs_from, crs_to, the coordinate systems for the
                transform. These must be valid inputs for pyproj.crs.CRS()
            input_labels: Names of columns containing coordinates corresponding
                to crs_from
            output_labels: Names of columns to be returned containing
                transformed coordinates
            replace_original (bool, optional): If set to True, columns
                corresponding to input_labels are replaced with output
                coordinates, otherwise result is concatenated.

        Returns:
            output_df: DataFrame with transformed coordinates as included
                columns

        '''
        # Test inputs
        all_labels = input_labels + output_labels
        assert all([isinstance(lbl, str) for lbl in all_labels]) == True, (
            'Input and output labels must be strings'
        )
        assert len(crs) == 2, 'Argument takes 2 inputs, crs_from, crs_to'
        assert len(input_labels) == len(output_labels), (
            'Input and output labels must be of same length'
        )
        if replace_original is not None:
            assert type(replace_original) == bool, (
                'Replace_original must be of type bool if argument is used'
            )
        else:
            # Replace original columns by default
            replace_original = True

        # Build pyproj transformer from input coordinate reference systems,
        # raise TypeError if pyproj raises a CRSError
        try:
            crs_from = pyproj.crs.CRS(crs[0])
            crs_to = pyproj.crs.CRS(crs[1])
        except CRSError:
            raise TypeError('Not a valid input for pyproj.crs.CRS()')
        transformer = pyproj.transformer.Transformer.from_crs(
            crs_from,
            crs_to
        )

        # Get columns corresponding to input labels from dataframe
        inputs = tuple([input_df[lbl].to_numpy() for lbl in input_labels])
        #transform inputs and output to dataframe
        outputs = transformer.transform(*inputs)
        outputs = np.array(outputs).T
        output_df = pd.DataFrame(outputs, columns=output_labels)

        if replace_original == False:
            # Concatenate inputs and outputs
            df = pd.concat([input_df, output_df], axis = 1)
        else:
            # Copy input df and replace input columns
            df = input_df.copy(deep=True)
            df[input_labels] = output_df[output_labels]
            # Replace output labels
            columns = dict(zip(input_labels,output_labels))
            output_df = df.rename(columns=columns)

        return output_df
