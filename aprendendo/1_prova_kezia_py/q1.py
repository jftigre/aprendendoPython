'''
Peça ao usuário para digitar 10 números. Armazene todos em uma lista. Depois, crie uma nova lista apenas com os valores únicos (sem repetições), mantendo a ordem em que foram digitados, e exiba essa nova lista.

'''
numeros = []
numeros_unicos = []

for i in range(1, 11):
    numero = float(input(f'Digite o {i}ª número: '))
    numeros.append(numero)

    if numero not in numeros_unicos:
        numeros_unicos.append(numero)

print(f'Todos os números: {numeros}')
print(f'Números únicos: {numeros_unicos}')