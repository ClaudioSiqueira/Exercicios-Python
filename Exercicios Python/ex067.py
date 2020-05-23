x = int(input('Quer ver a tabuada de qual valor ? '))
while True:
    for i in range(1,11):
        print(f'{i}x{x} = {i*x}')
    x = int(input('Quer ver a tabuada de qual valor ? '))

    if x < 0:
        break

#AO DIGITAR UM VALOR NEGATIVO O PROGRAMA PARA