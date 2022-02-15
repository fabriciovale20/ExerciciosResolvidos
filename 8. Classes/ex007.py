"""
    Exercício 7

    Classe Bichinho Virtual
Crie uma classe que modele um Tamagushi (Bichinho Eletrônico):
→ Atributos: Nome, Fome, Saúde e Idade
→ Métodos: Alterar Nome, Fome, Saúde e Idade;

Retornar Nome, Fome, Saúde e Idade 
Obs: Existe mais uma informação que devemos levar em consideração, o Humor do nosso tamagushi,
este humor é uma combinação entre os atributos Fome e Saúde, ou seja, um campo calculado, então não devemos criar um atributo
para armazenar esta informação por que ela pode ser calculada a qualquer momento.
"""

# Padronização de atributos
# Fome 1 à 10 | Saúde 1 à 10 | Idade 0 à 100 | Humor 0 à 20 (Automático) 0% à 50% Triste =( → 51% à 75% Alegre =) → 76% à 100% Feliz =D

from time import sleep

class Tamagushi():
    def __init__(self, nome, fome=5, saude=5, idade=0, status=''):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade
        self.status = status # Salvar status do humor

        self.verificador_humor() # Verificar humor

    def alterar_nome(self, novo_nome): # Função alterar nome
        self.nome = novo_nome

    def alterar_fome(self, qnt_fome): # Função alterar fome
        if self.fome + qnt_fome > 10 or self.fome + qnt_fome < 0: # Caso a fome exceder o valor 10 ou menor que 0
            if qnt_fome < 0:
                print('Fome inválida abaixo de 0') # Se o valor inserido for negativo
            else:
                print('Fome excedeu o máximo de 10') # Se o valor inserido for positivo
        else:
            self.fome += qnt_fome
            print(f'Fome alterada para {self.fome}') # Adiconado valor
        
        self.verificador_humor()

    def alterar_saude(self, qnt_saude): # Função alterar saúde
        if self.saude + qnt_saude > 10 or self.saude + qnt_saude < 0: # Caso a fome exceder o valor 10 ou menor que 0
            if qnt_saude < 0:
                print('Saude inválida abaixo de 0') # Se o valor inserido for negativo
            else:
                print('Saude excedeu o máximo de 10') # Se o valor inserido for positivo
        else:
            self.saude += qnt_saude
            print(f'Saude alterada para {self.saude}') # Adiconado valor
        
        self.verificador_humor()

    def alterar_idade(self, nova_idade): # Função alterar idade
        if self.idade + nova_idade > 100: # Caso a idade for maior que 100
            print('Idade inválida, excede os 100 anos')
        elif self.idade + nova_idade < 0: # Caso a idade for menor que 0
            print('Idade inválida, menor que 0 anos')
        else:
            print(f'Idade cadastrada, agora seu bichinho tem {nova_idade} anos')

    def verificador_humor(self): # Verificador de humor
        humor = (self.saude + self.fome)/0.2 # Somado a Fome e Saúde e realizado a porcentagem para definir o humor
        # Caso a fome for 10 e saúde 10, a porcentagem será 100%
        # Cálculo (10 + 10)/20/100 → 20/0,2 → 100%

        if humor >= 76:
            self.status = 'Feliz =D'
        elif 50 < humor < 76:
            self.status = 'Alegre =)'
        else:
            self.status = 'Triste =('

    def dados_tamagushi(self): # Função que mostra todos os dados
        print('-'*50)
        print(f'''Nome: {self.nome}
Fome: {self.fome}
Saúde: {self.saude}
Idade: {self.idade}
Humo: {self.status}''')
        print('-'*50)

# Exemplo interativo
print('JOGO DO TAMAGUSHI')

print('\nVamos começar?')
print('Primeiro dê um nome para seu bichinho.')
nome = input('Nome: ')
pet = Tamagushi(nome)

print('Vamos registrar seu bicho no nosso Pet, só um minutinho', end='')
for _ in range(5):
    sleep(0.8)
    print('.', end='')

print('\nOláááá, vamos cuidar do seu novo Pet?')
sleep(2)
print(f'Então ele se chama {pet.nome}!!!')
sleep(2)
print('Vamos analisar seu status:')
pet.dados_tamagushi()
sleep(2)

while True:
    sleep(2)
    print(f'Escolha uma opção que deseja para seu Pet {pet.nome}:')
    opc = int(input('''1. Mudar o nome
2. Fome
3. Saúde
4. Idade
5. Ver status
6. Sair
Opção: '''))

    while opc > 6 or opc < 1:
        opc = int(input('Opção inválida, escolha novamente: '))

    if opc == 1:
        nome = input('Qual seria o novo nome para seu Pet? ')
        pet.alterar_nome(nome)
    elif opc == 2:
        fome = int(input('Hummmm, nhaminhami!!! Quanto de comer você vai dar? '))
        if fome < 0:
            print('Pet: Pouca comida =(')
        else:
            print('Pet: Que gostoso =)')
        
        pet.alterar_fome(fome)
    elif opc == 3:
        saude = int(input('Vamos colocar seu bichinho pra dormir quanto tempo? '))

        if saude < 0:
            print('Pet: Não dormi quase nada O.O')
        else:
            print('Pet: Ohhh sono bom *-*')
        
        pet.alterar_saude(saude)
    elif opc == 4:
        idade = int(input('Quantos aninhos seu pet tem? '))
        pet.alterar_idade(idade)
    elif opc == 5:
        pet.dados_tamagushi()
    elif opc == 6:
        print(f'Até mais, vamos guardar seu bichinho {pet.nome}')


