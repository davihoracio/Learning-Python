q = int(input("Quantidade de jogadores? "))
li = []

print("Digite os dados para cada jogador:")
for c in range(q):
    entrada = input().split()
    nome = entrada[0]
    s, b, a = map(int, entrada[1:4])
    s1, b1, a1 = map(int, entrada[4:])
    li.append([nome, s, b, a, s1, b1, a1])

S = B = A = 0
S1 = B1 = A1 = 0

for jogador in li:
    S += jogador[1]
    B += jogador[2]
    A += jogador[3]
    S1 += jogador[4]
    B1 += jogador[5]
    A1 += jogador[6]

ps = (S1 / S) * 100 if S > 0 else 0
pb = (B1 / B) * 100 if B > 0 else 0
pa = (A1 / A) * 100 if A > 0 else 0

print("As estatísticas do jogo são as seguintes:")
print(f"Pontos de Saque: {ps:.2f} %")
print(f"Pontos de Bloqueio: {pb:.2f} %")
print(f"Pontos de Ataque: {pa:.2f} %")
