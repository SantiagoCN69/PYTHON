#primero

texto = input("intruduce un texto: ")
tiempo_1_palabras = 0.5
numero_de_palabras = len(texto.split(" "))

print("------------")
print(f"tardarias {numero_de_palabras * tiempo_1_palabras} segundos en decir {numero_de_palabras} palabras")
print("------------")

#sgundo 

texto = input("intruduce un texto: ")
tiempo_1_palabras = 0.5
numero_de_palabras = len(texto.split(" "))
tiempo_que_usa = numero_de_palabras * tiempo_1_palabras
if tiempo_que_usa > 60:
    print(f"para, estas escribiendo como que mucho, tardas {round(tiempo_que_usa, 2)} segundos en decir {numero_de_palabras} palabras")
else:
    print(f"tardas {round(tiempo_que_usa, 2)} segundos en decir {numero_de_palabras} palabras")

#tercero

tiempo_1_palabra_yo = tiempo_que_usa * 0.3
print(f"yo tardaria {tiempo_1_palabra_yo} segundos")

