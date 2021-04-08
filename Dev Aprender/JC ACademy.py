import PySimpleGUI as sg

# Criar as janelas e estilos (Layout)
def janela_login():
    layout = [
        [sg.Text('Usuário'), sg.Input(key='usuario', size=(30,1))],
        [sg.Text('Senha  '), sg.Input(key='senha', password_char='*', size=(30,1))],
        [sg.Button('Entrar'), sg.Button('Sair')],
        [sg.Radio('Aluno','escolha',key='aluno'),sg.Radio('Personal','escolha',key='personal')]
    ]
    return sg.Window('Login JC Academy', layout=layout, finalize=True)

def janela_personal():
    nome = valores['usuario']
    layout = [
        [sg.Text(f'Olá {nome}, selecione uma opção:')],
        [sg.Button('Cadastro de Clientes'), sg.Button('Consultar Aluno')]
    ]
    return sg.Window('JC Academy Personal', layout=layout, finalize=True, size=(320,80))

def janela_aluno():
    nome = valores['usuario']
    layout = [
        [sg.Text(f'Bem-vindo(a) {nome}, selecione uma opção:')],
        [sg.Button('Consultar Ficha'), sg.Button('Consultar Avaliação')]
    ]
    return sg.Window('Área do Aluno JC Academy', layout=layout, finalize=True, size=(320,80))

def janela_cadastro():
    layout = [
        [sg.Text('Nome:'),sg.Input(size=(50,1))],
        [sg.Text('\nEndereço')],
        [sg.Text('Bairro'),sg.Input(size=(10,1))],
        [sg.Text('Rua   '),sg.Input(size=(30,1)),sg.Text('Nº'),sg.Input(size=(5,1))],
        [sg.Text('\nMedições')],
        [sg.Text('Peso (Kg)'),sg.Input(size=(4,1))],
        [sg.Text('Altura'),sg.Input(size=(4,1))]
    ]
    return sg.Window('Cadastro de Clientes JC ACademy', layout=layout, finalize=True, size=(420,200))

# Criar as janelas iniciais
janela1,janela2,janela3 = janela_login(),None,None
# Criar um loop de leitura de eventos
while True:
    janela,evento,valores = sg.read_all_windows()
    # Quando a janela for fechada
    if evento == sg.WIN_CLOSED or evento == 'Sair':
        break
    # Quando queremos ir para próxima janela
    if janela == janela1 and valores['aluno'] == True and evento == 'Entrar':
        janela2 = janela_aluno()
        janela1.hide()
    elif janela == janela1 and valores['personal'] == True and evento == 'Entrar':
        janela3 = janela_personal()
        janela1.hide()
# Lógica de o que deve acontecer ao clicar os botões
    #Janela de Alunos
    if janela == janela2 and evento == 'Fazer Pedido':
        if valores['pizza1'] == True and valores['pizza2'] == True:
            sg.popup('Foram solicitados uma Pizza Pepperoni e uma Pizza Catupiri c/ Frango')
        elif valores['pizza1'] == True:
            sg.popup('Foi solicitado uma Pizza Peperoni')
        elif valores['pizza2'] == True:
            sg.popup('Foi solicitado uma Pizza Catupiro c/ Frango')
    #Janela de Personal
    if janela == janela3 and evento == 'Cadastro de Clientes':
        janela3.hide()
        janela2 = janela_cadastro()
