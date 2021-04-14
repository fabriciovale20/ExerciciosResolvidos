p1 = input("Telefonou para a vítima? ")
p2 = input("Esteve no local do crime?")
p3 = input("Mora perto da vítima?")
p4 = input("Devia para a vítima?")
p5 = input("Já trabalhou com a vítima?")

resultado = 0

if p1 in 'Ss':
    resultado += 1
if p2 in 'Ss':
    resultado += 1
if p3 in 'Ss':
    resultado += 1
if p4 in 'Ss':
    resultado += 1
if p5 in 'Ss':
    resultado += 1

if resultado < 2:
    print('Inocente')
elif resultado == 2:
    print('Suspeito')
elif 3 <= resultado <= 4:
    print('Cúmplice')
else:
    print('Assassino')