'''
Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através da função criada:

a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada
'''
from time import sleep


def contador(ini, fim, passo):
    for i in range(ini, fim, passo):
        print(i, end= ' ', flush=True) 
        sleep(0.25)
    print('\n')


contador(1, 11, 1)
contador(10, -2, -2)
print('AGORA É SUA VEZ! Crie uma contagem')
ini = int((input('Início: ')))
fim = int((input('Fim: ')))
passo = int((input('Passo: ')))
contador(ini, fim, passo)