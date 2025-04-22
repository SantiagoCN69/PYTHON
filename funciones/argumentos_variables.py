# Funciones con argumentos variables (*args y **kwargs) en Python

def suma_todos(*args):
    return sum(args)

print(suma_todos(1, 2, 3))  # 6
print(suma_todos(5, 10, 15, 20))  # 50

# **kwargs permite recibir argumentos con nombre

def mostrar_info(**kwargs):
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")

mostrar_info(nombre="Santiago", edad=25, ciudad="Ibague")
