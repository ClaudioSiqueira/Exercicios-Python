n1 = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = n1 + (12 - 1) * razao
for i in range(n1, decimo, razao):
    print(i, end='-> ')
print('Fim')
