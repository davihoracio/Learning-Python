def fatorial(num, show=False):
    f = 1
    for numero in range(num, 0, -1):
        f *=numero
        if show:
            print(numero, end= ' ')
            if numero > 1:
                print('x', end= ' ')
            else:
                print('=', end=' ')
    print(f)

fatorial(5, show=True)