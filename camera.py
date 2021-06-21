import cv2
from mtcnn import MTCNN

cam = cv2.VideoCapture(0)
detector = MTCNN()

while True:
    _, frame = cam.read()
    faces = detector.detect_faces(frame)

    for face in faces:
        x, y, w, h = face['box']

        pos_x, pos_y = (x, y), (x + w, y + h)
        color = (192, 255, 119)

        cv2.rectangle(frame, pos_x, pos_y, color, 2)

    cv2.imshow("FACEE_ID", frame)
    key = cv2.waitKey(1)
    if key == 27:
        break

cam.release()
cv2.destroyAllWindows()

