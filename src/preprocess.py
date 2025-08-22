import re

def limpiar_texto(texto):
    texto = texto.replace("\n", " ")       # unificamos saltos de línea
    texto = re.sub(r"\s+", " ", texto)     # múltiples espacios → 1 espacio
    texto = texto.strip()
    return texto

def dividir_texto(texto, max_long=500, solapamiento=50):
    lineas = texto.split("\n")
    fragmentos = []
    actual = ""
    fragmento_id = 0

    for linea in lineas:
        linea = linea.strip()
        if not linea:
            continue

        if len(actual) + len(linea) < max_long:
            actual += linea + " "
        else:
            fragmentos.append({
                "contenido": actual.strip(),
                "origen": f"Fragmento {fragmento_id}"
            })
            fragmento_id += 1
            actual = linea + " "

    if actual:
        fragmentos.append({
            "contenido": actual.strip(),
            "origen": f"Fragmento {fragmento_id}"
        })

    return fragmentos

