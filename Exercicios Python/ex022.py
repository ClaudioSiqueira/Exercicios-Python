nome = str(input('Digite o seu nome completo: ')).strip()
print('O seu nome em maiúsculas é {}'.format(nome.upper()))
print('o seu nome em minúsculas é {}'.format(nome.lower()))
print('Seu nome tem {} letras ao todo'.format(len(nome) - nome.count(' ')))
separa = nome.split()
print('O seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))









