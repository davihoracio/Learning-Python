def leiaInt(msg):
    while True:
        n = str(input(msg))
        if n.isnumeric():
            return int(n)  # Retorna direto, não precisa de break
        else:
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')

# Programa principal
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
