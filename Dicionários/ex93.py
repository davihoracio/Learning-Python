jogador = {}
jogador['nome'] = str(input('Nome do Jogador: '))
jogador['partidas'] = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
jogador['gols'] = []
for i in range(jogador['partidas']):
    gols = int(input(f'Quantos gols na partida {i + 1}? '))
    jogador['gols'].append(gols)    
jogador['total'] = sum(jogador['gols'])
print(f'\n📋 Dados do Jogador: {jogador["nome"]}')
print(f'O jogador {jogador["nome"]} jogou {jogador["partidas"]} partidas.')
for i, g in enumerate(jogador['gols']):
    print(f'Na partida {i + 1}, fez {g} gols.')