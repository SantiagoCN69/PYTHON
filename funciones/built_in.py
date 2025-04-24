# Ejemplos de funciones built-in de Python con comentarios explicativos

# sum(): Suma todos los elementos de un iterable (lista, tupla, etc.)
numeros = [1, 2, 3, 4, 5]
suma = sum(numeros)  # Resultado: 15
print("sum(numeros):", suma)

# round(): Redondea un número flotante al entero más cercano o a los decimales indicados
pi = 3.14159
pi_redondeado = round(pi, 2)  # Resultado: 3.14
print("round(pi, 2):", pi_redondeado)

# bool(): Convierte un valor a booleano (True o False)
valor = 0
es_verdadero = bool(valor)  # Resultado: False
print("bool(valor):", es_verdadero)

# all(): Devuelve True si todos los elementos de un iterable son verdaderos
valores = [True, True, False]
todos_verdaderos = all(valores)  # Resultado: False
print("all(valores):", todos_verdaderos)

# max(): Devuelve el valor máximo de un iterable
maximo = max(numeros)  # Resultado: 5
print("max(numeros):", maximo)

# min(): Devuelve el valor mínimo de un iterable
minimo = min(numeros)  # Resultado: 1
print("min(numeros):", minimo)