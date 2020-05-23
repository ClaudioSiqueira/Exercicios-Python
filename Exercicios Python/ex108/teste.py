import moeda
preco = float(input('Digite um preço: R$'))
print('A metade de {} é {}'.format(moeda.formatacao(preco), moeda.formatacao(moeda.metade(preco))))
print('O dobro de {} é {}'.format(preco, moeda.formatacao(moeda.dobro(preco))))
print('Aumentando 10% temos {}'.format(moeda.formatacao(moeda.aumentar(preco, 10))))
