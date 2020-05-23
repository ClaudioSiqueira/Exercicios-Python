numeros = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in numeros:
        numeros.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado, não vou adicionar...')
    resposta = input('Quer continuar ? [S/N] ')
    if resposta in 'Nn':
        break
numeros.sort()
print(numeros)










































'''
lista =[]
while True:
    n = int(input('Digite um valor :'))
    if n not in lista:
        lista.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado ! Não vou adicionar... ')
    resposta = input(('Quer continuar ? [S/N] ')).strip().upper()
    while resposta != 'S' and resposta != 'N':
        resposta = input(('Quer continuar ? [S/N] ')).strip().upper()
    if resposta == 'N':
        break
print('Você digitou os valores ',end ='')
print(sorted(lista))
'''