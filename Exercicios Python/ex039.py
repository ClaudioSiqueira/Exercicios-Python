from datetime import date
ano = int(input('Ano de nascimento: '))
idade = date.today().year - ano
print('Quem nasceu em {} tem {} anos em {}'.format(ano,idade,date.today().year))
if idade == 18:
    print('Você deve se alistar IMEDIATAMENTE')
elif idade < 18:
    falta = 18 - idade
    print('Ainda falta(m) {} ano(s) para o alistamento'.format(falta))
    print('Seu alistamento será em {}'.format(falta + date.today().year))
elif idade > 18:
    falta = idade - 18
    print('Você já deveria ter se alistado há {} ano(s) em {}'.format(falta, date.today().year - falta))








