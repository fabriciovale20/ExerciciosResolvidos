"""
    Exercício 15

    Faça um programa que leia um número indeterminado de valores, correspondentes a notas,
encerrando a entrada de dados quando for informado um valor igual a -1 (que não deve ser armazenado). Após esta entrada de dados, faça:
a) Mostre a quantidade de valores que foram lidos;
b) Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
c) Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
d) Calcule e mostre a soma dos valores;
e) Calcule e mostre a média dos valores;
f) Calcule e mostre a quantidade de valores acima da média calculada;
g) Calcule e mostre a quantidade de valores abaixo de sete;
h) Encerre o programa com uma mensagem;
"""

from time import sleep

numeros = []
cont = 1

print('-'*30)
print('COLETOR DE NÚMEROS'.center(30))
print('-'*30)

while True:
    try:
        num = str(input(f'{cont}º número: '))
        if num.isnumeric():
            num = float(num)
            numeros.append(num)
            cont += 1
        else:
            if num == '-1':
                break
            else:
                print('Valor inválido, tente novamente.')
            continue
    except Exception:
        print('Valor inválido, tente novamente.')

print('-'*20)
print('Finalizando coleta de números', end='')
for c in range(0, 3):
    sleep(1)
    print('.', end='')
print()

print(f'a) Mostre a quantidade de valores que foram lidos: {len(numeros)}')
print(f'b) Exiba todos os valores na ordem em que foram informados, um ao lado do outro:\nNúmeros: ', end='')
for num in numeros:
    print(num, end=' ')
print()

print(f'c) Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro:\nNúmeros: ')
for num in range(len(numeros)-1, -1, -1):
    print(numeros[num])
    
print(f'd) Calcule e mostre a soma dos valores: ', end='')
soma = sum(numeros)
print(soma)

print(f'e) Calcule e mostre a média dos valores: ', end='')
media = soma / len(numeros)
print(media)

print(f'f) Calcule e mostre a quantidade de valores acima da média calculada: ', end='')
numero_acima_media = 0
for num in numeros:
    if num > media:
        numero_acima_media += 1
print(numero_acima_media)

print(f'g) Calcule e mostre a quantidade de valores abaixo de sete: ', end='')
numero_abaixo_sete = 0
for num in numeros:
    if num < 7:
        numero_abaixo_sete += 1
print(numero_abaixo_sete)

print(f'h) Encerre o programa com uma mensagem: ')
print('-'*20)
print('PROGRAMA FINALIZADO'.center(20))
print('-'*20)
