matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somapar = 0
somaterceira = 0
maiorsegunda = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input('Digite um valor para [{},  {}]: '.format(l + 1, c + 1)))

for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^3}]', end='')
        if matriz[l][c] % 2 == 0:
            somapar += matriz[l][c]
    if matriz[l][2] != 0:
        somaterceira += matriz[l][2]
    print('')
for coluna in range(0, 3):
    if coluna == 0:
        maiorsegunda = matriz[l - 1][2]
    else:
        if maiorsegunda > matriz[2][c]:
            maiorsegunda = matriz[2][c]
print('A soma dos valores pares é {}'.format(somapar))
print('A soma dos valores da terceira coluna é {}'.format(somaterceira))
print('O maior valor da segunda linha é {}'.format(maiorsegunda))

