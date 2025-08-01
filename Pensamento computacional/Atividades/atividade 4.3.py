meses = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]

num = int(input("Qual o número do mês? "))
if 1 <= num <= 12:
    print("O mês é", meses[num - 1])
else:
    print("Erro: não existe mês de número {}! Por favor, digite um número entre 1 e 12.".format(num))