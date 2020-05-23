def ficha(jogador='<desconhecido>', gols=0):
    print('O jogador {} fez {} gols(s) no campeonato'.format(jogador, gols))


n = str(input('Nome do jogador: '))
g = str(input('Número de gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gols=g)
else:
    ficha(n, g)
