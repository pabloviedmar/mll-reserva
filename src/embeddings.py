from sentence_transformers import SentenceTransformer
import numpy as np
import faiss
import os
import pickle

def generar_embeddings_y_indice(fragmentos, ruta_salida):
    modelo = SentenceTransformer("all-MiniLM-L6-v2")

    # Usamos solo el contenido para generar vectores
    vectores = modelo.encode([frag["contenido"] for frag in fragmentos])

    index = faiss.IndexFlatL2(vectores.shape[1])
    index.add(np.array(vectores))

    os.makedirs(os.path.dirname(ruta_salida), exist_ok=True)
    faiss.write_index(index, ruta_salida + "/faiss.index")

    # Guardamos los fragmentos con 'origen' y 'contenido'
    with open(ruta_salida + "/fragmentos.pkl", "wb") as f:
        pickle.dump(fragmentos, f)

    return index, fragmentos
