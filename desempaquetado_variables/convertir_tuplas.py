# EXPLICACION convertir tuplas en Python

# Convertir una tupla a lista
tupla = (1, 2, 3)
lista = list(tupla)
print(f"Tupla original: {tupla}")
print(f"Convertida a lista: {lista}")

# Convertir una lista a tupla
nueva_tupla = tuple(lista)
print(f"Lista original: {lista}")
print(f"Convertida a tupla: {nueva_tupla}")

# Convertir una tupla a string (con join)
tupla_letras = ('h', 'o', 'l', 'a')
string = ''.join(tupla_letras)
print(f"Tupla de letras: {tupla_letras}")
print(f"Convertida a string: {string}")

# Convertir un string a tupla
otro_string = "python"
tupla_desde_string = tuple(otro_string)
print(f"String original: {otro_string}")
print(f"Convertido a tupla: {tupla_desde_string}")

# Ejemplo de desempaquetado doble (duple)
tupla_pares = ((1, 2), (3, 4), (5, 6))
for x, y in tupla_pares:
    print(f"x = {x}, y = {y}")

# También puedes desempaquetar directamente en variables
par = (10, 20)
a, b = par
print(f"a = {a}, b = {b}")
