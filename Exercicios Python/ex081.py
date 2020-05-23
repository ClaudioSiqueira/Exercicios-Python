lista = []
while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    resposta = input('Quer continuar ? [S/N] ')
    if resposta in 'Nn':
        break
print('Você digitou {} elementos'.format(len(lista)))
lista.sort(reverse=True)
print('Os valores em ordem decrescente são {}'.format(lista))
if 5 in lista:
    print('O valor 5 faz parte da lista !')
else:
    print('O valor 5 não faz parte da lista !')






















'''valores = []
while True:
    valores.append(input('Digite um valor: '))
    resposta = input('Quer continuar ? [S/N]').strip().upper()
    if resposta == 'N':
        break
print('-'*30)
print('Você digitou {} elementos'.format(len(valores)))
valores.sort(reverse=True)
print('Os valores em ordem decrescente são {}'.format(valores))
if 5 in valores:
    print('O valor 5 faz parte da lista')
else:
    print('O valor 5 não foi encontrado na lista')'''


