# Ejemplo de if-elif-else con condicionales anidados en Python
# Puedes poner un if (o elif, o else) dentro de otro if para evaluar condiciones más complejas.
# input() sirve para pedirle datos al usuario desde la consola.
# Lo que el usuario escriba se guarda como una cadena (str).
# Ejemplo: aquí pedimos la edad para decidir si es mayor o menor de edad.

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
        
#ejemplo 2
ingreso = int(input("¿Cuánto dinero ganas mensualmente?:$ "))
gastos = int(input("¿Cuánto dinero gastas mensualmente?:$ "))

if ingreso > 2000000:
    if gastos > ingreso * .8:
        print("Estas ganando mucho pero estas gastando demasiado, no te va a quedar gita")
    else: 
        print("Estas ganando mucho y te esta quedando gita, genial!!")

elif ingreso > 1500000:
    if gastos > ingreso * .8:
        print("Estas ganando mas del minimo pero estas gastando demasiado, no te va a quedar gita")
    else: 
        print("Estas ganando mas del minimo y te esta quedando gita, genial!!")
else:
    print("Estas ganando menos del minimo, sos pobre")
