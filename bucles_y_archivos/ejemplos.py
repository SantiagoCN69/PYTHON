# Ejemplo 1: Bucle for
print("Ejemplo 1: Bucle for")
for i in range(5):
    print(f"Iteración número {i}")

# Ejemplo 2: Bucle while
print("\nEjemplo 2: Bucle while")
contador = 0
while contador < 5:
    print(f"Contador vale {contador}")
    contador += 1

# Ejemplo 3: Leer archivo línea por línea
print("\nEjemplo 3: Leer archivo línea por línea")
with open("ejemplo.txt", "w", encoding="utf-8") as f:
    f.write("Línea 1\nLínea 2\nLínea 3\n")
with open("ejemplo.txt", "r", encoding="utf-8") as f:
    for linea in f:
        print(linea.strip())

# Ejemplo 4: Escribir en archivo
print("\nEjemplo 4: Escribir en archivo")
with open("salida.txt", "w", encoding="utf-8") as f:
    for i in range(3):
        f.write(f"Línea generada {i}\n")
print("Archivo 'salida.txt' creado.")

# Ejemplo 5: Leer archivo completo
def leer_archivo(nombre):
    with open(nombre, "r", encoding="utf-8") as f:
        return f.read()
print("\nEjemplo 5: Leer archivo completo")
contenido = leer_archivo("salida.txt")
print(contenido)
