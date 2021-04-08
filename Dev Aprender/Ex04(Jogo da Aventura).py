print('\033[1:31m{:-^60}\033[m'.format('BEM VINDO(A) AO JOGO DA AVENTURA!'))
print('\033[1:30mA história é a de Chapeuzinho Vermelho!\nUm belo dia, ela brincando pelo bosque, se deparou com 2 caminhos.\033[m\nQual caminho você escolheria?')
while True:
    print('1 - Estrada de barro.\n2 - Estrada da floresta.\n3 - Voltar para casa.')
    n = int(input('Escolha: '))
    if n == 1:
        print('Ela encontrou a Casa do Lenhador.')
        n = int(input('O que ela fez?\n1 - Pediu para deixar em casa.\n2 - Ficar na casa dele.\n3 - Chamar a Avó dela.\nEscolha: '))
        if n == 1:
            print('Ficou feliz quando chegou em casa.')
            break
        elif n == 2:
            print('Esperou o Lenhador acabar o trabalho para deixa-lá em casa.')
            break
        elif n == 3:
            print('Aguardou Avó delar vir busca-lá.')
            break
        else:
            print('\033[1:31mEscolha inválida!!!\033[m')
    elif n == 2:
        print('Ficou assustada e saiu correndo para casa.')
        break
    elif n == 3:
        print('Ela voltou para casa e comeu um Bolo.')
        break
    else:
        print('\033[1:31mEscolha inválida!!!\033[m')