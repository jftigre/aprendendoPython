'''
Fazer um programa que calcule e escreva a soma dos 50 primeiros termos da seguinte série:

'''

soma = 0
numerador = 1000
denominador = 1

for i in range(1, 51):
    soma += numerador / denominador
    numerador -= 3
    denominador += 1
print(f'A soma dos primeiros 50 termos é igual a {soma}')
