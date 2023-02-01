import random
from time import sleep
print('-=-' * 10)
n1 = int(input('Digite um núemro:')) # Eu digitei um número
num = random.randint(0, 5) # número aleátorio da máquina
print('-=-' * 10)
print('PROCESSANDO')
sleep(2)
if n1 == num:
    print('VOCÊ ACERTOU O NÚMERO')
else:
    print('VOCÊ ERROU O MEU NÚMERO FOI {} ... TENTE MAIS UMA VEZ' .format(num))
