from time import sleep
primeiro = int(input('Primeiro valor: '))
segundo = int(input('Segundo valor: '))
opcao = 0
while opcao != 5:
    print('''    [1] Somar 
    [2] Multiplicar
    [3] Maior valor
    [4] Novos números 
    [5] Sair do programa
=-=-=-=-=-=-=-=-=-=-=-=-=-=''')
    opcao = int(input('Qual é a sua opção ? '))
    if opcao == 1:
        soma = primeiro + segundo
        print('A soma entre {} e {} é {}'.format(primeiro, segundo, soma))
        sleep(1)
    elif opcao == 2:
        multiplicacao = primeiro * segundo
        print('O resultado de {} x {} é {}'.format(primeiro, segundo, multiplicacao))
        sleep(1)
    elif opcao == 3:
        if primeiro > segundo:
            maior = primeiro
        else:
            maior = segundo
            print('Entre {} e {} o maior valor é {}'.format(primeiro, segundo, maior))
    elif opcao == 4:
        print('Informe of números novamente')
        primeiro = int(input('Primeiro valor: '))
        segundo = int(input('Segundo valor: '))

print('Fim')



