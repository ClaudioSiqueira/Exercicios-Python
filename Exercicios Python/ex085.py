lista = [[], []]
for i in range(1, 8):
    valor = int(input('Digite um valor: '))
    if valor % 2 == 0:
        lista[0].append(valor)
    else:
        lista[1].append(valor)
lista[0].sort()
lista[1].sort()
print('Os valores pares digitados foram: {}'.format(lista[0]))
print('Os valores ímpares digitados foram: {}'.format(lista[1]))



























'''lista = []
par = []
impar = []
for i in range(1, 8):
    n = int(input('Digite o {}° número: '.format(i)))
    lista.append(n)
for j, v in enumerate(lista):
    if v % 2 == 0:
        par.append(v)
    else:
        impar.append(v)
par.sort()
impar.sort()
print('Os valoes pares digitados foram: ', par)
print('Os valores ímpares digitados foram: ', impar)'''