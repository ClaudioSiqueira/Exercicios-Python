cont = 0
maior = menor = 0
maior_nome = []
menor_nome = []
while True:
    name = input('Nome: ')
    weight = float(input('Peso : '))
    if cont == 0:
        menor = maior = weight
    elif cont >= 1:
        if weight > maior:
            maior = weight

            maior_nome.append(name)
        if weight < menor:
            menor = weight
            menor_nome.clear()
            menor_nome.append(name)

    answer = input('Quer continuar ? [S/N] ').upper()
    cont += 1
    if answer == 'N':
        break

print('Ao todo, você cadastrou {} pessoas'.format(cont))
print('O maior peso foi de {}. Peso de {}'.format(maior, maior_nome))
print('O menor peso foi de {}. Peso de {}'.format(menor, menor_nome))

