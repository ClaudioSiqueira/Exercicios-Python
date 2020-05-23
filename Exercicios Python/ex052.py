n = int(input('Digite um número: '))
if n == 1 or n == 0:
    print('Não é primo')
elif n == 2:
    print('É primo')
else:
    for i in range(2, n + 1):
        if n % i == 0:
            print('Não é primo')
            break
        else:
            print('É primo')
            break









































'''n = int(input('Digite um número: '))
if n == 0 or n == 1:
    print('Não é primo')
elif n == 2:
    print('É primo')
for i in range(2, n):

    if n % i == 0:
        print('Não é primo')
        break
    if i + 1 == n:
        print('É primo')'''
