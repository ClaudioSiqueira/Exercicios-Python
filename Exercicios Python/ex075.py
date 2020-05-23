num = (int(input('Digite um valor: ')),
       int(input('Digite outro valor: ')),
       int(input('Digite outro valor: ')),
       int(input('Digite outro valor: ')))
print('O número 9 apareceu {} vezes'.format(num.count(9)))
if 3 in num:
    print('O valor 3 apareceu na posição {}'.format(num.index(3) + 1))
else:
    print('O valor 3 não foi digitado')
print('Os valores pares digitados foram:')
for i in num:
    if i % 2 == 0:
        print(i, end=' ')

