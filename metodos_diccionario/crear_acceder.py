# Cómo crear y acceder a elementos en un diccionario de Python

datos = {"nombre": "Santiago", "edad": 25, "ciudad": "Medellín"}

# Acceso por clave
print(datos["nombre"])  # Santiago

# get(): acceso seguro (no da error si la clave no existe)
print(datos.get("profesion", "No especificado"))  # No especificado
