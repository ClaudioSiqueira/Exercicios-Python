from random import randint
tupla = (randint(0, 10),randint(0, 10),randint(0, 10),randint(0, 10),randint(0, 10))
x = sorted(tupla)
for i in tupla:
    print(f'{i}', end =' ')
print('')
print('O maior valor sorteado foi {}'.format(x[4]))
print('O menor valor sorteado foi {}'.format(x[0]))