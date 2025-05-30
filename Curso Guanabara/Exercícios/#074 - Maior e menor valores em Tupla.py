'''
Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem
de números gerados e também indique o menor e o maior valor que estão na tupla.
'''
from random import randint

numeros = (randint(1, 999), randint(1, 999), randint(1, 999), randint(1, 999), randint(1, 999))

print(f'Os números sorteados são: {numeros}')

print(f'O menor número é: {min(numeros)}')
print(f'O maior número é: {max(numeros)}')