from random import randint


def sorteio(lista):
    for i in range(0, 5):
        x = randint(1, 10)
        lista.append(x)
    print(numeros)


def soma_par(lista):
    soma = 0
    for i in lista:
        if i % 2 == 0:
            soma += i
    print(soma)


numeros = []
sorteio(numeros)
soma_par(numeros)
