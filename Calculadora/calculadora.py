import PySimpleGUI as sg

def janela_calculadora():
    layout = [
        [sg.Input()],
        [sg.Button('7',size=(3,1)),sg.Button('8',size=(3,1)),sg.Button('9',size=(3,1)),sg.Button('x',size=(3,1))],
        [sg.Button('4',size=(3,1)),sg.Button('5',size=(3,1)),sg.Button('6',size=(3,1)),sg.Button('-',size=(3,1))],
        [sg.Button('1',size=(3,1)), sg.Button('2',size=(3,1)), sg.Button('3',size=(3,1)),sg.Button('+',size=(3,1))],
        [sg.Button('+/-',size=(3,1)),sg.Button('0',size=(3,1)),sg.Button(',',size=(3,1)),sg.Button('=',size=(3,1))]
    ]
    return sg.Window('Calculadora', layout=layout, finalize=True, size=(250,300))

janela1 = janela_calculadora()

while True:
    janela,evento,valor = sg.read_all_windows()
    if evento == sg.WIN_CLOSED or evento == 'Sair':
        break