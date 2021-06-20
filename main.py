from mtcnn import MTCNN
from PIL import Image
from os import listdir
from os.path import isdir
from pathlib import Path
from numpy import array, asarray

detector = MTCNN()


def extract_face(filename, size=(160, 160)):
    img = Image.open(filename)
    img = img.convert('RGB')
    arr = asarray(img)

    results = detector.detect_faces(arr)
    x1, y1, width, height = results[0]['box']
    x1, y1 = abs(x1), abs(y1)
    x2, y2 = x1 + width, y1 + height

    face = arr[y1:y2, x1:x2]

    image = Image.fromarray(face)
    image = image.resize(size)

    return image


def flip_face(image):
    img = image.transpose(Image.FLIP_LEFT_RIGHT)
    return img


def load_faces(source, target):
    for filename in listdir(source):
        path = source + filename
        path_tg = target + filename
        path_tg_flip = target + "flipped"+filename
        path_tg_gs = target + "gs"+filename

        try:
            face = extract_face(path)
            flip = flip_face(face)
            darken = face.convert('1')
            face.save(path_tg, 'JPEG', quality=100, optimize=True, progressive=True)
            flip.save(path_tg_flip, 'JPEG', quality=100, optimize=True, progressive=True)
            darken.save(path_tg_gs, 'JPEG', quality=100, optimize=True, progressive=True)
        except:
            print("Erro ao ler imagem {}".format(path))


def discovery_dir(source, target):
    for subdir in listdir(source):
        path = source + subdir + "\\"
        path_target = target + subdir + "\\"
        Path(target + subdir + "\\").mkdir(parents=True, exist_ok=True)

        if not isdir(path):
            continue

        load_faces(path, path_target)


if __name__ == '__main__':
    discovery_dir("C:\\dataset\\fotos\\",
                  "C:\\dataset\\faces\\")
