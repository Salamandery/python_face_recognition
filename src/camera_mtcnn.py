import cv2
import ctypes
from mtcnn import MTCNN

user32 = ctypes.windll.user32
Cw, Ch = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

#target = "rtsp://10.42.117.199:554/user=facceid&password=Heat1234&channel=1&stream=0.sdp"
target = "rtsp://192.168.15.199:554/user=facceid&password=Heat1234&channel=1&stream=0.sdp"
detector = MTCNN()


def extract_face(img, box, size=(160, 160)):
    arr = np.asarray(img)
    x1, y1, width, height = box

    x2, y2 = x1 + width, y1 + height
    face = arr[y1:y2, x1:x2]

    image = Image.fromarray(face)
    image = image.resize(size)

    return np.asarray(image)


def execProcess():
    cam = cv2.VideoCapture(target)
    cam.set(cv2.CAP_PROP_FRAME_WIDTH, Cw)
    cam.set(cv2.CAP_PROP_FRAME_HEIGHT, Ch)

    while True:
        _, frame = cam.read()

        faces = detector.detect_faces(frame)

        for face in faces:
            x1, y1, w, h = face['box']
            color = (192, 255, 119)

            pos_x, pos_y = (x1, y1), (x1 + w, y1 + h)
            cv2.rectangle(frame, pos_x, pos_y, color, 2)

        cv2.imshow("FACEE_ID", frame)
        key = cv2.waitKey(1)
        if key == 27:
            break

    cam.release()
    cv2.destroyAllWindows()


def main():
    print("CAMERA DEBUG")


if __name__ == "__main__":
    execProcess()
