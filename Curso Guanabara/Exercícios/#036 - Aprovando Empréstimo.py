'''Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. 
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 
A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.'''

valor_casa = float(input('Qual o valor da casa: '))
salario = float(input('Qual o salário do comprador: R$'))
anos_casa = int(input('Quantos anos pretende pagar a casa: '))

prestacao = valor_casa / (12 * anos_casa)  # Cálculo da prestação mensal
limite = 0.3 * salario  # 30% do salário

if prestacao <= limite:
    print(f'O empréstimo foi APROVADO! A prestação será de R${prestacao:.2f}')
else:
    print(f'O empréstimo foi NEGADO. A prestação de R${prestacao:.2f} excede 30% do salário (R${limite:.2f}).')