s = float(input('Qual é o salário do funcionário ? R$'))
aumento = float(input('Quanto foi o aumento dele em porcentagem ?(apenas número)'))
conta = s * aumento/100
final = s + conta
print('O funcionário que ganhava R${:.2f}, com {:.2f}% de aumento, passará a receber R${:.2f}'.format(s, aumento, final))