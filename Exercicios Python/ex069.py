cont_idade = 0
cont_homem = 0
cont_mulher20 = 0
while True:
    print('-'*20)
    print('CADASTRE UMA PESSOA')
    print('-'*20)
    idade = int(input('Idade: '))
    sexo = input('Sexo: [M/F] ').strip().upper()
    while sexo != 'M' and sexo != 'F':
        sexo = input('Sexo: [M/F] ').strip().upper()
    print('-'*20)
    if idade >= 18:
        cont_idade += 1
    if sexo == 'M':
        cont_homem += 1
    if sexo == 'F' and idade < 20:
        cont_mulher20 += 1
    escolha = input('Quer continuar ? ').strip().upper()
    if escolha == 'N' or escolha == 'NÃO' or escolha == 'NAO':
        break
print('Total de pessoas com mais de 18 anos : {}'.format(cont_idade))
print('Ao todo temos {} homens cadastrados'.format(cont_homem))
print('E temos {} mulheres com menos de 20 anos'.format(cont_mulher20))