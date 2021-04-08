#Analisador de Textos
nome = str(input('Digite seu nome completo: ')).strip()
letras = len(nome)-nome.count(' ')
primeiro = nome.split()
l1 = primeiro[0]
l = len(l1)
print('Analisando seu nome...')
print(f'Seu nome em maiúsculas é {nome.upper()}.')
print(f'Seu nome em minúsculas é {nome.lower()}.')
print(f'Seu nome tem ao todo {letras} letras.')
print(f'Seu primeiro nome é {primeiro[0]} e ele tem {l} letras.')
