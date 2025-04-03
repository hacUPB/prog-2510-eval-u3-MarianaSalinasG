def suma(a, b=0):
	resultado = a + b
	return resultado


#Llamando a la función
numero1 = 12
numero2 = 3
resultado_suma = suma(numero1, numero2)
print(f"{numero1} + {numero2} = {resultado_suma}")


lista = [23, 45, 56, 32, 12]
print(lista)
lista.sort() #Método sort(): diseñado para cambiar el objeto.
print(lista)
resultado = sum(lista)
print(resultado)

