# EXPLICACION ARGUMENTOS VARIABLES: Ejemplo de *args y **kwargs en funciones de Python
# Funciones con argumentos variables (*args y **kwargs) en Python


#ARGS
def suma_todos(*args): #*args recibe argumentos variables y los devuelve como una tupla
    return sum(args) #sum() es una funcion integrada de python que suma todos los elementos de un iterable

print(suma_todos(4, 5, 6, 7, 8))  # 30
print(suma_todos(5, 10, 15, 20))  # 50

#UNO Y ARGS
def suma(nombre, *numeros):
    # La función recibe un nombre y una cantidad variable de números
    # sum(numeros) suma todos los números recibidos como argumentos
    return f"{nombre}, la suma de tus numeros es: {sum(numeros)}"

resultado = suma("Lucas", 5, 3, 9, 10, 20, 3)
print(resultado)


# **kwargs permite recibir argumentos con nombre

def mostrar_info(**kwargs): #**kwargs recibe argumentos con nombre y los devuelve como un diccionario
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")

mostrar_info(nombre="Santiago", edad=17, ciudad="Ibague")

