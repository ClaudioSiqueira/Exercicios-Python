from math import radians,sin,cos,tan
angulo = float(input('Digite o ângulo: '))
sen = sin(radians(angulo))
cos = cos(radians(angulo))
tan = tan(radians(angulo))
print('Seno de {} = {:.2f} '.format(angulo, sen))
print('Cosseno de {} = {:.2f} '.format(angulo, cos))
print('Tangente de {} = {:.2f} '.format(angulo, tan))
