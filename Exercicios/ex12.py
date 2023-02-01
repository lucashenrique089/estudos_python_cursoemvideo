prod = float(input('Qual o valor do produto R$: '))
desconto = prod - (prod*15/100)
print('O valor do produto com desconto é de R${:.2f}' .format(desconto))