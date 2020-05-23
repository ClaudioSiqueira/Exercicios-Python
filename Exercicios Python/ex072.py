cont = ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez',
        'onze','doze','treze','catorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')
while True:
    n = int(input('Digite um número entre 0 e 20: '))
    while n > 21 or n < 0:
        n = int(input('Digite um número entre 0 e 20: '))
    print('Você digitou o número {}'.format(cont[n]))
    resposta = input('Você quer continuar ? [S/N] ').strip().upper()
    while resposta != 'S' and resposta != 'N':
        resposta = input('Você quer continuar ? [S/N] ').strip().upper()
    if resposta == 'N':
        break








