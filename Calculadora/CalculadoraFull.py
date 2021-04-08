import PySimpleGUI as sg
from time import sleep
from math import factorial, sqrt

class TelaPython:
    def __init__(self):
        #Layout
        layout = [
            [sg.Text('Primeiro valor:', size=(11,0)), sg.Input(size=(15,0),key='a')],
            [sg.Text('Segundo valor:', size=(11,0)), sg.Input(size=(15,0),key='b')],
            [sg.Button('Calcular')],
            [sg.Output(size=(30,20))]
        ]
        #Janela
        self.janela = sg.Window('Calculadora').layout(layout)

    def Iniciar(self):
        while True:
            self.buttuon, self.values = self.janela.Read()
            a = self.values['a']
            b = self.values['b']
            a = int(a)
            b = int(b)
            def calc():
                soma = a + b
                sub = a - b
                mult = a * b
                div = a / b
                exp = a ** b
                faca = factorial(a)
                facb = factorial(b)
                raiza = sqrt(a)
                raizb = sqrt(b)

                print(f'Soma: {soma}')
                print(f'Subtração: {sub}')
                print(f'Multiplicação: {mult}')
                print(f'Divisão: {div:.2f}')
                print(f'Potência: {exp}')
                print(f'Fatorial de {a}!: {faca}')
                print(f'Fatorial de {b}!: {facb}')
                print(f'Raiz de {a}: {raiza:.2f}')
                print(f'Raiz de {b}: {raizb:.2f}')

            calc()

tela = TelaPython()
tela.Iniciar()