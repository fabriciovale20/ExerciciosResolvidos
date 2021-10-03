"""
    Exercício 43

    O cardápio de uma lanchonete é o seguinite:
Especificação   Código  Preço
Cachorro Quente 100     R$ 1,20
Bauru Simples   101     R$ 1,30
Bauru com ovo   102     R$ 1,50
Hambúrguer      103     R$ 1,20
Cheeseburguer   104     R$ 1,30
Refrigerante    105     R$ 1,00

    Faça um programa que leia o código dos itens pedidos e as quantidades desejadas. Calcule e mostre o valor a ser
pago por item (preço * quantidade) e o total geral do pedido. Considere que o cliente deve informar quando o pedido
deve ser encerrado.
"""

from time import sleep

cont = 1
lanche = resp = ''
lanche_100 = lanche_101 = lanche_102 = lanche_103 = lanche_104 = lanche_105 = total = 0

print('-' * 45)
print(f'\033[97m{"CARDÁPIO DA LANCHONETE":^45}\033[m')
print('-' * 45)

print('  \033[97mEspecificação   \033[91m|\033[m   \033[97mCódigo  \033[91m|\033[m   \033[97mPreço\033[m')
print(f'''\033[96m→ Cachorro Quente      100       R$ 1,20
→ Bauru Simples        101       R$ 1,30
→ Bauru com ovo        102       R$ 1,50
→ Hambúrguer           103       R$ 1,20
→ Cheeseburguer        104       R$ 1,30
→ Refrigerante         105       R$ 1,00\033[m''')
print('-' * 45)

while True:
    print(f'\033[97m••• {cont}º PEDIDO •••\033[m')
    try:
        cod = int(input('Código do produto: '))
        if cod < 100 or cod > 105:
            print(f'\033[91mAVISO: Não temos o lanche {cod} no cardápio.\033[m')
            continue
    except Exception:
        print('\033[91mERRO: Código do lanche inválido.\033[m')
        continue
    else:
        if cod == 100:
            lanche = 'Cachorro Quente'
        elif cod == 101:
            lanche = 'Bauru Simples'
        elif cod == 102:
            lanche = 'Bauru com ovo'
        elif cod == 103:
            lanche = 'Hambúrguer'
        elif cod == 104:
            lanche = 'Cheeseburguer'
        else:
            lanche = 'Refrigerante'

    while True:
        try:
            qnt = int(input(f'\033[97m{lanche}\033[m, quantidade: '))
        except Exception:
            print('\033[91mERRO: Quantidade do lanche inválida, tente novamente.\033[m')
            continue
        else:
            if cod == 100:
                lanche = 'Cachorro Quente'
                lanche_100 += qnt
            elif cod == 101:
                lanche = 'Bauru Simples'
                lanche_101 += qnt
            elif cod == 102:
                lanche = 'Bauru com ovo'
                lanche_102 += qnt
            elif cod == 103:
                lanche = 'Hambúrguer'
                lanche_103 += qnt
            elif cod == 104:
                lanche = 'Cheeseburguer'
                lanche_104 += qnt
            else:
                lanche = 'Refrigerante'
                lanche_105 += qnt
            break

    while True:
        try:
            resp = str(input('Realizar outro pedido? [S/N] ')).strip().upper()[0]
        except Exception:
            print('\033[91mERRO: resposta inválida, tente novamente.\033[m')
            continue
        else:
            if resp not in 'SN':
                continue
            else:
                break
    print('-' * 45)

    if resp == 'N':
        break

    cont += 1

total = (lanche_100 * 1.2) + (lanche_101 * 1.3) + (lanche_102 * 1.5) + (lanche_103 * 1.2) + (
            lanche_104 * 1.3) + lanche_105

print('\n\033[97mFinalizando pedido', end='')
for c in range(0, 3):
    print('.', end='')
    sleep(0.5)
print()

print(f'''\n\033[97mTOTAL DE PEDIDOS: {cont}\033[m
\033[97m  Especificação     \033[91m|\033[m   \033[97mQuantidade  \033[91m|\033[m   \033[97mTotal\033[m
\033[96m→ Cachorro Quente           {lanche_100:^2}         R$ {lanche_100 * 1.2:^6.2f}
→ Bauru Simples             {lanche_101:^2}         R$ {lanche_101 * 1.3:^6.2f}
→ Bauru com ovo             {lanche_102:^2}         R$ {lanche_102 * 1.5:^6.2f}
→ Hambúrguer                {lanche_103:^2}         R$ {lanche_103 * 1.2:^6.2f}
→ Cheeseburguer             {lanche_104:^2}         R$ {lanche_104 * 1.3:^6.2f}
→ Refrigerante              {lanche_105:^2}         R$ {lanche_105 * 1:^6.2f}\033[m

\033[7:30:107m  Valor à pagar: R$ {total:.2f}  \033[m''')
