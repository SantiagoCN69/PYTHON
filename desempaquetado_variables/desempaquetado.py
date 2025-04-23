# EXPLICACION desempaquetado de variables en Python

# Desempaquetado de una lista
datos = [1, 2, 3]
a, b, c = datos
print(a)
print(b)
print(c)
print(f"a = {a}, b = {b}, c = {c}")  # a = 1, b = 2, c = 3

# Desempaquetado de una tupla
coordenadas = (10, 20)
x, y = coordenadas
print(x)
print(y)
print(f"x = {x}, y = {y}")  # x = 10, y = 20

# Desempaquetado de cadena (string)
nombre = "ok"
letra1, letra2 = nombre
print(letra1)
print(letra2)
print(f"letra1 = {letra1}, letra2 = {letra2}")  # letra1 = o, letra2 = k

# Desempaquetado con * para capturar varios valores
valores = [1, 2, 3, 4, 5]
primero, *resto = valores
print(primero)
print(resto)
print(f"primero = {primero}, resto = {resto}")  # primero = 1, resto = [2, 3, 4, 5]

# Otro ejemplo con * en el medio
inicio, *centro, fin = [10, 20, 30, 40, 50]
print(inicio)
print(centro)
print(fin)
print(f"inicio = {inicio}, centro = {centro}, fin = {fin}")  # inicio = 10, centro = [20, 30, 40], fin = 50

# Desempaquetado de diccionarios (keys)
dic = {'a': 1, 'b': 2, 'c': 3}
print(dic)
clave1, clave2, clave3 = dic
print(clave1)
print(clave2)
print(clave3)
print(f"claves: {clave1}, {clave2}, {clave3}")  # claves: a, b, c

# Desempaquetado de diccionarios (valores)
valor1, valor2, valor3 = dic.values()
print(f"valores: {valor1}, {valor2}, {valor3}")  # valores: 1, 2, 3
print(valor1)
print(valor2)
print(valor3)
# Desempaquetado de diccionarios (items)
dic = {'a': 1, 'b': 2, 'c': 3}
for clave, valor in dic.items():
    
    print(f"clave: {clave}, valor: {valor}")
