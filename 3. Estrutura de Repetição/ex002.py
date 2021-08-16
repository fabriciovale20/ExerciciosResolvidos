usuario = input('Usuário: ')
senha = input('Senha: ')
print()

while usuario == senha:
    print('AVISO!!!')
    senha = input('Senha igual ao usuário, digite outra senha: ')

print(f'Usuário cadastrado!\nUsuário: {usuario}\nSenha: {senha}')