import random

titulo = input("Ingrese su título (Sr. o Sra.): ")
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
print(f"{titulo} {nombre} {apellido}, ¡Bienvenido a FastFast Airlines!")

print("\nVuelos a ciudades disponibles: Medellín, Bogotá, Cartagena")
origen = input("Ingrese la ciudad de origen: ")
destino = input("Ingrese la ciudad de destino: ")

dia_semana = input("Ingrese el día de la semana en el que desea viajar (por ejemplo, lunes): ").lower()
dia_mes = int(input("Ingrese el día del mes (un número entre 1 y 30): "))

if (origen == 'Medellín' and destino == 'Bogotá') or (origen == 'Bogotá' and destino == 'Medellín'):
    print("Ruta seleccionada: Medellín - Bogotá")
    distancia = 240

elif (origen == 'Medellín' and destino == 'Cartagena') or (origen == 'Cartagena' and destino == 'Medellín'):
    print("Ruta seleccionada: Medellín - Cartagena")
    distancia = 650
elif (origen == 'Bogotá' and destino == 'Cartagena') or (origen == 'Cartagena' and destino == 'Bogotá'):
    print("Ruta seleccionada: Bogotá - Cartagena")
    distancia = 1150

else:
    print("Error: Ruta no válida.")
 
if distancia < 400:
    precio = [79900, 119900]
else:
    precio = [199000, 250000]

if dia_semana == "viernes" or dia_semana == "sábado" or dia_semana == "domingo":
    precio = precio[1]

else:
    precio = precio[0]  

preferencia = input("¿Prefiere un asiento en el pasillo, junto a la ventana o sin preferencia? ").lower()

if preferencia == "pasillo":
    asiento = f"{numero_asiento}C"
elif preferencia == "ventana":
    asiento = f"{numero_asiento}A"
else:
    asiento = f"{numero_asiento}B"

numero_asiento = random.randint(1, 29)

print("\n--- Detalles de su reserva ---")
print(f"Nombre: {titulo} {nombre} {apellido}")
print(f"Origen: {origen}")
print(f"Destino: {destino}")
print(f"Fecha de vuelo: {dia_semana.capitalize()} {dia_mes}")
print(f"Precio del boleto: ${precio:,}")
print(f"Asiento asignado: {asiento}")