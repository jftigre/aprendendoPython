'''
Faça um Programa que leia 5 números inteiros, armazene-os em uma lista
'''
numeros = []

for i in range(1, 6):
    numero = int(input('Digite um número: '))
    numeros.append(numero)
print(f'os números foram: {numeros}')