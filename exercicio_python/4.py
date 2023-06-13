""" while True
total = 0
dinheiro = 0
while True:
    idade = input('Informe sua idade: ')
    if idade == 'sair':
        break
    idade = int(idade)
    total += 1
    if idade < 3:
        ingresso = 0
    else:
        if idade > 12:
            ingresso = 30
        else:
            ingresso = 15
    dinheiro += ingresso
media = dinheiro / total
print('Total de pessoas: {}'.format(total))
print('Total arrecadado: R$ {}'.format(dinheiro))
print('Média arrecadada: R$ {} por pessoa'.format(media))"""
""" repetição com cédulas
valor = float(input('Digite o valor em R$: '))
while True:
    if valor >= 100:
        cedulas_100 = valor // 100
        valor -= cedulas_100 * 100
        print('Cédulas de 100: {}'.format(cedulas_100))
        if not valor:
            break
    if valor >= 50:
        cedulas_50 = valor // 50
        valor -= cedulas_50 * 50
        print('Cédulas de 50: {}'.format(cedulas_50))
        if not valor:
            break
    if valor >= 20:
        cedulas_20 = valor // 20
        valor -= cedulas_100 * 20
        print('Cédulas de 20: {}'.format(cedulas_20))
        if not valor:
            break
    if valor >= 10:
        cedulas_10 = valor // 10
        valor -= cedulas_10 * 10
        print('Cédulas de 10: {}'.format(cedulas_10))
        if not valor:
            break
    if valor >= 5:
        cedulas_5 = valor // 5
        valor -= cedulas_5 * 5
        print('Cédulas de 5: {}'.format(cedulas_5))
        if not valor:
            break
    if valor:
        cedulas_1 = valor
        print('Cédulas de 1: {}'.format(cedulas_1))
        break"""
""" calculadora
print('CALCULADORA')
print('+ Adição')
print('- Subtração')
print('* Multiplicação')
print('/ Divisão')
print('Pressione "s" para sair')
while True:
    op = str(input('Qual operação deseja fazer? '))
    if (op == '+' or op == '-' or op == '*' or op == '/'):
        x = float(input('Digite o primeiro valor: '))
        y = float(input('Digite o segundo valor: '))

    if (op == '+'):
        res = x + y
        print('Resultado: {} + {} = {}'.format(x, y, res))
        continue
    elif (op == '-'):
        res = x - y
        print('Resultado: {} - {} = {}'.format(x, y, res))
        continue
    elif (op == '*'):
        res = x * y
        print('Resultado: {} * {} = {}'.format(x, y, res))
        continue
    elif (op == '/'):
        res = x / y
        print('Resultado: {} / {} = {}'.format(x, y, res))
        continue
    elif (op == 's'):
        break
    else:
        print('Operação inválida!')
print('Programa encerrado...')"""
"""i = 0
while (i < 10 and i != 9):
    print(i)
    i += 2
for i in range(0, 10, 2):
    print(i)"""
"""for i in range(0, 13, 1):
    print(i)
i = 0
while (i < 10):
    print(i)
    i += 1
"""
""" while/ for/ for and while
#2 while
tabuada = 1
while tabuada <= 10:
    print('TABUADA DO {}'.format(tabuada))
    i = 1
    while i <= 10:
        print('{} * {} = {}' .format(tabuada, i, tabuada * i))
        i += 1
    tabuada += 1

for tabela in range(1, 11, 1):
    print('TABUADA DO {}: '.format(tabela))
    for a in range(1, 11, 1):
        print('{} * {} = {}' .format(tabela, a, tabela * a))
        form = 1
while form <= 10:
    print('TABUADA DO {}'.format(form))
    d = 1
    for d in range(1, 11, 1):
        print('{} * {} = {}' .format(form, d, form * d))
    form += 1
"""
""" alinhar estruturas de repetição
podemos inserir laços dentro de outro laço
não existe limite para quantos laços podemos colocar dentro de outro
podemos misturar while and for
"""
""" estrutura for para média de numeros pares
soma = 0
qtd = 0
for i in range(1,101):
    if (i % 2 == 0):
        soma += i
        qtd += 1
media = soma / qtd
print('A média dos pares de 1 até 100 é: {}'.format(media))
"""
""" comparativo for and while
x = 1
while(x < 6):
    print(x)
    x += 1
for in range(1,6,1):
    print(i)
"""
""" utilizando for
for i in range(6): # conta de 0 a 5
    print(i)
for i in range(0,6,2): # conta de 2 em 2
    print(i)
for i in range(10, 0, -2):
    print(i)
"""
""" for
Assim como while, essa estrutura repete um bloco de instruções enquanto
uma condição se mantiver verdadeira;
no entanto, diferentemente do while, o for é empregado em situações em 
que o número de vezes que o laço irá executar é finito e bem definido

for i in range(6):
"""
""" utilizando Truthy and Falsey
nome = ''
while not nome:
    nome = input('Digite seu nome: ')
valor = int(input('Digite qualquer número: '))
if valor:
    print('Você digitou um valor diferente de zero. ')
else:
    print('Você digitou zero.')
"""
""" truthy and falsey
dados não booleanos também podem ser tratados como True e False em uma
condição, seja esta de uma estrutura condicionada ou de um laço

Falsey / False -> número zero (int ou float) and string vazia
Truthy / True -> qualquer outro lado
"""
""" utilizando continue
while True:
    nome = str((input('Qual o seu nome? ')))
    if (nome != 'Nozinho'):
        continue
    senha = str(input('Qual a sua senha? '))
    if (senha == 'Svp0rt123'):
        break
print('Acesso concedido.')
"""
""" continue
Serve para retornar o laço ao início a qualquer momento, independente do
estado da variável de controle da condicional do laço
"""
""" utilizando o break
print('Digite uma mensagem que irei repetir para você! ')
print('Caso deseje sair favor digitar "sair"!. ')
while True:
    texto = input('')
    print(texto)
    if texto == 'sair':
        break
print('Encerrando programa...')
"""
""" break
Serve para encerrar um laço de repetição previamente, independente do estado
da variável de controle do laço
"""
""" repetição até ser digitado o valor desejado
x = int(input('Digite um valor maior que zero: '))
while (x <= 0):
    x = int(input('Digite um valor maior que zero: '))
print('Você digitou {}. Programa encerrado'.format(x))
"""
""" variantes
x = x + 1 -> x+=1
x = x - 1 -> x-=1
x = x * 2 -> x*=2
x = x / 2 -> x/=2
x = x ** 2 -> x**=2
x = x // 2 -> x//=4
"""
""" acumuladores
soma = 0
cont = 1
while (cont <= 5):
    x = float(input('Digite a {}ª nota: '.format(cont)))
    soma += x
    cont += 1
media = soma / 5
print('Média final: {}'.format(media))
if media >= 7:
    print('Aprovado!')
elif media >= 5:
    print('Recuperação')
elif media < 5:
    print('Reprovado')
else:
    print('Error')
"""
""" contadores com números par
inicial = int(input('Qual valor deseja iniciar a contagem? '))
final = int(input('Qual valor deseja encerrar a contagem? '))
x = inicial
while (x <= final):
    if(x % 2 == 0):
        print(x)
    x = x + 1
# Estruturas de repetição
# estrutura iterativa, laço de repetição ou loop de repetição
# while and for
"""
""" while
while - enquanto
-> repete um bloco de instruções enquanto determinada condição se mantiver 
verdadeira. Caso contrário, ocorre o desvio para a primeira linha de código
após este bloco de repetição
resultado booleano falso fim do bloco de repetição
while(x>y):
"""
""" variáveis contadores e acumuladoras
contadoras
    acrescentam valores constantes em uma variável
acumuladoras
    acumulam totais, como um somatório
x = 1
while (x != 100):
    print(x)
    x = x + 1
else: 
    print('Programa finalizado!')
"""