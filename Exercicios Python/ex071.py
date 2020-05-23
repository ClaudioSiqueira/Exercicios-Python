valor = int(input('Valor da compra: '))
n1 = valor // 100
resto1 = valor % 100
n2 = resto1 // 50
resto2 = resto1 %50
n3 = resto2// 20
resto3 = resto2 % 20
n4 = resto3// 10
resto4 = resto3 % 10
n5 = resto4 // 5
resto5 = resto4 % 5
n6 = resto5 // 2
resto6 = resto5 % 2
n7 = resto6 // 1
resto7 = resto6 % 1

print('Notas de 100: {}'.format(n1))
print('Notas de 50: {}'.format(n2))
print('Notas de 20: {} '.format(n3))
print('Notas de 10: {}'.format(n4))
print('Notas de 5: {}'.format(n5))
print('Notas de 2: {}'.format(n6))
print('Moedas de 1: {}'.format(n7))
