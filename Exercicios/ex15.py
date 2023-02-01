aluguel = int(input('Quantos dias teve de aluguel do carro: '))
km_rodado = float(input('KM rodados: '))
pago = (aluguel * 60.00) + (km_rodado * 0.15)
print('Os dias alugados foram {} e Km rodados {} o total é: R${:.2f}' .format(aluguel, km_rodado, pago))
