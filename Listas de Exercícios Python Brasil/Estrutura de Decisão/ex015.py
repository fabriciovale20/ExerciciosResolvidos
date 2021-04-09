n1 = int(input('Primeiro lado: '))
n2 = int(input('Segundo lado: '))
n3 = int(input('Terceiro lado: '))

if n1 + n2 > n3 and n1 + n3 > n2 and n2 + n3 > n1:
    print('Os valores informados forma um triângulo ', end='')
    if n1 == n2 == n3:
        print('Equilátero.')
    elif n1 == n2 or n2 == n3 or n1 == n3:
        print('Isósceles.')
    elif n1 != n2 != n3:
        print('Escaleno.')
else:
    print('Os valores informados NÃO forma um triângulo.')