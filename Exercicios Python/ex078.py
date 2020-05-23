lista = []
maior = menor = 0
for c in range(0, 5):
    lista.append(int(input(f'Digite um valor para a posição {c}: ')))
    if c == 0:
        maior = menor = lista[c]
    else:
        if lista[c] > maior:
            maior = lista[c]
        if lista[c] < menor:
            menor = lista[c]
print('Você digitou os valores ', lista)
print(f'O maior valor digitado foi {maior} nas posições ', end='')
for i, v in enumerate(lista):
    if v == maior:
        print(f'{i}...', end=' ')
print(' ')
print(f'O menor valor digitado foi {menor} nas posições ', end='')
for j, va in enumerate(lista):
    if va == menor:
        print(f'{j}...', end=' ' )
















































'''listanum = []
maior = 0
menor = 0
for c in range(0, 5):
    listanum.append(input(f'Digite um valor para a posição {c}: '))
    if c == 0:
        maior = menor = listanum[c]
    else:
        if listanum[c] > maior:
            maior = listanum[c]
        if listanum[c] < menor:
            menor = listanum[c]
print(f'O maior valor digitado foi {maior}')
for i, v in enumerate(listanum):
    if v == maior:
        print(f'{i}...', end='')
print()
print(f'O menor valor digitado foi {menor}')
for i, v in enumerate(listanum):
    if v == menor:
        print(f'{i}...', end ='')
print()'''