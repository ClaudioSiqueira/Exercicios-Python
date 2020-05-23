peso = float(input('Qual é seu peso ? (KG)'))
altura = float(input('Qual é a sua altura ? (m)'))
imc = peso/(altura**2)
print('IMC = {:.2f}'.format(imc))
if imc < 18.5:
    print('ABAIXO DO PESO')
elif imc < 25 and imc >= 18.5:
    print('PESO IDEAL')
elif imc <30 and imc >= 25:
    print('SOBREPESO')
elif imc <40 and imc >= 30:
    print('OBESIDADE')
elif imc >= 40:
    print('OBESIDADE MÓRBITA')

