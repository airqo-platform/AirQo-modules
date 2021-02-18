from data_models.models.DataModels import BaseDataModel
import pytest
import pandas as pd

@pytest.fixture
def data_model():
    return BaseDataModel('test')

@pytest.fixture
def test_df():
    a = [1, 2, 3]
    b = [4, 5, 6]
    c = [7, 8, 9]

    df = pd.DataFrame({'a': a, 'b': b, 'c': c})

    return df

def test_model_name(data_model):
    assert data_model.name == 'test'

def test_swap_columns(data_model, test_df):

    swap_ab = data_model.swap_df_columns(test_df, ['a', 'b'])
    swap_ca = data_model.swap_df_columns(
        test_df,
        ['a', 'b', 'c'],
        ['c', 'b', 'a']
    )
    swap_all = data_model.swap_df_columns(
        test_df,
        ['a', 'b', 'c'],
        ['c', 'a', 'b']
    )

    assert (swap_ab == test_df[['b', 'a', 'c']]).all(axis=None)
    assert (swap_ca == test_df[['c','b','a']]).all(axis=None)
    assert (swap_all == test_df[['c','a','b']]).all(axis=None)
