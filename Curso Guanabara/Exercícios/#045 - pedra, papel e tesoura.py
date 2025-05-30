'''Crie um programa que faça o computador jogar Jokenpô com você.'''

from random import randint
from time import sleep

print('''SUAS OPÇÕES:
[1] PEDRA
[2] PAPEL
[3] TESOURA
''')

itens = ('pedra', 'papel', 'tesoura')

jogada = str(input('Qual a sua jogada ? '))

print('JO') 
sleep(1)
print('KEN') 
sleep(1)
print('PO')  
sleep(1)

jogada_pc = randint(0,2)

print(f'O pc escolheu {jogada_pc} ')


