import cv2
import os
from datetime import datetime

QUANTIDADE_FOTOS = 300
CAMERA = 0

classificador_face = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

def criar_diretorio(nome_pasta):
    caminho = os.path.join("photos", nome_pasta)
    if not os.path.exists(caminho):
        os.makedirs(caminho)
    return caminho


def capturar_fotos(nome_pessoa, num_fotos=QUANTIDADE_FOTOS):

    caminho_pasta = criar_diretorio(nome_pessoa)
    captura_video = cv2.VideoCapture(CAMERA)
    
    contador_fotos = 0
    print(f"Capturando fotos para '{nome_pessoa}'...")
    print('-=' * 10)

    while contador_fotos < num_fotos:
        print(f"Foto {contador_fotos + 1}/{num_fotos}")
        resultado, quadro = captura_video.read()
        if not resultado:
            print("Erro ao acessar a webcam!")
            break

        quadro_cinza = cv2.cvtColor(quadro, cv2.COLOR_BGR2GRAY)
        faces = classificador_face.detectMultiScale(
            quadro_cinza, scaleFactor=1.2, minNeighbors=5, minSize=(40, 40)
        )

        for (x, y, w, h) in faces:
            cv2.rectangle(quadro, (x, y), (x + w, y + h), (0, 255, 0), 2)

            face_detectada = quadro_cinza[y : y + h, x : x + w]

            caminho_arquivo = os.path.join(
                caminho_pasta, f"{datetime.now().isoformat().replace(':', '_')}.jpg"
            )
            face_redimensionada = cv2.resize(face_detectada, (100, 100))
            cv2.imwrite(caminho_arquivo, face_redimensionada)

            contador_fotos += 1
            if contador_fotos >= num_fotos:
                break

        cv2.namedWindow("Captura de Fotos", cv2.WINDOW_NORMAL)
        cv2.setWindowProperty("Captura de Fotos", cv2.WND_PROP_TOPMOST, 1)

        cv2.imshow("Captura de Fotos", quadro)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    captura_video.release()
    cv2.destroyAllWindows()
    print(f"Captura concluída! Fotos salvas em: {caminho_pasta}")

nome = input("Digite o nome da pessoa: ").strip()
if nome:
    capturar_fotos(nome)
else:
    print("Nome inválido. Encerrando o programa.")
