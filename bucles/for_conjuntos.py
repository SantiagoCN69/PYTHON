# iterar listas (recorrer)
colores = {"rojo", "verde", "azul"}
#color es la variable que almacena el valor de cada elemento
for color in colores:
    print(f"Color: {color}")

#Bucle for con enumerate
for i, color in enumerate(colores):
    print(f"el elemento {i} es: {color}")
    
    
#Otra forma de bucle for con enumerate
for i in enumerate(colores): #i es un par (índice, valor)
    indice = i[0] #índice
    valor = i[1] #valor
    print(f"el elemento {indice} es: {valor}")
