import src.rect_pic as rectExecProcess
import src.facenet as facenetExecProcess
import src.load_model_keras as loadModelKeras
import src.facee_id as facee_id
import src.camera as camera_debug
import src.data as database_debug


SOURCE = "C:\\dataset\\fotos\\"
TARGET = "C:\\dataset\\faces\\"

switcher = {
    1: rectExecProcess,
    2: facenetExecProcess,
    3: loadModelKeras,
    4: facee_id,
    5: camera_debug,
    6: database_debug
}

if __name__ == '__main__':
    print("1 - TRATAMENTO DE IMAGEM;")
    print("2 - GERAR EMBEDDING DAS IMAGENS;")
    print("3 - TREINAMENTO FACENET DE RECONHECIMENTO;")
    print("4 - INICIAR FACEE_ID FACE RECOGNITION;")
    print("5 - DEPURAR CAMERA.")
    goTo = int(input("Escolha uma opcao: "))

    if goTo == 1:
        switcher.get(goTo, "OPCAO INVALIDA").execProcess(SOURCE, TARGET)
    elif goTo == 2:
        switcher.get(goTo, "OPCAO INVALIDA").execProcess(TARGET)
    elif goTo == 5:
        switcher.get(goTo, "OPCAO INVALIDA").webcam.get_current_frame()
    elif goTo == 6:
        switcher.get(goTo, "OPCAO INVALIDA").execProcess("SELECT * FROM V$SESSION")
    else:
        switcher.get(goTo, "OPCAO INVALIDA").execProcess()
