'''
Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.
'''
from random import randint
from time import sleep

def sorteia(lista):
    print('SORTEANDO 5 VALORES...\n', end=' ')
    for i in range(0, 5):
        nums = randint(1, 25)
        lista.append(nums)
        print(f'{nums}', end= ' ', flush=True)
        sleep(0.25)

def somapar(lista):
    numeros_pares = []
    soma = 0
    for num in lista:
        if num % 2 == 0:
            numeros_pares.append(num)
            soma += num
    print(f'\nSomando os valores pares:{numeros_pares}, temos {soma}')

numeros = []
sorteia(numeros)
somapar(numeros)