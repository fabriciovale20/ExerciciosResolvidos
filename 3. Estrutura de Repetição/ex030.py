n = 0

print('Preço do pão: R$ 0.18\n'
      'Panificadora Pão de Ontem - Tabela de preços')

for c in range(1, 51):
    n += 0.18
    print(f'{c} - R$ {n:.2f}')