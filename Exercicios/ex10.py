din = float(input('Quanto você tem na carteira? '))
compra = din / 5.22
compra2 = din / 5.59
print('Você pode comprar com R${:.2f} reais, uma quantia de ${:.2f} Dolar' .format(din, compra))
print('Você pode comprar com R${:.2f} reais, uma quantia de ${:.2f} Euro' .format(din, compra2))