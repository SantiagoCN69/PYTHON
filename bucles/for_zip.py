# Ejemplo 3: Iterar dos listas con zip
nombres = ["Ana", "Luis", "Carlos"]
edades = [20, 25, 30]
for nombre, edad in zip(nombres, edades):
    print(f"{nombre} tiene {edad} años")

