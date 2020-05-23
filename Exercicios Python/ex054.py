from datetime import date
hoje = date.today().year
count1 = 0
count2 = 0
for i in range(1, 8):
    ano = int(input('Em que ano a {} pessoa nasceu ? '.format(i)))
    idade = hoje - ano
    if idade < 18:
        count1 = count1 + 1
    else:
        count2 = count2 + 1
print('')
print('Ao todos tivemos {} pessoas maiores de idade'.format(count2))
print('E também tivemos {} pessoas menores de idade '.format(count1))

