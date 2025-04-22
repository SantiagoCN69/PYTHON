# EXPLICACION METODOS CADENA VALIDACION: Ejemplos de validar letras, números y alfanuméricos en una cadena en Python
# Métodos para validar el contenido de una cadena en Python

texto = "Python123"

# isalpha(): solo letras
print(texto.isalpha())  # False (tiene números)

# isdigit(): solo dígitos
print(texto.isdigit())  # False (tiene letras)

# isalnum(): letras y números
print(texto.isalnum())  # True (solo letras y números)

# startswith(): comienza con...
print(texto.startswith("Py"))  # True

# endswith(): termina con...
print(texto.endswith("3"))     # True
