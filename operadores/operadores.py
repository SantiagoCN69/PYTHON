# Ejemplos de operadores en Python

# Operadores aritméticos
suma = 5 + 3          # 8
resta = 10 - 4        # 6
multiplicacion = 2 * 6 # 12
division = 8 / 2      # 4.0 devuelve float siempr
modulo = 9 % 2        # 1 (resto de la división)
exponente = 2 ** 3    # 8
division_entera = 9 // 2  # 4 devuelve int redondea abajo

print("Resultados:", suma, resta, multiplicacion, division, modulo, exponente, division_entera)
# Operadores de comparación
mayor = 5 > 3          # True
menor = 5 < 3          # False
igual = 5 == 5         # True
diferente = 5 != 4     # True
mayor_igual = 5 >= 5   # True
menor_igual = 3 <= 2   # False

print("Comparación:", mayor, menor, igual, diferente, mayor_igual, menor_igual)

# Operadores lógicos
and_logico = True and False   # False
or_logico = True or False     # True
not_logico = not True         # False

print("Lógicos:", and_logico, or_logico, not_logico)

# Operadores de asignación
x = 10
x += 2  # x = x + 2
x -= 1  # x = x - 1
print("Asignación:", x)

# Operadores de pertenencia
lista = [1, 2, 3]
print(2 in lista)      # True
print(5 not in lista)  # True

# Operadores de identidad
a = [1, 2, 3]
b = a
c = [1, 2, 3]
print(a is b)   # True (mismo objeto)
print(a is c)   # False (mismo contenido, distinto objeto)
print(a == c)   # True (mismo contenido)