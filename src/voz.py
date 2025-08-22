import pyttsx3

def hablar(texto):
    engine = pyttsx3.init()
    engine.setProperty('rate', 160)     # velocidad de habla
    engine.setProperty('volume', 1.0)   # volumen máximo

    # Opcional: cambiar la voz (solo en Windows)
    voces = engine.getProperty('voices')
    engine.setProperty('voice', voces[0].id)  # puedes probar con voces[1] si quieres voz femenina

    engine.say(texto)
    engine.runAndWait()
