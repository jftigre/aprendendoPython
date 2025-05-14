'''
Faça um Programa que leia uma lista A com 10 números inteiros, calcule e mostre a soma dos quadrados dos 
elementos do vetor.
'''
lista_a = []
soma_dos_qauadrados = 0

for i in range(1, 4):
    numero = int(input(f'Digite o {i}º número: '))
    lista_a.append(numero)
    soma_dos_qauadrados += numero**2
print(f'A lista dos números é igual a: {lista_a} \nA soma dos quadrados é igual a: {soma_dos_qauadrados} ')