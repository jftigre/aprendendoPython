'''
Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na 
ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética. 
d) Em que posição está o Hamilton.
'''
pilotos_f1_2024 = ('Max Verstappen', 'Lando Norris', 'Charles Leclerc', 'Oscar Piastri', 'Carlos Sainz', 'George Russell', 'Lewis Hamilton', 'Sergio Pérez', 'Fernando Alonso', 'Pierre Gasly', 'Nico Hülkenberg', 'Yuki Tsunoda', 'Lance Stroll', 'Esteban Ocon', 'Kevin Magnussen', 'Alexander Albon', 'Daniel Ricciardo', 'Oliver Bearman', 'Isack Hadjar', 'Andrea Kimi Antonelli')

print('-'*25)
print(f'a){pilotos_f1_2024[0:5]}')
print('-'*25)
print(f'b){pilotos_f1_2024[-4:]}')
print('-'*25)
print(f'd){sorted(pilotos_f1_2024)}')
print('-'*25)
posicao_hamilton = pilotos_f1_2024.index("Lewis Hamilton")+1
print(f'd){pilotos_f1_2024[6]} está na posição {posicao_hamilton}')