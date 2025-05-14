'''
Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número 
já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em 
ordem crescente. 
'''
numeros = []

while True:
    numero = float(input('Digite um valor: '))

    if numero not in numeros:
        numeros.append(numero)
        print('Valor adicionado!')
    else:
        print('Valor duplicado! Não adicionado')
    continuar = str(input('Deseja continuar ? [S/N]: ')).upper().strip()[0]
    if continuar == 'N':
        break
numeros.sort()
print(f'Você digitou os números: {numeros}')