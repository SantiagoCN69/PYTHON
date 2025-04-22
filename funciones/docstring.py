# EXPLICACION DOCSTRING: Ejemplo de cómo documentar funciones con docstring en Python
# Ejemplo de docstring (comentario especial para documentar funciones en Python)

def area_circulo(radio):
    """
    Calcula el área de un círculo dado su radio.
    Parámetros:
        radio (float): El radio del círculo.
    Retorna:
        float: El área del círculo.
    """
    import math
    return math.pi * radio ** 2

print(area_circulo(5))
print(area_circulo.__doc__)
