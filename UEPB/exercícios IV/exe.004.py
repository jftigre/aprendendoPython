'''
Faça um Programa que leia 20 números inteiros e armazene-os numa lista. Armazene os números pares na lista PAR 
e os números IMPARES na lista impar. Imprima as três listas.
'''
numeros_pares = []
numeros_impares = []
numeros = []

for i in range(1, 5):
    numero = int(input(f'Digite o {i}º número: '))
    numeros.append(numero)
    
    if numero % 2 == 0:
        numeros_pares.append(numero)
    else:
        numeros_impares.append(numero)

print(f'lista dos números: {numeros}')
print(f'lista dos números pares: {numeros_pares}')
print(f'lista dos números impares: {numeros_impares}')