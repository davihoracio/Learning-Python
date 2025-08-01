def ficha(jog='<desconhecido>', gol=0):
    print(f'O jogador {jog} fez {gol} gol(s) no campeonato.')

# Programa principal
n = input("Nome do Jogador: ").strip()
g = input("Número de Gols: ").strip()

# Validação do número de gols
if g.isnumeric():
    g = int(g)
else:
    g = 0

# Verificação de nome vazio
if n == '':
    ficha(gol=g)
else:
    ficha(n, g)
