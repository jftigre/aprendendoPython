'''
Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
'''
dados = {}

dados['nome'] = str(input('Nome do jogador: '))
dados['partidas'] = int(input(f'Quantas partidas {dados["nome"]} jogou ? '))
dados['gols'] = 0

for i in range(1, dados['partidas']+1):
    dados[f'partida {i}'] = int(input(f'Quantos gols na {i}º partida: '))
    dados['gols'] += dados[f'partida {i}']

print(dados)
print('-='*20)
for k, v in dados.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*20)
print(f'O jogador {dados["nome"]} jogou {dados["partidas"]} partidas')
for k, v in dados.items():
    if k.startswith('partida'):
        print(f'=> Na {k}, marcou {v} gols')