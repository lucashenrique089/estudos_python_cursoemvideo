n1 = int(input('Digite um número: '))
dobro = n1 * 2
triplo = n1 * 3
raiz = n1 ** (1/2) #raiz quadrada. Ou usar pow (n, (1/2))
print('O número {}, tem o drobro de {} e o triplo de {},\n e sua raiz quadrada é {:.2f}' .format(n1, dobro, triplo, raiz), end='')