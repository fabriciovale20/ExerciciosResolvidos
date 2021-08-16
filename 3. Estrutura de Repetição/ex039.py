for c in range(1,11):
    print(f'{c}º Aluno')
    altura = float(input('Altura: '))
    if c == 1:
        aluno_alto = c
        altura_maior = altura
        aluno_baixo = c
        altura_menor = altura
    if altura > altura_maior:
        aluno_alto = c
        altura_maior = altura
    elif altura < altura_menor:
        aluno_baixo = c
        altura_menor = altura

print(f'Aluno {aluno_alto} é o mais alto com {altura_maior} metros.')
print(f'Aluno {aluno_baixo} é o mais alto com {altura_menor} metros.')