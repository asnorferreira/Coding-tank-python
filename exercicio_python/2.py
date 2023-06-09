"""
preco_produto1 = float(input('Qual o valor do produto: '))
desconto = float(input('Digite o valor de desconto (0-100)%: ')) 
preco_final = preco_produto1 * (desconto /100)
valor = preco_produto1 - preco_final
print('O valor do produto foi de {}, com um desconto de {}, logo valor final é: {}'.format(preco_produto1, preco_final, valor))
print()
distancia = float(input('Quantos kilômetros o seu carro percorreu? '))
dias_rodados = int(input('Há quantos dias você está com o carro? '))
diaria = 60
km_rodado = 0.15
valor_km_rodado = (distancia * km_rodado) + (dias_rodados * diaria)
print('O total a pagar por {} kilômetros rodados e {} dias é de R$ {}.' .format(distancia, dias_rodados, valor_km_rodado))
print()


number = 0 + 1 + 2 + 3 + 4
print(number)
media = (23 +19 +31) / 3
print(media)
times = 403 / 73
print(times)
sobra = 403 % 73
print(sobra)
print(2 ** 10)
print(54 - 57)
def menor(x, y, z):
    min = x
    if y < min:
        min = y
    if z < min:
        min = z
    return min
def menu():
    x = int(input('numero 1: '))
    y = int(input('numero 2: '))
    z = int(input('numero 3: '))
    print('Menor número é: ', menor(x, y, z))
while True:
    menu()

////
print(min(valores))
print(max(valores))
"""