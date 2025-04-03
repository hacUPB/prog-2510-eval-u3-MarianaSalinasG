## Operaciones Aritméticas

print("S. Suma\nR. Resta\nD. División\nM. Multiplicación")
opcion = int(input("Elija una opción: "))

if opcion == "S":
    print("Sumar")
elif opcion == "R":
    print("Restar")
elif opcion == "D":
    print("Dividir")
elif opcion == "M":
    print("Multiplicar")
else:
    print("Opción no válida")