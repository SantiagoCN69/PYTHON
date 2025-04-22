# Funciones que retornan múltiples valores en Python

def operaciones(a, b):
    suma = a + b
    resta = a - b
    return suma, resta

resultado = operaciones(10, 3)
print(resultado)  # (13, 7)

# Puedes desempacar los valores
suma, resta = operaciones(5, 2)
print("Suma:", suma)
print("Resta:", resta)
