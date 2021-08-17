"""
    Exercício 15

    Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser
um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.

Dicas:
→ Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
→ Triângulo Equilátero: três lados iguais;
→ Triângulo Isósceles: quaisquer dois lados iguais;
→ Triângulo Escaleno: três lados diferentes;
"""

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
