# Ejemplo básico de bucle while en Python


# Inicializamos una variable llamada 'contador' con el valor 1
contador = 1

# El bucle while se ejecutará mientras 'contador' sea menor o igual a 5
while contador <= 5:
    # Imprimimos el valor actual de 'contador'
    print("El contador es:", contador)
    # Incrementamos el valor de 'contador' en 1 para evitar un bucle infinito
    contador += 1

# Cuando la condición del while deja de cumplirse, el bucle termina
print("¡El bucle ha terminado!")