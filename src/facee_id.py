import numpy as np
from src.data import execProcess as executeQuery
from PIL import Image
from mtcnn.mtcnn import MTCNN
from tensorflow.keras.models import load_model
from sklearn.preprocessing import Normalizer
import cv2
import os
import torch

# CONFIGURAÇÕES
BIN_DIR = os.path.dirname(__file__) + "\\bin\\"
FACENET_DIR = BIN_DIR + "facenet_keras.h5"
FACES_DIR = BIN_DIR + "faces.h5"
#CAM_TARGET = "rtsp://192.168.15.199:554/user=facceid&password=Heat1234&channel=1&stream=0.sdp"
CAM_TARGET = "output1.mp4"
facenet = load_model(FACENET_DIR)
model = load_model(FACES_DIR)
detector = MTCNN()

p = [0, 1, 2, 3]
num_class = len(p)

cap = cv2.VideoCapture(CAM_TARGET)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

device = torch.cuda.is_available()
print(device)


def extract_face(img, box, size=(160, 160)):
    arr = np.asarray(img)
    x1, y1, width, height = box

    x2, y2 = x1 + width, y1 + height
    face = arr[y1:y2, x1:x2]

    image = Image.fromarray(face)
    image = image.resize(size)

    return np.asarray(image)


def get_embedding(model, face_pixels):
    face_pixels = face_pixels.astype('float32')
    mean, std = face_pixels.mean(), face_pixels.std()
    face_pixels = (face_pixels - mean) / std

    samples = np.expand_dims(face_pixels, axis=0)
    yhat = model.predict(samples)

    return yhat[0]


def detectFaces(frame):
    faces = detector.detect_faces(frame)

    if len(faces) >= 1:
        for face in faces:
            confidence = face['confidence'] * 100

            if confidence >= 98:
                x1, y1, w, h = face['box']
                face = extract_face(frame, face['box'])

                font = cv2.FONT_HERSHEY_SIMPLEX
                font_scale = 0.5
                font_x = (x1, y1 - 10)
                pos_x, pos_y = (x1, y1), (x1 + w, y1 + h)

                face = face.astype("float32") / 255
                emb = get_embedding(facenet, face)

                tensor = np.expand_dims(emb, axis=0)
                norm = Normalizer(norm='l2')
                tensor = norm.transform(tensor)
                classe = model.predict_classes(tensor)[0]

                prob = model.predict(tensor)
                prob = prob[0][classe] * 100

                if prob >= 98:
                    user = str(p[classe]).upper()
                    if not classe == 0:
                        color = (192, 255, 119)

                        select = "SELECT CD_PRESTADOR FROM REG_ENT WHERE TO_CHAR(DT_REG_ENT, 'DD/MM/YYYY') = TO_CHAR(SYSDATE, 'DD/MM/YYYY') AND CD_PRESTADOR = {} AND TP_REG_ENT = 'E'".format(user)
                        entrou = executeQuery(select, "SELECT")

                        if not len(entrou) > 0:
                            query = "INSERT INTO REG_ENT (CD_REG_ENT, CD_PRESTADOR, DT_REG_ENT, TP_REG_ENT) VALUES (REG_ENT_SEQ.NEXTVAL, {}, SYSDATE, 'E')".format(user)
                            executeQuery(query, "INSERT")
                    else:
                        color = (0, 0, 255)

                    cv2.rectangle(frame, pos_x, pos_y, color, 2)
                    cv2.putText(frame, user, font_x, font,
                                fontScale=font_scale, color=color, thickness=1)
                else:
                    color = (0, 0, 255)

                    cv2.rectangle(frame, pos_x, pos_y, color, 2)
                    cv2.putText(frame, "DESCONHECIDO", font_x, font,
                                fontScale=font_scale, color=color, thickness=1)
            else:
                x1, y1, w, h = face['box']
                pos_x, pos_y = (x1, y1), (x1 + w, y1 + h)
                color = (255, 0, 0)

                cv2.rectangle(frame, pos_x, pos_y, color, 2)


def execProcess():
    while True:
        ret, frame = cap.read()

        try:
            detectFaces(frame)

            cv2.imshow("FACEE_ID", frame)
            key = cv2.waitKey(1)

            if key == 27:
                break
        except Exception as e:
            print(e)

    cap.release()
    cv2.destroyAllWindows()


def main():
    print("ABRINDO FACEE_ID RECONHECIMENTO FACIAL")


if __name__ == "__main__":
    execProcess()
