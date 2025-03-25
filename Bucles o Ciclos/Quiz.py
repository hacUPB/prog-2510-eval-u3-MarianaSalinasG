num_correcto = 15
cont = 0

print("Bienvenido al juego Adivina el número")
num = int(input("Ingresa el número que consideras correcto, tienes que adivinar un número entre 1 y 100: "))

while num != num_correcto:
    if num < num_correcto:
        print("El número es menor. Intenta de nuevo")
    elif num > num_correcto:
        print("El número es mayor. Intenta de nuevo")
    cont += 1
    num = int(input("Ingresa otro número: "))

cont += 1  
print(f"Felicidades, has adivinado el número en {cont} intentos")