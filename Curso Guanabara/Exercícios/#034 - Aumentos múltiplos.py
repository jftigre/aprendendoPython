'''Escreva um programa que pergunte o salário de um funcionário e 
calcule o valor do seu aumento. Para salários superiores a R$1250,00, 
calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.'''

salario = float(input('Qual o salário: '))

saario_10 = salario * 1.1
salario_15 = salario *1.15

if salario > 1250:
    print(f'O salário de R${salario:.2f} recebeu um aumento de 10%. O valor após o aumento será de R${saario_10:.2f}')
if salario <= 1250:
    print(f'O salário de R${salario:.2f} recebeu um aumento de 15%. O valor apóso aumento será de R${salario_15:.2f}')
