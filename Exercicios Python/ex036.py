casa = float(input('Qual é o valor da casa ? R$' ))
salario = float(input('Quanto é o salário do comprador ? R$'))
anos = int(input('Quantos anos de financiamento ?'))
financiamento = casa/(anos*12)
prestacao = 0.3*salario
if prestacao > financiamento:
    print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}'.format(casa,anos,financiamento))
    print('Empréstimo pode ser CONCEDIDO !')
else:
    print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de R$ {:.2f}'.format(casa,anos,financiamento))
    print('Empréstimo NEGADO !')



