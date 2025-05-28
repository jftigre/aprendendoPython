'''
Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
'''
jogadores = []

while True:
    dados = {}  # Cria um novo dicionário a cada iteração
    dados['nome'] = input('Nome do jogador: ')
    partidas = int(input(f'Quantas partidas {dados["nome"]} jogou? '))
    
    gols = []
    for i in range(partidas):
        gols.append(int(input(f'Quantos gols na {i + 1}ª partida? ')))
    
    dados['gols'] = gols
    dados['total'] = sum(gols)
    
    jogadores.append(dados.copy())  # Adiciona uma cópia do dicionário à lista
    
    while True:
        continuar = input('Deseja continuar [S/N]: ').strip().upper()
        if continuar in 'SN':
            break
        print('ERRO! Por favor, somente S ou N.')
    if continuar == 'N':
        break

print('-=' * 30)
print('cod ', end='')
for k in jogadores[0].keys():
    print(f'{k:<15}', end='')
print()

for i, jogador in enumerate(jogadores):
    print(f'{i:<4}', end='')
    for v in jogador.values():
        print(f'{str(v):<15}', end='')
    print()

# Sistema de visualização de detalhes
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(jogadores):
        print(f'ERRO! Não existe jogador com código {busca}!')
    else:
        print(f'Levantamento do jogador {jogadores[busca]["nome"]}:')
        for i, g in enumerate(jogadores[busca]['gols']):
            print(f'   No jogo {i + 1} fez {g} gols.')
