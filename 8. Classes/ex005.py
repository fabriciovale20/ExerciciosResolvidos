"""
    Exercício 5

    Classe Conta Corrente: Crie uma classe para implementar uma conta corrente.

A classe deve possuir os seguintes atributos: número da conta, nome do correntista e saldo.
Os métodos são os seguintes: alterarNome, depósito e saque;
No construtor, saldo é opcional, com valor default zero e os demais atributos são obrigatórios.
"""

class ContaCorrente():
    def __init__(self, num_conta, nome_correntista, saldo=0):
        self.num_conta = num_conta
        self.nome_correntista = nome_correntista
        self.saldo = saldo

    def alterarNome(self, novo_nome_correntista): # Função para alterar nome do correntista
        self.nome_correntista = novo_nome_correntista

    def deposito(self, valor_deposito): # Função depositar
        self.saldo += valor_deposito

    def saque(self, valor_retirado): # Função de saque
        if self.saldo <= 0: # Validar se o saldo é maior que 0
            print(f'Saque indisponível! Saldo em conta R$ {self.saldo:.2f}')
        elif self.saldo - valor_retirado < 0: # Validar se o valor para saque é maior do que o que tem em saldo
            print(f'Saque excede o saldo disponível! Saldo em conta R$ {self.saldo:.2f}, saque solicitado R$ {valor_retirado:.2f}.')
        else:
            self.saldo -= valor_retirado # Saque disponível
            print(f'Saque realizado com sucesso! Saldo em conta R$ {self.saldo:.2f}')

    def mostrar_dados(self): # Função extra apenas para mostrar os dados no terminal para facilitar o acompanhamento
        print(f'''Nº da conta: {self.num_conta}
Nome do correntista: {self.nome_correntista}
Saldo: R$ {self.saldo:.2f}''')

conta1 = ContaCorrente(25, 'Fabrício', 250)
conta1.alterarNome('Dylan')
conta1.deposito(250)
conta1.mostrar_dados()

print('-'*50)

conta2 = ContaCorrente(30, 'Paula')
conta2.mostrar_dados()
conta2.saque(2)
