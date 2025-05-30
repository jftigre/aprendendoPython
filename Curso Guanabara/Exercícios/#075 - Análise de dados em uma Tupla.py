'''
Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.
'''
numeros = (int(input('Digite um número: ')),
           int(input('Digite outro número: ')),
           int(input('Digite mais número: ')),
           int(input('Digite o último número: ')),)
print(f'Você digitou os números: {numeros}')
print(f'O valor 9 foi digitado {numeros.count(9)} vezes')
if 3 in numeros:
    print(f'O valor 3 foi digitado primeiro na posição {numeros.index(3)+1}')
else:
    print('O número 3 não foi digitado')

pares = [n for n in numeros if n % 2 == 0]
if pares:
    print(f'Números pares digitados: {pares}')
else:
    print('Nenhum número par foi digitado.')