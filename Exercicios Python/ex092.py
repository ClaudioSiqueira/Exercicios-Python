from datetime import datetime
pessoa = {}
pessoa['Nome'] = input('Nome: ')
nascimento= int(input('Ano de nascimento: '))
pessoa['Idade'] = datetime.now().year - nascimento
pessoa['Ctps'] = int(input('Carteira de Trabalho: (0 não tem) '))
if pessoa['Ctps'] != 0:
    pessoa['Contratação'] = int(input('Ano de contratação: '))
    pessoa['Salário'] = float(input('Salário: R$'))
    pessoa['Aposentadoria'] = pessoa['Contratação'] + 35 - datetime.now().year + pessoa['Idade']
print('-=' * 30)

for k, v in pessoa.items():
    print('  -{} tem o valor {}'.format(k, v))

