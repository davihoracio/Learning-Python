total = 0

while True:
    codigo = int(input('Digite o código do item: '))
    if codigo == -1:
        break
    quantidade = int(input('Digite a quantidade: '))

    if codigo == 100:
        total = total + quantidade * 5.5
    elif codigo == 101:
        total = total + quantidade * 15
    elif codigo == 103:
        total = total + quantidade * 20
    elif codigo == 104:
        total = total + quantidade * 18
    elif codigo == 105:
        total = total + quantidade * 6

print('Total a pagar: R$%.2f' % total)