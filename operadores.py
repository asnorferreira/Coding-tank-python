# >  Trabalhamos muito com matemática ex: Operações matemáticas e boobleanos;

# > Operações Matemáticas (Aritméticas)

"""
- soma: +
- subtração: -
- multiplicação: *
- divisão: /
- divisão inteira: // (descarta a parte decimal)
- resto da divisão: %
- potência: **

"""
numero1 = 10
numero2 = 20

print(type(numero1))
print(type(numero2))

print(numero1 + numero2)
print(numero1 - numero2)
print(numero1 * numero2)
print(numero1 / numero2)
print(numero1 // numero2)
print(20 // 3)
# O que estiver posterior a vírgula do resto não irá aparecer
print(20 % 3)
# Operador módulo: %-
# % resto da divisão
print(2 ** 3)


# > OPERADORES BOOLEANOS

idade1 = 10
idade2 = 15
altura1 = 1.77
altura2 = 1.65
altura3 = altura2

print(type(idade1))
print(type(idade2))
print(type(altura1))
print(type(altura2))
print(type(altura3))

# Operadores booleanos são operadores de comparação;

print(idade1 > idade2) #.False
# Maior que ...
# int
print(idade1 <= idade2) #.True
# Menor ou igual A ...
# int
print('Python' == 'python') #.False
# Igual A ...
# str
print('banana' != 'abacaxi') #.True
# Diferente de ...
# str
print(altura1 >= altura2) #.True
# Maior ou igual A ...
# float
print(altura2 > altura3) #.False
# Maior que ...
# float

# Tabela ask
# Case sensitive
# Python é orientado a objeto