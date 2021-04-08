import random
n = int(input('Informe um número: '))
pc = random.randint(0,100)
cont=0
while n != pc:
    if n > pc:
        n = int(input('\033[31mInforme um número menor...\033[m: '))
        cont+=1
    else:
        n = int(input('\033[34mInforme um número maior...\033[m: '))
        cont+=1
print(f'\033[32mPARABÉNS!!! Você acertou.\nO número escolhido foi {pc}\033[m.\n\033[31mVocê acertou depois de {cont} tentativas.\033[m')