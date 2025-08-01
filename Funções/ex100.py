import random

def sorteio(quantidade):
    numeros = [random.randint(1, 10) for num in range(quantidade)]
    print(f'Números sorteados: {numeros}')
    return numeros

def somapar(lista):
    pares = [num for num in lista if num % 2 == 0]
    soma_pares = sum(pares)
    print(f'Números pares encontrados: {pares}')
    print(f'Soma dos números pares: {soma_pares}')

# Programa principal
quantidade = int(input('Digite a quantidade de números a sortear: '))
numeros_sorteados = sorteio(quantidade)
somapar(numeros_sorteados)