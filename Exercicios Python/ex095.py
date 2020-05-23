jogador = {}
time = []
lista = []
total = 0
while True:
    jogador.clear()
    jogador['Nome'] = input('Nome do jogador: ')
    quantidade = int(input('Quantas partidas {} jogou ? '.format(jogador['Nome'])))
    lista.clear()
    for i in range(0, quantidade):
        gol_quantidade = int(input('Quantos gols na partida {} ? '.format(i + 1)))
        total += gol_quantidade
        lista.append(gol_quantidade)
    jogador['Gols'] = lista
    jogador['Total'] = total
    time.append(jogador.copy())
    resposta = str(input('Quer continuar ? [S/N] '))
    if resposta in 'Nn':
        break
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print('')

print('-=' * 30)
print('O jogador {} jogou {} partidas'.format(jogador['Nome'], quantidade))
for i, valor in enumerate(jogador['Gols']):
    print('  => Na partida {} , fez {} gols'.format(i + 1, valor))

print('Foi um total de {} gols'.format(total))
