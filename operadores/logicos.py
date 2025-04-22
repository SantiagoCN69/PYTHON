# EXPLICACION OPERADORES LOGICOS: Ejemplo de operadores lógicos en Python
# Operadores lógicos: and, or, not

# AND: Solo es True si ambas condiciones son True
print(True and True)   # True
print(True and False)  # False
print(False and False) # False

# OR: Es True si al menos una condición es True
print(True or False)   # True
print(False or False)  # False
print(True or True)    # True

# NOT: Invierte el valor lógico
print(not True)    # False
print(not False)   # True

# Ejemplo práctico
a = 5
b = 10
print(a > 0 and b > 0)   # True (ambos son mayores que 0)
print(a > 0 or b < 0)    # True (al menos uno es mayor que 0)
print(not (a > 0))       # False (a > 0 es True, pero not lo invierte)
