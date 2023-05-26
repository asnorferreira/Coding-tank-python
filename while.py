# Laços de repetição
"""
 Estrutura de laço condicional, ou seja, quando é necessário
 repetir um trecho de código até determinada condição 
 ser satisfeita
"""
# Quando não for mais satisfeita, fluxo interrompido;
# Escolher número, salvar a variável



# Como gerar um número int aleatório
"""
função random() -> gera números reais (float)
entre 0 (incluído) e 1 (não incluido)
Representando a probabilidade de um evento acontecer
"""
# Função random() gera números float

"""
import random

x = random.random()
print(x)

"""



# Funções randrange() e randint() geram números int aleatórios dentro de um intervalo estabelecido.

"""
import random

x = random.randint(1,52)
print(x)

x = random.randrange(1,52)
print(x)

"""



# Podemos utilizar um array numpy com valores aleatórios

"""
import random
import numpy as np

# Criar o array 3 x 3 com números aleatórios entre 1 e 52
x = np.random.randint(1,52, (3,3))

print(x)
"""



# Módulo Random provê uma função -shuffle (função que permite reordenar)
# shuffle - embaralhar os elementos de uma lista, string, tupla
# Embaralha os números
"""
random.shuffle(sequencia, função)

sequencia - pode ser uma lista, tupla, string
função (opcional) - o nome da função

import random

# Criar uma lista com números entre 1 e 52
cartas = list(range(1,53))

print(cartas)

# Embaralha a lista de números
random.shuffle(cartas)

print(cartas)
"""


# Outro exemplo de aleatoriedade do método shuffle()

"""
import random

# Define uma função que cria um peso para ordenar
def peso():
    return random.random()

lista = ['maçã', 'banana', 'morango']

random.shuffle(lista, peso)

print(lista)
"""
"""
numero_sorteado = 15
numero_escolhido = int(input('Informe um número entre 1 e 20: '))

while numero_sorteado != numero_escolhido:
    print('Você errou o número, tente novamente...')

    numero_escolhido = int(input('Informe um número entre 1 e 20: '))

print('Parabéns! Você acertou')

# != -> diferente de ...
# == -> igual a ...
# Comando while -> enquanto algo
# Este código não possui um loop para chegarmos ao resultado esperado
# Com o while se não for delimitado um final haverá um looping infinito
# Observar se a variável muda dentro do while

"""

# > ESTRUTURA CONTROLADO COM WHILE
# contador = 0
# contador < 5?
# se sim - contador = contador + 1
# se não - fim do laço de repetição

# EXEMPLO 2: ESTRUTURA COM CONTADOR

contador = 0

while contador <= 5:
    print(contador)

    contador = contador + 1

print('Programa finalizado!')
