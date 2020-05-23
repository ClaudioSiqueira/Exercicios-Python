n = 0
cont = 0
soma = 0
while n!= 999:
    n = int(input('Digite um número (999 para parar): '))
    cont = cont + 1
    soma = soma + n
print(f'Você digitou {cont-1} números e a soma entre eles é {soma-999}')
