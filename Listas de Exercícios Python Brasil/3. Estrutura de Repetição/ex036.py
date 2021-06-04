valor = int(input('Montar a tabuada de: '))
inicio = int(input('Começa por: '))
final = int(input('Termina em: '))


def tabuada(valor, inicio, final):
    if final > inicio:
        for c in range(inicio, final + 1):
            print(f'{valor} x {c} = {valor * c}')
    else:
        for c in range(inicio, final - 1, -1):
            print(f'{valor} x {c} = {valor * c}')


tabuada(valor, inicio, final)
