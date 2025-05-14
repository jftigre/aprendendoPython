'''
Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo
 compreendido por eles
'''
num_1 = int(input('Digite o primeiro valor inteiro: '))
num_2 = int(input('Digite o segundo valor inteiro: '))

if num_1 > num_2:
    num_1, num_2 = num_2, num_1

for i in range(num_1, num_2 + 1):
    print(f'{i}')