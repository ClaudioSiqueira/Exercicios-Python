def fatorial(num, show=False):
    """
    ->  Calcula o fatorial de um número
    :param num: Número a ser calculado
    :param show: Se quer mostrar a conta ou não
    :return: Retorna o resultado do fatorial
    """
    fat = 1
    for i in range(num, 0, -1):
        if show:
            print(f'{i} ', end='')
            if i > 1:
                print('x ', end='')
            else:
                print('= ', end='')
        fat *= i
    return fat


print('-' * 30)
print(fatorial(5))
help(fatorial)
