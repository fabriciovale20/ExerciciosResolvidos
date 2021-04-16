numero = 1
anterior = anterior_2 = 0
while numero < 500:
    if numero == 1:
        anterior = 2
        anterior_2 = 1
        print(f'0 {numero} {numero} {anterior}', end=' ')
    numero = anterior + anterior_2
    anterior_2 = anterior
    anterior = numero

    print(numero, end=' ')
