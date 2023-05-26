# Conversão de tipos
# Em dado momento poderemos ter a intenção de mudar os tipos das variáveis

# > CONVERSAO_DE_TIPOS

idade = '26'
numero1 = '10'
numero2 = '20'

# Continuam possuindo valores inteiros dentro de str (string)

print(numero1 + numero2)
# Efetuou uma concatenação, ou seja, juntou os str

# Como transformar e converter variáveis

idade1 = '25'

print(idade1, type(idade1))

idade1_inteira = int(idade1)
# Para nomes compostos é aconselhável utilizar o '_' para separar os nomes compostos

print(idade1_inteira, type(idade1_inteira))

# int()
# str()
# float()
# bool()

# Função input -> 

altura = float(input('Informe a sua altura: '))
# Ler tudo o que for digitado como texto
# Caso tenha certeza de que o que irá ser digitado for float, transforme em float e vice versa para as demais variáveis
# Podemos exibir o tipo da variável
print(altura, type(altura))

# Podemos converter explicitamente as variáveis
# Podemos transformar as variáveis com o comando input
