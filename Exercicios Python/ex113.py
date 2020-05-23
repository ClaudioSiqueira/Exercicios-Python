def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('Esse não é um numero valido')
        except KeyboardInterrupt:
            print('Programa encerrado')
        else:
            return n


num = leiaInt('Digite um número inteiro: ')