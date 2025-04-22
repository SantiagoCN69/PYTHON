# Ejemplo de if-elif-else con condicionales anidados en Python
# Puedes poner un if (o elif, o else) dentro de otro if para evaluar condiciones más complejas.

edad = int(input("¿Cuál es tu edad?: "))

if edad >= 18:
    print("Eres mayor de edad")
    # if anidado: solo se evalúa si la persona es mayor de edad
    licencia = input("¿Tienes licencia de conducir? (s/n): ")
    if licencia == "s":
        print("Puedes conducir legalmente.")
    elif licencia == "n":
        print("No puedes conducir, necesitas licencia.")
    else:
        print("Respuesta no válida.")
else:
    print("Eres menor de edad")
    # if anidado: solo se evalúa si la persona es menor de edad
    permiso = input("¿Tienes permiso especial de tus padres? (s/n): ")
    if permiso == "s":
        print("Puedes conducir con supervisión.")
    else:
        print("No puedes conducir.")
