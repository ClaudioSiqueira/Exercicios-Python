def escreva(msg):
    tam = len(msg) + 4
    print('~' * tam)
    print('  {}'.format(msg))
    print('~' * tam)


escreva('Python is really good')
