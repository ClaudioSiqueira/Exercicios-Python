lista = []
pares = []
impar = []
while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    resposta = input('Quer continuar ? [S/N] ')
    if resposta in 'Nn':
        break

for i, v in enumerate(lista):
    if v % 2 == 0:
        pares.append(v)
    if v % 2 == 1:
        impar.append(v)
lista.sort()
pares.sort()
impar.sort()
print('A lista completa é {}'.format(lista))
print('A lista de pares é {}'.format(pares))
print('A lista de ímpares é {}'.format(impar))





































'''lista = []
pares = []
impar = []
while True:
    lista.append(int(input('Digite um número: ')))
    resposta = input('Quer continuar ? [S/N] ')
    if resposta in 'Nn':
        break
for i, v in enumerate(lista):
    if v % 2 == 0:
        pares.append(v)
    else:
        impar.append(v)
print('A lista completa é {}'.format(lista))
print('A lista de pares é {}'.format(pares))
print('A lista de ímpares é {}'.format(impar))'''