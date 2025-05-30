'''Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça 
para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá 
escrever na tela se o usuário venceu ou perdeu.'''

import random
from time import sleep

numero = random.randint(1, 5)

numero_aleatorio = int(input('Tente adivinhar o número entre 0 e 5: '))

print('PROCESSANDO...')
sleep(2)

if numero == numero_aleatorio:
    print(f'Parabéns !!! {numero} foi o número correto')
else:
    print(f'Você errou, infelizmente o número escolhido era {numero}')    