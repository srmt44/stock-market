import tensorflow as tf
from tensorflow import keras

def build_model(input_shape):
    model = keras.models.Sequential()
    model.add(keras.layers.LSTM(30, return_sequences=True, input_shape=input_shape))
    # model.add(keras.layers.Dropout(0.2))
    model.add(keras.layers.LSTM(20, activation='relu'))
    # model.add(keras.layers.Dropout(0.2))
    model.add(keras.layers.Dense(21))
    return model