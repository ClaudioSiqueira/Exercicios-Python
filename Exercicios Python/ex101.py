from datetime import date

def votacao(ano):
    idade = date.today().year - ano
    if idade <= 15:
        voto = 'Com {} anos o voto é NEGADO'.format(idade)
    elif idade == 16 or idade == 17 or idade > 60:
        voto = 'Com {} anos o voto é OPCIONAL'.format(idade)
    elif 18 <= idade <= 60:
        voto = 'Com {} anos o voto é OBRIGATÓRIO'.format(idade)
    return voto


print('-' * 30)
ano = int(input('Em que ano você nasceu ? '))
print(votacao(ano))
