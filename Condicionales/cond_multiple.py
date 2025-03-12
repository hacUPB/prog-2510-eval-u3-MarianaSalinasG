print("*" * 60)
print ("Calculadora")
print ("*" * 60)

print ("S. Sumar\nR. Restar\nM. Multiplicar\nD. Dividir\nP. Potencia")
opcion = input("Elija la opción: ").upper()

num1 = float(input("Ingrese un número 1: "))
num2 = float(input("Ingrese un número 2: "))

match opcion:
    case 'S':
        resultado = num1 + num2
        operador = "+"
    case 'R':
        resultado == num1 - num2
        operador = "-"
    case 'M':
        resultado == num1 * num2
        operador = "*"
    case 'D':
        operador = "/"
        if num2 != 0:
            resultado = num1 / num2
        else:
            resultado = "Indeterminado"
            print ("Denominador igual a 0")
    case 'P':
        resultado = num1 ** num2
        operador = "^"
    case _:
        print("Opción no válida")
print(f"{num1} {operador} {num2} = {resultado}")