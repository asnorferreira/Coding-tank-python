x = 4.2

y = 10

z = "42"

print(not ((x * y == z) and not (x < y))or y % 2 == 0)

a = int(input("Digite o primeiro número inteiro: "))
b = int(input("Digite o segundo número inteiro: "))
c = int(input("Digite o terceiro número inteiro: "))

if a > b and a > c:

  resposta = a % 2 == 0

elif b > a and b > c:

  resposta = b % 2 == 0

else:

  resposta = c % 2 == 0

print( resposta)

