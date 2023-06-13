"""
Olá seja bem-vindo!
Este é meu trabalho prático da cadeira: 
Lógica de Programação e Algoritmos
"""
# EXERCÍCIO 2
print('''Olá sejam bem-vindos ao meu trabalho prático! Me chamo Asnor Ferreira Quirino Silva.
''')
print('Bem-vindo a sorveteria Vestrô do Asnor Ferreira Quirino Silva')
print('--------------------------------------Cardápio-------------------------------------')
print('| Nº DE BOLAS | Sabor Tradicional (tr) | Sabor Premium (pr) | Sabor Especial (es) |')
print('|      1      |        R$ 6,00         |      R$ 7,00       |       R$ 8,00       |')
print('|      2      |        R$ 11,00        |      R$ 13,00      |       R$ 15,00      |')
print('|      3      |        R$ 15,00        |      R$ 18,00      |       R$ 21,00      |')
print('-----------------------------------------------------------------------------------')

dinheiro = 0 #Variável acumuladora para os pedidos de sorvete

while True:
    sabor = input('Informe o sabor desejado, use (tr/pr/es) para responder:  ') 
    if sabor != 'tr' and sabor != 'pr' and sabor != 'es': #uso do and no código ao invés de or para evitar looping sem fim
        print('Sabor de sorvete Inválido. Tente novamente')
        continue # ao ser digitado um valor inválido, irá retornar para o while
    numero_de_bolas = int(input('Informe o número de bolas de sorvete desejado, use (1/2/3) para responder: '))
    if numero_de_bolas != 1 and numero_de_bolas != 2 and numero_de_bolas != 3: 
        print('Quantidade de sorvete Inválida. Tente novamente')
        continue # ao ser digitado um número inválido o valor volta ao início do while

    # para o sabor tradicional
    elif sabor == 'tr' and numero_de_bolas == 1:
        sabor = 'Sabor Tradicional'
        dinheiro = dinheiro + 6 # acumulador somado a 6
        print('Você selecionou {} com {}. Seu valor foi de R$ 6,00'.format(sabor, numero_de_bolas))
    elif sabor == 'tr' and numero_de_bolas == 2:
        sabor = 'Sabor Tradicional'
        dinheiro = dinheiro + 11 #repetição com uso do .format para facilitar as informações
        print('Você selecionou {} com {}. Seu valor foi de R$ 11,00'.format(sabor, numero_de_bolas))
    elif sabor == 'tr' and numero_de_bolas == 3:
        sabor = 'Sabor Tradicional'
        dinheiro = dinheiro + 15 # valor que continha no acumulador somado com o novo representado
        print('Você selecionou {} com {}. Seu valor foi de R$ 15,00'.format(sabor, numero_de_bolas))

    # para sabor premium
    elif sabor == 'pr' and numero_de_bolas == 1:
        sabor = 'Sabor Premium'
        dinheiro = dinheiro + 7 # valor que continha no acumulador somado com o novo representado
        print('Você selecionou {} com {}. Seu valor foi de R$ 7,00'.format(sabor, numero_de_bolas))
    elif sabor == 'pr' and numero_de_bolas == 2:
        sabor = 'Sabor Premium'
        dinheiro = dinheiro + 13 # valor que continha no acumulador somado com o novo representado
        print('Você selecionou {} com {}. Seu valor foi de R$ 13,00'.format(sabor, numero_de_bolas))
    elif sabor == 'pr' and numero_de_bolas == 3:
        sabor = 'Sabor Premium'
        dinheiro = dinheiro + 18 # valor que continha no acumulador somado com o novo representado
        print('Você selecionou {} com {}. Seu valor foi de R$ 18,00'.format(sabor, numero_de_bolas))

    # sabor especial
    elif sabor == 'es' and numero_de_bolas == 1: # sorvetes de sabor especial, programas repetidos com o mesmo objetivo
        sabor = 'Sabor Especial'
        dinheiro = dinheiro + 8 # valor que continha no acumulador somado com o novo representado
        print('Você selecionou {} com {}. Seu valor foi de R$ 8,00'.format(sabor, numero_de_bolas))
    elif sabor == 'es' and numero_de_bolas == 2:
        sabor = 'Sabor Especial'
        dinheiro = dinheiro + 15 # valor que continha no acumulador somado com o novo representado
        print('Você selecionou {} com {}. Seu valor foi de R$ 15,00'.format(sabor, numero_de_bolas))
    elif sabor == 'es' and numero_de_bolas == 3:
        sabor = 'Sabor Especial'
        dinheiro = dinheiro + 21 # valor que continha no acumulador somado com o novo representado
        print('Você selecionou {} com {}. Seu valor foi de R$ 21,00'.format(sabor, numero_de_bolas))
    
    adicionar_pedido = input('Deseja adicionar mais algum sorvete (S/ digite outra tecla)?: ')
    adicionar_pedido = adicionar_pedido.upper() # soluciona problemas ao digitar letras maiúsculas ou minúsculas
    if adicionar_pedido == 'S':
        continue
    else:
        print('O valor total a ser pago foi de R${:.2f}'.format(dinheiro))
        break
print('')
print('Obrigado por escolher a sorveteria Vestrô, volte sempre!')