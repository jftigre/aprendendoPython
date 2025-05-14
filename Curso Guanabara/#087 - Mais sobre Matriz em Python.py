'''
Aprimore o desafio anterior, mostrando no final: 
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.
'''

soma_pares = 0
soma_terceira_coluna = 0
valores_segunda_linha = 0
matriz = [[], [], []]

for linha in range(3):
    for coluna in range(3):
        valor = int(input(f'Digite um valor para [{linha}][{coluna}]: '))
        matriz[linha].append(valor)

        

        if valor % 2 == 0:#a)SOMA DOS PARES
            soma_pares += valor

print('\n   Matriz 3x3:\n')
for linha in matriz:
    for valor in linha:
        print(f'{valor:^5}', end=' ')
    print()

print(f'A soma dos valores pares é igual a {soma_pares}')

