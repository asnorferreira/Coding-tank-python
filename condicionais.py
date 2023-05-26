# ESTRUTURAS CONDICIONAIS
# Estruturas de controle de fluxo
# Executadas de maneira invariável

# Para estabelecer uma condição de uma linha ou outra ser executada

# Faz com que o fluxo de execução do código seja autorado
# Executar varias vezes um mesmo bloco

# tipos: Condicionais e laços de repetição

"""
    Imagine que você queira imprimir "Aprovado(o)", caso o estudante tenha uma média
    superior ou igual a 7, e "Reprovado, caso a média seja inferior a 7.
"""

# Estrutura básica do if
# Do contrário -> else
# Se -> if
# Então -> :
"""

idade = int(input('Digite sua idade: '))

if idade >= 18: # Os ":" significam então
    print('Você é maior de idade.')
else:
    print('Você é menor de idade.')


nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))

media = ((nota1 * 4)+ (nota2 * 6)) / 10

print('O peso da sua primeira nota é 4 e o da segunda é 6.')
print('Sua média foi: ', media)
if media >= 7:
    print('Parabéns você está aprovado!')
elif media >=5:
    print('Você irá para a recuperação!')
else:
    print('Infelizmente não foi desta vez, reprovado!')

"""
# Estrutura chamada else if é chamada no python por elif.
# Caso o estudante tenha tirado 5 ou mais pode ir para a recuperação.
# Este código pede as notas, calcula a média e imprime o estado de aprovação.

# Funções if, elif, else
# Para ser aprovado deve haver duas condições: presença em 70% e média 7.

# INICIO
nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))
print('Obrigado pelas informações! :) ')
presenca = float(input('Digite sua taxa de presença em porcentagem: '))

print('Sua presença na cadeira foi de: ', presenca,'%')

media = ((nota1 * 4)+ (nota2 * 6)) / 10

# Comando e no if e adiante usamos o and
# and -> as duas condições devem ser verdadeiras
# or -> Uma ou outra ou as duas podem ser verdadeiras

print('O peso da sua primeira nota é 4 e o da segunda é 6.')
print('Sua média foi:', media)
if media >= 7 and presenca >= 70:
    print('Parabéns você está aprovado!')
elif media >=5 and presenca >= 70:
    print('Você irá para a recuperação!')
else:
    print('Infelizmente não foi desta vez, reprovado!')

