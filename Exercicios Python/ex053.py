#
frase = str(input('Digite uma frase: ')).upper()
if frase.replace(' ', '') == frase[::-1].replace(' ', ''):
    print(frase.replace(' ', ''))
    print('É um palíndromo')
else:
    print(frase, 'não é palindromo')
#