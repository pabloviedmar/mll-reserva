import os
from datetime import datetime

def guardar_en_historial(pregunta, respuesta, ruta_salida="outputs/respuestas.txt"):
    os.makedirs(os.path.dirname(ruta_salida), exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(ruta_salida, "a", encoding="utf-8") as f:
        f.write(f"🕒 {timestamp}\n")
        f.write(f"❓ Pregunta: {pregunta}\n")
        f.write(f"💬 Respuesta: {respuesta}\n")
        f.write("=" * 50 + "\n")
