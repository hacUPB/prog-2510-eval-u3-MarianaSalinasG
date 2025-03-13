print("*" * 60)
print ("Calculadora")
print ("*" * 60)

print ("S. Sumar\nR. Restar\nM. Multiplicar\nD. Dividir\nP. Potencia")
opcion = input("Elija la opción: ").upper()

num1 = float(input("Ingrese un número 1: "))
num2 = float(input("Ingrese un número 2: "))

if opcion == 'S':
    resultado = num1 + num2
    operador = "+"
elif opcion == 'R':
    resultado == num1 - num2
    operador = "-"
elif opcion == 'M':
    resultado == num1 * num2
    operador = "*"
elif opcion == 'D':
    if num2 != 0:
        resultado = num1 / num2
    else:
        resultado = 0 
        print ("Denominador igual a 0")
    operador = "/"
elif opcion == 'P':
    resultado = num1 ** num2
    operador = "^"
else:
    print("Opción no válida")
print(f"{num1} {operador} {num2} = {resultado}")