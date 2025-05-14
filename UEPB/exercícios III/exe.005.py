'''
Faça um programa para calcular a área de N quadriláteros. Fórmula: Área = Lado * Lado
'''

n = int(input('Quantos quadriláteros deseja calcular? '))

for i in range(1, n + 1):
    lado = float(input(f'Digite o lado do {i}º quadrilátero: '))
    area = lado **2
    print(f'A área do {i}º quadrilátero é: {area:.2f}')
