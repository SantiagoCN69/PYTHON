# Métodos para buscar, contar y acceder por índice en listas de Python

numeros = [1, 2, 3, 2, 4, 2, 5]

# index(): devuelve el índice de la primera aparición de un valor
print(numeros.index(2))  # 1

# count(): cuenta cuántas veces aparece un elemento
print(numeros.count(2))  # 3

# Acceso por índice: obtener el elemento en una posición específica
print(numeros[0])   # 1 (primer elemento)
print(numeros[3])   # 2 (cuarto elemento)

# Acceso por índice negativo: desde el final
print(numeros[-1])  # 5 (último elemento)
print(numeros[-2])  # 4 (penúltimo elemento)
