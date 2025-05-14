'''
Faça um programa para calcular um valor A elevado a um expoente B. Os valores A e B deverão ser lidos. 
Não usar A** B e sim uma estrutura de repetição.
'''

a = int(input('Digite um número inteiro: '))
b = int(input('Digite o número inteiro que será o expoente: '))

for i in range(1, b + 1):
    potencia = a**i
print(f'{a} elevado a {b} é igual a {potencia}')