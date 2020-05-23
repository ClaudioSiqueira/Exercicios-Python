L = float(input('Largura da parede em metros:'))
Al = float(input('Altura da parede em metros'))
a = L * Al
p = a/2

print('Sua parede tem dimensão de {}x{} e sua área é de {}m²'.format(L, Al, a))
#A CADA 2m² DE PAREDE PRECISA DE 1L DE TINTA
print('Para pintar essa parede você precisará de {}L de tinta'.format(p))


