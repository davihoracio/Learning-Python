jogadores = []

while True:
    jogador = {}
    jogador['nome'] = input('Digite o nome: ')

    partidas = int(input('Quantas partidas ele jogou? '))
    gols = []
    for partida in range(1, partidas + 1):
        gol = int(input(f'Quantos gols no {partida}° jogo? '))
        gols.append(gol)

    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)
    jogadores.append(jogador.copy())

    while True:
        continuar = input('Deseja continuar? [S/N] ').strip().upper()[0]
        if continuar in 'SN':
            break
        else:
            print('Resposta inválida. Digite S ou N.')

    if continuar == 'N':
        break

# Exibição do cabeçalho da tabela
print('-=' * 30)
print(f'{"Cod":<5}{"Nome":<15}{"Gols":<20}{"Total":<5}')
print('-' * 50)

# Exibir jogadores
for identificador, jogador in enumerate(jogadores):
    print(f'{identificador:<5}{jogador["nome"]:<15}{str(jogador["gols"]):<20}{jogador["total"]:<5}')

while True:
    mostrar_dados = int(input('Deseja mostrar os dados de qual jogador (digite 999 para finalizar)? '))
    if mostrar_dados == 999:
        break
    else:
        jogador = jogadores[mostrar_dados]
        print(f'-- LEVANTAMENTO DO JOGADOR {jogador["nome"]}:')
        for i, gols in enumerate(jogador["gols"]):
            print(f'   No jogo {i + 1} fez {gols} gols.')