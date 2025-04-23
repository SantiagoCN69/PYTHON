# Precios de camisetas en dólares
precio_minimo = 10    # Precio mínimo de otras camisetas
precio_maximo = 30    # Precio máximo de otras camisetas
precio_promedio = 20  # Precio promedio de otras camisetas
mi_precio = 8         # Precio de mi camiseta

# Calcula el porcentaje de diferencia respecto al precio mínimo
porcentaje_min = ((mi_precio - precio_minimo) / precio_minimo) * 100
print(porcentaje_min) # -20% mi preciero respecto al precio mínimo
if porcentaje_min < 0:
    print(f"Tu camiseta es más barata que el mínimo por {round(abs(porcentaje_min), 2)}%.")
elif porcentaje_min > 0:
    print(f"Tu camiseta es más cara que el mínimo por {round(abs(porcentaje_min), 2)}%.")
else:
    print("Tu camiseta cuesta exactamente lo mismo que el mínimo.")

# Calcula el porcentaje de diferencia respecto al precio máximo
porcentaje_max = ((mi_precio - precio_maximo) / precio_maximo) * 100
print(porcentaje_max) # -73.33% mi precio respecto al precio máximo
if porcentaje_max < 0:
    print(f"Tu camiseta es más barata que el máximo por {round(abs(porcentaje_max), 2)}%.")
elif porcentaje_max > 0:
    print(f"Tu camiseta es más cara que el máximo por {round(abs(porcentaje_max), 2)}%.")
else:
    print("Tu camiseta cuesta exactamente lo mismo que el máximo.")

# Calcula el porcentaje de diferencia respecto al precio promedio
porcentaje_prom = ((mi_precio - precio_promedio) / precio_promedio) * 100
print(porcentaje_prom) # -60% mi precio respecto al precio promedio
if porcentaje_prom < 0:
    print(f"Tu camiseta es más barata que el promedio por {round(abs(porcentaje_prom), 2)}%.")
elif porcentaje_prom > 0:
    print(f"Tu camiseta es más cara que el promedio por {round(abs(porcentaje_prom), 2)}%.")
else:
    print("Tu camiseta cuesta exactamente lo mismo que el promedio.")

# Explicación:
# abs(x) convierte cualquier número negativo en positivo. Por ejemplo, abs(-5) es 5.
# round(x, 2) redondea el número x a 2 decimales. Por ejemplo, round(3.14159, 2) es 3.14.
# Así los resultados son más fáciles de leer y comparar.