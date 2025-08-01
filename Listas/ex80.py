li = list()
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0:
        li.append(n)
    elif n >= li[-1]:
        li.append(n)
    else:
        cont = 0
        while cont <= len(li):
            if n <= li[cont]:
                li.insert(cont, n)
                break
            cont += 1
print(f'Os números digitados foram: {li}')