li = []
while True:
    n = int(input('Digite um valor: '))
    if n not in li:
        li.append(n)
        print('Valor adicionado com sucesso!')
    else:
        print('O número já está na lista.')
    c = input('Quer continuar [S/N]? ').strip().upper()
    if c == 'N':
        break
li.sort()
print(f'\nVocê digitou os números: {li}')
