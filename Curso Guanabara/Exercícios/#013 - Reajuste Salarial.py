'''
Exercício 11:
Faça um algoritmo que leia o salário de um funcionário e 
mostre seu novo salário com 15% de aumento

'''

s = float(input('Qual o salário do funcionário ? R$ '))

a = s*(115/100)

print(f'Um funcionário que ganhava R${s}, com 15% de aumento, passa a receber R${a:.2f}')
