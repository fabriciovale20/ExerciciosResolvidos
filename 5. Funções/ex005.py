"""
    Exercício 5

    Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais: taxaImposto, que é a quantia de imposto
sobre vendas expressa em porcentagem e custo, que é o custo de um item antes do imposto.
A função “altera” o valor de custo para incluir o imposto sobre vendas.
"""

def somaImposto(taxaImposto, custo):
    custo += custo * (taxaImposto/100)
    print(f'Valor com imposto aplicado R$ {custo:.2f}')

imposto = int(input('Valor do imposto em %: '))
valor = float(input('Custo do produto: R$ '))

print(f'Valor do produto R$ {valor:.2f}')
print(f'Taxa de imposto {imposto} %.')
somaImposto(imposto, valor)
