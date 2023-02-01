lag = float(input('Qual a largur: '))
alt = float(input('Qual a altura: '))
area = lag * alt
print('A sua parede tem {} largura, e {} altura e a área de dimensão é {}m²' .format(lag, alt, area))
tinta = area / 2
print('Para pintar a parede ira precisar de {} litros de tinta'.format(tinta))