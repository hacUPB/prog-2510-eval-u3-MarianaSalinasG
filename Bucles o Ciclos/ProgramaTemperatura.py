print("Programa de Conversión de Temperatura")
print("_"*35)
print("Celcius\t|\tFahrenheit")
print("_"*35)

for celcius in range(0,110,10):

    fahrenheit = (celcius * 9/5) + 32
    print(f"{celcius}\t|\t{fahrenheit}") 

print("_"*35)                                               

    
