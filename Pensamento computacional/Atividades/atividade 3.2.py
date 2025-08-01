valores = []
print('Insira a taxa do exame para 10 pacientes:')
for i in range(10):
    numero = float(input())
    valores.append(numero)

mediaarit = sum(valores) / len(valores)
mediaharm = len(valores) / sum(1 / v for v in valores)
produto = 1
for v in valores:
    produto *= v
mediageo = produto ** (1 / len(valores))

erroharm = (mediaharm - mediaarit) / mediaarit
errogeo = (mediageo - mediaarit) / mediaarit
erromed = (erroharm + errogeo) / 2

print('Média aritmética: %.2f' % mediaarit)
print('Média harmônica: %.2f' % mediaharm)
print('Média geométrica: %.2f' % mediageo)
print('Erro médio: %.2f%%' % (erromed * 100))
