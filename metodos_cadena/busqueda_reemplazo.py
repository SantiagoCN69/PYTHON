# EXPLICACION METODOS CADENA BUSQUEDA/REEMPLAZO: Ejemplos de buscar, contar y reemplazar subcadenas en Python
# Métodos de búsqueda y reemplazo en cadenas de texto en Python

texto = "Me gusta Python. Python es genial."

# find(): busca la primera aparición y devuelve el índice
print(texto.find("Python"))  # 9

# rfind(): busca la última aparición
print(texto.rfind("Python"))  # 17

# count(): cuenta cuántas veces aparece un substring
print(texto.count("Python"))  # 2

# replace(): reemplaza una subcadena por otra
nuevo_texto = texto.replace("Python", "JavaScript")
print(nuevo_texto)  # 'Me gusta JavaScript. JavaScript es genial.'
