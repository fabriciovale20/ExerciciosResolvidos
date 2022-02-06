"""
    Exercício 13

    Desenha moldura. Construa uma função que desenhe um retângulo usando os caracteres '+' , '-' e '|'.
Esta função deve receber dois parâmetros, linhas e colunas, sendo que o valor por omissão é o valor mínimo igual a 1 e o valor máximo é 20.
Se valores fora da faixa forem informados, eles devem ser modificados para valores dentro da faixa de forma elegante.    
"""

def retangulo(linha, coluna):
    for l in range(0, linha):
        if l == 0 or l == linha - 1: # Símbolo de + para os primeiro caracter da 1º e última linha
            print('+', end='')
        else:
            print('|', end='') # Para o primeiro caracter das linhas (Exceto a primeira e a última)
        for c in range(0, coluna):
            if c != coluna - 1: # Verificar se é a última coluna
                if l == 0 or l == linha - 1: # Verificar se é a 1º ou última linha
                    print('—', end='')
                else:
                    print(' ', end='')
            elif l == 0 and c == coluna - 1 or l == linha - 1 and c == coluna - 1: # Identificar a linha
                print('+') # Inserido no final da linha (Para caso for a 1º ou última linha)
            else:
                print('|') # Inserido no final da linha (Exceto para a 1º e última linha)

while True:
    print('Valor mínimo e máximo de linhas e colunas: 1 e 20')
    linha = int(input('Nº de linhas: ')) 
    if 1 > linha > 20:
        print('Valor de linhas inválido. Modificado para 3')
        linha = 3

    coluna = int(input('Nº de colunas: '))
    if 1 > coluna > 20:
        print('Valor de colunas inválido. Modificado para 3')
        coluna = 3

    retangulo(linha, coluna)
