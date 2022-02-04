"""
    Exercício 11

    Data com mês por extenso. Construa uma função que receba uma data no formato DD/MM/AAAA e devolva uma string no formato D de mesPorExtenso de AAAA.
Opcionalmente, valide a data e retorne NULL caso a data seja inválida.
"""

def validador(data):
    barra = 0

    if len(data) != 10:  # Validar total de dígitos da data
        return "Data inválida (Dígitos)"
    else:
        for c in data: # Consultar se a data contém as duas barras que divide a data
            if c == '/':
                barra += 1
        
        if barra != 2: # Validar barras
            return "Data inválida (Formato)"
        else:
            if data[2] != '/' and data[5] != '/': # Validar se as barras estão na posição correta
                return "Data inválida (Formato incorreto)"

    dia = int(data[:2])
    mes = int(data[3:5])
    ano = int(data[6:])

    if dia < 1 or dia > 31: # Validar dia
        return "Dia inválido"
    elif mes < 1 or mes > 12: # Validar mês
        return "Mês inválido"
    elif ano < 1: # Validar ano
        return "Ano inválido"
    elif mes == 2 and dia >= 29:
        if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0: # Validar dia para o mês de fevereiro em anos bissexto
            pass
        else:
            if dia >= 29:
                return "Data inválida (Ano não bissexto)"
    
    if mes == 1:
        mes_string = 'Janeiro'
    elif mes == 2:
        mes_string = 'Fevereiro'
    elif mes == 3:
        mes_string = 'Março'
    elif mes == 4:
        mes_string = 'Abril'
    elif mes == 5:
        mes_string = 'Maio'
    elif mes == 6:
        mes_string = 'Junho'
    elif mes == 7:
        mes_string = 'Julho'
    elif mes == 8:
        mes_string = 'Agosto'
    elif mes == 9:
        mes_string = 'Setembro'
    elif mes == 10:
        mes_string = 'Outubro'
    elif mes == 11:
        mes_string = 'Novembro'
    elif mes == 12:
        mes_string = 'Dezembro'
    
    return f'{dia} de {mes_string} de {ano}'

def mesPorExtenso():
    pass

while True:
    data = input('Informe uma data (DD/MM/AAAA): ')

    print(validador(data))
