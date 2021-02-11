# AirQo DataModel Module

import pandas as pd

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
        df: pd.DataFrame,
        input_columns: list,
        target_columns = None
    )-> pd.DataFrame:
        '''Swaps columns of a DataFrame given input and target orders, the
        relative order of all the columns stays the same.

        e.g. if df has columns ['x', 'y', 'z'], input_columns = ['x', 'z'] and
        target_columns = ['z', 'x'] the function returns a DataFrame with
        columns ['z', 'y' 'x']

        Args:
            df: DataFrame containing columns to be swapped
            input_columns: Names of columns to be swapped in the order they
                appear in df
            target_columns (optional): Names of columns to be swapped in the
                desired order. If len(input_columns) == 2, target_columns does
                not need to be specified and input_columns are swapped

        Returns:
            df: DataFrame with swapped columns

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
        cols = list(df.columns)
        swap_cols = cols.copy()
        # Find indexes of input columns
        idx = [cols.index(col) for col in input_columns]
        # Fetch desired index order
        swap = [cols.index(col) for col in target_columns]
        # Reorder column names
        for i in range(len(idx)):
            cols[idx[i]] = swap_cols[swap[i]]
        # Reorder df
        df = df[cols]
        return df

class CoordinateTransformModel(BaseDataModel)
    def __init__(self, *args, **kwargs):
        super.__init__(self, *args, **kwargs)

    def coordinate_transform_model(
    input_df: pd.DataFrame,
    crs: list,
    input_labels: list,
    output_labels: list,
    replace_original = False
    )-> pd.DataFrame:

        #test inputs
        all_labels = input_labels + output_labels
        assert all([isinstance(lbl, str) for lbl in all_labels]) == True, 'input and output labels must be strings'
        assert len(crs) == 2, 'argument takes 2 inputs, crs_from, crs_to'
        assert len(input_labels) == len(output_labels), 'input and output labels must be of same length'

        #build pyproj transformer from input coordinate reference systems
        try:
            crs_from = pyproj.crs.CRS(crs[0])
            crs_to = pyproj.crs.CRS(crs[1])
        except CRSError:
            raise TypeError('Not a valid input for pyproj.crs.CRS()')
        transformer = pyproj.transformer.Transformer.from_crs(crs_from, crs_to)

        #get columns corresponding to input labels from dataframe
        inputs = tuple([input_df[lbl].to_numpy() for lbl in input_labels])
        #transform inputs and output to dataframe
        outputs = transformer.transform(*inputs)
        outputs = np.array(outputs).T
        output_df = pd.DataFrame(outputs, columns=output_labels)

        if replace_original == False:
            #concatenate inputs and outputs
            df = pd.concat([input_df, output_df], axis = 1)
        else:
            #copy input df and replace input columns
            df = input_df.copy(deep=True)
            df[input_labels] = output_df[output_labels]
            #replace output labels
            columns = dict(zip(input_labels,output_labels))
            df = df.rename(columns=columns)

        return df
