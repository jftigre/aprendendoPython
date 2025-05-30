'''
exercício 007:
Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média 

1 - receba as duas notas do bimestre
2 - some a n1 e a n2 e dps divida por 2
3 - print o resultado com casas decimais

'''
'''
#CÓDIGO FUNCIONANDO#

n1 = float(input('Insira a nota da primeria prova: '))
n2 = float(input('Insira a nota da segunda prova: '))
m = float(n1+n2)/2 

print(f'A média entre {n1} e {n2} é igual a {m} ')

'''
#VOU FAZER UM ALGORITMO PARA CALCULAR NOTAS DO COM PESO

#NOTAS
l = float(input('Insira a sua nota de Linguagens: '))
h = float(input('Insira sua nota de Humanas: '))
n = float(input('Insira sua nota de Naturezas: '))
m = float(input('Insira sua nota de Matemática: '))
r = float(input('Insira sua nota de Redação: '))
#PESOS
pl = 2
ph = 1.5
pn = 1
pm = 2.5
pr = 3
#FÓRMULA
mp = (l*pl + h*ph + n*pn + m*pm + r*pr) / (pl+ph+pn+pm+pr)

print(f'A sua nota do ENEM é: {mp}')
