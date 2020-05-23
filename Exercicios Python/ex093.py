jogador = {}
lista = []
total = 0
jogador['Nome'] = input('Nome do jogador: ')
quantidade = int(input('Quantas partidas {} jogou ? '.format(jogador['Nome'])))
for i in range(0, quantidade):
    gol_quantidade = int(input('Quantos gols na partida {} ? '.format(i + 1)))
    total += gol_quantidade
    lista.append(gol_quantidade)
jogador['Gols'] = lista
jogador['Total'] = total
print('-=' * 30)
print(jogador)
print('-=' * 30)
for k, v in jogador.items():
    print('O campo {} tem valor {}'.format(k, v))
print('-=' * 30)
print('O jogador {} jogor {} partidas'.format(jogador['Nome'], quantidade))
for i, valor in enumerate(jogador['Gols']):
    print('  => Na partida {} , fez {} gols'.format(i + 1, valor))

print('Foi um total de {} gols'.format(total))
