# Duraciones de cursos en horas
minimo_cursos = 2.5   # Mínima duración de otros cursos
maximo_cursos = 7     # Máxima duración de otros cursos
promedio = 4          # Duración promedio de otros cursos
este_curso = 1.5      # Duración de este curso

# Calcula el porcentaje de diferencia respecto al mínimo
# Si el resultado es negativo, este curso es más corto; si es positivo, es más largo.
diferencia_con_min = ((este_curso - minimo_cursos) / minimo_cursos) * 100
print("Diferencia con el mínimo:", round(diferencia_con_min, 2), "%")

# Calcula el porcentaje de diferencia respecto al máximo
# Si el resultado es negativo, este curso es más corto; si es positivo, es más largo.
diferencia_con_max = ((este_curso - maximo_cursos) / maximo_cursos) * 100
print("Diferencia con el máximo:", round(diferencia_con_max, 2), "%")

# Calcula el porcentaje de diferencia respecto al promedio
# Si el resultado es negativo, este curso es más corto; si es positivo, es más largo.
diferencia_con_prom = ((este_curso - promedio) / promedio) * 100
print("Diferencia con el promedio:", round(diferencia_con_prom, 2), "%")

# Explicación:
# round(x, 2) redondea el número x a 2 decimales. Por ejemplo, round(3.14159, 2) es 3.14.
# Si el resultado es negativo, significa que este curso es más corto que la comparación. Si es positivo, es más largo.