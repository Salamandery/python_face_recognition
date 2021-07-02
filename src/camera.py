import cv2
import ctypes
from tensorflow.python.client import device_lib
print(device_lib.list_local_devices())

user32 = ctypes.windll.user32
Cw, Ch = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

target = 0
#target = "rtsp://10.42.117.199:554/user=facceid&password=Heat1234&channel=1&stream=0.sdp"
#target = "rtsp://192.168.15.199:554/user=facceid&password=Heat1234&channel=1&stream=0.sdp"

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (1280, 720))


def execProcess():
    print(cv2.getBuildInformation())
    cam = cv2.VideoCapture(target)
    cam.set(cv2.CAP_PROP_FRAME_WIDTH, Cw)
    cam.set(cv2.CAP_PROP_FRAME_HEIGHT, Ch)

    while True:
        _, frame = cam.read()
        cv2.imshow("FACEE_ID", frame)
        out.write(frame)
        key = cv2.waitKey(1)
        if key == 27:
            break

    out.release()
    cam.release()
    cv2.destroyAllWindows()


def main():
    print("CAMERA DEBUG")


if __name__ == "__main__":
    execProcess()
