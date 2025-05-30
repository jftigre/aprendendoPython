'''
Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos 
serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta
'''
'''import random

jogos = int(input('Quantos jogos serão realizados: '))

for i in range(0, jogos):
    for i in range(1, 7):
        sorteio = random.randint(1, 60)
        print(sorteio, end = ' ')
    print()'''
import random

jogos = []
quantidade = int(input('Quantos jogos serão gerados? '))

for _ in range(quantidade):
    jogo = []
    while len(jogo) < 6:
        numero = random.randint(1, 60)
        if numero not in jogo:
            jogo.append(numero)
    jogo.sort()  # opcional: deixa os números em ordem crescente
    jogos.append(jogo)

# Mostrando os jogos
print('\nPalpites da Mega Sena:')
for i, jogo in enumerate(jogos, start=1):
    print(f'Jogo {i}: {jogo}')