# Ejemplo de función que no retorna valores, solo imprime una contraseña generada aleatoriamente

def crear_contraseña_random(num):
    # Definimos una cadena de caracteres posibles para la contraseña
    chars = "abcdefghij"
    
    # Convertimos el número recibido a string para poder indexar
    num_entero = str(num)
    # Tomamos el primer dígito del número recibido (en caso de que sea de más de una cifra)
    num = int(num_entero[0])
    
    # Calculamos los índices para seleccionar caracteres
    c1 = num - 2
    c2 = num - 5
    c3 = num + 5
    
    # Construimos la contraseña usando f-strings y los índices calculados
    contraseña = f"{chars[c1]}{chars[c2]}{chars[c3]}{num*2}"
    # Imprimimos la contraseña generada
    print(contraseña)

# Llamamos la función con el argumento 1 como ejemplo
crear_contraseña_random(1)


#retornando el valor

def crear_contraseña_random(num):
    # Definimos una cadena de caracteres posibles para la contraseña
    chars = "abcdefghij"
    
    # Convertimos el número recibido a string para poder indexar
    num_entero = str(num)
    # Tomamos el primer dígito del número recibido (en caso de que sea de más de una cifra)
    num = int(num_entero[0])
    
    # Calculamos los índices para seleccionar caracteres
    c1 = num - 2
    c2 = num - 5
    c3 = num + 5
    
    # Construimos la contraseña usando f-strings y los índices calculados
    contraseña = f"{chars[c1]}{chars[c2]}{chars[c3]}{num*2}"
    # Retornamos la contraseña generada
    return contraseña

# Llamamos la función con el argumento 1 como ejemplo
password = crear_contraseña_random(1)
print(f"tu contraseña es {password}")

#retornar 2 valores de una fucnion

def crear_contraseña_random(num):
    # Definimos una cadena de caracteres posibles para la contraseña
    chars = "abcdefghij"
    
    # Convertimos el número recibido a string para poder indexar
    num_entero = str(num)
    # Tomamos el primer dígito del número recibido (en caso de que sea de más de una cifra)
    num = int(num_entero[0])
    
    # Calculamos los índices para seleccionar caracteres
    c1 = num - 2
    c2 = num - 5
    c3 = num + 5
    
    # Construimos la contraseña usando f-strings y los índices calculados
    contraseña = f"{chars[c1]}{chars[c2]}{chars[c3]}{num*2}"
    # Retornamos la contraseña generada
    return contraseña, num #retornamos 2 valores en una tupla

# Llamamos la función con el argumento 1 como ejemplo
password, num = crear_contraseña_random(1) #desempaquetamos los valores
print(f"tu contraseña es {password}")
print(f"el numero es {num}")
