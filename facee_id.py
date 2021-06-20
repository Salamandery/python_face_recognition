import numpy as np
from PIL import Image
from mtcnn.mtcnn import MTCNN
from tensorflow.keras.models import load_model
from sklearn.preprocessing import Normalizer
import cv2

#p = ["BILLGATES", "FELIPE LOBO MAL", "LARRYPAGE", "MARKZUCKERBERG", "RODOLFO", "TAYLINE", "TIRIRICA"]
p = ["FELIPE", "RODOLFO"]
num_class = len(p)

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

facenet = load_model("facenet_keras.h5")
model = load_model("faces.h5")
detector = MTCNN()


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


while True:
    _, frame = cap.read()
    faces = detector.detect_faces(frame)

    for face in faces:
        confidence = face['confidence']*100

        x1, y1, w, h = face['box']
        face = extract_face(frame, face['box'])

        font = cv2.FONT_HERSHEY_SIMPLEX
        font_scale = 0.5
        font_x = (x1, y1 - 10)
        pos_x, pos_y = (x1, y1), (x1 + w, y1 + h)

        if confidence >= 98:
            face = face.astype("float32") / 255
            emb = get_embedding(facenet, face)

            tensor = np.expand_dims(emb, axis=0)
            #norm = Normalizer(norm='l2')
            #tensor = norm.transform(tensor)
            classe = model.predict_classes(tensor)[0]
            print(tensor)
            print("classe: ", classe)
            prob = model.predict(tensor)
            print("prob_predict: ", prob)
            prob = prob[0][classe] * 100
            print("prob_classe: ", prob)

            print(prob)
            if prob >= 98:
                user = str(p[classe]).upper()

                color = (192, 255, 119)

                cv2.rectangle(frame, pos_x, pos_y, color, 2)
                cv2.putText(frame, user, font_x, font,
                            fontScale=font_scale, color=color, thickness=1)
            else:
                color = (0, 0, 255)

                cv2.rectangle(frame, pos_x, pos_y, color, 2)
                cv2.putText(frame, "DESCONHECIDO", font_x, font,
                            fontScale=font_scale, color=color, thickness=1)
        else:
            color = (0, 0, 255)

            cv2.rectangle(frame, pos_x, pos_y, color, 2)
            cv2.putText(frame, "DESCONHECIDO", font_x, font,
                        fontScale=font_scale, color=(255, 255, 255), thickness=1)

    cv2.imshow("FACEE_ID", frame)
    key = cv2.waitKey(1)

    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
