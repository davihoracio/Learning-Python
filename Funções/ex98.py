def contagem(inicio, fim, passo):
    if passo == 0:
        print('Passo inválido. Considerando passo 1.')
        passo = 1
    passo = abs(passo)

    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')

    if inicio < fim:
        for num in range(inicio, fim +1, passo):
            print(num, end=' ')
    else:
        for num in range(inicio, fim -1, -passo):
            print(num, end = ' ')
    print('\n')

contagem(1, 10, 1)
contagem(10, 0, 2)

# Personalização
print('Agora personalize a contagem:')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contagem(inicio, fim, passo)