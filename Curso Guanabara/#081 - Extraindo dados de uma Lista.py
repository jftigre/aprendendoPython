'''
Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.
'''
numeros = []

while True:
    numeros.append(int(input('Digite um número: ')))

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar ? [S/N]: ')).upper().strip()[0]
    if continuar == 'N':
        print('FIM DO PROGRAMA!')
        break
print('\nFIM DO PROGRAMA!')
print('-' * 40)

print(f'A quantidade de números digitados foi: {len(numeros)}')

numeros.sort(reverse=True)
print(f'Lista em ordem decrescente: {numeros}')

if 5 in numeros:
    print('O número 5 está na lista.')
else:
    print('O número 5 NÃO está na lista.')
