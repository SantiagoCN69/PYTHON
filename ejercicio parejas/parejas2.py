#import
import random
import time
from tkinter import Tk, Button, messagebox

#iniciar la ventana
root = Tk()
root.title("Juego de las Parejas")
root.resizable(width=False, height=False)

#botones
buttons = {}
button_symbols = {}  # no esta esto en la guia y es necesario

#comprobar si el simbolo es le primero en el emparejamiento
first = True

#diccionario que guarda los simbolo de cada boton
symbols = [ u'\u2600', u'\u2600', u'\u2601', u'\u2601', u'\u2602', u'\u2602',
           u'\u2603', u'\u2603', u'\u25EF', u'\u25EF', u'\u2605', u'\u2605',
           u'\u2606', u'\u2606', u'\u260E', u'\u260E', u'\u260F', u'\u260F',
           u'\u25C6', u'\u25C6', u'\u25C7', u'\u25C7', u'\u263B', u'\u263B']

#filas
rows = 4
columns = 6

#mezcalr los simbolos
random.shuffle(symbols)



#crear los btones, asigna un simbolo a cada uno y añadelos a los diccionarios
for x in range(rows):
    for y in range(columns):
        button = Button(command = lambda x=x, y=y: show_symbol(x, y), width=3, height=2)
        button.grid(column=y, row=x)
        buttons[x, y] = button
        button_symbols[x, y] = symbols.pop()
        
first = True


def show_symbol(x, y):
    
    global first, pairs
    global previousX, previousY
    
    buttons[x, y]["text"] = button_symbols[x, y] #esta linea nos permite mostrar el simbolo de la carta
    buttons[x, y].update_idletasks() #actualiza la pantalla
    
    if first:
        #si el usuria hace lick en el primer turno de part, guarde sus coordenadas y agrega un movimiento
        previousX = x
        previousY = y
        first = False
    elif previousX != x or previousY != y:
        #si el usuario hace click en una carta diferente, comprobar si son pareja
        
        if buttons[previousX, previousY]["text"] != buttons[x, y]["text"]:
        #muestre los simbolos por .5 segundos y ocultarlos
            time.sleep(0.5)
            buttons[previousX, previousY]["text"] = ""
            buttons[x, y]["text"] = ""
        
        #si los botones si coinciden
        else:
            #si las parejas coinciden deshabilitarlos
            buttons[previousX, previousY] = DISABLED
            buttons[x, y] = DISABLED
            
        first = True #esto hace que la fucnion este lista para la priemr apreiso del boton e ne el siguiente intento
        
#iniciar el bucle principal
root.mainloop() 