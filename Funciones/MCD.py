from fraccion import mcd, imprime_la_fraccion

def main():
    num = int(input("Introduce el numerador: "))
    den = int(input("Introduce el denominador: "))
    maximo = mcd(num, den)
    print(f"M.C.D = {maximo}")
    imprime_la_fraccion(num, den, maximo)

if __name__ == "__main__":
    main()