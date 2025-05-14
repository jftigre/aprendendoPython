'''
Faça um Programa que peça um número inteiro e determine se ele é par ou impar.
'''
num = int(input('Digite um número: '))

if num == 0:
    resultado = ('Número inválido')
else:
    if num%2 == 1:
        resultado = ('Esse número é ÍMPAR')
    else:
        if num%2 == 0:
            resultado = ('Esse número é PAR')
print(f'{resultado}')