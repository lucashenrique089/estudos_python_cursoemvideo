frase = str(input('Digite uma frase:')).strip().upper()
print('Quantas vezes aparece o A {}' .format(frase.count('A')))
print('Em que posição aparece o primeiro A {}' .format(frase.find('A')+1))
print('Em que posição aparece o último A {}' .format(frase.rfind('A')+1)) #rfind pega os valores a direita, diferente do find que é a esquerda