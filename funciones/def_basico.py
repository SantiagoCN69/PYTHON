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

#PARAMETOR EN OTRO ORDEN

def frase(nombre, apellido, adjetivo):
    # Esta función recibe tres parámetros y devuelve una frase personalizada
    return f"Hola {nombre} {apellido}, eres muy {adjetivo}"

# Podemos llamar la función usando argumentos en distinto orden usando el nombre del parámetro
frase_resultante = frase(adjetivo="crack", nombre="Santiago", apellido="Cardona")
print(frase_resultante)

#Funcion con parámetros opcionales


def frase(nombre, apellido, adjetivo="crack"):
    # Esta función recibe tres parámetros y devuelve una frase personalizada
    return f"Hola {nombre} {apellido}, eres muy {adjetivo}"

frase_resultante = frase("Santiago", "Cardona")
print(frase_resultante) # Hola Santiago Cardona, eres muy crack
