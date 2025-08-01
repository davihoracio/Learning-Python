li = list()
par = list()
impar = list()
while True:
    n = int(input('Digite um número: '))
    li.append(n)
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
    c = str(input('Quer continuar [S/N]?' ).upper().strip())
    if c[0] in "N":
        break
print(f'A lista completa é {li}\nOs pares são {par}\nOs impares são {impar}.')