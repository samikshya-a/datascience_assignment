#!/usr/bin/env python
# coding: utf-8

# In[2]:


import tensorflow as tf
from tensorflow.keras import layers

# Load and preprocess the MNIST dataset
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()
x_train = x_train.reshape(-1, 28, 28, 1).astype("float32") / 255.0
x_test = x_test.reshape(-1, 28, 28, 1).astype("float32") / 255.0
num_classes = 10

# Architecture 1: Simple Convolutional Neural Network
def cnn_architecture_1():
    model = tf.keras.Sequential([
        layers.Conv2D(32, (3, 3), activation="relu", input_shape=(28, 28, 1)),
        layers.MaxPooling2D((2, 2)),
        layers.Flatten(),
        layers.Dense(64, activation="relu"),
        layers.Dense(num_classes, activation="softmax")
    ])
    return model

# Architecture 2: Deeper Convolutional Neural Network
def cnn_architecture_2():
    model = tf.keras.Sequential([
        layers.Conv2D(32, (3, 3), activation="relu", input_shape=(28, 28, 1)),
        layers.MaxPooling2D((2, 2)),
        layers.Conv2D(64, (3, 3), activation="relu"),
        layers.MaxPooling2D((2, 2)),
        layers.Flatten(),
        layers.Dense(64, activation="relu"),
        layers.Dense(num_classes, activation="softmax")
    ])
    return model

# Architecture 3: Increased Filter Sizes Convolutional Neural Network
def cnn_architecture_3():
    model = tf.keras.Sequential([
        layers.Conv2D(64, (5, 5), activation="relu", input_shape=(28, 28, 1)),
        layers.MaxPooling2D((2, 2)),
        layers.Conv2D(128, (5, 5), activation="relu"),
        layers.MaxPooling2D((2, 2)),
        layers.Flatten(),
        layers.Dense(128, activation="relu"),
        layers.Dense(num_classes, activation="softmax")
    ])
    return model

# Compile and train the models
models = [cnn_architecture_1(), cnn_architecture_2(), cnn_architecture_3()]
history = []

for model in models:
    model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])
    model.fit(x_train, y_train, batch_size=128, epochs=10, verbose=1)
    _, accuracy = model.evaluate(x_test, y_test, verbose=0)
    history.append(accuracy)

# Create a comparison table
print("Architecture\tAccuracy")
print("-------------------------")
print("1\t\t{:.2f}%".format(history[0] * 100))
print("2\t\t{:.2f}%".format(history[1] * 100))
print("3\t\t{:.2f}%".format(history[2] * 100))


# In[ ]:




