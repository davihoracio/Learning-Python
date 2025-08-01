n1 = float(input("Qual é a nota da primeira unidade? "))
n2 = float(input("Qual é a nota da segunda unidade? "))
n3 = float(input("Qual é a nota da terceira unidade? "))

media = (n1 * 2 + n2 * 3 + n3 * 4) / 9

if media >= 7:
    print("\nFrancisco está aprovado")
elif media < 3:
    print("\nFrancisco está reprovado")
else:
    print("\nFrancisco está em prova final")