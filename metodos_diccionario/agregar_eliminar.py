# Métodos para agregar y eliminar elementos en un diccionario de Python

datos = {
    "nombre": "Santiago", 
    "edad": 25
}

# Agregar o actualizar un valor
datos["ciudad"] = "ibague"
print(datos)

# update(): agregar varios valores o actualizar
nuevos = {"profesion": "Developer", "edad": 17}
datos.update(nuevos)
print(datos)

# pop(): eliminar una clave y obtener su valor
edad = datos.pop("edad")
print(edad)  # 17
print(datos)

# popitem(): elimina el último par clave-valor
ultimo = datos.popitem() # ('ciudad', 'ibague')
print(ultimo)
print(datos)
