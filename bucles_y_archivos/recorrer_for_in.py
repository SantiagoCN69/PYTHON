# EXPLICACION recorrer colecciones con for...in en Python
# Ejemplos de cómo usar for...in para recorrer listas, tuplas, conjuntos y diccionarios

# Recorrer una lista
lista = [10, 20, 30]
for elemento in lista:
    print(f"Elemento de la lista: {elemento}")

# Recorrer una tupla
tupla = ('a', 'b', 'c')
for letra in tupla:
    print(f"Letra de la tupla: {letra}")

# Recorrer un conjunto
conjunto = {1, 2, 3}
for numero in conjunto:
    print(f"Número del conjunto: {numero}")

# Recorrer un diccionario (solo claves)
dic = {'nombre': 'Ana', 'edad': 25}
for clave in dic:
    print(f"Clave del diccionario: {clave}")

# Recorrer un diccionario (claves y valores)
for clave, valor in dic.items():
    print(f"Clave: {clave}, Valor: {valor}")
