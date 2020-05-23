from datetime import date
ano = int(input('Ano de nascimento do atleta: '))
idade = date.today().year - ano
print('O atleta tem {} anos'.format(idade))
if idade <= 9:
    print('CLASSIFICAÇÃO: MIRIM')
elif idade <= 14:
    print('CLASSIFICAÇÃO : INFANTIL')
elif idade <= 19:
    print('CLASSIFICAÇÃO : JUNIOR')
elif idade <= 25:
    print('CLASSIFICAÇÃO : SÊNIOR')
elif idade > 25:
    print('CLASSIFICAÇÃO : MASTER')


