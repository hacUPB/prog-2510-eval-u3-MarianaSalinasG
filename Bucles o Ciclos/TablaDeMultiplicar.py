num = int(input("Ingrese un número entero positivo: "))
incremento = 1

while incremento <= 10:
    resultado = num * incremento 
    print(f"{num} x {incremento} = {resultado}")
    incremento += 1 #El += es para que el bucle no sea infinito, así se incrementa en cada interación hasta que llega a 10. 