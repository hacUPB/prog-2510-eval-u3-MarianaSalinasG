## Ejercicio 2

envio = 9000
compra = input("Ingrese el valor de la compra: ")
valor_compra = int(compra)
if valor_compra >= 100000:
    envio = 0
total = valor_compra + envio
print(f"El total a pagar es: {total}")



