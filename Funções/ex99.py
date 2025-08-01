def maior():
    quantidade = int(input('Digite quantos valores deseja analisar: '))
    numeros = []

    for numero in range(quantidade):
        valor = int(input('Digite um valor: '))
        numeros.append(valor)

    print(f'Valores digitados: {numeros}')
    print(f'O maior valor digitado foi: {max(numeros)}')

# Chamando a função
maior()