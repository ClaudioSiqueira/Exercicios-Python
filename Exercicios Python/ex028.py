from random import randint
from time import sleep
computador = randint(1, 5)
print('\033[34m-==-\033[m'*17)
print('Vamos jogar um jogo, tente adivinhar o número que estou pensando !')
sleep(1)
jogador = int(input('Chute um valor de 1 até 5: '))
print('PROCESSANDO...')
sleep(1)

if jogador == computador:
    print('\033[1;32mPARABÉNS, VOCÊ ACERTOU!!\033[m Eu realmente esta pensando no número {} !'.format(computador))
else:
    print('\033[1;31mERROUUUU !!\033[m Eu estava pensando no número {} e não no número {}'.format(computador,jogador))

print('\033[34m-==-'*17)