"""
Olá seja bem-vindo!
Este é meu trabalho prático da cadeira: 
Lógica de Programação e Algoritmos
"""
# EXERCÍCIO 3
print('''Olá sejam bem-vindos ao meu trabalho prático! Me chamo Asnor Ferreira Quirino Silva.
''')

# Criar uma função chamada 'cachorro_peso'
def cachorro_peso():
    print('-'*25,'| Menu 1 de 3 - Peso do pet',' '*10,'|','-'*25)
    print("""         Possuímos 3 categorias de peso para seu Pet aqui na Vestrô Pets
                |      TABELA DE PESOS      |           VALOR BRUTO         |         
                |   -> Menor que 3 kg       |            R$ 40,00           |
                |   -> De 3 até 9 kg        |            R$ 50,00           |
                |   -> De 10 até 29 kg      |            R$ 60,00           |
                |   -> De 30 até 49 kg      |            R$ 70,00           |
    OBS: Os tamanhos de pelo podem variar o valor final do serviço!\n""")
    while True:
        try:
            base_pet = float(input('Digite o peso do seu pet:\n'+'>> '))
            if (base_pet > 0) and (base_pet < 3):
                return 40
            elif (base_pet >= 3) and (base_pet <=9):
                return 50
            elif (base_pet >= 10) and (base_pet <= 29):
                return 60
            elif (base_pet >= 30) and (base_pet <= 49):
                return 70
            else: # caso o usuário digite valores menores ou iguais a zero e iguais ou maiores que 50
                print('Não aceitamos cachorros com este peso! Não informe valores menores ou iguais a zero ou iguais e acima de 50')
                print('Digite corretamente o valor do cachorro.')
                continue # retorna para a pergunta inicial
        except ValueError: # Em casos do usuário digitar strings este except irá auxiliar para prosseguir o código
            print('Não são válidos para nossos sistema pesos não numéricos!')
            print('Digite corretamente o valor do cachorro.')
# Fim da função cachorro_peso()

# Criar uma função chamada 'cachorro_pelo'
def cachorro_pelo():
    print('-'*25,'| Menu 2 de 3 - Tamanho do pelo do pet |','-'*25)
    print("""           Obrigado pela informação, agora quanto ao tamanho do pelo:
                |      TABELA DE PESOS      |           MULTIPLICADOR       |         
                |   -> Pelo curto (c)       |                x1             |
                |   -> Pelo médio (m)       |                x1.5           |
                |   -> Pelo longo (l)       |                x2             |\n""")
    while True:
        multiplicador_pet = input('Digite o tamanho de pelo do seu pet:\n'+'(c) Pets com pelos curtos\n'+'(m) Pets com pelos médios\n'+'(l) Pets com pelos longos\n'+'>> ')
        multiplicador_pet = multiplicador_pet.lower() # utiliza apenas letras minúsculas
        multiplicador_pet = multiplicador_pet.strip() # evita espaçamentos, removendo caracteres não visíveis
        if multiplicador_pet == 'c':
            return 1.0
        elif multiplicador_pet == 'm':
            return 1.5
        elif multiplicador_pet == 'l':
            return 2.0
        else:
            print('Error. Digite um valor entre c/m/l!')
            continue # retorna para o início do laço (retorna para a pergunta do pelo)
# Fim da função cachorro_pelo()

# Criar uma função chamada 'cachorro_extra'
def cachorro_extra():
    print('-'*25,'| Menu 3 de 3 - Adicional do pet',' '*5,'|','-'*25)
    print("""           Serviços adicionais do Vestrô Pets:
                |    TABELA DE ADICIONAIS   |              VALORES          |         
                |     cortar unha (1)       |            R$ 10,00           |
                |   escovar os dentes (2)   |            R$ 12,00           |
                |     limpar orelhas (3)    |            R$ 15,00           |
                |  não querer mais nada (0) |            R$ 0,00            |\n""")
    extra_pet = 0 # acumulador
    while True:
        adicional = input('Deseja adicionar mais algum serviço?\n'+'>> ')
        if adicional == '0':
            return extra_pet
        elif adicional == '1':
            extra_pet += 10.0 # Adiciona este valor ao acumulador
            continue # retorna para a pergunta de adicionar mais algum serviço - while True
        elif adicional == '2':
            extra_pet += 12.0 # Adiciona este valor ao acumulador
            continue # retorna para a pergunta de adicionar mais algum serviço - while True
        elif adicional == '3':
            extra_pet += 15.0 # Adiciona este valor ao acumulador
            continue # retorna para a pergunta de adicionar mais algum serviço - while True
        else:
            print('Error. Digite um valor entre 0/1/2/3')
            continue # retorna para o início do laço (retorna para a pergunta do serviço adicional)
# Fim da função cachorro_extra()

# Programa principal
print('-'*15,'| Bem-vindo ao Vestrô Pets do Asnor Ferreira Quirino Silva |','-'*15)
base = cachorro_peso()
multiplicador = cachorro_pelo()
extra = cachorro_extra()
total = (base * multiplicador) + extra
print('Valor total a pagar: R${:.2f} (valor do peso: R${:.2f} * valor do tamanho do pelo: R${:.2f} + valor do adicional: R${:.2f})'.format(total,base,multiplicador,extra))
print('Obrigado por Escolher a Vestrô Pets')
# fim do programa




# cães com peso < 3 ; base = 40
# cães com peso >= 3 ; base = 50
# cães com peso >= 10 ; base = 60
# cães com peso >= 30 ; base = 70
# def cachorro_pelo(pergunta,min 0, max 50):

# cães com pelo curto (c) -> multiplicador = 1
# cães com pelo médio (m) -> multiplicador = 1.5
# cães com pelo longo (l) -> multiplicador = 2

# adicional
# cortar unha (1) = 10 (valor extra)
# escovar os dentes (2) = 12 (valor extra)
# limpar orelhas (3) = 15 (valor extra)
# não querer mais nada (0) = 0 (valor extra)

# valor final
# total = base * multiplicador + extra

#A
# mensagem de boas-vindas
# B
# criar função = 'cachorro_peso()'
# perguntar 'peso' do cachorro
# retornar o valor 'base' com base no peso
# se peso >= 50 repetir (perguntar 'peso' do cachorro) 
# se digitar valor não numérico repetir (perguntar 'peso' do cachorro)
# C
# criar função = 'cachorro_pelo()'
# perguntar o 'pelo' do cachorro
# retornar o multiplicador com base nos itens descritos no enunciado
# se digitar uma opção diferente de c/m/l repetir pergunta
# D
# criar função = 'cachorro_extra()'
# perguntar pelo serviço 'adicional'
# acumular o valor 'extra' de cada 'adicional'
# enquanto não se digitar a opção de: 'não querer mais nada (0)'
# quando o 'adicional' (0) for selecionado retornar o valor extra
# E
# calcular o total a pagar do serviço
# total = 'base' * 'multiplicador' + 'extra'
# F
# utilizar o try/except
# G
# fazer comentários
# H
# colocar na saída um pedido para o usuário que digitou um valor não numérico para peso
# 'Erro ao digitar um valor não numérico. Você não digitou um peso válido!'
# 'Por favor digite novamente o valor do peso do seu pet.' I
# I
# colocar na saída um pedido para o usuário que digitou um valor acima de 50 para o peso
# # 'Erro ao digitar fora do peso permitido.'
# 'Por favor digite novamente o valor do peso do seu pet.' I
# else:
#   print('Entrada correta de peso!')
# J
# colocar um pedido onde o peso e o tipo sejam válidos e com mais 2 extras