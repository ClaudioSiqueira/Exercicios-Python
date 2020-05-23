preço = float(input('Qual é o preço do produto ? R$'))
desconto = float(input('Qual é a porcentagem do desconto ?'))
calculo = preço * desconto/100
final = preço - calculo


print('O produto que custava {} reais, fica por {} reias com o desconto de {}%'.format(preço, final, desconto))


