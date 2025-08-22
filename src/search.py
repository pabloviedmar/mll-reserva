import faiss
import pickle
import numpy as np
from sentence_transformers import SentenceTransformer

def cargar_indice(ruta_salida):
    index = faiss.read_index(ruta_salida + "/faiss.index")
    with open(ruta_salida + "/fragmentos.pkl", "rb") as f:
        fragmentos = pickle.load(f)
    return index, fragmentos

def buscar_contexto(pregunta, index, fragmentos, top_k=5):
    modelo = SentenceTransformer("all-MiniLM-L6-v2")
    vector_pregunta = modelo.encode([pregunta])
    
    # Realiza la búsqueda en el índice FAISS
    distancias, indices = index.search(np.array(vector_pregunta), top_k)
    
    resultados = []
    for idx in indices[0]:
        if idx < len(fragmentos):  # Evitar errores si el índice es inválido
            resultados.append(fragmentos[idx])
    return resultados
