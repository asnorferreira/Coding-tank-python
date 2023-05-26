# > FOR - comando de laços de repetição
"""
Estrutura de repetição chamado for
estrutura de maneira controlada
utilização do comando for para os laços de repetição

"""

# for -> para uma determinada ou para algo....
# in -> dentro do que? de oque? dentro de uma faixa
# and -> as duas variáveis devem ter a mesma função
# or -> uma ou outra ou as duas variáveis
# função range - representa faixa
# range admite 1, 2 ou 3 parâmetros

""" for variavel in range(5): 
    print(variavel) """
# vai de 0 até menor que 5, não inclui o 5

""" for variavel in range(1,10): # Para uma determinada variável dentro de uma determinada faixa faça tal coisa
    print(variavel) """
# vai de 1 até menor que 10, não inclui o 10

""" for variavel in range(1,30,3):
    print(variavel) """
#pula de 3 em 3


# Como automatizar este código?

"""
nota1 = float(input('Informe sua nota 1: '))
nota2 = float(input('Informe sua nota 2: '))
nota3 = float(input('Informe sua nota 3: '))
"""
# Python possui uma forma de trabalhar com string, chamamos de f string
# f -> para injetarmos uma variável dentro dela
# f string

soma = 0

for i in range(0):
    nota = float(input(f'Informe sua nota {i}: '))

    soma = soma + nota

print(soma / 3)

# Estrutura para repetir de maneira controlada, melhor utilizarmos o for