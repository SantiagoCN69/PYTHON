# Métodos para ordenar y revertir listas en Python

letras = ['b', 'a', 'd', 'c']

# sort(): ordena la lista (modifica la lista original)
letras.sort()
print(letras)  # ['a', 'b', 'c', 'd']

# reverse(): revierte el orden de los elementos
letras.reverse()
print(letras)  # ['d', 'c', 'b', 'a']

# sorted(): devuelve una nueva lista ordenada (no modifica la original)
numeros = [3, 1, 4, 2]
print(sorted(numeros))  # [1, 2, 3, 4]
print(numeros)  # [3, 1, 4, 2]
