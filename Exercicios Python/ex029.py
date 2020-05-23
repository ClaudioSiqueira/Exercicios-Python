from time import sleep
vel = float(input('Qual é a velocidade atual do carro ? '))
limite = 80
multa = (vel-80) * 7
if vel < limite:
    print('Você está dentro do limite de velocidade, continue assim !')
else:
    print('Você está acima do limite de velocidade ! Recebeu uma multa {} reais !'.format(multa))
sleep(1)
print('Tenha um bom dia ')

