total = []
idades = soma = 0

while True:
    pessoa = {}
    pessoa['nome'] = input('Nome: ')

    while True:
        pessoa['sexo'] = input('Sexo (M/F): ').upper()
        if pessoa['sexo'] in ['M', 'F']:
            break
        else:
            print('Sexo inválido. Digite M ou F.')

    pessoa['idade'] = int(input('Idade: '))
    idades += pessoa['idade']

    total.append(pessoa)
    continuar = input('Deseja adicionar outra pessoa? (S/N): ').upper()
    if continuar != 'S':
        break

print(f'\nA) Foram cadastradas {len(total)}')
media = idades/len(total)
print(f'B) A média das idades é: {media:5.2f}')
print(f'C) As mulheres são: ', end='')
for c in total:
    if c['sexo'] == 'F':
        print(f'{c["nome"]}')
print(f'D) As pessoas mais velhas que a média são: ')
for c in total:
    if c['idade'] > media:
        for k, v in c.items():
            print(f'{k}: {v}')