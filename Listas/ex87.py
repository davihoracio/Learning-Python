matriz = [[0, 0, 0], [0,0,0], [0,0,0]]
somapar = somacol3 = maiorvalor = 0
for l in range(3):
    for c in range(3):
        matriz[l][c] = int(input(f'Digite o valor [{l}][{c}]: '))
        if matriz[l][c] % 2 == 0:
            somapar += matriz[l][c]
        if c == 2:
            somacol3 += matriz[l][c]
        if l == 1:
            if c == 0:
                maiorvalor = matriz[l][c]
            if matriz[l][c] > maiorvalor:
                maiorvalor = matriz[l][c]
for l in range(3): 
    for c in range(3):
        print(f'[{matriz[l][c]}]', end='')
    print()
print(f'O valor da soma dos números pares é: {somapar}')
print(f'O valor da soma da terceira coluna é: {somacol3}')
print(f'O maior valor da segunda linha é: {maiorvalor}')

