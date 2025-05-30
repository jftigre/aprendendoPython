'''Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
O primeiro valor é maior
O segundo valor é maior
Não existe valor maior, os dois são iguais'''

numero_1 = int(input('Digite o primeiro número: '))
numero_2 = int(input('Digite o segundo número: '))

if numero_1 < numero_2:
    print(f'O {numero_1} é menor que o número {numero_2} ')
elif numero_2 < numero_1:
    print(f'O {numero_2} é menor que o número {numero_1}')
else:
    print('Não existe valor menor, os valores são iguais')