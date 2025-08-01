num = list()
for cont in range(1, 6):
    n = int(input('Digite um número: '))
    num.append(n)
maior = max(num)
menor = min(num)
print(f'\nVocê digitou: {num}')
print(f'O maior valor foi {maior} nas posições: ', end='')
for i, v in enumerate(num):
    if v == maior:
        print(f'{i} ', end='')
print(f'\nO menor valor foi {menor} nas posições: ', end='')
for i, v in enumerate(num):
    if v == menor:
        print(f'{i} ', end='')