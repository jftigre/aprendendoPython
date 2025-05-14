'''
Escreva um programa que imprima os N termos de uma Progressão Aritmética, conforme fórmula a seguir. O usuário
deverá fornecer o valor de: n (número de termos), r (razão) e a1 (primeiro termo da série)
'''
n_termos = int(input('Digite a quantidade de termos: '))
a1 = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))

an = a1 + ((n_termos - 1)*razao)

for i in range(1, n_termos + 1):
    an = a1 + ((i - 1)*razao)

    if i < n_termos:
        print(an, end=' → ')
    else:
        print(an)