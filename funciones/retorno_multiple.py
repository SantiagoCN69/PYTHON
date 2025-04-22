# EXPLICACION RETORNO MULTIPLE: Ejemplo de función que retorna múltiples valores en Python

def operaciones(a, b):
    suma = a + b
    resta = a - b
    return suma, resta

resultado_suma, resultado_resta = operaciones(10, 5)
print("Suma:", resultado_suma)
print("Resta:", resultado_resta)

# Puedes desempacar los valores
suma, resta = operaciones(5, 2)
print("Suma:", suma)
print("Resta:", resta)
