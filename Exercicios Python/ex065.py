soma = cont = media = maior = menor = 0
resposta = ''
while resposta != 'N':
    n = int(input('Digite um número : '))
    resposta = input('Quer continuar ? [S/N] ').strip().upper()
    cont += 1
    soma = soma + n
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
media = soma/cont

print(f'Você digitou {cont} números e a média foi {media}')
print(f'O maior valor foi {maior} e o menor foi {menor}')

