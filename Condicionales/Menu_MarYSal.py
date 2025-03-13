#Crear un menu con diferentes platos.
#Cuando el usuario selecciona uno, se debe imrpmir que contiene el plato
#Minimo 3 platos

print("*" * 60)
print ("MarYSal")
print ("*" * 60)

print ("T. Tilapia\nM. Mojarra\nC. Ceviche de camarones\nP. Pargo Rojo\nA. Atún")
plato = input("Ingrese el plato a ordenar: ").upper()

match plato:
    case 'T':
        print ("El plato viene acompañado de: Arroz de coco, ensalada, patacones y guandol.o")
    case 'M': 
        print ("El plato viene acompañado de: Chips de platano, ensalada de papa y guandolo.")
    case 'C': 
        print ("El plato viene acompañado de: Galleta Saltín Noel y guandolo.")
    case 'P': 
        print ("El plato viene acompañado de: Yuca frita, ensalada de repollo y guandolo.")
    case 'A': 
        print ("El plato viene acompañado de: Monedas de platano verde, arroz de coco y guandolo.")