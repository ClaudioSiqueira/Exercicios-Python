km = int(input('Qual a distância da viagem ? '))
if km < 200:
    preco = km * 0.5
else:
    preco = km * 0.45
print('O preço da passagem é de {} reais'.format(preco))

# A EMPRESA OFERECE DESCONTO COM VIAGEM > 200 KM