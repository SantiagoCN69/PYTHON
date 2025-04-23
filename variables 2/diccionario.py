# EXPLICACION diccionarios en Python
# Ejemplos de cómo crear y usar diccionarios

# Crear un diccionario vacío
dic_vacio = {}
print(f"Diccionario vacío: {dic_vacio}")

# Crear un diccionario con datos
persona = {
    "nombre": "Santiago",
    "edad": 17,
    "ciudad": "Ibague"
}
print(f"Diccionario persona: {persona}")

#otra forma de crear
diccionario = dict(nombre="Santiago", edad=17, ciudad="Ibague")
print(f"Diccionario: {diccionario}")

#otra forma con from keys
fromkeys = dict.fromkeys(["nombre", "edad", "ciudad"]) #solo claves sin valores
print(f"Diccionario con fromkeys: {fromkeys}")

# Acceder a valores por clave
print(f"Nombre: {persona['nombre']}")
print(f"Edad: {persona['edad']}")

# Agregar y modificar valores
persona["profesion"] = "Ingeniero"
persona["edad"] = 17
print(f"Diccionario actualizado: {persona}")

# Recorrer claves y valores
for clave in persona:
    print(f"Clave: {clave}, Valor: {persona[clave]}")

# Otra forma de recorrer claves y valores
for clave, valor in persona.items():
    print(f"Clave: {clave}, Valor: {valor}")

# Eliminar una clave
persona.pop("ciudad")
print(f"Diccionario después de eliminar 'ciudad': {persona}")
