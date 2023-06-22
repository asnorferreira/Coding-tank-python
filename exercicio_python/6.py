# Tuplas ()
""" o que são tuplas ()
variável simples - armazena somente um dado
variável composta - armazena um conjunto de dados
-> composta variável
- (mochila[0]) - martelo
- mochila[1] - chaves
- estrutura de dados -> conjunto de dados organizados de uma maneira específica na memória do programa
    Maneira como os dados estão organizados na memória, como podem ser buscados,
    manipulados e acessados, é o que 
Tupla é uma estrutura estática
"""
"""mochila = ('machado','camisa','martelo', 'assadeira')
print(mochila)
print(mochila[0]) # print do elemento 1 - índice 0
print(mochila[2]) # print do elemento 3 - índice 3
print(mochila[0:2]) # print do elemento 1 e 2 - índice 0 e 1
print(mochila[2:]) # print dos elementos a partir do índice 2
print(mochila[-1]) # print do último
# mochila[2] = 'ovos' # vai dar error pois a tupla é imutável

for item in mochila:
    print('Dentro da mochila temos: {}'.format(item))

tam = len(mochila)
for i in range (0, tam, 1):
    print('Na minha mochila tem: {}'.format(mochila))

mochila = ('Martelo0','Cadeira','Martelo','Alicate',)
upgrade = ('Laranja','Manga','Abacate','Maxixi',)

big_mochila = mochila + upgrade

print(mochila)
print(upgrade)
print(big_mochila)

big_mochila_invert = upgrade + mochila
print(big_mochila)
print(big_mochila_invert)

-> Desempacotamento de parâmetros em funções
"""
""" Desempacotamento de parâmetros e funçoes
def soma(*num): # o '*' é um desempacotamento, pegando todos os dados como parâmetro e jogando para a variável num
    soma = 0
    print('Tupla: {}'.format(num))
    for i in num:
        soma += i
    return soma

# Programa inicial
print('Resultado: {}\n'.format(soma(1,2)))
print('Resultado: {}\n'.format(soma(1,2,3,4,5,6,7,8,9)))"""
# Listas []
""" listas [] definição
São estruturas de dados dinâmicos
podemos alterar dados e tamanho
indexar por valores numéricos inteiros
representado por colchetes []
"""
""" Listas []
mochila = ('m','d','q','w')
print('Tupla ',mochila)
mochila = ['m','d','q','w']
print('Lista ',mochila)
mochila[2] = 'laranja' # Subistitui o valor
print('Lista ',mochila)

mochila.append('Ovos') # adiciona ao final
print('Lista ',mochila)

mochila.insert(1,'Canivete') # adiciona onde for direcionado
print('Lista ',mochila)

del mochila[1] # maneira 1 de remover
print('Lista', mochila)
mochila.remove('Ovos') # maneira 2 de remover
print('Lista ', mochila)

# mesma referência
x = [5, 7, 9, 11]
y = x
print(x)
print(y)

y[0] = 2
print(x)
print(y)

# copia
x = [5, 7, 9, 11]
y = x[:] # cria uma cópia diferente da outra variável
print(x)
print(y)

y[0] = 2
print(x)
print(y)"""
""" métodos
paradígma (orientação a objetos)
- uma lista é um objeto de uma classe dentro do python
- paradigmas de programação orientada a objetos (POO)
 -> método é equivalente à função 
    mochila.append('Ovos') # adiciona ao final
    variavel.funcao(parametro)
"""
# Strings e listas dentro de listas
""" strings e listas dentro de listas
Strings dentro das listas
mochila = ['mochila','camisa','bacon','abacate']
m a c h a d o
| | | | | | |
0 1 2 3 4 5 6
mochila[0][0] -> m
 - dupla indexação -> o primeiro índice é referente a cada item da lista
 - Segundo indice é referente a cada caractere da string
 - podendo acessar não so cada dado dentro da lista, mas também cada caractere das strings de um índice da lista


"""
""" string dentro de lista
mochila = ['mochila','camisa','bacon','abacate']
print(mochila[0][0])
print(mochila[3][2])

for item in mochila:
    for letra in item:
        print(letra, end='')
    print()

for i in range(0,len(mochila),1):
    for j in range(0,len(mochila[i]),1):
        print(mochila[i][j], end='')
    print()
"""
""" lista dentro de lista
                  [0]              [1]             [2]
                   |                |               |
mochila = [['Cebola',0.39], ['Tomate',0.49], ['Maçã',0.89]]
                |      |        |       |       |      |
               [0]    [1]      [0]     [1]     [0]    [1]

item = []
mercado = []

for i in range(3):
    item.append(input('Digite o nome do item: '))
    item.append(int(input('Digite a quantidade: ')))
    item.append(float(input('Digite o valor: ')))
    mercado.append(item[:])
    item.clear()
print(mercado)               

mercado = []
for i in range(3):
    nome = input('Digite o nome do item: ')
    qtd = int(input('Digite a quantidade: '))
    valor = float(input('Digite o valor: '))
    mercado.append([nome, qtd, valor])
print(mercado)
soma = 0
print('Lista de compras: ')
print('-' * 20)
print('item | quantidade | valor unitário | total do item')
for item in mercado:
    print('{} | {} | {} | {}'.format(item[0], item[1], item[2], item[1] * item[2]))
    soma += item[1] * item[2]
print('-' * 20)
print('Total a ser pago: {}'.format(soma))
"""
# Dicionários {}
""" dicionários {}
-> estrutura dinâmica
-> podemos alterar dados e tamanho
-> indexados por chaves
-> {}
métodos para dicionários
- values: obtém somente dados
- keys: obtém somente chaves
- items: obtém o par chave: dado
"""
""" dicionários {}
game = {'nome':'Super Mário',
        'desenvolvedora':'Nitendo',
        'ano':1990}
print(game)
print(game['nome'])
print(game['desenvolvedora'])
print(game['ano'])

print(game.values())
for i in game.values():
    print(i)

print(game.keys())
for i in game.keys():
    print(i)

print(game.items())
for i,j in game.items():
    print('{} = {}'.format(i, j))"""
""" listas com dicionários
- uma lista contendo, em cada índice, um dicionário
"""
""" dicionários dentro de listas
games = []
games1 = {'nome':'Super Mário',
          'videogame':'Super Nitendo',
          'ano':1990}
games2 = {'nome':'Zelda Ocarina of time',
          'videogame':'Nitendo 64',
          'ano':1998}
games3 = {'nome':'Pokemon Yellow',
          'videogame':'Game boy',
          'ano':1999}
games = [games1, games2, games3]
print(games)

game = {}
games = []
for i in range(3):
    game['nome'] = input('Qual o nome do jogo? ')
    game['videogame'] = input('Para qual video-game ele foi lançado? ')
    game['ano'] = input('Qual o ano de lançamento? ')
    games.append(game.copy())
print('-' * 20)
for e in games:
    for i, j in e.items():
        print('O campor {} tem o valor {}'.format(i, j))"""
""" listas dentro de dicionários
games = {'nome':['Super Mario', 'Zelda', 'Pokemon'],
         'videogame':['Super Nitendo', 'Nintendo 64', 'Game Boy'],
         'ano':['1990','1998','1999']}
print(games)

games = {'nome':[],'videogame':[],'ano':[]}
for i in range(3):
    nome = input('Qual o nome do jogo? ')
    videogame = input('Para qual video-game ele foi lançado? ')
    ano = input('Qual o ano do lançamento? ')
    games['nome'].append(nome)
    games['videogame'].append(videogame)
    games['ano'].append(ano)
print('-' * 20)
print(games)"""
# Métodos em strings
""" métodos em strings TABELA
 - listas e métodos
 uma string é imutável, mas com listas podemos alterá-la
TABELA
--------------------------------------------------------------------------------------------
          FUNÇÃO/ MÉTODO          OBJETO
|append(item)                   Adiciona um item ao final da lista
|count(item)                    Retorna o número de ocorrências de item na lista
|index(item)                    Retorna o índice da primeira ocorrência de item
|insert(índice, item)           Insere item no respectivo índice
|pop()                          Remove o último item
|remove(item)                   Remove a primeira ocorrência de item na lista
|reverse()                      Inverte a ordem da lista
|sort()                         Ordena a lista

          FUNÇÃO/ MÉTODO          OBJETO
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

    FUNÇÃO/ MÉTODO          RETORNA True para uma string com
|isalnum                    Somente letras e números; acentos são aceitos
|isalpha                    Somente letras; acentos são aceitos
|isdigit                    Somente números
|isnumeric                  Somente números; aceita também caracteres matemáticos, como frações
|isupper                    Somente caracteres maiúsculos
|islower                    Somente caracteres minúsculos
|isspace                    Somente espaços. Inclui TAB, quebra de linha, retorno, etc.
|isprintable                Somente caraceters possíveis de serem impressos na tela
"""
""" manipulação de strings com métodos
s1 = list('Algoritmos')
print(s1) # print separado
print(''.join(s1)) # print agrupado
s1[0] = 'a'
print(''.join(s1))"""