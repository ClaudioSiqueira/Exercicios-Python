from random import randint
cont = 0
while True:
    print('=-'*15)
    print('VAMOS JOGAR PAR OU ÍMPAR')
    print('=-'*15)
    jogador = int(input('Digite um valor: '))
    while jogador > 11 or jogador < 0:
        jogador = int(input('Digite um valor: '))
    escolha = input('Par ou Ímpar ? [P/I] ').strip().upper()
    while escolha !='P' and escolha != 'I':
        escolha = input('Par ou Ímpar ? [P/I] ').strip().upper()
    computador = randint(1, 10)
    soma = computador + jogador
    if soma % 2 == 0:
        print('Voce jogou {} e o computador jogou {}. Total de {} PAR'.format(jogador, computador, soma))
    elif soma % 2 == 1:
        print('Voce jogou {} e o computador jogou {}. Total de {} ÍMPAR'.format(jogador, computador, soma))
    if soma % 2 == 0 and escolha == 'P':
        print('VOCÊ VENCEU!')
    elif soma % 2 == 1 and escolha =='I':
        print('VOCÊ VENCEU!')

    elif soma % 2 == 0 and escolha == 'I':
        print('VOCÊ PERDEU!')
        break
    elif soma % 2 == 1 and escolha =='P':
        print('VOCÊ PERDEU!')
        break
    cont += 1
print('-='*15)
print('GAME OVER! VOCÊ VENCEU {} VEZES.'.format(cont))
