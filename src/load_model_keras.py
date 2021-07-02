from tensorflow.keras.callbacks import ModelCheckpoint, ReduceLROnPlateau
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import Normalizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from mlxtend.plotting import plot_confusion_matrix
from tensorflow.keras.utils import to_categorical
from tensorflow.keras import models
from tensorflow.keras import layers
from sklearn.utils import shuffle
import matplotlib.pyplot as plt
from os.path import dirname
import numpy as np
import pandas as pd

BIN_DIR = dirname(__file__) + "\\bin\\"
FACENET_DIR = BIN_DIR + "facenet_keras.h5"
FACES_CSV = BIN_DIR + "faces.csv"
FACES_VALIDATION_CSV = BIN_DIR + "faces.csv"
FACES_UNKNOW = BIN_DIR + "unknow.csv"

batch_size = 8
input_shape = (128,)
random_state = 42
alpha = 1e-5
epoch = 100


def print_confusion_matrix(model_name, valY, yhat_val):
    cm = confusion_matrix(valY, yhat_val)
    total = sum(sum(cm))
    acc = (cm[0, 0] + cm[1, 1]) / total
    sensitivity = cm[0, 0] / (cm[0, 0] + cm[0, 1])
    specificity = cm[1, 1] / (cm[1, 0] + cm[1, 1])

    print("MODEL: {}".format(model_name))
    print("ACCURACY: {:.4f}".format(acc))
    print("SENSITIVE: {:.4f}".format(sensitivity))
    print("SPECITIVY: {:.4f}".format(specificity))

    fig, ax = plot_confusion_matrix(conf_mat=cm, figsize=(5, 5))
    plt.show()


def execProcess():
    df = pd.read_csv(FACES_CSV)
    df_unknow = pd.read_csv(FACES_UNKNOW)

    df = pd.concat([df_unknow, df])

    X = np.array(df.drop("target", axis=1))
    y = np.array(df.target)

    X, y = shuffle(X, y, random_state=random_state)
    trainX, valX, trainY, valY = train_test_split(X, y, train_size=0.20, random_state=random_state)
    in_encoder = Normalizer(norm='l2')
    trainX = in_encoder.transform(trainX)
    valX = in_encoder.transform(valX)

    np.unique(trainY)
    print(np.unique(trainY))
    print(np.unique(valY))
    classes = len(np.unique(trainY))

    out_encoder = LabelEncoder()
    out_encoder.fit(trainY)
    LabelEncoder()
    trainY = out_encoder.transform(trainY)

    out_encoder = LabelEncoder()
    out_encoder.fit(valY)
    LabelEncoder()
    valY = out_encoder.transform(valY)

    trainY = to_categorical(trainY)
    valY = to_categorical(valY)

    filepath = BIN_DIR+"faces_weights.hdf5"
    checkpoint = ModelCheckpoint(filepath, monitor='val_acc', verbose=1, save_best_only=True, mode='max')
    lr_reduce = ReduceLROnPlateau(monitor='val_acc', factor=0.1, min_delta=alpha, patience=5, verbose=1)
    callbacks = [checkpoint, lr_reduce]

    model = models.Sequential()
    model.add(layers.Dense(128, activation="relu", input_shape=input_shape))
    model.add(layers.Dropout(0.5))
    model.add(layers.Dense(classes, activation="softmax"))

    model.summary()
    model.compile(optimizer="adam",
                  loss="categorical_crossentropy",
                  metrics=['accuracy'])
    history = model.fit(trainX, trainY,
                        epochs=epoch, batch_size=batch_size,
                        validation_data=(valX, valY))

    plt.plot(history.history['accuracy'])
    plt.plot(history.history['val_accuracy'])
    plt.title("model accuracy")
    plt.ylabel("acc")
    plt.xlabel("epoch")
    plt.legend(['train', 'test'], loc='upper left')
    plt.show()

    plt.plot(history.history['loss'])
    plt.plot(history.history['val_loss'])
    plt.title("model loss")
    plt.ylabel("loss")
    plt.xlabel("epoch")
    plt.legend(['train', 'test'], loc='upper left')
    plt.show()

    yhat_train = model.predict(trainX)
    yhat_val = model.predict(valX)

    yhat_val = np.argmax(yhat_val, axis=1)
    valY = np.argmax(valY, axis=1)

    print_confusion_matrix("KERAS", valY, yhat_val)
    model.save(BIN_DIR + "faces.h5")


def main():
    print("KERAS TRAINING")


if __name__ == "__main__":
    execProcess()
