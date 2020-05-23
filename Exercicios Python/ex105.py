def notas(*n, sit=False):
    """

    :param n: Uma ou mais notas do aluno
    :param sit: Valor boleano  que informa ou n a situação
    :return: Retorna o resultado
    """
    r = {}
    r['Total'] = len(n)
    r['Maior'] = max(n)
    r['Menor'] = min(n)
    r['Média'] = sum(n)/len(n)

    if sit:
        if r['Média'] >= 7:
            r['Situação'] = 'Boa'
        elif r['Média'] >= 5:
            r['Situação'] = 'Razoável'
        else:
            r['Situação'] = 'Ruim'

    return r


resp = notas(5.5, 2.5, 9, 8.5, sit=True)
for k, v in resp.items():
    print(f'{k} é {v}')
