sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'FM':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()[0]
if sexo == 'M':
    sexo = 'masculino'
elif sexo == 'F':
    sexo = 'feminino'
print('Sexo {} registrado com sucesso'.format(sexo))


