'''
Faça um Programa que leia 40 notas, mostre as notas e a média na tela
'''
quantidade = int(input("Quantas notas deseja digitar? "))
soma = 0
notas = []

for i in range(1, quantidade + 1):
    nota = float(input(f'Digite a nota {i}: '))
    notas.append(nota)
    soma += nota

media = soma / quantidade
print(f'\nNotas: {notas}')
print(f'Média: {media:.2f}')