import pandas as pd
from pandas import DataFrame


def get_dummies_countries(df: DataFrame) -> DataFrame:
    df['Origin'] = df['Origin'].map({1: 'USA', 2: 'Europe', 3: 'Japan'})
    dataset = pd.get_dummies(df, columns=['Origin'], prefix='', prefix_sep='')

    return dataset


def load_data() -> DataFrame:
    url = 'http://archive.ics.uci.edu/ml/machine-learning-databases/auto-mpg/auto-mpg.data'
    column_names = ['MPG', 'Cylinders', 'Displacement', 'Horsepower', 'Weight',
                    'Acceleration', 'Model Year', 'Origin']

    raw_dataset = pd.read_csv(url, names=column_names,
                              na_values='?', comment='\t',
                              sep=' ', skipinitialspace=True)

    dataset = raw_dataset.dropna()

    dataset_dummies = get_dummies_countries(dataset)

    return dataset_dummies


def train_test_split(data: DataFrame) -> tuple:
    train_dataset = data.sample(frac=0.8, random_state=0)
    test_dataset = data.drop(train_dataset.index)

    train_features = train_dataset.copy()
    test_features = test_dataset.copy()

    train_labels = train_features.pop('MPG')
    test_labels = test_features.pop('MPG')

    return train_features, test_features, train_labels, test_labels
