# > DICIONÁRIO
# chave = palavra e o valor = significado
# indice eu tenho o elemento x
# no dicionario posso definir um nome único que posso associá-lo a um determinado elemento
# lible = chave a uma estrutura, associando-o

# Como criar??
"""
lista = [] - criando uma lista vaiza
"""
dicionario = {} # Adiciona um dicionário vazio 
dicionario = dict() # Função que cria um dicionario vazio por padrão

# Definir uma chave ao dicionário
"""dicionario = {chave: valor, chave1: valor1}"""
dicionario = {'nome': 'Asnor', 'idade': 26, 'altura': 1.77, 'verde': True}
# Acessar os elementos do dicionário
print(dicionario)
# print(lista[0, 5]) para listas - notou a diferença?
print(dicionario['nome']) # Para dicionarios


# Adicionar elementos em um dicionário

dicionario['programador'] = True
print(dicionario)

# o dicionario pode sobrescrever o conteúdo, caso ja exista uma chave com elemento existente
dicionario['altura'] = 2
print(dicionario)



# Iterando sobre um dicionário - percorrer todas as chaves e elementos

for chave in dicionario:
    print(chave) #percorre as chaves por padrão
for chave in dicionario:
    print(chave, dicionario[chave]) #percorre as chaves e os elementos
for chave in dicionario:
    print(dicionario[chave]) #percorre os elementos


# Como sabermos se uma chave ja existe ou não

print('peso' in dicionario)
print('altura' in dicionario)

