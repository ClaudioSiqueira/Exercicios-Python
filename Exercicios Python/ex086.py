matriz = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]

for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input('Digite um valor para [{}, {}]: '.format(linha + 1, coluna + 1)))

for l in range(0, 3):
    for c in range(0, 3):
        print('[{:^5}] '.format(matriz[l][c]), end='')
    print('')
