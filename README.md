# 🤖 Python Face Recognition System

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/TensorFlow-2.8+-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white"/>
  <img src="https://img.shields.io/badge/OpenCV-4.5+-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white"/>
  <img src="https://img.shields.io/badge/Keras-2.8+-D00000?style=for-the-badge&logo=keras&logoColor=white"/>
  <img src="https://img.shields.io/badge/scikit--learn-1.0+-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white"/>
  <img src="https://img.shields.io/badge/MTCNN-Face%20Detection-00A8E1?style=for-the-badge&logo=face-recognition&logoColor=white"/>
</p>

<div align="center">
  <b>🇧🇷 Português | <a href="#english-version">🇺🇸 English below</a></b>
</div>

---

## 📑 Sumário | Table of Contents
- [Sobre o Projeto | About](#sobre-o-projeto--about)
- [Tecnologias | Technologies](#tecnologias--technologies)
- [Requisitos do Sistema | System Requirements](#requisitos-do-sistema--system-requirements)
- [Estrutura | Structure](#estrutura--structure)
- [Funcionalidades | Features](#funcionalidades--features)
- [Instalação e Execução | Setup & Run](#instalação-e-execução--setup--run)
- [Exemplos de Uso | Usage Examples](#exemplos-de-uso--usage-examples)
- [Configurações | Configuration](#configurações--configuration)
- [Troubleshooting | Troubleshooting](#troubleshooting--troubleshooting)
- [Contribuição | Contributing](#contribuição--contributing)
- [Licença | License](#licença--license)
- [Autor | Author](#autor--author)

---

## Sobre o Projeto | About

**PT-BR:**
> Sistema completo de reconhecimento facial em Python utilizando TensorFlow, Keras e MTCNN. O projeto inclui processamento de imagens, extração de embeddings, treinamento de modelos de machine learning e reconhecimento facial em tempo real com integração a banco de dados Oracle.

**EN:**
> Complete facial recognition system in Python using TensorFlow, Keras, and MTCNN. The project includes image processing, embedding extraction, machine learning model training, and real-time facial recognition with Oracle database integration.

---

## 🚀 Tecnologias | Technologies

**PT-BR:**
- **Python 3.8+**: Linguagem principal do projeto
- **TensorFlow 2.8+**: Framework de machine learning para treinamento de modelos
- **Keras**: API de alto nível para redes neurais
- **OpenCV 4.5+**: Processamento de imagens e captura de vídeo
- **MTCNN**: Detecção facial multi-task cascaded convolutional networks
- **scikit-learn**: Algoritmos de machine learning (SVM, KNN)
- **Pandas & NumPy**: Manipulação de dados e arrays
- **PIL (Pillow)**: Processamento de imagens
- **cx_Oracle**: Conexão com banco de dados Oracle
- **PyTorch**: Suporte para GPU (CUDA)

**EN:**
- **Python 3.8+**: Main project language
- **TensorFlow 2.8+**: Machine learning framework for model training
- **Keras**: High-level API for neural networks
- **OpenCV 4.5+**: Image processing and video capture
- **MTCNN**: Multi-task cascaded convolutional networks for face detection
- **scikit-learn**: Machine learning algorithms (SVM, KNN)
- **Pandas & NumPy**: Data manipulation and arrays
- **PIL (Pillow)**: Image processing
- **cx_Oracle**: Oracle database connection
- **PyTorch**: GPU support (CUDA)

---

## 💻 Requisitos do Sistema | System Requirements

**PT-BR:**
- **Sistema Operacional**: Windows 10/11, Linux, macOS
- **Python**: 3.8 ou superior
- **RAM**: Mínimo 8GB (recomendado 16GB+)
- **GPU**: NVIDIA GPU com CUDA (opcional, mas recomendado)
- **Armazenamento**: 2GB de espaço livre
- **Câmera**: Webcam ou câmera IP
- **Banco de Dados**: Oracle Database 11g ou superior

**EN:**
- **Operating System**: Windows 10/11, Linux, macOS
- **Python**: 3.8 or higher
- **RAM**: Minimum 8GB (recommended 16GB+)
- **GPU**: NVIDIA GPU with CUDA (optional, but recommended)
- **Storage**: 2GB free space
- **Camera**: Webcam or IP camera
- **Database**: Oracle Database 11g or higher

---

## 🗂️ Estrutura | Structure
```
python_face_recognition/
├── main.py                          # Menu principal do sistema
├── src/
│   ├── facee_id.py                  # Sistema principal de reconhecimento facial
│   ├── facenet.py                   # Geração de embeddings faciais
│   ├── rect_pic.py                  # Extração e processamento de faces
│   ├── load_model_keras.py          # Treinamento do modelo Keras
│   ├── load_model_svm.py            # Treinamento do modelo SVM
│   ├── load_model_knn.py            # Treinamento do modelo KNN
│   ├── binary_model_keras.py        # Modelo binário Keras
│   ├── camera.py                    # Captura de câmera básica
│   ├── camera_mtcnn.py              # Captura com detecção MTCNN
│   ├── data.py                      # Integração com banco de dados
│   ├── bin/                         # Modelos treinados e arquivos binários
│   │   ├── facenet_keras.h5         # Modelo FaceNet pré-treinado
│   │   ├── faces.h5                 # Modelo de reconhecimento treinado
│   │   └── faces_svm.sav            # Modelo SVM treinado
│   └── *.sql                        # Scripts SQL para banco de dados
└── README.md
```

---

## ⚡ Funcionalidades | Features

**PT-BR:**

### 🔍 **Processamento de Imagens**
- Extração automática de faces de imagens
- Redimensionamento para 160x160 pixels
- Geração de variações (flip horizontal, escala de cinza)
- Detecção facial usando MTCNN

### 🧠 **Machine Learning**
- Geração de embeddings faciais com FaceNet
- Treinamento de modelos Keras (Dense Neural Networks)
- Suporte a modelos SVM e KNN
- Normalização L2 dos embeddings
- Validação cruzada e métricas de performance

### 👤 **Reconhecimento Facial**
- Reconhecimento em tempo real via webcam
- Integração com banco de dados Oracle
- Registro automático de entrada/saída
- Classificação de usuários conhecidos vs desconhecidos
- Interface visual com retângulos coloridos

### 🗄️ **Banco de Dados**
- Conexão Oracle com cx_Oracle
- Registro de presença (entrada/saída)
- Consultas personalizadas
- Transações automáticas

**EN:**

### 🔍 **Image Processing**
- Automatic face extraction from images
- Resizing to 160x160 pixels
- Generation of variations (horizontal flip, grayscale)
- Face detection using MTCNN

### 🧠 **Machine Learning**
- Facial embedding generation with FaceNet
- Keras model training (Dense Neural Networks)
- SVM and KNN model support
- L2 normalization of embeddings
- Cross-validation and performance metrics

### 👤 **Facial Recognition**
- Real-time recognition via webcam
- Oracle database integration
- Automatic entry/exit registration
- Known vs unknown user classification
- Visual interface with colored rectangles

### 🗄️ **Database**
- Oracle connection with cx_Oracle
- Attendance registration (entry/exit)
- Custom queries
- Automatic transactions

---

## ⚙️ Instalação e Execução | Setup & Run

**PT-BR:**
1. **Pré-requisitos:** Python 3.8+, pip, Oracle Client
2. **Clone o repositório:**
   ```bash
   git clone <repository-url>
   cd python_face_recognition
   ```
3. **Instale as dependências:**
   ```bash
   pip install tensorflow opencv-python mtcnn scikit-learn pandas numpy pillow cx-oracle torch
   ```
4. **Configure o banco de dados:**
   - Configure `src/bin/db_con.py` com suas credenciais Oracle
   - Execute os scripts SQL para criar as tabelas necessárias
5. **Execute o sistema:**
   ```bash
   python main.py
   ```

**EN:**
1. **Prerequisites:** Python 3.8+, pip, Oracle Client
2. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd python_face_recognition
   ```
3. **Install dependencies:**
   ```bash
   pip install tensorflow opencv-python mtcnn scikit-learn pandas numpy pillow cx-oracle torch
   ```
4. **Configure database:**
   - Configure `src/bin/db_con.py` with your Oracle credentials
   - Execute SQL scripts to create necessary tables
5. **Run the system:**
   ```bash
   python main.py
   ```

---

## 📖 Exemplos de Uso | Usage Examples

**PT-BR:**

### **1. Processamento de Imagens**
```bash
python main.py
# Selecione opção 1 para extrair faces das imagens
```

### **2. Treinamento do Modelo**
```bash
python main.py
# Selecione opção 2 para gerar embeddings
# Selecione opção 3 para treinar o modelo
```

### **3. Reconhecimento Facial**
```bash
python main.py
# Selecione opção 4 para iniciar reconhecimento
```

**EN:**

### **1. Image Processing**
```bash
python main.py
# Select option 1 to extract faces from images
```

### **2. Model Training**
```bash
python main.py
# Select option 2 to generate embeddings
# Select option 3 to train the model
```

### **3. Facial Recognition**
```bash
python main.py
# Select option 4 to start recognition
```

---

## 🔧 Configurações | Configuration

**PT-BR:**

### **Menu Principal (main.py)**
- **Opção 1**: Tratamento de imagem (extração de faces)
- **Opção 2**: Geração de embeddings das imagens
- **Opção 3**: Treinamento FaceNet de reconhecimento
- **Opção 4**: Iniciar FACEE_ID face recognition
- **Opção 5**: Depurar câmera
- **Opção 6**: Consultas de banco de dados

### **Configurações de Câmera**
- Resolução: 1280x720
- Fonte: webcam ou arquivo de vídeo
- Suporte a RTSP para câmeras IP

### **Modelos de Machine Learning**
- **Keras**: Rede neural densa com dropout
- **SVM**: Support Vector Machine para classificação
- **KNN**: K-Nearest Neighbors para classificação

**EN:**

### **Main Menu (main.py)**
- **Option 1**: Image processing (face extraction)
- **Option 2**: Generate image embeddings
- **Option 3**: FaceNet recognition training
- **Option 4**: Start FACEE_ID face recognition
- **Option 5**: Debug camera
- **Option 6**: Database queries

### **Camera Settings**
- Resolution: 1280x720
- Source: webcam or video file
- RTSP support for IP cameras

### **Machine Learning Models**
- **Keras**: Dense neural network with dropout
- **SVM**: Support Vector Machine for classification
- **KNN**: K-Nearest Neighbors for classification

---

## 🔧 Troubleshooting | Troubleshooting

**PT-BR:**

### **Problemas Comuns**
- **Erro de câmera**: Verifique se a webcam está conectada e funcionando
- **Erro de banco**: Confirme as credenciais Oracle em `src/bin/db_con.py`
- **Erro de GPU**: Instale CUDA e cuDNN para TensorFlow
- **Erro de memória**: Reduza o batch_size nos modelos

### **Logs e Debug**
- Use a opção 5 para testar a câmera
- Use a opção 6 para testar conexão com banco
- Verifique os logs de erro no console

**EN:**

### **Common Issues**
- **Camera error**: Check if webcam is connected and working
- **Database error**: Confirm Oracle credentials in `src/bin/db_con.py`
- **GPU error**: Install CUDA and cuDNN for TensorFlow
- **Memory error**: Reduce batch_size in models

### **Logs and Debug**
- Use option 5 to test camera
- Use option 6 to test database connection
- Check error logs in console

---

## 🤝 Contribuição | Contributing

**PT-BR:**
Contribuições são bem-vindas! Para contribuir:

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

**EN:**
Contributions are welcome! To contribute:

1. Fork the project
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 Licença | License

**PT-BR:**
Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

**EN:**
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Autor | Author

**PT-BR:**

<div align="center">

**Rodolfo M. F. Abreu**  
Desenvolvedor de software apaixonado por tecnologia, aprendizado contínuo e boas práticas de programação. Sempre em busca de novos desafios e oportunidades para colaborar em projetos inovadores.

[![GitHub](https://img.shields.io/badge/GitHub-rodolfomfabreu-black?style=for-the-badge&logo=github)](https://github.com/salamandery)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Rodolfo%20Abreu-blue?style=for-the-badge&logo=linkedin)](https://linkedin.com/in/rodolfo-marques-ferreira-de-abreu/)

Sinta-se à vontade para entrar em contato para dúvidas, sugestões ou colaborações!

</div>

**EN:**

<div align="center">

**Rodolfo M. F. Abreu**  
Software developer passionate about technology, continuous learning, and best programming practices. Always looking for new challenges and opportunities to collaborate on innovative projects.

[![GitHub](https://img.shields.io/badge/GitHub-rodolfomfabreu-black?style=for-the-badge&logo=github)](https://github.com/salamandery)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Rodolfo%20Abreu-blue?style=for-the-badge&logo=linkedin)](https://linkedin.com/in/rodolfo-marques-ferreira-de-abreu/)

Feel free to get in touch for questions, suggestions, or collaborations!

</div>

---

<div align="center">
  <b>Feito com 💙 para estudos de Inteligência Artificial, Machine Learning e Reconhecimento Facial.<br/>
  Made with 💙 for Artificial Intelligence, Machine Learning and Facial Recognition studies.</b>
</div>

---

<div align="center" id="english-version">
  <b>🇺🇸 English version above | <a href="#top">🇧🇷 Versão em português acima</a></b>
</div>