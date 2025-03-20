#  Eliminar Elementos de una Lista

Aviones = ["A300", "A310", "A320", "A330", "A340"]

# Eliminar un elemento por valor
Aviones.remove(2)

# Eliminar un elemento por índice y obtener su valor
valor_eliminado = Aviones.pop(1)

# Eliminar todos los elementos de la lista
Aviones.clear()

print(Aviones)
print("Valor Eliminado:", valor_eliminado)