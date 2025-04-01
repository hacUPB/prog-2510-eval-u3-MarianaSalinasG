def conversionDePuntuacion(puntuacion:int):
    if puntuacion < 0:
        letra = 'Puntaje no válido'
    elif puntuacion < 60:
        letra = 'F'
    elif puntuacion < 70:
        letra = 'D'
    elif puntuacion < 80:
        letra = 'C'
    elif puntuacion < 90:
        letra = 'B'
    elif puntuacion <= 100:
        letra = 'A'
    else:    
        letra = 'Puntaje no válido'
    return letra    

def main():   
    puntuacion = int(input('Ingrese la puntuación: '))
    print(f"La calificación en letras es: {conversionDePuntuacion(puntuacion)}")

if __name__ == "__main__":  
    main()