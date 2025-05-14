'''
Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros 
termos da progressão usando a estrutura while.
'''
a1 = float(input('Digite o primeiro termo: '))
razao = float(input('Digite a razão: '))
contador = 1
termo = a1

print('Os 10 primeiros termos são: ', end='')

while contador <= 10:
    print(f'{termo:.1f}', end=' → ')
    termo += razao
    contador += 1

print('Fim')