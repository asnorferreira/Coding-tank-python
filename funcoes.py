# > FUNÇÕES
""" 
Caixa preta - cria para abstrair uma 
lógica que será utilizada várias vezes
Pegar um texto que possui letras aleatorias e embaralhadas 
- e queremos realizar um processamento para deixar tudo organizado
"""

# 1. O que são funções e por que utilizá-la
""" Muitas vezes desejamos abstrair -- cria uma caixa preta
fazendo uma entrada e fazer uma lógica - o que a função irá devolver
"""

"""print() # Imprimi uma mensagem (int, float, str) no console (terminal, cmd)
input() # Retorna um dado informado pelo usuário (entrada padrão) e pode recever uma string
len() # Recebe uma lista e retorna o tamanho da lista
max() # Retorna o maior valor de uma lista"""

# 2. Criação de funções

# Função inicial - saudação
# def - define - definindo uma função
# def nome da função ():
"""def saudacao():
    print('Seja bem-vindo(a)')
    print('Olá, é um prazer fazer parte deste treinamento!')
"""
# definirmos a arquitetura, a caixa preta
# função criada, agora precisamos chamar a função

"""saudacao()"""
# função chamada, e executada


# Função com parâmetros
# dentro do () diremos os parâmetros
# Ao chamarmos a função saudacao, recebe um parametro que chamamos de nome
# O que passar será atribuido a variável, neste caso chamamos de nome
# f - string
"""def saudacao(nome, curso):
    print(f'Seja bem-vindo(a), {nome}!')
    print(f'Olá, é um prazer fazer parte do treinamento de {curso}')
# A função agora espera um valor - precisamos passar algo a ela
saudacao('Asnor', 'Python')
saudacao('Emilly', 'JavaScript')
"""

# Função com parâmetros default -> cria um valor padrão
# curso por default= 'Python' -> por padrão
"""def saudacao(nome, curso= 'Python'):
    print(f'Seja bem-vindo(a), {nome}!')
    print(f'Olá, é um prazer fazer parte do treinamento de {curso}')

saudacao('Asnor')
saudacao('Emilly')
"""


# Funções com retorno
# Resultado de uma função é um retorno e não o print
# return
# utilizar o return no final da execução, pois o que vier após não será executado

"""def soma(num1, num2):
    return num1 + num2

resultado = soma(5, 7)
print('O resultado da soma é', resultado)
"""
"""def calculadora(num1, num2, operacao= '+'):
    if operacao == '+':
        return num1 + num2
    elif operacao == '-':
        return num1 - num2
    else:
        return num1 * num2
  
resultado = calculadora(10, 20)
print(resultado)"""

"""def calculate():
    operation = input('Digite qual será a operação matemática desejada: + para adição; - para subtração; * para multiplicação; / para divisão: ')
    num1 = int(input('Digite o número: '))
    num2 = int(input('Digite o número: '))
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        return num1 / num2
    else:
        print('Error você não digitou um valor, tente novamente!')
    again()
    def again():
        calc_again = str(input('Você deseja calcular novamente? '))
        if calc_again.upper() == 'sim':
            calculate()
        elif calc_again.upper() == 'não':
            print('Até logo =).')
        else:
            again()
calculate()"""

def calculate():
    operation = input('''
Please type in the math operation you would like to complete:
+ for addition
- for subtraction
* for multiplication
/ for division
''')

    number_1 = int(input('Please enter the first number: '))
    number_2 = int(input('Please enter the second number: '))

    if operation == '+':
        print('{} + {} = '.format(number_1, number_2))
        print(number_1 + number_2)

    elif operation == '-':
        print('{} - {} = '.format(number_1, number_2))
        print(number_1 - number_2)

    elif operation == '*':
        print('{} * {} = '.format(number_1, number_2))
        print(number_1 * number_2)

    elif operation == '/':
        print('{} / {} = '.format(number_1, number_2))
        print(number_1 / number_2)

    else:
        print('You have not typed a valid operator, please run the program again.')

    # Add again() function to calculate() function
    again()

def again():
    calc_again = input('''
Do you want to calculate again?
Please type Y for YES or N for NO.
''')

    if calc_again.upper() == 'Y':
        calculate()
    elif calc_again.upper() == 'N':
        print('See you later.')
    else:
        again()

calculate()

