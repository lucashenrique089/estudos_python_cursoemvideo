#todo número par que é dividido por 2 é igual a zero e os ímpares é 1#

num = int(input('Digite um número: '))
resultado = num % 2
if resultado == 0:
    print('NUMÉRO PAR')
else:
    print('NÚMERO ÍMPAR')
