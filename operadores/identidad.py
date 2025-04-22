# Ejemplos de operadores de identidad en Python

a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)   # True (mismo objeto en memoria)
print(a is c)   # False (contenido igual, objetos distintos)
print(a == c)   # True (contenido igual)
