pessoa = {}
lista = []
total_idade = 0
while True:
    pessoa['Nome'] = str(input('Nome: '))
    pessoa['Sexo'] = str(input('Sexo [M/F] '))
    while pessoa['Sexo'] not in 'MmFf':
        pessoa['Sexo'] = str(input('ERRO ! Responda apenas com M ou F. '))
    pessoa['Idade'] = int(input('Idade: '))
    total_idade += pessoa['Idade']
    lista.append(pessoa.copy())
    resposta = str(input('Quer continuar ? [S/N] '))
    while resposta not in 'NnSs':
        resposta = str(input('ERRO ! Responda apenas S ou N. '))
    if resposta in 'Nn':
        break
print('A) Ao todo temos {} pessoas cadastradas.'.format(len(lista)))
print('B) A média de idade é de {:.2f} anos'.format(total_idade/len(lista)))
print('C) As mulheres cadastradas foram ', end='')
for p in lista:
    if p['Sexo'] in 'Ff':
        print('{}'.format(p['Nome']), end=' ')
print(' ')
print('D) Lista de pessoas que estão acima da média: ')
for p in lista:
    if p['Idade'] > total_idade/len(lista):
        print('   Nome  = {}; Sexo = {}; Idade = {};'.format(p['Nome'], p['Sexo'], p['Idade']))
print('<<ENCERRADO>>')