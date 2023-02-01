import math
from time import sleep
print('-=-' * 15)
print('PROCESSANDO OS TRIÂNGULOS')
sleep(1.5)

r1 = float(input('Digite um valor:'))
r2 = float(input('Digite o segundo valor:'))
r3 = float(input('Digite o terceiro valor:'))

if r1 < r3 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os seguimentos acima se formam')
else:
    print('Não consigo Formar...')


