import os

HISTORIAL_PATH = "outputs/respuestas.txt"

def guardar_en_historial(pregunta, respuesta):
    os.makedirs(os.path.dirname(HISTORIAL_PATH), exist_ok=True)
    with open(HISTORIAL_PATH, "a", encoding="utf-8") as f:
        f.write(f"🟢 Pregunta: {pregunta}\n")
        f.write(f"📘 Respuesta: {respuesta}\n")
        f.write("-" * 60 + "\n")

def ver_historial():
    if not os.path.exists(HISTORIAL_PATH):
        print("⚠️ No hay historial disponible.")
        return

    print("\n📜 Historial de Preguntas y Respuestas:\n")
    with open(HISTORIAL_PATH, "r", encoding="utf-8") as f:
        print(f.read())
