'''Faça um programa que leia um ano qualquer e mostre se ele é bissexto.'''

from time import sleep

ano = int(input('Digite um ano: '))
print('CALCULANDO...')
sleep(1)

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} é BISSEXTO !')
else:
    print(f'O ano {ano} NÃO É BISSEXTO !')