'''
 Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
'''
def maior(*numeros):
    o_maior = numeros[0]
    for num in numeros:
        if num > o_maior:
            o_maior = num
    print('ANALISANDO OS NÚMEROS ESCOLHIDOS...')
    print(f'{numeros} foram escolhidos. Sendo {len(numeros)} valores ao todo.\n')
    print(f'O maior valor de {numeros} foi {o_maior}')

maior(1, 4, 4.5, 9.3, 4.6, 9.85, 11.4, 22.43, 22)