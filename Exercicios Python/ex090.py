aluno = {}
aluno['Nome'] = input('Nome: ')
aluno['Media'] = float(input('Média de {}: '.format(aluno['Nome'])))
if aluno['Media'] < 6:
    situacao = 'Reprovado'
elif aluno['Media'] >= 7:
    situacao = 'Aprovado'
else:
    situacao = 'Recuperação'
aluno['Situacao'] = situacao
print('-=' * 30)
for k, v in aluno.items():
    print('   {} é igual a {}'.format(k, v))
