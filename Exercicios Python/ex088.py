from random import randint
from time import sleep
lista = []
jogos = []
print('-' * 30)
print('    SIMULADOR MEGA SENA')
print('-' * 30)
quant = int(input('Digite a quantidade de jogos que você quer sortear: '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        n = randint(1, 60)
        if n not in lista:
            lista.append(n)
            cont += 1
        if cont == 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1

print('SORTEANDO JOGOS')
for i, l in enumerate(jogos):
    print('Jogo {}: {} '.format(i + 1, l))
    sleep(1)
print('BOA SORTE')
print(jogos)
