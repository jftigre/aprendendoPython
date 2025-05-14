'''
Escreva um programa que leia 10 números e informe o maior e o menor número.
'''

numeros = []

for i in range(1, 11):
    numero = float(input(f'Digite o {i}ª núnero: '))
    numeros.append(numero)

maior_numero= max(numeros)

print(f'Os números são: {numeros}')
print(f'O maior número é igual a {maior_numero}')