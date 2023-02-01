nome = str(input('O nome do aluno: '))
nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2) / 2
print ('A nota final do aluno {} é de {:.1f}' .format(nome, media))