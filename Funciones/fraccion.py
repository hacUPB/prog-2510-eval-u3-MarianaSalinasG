def mcd(num, den):
    if num <= den:
        menor = num
    else:
        menor = den

    for divisor in range (menor, 0, -1):
        if num % divisor == 0 and den % divisor == 0:
            max_comun_div = divisor             
            break
    return max_comun_div

def imprime_la_fraccion(num, den, maximo):
    print(f"Fraccion original: {num}/{den}")
    num = num // maximo
    den = den // maximo     
    print(f"Fraccion simplificada: {num}/{den}")