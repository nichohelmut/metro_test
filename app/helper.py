import pandas as pd
from pandas import DataFrame


def get_dummies_countries(df: DataFrame) -> DataFrame:
    df['Origin'] = df['Origin'].map({1: 'USA', 2: 'Europe', 3: 'Japan'})
    dataset = pd.get_dummies(df, columns=['Origin'], prefix='', prefix_sep='')

    return dataset
