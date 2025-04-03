altitud_inicial = print("Ingrese la altitud inicial del satélite (en kilómetros): ")
coeficiente_arrastre = print("Ingrese el coeficiente de arrastre inicial (un valor decimal pequeño, como 0.01): ")
altitud_minima = print("Ingrese la altitud mínima de seguridad del satélite (en kilómetros): ")

print("Simulando la desintegración del orbital...")

while altitud_inicial > altitud_minima:
    altitud_perdida = coeficiente_arrastre * altitud_inicial
    altitud_inicial -= altitud_perdida
    orbitas_completadas += 1
    coeficiente_arrastre *= 0.0001  

    print(f"Órbita {orbitas_completadas}: Altitud actual = {altitud_inicial:.2f} km")

if altitud_inicial <= 0:
    print("El satélite ha reeingresado en la atmósfera.")
else:
    print(f"El satélite ha ingresado a una {altitud_inicial:.2f} km después de {orbitas_completadas} órbitas.")


altitud_perdida = coeficiente_arrastre * altitud_inicial
diferencia_altitud = altitud_inicial - altitud_perdida
