salario = float(input('Qual é o salário do funcionário ? '))
if salario > 1250:
    total = (salario * 0.1) + salario
else:
    total = (salario * 0.15) + salario
print('O valor final é de {} reais '.format(total))

#CALCULA O AUMENTO DO FUNCIONARIO, VARIA DE ACORDO COM O SALARIO ATUAL
