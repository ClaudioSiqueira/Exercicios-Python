n = int(input('Digite um número inteiro: '))
print('''Escolha uma nas bases para conversão
[1] Converter para BINÁRIO
[2] Converter para OCTAL
[3] Converter para HEXADECIMAL''')
opcao = int(input('Qual é sua opção ? '))
print('Sua opção: {}'.format(opcao))
if opcao == 1:
    print('{} convertido em BINÁRIO é igual a {}'.format(n,bin(n)[2:]))
elif opcao == 2:
    print(' {} convertido em OCTAL é igual a {}'.format(n,oct(n)[2:]))
elif opcao == 3:
    print('{} convertido em HEXADECIMAL é igual a {}'.format(n,hex(n)[2:]))
else:
    print('Opção invalida, tente novamente')










