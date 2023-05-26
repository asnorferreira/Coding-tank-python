# > ESTRUTURA DE LISTAS
# Variáveis primitivas: str, bool, int, float
# Estrutura de dados
# lista -> armazena um acúmulo de variáveis dentro dela
# Estrutura que guarda várias ao mesmo tempo

# ANTES
"""nota1 = 2.5 
nota2 = 10
nota3 = 9.6"""

# Com lista
# Para definirmos uma lista abrirmos um "{}"

"""notas = {2.5, 10, 9.6}"""
# Criando listas -> definirmos chochetes {}
"""
lista = {} # lista vazia, interessante pois podemos adicionar posteriormente valores
lista = list() # Criação de uma estrutura em uma lista, que por acaso é uma lista vazia
lista = [26, 'Asnor', 0.256, False] # Permite diferente tipos de dados: float + bool + int + str
lista_de_listas = [10, [1, 2, 3]] # Listas de listas - python é uma linguagem flexível
"""
# Indexação e Slices (fatiamento)

"""
lista = [10, 'Asnor Ferreira', 0.2556, True]
print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])
print(lista[-1])
"""
# Indices no python sempre se iniciam no 0
# É uma forma que utilizamos para informarmos que estamos acessando um elemento da lista por meio de um indice
# Também podemos indexar ou acessar indices negativos
# Ultimo elemento de uma lista -1

"""
lista = [10, 50, 30, 40, 25, 60, 5]

print(lista[0:3])
print(lista[3:6])
print(lista[3:])
print(lista[2:6:2])
"""
# Começa no indice 0 e vai até no menor que 3
# Slices



# > Iterações com FOR
# Como percorrer todos os elementos de uma lista

# 1. Utilizando os próprios elementos da lista
# Para cada elemento dentro da lista, imprima elemento
"""
for elemento in lista:
    print(elemento)
"""

# 2. Utilizando os índices
# Como saber quantos elementos uma lista possui
# len -> lenf de comprimento
"""
print('Comprimento da lista: ', len(lista))

for i in range(len(lista)):
    print(lista[i])
"""
# Indices da lista ou array


# > MÉTODOS E FUNÇÕES DE LISTAS
# Oque é um método? é uma (função) que está atrelada a uma variável

lista = [1, 3, 12, 8, 2]

# appened (acidionar um elemento ao final da sua lista)
# Função dentro de uma variável - chamamos de método

print('Antes do append', lista)

lista.append(3) #adicionamos um elemento

print('Depois do append', lista)

# insert (adiciona um elemento, onde selecionamos a posição e qual elemento desejamos)
# lista.insert(indice, elemento)

print('Antes do insert', lista)

lista.insert(2, 10)

print('Depos do insert', lista)

# extend - serve para juntarmos listas - duas listas
lista2 = [1, 4, 6]

lista.extend(lista2)

print('Depois do extend', lista)


# REMOVER

# pop - remover o elemento especificado ou caso não seja irá remover o ultimo elemento
# lista.pop(indice)

lista.pop()

print('Depois do pop', lista)

lista.pop(0)

print('Depois do pop', lista)

# remove - estabelece o elemento ou valor que deseja retirar
# lista.remove(elemento)
# sempre remove o primeiro encontrado

lista.remove(3)

print('Depois do remove', lista)

# count - contar quantas vezes um elemento aparece na minha lista

print('Quantidade de 2 na lista', lista.count(2))

# index - Diz o indice de um determinado elemento dentro da lista

print('Índice do elemento 12: ', lista.index(12))

# sort - ordenar a lista de maneira crescente
# lista.sort(reverse=true) - ordena de maneira decrescente

lista.sort()

print(lista)

lista.sort(reverse=True)

print(lista)

# FUNÇÕES PARA LISTAS

# len - comprimento - quantos elementos possuímos na lista

print(len(lista))

# sum - soma de lista - soma todos os elementos da lista

print(sum(lista))

# max - maior valor da lista

print('Maior elemento da lista: ', max(lista))

# min - menor valor da lista

print('Menor elemento da lista: ', min(lista))