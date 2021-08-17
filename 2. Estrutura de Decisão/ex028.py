"""
    Exercício 28

    O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:

                                  Até 5 Kg           Acima de 5 Kg
            File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
            Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
            Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg

Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção,
porém não há limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o cliente receberá
ainda um desconto de 5% sobre o total da compra. Escreva um programa que peça o tipo e a quantidade de carne comprada
pelo usuário e gere um cupom fiscal, contendo as informações da compra: tipo e quantidade de carne, preço total,
tipo de pagamento, valor do desconto e valor a pagar.
"""

print('-'*30)
print('{:^30}'.format('SUPERMERCADO TABAJARA'))
print('-'*30)

tipo_de_carne = int(input('Tipos de carne\n1- Filé Duplo\n2- Alcatra\n3- Picanha\n'
                          'Escolha: '))
peso_da_carne = int(input('Informe o peso: '))

if tipo_de_carne == 1:
    nome_da_carne = 'Filé Duplo'
    if peso_da_carne <= 5:
        preco_carne = 4.9
    else:
        preco_carne = 5.8

elif tipo_de_carne == 2:
    nome_da_carne = 'Alcatra'
    if peso_da_carne <= 5:
        preco_carne = 5.9
    else:
        preco_carne = 6.8

elif tipo_de_carne == 3:
    nome_da_carne = 'Picanha'
    if peso_da_carne <= 5:
        preco_carne = 6.9
    else:
        preco_carne = 7.8

print()
print(f'Você escolheu a carne {nome_da_carne} e {peso_da_carne}Kg')
forma_de_pagamento = int(input('1- Cartão Tabajara (10% desconto)\n2- Dinheiro\nQual forma de pagamento? '))

total = peso_da_carne * preco_carne

if forma_de_pagamento == 1:
    desconto = 10
    pagamento = 'Cartão Tabajara'
    string_desconto = '(Desconto 10%)'
else:
    desconto = 0
    pagamento = 'Dinheiro'
    string_desconto = ''

valor_desconto = total * (desconto/100)
total_a_pagar = total - valor_desconto

print()
print('='*50)
print('\033[1:97m{:^50}\033[m'.format('NOTA FISCAL'))
print('='*50)
print(f'Código: \033[96m{tipo_de_carne}\033[m\n'
      f'Descrição: \033[96m{nome_da_carne}\033[m\n'
      f'Peso: \033[96m{peso_da_carne} Kg\033[m\n'
      f'Preço: \033[96mR$ {preco_carne:.2f}\033[m\n'
      f'Forma de pagamento: \033[96m{pagamento} {string_desconto}\033[m\n'
      f'\n'
      f'\033[1:97mValor à pagar: R$ {total_a_pagar:.2f}\033[m \033[37m(Desconto de R$ {valor_desconto:.2f})\033[m')
print('='*50)
