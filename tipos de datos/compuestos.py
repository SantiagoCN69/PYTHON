# Ejemplo de datos compuestos en Python

# Lista (list): colección ordenada y modificable de elementos
frutas = ["manzana", "banana", "cereza"]

print(frutas[0]) #manzana
print(frutas[1]) #banana
print(frutas[2]) #cereza

print("Lista:", frutas[0]) #manzana
print("Lista:", frutas[1]) #banana
print("Lista:", frutas[2]) #cereza
#modificador elemtno
frutas[0] = "uva"
print("Lista:", frutas[0]) #uva
print (frutas[0]) #uva 


# Tupla (tuple): colección ordenada e inmutable de elementos
coordenadas = (10, 20)
print("Tupla:", coordenadas)

# Conjunto (set): colección desordenada de elementos únicos #no almacena duplicados
numeros_unicos = {1, 2, 3, 2, 1}
print("Set:", numeros_unicos) #o 
print(numeros_unicos)


# Diccionario (dict): colección de pares clave-valor
persona = {"nombre": "Santiago", "edad": 17}
print("Diccionario:", persona) #o 
print(persona) 
print(persona["nombre"])
print(persona["edad"] + 1) #suma 1 a la edad y muestra obvio

# No se puede acceder por índice numérico:
# print(persona[1])  # Esto da error: KeyError: 1

# Si quieres acceder por posición, convierte los valores a lista:
valores = list(persona.values())
print(valores[1])  # Muestra 17
print(valores)
