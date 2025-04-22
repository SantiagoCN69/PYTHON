# EXPLICACION INPUT: Ejemplos de uso de input() para recibir datos del usuario en Python
# input() siempre devuelve un string (cadena de texto)
nombre = input("¿Cómo te llamas?: ")
print("Hola, " + nombre)

# Para trabajar con números, convierte el input a int o float
edad = int(input("¿Cuántos años tienes?: "))
print(f"Tienes {edad} años.")

# Puedes pedir varios datos y usarlos juntos
a = float(input("Ingresa un número decimal: "))
b = float(input("Ingresa otro número decimal: "))
print(f"La suma es: {a + b}")

# Ejemplo de input para listas (separadas por coma)
valores = input("Ingresa varios números separados por coma: ")
lista = valores.split(",")
print(lista)

# Para convertir la lista de strings a enteros:
lista_numeros = [int(x) for x in lista]
print(lista_numeros)
