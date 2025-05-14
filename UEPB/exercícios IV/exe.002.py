'''
Faça um Programa que leia 10 números reais e mostre-os na ordem inversa
'''
numeros = []

for i in range(1, 11):
    numero = int(input('Digite um número: '))
    numeros.append(numero)
    lista_invertida = numeros[::-1]
print(f'os números foram: {lista_invertida}')