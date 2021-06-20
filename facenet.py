from PIL import Image
from os import listdir
from os.path import isdir
from numpy import asarray, expand_dims
from tensorflow.keras.models import load_model
from sklearn.utils import shuffle
import pandas as pd

random_state = 42


def face_to_array(filename, size=(160, 160)):
    img = Image.open(filename)
    img = img.convert('RGB')
    img = img.resize(size)

    return asarray(img)


def load_faces(source):
    faces = list()

    for filename in listdir(source):
        path = source + filename
        try:
            faces.append(face_to_array(path))
        except:
            print("Erro ao ler imagem {}".format(path))

    return faces


def load(source):
    x, y = list(), list()
    for subdir in listdir(source):
        path = source + subdir + "\\"

        if not isdir(path):
            continue

        faces = load_faces(path)
        labels = [subdir for _ in range(len(faces))]
        print('Carregado %d faces da classe %s'% (len(faces), subdir))

        x.extend(faces)
        y.extend(labels)

    return asarray(x), asarray(y)


def get_embedding(model, face_pixels):
    face_pixels = face_pixels.astype('float32')
    mean, std = face_pixels.mean(), face_pixels.std()
    face_pixels = (face_pixels - mean) / std

    samples = expand_dims(face_pixels, axis=0)
    yhat = model.predict(samples)

    return yhat[0]


trainX, trainY = load(source="C:\\dataset\\faces\\")
print(trainX.shape, trainY.shape)
newTrainX = list()
model = load_model('facenet_keras.h5')

for face_pixels in trainX:
    embedding = get_embedding(model, face_pixels)
    newTrainX.append(embedding)

newTrainX = asarray(newTrainX)
print("Shape: ", newTrainX.shape)
#print(newTrainX)

df = pd.DataFrame(data=newTrainX)
df['target'] = trainY
df.to_csv('faces.csv')
x, y = shuffle(newTrainX, trainY, random_state=random_state)
