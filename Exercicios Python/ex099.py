def maior(* num):
    cont = maior = 0
    for valor in num:
        if cont == 0:
            maior = valor
        if valor > maior:
            maior = valor
        cont += 1
    print(maior)


maior(-1, -2)
