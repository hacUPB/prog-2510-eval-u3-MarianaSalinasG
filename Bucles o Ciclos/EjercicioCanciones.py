#Crear una lista con su top 5 canciones favoritas
#Otra lista con el artista que la interpreta

canciones = ["Esclava de sus besos", "Las mujeres están de moda", "Un Zombie a la interperie", "Tu te imaginas", "Con Bochinche"]
artistas = ["Guido G", "Grupo Niche", "Alejandro Sanz y Luis Enrique", "De la Ghetto", "Sech"]


indice = 0
while indice < 5:
    print(f"{canciones[indice]}, interpretada por {artistas[indice]}") #Accede a los valores del indice de la lista, de 0 a 4, y los imprime.
    indice = indice + 1

for indice in range(0,5,1): #El for sirve para elementos iterables (Listas, cadenas de caracteres, diccionarios y tuplas). Lo mas importante es el range, genera una secuencia de numeros enteros y se lo asigna a la varibale para así después ejecutar el bloque de código.
    print(f"{canciones[indice]}, interpretada por {artistas[indice]}")

for cancion in canciones:
    print(cancion)  # Imprime el nombre de la canción, el for recorre toda la lista de canciones y en cada iteración guarda el nombre de la canción en la variable cancion.

#Los elemetos iterables son: estructuras de datos que se puede recorrer elemento por elemento con un bucle. 
# Los que cambian: mutables (lista).
# Los que no cambian: inmutables, (string).