print('Analizador de triângulos ')
s1 = float(input('Quanto mede o primeiro seguimento ?'))
s2 = float(input('Quanto mede o segundo seguimento ? '))
s3 = float(input('Quanto mede o terceiro seguimeto ?'))
if s1 + s2 > s3 and s1 + s3 > s2 and s2 + s3 > s1:
    print('Os seguimentos acima PODEM formar um triângulo ', end = '')
    if s1 == s2 == s3:
        print('EQUILÁTERO')
    if s1 != s2 != s3 != s1:
        print('ESCALENO')
    else:
        print('ISÓCELES')
else:
    print('Os seguimentos acima NÃO PODEM formar um triângulo')