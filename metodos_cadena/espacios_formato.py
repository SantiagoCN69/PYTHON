# Métodos para eliminar espacios y formatear cadenas en Python

texto = "  Hola Mundo  "

# strip(): elimina espacios al inicio y final
print(texto.strip())  # 'Hola Mundo'

# lstrip(): elimina espacios al inicio
print(texto.lstrip())  # 'Hola Mundo  '

# rstrip(): elimina espacios al final
print(texto.rstrip())  # '  Hola Mundo'

# zfill(): rellena con ceros a la izquierda
numero = "42"
print(numero.zfill(5))  # '00042'
