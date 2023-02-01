import random

pes01 = str(input('Digite o nome:'))
pes02 = str(input('Digite o nome:'))
pes03 = str(input('Digite o nome:'))
pes04 = str(input('Digite o nome:'))
lista = [pes01, pes02, pes03, pes04]
random.shuffle(lista)
print('A lista será sorteada!!!')
print(lista)


