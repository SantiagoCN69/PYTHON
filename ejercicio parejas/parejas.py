# Juego de parejas con opción de jugar de nuevo y comentarios explicativos
import tkinter as tk
from tkinter import messagebox
import random
import time
from symbols import symbols as all_symbols

# Variable global para el nivel seleccionado
nivel_seleccionado = None

def elegir_nivel(nivel):
    """Función que guarda el nivel elegido y cierra la ventana de selección."""
    global nivel_seleccionado
    nivel_seleccionado = nivel
    selector.destroy()

def seleccionar_nivel():
    """Muestra la ventana para seleccionar el nivel de dificultad."""
    global nivel_seleccionado, selector
    nivel_seleccionado = None
    selector = tk.Tk()
    selector.title("Selecciona nivel")
    tk.Label(selector, text="Elige nivel de dificultad", font=("Arial", 14)).pack(pady=10)
    tk.Button(selector, text="Fácil", width=20, command=lambda: elegir_nivel("Fácil")).pack(pady=5)
    tk.Button(selector, text="Medio", width=20, command=lambda: elegir_nivel("Medio")).pack(pady=5)
    tk.Button(selector, text="Difícil", width=20, command=lambda: elegir_nivel("Difícil")).pack(pady=5)
    selector.mainloop()

# Diccionario que define la cantidad de pares según el nivel
niveles = {
    "Fácil": 6,
    "Medio": 12,
    "Difícil": 18
}

def iniciar_juego():
    """Configura y lanza la ventana principal del juego."""
    global root, start_time, buttons, first_click, previousX, previousY, moves, pairs_found, symbols, pares, total, cols, rows
    pares = niveles[nivel_seleccionado]  # Número de pares según el nivel
    total = pares * 2  # Total de cartas
    symbols = all_symbols[:total]  # Selecciona los símbolos necesarios
    random.shuffle(symbols)  # Mezcla los símbolos

    root = tk.Tk()
    root.title("Juego de las Parejas")
    root.resizable(False, False)

    start_time = time.time()  # Guarda el tiempo de inicio
    buttons = {}  # Diccionario para los botones
    first_click = True  # Indica si es el primer click de un turno
    previousX = previousY = None  # Guarda la posición del primer click
    moves = 0  # Contador de movimientos
    pairs_found = 0  # Contador de parejas encontradas

    # Calcula columnas y filas para la cuadrícula
    cols = 6
    rows = total // cols

    # Crea los botones (cartas) en la cuadrícula
    for y in range(rows):
        for x in range(cols):
            b = tk.Button(root, text="", width=4, height=2,
                          command=lambda x=x, y=y: show_symbol(x, y))
            b.grid(row=y, column=x)
            buttons[x, y] = b

    root.mainloop()

def show_symbol(x, y):
    """Muestra el símbolo al hacer click y gestiona la lógica de emparejamiento."""
    global first_click, previousX, previousY, moves, pairs_found

    button = buttons[x, y]
    button.config(text=symbols[cols * y + x])  # Muestra el símbolo
    button.update_idletasks()

    if first_click:
        previousX, previousY = x, y
        first_click = False
        moves += 1  # Cuenta el movimiento solo en el primer click
    else:
        if previousX == x and previousY == y:
            return  # Ignora si se hace click dos veces en la misma carta
        if symbols[cols * y + x] != symbols[cols * previousY + previousX]:
            # Si no son iguales, espera 500ms y oculta ambos
            root.after(500, ocultar_cartas, x, y, previousX, previousY)
        else:
            # Si son iguales, desactiva ambos botones
            button.config(state="disabled")
            buttons[previousX, previousY].config(state="disabled")
            pairs_found += 1
        first_click = True

    # Si se encuentran todas las parejas, muestra mensaje y pregunta si quiere jugar de nuevo
    if pairs_found == pares:
        end_time = time.time()
        duracion = int(end_time - start_time)
        jugar_de_nuevo = messagebox.askyesno("¡Ganaste!", f"Movimientos: {moves}\nTiempo: {duracion} segundos\n\n¿Quieres jugar de nuevo?")
        root.destroy()
        if jugar_de_nuevo:
            seleccionar_nivel()
            iniciar_juego()


def ocultar_cartas(x1, y1, x2, y2):
    """Oculta las cartas si no son pareja."""
    buttons[x1, y1].config(text="")
    buttons[x2, y2].config(text="")

# --- Inicio del programa ---
seleccionar_nivel()
iniciar_juego()
