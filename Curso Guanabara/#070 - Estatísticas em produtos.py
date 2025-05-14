'''
Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai 
continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato. 

'''

while True:
    nome = str(input('Digite o nome do produto: '))
    preco = float(input('Digite o valor do produto: '))
    
    contiunar = ''
    while contiunar not in 'SN':
         contiunar = str(input('Deseja continuar ? [S/N]: ')).strip().upper()[0]
         