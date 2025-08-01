pessoas = []
maior = menor = 0

while True:
    n = input('Nome: ')
    p = float(input('Peso: '))
    pessoas.append([n, p])

    if len(pessoas) == 1:
        maior = menor = p
    else:
        if p > maior:
            maior = p
        if p < menor:
            menor = p

    cont = input('Deseja continuar [S/N]? ').strip().upper()
    if cont[0] == 'N':
        break

print(f'\nTotal de pessoas cadastradas: {len(pessoas)}')
print(f'Maior peso: {maior} kg. Peso de: ', end='')
for pessoa in pessoas:
    if pessoa[1] == maior:
        print(pessoa[0], end=' ')

print(f'\nMenor peso: {menor} kg. Peso de: ', end='')
for pessoa in pessoas:
    if pessoa[1] == menor:
        print(pessoa[0], end=' ')