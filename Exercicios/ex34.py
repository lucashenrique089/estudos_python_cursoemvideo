nome = str(input('Digite seu nome:'))
salario = float(input('Qual o sálario do funcionário?'))

if salario >=1250.00:
    novo = salario + (salario*10/100)
else:
    novo = salario + (salario * 15 / 100)

print(' O funcionário {} tem o sálario de R${:.2f} e seu aumento em porcentagem foi para {:.2f}' .format(nome, salario, novo))
