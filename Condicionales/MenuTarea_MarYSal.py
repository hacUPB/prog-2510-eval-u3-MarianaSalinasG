#Crear un menu que le permita la seleccion al usuario de los demas ingredientes con los que desea acompañar su menu.

print("*" * 60)
print ("MarYSal")
print ("*" * 60)

print ("T. Tilapia\nM. Mojarra\nC. Ceviche de camarones\nP. Pargo Rojo\nA. Atún")
plato = input("Ingrese el plato a ordenar: ").upper()

if plato == "T":
    acompanante = input("Seleccione el acompañante: \nA. Arroz con coco\nP. Papas a la francesa\nE. Ensalada\n").upper()
    if acompanante == "A":
        print("Usted ha ordenado: Tilapia con Arroz con coco")
    elif acompanante == "P":
        print("Usted ha ordenado: Tilapia con Papas a la francesa")
    elif acompanante == "E":
        print("Usted ha ordenado: Tilapia con Ensalada")
    else:
        print("Opción no válida")
    bebida = input("Seleccione la bebida: \nL. Limonada\nS. Soda de Sandía\nC. Coca Cola\n").upper()
    if bebida == "L":
        print("Usted ha ordenado: Tilapia con Arroz con coco y Limonada")
    elif bebida == "S":
        print("Usted ha ordenado: Tilapia con Arroz con coco y Soda de Sandía")
    elif bebida == "C":
        print("Usted ha ordenado: Tilapia con Arroz con coco y Coca Cola")
    else:
        print("Opción no válida")

elif plato == "M":
    acompanante = input("Seleccione el acompañante: \nA. Arroz con coco\nP. Papas a la francesa\nE. Ensalada\n").upper()
    if acompanante == "A":
        print("Usted ha ordenado: Mojarra con Arroz con coco")
    elif acompanante == "P":
        print("Usted ha ordenado: Mojarra con Papas a la francesa")
    elif acompanante == "E":    
        print("Usted ha ordenado: Mojarra con Ensalada")      
    else:
        print("Opción no válida")
    bebida = input("Seleccione la bebida: \nL. Limonada\nS. Soda de Sandía\nC. Coca Cola\n").upper()
    if bebida == "L":
        print("Usted ha ordenado: Mojarra con Arroz con coco y Limonada")
    elif bebida == "S":
        print("Usted ha ordenado: Mojarra con Arroz con coco y Soda de Sandía")
    elif bebida == "C":
        print("Usted ha ordenado: Mojarra con Arroz con coco y Coca Cola")
    else:
        print("Opción no válida")

elif plato == "C":
    acompanante = input("Seleccione el acompañante: \nA. Arroz con coco\nP. Papas a la francesa\nE. Ensalada\n").upper()
    if acompanante == "A":
        print("Usted ha ordenado: Ceviche de camarones con Arroz con coco")
    elif acompanante == "P":
        print("Usted ha ordenado: Ceviche de camarones con Papas a la francesa")
    elif acompanante == "E":    
        print("Usted ha ordenado: Ceviche de camarones con Ensalada")      
    else:
        print("Opción no válida")
    bebida = input("Seleccione la bebida: \nL. Limonada\nS. Soda de Sandía\nC. Coca Cola\n").upper()
    if bebida == "L":
        print("Usted ha ordenado: Ceviche de camarones con Arroz con coco y Limonada")
    elif bebida == "S":
        print("Usted ha ordenado: Ceviche de camarones con Arroz con coco y Soda de Sandía")
    elif bebida == "C":
        print("Usted ha ordenado: Ceviche de camarones con Arroz con coco y Coca Cola")
    else:
        print("Opción no válida")

elif plato == "P":
    acompanante = input("Seleccione el acompañante: \nA. Arroz con coco\nP. Papas a la francesa\nE. Ensalada\n").upper()
    if acompanante == "A":
        print("Usted ha ordenado: Pargo Rojo con Arroz con coco")
    elif acompanante == "P":
        print("Usted ha ordenado: Pargo Rojo con Papas a la francesa")
    elif acompanante == "E":    
        print("Usted ha ordenado: Pargo Rojo con Ensalada")      
    else:
        print("Opción no válida")
    bebida = input("Seleccione la bebida: \nL. Limonada\nS. Soda de Sandía\nC. Coca Cola\n").upper()
    if bebida == "L":
        print("Usted ha ordenado: Pargo Rojo con Arroz con coco y Limonada")
    elif bebida == "S":
        print("Usted ha ordenado: Pargo Rojo con Arroz con coco y Soda de Sandía")
    elif bebida == "C":
        print("Usted ha ordenado: Pargo Rojo con Arroz con coco y Coca Cola")
    else:
        print("Opción no válida")  

elif plato == "A":
    acompanante = input("Seleccione el acompañante: \nA. Arroz con coco\nP. Papas a la francesa\nE. Ensalada\n").upper()
    if acompanante == "A":
        print("Usted ha ordenado: Atún con Arroz con coco")
    elif acompanante == "P":
        print("Usted ha ordenado: Atún con Papas a la francesa")
    elif acompanante == "E":
        print("Usted ha ordenado: Atún con Ensalada")
    else:
        print("Opción no válida")
    bebida = input("Seleccione la bebida: \nL. Limonada\nS. Soda de Sandía\nC. Coca Cola\n").upper()
    if bebida == "L":
        print("Usted ha ordenado: Atún con Arroz con coco y Limonada")
    elif bebida == "S":
        print("Usted ha ordenado: Atún con Arroz con coco y Soda de Sandía")
    elif bebida == "C":
        print("Usted ha ordenado: Atún con Arroz con coco y Coca Cola")
    else:
        print("Opción no válida")
else:
    print("Opción no válida")
    