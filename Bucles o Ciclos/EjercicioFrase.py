# Ejericicio:
# 1. Solicitar al usuario una frase de al menos 30 palabras.
# 2. Contar cuantas palabras tiene la frase.
# 3. Contar cuantos caracteres, inlcuyendo espacios en blanco que hay en el texto.
# 4. Contar los caracteres sin esoacios en blanco.
# 5. Contar cuantas veces se repite la vocal e y la vocal a.

# Regla para el resto del semestre>
# No se permite el uso de list comprehensions, ni funciones de avanzadas.

frase = input("Escribe una frase de al menos 30 palabras: ")

car_con_espacios = len(frase)
print(car_con_espacios)

palabras = frase.split(" ")
print(palabras)
num_palabras = len(palabras)
print(f"Palabras en la frase: {num_palabras}")

#El count sirve para ver cuantos se repiten.
blancos = frase.count(" ")
print(f"Espacios en blanco: {blancos}")

caracteres_sin_espacio = car_con_espacios - blancos
print(f"Total de caracteres sin espacios: {caracteres_sin_espacio}")

letras_a = frase.lower().count("a")
letras_e = frase.lower().count("a")
print(f"La letra a se repite: {letras_a} veces y la letra e se repite: {letras_e} veces")