somaidade = 0
countmulher = 0
maioridadehomem = 0
nomevelho = ''
for i in range(1, 5):
    print('----- {}ª PESSOA -----'.format(i))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo[M/F]:')).strip()
    somaidade = somaidade + idade
    mediaidade = somaidade/3
    if i == 1 and sexo in 'mM':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'mM' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        countmulher = countmulher + 1
print('A média de idade do grupo é de {:.1f} anos'.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {}'.format(maioridadehomem, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(countmulher))
