# Software de gerenciamento de pessoas
""" menu e opções
1) cadastrar colaborador
2) consultar colaborador
    1. consultar todos
    2. consultar por id
    3. consultar por setor
    4. retornar ao menu
3) remover colaborador
4) encerrar programa
"""
""" a - 
a) print  name
b) criar uma lista vazia -> 'lista_colaboradores'
    criar variável       -> 'id_global' (valor inicial = 0)
c) criar função          -> 'cadastrar_colaborador(id)'
    a. perguntar nome, setor, pagamento do colaborador
    b. armazenar o id (parâmetro de função), nome, setor
    , salário dentro de um dicionário
    c. copiar o dicionário para a 'lista_colaboradores'
d) Deve-se criar uma função chamada consultar_colaborador() em que: [EXIGÊNCIA DE CÓDIGO 3 de 7];
    a. Deve-se pergunta qual opção deseja 
    (1. Consultar Todos / 2. Consultar por Id / 3. Consultar por Setor / 4. Retornar ao menu) 
    e realizar o print “Opção inválida" se entrar com valor diferente de 1, 2, 3 ou 4:
    i. Se Consultar Todos, apresentar todos os colaboradores com todos os seus dados cadastrados;
    ii. Se Consultar por Id, apresentar o colaborador específico com todos os seus dados cadastrados;
    iii. Se Consultar por Setor, apresentar todos os colaboradores do setor específico com todos os seus dados cadastrados;
    iv. Se Retornar ao menu, deve-se retornar ao menu principal
e) Deve-se criar uma função chamada remover_colaborador() em que: [EXIGÊNCIA DE CÓDIGO 4 de 7];
    a. Deve-se pergunta pelo id do colaborador a ser removido;
    b. Remover o colaborador da lista_colaboradores;
f) Deve-se criar uma estrutura de menu no main em que: [EXIGÊNCIA DE CÓDIGO 5 de 7];
    a. Deve-se pergunta qual opção deseja 
    (1. Cadastrar Colaborador / 2. Consultar Colaborador / 3. Remover Colaborador / 4. Encerrar Programa) e 
    realizar o print “Opção inválida" se entrar com valor diferente de 1, 2, 3 ou 4 :
    i. Se Cadastrar Colaborador, acrescentar em um a variavel id_ global e chamar a função cadastrar_colaborador(id_ global);
    ii. Se Consultar Colaborador, chamar função consultar_colaborador();
    iii. Se Remover Colaborador, chamar função remover_colaborador();
    iv. Se Encerrar Programa, sair do menu (e com isso acabar a execução do código);
g) Deve-se utilizar lista de dicionários (uma lista contento dicionários dentro)  [EXIGÊNCIA DE CÓDIGO 6 de 7];
h) Deve-se fazer comentários no código [EXIGÊNCIA DE CÓDIGO 7 de 7];

i) Deve-se colocar na apresentação de saída de console o cadastro de 3 colaboradores (sendo 2 deles no mesmo setor) [EXIGÊNCIA DE SAÍDA DE CONSOLE 1 de 4];
j) Deve-se colocar na apresentação de saída de console a consulta de todos os colaboradores [EXIGÊNCIA DE SAÍDA DE CONSOLE 1 de ];
k) Deve-se colocar na apresentação de saída de console a consulta por código de um dos colaboradores [EXIGÊNCIA DE SAÍDA DE CONSOLE 2 de 4];
l) Deve-se colocar na apresentação de saída de console a consulta por setor em que 2 colaboradores façam parte [EXIGÊNCIA DE SAÍDA DE CONSOLE 3 de 4];
m) Deve-se colocar na apresentação de saída de console a remoção de um dos colaboradores e na sequência a consulta de todos os colaboradores [EXIGÊNCIA DE SAÍDA DE CONSOLE 4 de 4];
"""


# EXERCÍCIO 4
print('''Olá sejam bem-vindos ao meu trabalho prático! Me chamo Asnor Ferreira Quirino Silva.
''')

#------------       Variáveis globais       ------------
lista_colaboradores = []
id_global = 0
#------------              fim              ------------

#------------    cadastrar_colaborador()    ------------
def cadastrar_colaborador(id_colaborador):
    print('Olá seja bem-vindo ao menu de cadastro do colaborador ')
    print('Id do colaborador: {}'.format(id_colaborador))
    nome = input('Entre com o NOME do colaborador: ')
    setor = input('Entre com o SETOR do colaborador: ')
    pagamento_colaborador = int(input('Entre com o VALOR de pagamento do colaborador: R$'))
    print()
    dicionario_colaborador = {'id_colaborador'      : id_colaborador,
                              'nome'                : nome,
                              'setor'               : setor,
                              'salario'             : pagamento_colaborador} 
    lista_colaboradores.append(dicionario_colaborador.copy())
#------------              fim              ------------

#------------    consultar_colaborador()    ------------
def consultar_colaborador():
    print('Olá seja bem-vindo ao menu de consultar do colaborador ')
    while True: 
        consultar_option = input('     - MENU DE CONSULTAS -\n'+
                            '\nInforme qual opção você deseja:\n'+
                            '1 - Consultar TODOS os Colaboradores(as)\n'+
                            '2 - Consultar por ID dos Colaboradores\n'+
                            '3 - Consultar por SETOR de Colaboradores\n'+
                            '4 - Retornar ao MENU\n'+
                            '>> ')
        if consultar_option == '1':
            print('Opção Consultar Todos os Colaboradores(as) selecionada!')
            for colaborador in lista_colaboradores: # colaborador irá varrer toda a lista de colaboradores
                print('--------------------------------------')
                for key, value in colaborador.items(): # varrer todos os conjuntos chave e valor do dicionario colaboradores
                    print('{}: {}'.format(key, value))
                print('--------------------------------------')
        elif consultar_option == '2':
            print('Opção Consultar por Id selecionada!\n')
            id_desejada = int(input('Entre com o ID desejado: '))
            for colaborador in lista_colaboradores:
                if colaborador['id_colaborador'] == id_desejada: # o id do colaborador é igual ao id desejado
                    print('--------------------------------------')
                    for key, value in colaborador.items(): # varrer todos os conjuntos chave e valor do dicionario colaboradores
                        print('{}: {}'.format(key, value))
                print('--------------------------------------')
        elif consultar_option == '3':
            print('Opção Consultar por Setor selecionada!\n')
            setor_desejada = input('Entre com o SETOR desejado: ')
            for colaborador in lista_colaboradores:
                if colaborador['setor'] == setor_desejada: # o id do colaborador é igual ao id desejado
                    print('--------------------------------------')
                    for key, value in colaborador.items(): # varrer todos os conjuntos chave e valor do dicionario colaboradores
                        print('{}: {}'.format(key, value))
                print('--------------------------------------')
        elif consultar_option == '4':
            print('Opção Retornar ao menu selecionada!\n')
            return # sair da função consultar_colaborador e retornar ao programa principal
        else:
            print('Opção inválida! Digite novamente um valor correto\n')
            continue # retorna ao início do laço - pergunta novamente a opção desejada

#------------              fim              ------------

#------------     remover_colaborador()     ------------
def remover_colaborador():
    print('Olá seja bem-vindo ao menu de remover do colaborador ')
    id_desejada = int(input('Entre com o ID do colaborador que deseja remover do nosso sistemas: '))
    for colaborador in lista_colaboradores:
        if colaborador['id_colaborador'] == id_desejada: # o id do colaborador é igual ao id desejado
            lista_colaboradores.remove(colaborador)
            print('Colaborador REMOVIDO')

#------------              fim              ------------



#------------       Programa principal      ------------
print('Olá, seja bem-vindo ao Vestrô Software do Asnor Ferreira Quirino Silva\n')
while True: 
    menu_option = input('     | Vestrô Software |\n'+
                         '\nInforme qual opção você deseja:\n'+
                         '1 - Cadastrar Colaborador(a)\n'+
                         '2 - Consultar Colaborador(es/as)\n'+
                         '3 - Remover Colaborador(a)\n'+
                         '4 - Encerrar Programa\n'+
                         '>> ')
    if menu_option == '1':
        id_global += 1
        cadastrar_colaborador(id_global)
    elif menu_option == '2':
        consultar_colaborador()
    elif menu_option == '3':
        remover_colaborador()
    elif menu_option == '4':
        break # sair do menu (e com isso acabar a execução do código) - encerra p laço principal
    else:
        print('Opção inválida! Digite novamente um valor correto')
        continue # retorna ao início do laço - pergunta novamente a opção desejada


#------------              fim              ------------

