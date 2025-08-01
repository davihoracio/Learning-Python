pessoas = int(input('Qual o número de pessoas? \n'))
print('Informe as idades: ')
lista = []
for c in range(1, pessoas+1):
    n = int(input(''))
    lista.append(n)
media = sum(lista)/len(lista)
print('A média de idade das pessoas é {} anos'.format(media))