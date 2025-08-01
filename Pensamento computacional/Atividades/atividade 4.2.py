notas = []
print('Digite 10 números: ')
for n in range(10):
    nota = int(input())
    notas.append(nota)

media = sum(notas) / len(notas)
print('A média é: {}'.format(media))

print('Notas maiores que a média:')
for nota in notas:
    if nota > media:
        print(nota)