# Métodos para recorrer y buscar en un diccionario de Python

datos = {"nombre": "Santiago", "edad": 17, "ciudad": "Ibague"}

# keys(): obtener todas las claves
print(list(datos.keys()))  # ['nombre', 'edad', 'ciudad']

# values(): obtener todos los valores
print(list(datos.values()))  # ['Santiago', 17, 'Ibague']

# items(): obtener pares clave-valor
print(list(datos.items()))  # [('nombre', 'Santiago'), ('edad', 17), ('ciudad', 'Ibague')]

# Recorrer el diccionario
for clave, valor in datos.items():
    print(f"{clave}: {valor}")

# Comprobar si una clave existe
print("edad" in datos)  # True
