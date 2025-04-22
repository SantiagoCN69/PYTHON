# Métodos para validar el contenido de una cadena en Python

texto = "Python123"

# isalpha(): solo letras
print(texto.isalpha())  # False

# isdigit(): solo dígitos
print(texto.isdigit())  # False

# isalnum(): letras y números
print(texto.isalnum())  # True

# startswith(): comienza con...
print(texto.startswith("Py"))  # True

# endswith(): termina con...
print(texto.endswith("123"))  # True
