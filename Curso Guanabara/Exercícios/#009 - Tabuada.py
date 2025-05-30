'''
exercício 009:
Faça um programa que leia um número inteiro qualquere e mostre na tela a sua tabuada

1 - receba um numero'int'
2 - faça a tabela de bem formatada 

'''
n = int(input('Digite um número para ver a sua tabuada: '))


print(f'''
Tabuada do {n}

======================
{n} x  1  = {n * 1:2}
{n} x  2  = {n * 2:2}
{n} x  3  = {n * 3:2}
{n} x  4  = {n * 4:2}
{n} x  5  = {n * 5:2}
{n} x  6  = {n * 6:2}
{n} x  7  = {n * 7:2}
{n} x  8  = {n * 8:2}
{n} x  9  = {n * 9:2}
{n} x 10  = {n * 10:2}
======================

''')
