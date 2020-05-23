print('-=-'*20)
preco = float(input('Preço das compras: R$'))
opcao = int(input('''FORMAS DE PAGAMENTO:
[1] à vista dinheiro/cheque (10% de desconto)
[2] à vista no cartão (5% de desconto)
[3] 2x no cartão (Preço normal parcelado)
[4] 3x ou mais no cartão (20% de juros) '''))
if opcao == 1:
    valor = preco - (preco * 0.1)
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final '.format(preco, valor))
elif opcao == 2:
    valor = preco - (preco * 0.05)
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(preco, valor))
elif opcao == 3:
    valor = preco/2
    print('Sua compra de R${:.2f} vai custar 2x de R${:.2f} no final'.format(preco, valor))
elif opcao == 4:
    parcela = int(input('Quantas parcelas ?'))
    valor = (preco*1.2/parcela)
    final = preco + (preco*0.2)
    print('Sua compra será parcelada em {}x de R${:.2f} COM 20% DE JUROS'.format(parcela, valor))
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(preco, final))
else:
    print('\033[31mOPÇÃO INVALIDA, TENTE NOVAMENTE')
print('-=-' * 20)