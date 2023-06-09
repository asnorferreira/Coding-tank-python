""" input
nome = input('Informe seu nome: ')
idade = input('Informe sua idade: ')

print('Seu nome é {0} e sua idade é {1}'.format (nome, idade))


print(nome, idade)
print(nome, idade, end='...\n')
print(nome, idade, sep='#')
"""
""" sep and end
nome = 'daniella'
sobrenome = 'marinho'

print(nome, sobrenome)
print(nome, sobrenome, end='...\n')
print(nome, sobrenome, sep='#')
"""
""" funcoes_de_entrada__e__saida
função print recebe tipo varargs de objetos e 4 argumentos opcionais (sep, end, file e flsuh)
os objetos são convertidos para string, separados por sep e terminados por end
"""
""" changing types
price = 10.5
idade = 55

print(str(price))
print(str(idade))

text = f"idade {idade} price {price}"
print(text)
"""
""" changing types
price = 10
print(price)

price = float(price)
print(price)

price = 10 / 2
print(price)
"""
""" CONSTANTE
nome = 'luck'
idade = 20

nome = 'anakin'

print(nome, idade)

limite_saque_diario = 1000

BRAZILIAN_SAQUES = ['PE', 'BA', 'PB']
print(BRAZILIAN_SAQUES)
"""
""" use %d
print('valor de a = {0}'.format(a))
print('valor de a = %d' % (a))
"""
""" variaveis
Tipos built-in:
booleano: bool 
texto: str
numérico: float (números racionais), int (números inteiros), complex
sequência: list, tuple, range
mapa: dict
coleção: set, fronzenset
binário: bytes, bytearray, memoryview
"""
""" dir e help
 Modo interativo - flag -i (file)
 função dir - retorna a lista de nomes no escopo local atual
 dir()
 dir(100)
 função help - inovca o sistema de ajuda integrado.
 Informar por parâmetro qual o nome do módulo, função, classe, método ou variável
 help()
 help(100)
"""
""" type variable
base = 10
altura = 4
area = base * altura
print(altura)

print(type(base))
print(type(altura))
print(type(area))

x = 1.0
print(type(x))
y = 18
print(type(y))
z = x + y
print(type(z))
a = 1 + 3j
print(type(a))
"""
""" +=
a = a + 1 == a +=1
"""
"""math e cmath são funções que fornecem variedade de funções matemáticas prontas"""
""" sqrt
from math import sqrt
x = 9
r = sqrt(x)
print(r)
"""
""" math and cmath
abs (x) - valor absoluto módulo de x - biblioteca padrão
int (x) - converter x para inteiro eliminando sua parte decimal - bib. padrão
float (x) - converte x para número real - bib. padrão
round (x[, n]) arredonda x com n dígitos decimais. Se n for omitido, o valor 0 é assumido - bib. padrão

trunc (x) - a parte decimal é eliminada == int(x) - bib. math
floor (x) - retorna o maior inteiro <= x. - bib.math
ceil (x) - retorna o menorinteiro >= x. - bib.math

sqrt (x) - calcula a raiz quadrada de x - bib.math e cmath
exp (x) - retorna o exponencial de x, e^x - bib.math e cmath
log (x[, base]) - retorna o logaritmo de x na base fornecida - bib.math e cmath
sin (x) - retorna o seno do ângulo x radianos - bib. math e cmath
cos (x) - retorna o cosseno do ângulo x radianos - bib.math e cmath
tan (x) - retorna o tangente do ângulo x radianos - bib.math e cmath
rect (r, phi) - converte um número complexo expresso em coordenadas polares para sua representação retangular - bib.cmath
polar (x) - retorna a representação de x em coordenadas polares. retorna uma tupla com o par (r, phi), em que r é o módulo e phi é a fase

"""
""" use format and {}
a = 12
b = 156

print('Valor de a = {0} e valor de b = {1}'.format(a, b))"""
#comandos separadores -> sep=', ' or sep='-'
""" CONSTANTE
CONSTANTE
variavel
nome deve ser snake case
escolher nomes sugestivos
nome de cosntante todo em maiúsculo
"""