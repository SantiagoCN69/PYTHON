# EXPLICACION conjuntos en Python
# Ejemplos de cómo crear y usar conjuntos (set) en Python

# Crear un conjunto vacío
a = set()
print(f"Conjunto vacío: {a}")

#crear con 
a2 = set([1, 2, 3, 4])
print(f"Conjunto con elementos: {a2}")

# Crear un conjunto con elementos
b = {1, 2, 3, 4}
print(f"Conjunto con elementos: {b}")

# Los conjuntos no permiten elementos repetidos
duplicados = {1, 2, 2, 3, 4, 4}
print(f"Conjunto sin duplicados: {duplicados}")

# Convertir una lista a conjunto
lista = [1, 2, 2, 3, 4, 4]
conjunto_desde_lista = set(lista)
print(f"Lista original: {lista}")
print(f"Lista convertida a conjunto: {conjunto_desde_lista}")

# Recorrer un conjunto
for elemento in b:
    print(f"Elemento: {elemento}")

# Agregar y eliminar elementos
a = set()
print(f"Conjunto original: {a}")
a.add(5)
print(f"Conjunto después de agregar 5: {a}")
a.discard(5)
print(f"Conjunto después de eliminar 5: {a}")

# Operaciones de conjuntos
x = {1, 2, 3}
y = {3, 4, 5}
print(f"Unión: {x | y}")        # {1, 2, 3, 4, 5}
print(f"Intersección: {x & y}") # {3}
print(f"Diferencia: {x - y}")   # {1, 2}
print(f"Diferencia simétrica: {x ^ y}") # {1, 2, 4, 5}