import random
aluno1 = str(input('Nome do aluno: '))
aluno2 = str(input('Nome do aluno:'))
aluno3 = str(input('Nome do aluno:'))
aluno4 = str(input('Nome do aluno:'))
lista = [aluno1, aluno2, aluno3, aluno4] #lista sempre sera com []
sorteio = random.choice(lista)
print('O aluno {}, foi sorteado ganhando um PS4' .format(sorteio))
