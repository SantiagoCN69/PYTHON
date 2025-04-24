# Ejemplo 5: Bucle for con tuplas
pares = [(1, "uno", ), (2, "dos"), (3, "tres")]
for numero, nombre in pares:
    #numero y nombre son variables que almacenan el valor de cada elemento
    #primer es el número, segundo es el nombre
    print(f"El número {numero} se escribe {nombre}")

