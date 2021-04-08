import PySimpleGUI as sg

# Janela Login
def janela_login():
    sg.theme('Reddit')
    layout = [
        [sg.Text('Nome')],
        [sg.Input()],
        [sg.Button('Entrar')]
    ]
    return sg.Window('Login JC Academy', layout=layout, finalize=True)

# Janela de Login inserido
def janela_logininserido():
    sg.theme('Reddit')
    layout = [
        [sg.Text('Selecione sua opção abaixo')],
        [sg.Button('Cadastro de Clientes')]
    ]
    return sg.Window('JC Academy', layout=layout, finalize=True)


# Janela de Cadastro de Clientes
# Criação de janelas
janela1, janela2 = janela_login, None
# Criando Loop de leitura de eventos
while True:
    window, event, values = sg.read_all_windows()
    # Quando a janela for fechada
    if window == janela1 and event == sg.WINDOW_CLOSED:
        break
    # Quando queremos ir para a próxima janela
    if window == janela1 and event == 'Entrar':
        janela2 = janela_logininserido()
        janela1.hide()
    # Quando queremos voltar para janela anterior
# Ler eventos
