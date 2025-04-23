# EXPLICACION teoría y métodos de conjuntos en Python
# Ejemplos de métodos importantes de conjuntos: issubset, issuperset, isdisjoint, copy, clear, etc.

# issubset: ¿Es subconjunto?
a = {1, 2, 3}
b = {1, 2, 3, 4, 5}
print(f"¿a es subconjunto de b? {a.issubset(b)}")  # True
print(f"¿b es subconjunto de a? {b.issubset(a)}")  # False

# issuperset: ¿Es superconjunto?
print(f"¿b es superconjunto de a? {b.issuperset(a)}")  # True
print(f"¿a es superconjunto de b? {a.issuperset(b)}")  # False

# isdisjoint: ¿No tienen elementos en común?
c = {7, 8}
print(f"¿a y c no tienen elementos en común? {a.isdisjoint(c)}")  # True
print(f"¿a y b no tienen elementos en común? {a.isdisjoint(b)}")  # False

# copy: Copiar un conjunto
d = a.copy()
print(f"Copia de a: {d}")

# clear: Vaciar un conjunto
d.clear()
print(f"Conjunto d después de clear(): {d}")

# Métodos de actualización
e = {1, 2, 3}
f = {3, 4, 5}
e.update(f)  # Unión en el mismo conjunto
e.add(6)     # Agregar un solo elemento
print(f"Conjunto e después de update y add: {e}")

g = {1, 2, 3, 4, 5}
g.discard(3)  # Eliminar elemento si existe (sin error)
g.remove(2)   # Eliminar elemento, da error si no existe
print(f"Conjunto g después de discard y remove: {g}")