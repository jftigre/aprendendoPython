'''Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço
da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.'''
from time import sleep

distancia = float(input('Qual a distância da viagem em Km ? '))
print('CALCULANDO...')
sleep(2)

preco = distancia * 0.5
preco_longas = distancia * 0.45

if distancia <= 200:
    print(f'Viajando {distancia:.0f}Km, o preço da passagem custará R${preco:.2f}')
else:
    print(f'Viajando {distancia:.0f}Km, o preço da passagem custará R${preco_longas:.2f}')