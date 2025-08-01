print("Informe os gastos no dia:")

gastos = []

while True:
    gasto = float(input())
    if gasto == 0:
        break
    gastos.append(gasto)

if not gastos:
    print("Você não teve gastos hoje!")
else:
    maior_gasto = max(gastos)
    print("O seu maior gasto hoje foi R$ %.2f" % maior_gasto)
