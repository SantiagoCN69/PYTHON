#primero

texto = input("intruduce un texto: ")
tiempo_1_palabras = 0.5
numero_de_palabras = len(texto.split(" "))

print("------------")
print(f"tardarias {numero_de_palabras * tiempo_1_palabras} segundos en decir {numero_de_palabras} palabras")
print("------------")

#sgundo 

if numero_de_palabras > 120:
    print(f"para, estas escribiendo como que mucho, tardas {round(numero_de_palabras * tiempo_1_palabras, 2)} segundos en decir {numero_de_palabras} palabras")
else:
    print(f"tardas {round(numero_de_palabras * tiempo_1_palabras, 2)} segundos en decir {numero_de_palabras} palabras")

#tercero

print(f"yo tardaria {tiempo_que_usa * 0.3} segundos en decir {numero_de_palabras} palabras")

