'''
Faça um programa que leia um número qualquer e mostre o seu fatorial.

Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120
'''
import math

num = int(input('Digite um número inteiro qualquer: '))
contador = num
fatorial = 1

while contador > 0:
    fatorial *= contador
    contador -= 1
print(f'O fatorial de {num} é igual a {fatorial}')