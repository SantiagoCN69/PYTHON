# EXPLICACION FUNCION BASICA: Ejemplo de cómo definir y usar una función simple en Python

def saludar():
    print("Hola, bienvenido a Python!")

saludar()

# Función con parámetros

def sumar(a, b):
    resultado = a + b
    return resultado

print(sumar(3, 5))  # 8

# Puedes llamar a la función con diferentes valores
x = 10
y = 20
print(sumar(x, y))  # 30
