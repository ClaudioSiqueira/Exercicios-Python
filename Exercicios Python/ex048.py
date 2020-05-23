soma = 0
count = 0
for c in range(3, 501, 3):
    if c % 2 == 1:
        soma = soma + c
        count = count + 1
print('A soma dos {} valores solicitados é {}'.format(count, soma))
