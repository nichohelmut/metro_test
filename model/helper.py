import matplotlib.pyplot as plt
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


def plot_loss(history):
    plt.plot(history.history['loss'], label='loss')
    plt.plot(history.history['val_loss'], label='val_loss')
    plt.ylim([0, 10])
    plt.xlabel('Epoch')
    plt.ylabel('Error [MPG]')
    plt.legend()
    plt.grid(True)
