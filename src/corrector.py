import language_tool_python

# Creamos un objeto LanguageTool para español
tool = language_tool_python.LanguageTool('es')

def corregir_texto(texto):
    # Busca errores en el texto
    matches = tool.check(texto)
    # Aplica las correcciones
    texto_corregido = language_tool_python.utils.correct(texto, matches)
    return texto_corregido
