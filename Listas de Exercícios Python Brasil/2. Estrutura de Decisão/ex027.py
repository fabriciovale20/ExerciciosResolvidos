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
print(f'\033[1:31mMORANGOS\033[m\n- {qnt_morango}Kg\n- R$ {preco_morango:.2f}\nTotal R$ {valor_morango:.2f}\n')
print(f'\033[1:32mMAÇÃS\033[m\n- {qnt_maca}Kg\n- R$ {preco_maca:.2f}\nTotal R$ {valor_maca:.2f}')
print()
print(f'\033[1:97mValor à pagar R$ {valor_frutas:.2f}', end='')
if desconto > 0:
    print(f' (Desconto de 10% - R$ {desconto:.2f})')
print()