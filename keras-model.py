import os
import numpy as np
import keras
from keras import layers
import tensorflow as tf
import matplotlib.pyplot as plt
import sys

save_name = "default_save"
model_epochs = 10

if len(sys.argv) > 2:
    save_name = sys.argv[1]
    model_epochs = int(sys.argv[2])

image_size = (32, 32)
batch_size = 128

train_ds, val_ds = keras.utils.image_dataset_from_directory(
    "CIFAR-10-images/train",
    validation_split=0.2,
    subset="both",
    label_mode="int",
    seed=1337,
    image_size=image_size,
    batch_size=batch_size
)

def make_model(input_shape, num_classes):
    inputs = keras.Input(shape=input_shape)

    x = layers.Conv2D(64, 3, padding="same", activation="relu")(inputs)
    x = layers.MaxPooling2D(2)(x)
    x = layers.Conv2D(128, 3, padding="same", activation="relu")(x)
    x = layers.MaxPooling2D(2)(x)
    x = layers.Conv2D(256, 3, padding="same", activation="relu")(x)
    x = layers.GlobalAveragePooling2D()(x)
    x = layers.Dense(128, activation="relu")(x)
    x = layers.Dropout(0.25)(x)
    outputs = layers.Dense(num_classes, activation=None)(x)

    return keras.Model(inputs, outputs)

model = make_model(input_shape=image_size + (3,), num_classes=10)

model.compile(
    optimizer=keras.optimizers.Adam(1e-4),
    loss=keras.losses.SparseCategoricalCrossentropy(from_logits=True),
    metrics=[keras.metrics.CategoricalAccuracy(name="acc")],
)

model.fit(
    train_ds,
    epochs=model_epochs,
    validation_data=val_ds,
)

model.save(f'{save_name}.keras')

loss, accuracy = model.evaluate(train_ds)

with open(f'{save_name}-accuracy.txt', 'w') as file:
    file.write(str(accuracy))
