import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

# Make NumPy printouts easier to read.
np.set_printoptions(precision=3, suppress=True)


def build_and_compile_model(norm):
    model = keras.Sequential([
        norm,
        layers.Dense(64, activation='relu'),
        layers.Dense(64, activation='relu'),
        layers.Dense(1)
    ])

    model.compile(loss='mean_absolute_error',
                  optimizer=tf.keras.optimizers.Adam(0.001))
    return model


def model_fit(normalizer, train_features, train_labels):
    dnn_model = build_and_compile_model(normalizer)
    history = dnn_model.fit(
        train_features,
        train_labels,
        validation_split=0.2,
        verbose=1, epochs=100)

    return history, dnn_model


def model_eval(test_features, test_labels, model) -> float:
    test_result = model.evaluate(test_features, test_labels, verbose=0)
    return test_result
