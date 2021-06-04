from time import sleep

print('Coletor de Temperatura (Parar encerrar o programa digite "Parar")')
cont = soma = 0

while True:
    try:
        cont += 1
        temp = float(input(f'Temperatura {cont}º: '))
        if cont == 1:
            maior = temp
            menor = temp
        if temp > maior:
            maior = temp
        elif temp < menor:
            menor = temp
        soma += temp
    except:
        cont -= 1
        print('Coleta finalizada, processando', end = '')
        break

for n in range(0,10):
    sleep(0.3)
    print('.', end = '')

print()
print('='*30)
print(f'Soma : {soma:.2f}\n'
      f'Média : {soma/cont:.2f}\n'
      f'Maior temperatura : {maior:.2f}\n'
      f'Menor temperatura : {menor:.2f}')
