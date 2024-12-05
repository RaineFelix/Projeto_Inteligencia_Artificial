# Projeto de Reconhecimento Facial 

Este projeto utiliza Python e OpenCV para criar uma aplicação de reconhecimento facial. 

## Índice
- [Descrição](#descrição)
- [Pré-requisitos](#pré-requisitos)
- [Instalação](#instalação)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Utilização do projeto](#utilização-do-projeto)
- [Contribuidores](#contribuidores)

---

## Descrição
O projeto é uma aplicação de reconhecimento facial baseada em aprendizado local usando o algoritmo LBPH (Local Binary Patterns Histograms). Ele detecta faces usando classificadores Haar e permite identificar rostos previamente cadastrados. As imagens para treinamento são capturadas diretamente da câmera, possibilitando o treinamento personalizado para diferentes usuários. Além disso, este trabalho é referente à matéria de IA na FATEC Mogi Mirim, ministrada pelo professor Marcos Roberto Nava.


---

## Pré-requisitos
- Python 3.6 ou superior
- Câmera funcional para capturar imagens
- OpenCV e outras dependências instaladas (ver seção de instalação)

---

## Instalação
1. Certifique-se de ter o Python 3.6+ instalado no sistema.
2. Instale as bibliotecas necessárias executando o comando abaixo no terminal:
   ```bash
   pip install opencv-python opencv-contrib-python numpy


## Estrutura do Projeto

```bash
IA/
│
├── main.py          # Código principal para reconhecimento facial
├── treinar.py       # Código para capturar imagens e treinar o modelo
├── photos/          # Diretório onde as imagens capturadas são armazenadas
```

## Utilização do projeto

### Passo 1: Captura de Imagens
Execute o script `treinar.py` para capturar imagens:

```bash
python treinar.py
```

1- Insira o nome do usuário quando solicitado.

2- Posicione-se na frente da câmera e tire fotos de diferentes ângulos até atingir o número configurado (padrão: 200 fotos).

3- As fotos serão salvas na pasta photos.

### Passo 2: Treinamento do Modelo

O modelo será automaticamente treinado ao executar o script principal main.py.

```bash
python main.py
```

### Passo 3: Reconhecimento Facial

Execute o script main.py:

```bash
python main.py
```


1- O programa iniciará o reconhecimento facial em tempo real.

2- As faces detectadas aparecerão com caixas delimitadoras e os nomes associados serão exibidos na tela.

3- Pressione q para encerrar o programa.

## Contribuidores

- Fábio Eloy Passos
- Larissa Gabrielle de Souza
- Raíne Vitória Felix Morreira
