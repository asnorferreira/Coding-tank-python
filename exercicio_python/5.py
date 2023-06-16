# Desenvolvimento de funções
# funções com e sem retorno de valores
# passagem de parâmetros
# escopo de variável
# tratamento de exceções
# função lambida
""" funções
- são rotinas de códigos que podem ser executadas quando
tem seu nome invocado dentro do programa
- funções deixam nossos programas mais simples
- confinam bugs para dentro delas
- tornam programas mais portáveis
- auxiliam no trabalho colaborativo
COMO CRIAR UMA FUNÇÃO?
def (palavra-chave) realce (nome da função) ()(parênteses obrigatórios):
"""
# fluxo de funções
"""def realce():
    #corpo da função
    print('|','__'*10,'|')
    print('|','__'*10,'|')
# primeiro definir uma função para depois ser chamada posteriormente
realce()
print('           MENU')
realce()"""
# passagem de parâmetros
""" passagem de parâmetros
dado recebido pela função
- ato de enviar um dado para uma função
def realce(s1):
"""
# def realce():; def realce(s1):
"""def realce(s1):
    print('|','__'*10,'|')
    print('|','__'*10,'|')
    print(s1)
    print('|','__'*10,'|')
    print('|','__'*10,'|')
# programa principal
realce('        ASNOR')
def sub2(x, y):
    res = x - y
    print(res)
# programa principal
sub2(5, 7)
sub2(y = 5, x =7)"""
# PARÂMETROS OPCIONAIS
""" parâmetros opcionais
flexibilizão o uso de funções
"""
"""def soma3(x = 0, y = 0, z =0): #cabeçalho da função
    res = x + y +z
    print(res)
x = int(input( ))
y = int(input( ))
z = int(input( ))
soma3(x,y,z)
soma3(1,2,3)
soma3(1,2)
soma3(1)
soma3()"""
""" função com parâmetro
def borda(s1):
    tam = len(s1)
    #irá imprimir caso exista algum caractere
    if tam:
        print('+', '-' * tam, '+')
        print('|',s1,'|')
        print('+', '-' * tam, '+')
# Programa principal
s1 = str(input('Informe a palvra ou frase: '))
borda(s1)
s1 = str(input('Informe a palvra ou frase: '))
borda(s1)"""
""" escopo de variável local e global
- é a propriedade que determina onde uma variável pode ser 
utilizada dentro de um programa
(escopo local)
- criado sempre que uma função é chamada 
- variáveis criadas, seja no campo de um parâmetro ou dentro do
corpo da função, fazem parte do escopo local daquela função e são chamadas de variáveis locais.
variáveis que só existem dentro daquela própria função
(escopo global)
- criado no programa principal
- variáveis globais, pertencem a um escopo global e são variáveis
criadas dentro do programa principal. Uma variável global existe também em todas as funções
invocadas ao longo do programa.
"""
""" escopo global e local
def comida(): #escopo global
    print(ovos)
# programa principal
ovos = 12
comida()

def comida(): #escopo local
    ovos = 12 # criação da variável ovos localmente na função comida
    bacon() # invoca função bacon
    print(ovos)
def bacon(): #escopo local
    ovos = 6 # função local
# programa principal
comida()
"""
""" função global e local
def comida():
    ovos = 'variável local de comida'
    print(ovos)
def bacon():
    ovos = 'variável local de bacon'
    print(ovos)
    comida()
    print(ovos)
#programa principal
ovos = 'variável global'
bacon()
print(ovos)"""
"""instrução global:
força nosso programa a não criar uma variável local de mesmo nome
e manipular somente a global dentro de uma função
"""
""" instrução global
def comida():
    global ovos
    ovos = 'comida'
ovos = 'global'
comida()
print(ovos)"""
""" retorno de valores em funções
- procedimento (procedure) - uma rotina sem retorno
- função - uma rotina que retorna um valor
"""
""" função retorno de valores
def soma3(x = 0, y = 0, z = 0):
    res = x + y + z
    return res
#Programa principal
retornado = soma3(1,2,3)
print(retornado)
# forma alternativa simplificada
print(soma3(2,2))
retornado1 = soma3(1,2,3)
retornado2 = soma3(1,2,)
retornado3 = soma3()
print('Somatórios: {}, {} e {}'.format(retornado1, retornado2, retornado3))
"""
""" valida strings
def valida_string(pergunta, min, max):
    s1 = input(pergunta)
    tam = len(s1)
    while ((tam < min) or (tam > max)):
        s1 = input(pergunta)
        tam = len(s1)
    return s1
# Programa principal
x = valida_string('Digite uma string: ', 10,30)
print('Você digitou a string: {}. \n Dado válido. Encerrando o programa....'.format(x))
"""
""" erro de exceção
ZeroDivisionError - erro de divisão por zero
ValueError - erro de um dado não esperado sendo digitado
IndexError - erro de índice inexistente sendo acessado
"""
"""def div():
    try:
        num1 = int(input('Digite um número: '))
        num2 = int(input('Digite um número: '))
        res = num1 / num2
    except ZeroDivisionError:
        print('Oops! Erro de divisão por zero...')
    except:
        print('Algo de errado aconteceu...')
    else: 
        return res
    finally:
        print('Executará sempre!')

#programa principal
print(div())"""
"""# função de parâmetro de função
def imprime_com_condicao(num, fcond):
    if fcond(num):
        print(num)
def par(x):
    return x % 2 == 0
def impar(x):
    return not par(x)

#programa principal
imprime_com_condicao(5, impar)
"""
""" lambida
função simples, sem nome, chamada de funções lambida
pode ser escrita em uma so linha de código"""
""" lambida
res = lambda x: x * x
print(res(3))"""
# def realce(s1):
# def realce():
""" interactive help
- manual explicativo de tudo dentro do python
- comando/ função via terminal: help()
- para sair do help, digitar: quit
"""
""" docstrings
- strings inseridas dentro de nosso código python que explicam o funcionamento dele
- a string é colocada na primeira linha da definição de uma função
"""
""" docstring
def soma(x=0, y=0, z=0):
    ---
    retorna o somatório de até 3 valores numéricos quaisquer.
    Todos os parâmetro são opcionais.

    x: valor numérico (opcional)
    y: valor numérico (opcional)
    z: valor numérico (opcional)
    return: soma inteira
    ---
    return x+y+z

print(soma(3,2))
help(soma)
"""
""" exercicio 1
def valida_int(pergunta, min, max):
    x = int(input(pergunta))
    while (x < min) or (x > max):
        x = int(input(pergunta))
    return x

def fatorial(num):
    ---_summary_
    calcular fatorial
    Args:
        num (_type_): _description_

    Returns:
        _type_: _description_
    ---
    fat = 1
    if num == 0:
        return fat
    for i in range(1,num+1,1):
        fat *= i # fatorial recebe ela mesma vezes i fat *= i
    return fat

# Programa principal
x = valida_int('Digite um valor para calcular a fatorial: ', 0, 9999999)
print('{}! = {}'.format(x, fatorial(x)))
help(fatorial)"""
# FUNÇÕES DE MANIPULAÇÃO 
""" abrir arquivo: open()
MODO    |   Operações
r   ->    leitura
w   ->    escrita, apaga conteúdo se já existir
a   ->    escrita, mas preserva o conteúdo se já existir
b   ->    modo binário
+   ->    atualização (leitura e escrita)
fechar arquivo>
    arquivo.close()
ler arquivo>
    arquivo.read()
    arquivo.readlines()
escrever arquivo>
    arquivo.write()
)
"""


