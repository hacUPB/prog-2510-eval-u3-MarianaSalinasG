# Crear una lista vacía y llenar esa lista con 100 números al azar entre 1 y 100.
import random

lista = []

for i in range(0, 100):
    lista.append(random.randint(1, 100))

print(f"{i} = {lista}")    
