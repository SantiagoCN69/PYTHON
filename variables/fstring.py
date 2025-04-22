# Ejemplo de uso de f-string en Python
numero = 1
nombre = "santiago"

# Forma tradicional (concatenación)
print("hola " + nombre + " eres el numero " + str(numero))

# Forma recomendada: f-string
bienvenida = f"hola {nombre} eres el numero {numero}"
print(bienvenida)

# Sugerencias:
# - Usa f-strings para hacer tu código más legible y fácil de escribir.
# - Puedes incluir operaciones dentro de las llaves, por ejemplo:
print(f"El doble de {numero} es {numero * 2}")
# - Puedes usar f-strings para formatear números, fechas, etc.
