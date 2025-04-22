# Ejemplo de if-elif-else en Python
# El if-elif-else permite evaluar múltiples condiciones de manera ordenada.
# Python revisa cada condición en orden y ejecuta el primer bloque que sea verdadero.

numero = int(input("Ingresa un número: "))

if numero > 0:
    print("El número es positivo")
elif numero == 0:
    print("El número es cero")
else:
    print("El número es negativo")

# Otro ejemplo práctico:
nota = int(input("Ingresa tu nota (0-10): "))
if nota == 10:
    print("¡Excelente!")
elif nota >= 7:
    print("Aprobado")
elif nota >= 5:
    print("Suficiente")
else:
    print("Reprobado")

# Puedes usar tantos elif como necesites para cubrir diferentes casos.
