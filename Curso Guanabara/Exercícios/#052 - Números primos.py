'''Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.'''

num = int(input('Digite um número: '))
total = 0

for i in range(1, num + 1):
    if num % i == 0:
        print(f'\033[33m{i}', end = ' ')
        total += 1
    else:
        print(f'\033[31m{i}', end = ' ')
print(f'\n\ O número {num} foi dvisível {total} vezes')

if total == 2:
    print(f'O número {num} é PRIMO!')
else:
    print(f'O número {num} NÃO é primo.')