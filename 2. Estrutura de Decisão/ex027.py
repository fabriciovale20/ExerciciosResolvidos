"""
    Exercício 27

    Uma fruteira está vendendo frutas com a seguinte tabela de preços:

                                  Até 5 Kg           Acima de 5 Kg
            Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
            Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg

Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um
desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg)
de maças adquiridas e escreva o valor a ser pago pelo cliente.
"""

qnt_morango = int(input('Quantidade em Kg de Morango: '))
qnt_maca = int(input('Quantidade em Kg de Maçã: '))
print()

qnt_fruta = qnt_morango + qnt_maca

if qnt_morango <= 5:
    preco_morango = 2.5
    valor_morango = preco_morango * qnt_morango
else:
    preco_morango = 2.2
    valor_morango = preco_morango * qnt_morango

if qnt_maca <= 5:
    preco_maca = 1.8
    valor_maca = preco_maca * qnt_maca
else:
    preco_maca = 1.5
    valor_maca = preco_maca * qnt_maca

valor_frutas = valor_morango + valor_maca

if qnt_fruta > 8 or valor_frutas > 25:
    desconto = valor_frutas * 0.01
else:
    desconto = 0

valor_frutas -= desconto

print('-'*30)
print('{:^30}'.format('QUANTIDADE E VALORES'))
print('-'*30)
print(f'\033[1:31mMORANGOS\033[m\n'
      f'- {qnt_morango}Kg\n'
      f'- R$ {preco_morango:.2f}\n'
      f'Total R$ {valor_morango:.2f}\n')
print(f'\033[1:32mMAÇÃS\033[m\n'
      f'- {qnt_maca}Kg\n'
      f'- R$ {preco_maca:.2f}\n'
      f'Total R$ {valor_maca:.2f}')
print()
print(f'\033[1:97mValor à pagar R$ {valor_frutas:.2f}', end='')
if desconto > 0:
    print(f' (Desconto de 10% - R$ {desconto:.2f})')
print()
