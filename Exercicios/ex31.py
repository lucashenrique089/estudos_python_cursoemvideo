nome = str(input('Qual o seu nome?'))
local = str(input('Para onde você esta indo?'))
distancia = float(input('Digite a distância da viagem:'))
pass1 = distancia * 0.50 #até 200
pass2 = distancia * 0.45 #acima de 200

if distancia <= 200:
    print('O cliente {} que vai para {} para pela viagem R${:.2f}' .format(nome, local, pass1))
else:
    print('O cliente {} fará uma viagem para {} que é longa e pagará R${:.2f}'.format(nome, local, pass2))
