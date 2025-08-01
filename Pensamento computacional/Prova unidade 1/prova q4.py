numeros = []

print('Digite 10 números: ')
for i in range(10):
    n = int(input())
    numeros.append(n)

media = sum(numeros) / len(numeros)

print(f'A média é: {media}')
print('Os números a cima da média são: ')
for num in numeros:
    if num > media:
        print(num)