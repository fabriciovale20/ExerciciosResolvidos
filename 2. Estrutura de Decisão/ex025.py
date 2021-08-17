"""
    Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:

a) "Telefonou para a vítima?"
b) "Esteve no local do crime?"
c) "Mora perto da vítima?"
d) "Devia para a vítima?"
e) "Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a
participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como
"Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".
"""

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
