import inspect
import os

import numpy as np
import tensorflow as tf

from helper import load_data
from model import model_fit, model_eval

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)

data = load_data()


def main():
    train_dataset = data.sample(frac=0.8, random_state=0)
    test_dataset = data.drop(train_dataset.index)

    train_features = train_dataset.copy()
    test_features = test_dataset.copy()

    train_labels = train_features.pop('MPG')
    test_labels = test_features.pop('MPG')

    normalizer = tf.keras.layers.Normalization(axis=-1)
    normalizer.adapt(np.array(train_features))

    history, model = model_fit(normalizer, train_features, train_labels)
    model_evalu = model_eval(test_features, test_labels, model)

    print("MPG prediction {}".format(model_evalu))

    model.save('{}/app/artifacts'.format(parent_dir))


if __name__ == "__main__":
    main()
