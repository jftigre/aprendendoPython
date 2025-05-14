'''
Escreva um programa que calcula o fatorial de um dado número N.
'''
num = int(input('Digite um número inteiro: '))

if num < 0:
    print('Não existe fatorial de número negativo.')
else:
    fatorial = 1

    for i in range(1, num + 1):
        fatorial *= i

    print(f'O fatorial de {num} é igual a {fatorial}')



'''import math

num = int(input('Digite um número inteiro: '))
resultado = math.factorial(num)

print(f'O fatorial de {num} é igual a {resultado}')'''