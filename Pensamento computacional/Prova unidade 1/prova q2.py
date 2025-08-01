itens = int(input('Quantos itens serão calculados? '))
valortotal = 0
total = 0
for c in range(1, itens+1):
    valor = float(input(f'Qual o valor do item {c}: '))
    quantidade = int(input(f'Qual a quantidade do item {c}: '))
    valortotal = valor * quantidade
    total +=valortotal
print(f'O valor total de sua compra: {total:.2f}')
