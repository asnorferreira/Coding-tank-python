"""
Olá seja bem-vindo!
Este é meu trabalho prático da cadeira: 
Lógica de Programação e Algoritmos
"""
# EXERCÍCIO 1
print('''
Olá sejam bem-vindos ao meu trabalho prático!
Me chamo Asnor Ferreira Quirino Silva.
''')
# Empresa SpaceX
# Dar descontos maiores por unidade
# produto: internet
nome = str(input('Qual seu nome? ')) 
print('''
Olá {} seja bem-vindo a SpaceX, estamos com novas ofertas e promoções.
Nossa empresa trabalha com a distribuição de internet link.
'''.format(nome))
# Definição prática
valor_unit = float(input('Informe o valor do produto (valor sugerido pela internet - R$ 0.15): '))
# Definição do valor da internet por megas
quantidade = int(input('Quantos megas você deseja contratar? '))
valor_total = valor_unit * quantidade
# Valores unitários, quantidades definidos e o valor total calculado 
print()
if quantidade < 200 and quantidade >= 1:
    desconto = valor_total - (valor_total * (0 / 100)) # Cálculo do desconto, incluindo o valor final e inicial
    print('O valor sem desconto é de R${}'. format(valor_total)) # Apresentação do valor sem desconto
    print('O serviço contratado foi de {} megas. Seu desconto foi de 0%, logo o valor total será R${}.'.format(quantidade, desconto))
    # Valor com desconto, número de megas contratados e o percentual de desconto atribuido
elif quantidade >= 200 and quantidade < 1000:
    desconto = valor_total - (valor_total * (5 / 100))
    print('O valor sem desconto é de R${}'. format(valor_total))
    print('O serviço contratado foi de {} megas. Seu desconto foi de 5%, logo o valor total será R${}.'.format(quantidade, desconto))
elif quantidade >= 1000 and quantidade < 2000:
    desconto = valor_total - (valor_total * (10 / 100))
    print('O valor sem desconto é de R${}'. format(valor_total))
    print('O serviço contratado foi de {} megas. Seu desconto foi de 10%, logo o valor total será R${}.'.format(quantidade, desconto))
elif quantidade >= 2000:
    desconto = valor_total - (valor_total * (15 / 100))
    print('O valor sem desconto é de R${}'. format(valor_total))
    print('O serviço contratado foi de {} megas. Seu desconto foi de 15%, logo o valor total será R${}.'.format(quantidade, desconto))
else:
    print('Desculpe, infelizmente não poderemos seguir com a compra. Tente novamente!')
    # Para valores iguais a 0 ou inferiores e variáveis fora do padrão int para quantidade, até mesmo str localizam o erro.