import math
an = float(input('Digite o ângulo que você deseja:'))
seno = math.sin(math.radians(an))
coseno = math.cos(math.radians(an))
tangente = math.tan(math.radians(an))
print('O tamanho do SENO é {:.2f} e do COSSENO {:.2f}! Já a Tangente {:.2f}' .format(seno, coseno,tangente))