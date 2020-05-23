print('-'*20)
print('LOJA SUPER BARATÃO')
print('-'*20)
precototal = 0
cont_1000 = 0
barato = 999999999999999999999999999999999999999999999999999999999999999999999999999
maisbarato = ''

while True:
    produto = input('Nome do produto: ')
    preco = float(input('Preço: R$'))
    if preco > 1000:
        cont_1000 += 1
    if preco < barato:
        barato = preco
        maisbarato = produto
    resposta = input('Quer continuar ? [S/N]').strip().upper()
    while resposta != 'N' and resposta != 'S':
        resposta = input('Quer continuar ? [S/N]').strip().upper()
    precototal += preco
    if resposta == 'N':
        break

print('O total da compra foi R${:.2f}'.format(precototal))
print('Temos {} produtos custando mais de R$1000.00 '.format(cont_1000))
print('O produto mais barato foi {} que custa R${}'.format(maisbarato, barato))
