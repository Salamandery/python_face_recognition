import numpy as np
import pandas as pd
from sklearn.utils import shuffle
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix
from mlxtend.plotting import plot_confusion_matrix
import matplotlib.pyplot as plt


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


df = pd.read_csv("faces.csv")

X = np.array(df.drop("target", axis=1))
y = np.array(df.target)

trainX, trainY = shuffle(X, y, random_state=0)
out_encoder = LabelEncoder()

out_encoder.fit(trainY)
LabelEncoder()
trainY = out_encoder.transform(trainY)

df_val = pd.read_csv("faces.csv")

valX = np.array(df_val.drop("target", axis=1))
valY = np.array(df_val.target)

out_encoder.fit(valY)
LabelEncoder()

valY = out_encoder.transform(valY)

knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(trainX, trainY)

KNeighborsClassifier(algorithm='auto', leaf_size=30, metric='minkowski',
                     metric_params=None, n_jobs=None, n_neighbors=5, p=2, weights='uniform')

yhat_train = knn.predict(trainX)
yhat_val = knn.predict(valX)

print_confusion_matrix("KNN", valY, yhat_val)

