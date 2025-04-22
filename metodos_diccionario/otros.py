# EXPLICACION METODOS DICCIONARIO OTROS: Ejemplos de copiar, limpiar y contar elementos en un diccionario en Python
# Otros métodos útiles de diccionarios en Python

datos = {"nombre": "Santiago", "edad": 17}

# copy(): crea una copia del diccionario
copia = datos.copy()
print(copia)

# clear(): elimina todos los elementos del diccionario
datos.clear()
print(datos)  # {}

# len(): cantidad de pares clave-valor
print(len(copia))  # 2
