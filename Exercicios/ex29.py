#carro e multa

nome = str(input('Digite seu nome:')).upper()
carro_velocidade = float(input('Digite a velocidade que o corredor atingiu:'))
multa = (carro_velocidade - 80) * 7

if carro_velocidade > 80:
    print('VOCÊ {} PASSOU DOS LIMITES NESTA RUA, VOCÊ NÃO É O TORETO A MULTA FOI DE R${:.2f}' .format(nome, multa))
else:
    print('OK VOCÊ SE SAFOU...')