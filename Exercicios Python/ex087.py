maior_segunda = 9*(10 ^ 200) * (-1)
par = 0
soma_terceiro = 0
matriz = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input('Digite um valor para a posição [{}, {}]: '.format(linha + 1, coluna + 1)))
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        if matriz[l][c] % 2 == 0:
            par += matriz[l][c]
        if c == 2:
            soma_terceiro += matriz[l][2]
        if l == 2:
            if matriz[1][c] > maior_segunda:
                maior_segunda = matriz[1][c]
        print('[{:^5}]'.format(matriz[l][c]), end=' ')
    print('')
print('-=' * 30)
print('A soma dos valores pares é {}'.format(par))
print('A soma dos valores da terceira coluna é {}'.format(soma_terceiro))
print('O maior valor da segunda linha é {}'.format(maior_segunda))
