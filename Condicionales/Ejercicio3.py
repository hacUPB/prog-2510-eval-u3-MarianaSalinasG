## Ejercicio 3
#Determinar si un número es par o impar

num = int(input("Ingrese un número entero: "))
residuo = num % 2
if residuo == 0:
    print(f"{num} es un número par")
else:
    print(f"{num} es un número impar")
