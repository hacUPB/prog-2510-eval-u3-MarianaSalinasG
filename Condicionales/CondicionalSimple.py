# Ejercicio 4

# Condicional simple: Estoy en Universal y me voy a montar a VelociCoaster. Si la altura del usuario es menor a 130 centimetros, no puede montar.

# Condicional doble: Estoy en el corral, se pregunta al usuario que desea comer, si elige una hamburguesa, se le pregunta si desea papitas, si no quiere papitas, se le pregunta si desea aros de cebolla.

numero = input("Ingrese el número telefónico: ")
contador = 0
for digito in numero:
    contador = contador + 1
if contador != 10:
    print("Eso no es un número telefónico válido")
