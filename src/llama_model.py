from llama_cpp import Llama

modelo = None

def cargar_llama(ruta_modelo):
    global modelo
    modelo = Llama(model_path=ruta_modelo, n_ctx=2048)

def generar_respuesta(contexto, pregunta):
    prompt = f"""
Eres un asistente legal experto en normativa militar chilena. Usa el siguiente contexto legal para responder la pregunta de forma clara, formal, y completa.

Contexto:
\"\"\"
{contexto}
\"\"\"

Pregunta:
{pregunta}

Tu respuesta debe ser bien redactada y fácil de entender para un ciudadano chileno que no necesariamente tiene formación militar o legal. Evita tecnicismos sin explicar su significado. Si no encuentras suficiente información en el contexto, acláralo en la respuesta.
"""

    from llama_cpp import Llama
    llama = Llama(
    model_path="modelo/mistral.gguf",
    n_ctx=2048,         # Contexto razonable para tareas legales
    n_threads=4,        # Usa todos los núcleos de tu CPU (ajusta según tu hardware)
    n_batch=512,        # Procesa más tokens por paso (mayor velocidad)
    verbose=False       # Silencia logs innecesarios
    )

    output = llama(
        prompt,
        max_tokens=256,     # Menor cantidad de tokens generados = más rápido
        temperature=0.7,
        top_p=0.9,
        stop=["</s>"]
    )

    return output["choices"][0]["text"].strip()
