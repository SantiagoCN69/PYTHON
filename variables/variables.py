# EXPLICACION VARIABLES: Ejemplo de cómo crear y usar variables en Python
# Ejemplo de variables y operaciones básicas en Python

# Declarar variables
numero = 1
nombre = "santiago"
# Declarar variables con snake_case
nombre_usuario = "santiago cardona"

# Mostrar texto y variables usando concatenación y f-string
print("hola " + nombre + " eres el numero " + str(numero))
print(f"hola {nombre} eres el numero {numero}")

# Sumar dos números y guardar el resultado en una variable
resultado = 10 + 5  # Esto da 15
print("El resultado de 10 + 5 es:", resultado)

# Incrementar una variable
numero = 10
numero += 1  # Ahora numero es 11
print("El valor de numero después de incrementar es:", numero)

# Ejemplo de mostrar texto en pantalla
mensaje = "¡Hola, este es un texto!"
print(mensaje)

# Mostrar el valor de una variable dentro de un texto usando f-string
print(f"El mensaje es: {mensaje} y el número es {numero}")
