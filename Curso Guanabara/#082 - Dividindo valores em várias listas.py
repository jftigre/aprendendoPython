'''
Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras 
que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre 
o conteúdo das três listas geradas.
'''
numeros = []
numeros_pares = []
numeros_impares = []

while True:
    numero = (int(input('Digite um valor: ')))
    numeros.append(numero)
    
    if numero % 2 == 0:
        numeros_pares.append(numero)
    else:
        numeros_impares.append(numero)

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar ? [S/N]: ')).upper().strip()[0]
    if continuar == 'N':
        print('FIM DO PROGRAMA!')
        break

print(f'A lista completa é {numeros}')
print(f'A lista de pares é {numeros_pares}')
print(f'A lista de impares é {numeros_impares}')