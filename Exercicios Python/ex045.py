from random import randint
from time import sleep
print('--'*20)
jogador = (int(input('''Suas opções :
[0] PEDRA
[1] PAPEL 
[2] TESOURA 
Qual é sua jogada ? ''')))
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
print('-='*20)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-='*20)
if computador == 0:
    if jogador == 0:
        print('EMPATE !')
    elif jogador == 1:
        print('JOGADOR VENCE !')
    elif jogador == 2:
        print('COMPUTADOR VENCE !')
    else:
        print('Jogada inválida')
if computador == 1:
    if jogador == 0:
        print('COMPUTADOR VENCE !')
    elif jogador == 1:
        print('EMPATE !')
    elif jogador == 2:
        print('JOGADOR VENCE !')
    else:
        print('Jogada inválida')
if computador == 2:
    if jogador == 0:
        print('JOGADOR VENCE !')
    elif jogador == 1:
        print('COMPUTADOR VENCE !')
    elif jogador == 2:
        print('EMPATE !')
    else:
        print('Jogada inválida')