nome = str(input('Digite seu nome:')).strip()
print('Analisando seu nome...')
v1 = nome.upper()
v2 = nome.lower()
v3 = len(nome) - nome.count(' ')
v4 = nome.split()
v5 = len(v4[0])
print('Seu nome em maiúsculo {}'.format(v1))
print('Seu nome em minusculo {}' .format(v2))
print('Quantas letas tem seu nome: {}' .format(v3))
print('Seu primero nome tem número de letras de {}' .format(v5))
