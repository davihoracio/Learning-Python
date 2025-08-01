lista = ['Daniel', 'Aluizio', 'Isabel', 'Teles', 'Eduardo']
name = str(input('Qual nome você quer verificar? '))
print('A lista contém os seguintes nomes: ')
for nome in lista:
    print(nome)
if name in lista:
    print('O nome {} está na lista, acesso permitido!'.format(name))
else:
    print('O nome {} não está na lista, acesso negado!'.format(name))