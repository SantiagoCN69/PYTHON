# EXPLICACION OPERADORES IDENTIDAD: Ejemplo de operadores de identidad en Python
# Operadores de identidad: is, is not
a = [1, 2, 3]
b = a
c = [1, 2, 3]
print(a is b)    # True (mismo objeto)
print(a is c)    # False (objetos diferentes)
print(a is not c) # True
