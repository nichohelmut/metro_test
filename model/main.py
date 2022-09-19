import numpy as np
import tensorflow as tf

from helper import load_data, train_test_split
from model import model_fit, model_eval

data = load_data()


def main():
    train_features, test_features, train_labels, test_labels = train_test_split(data)

    normalizer = tf.keras.layers.Normalization(axis=-1)
    normalizer.adapt(np.array(train_features))

    history, model = model_fit(normalizer, train_features, train_labels)
    model_evalu = model_eval(test_features, test_labels, model)

    print("MPG prediction {}".format(model_evalu))

    model.save('./artifacts')


if __name__ == "__main__":
    main()
