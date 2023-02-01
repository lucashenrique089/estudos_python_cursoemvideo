nome = input('Digite seu nome:')
idade = input('Digite sua idade:')
print('Boa Tarde, {}{}{} é um prazer em conhecer você! A Sua idade é: {}' .format('\033[1;36m', nome, '\033[m', idade))

#quando colocamos o {} dentro de uma função, é para no final após as aspas ter o .format e é em ordem de cada varivale que será colocada e atribuida.