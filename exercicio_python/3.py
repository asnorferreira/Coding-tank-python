
"""
nome = str(input('Digite seu nome: '))
idade = int(input('Digite sua idade: '))
print('Seu nome é {} e você possui {} anos!'.format(nome, idade))
if nome == 'Vinicius':
    print('Olá Vinicius!')
elif idade < 18:
    print('Você é de menor!')
elif idade > 100:
    print('Usuário inexistente!')
"""
"""
uso de elif, if e else
print('''
Olá, seja bem-vindo ao nosso hortfruit
Temos 3 tipos de frutas disponíveis:
    maça (1)
    laranja (2)
    banana (3)''')
fruta = int(input('Digite a fruta que deseja: '))
quantidade = int(input('Quantas você deseja? '))
if fruta == 1:
    pagar = quantidade * 2.30
    print('Você comprou {} maçãs. Total à pagar é R$ {}'.format(quantidade, pagar))
elif fruta == 2:
    pagar = quantidade * 3.60
    print('Você comprou {} maçãs. Total à pagar é R$ {}'.format(quantidade, pagar))
elif fruta == 3:
    pagar = quantidade * 1.85
    print('Você comprou {} maçãs. Total à pagar é R$ {}'.format(quantidade, pagar))
else:
    print('Produto não identificado')
"""
""" operadores lógicos
not - não - negação
    V       /       not V
    True            False
    False           True
and - e - conjunção
    V1      V2          v1 and v2
    False   False       False
    True    False       False
    False   True        False
    True    True        True
or - ou - condição
    V1      V2          v1 or v2
    False   False       False
    False   True        True
    True    False       True
    True    True        True
""" 
"""
valor = int(input('Digite o valor a ser trabalhado: '))
if (valor % 2 ==0):
    print('O número {} é par;'.format(valor))
else:
    print('O número {} é impar;'.format(valor))

print('''Produtos disponíveis: 
    boneco malandrinho; 
    spinner pequeno; 
    cubo mágico;''')
print()
produto = str(input('Qual o produto? '))
valor_unit = float(input('Qual o valor do {}? ' .format(produto)))
quantidade_vendida = int(input('Quantos foram vendidos: '))
valor_total = valor_unit * quantidade_vendida
print()
produto2 = str(input('Qual o produto? '))
valor_unit2 = float(input('Qual o valor do {}? ' .format(produto2)))
quantidade_vendida2 = int(input('Quantos foram vendidos: '))
valor_total2 = valor_unit2 * quantidade_vendida2
print()
produto3 = str(input('Qual o produto? '))
valor_unit3 = float(input('Qual o valor do {}? ' .format(produto3)))
quantidade_vendida3 = int(input('Quantos foram vendidos: '))
valor_total3 = valor_unit3 * quantidade_vendida3
print()
print('''
    O primeiro produto custa R$ {}
    O segundo produto custa R$ {}
    O terceiro produto custa R$ {}
''' .format(valor_total, valor_total2, valor_total3))
"""