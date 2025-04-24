#JEERICCIO NUMRO SECRETO
print("Piensa en un numero")
print("haz las siguientes operaicones")
print("---------")
print("1. Suma 5")
print("2. Multiplica por 3")
print("3. Resta 4")
print("4. Dividir por 2")
print("5. Resta 1")
print("---------")
numero = float(input("¿Cuál es el resultado?: "))
numero = ((((numero + 1) * 2) + 4) / 3) - 5
print( f"tu numeor es: {numero}")


#MISMO EJERCICIO 
# EJERCICIO NÚMERO SECRETO
print("Piensa en un número")
operaciones = [
    "1. Suma 5",
    "2. Multiplica por 3",
    "3. Resta 4",
    "4. Divide por 2",
    "5. Resta 1"
]
print("Haz las siguientes operaciones:")
print("---------")
for op in operaciones:
    print(op)
print("---------")

resultado = float(input("¿Cuál es el resultado?: "))
numero = ((((resultado + 1) * 2) + 4) / 3) - 5

# Mostrar solo el entero si no hay decimales
print(f"Tu número es: {numero}")