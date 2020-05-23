from time import sleep
from random import randint
computador = randint(0, 10)
soma = 0
print('''Sou seu computador ....
Acabei de pensar em um número entre 0 e 10.
Será que você consegue adivinhar qual foi ?''')
sleep(2)
palpite = int(input('Qual é o seu palpite ? '))
while palpite != computador:
    soma = soma + 1
    if palpite > computador:
        palpite = int(input(('''Menos... Tente mais uma vez. 
Qual é o seu palpite ? ''')))
    elif palpite < computador:
        palpite = int(input(('''Mais... tente mais uma vez 
Qual é o seu palpite ? ''')))
print('\033[32mAcertou com {} tentativas. Parabéns !'.format(soma + 1))

