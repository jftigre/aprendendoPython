'''
Peça ao usuário para digitar 5 números inteiros e armazene em uma lista.
No final, mostre:

Qual foi o maior valor digitado e em que posição(ões) ele está,

E qual foi o menor valor e sua(s) posição(ões).
'''

numeros = []

for i in range(1, 6):

    numero = int(input(f'Digite o {i}ª número: '))
    numeros.append(numero)

maior_numero = max(numeros)
menor_numero = min(numeros)

print(f'O maior número foi {maior_numero} na posição {numeros.index(maior_numero)}')    
print(f'O menor número foi {menor_numero} na posição {numeros.index(menor_numero)}')    
