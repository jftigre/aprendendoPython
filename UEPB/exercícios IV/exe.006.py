'''
Faça um Programa que leia e armazene 50 números inteiros, mostre a soma, a multiplicação e os números.
'''
numeros = []
soma = 0
multiplicacao = 1

for i in range(1, 5):
    numero = int(input(f'Digite o {i}º número: '))
    numeros.append(numero)
    soma += numero
    multiplicacao *= numero
print(f'A soma é igual a {soma} \nA multiplicação entre os números é igual a {multiplicacao} \nOs números são: {numeros}')