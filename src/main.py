from pdf_reader import leer_pdf
from preprocess import dividir_texto
from embeddings import generar_embeddings_y_indice
from search import cargar_indice, buscar_contexto
from llama_model import cargar_llama, generar_respuesta
from logger import guardar_en_historial
from historial import guardar_en_historial, ver_historial
from corrector import corregir_texto
from voz import hablar

import os

PDF_PATH = "data/DL-2306_12-SEP-1978.pdf"
INDICE_PATH = "outputs/indices"
MODELO_LLAMA_PATH = "modelo/mistral.gguf"  

def preparar_sistema():
    print("📄 Leyendo PDF...")
    texto = leer_pdf(PDF_PATH)
    partes = dividir_texto(texto)
    print(f"🔹 Fragmentos creados: {len(partes)}")

    print("💾 Generando índice FAISS...")
    generar_embeddings_y_indice(partes, INDICE_PATH)

def responder_pregunta(pregunta):
    print("🔍 Buscando contexto...")
    index, fragmentos = cargar_indice(INDICE_PATH)
    partes_relevantes = buscar_contexto(pregunta, index, fragmentos)

    contexto = "\n".join(partes_relevantes)

    print("🧠 Generando respuesta con Mistral...")
    cargar_llama(MODELO_LLAMA_PATH)
    respuesta = generar_respuesta(contexto, pregunta)

    respuesta_corregida = corregir_texto(respuesta)

    print("\n📝 Respuesta:")
    print(respuesta_corregida)

    escuchar = input("¿Deseas escuchar la respuesta? (s/n): ").lower()
    if escuchar == "s":
        hablar(respuesta_corregida)

    guardar_en_historial(pregunta, respuesta_corregida)
    


if __name__ == "__main__":
    if not os.path.exists("outputs/indices/faiss.index"):
        preparar_sistema()

    opcion = input("¿Qué deseas hacer? (1: Preguntar | 2: Ver historial): ")

    if opcion == "1":
        pregunta = input("Escribe tu pregunta legal: ")
        responder_pregunta(pregunta)

        escuchar = input("¿Deseas escuchar la respuesta? (s/n): ").lower()
        if escuchar == "s":
            with open("outputs/indices/respuestas.txt", "r", encoding="utf-8") as f:
                lineas = f.readlines()
                if lineas:
                    ultima_respuesta = lineas[-1].strip()
                    hablar(ultima_respuesta)
    elif opcion == "2":
        ver_historial()
    else:
        print("❌ Opción no válida.")


