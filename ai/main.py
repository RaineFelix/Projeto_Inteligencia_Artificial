import cv2
import os
import numpy as np

CAMERA = 0

classificador_face = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

captura_video = cv2.VideoCapture(CAMERA)

reconhecedor = cv2.face.LBPHFaceRecognizer_create()

def treinar_reconhecedor(caminho_dados):
    print('Treinando o modelo...Isso pode demorar um pouco!')
    faces = []
    labels = []
    dicionario_labels = {}
    contador_labels = 0

    for index, (root, dirs, files) in enumerate(os.walk(caminho_dados)):
        for file_index, file in enumerate(files):
            print(f'Processando ({file_index + 1}/{len(files)}) {file}:')
            if file.endswith("jpg") or file.endswith("png"):
                caminho = os.path.join(root, file)
                label = os.path.basename(root)

                if label not in dicionario_labels:
                    dicionario_labels[label] = contador_labels
                    contador_labels += 1

                img = cv2.imread(caminho, cv2.IMREAD_GRAYSCALE)
                faces.append(img)
                labels.append(dicionario_labels[label])

    reconhecedor.train(faces, np.array(labels))
    print('Treinamento concluído!')
    return dicionario_labels

dicionario_labels = treinar_reconhecedor("photos")

def detectar_caixa_delimitadora(vid):
    imagem_cinza = cv2.cvtColor(vid, cv2.COLOR_BGR2GRAY)
    faces = classificador_face.detectMultiScale(imagem_cinza, 1.2, 5, minSize=(40, 40))
    for (x, y, w, h) in faces:
        cv2.rectangle(vid, (x, y), (x + w, y + h), (0, 255, 0), 4)
    return faces, imagem_cinza

print('-=' * 10)
print('Inicializando reconhecimento facial...')
print('Pressione "q" para sair')

while True:
    resultado, quadro_video = captura_video.read()
    if not resultado:
        break

    faces, quadro_cinza = detectar_caixa_delimitadora(quadro_video)
    nomes_reconhecidos = []
    acesso_liberado = False

    for face in faces:
        x, y, w, h = face
        face_detectada = quadro_cinza[y:y+h, x:x+w]
        face_redimensionada = cv2.resize(face_detectada, (100, 100))

        try:
            label, confianca = reconhecedor.predict(face_redimensionada)
        except:
            continue

        nome_reconhecido = "Desconhecido"

        if confianca > 70 and confianca < 100:
            for nome, id in dicionario_labels.items():
                if id == label:
                    nome_reconhecido = nome
                    acesso_liberado = True
                    break

        nomes_reconhecidos.append((nome_reconhecido, x, y))

    for (nome_reconhecido, x, y) in nomes_reconhecidos:
        cv2.putText(quadro_video, nome_reconhecido, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    if acesso_liberado:
        cv2.putText(quadro_video, "ACESSO LIBERADO!", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 255, 0), 3)

    cv2.imshow("Reconhecimento Facial", quadro_video)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

captura_video.release()
cv2.destroyAllWindows()
