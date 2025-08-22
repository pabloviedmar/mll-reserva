# 🛡️ MLL RESERVA – Chatbot Legal con IA

**MLL RESERVA** es un chatbot legal técnico que responde preguntas en lenguaje natural sobre normativas chilenas, como la Ley 2306 y el Código del Trabajo. Utiliza modelos de lenguaje locales (LLMs) y técnicas de recuperación aumentada (RAG) para generar respuestas precisas y confiables, con salida por voz.

---

## 🚀 Características

- 📄 Lectura y análisis de documentos legales en PDF.
- 🔍 Búsqueda semántica con FAISS.
- 🧠 Generación de respuestas con Mistral 7B (formato GGUF).
- 🗣️ Respuestas habladas con Text-to-Speech (TTS).
- 🧾 Historial de preguntas y respuestas.
- 🛠️ 100% local, sin conexión a internet.

---

## 📦 Requisitos

- Python 3.10+
- CPU con soporte AVX2 (recomendado)
- Sistema operativo: Windows, Linux o macOS

---

## 🧪 Instalación

1. **Clona el repositorio**
   ```bash
   git clone https://github.com/tuusuario/mll-reserva.git
   cd mll-reserva
   ```
2. **Intalar entorno virtual**
   ```shell
   virtualenv env
   ```
2. **Intalar librerias**
   ```shell
   pip install -r requirements.txt
   ```


## ▶️ Uso
Ejecuta el chatbot desde la raíz del proyecto:
   ```shell
   python src/main.py
   ```

   Opciones disponibles:
   1. Realizar una pregunta legal.

   2. Ver historial de preguntas y respuestas.

      Al final de cada respuesta, puedes optar por escucharla en voz alta.

## 📁 Estructura del proyecto

MLL RESERVA/

├── data/                  # Documentos legales en PDF (ej. DL-2306_12-SEP-1978.pdf)

├── modelo/                # Archivo GGUF del modelo Mistral (ej. mistral.gguf)

├── outputs/

    └── indices/           # Índices FAISS y archivos auxiliares

        ├── faiss.index

        ├── fragmentos.pkl

        └── respuestas.txt

├── src/                   # Código fuente del chatbot

    ├── main.py            # Script principal del sistema

    ├── voz.py             # Módulo de voz (Text-to-Speech)

    ├── corrector.py       # Corrección de texto generado

    ├── embeddings.py      # Generación de embeddings

    ├── historial.py       # Manejo del historial de preguntas/respuestas

    ├── llama_model.py     # Carga y ejecución del modelo Mistral

    ├── logger.py          # Registro de eventos

    ├── pdf_reader.py      # Lectura de documentos PDF

    ├── preprocess.py      # División y limpieza de texto legal

    ├── search.py          # Búsqueda semántica en fragmentos

 │   └── requirements.txt   # Lista de dependencias

├── README.md              # Documentación del proyecto

├── env/                   # Entorno virtual de Python
