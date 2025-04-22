# EXPLICACION METODOS CADENA ESPACIOS/FORMATO: Ejemplos de eliminar espacios y formatear cadenas en Python
# Métodos para eliminar espacios y formatear cadenas en Python

texto = "  hola mundo  "

# strip(): elimina espacios al inicio y final
print(texto.strip())   # 'hola mundo'

# lstrip(): elimina espacios al inicio
print(texto.lstrip())  # 'hola mundo  '

# rstrip(): elimina espacios al final
print(texto.rstrip())  # '  hola mundo'

# zfill(): rellena con ceros a la izquierda
numero = "5"
print(numero.zfill(3)) # '005'
