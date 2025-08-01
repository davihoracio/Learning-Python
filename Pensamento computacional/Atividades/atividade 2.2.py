compra = float(input("Qual o valor da compra? "))
pagamento = input("Como gostaria de pagar à vista(V) ou à prazo (P)? ").upper()

if pagamento == 'V':
    valorfinal = compra * 0.95
    print("Valor à pagar: " + str(valorfinal))
elif pagamento == 'P':
    valorfinal = compra * 1.08
    parcela = valorfinal / 3
    print("Valor à pagar: " + str(valorfinal))
    print("Parcela 1: " + str(parcela))
    print("Parcela 2: " + str(parcela))
    print("Parcela 3: {}'.)
else:
    print("Opção inválida.")