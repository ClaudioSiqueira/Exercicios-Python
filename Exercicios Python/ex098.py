from time import sleep


def contagem(inicio, fim, passo):
    print('-=' * 20)
    print('Contagem de {} até {} de {} em {}'.format(inicio, fim, passo, passo))

    if passo == 0:
        passo = 1
    if passo < 0:
        passo *= (-1)
    if inicio < fim:
        cont = inicio
        while cont <= fim:
            print(f'{cont} ', end='', flush=True)
            sleep(0.25)
            cont += passo
        print('Fim !')
    else:
        cont = inicio
        while cont >= fim:
            print(f'{cont} ', end='', flush=True)
            sleep(0.25)
            cont -= passo
        print('Fim !')
    print('')


contagem(0, 100, 10)
contagem(100, 0, 10)

print('Agora é sua vez de personalizar a contagem')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contagem(inicio, fim, passo)
