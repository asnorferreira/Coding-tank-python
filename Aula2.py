a = int(input('número de a: '))
b = int(input('número de b: '))
c = int(input('número de c: '))
print(type(a))
print(type(b))
print(type(c))
print(a, b, c)

x1 = (int(input('número de x1: ')))
y1 = (int(input('número de y1: ')))
x2 = (int(input('número de x2: ')))
y2 = (int(input('número de y2: ')))

op = (a + b) / 2
print(op)
from math import sqrt
op2 = (- b + sqrt((b**2) - 4 * a * c)) / 2 * a
print(op2)

""" exe2
tamanho_de_calca = 42
TAMANHO = 45
print(type(tamanho_de_calca))
print(type(TAMANHO))
print('O tamanho é {0} e o segundo é {1}'.format(tamanho_de_calca, TAMANHO))
"""
"""
print('Início do programa')
print('')
fixo = 500.00
vendas = float(input('Digite o valor das vendas: '))
comissao = 6 /100
fat = fixo + vendas * comissao
print('faturamento do mês = {0:.2f}'.format(fat))
print('')
print('Fim do programa')
"""
""" exe1
x = 0.0
y = 18
z = x + y
print('O valor total foi {0:.2f}'.format(z))
"""