from tkinter import messagebox, Tk, Button, Label
import random
import time
from symbols import symbols as all_symbols

nivel_seleccionado = None

def elegir_nivel(nivel):
    global nivel_seleccionado
    nivel_seleccionado = nivel
    selector.destroy()

def seleccionar_nivel():
    global nivel_seleccionado, selector
    nivel_seleccionado = None
    selector = Tk()
    selector.title("Selecciona nivel")
    Label(selector, text="Elige nivel de dificultad", font=("Arial", 14)).pack(pady=10)
    Button(selector, text="Fácil", width=20, command=lambda: elegir_nivel("Fácil")).pack(pady=5)
    Button(selector, text="Medio", width=20, command=lambda: elegir_nivel("Medio")).pack(pady=5)
    Button(selector, text="Difícil", width=20, command=lambda: elegir_nivel("Difícil")).pack(pady=5)
    selector.mainloop()

niveles = {
    "Fácil": 6,
    "Medio": 12,
    "Difícil": 18
}

def iniciar_juego():
    global root, start_time, buttons, first_click, previousX, previousY, moves, pairs_found, symbols, pares, total, cols, rows
    pares = niveles[nivel_seleccionado]
    total = pares * 2
    symbols = all_symbols[:total]
    random.shuffle(symbols)

    root = Tk()
    root.title("Juego de las Parejas")
    root.resizable(False, False)

    start_time = time.time()
    buttons = {}
    first_click = True
    previousX = previousY = None
    moves = 0
    pairs_found = 0

    cols = 6
    rows = total // cols

    for y in range(rows):
        for x in range(cols):
            b = Button(root, text="", width=4, height=2,
                          command=lambda x=x, y=y: show_symbol(x, y))
            b.grid(row=y, column=x)
            buttons[x, y] = b

    root.mainloop()

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
            root.after(500, ocultar_cartas, x, y, previousX, previousY)
        else:
            button.config(state="disabled")
            buttons[previousX, previousY].config(state="disabled")
            pairs_found += 1
        first_click = True

    if pairs_found == pares:
        end_time = time.time()
        duracion = int(end_time - start_time)
        jugar_de_nuevo = messagebox.askyesno("¡Ganaste!", f"Movimientos: {moves}\nTiempo: {duracion} segundos\n\n¿Quieres jugar de nuevo?")
        root.destroy()
        if jugar_de_nuevo:
            seleccionar_nivel()
            iniciar_juego()

def ocultar_cartas(x1, y1, x2, y2):
    buttons[x1, y1].config(text="")
    buttons[x2, y2].config(text="")

seleccionar_nivel()
iniciar_juego()
