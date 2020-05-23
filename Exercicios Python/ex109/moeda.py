def metade(preco):
    res = preco/2
    return res


def aumentar(preco, taxa, formato=False):
    res = preco + (preco * taxa/100)
    return res if formato is False else aumentar(res)


def diminuir(preco, taxa, formato =False):
    res = preco - (preco * taxa/100)
    return res if formato is False else diminuir(res)


def dobro(preco):
    res = preco * 2
    return res


def moeda(preco = 0, moeda = 'R$'):
    return f'{moeda}{preco:.2f}'.replace('.', ',')
