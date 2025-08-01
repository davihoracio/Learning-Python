n = int(input("Digite um número: "))

if n <= 0:
    print("O número deve ser maior que 0.")
else:
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    print(f"Resultado do fatorial: {resultado}")