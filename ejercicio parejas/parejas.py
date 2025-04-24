import tkinter as tk
from tkinter import messagebox
import random
import time
from symbols import symbols as all_symbols

# Variables globales
nivel_seleccionado = None

# Ventana para seleccionar nivel
def elegir_nivel(nivel):
    global nivel_seleccionado
    nivel_seleccionado = nivel
    selector.destroy()

selector = tk.Tk()
selector.title("Selecciona nivel")

tk.Label(selector, text="Elige nivel de dificultad", font=("Arial", 14)).pack(pady=10)

tk.Button(selector, text="Fácil", width=20, command=lambda: elegir_nivel("Fácil")).pack(pady=5)
tk.Button(selector, text="Medio", width=20, command=lambda: elegir_nivel("Medio")).pack(pady=5)
tk.Button(selector, text="Difícil", width=20, command=lambda: elegir_nivel("Difícil")).pack(pady=5)

selector.mainloop()

# Configuración según nivel
niveles = {
    "Fácil": 6,
    "Medio": 12,
    "Difícil": 18
}

pares = niveles[nivel_seleccionado]
total = pares * 2
symbols = all_symbols[:total]
random.shuffle(symbols)

# Juego principal
root = tk.Tk()
root.title("Juego de las Parejas")
root.resizable(False, False)

start_time = time.time()
buttons = {}
first_click = True
previousX = previousY = None
moves = 0
pairs_found = 0

def show_symbol(x, y):
    global first_click, previousX, previousY, moves, pairs_found

    button = buttons[x, y]
    button.config(text=symbols[cols * y + x])
    button.update_idletasks()

    if first_click:
        previousX, previousY = x, y
        first_click = False
        moves += 1
    else:
        if previousX == x and previousY == y:
            return
        if symbols[cols * y + x] != symbols[cols * previousY + previousX]:
            time.sleep(0.5)
            button.config(text="")
            buttons[previousX, previousY].config(text="")
        else:
            button.config(state="disabled")
            buttons[previousX, previousY].config(state="disabled")
            pairs_found += 1

        first_click = True

    if pairs_found == pares:
        end_time = time.time()
        duracion = int(end_time - start_time)
        messagebox.showinfo("¡Ganaste!", f"Movimientos: {moves}\nTiempo: {duracion} segundos")
        root.destroy()

# Crear botones
cols = 6
rows = total // cols
for y in range(rows):
    for x in range(cols):
        b = tk.Button(root, text="", width=4, height=2,
                      command=lambda x=x, y=y: show_symbol(x, y))
        b.grid(row=y, column=x)
        buttons[x, y] = b

root.mainloop()
