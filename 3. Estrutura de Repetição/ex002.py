"""
    Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário,
mostrando uma mensagem de erro e voltando a pedir as informações.
"""

usuario = input('Usuário: ')
senha = input('Senha: ')
print()

while usuario == senha:
    print('AVISO!!!')
    senha = input('Senha igual ao usuário, digite outra senha: ')

print(f'Usuário cadastrado!\nUsuário: {usuario}\nSenha: {senha}')
