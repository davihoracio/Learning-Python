print("Informe as pontuações dos atletas. Digite -1 para encerrar ")

pontos = []
maiorponto = 0

while True:
    ponto = float(input())
    if ponto == -1:
        break
    pontos.append(ponto)
maiorponto = max(pontos)
print('O recorde de pontos é {:.0f}.'.format(maiorponto))