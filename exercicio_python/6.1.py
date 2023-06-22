# Importar bibliotecas
""" estruturas que existem na linguagem python - bibliotecas
RECURSOS
Importar bibliotecas  -> novas funções; podendo ser pré-definidas da linguagem, criadas por outra pessoa ou por mim mesmo
Encontrar a versão do python
"""
""" importando bibliotecas de jeitos diferentes, por apelido, diretamente, e geral posterior específico
import math
print(math.sqrt(9))
//

import math as m # Da uma apelido à biblioteca
print(m.sqrt(9))

from math import sqrt # Importa somente a função desejada:
print(m.sqrt(9))
"""
""" métodos em strings TABELA
 - listas e métodos
 uma string é imutável, mas com listas podemos alterá-la
TABELA
--------------------------------------------------------------------------------------------

FUNÇÃO                          MÉTODO      

|append(item)                   Adiciona um item ao final da lista
|count(item)                    Retorna o número de ocorrências de item na lista
|index(item)                    Retorna o índice da primeira ocorrência de item
|insert(índice, item)           Insere item no respectivo índice
|pop()                          Remove o último item
|remove(item)                   Remove a primeira ocorrência de item na lista
|reverse()                      Inverte a ordem da lista
|sort()                         Ordena a lista


FUNÇÃO/ MÉTODO           OBJETO

|startswith              Verifica se caracteres existem no início da string
|endswith                Verifica se caracteres existem no final da string
|lower                   Converte string para minúscula
|upper                   Converte string para maiúscula
|find                    Busca a primeira ocorrência de um padrão de caracteres em uma string
|rfind                   Idêntico ao find, mas inicia a busca da direta para a esquerda
|center                  Centraliza uma string
|ljust, rjust            Ajustam uma string com alinhamentos à esquerda ou à direita
|split                   Divide uma string
|replace                 Substitui caracteres em uma string
|lstrip, rstrip          Remove espaços em branco à esquerda ou a direita   
|strip                   Remove espaços em branco das extremidades


FUNÇÃO/ MÉTODO              RETORNA True para uma string com

|isalnum                    Somente letras e números; acentos são aceitos
|isalpha                    Somente letras; acentos são aceitos
|isdigit                    Somente números
|isnumeric                  Somente números; aceita também caracteres matemáticos, como frações
|isupper                    Somente caracteres maiúsculos
|islower                    Somente caracteres minúsculos
|isspace                    Somente espaços. Inclui TAB, quebra de linha, retorno, etc.
|isprintable                Somente caraceters possíveis de serem impressos na tela
"""
""" using lists
notas = []
mai = 0
men = 0
for c in range(0, 6):
    notas.append(int(input('Digite sua nota {}ª: '.format(c))))
    if c == 0:
        mai = men = notas[c]
    else:
        if notas[c] > mai:
            mai = notas[c]
        if notas[c] < men:
            men = notas[c]
print('=-'*30)
print('Você informou {}'.format(notas))
print('Sua maior nota foi {}, vocêu digitou na '.format(mai), end='')
for i, v in enumerate(notas):
    if i == mai:
        print('{}ª'.format(i), end='')
print()
print('Você informou {}'.format(notas))
print('Sua menor nota foi {}, vocêu digitou na '.format(men), end='')
for i, v in enumerate(notas):
    if v == men:
        print('{}ª'.format(v), end='')
notas.sort(reverse=True) # ordenar listas
print(notas)
media = sum(notas) / 6 # media das notas
print(media) """

"""# Exercício de número 1
words = ('mario', 'luigi', 'bowser', 'peach', 'yoshi')

for word in words: #uso de tupla
    print('\nThe word: {}. Vogais'.format(word.upper())) # temos strings dentro de tuplas -> indexação dupla
    for letter in word:
        if letter.lower() in 'aeiou': # identificar cada caracter
            print(letter.upper(), end=' ')

# Exercício de número 2
# Jogo de jokenpô
# manipular função
import random # biblioteca random

def valid_int(pergunta, min, max):
    x = int(input(pergunta))
    while ((x<min) or (x>max)):
        x = int(input(pergunta))
    return x

def winner(player1, player2):
    global empate, victory1, victory2
    if player1 == 1: # Pedra
        if player2 == 1: # Pedra
            empate += 1
        elif player2 == 2: # Papel
            victory2 += 1
        elif player2 == 3: # Tesoura
            victory1 += 1
    elif player1 == 2: # Papel
        if player2 == 1: # Pedra
            victory1 += 1
        elif player2 == 2: # Papel
            empate += 1
        elif player2 == 3: # Tesoura
            victory2 += 1
    elif player1 == 3: # Tesoura
        if player2 == 1: # Pedra
            victory2 += 1
        elif player2 == 2: # Papel
            victory1 += 1
        elif player2 == 3: # Tesoura
            empate += 1
    results = [victory1, victory2, empate]
    return results
# main program
print('JOKENPÔ')    
print('1 - Pedra')
print('2 - Papel')
print('3 - Tesoura')

results = []
play = []
victory1 = 0
victory2 = 0
empate = 0

while True:
    player1 = valid_int('Escolha sua jogada: ', 0, 3)
    if not player1:
        break 
# biblioteca que gera números aleatórios (random -> random.randint(a,b))
    player2 = random.randint(1,3) # jogadas aleatórias
    play.append([player1, player2])
    # print(play)
    results = winner(player1, player2)
    # print(winner(player1, player2))

    for plays in play:
        for data in plays:
            print(data, end=' ')
        print()

print('Number of victorys of player1: {}'.format(results[0]))
print('Number of victorys of player2: {}'.format(results[1]))
print('Number of victorys of empty: {}'.format(results[2]))"""

register = {'name':[],'sexo':[],'ano':[]}

while True:
    terminar = input('Deseja cadastrar uma pessoa? [S/N]')
    if terminar.upper() in 'N':
        break
    if terminar.upper() not in 'S':
        print('Digite S para Sim ou N para Não')
        continue
    name = input('Qual seu nome? ')
    sexo = input('Qual seu sexo [M/F]? ')
    ano = int(input('Qual seu ano de nascimento? '))
    register['name'].append(name)
    register['sexo'].append(sexo.upper())
    register['ano'].append(ano)

print(register)