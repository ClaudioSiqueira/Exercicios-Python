from ex109  import moeda
preco = float(input('Digite um preço: R$'))
print('A metade de {} é {}'.format(moeda.moeda(preco), moeda.moeda(moeda.metade(preco))))
print('O dobro de {} é {}'.format(preco, moeda.moeda(moeda.dobro(preco))))
print('Aumentando 10% temos {}'.format(moeda.moeda(moeda.aumentar(preco, 10))))
