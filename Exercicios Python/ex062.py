'''primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
for i in range(primeiro,(primeiro + (10*razao)),razao):
    print(i, end = '->')
print('fim')'''



print('Gerador de PA')
print('-='*10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
cont = 1
while cont <= 10:
    print('{} ->'.format(termo), end = '')
    termo += razao
    cont += 1
print('FIM')
