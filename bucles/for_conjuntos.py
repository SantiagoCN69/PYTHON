# iterar listas (recorrer)
colores = {"rojo", "verde", "azul"}
#color es la variable que almacena el valor de cada elemento
for color in colores:
    print(f"Color: {color}")

# Ejemplo 2: Bucle for con enumerate
for i, color in enumerate(colores):
    print(f"Color {i+1}: {color}")
