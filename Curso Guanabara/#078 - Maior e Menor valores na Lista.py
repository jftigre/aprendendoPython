'''
Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado 
e as suas respectivas posições na lista. 
'''
numeros = []
numero_max = 0
numero_min = 0

for i in range(1, 6):
    numeros.append(float(input(f'Digite o {i}º número: ')))
numero_max = max(numeros)
numero_min = min(numeros)

print(f'A lista é {numeros} \nO maior número foi: {numero_max} na posição {numeros.index(numero_max)+1} \nO menor número foi: {numero_min} na posição {numeros.index(numero_min)+1}')