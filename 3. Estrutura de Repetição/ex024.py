numero = int(input('Digite um número: '))

cont = soma_nota = 0

for c in range(1, numero+1):
    nota = float(input(f'{c}º nota: '))
    cont += 1
    soma_nota += nota
    if cont == 1:
        maior = nota
        menor = nota
    elif nota > maior:
        maior = nota
    elif nota < menor:
        menor = nota

print(f'Foram digitadas {cont} notas.\n'
      f'Pontuação total: {soma_nota:.2f} - Maior nota: {maior:.2f} / Menor nota: {menor:.2f}\n'
      f'Média: {soma_nota/cont:.2f}')
