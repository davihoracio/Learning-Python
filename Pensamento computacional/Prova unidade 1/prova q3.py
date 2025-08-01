print('Digite seus dados para confirmar se você pode entrar ou não na atração')
idade = int(input("Qual a idade da pessoa? "))
altura = float(input("Qual a altura da pessoa (em cm)? "))

if idade >= 12 and altura >= 140:
    print("Você pode entrar na atração")
else:
    print("Você não pode entrar na atração")