dia = int(input('Você alugou o carro por quantos dias ? '))
diap = float(input('Quantos reais a empresa cobra por dia ? R$'))
km = float(input('Quantos quilometros você andou com o carro ?'))
kmp = float(input('Quanto a empresa cobra por km rodado ? '))
diaxtaxa = dia * diap #taxa é o valor que a empresa cobra
kmxtaxa = km * kmp
final = diaxtaxa + kmxtaxa

print('O total a pagar é R${:.2f}'.format(final))