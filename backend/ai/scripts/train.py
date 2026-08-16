import os
import numpy as np
import pandas as pd
from PIL import Image

BASE_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..", "..")
)
DATASET_DIR = os.path.join(BASE_DIR, "dataset")

IMAGE_SIZE = (128, 128)
def load_dataset(folder_path):
    csv_file = os.path.join(folder_path, "_classes.csv")
    df = pd.read_csv(csv_file)
    images = []
    labels = []

    for _, row in df.iterrows():
        image_path = os.path.join(folder_path, row["filename"])

        img = Image.open(image_path)
        img = img.resize(IMAGE_SIZE)
        img = np.array(img)
        images.append(img)
        labels.append([
            row["fate"],
            row["head"],
            row["heart"],
            row["life"],
            row["palm_width"],
            row["line_density"]
        ])
    return np.array(images), np.array(labels)

X_train, y_train = load_dataset(os.path.join(DATASET_DIR, "train"))
X_valid, y_valid = load_dataset(os.path.join(DATASET_DIR, "valid"))
X_test, y_test = load_dataset(os.path.join(DATASET_DIR, "test"))

train_df = pd.read_csv(
    os.path.join(DATASET_DIR, "train", "_classes.csv")
)
print(y_train[:10])

print("Label counts:")
print(train_df[["fate", "head", "heart", "life"]].sum())

print("\nTotal samples:")
print(len(train_df))

print("\nNumber of 0s:")
print(len(train_df) - train_df[["fate", "head", "heart", "life", "palm_width", "line_density"]].sum())

# Normalize images
X_train = X_train.astype("float32") / 255.0
X_valid = X_valid.astype("float32") / 255.0
X_test = X_test.astype("float32") / 255.0

#print(y_train.mean(axis=0))
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import (Conv2D, MaxPooling2D, Flatten, Dense, Dropout, BatchNormalization,
    LeakyReLU)

model = Sequential([
    Conv2D(32, (3,3), padding="same", input_shape=(128,128,3)),
    BatchNormalization(),
    LeakyReLU(negative_slope=0.01),
    MaxPooling2D(2,2),

    Conv2D(64, (3,3), padding="same"),
    BatchNormalization(),
    LeakyReLU(negative_slope=0.01),
    MaxPooling2D(2,2),

    Conv2D(128, (3,3), padding="same"),
    BatchNormalization(),
    LeakyReLU(negative_slope=0.01),
    MaxPooling2D(2,2),

    Flatten(),

    Dense(256),
    LeakyReLU(negative_slope=0.01),
    Dropout(0.4),

    Dense(128),
    LeakyReLU(negative_slope=0.01),
    Dropout(0.3),

    Dense(6, activation="sigmoid")
])

from tensorflow.keras.optimizers import Adam

optimizer = Adam(learning_rate=0.0001)
model.compile(
    optimizer=optimizer,
    loss="binary_crossentropy",
    metrics=[tf.keras.metrics.BinaryAccuracy()]
)

from tensorflow.keras.callbacks import EarlyStopping

early_stop = EarlyStopping(
    monitor="val_loss",
    patience=5,
    restore_best_weights=True
)

history = model.fit(
    X_train,
    y_train,
    validation_data=(X_valid, y_valid),
    epochs=10,
    batch_size=32
)

model.save("saved_models/palm_model.keras")
print("Model Saved Successfully!")