# EXPLICACION METODOS LISTA AGREGAR/ELIMINAR: Ejemplos de agregar y eliminar elementos en una lista en Python
# Métodos para agregar y eliminar elementos en listas de Python

lista = [1, 2, 3]

# append(): agrega un elemento al final
lista.append(4)  # Agrega 4 al final
print(lista)  # [1, 2, 3, 4]

# insert(): agrega un elemento en una posición específica
lista.insert(1, 10)  # Inserta 10 en la posición 1
print(lista)  # [1, 10, 2, 3, 4]

# extend(): agrega varios elementos al final
lista.extend([5, 6])  # Agrega varios elementos
print(lista)  # [1, 10, 2, 3, 4, 5, 6]

# remove(): elimina la primera aparición de un elemento
lista.remove(10)  # Elimina la primera aparición de 10
print(lista)  # [1, 2, 3, 4, 5, 6]

# pop(): elimina y retorna el último elemento (o el de una posición)
valor = lista.pop()  # Elimina y retorna el último elemento
print(valor)  # 6
valor2 = lista.pop(1)  # Elimina el elemento en la posición 1
print(valor2)  # 2
print(lista)  # [1, 3, 4, 5]
