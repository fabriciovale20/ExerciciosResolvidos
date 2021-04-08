#Radar eletrônico
vel = int(input('Qual é a velocidade atual do carro? '))
multa = (vel-80)*7
if vel > 80:
    print('\033[31mMULTADO! Você execedeu o limite permitido que é de 80Km/h.')
    print(f'Você deve pagar uma multa de R${multa}\033[m.')
print('\033[32mTenha um bom dia! Dirija sempre com segurança!\033[m')