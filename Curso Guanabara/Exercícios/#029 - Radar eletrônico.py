''' Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, 
mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.'''

import random
from time import sleep

velocidade = random.randint(60, 125)
print('VERIFICANDO A VELOCIDADE...')
sleep(2)

velocidade_irregular = velocidade - 80
multa = velocidade_irregular * 7

if velocidade <= 80 :
    print('Velocidade está regular')
else:
    print(f'''
A velocidade está irregular! 
o condutor ultrapassou com a velocidade de {velocidade} e precisa pagar uma multa de R${multa}''')