# Métodos para dividir y unir cadenas en Python

texto = "uno,dos,tres,cuatro"

# split(): divide la cadena en una lista
lista = texto.split(",")
print(lista)  # ['uno', 'dos', 'tres', 'cuatro']

# join(): une una lista de cadenas en una sola cadena
nueva_cadena = "-".join(lista)
print(nueva_cadena)  # 'uno-dos-tres-cuatro'

nombre = "santiago cardona"
print(nombre.split())
print(type(nombre.split()))
