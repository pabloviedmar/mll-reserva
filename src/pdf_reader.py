import fitz

def leer_pdf(path):
    texto = ""
    with fitz.open(path) as doc:
        for pagina in doc:
            texto += pagina.get_text()
    return texto
