'''
Uma fruteira está vendendo frutas com a seguinte tabela de preços:

Até 5 Kg                     Acima de 5 Kg

Morango R$ 2,50 por Kg       R$ 2,20 por Kg

Maçã R$ 1,80 por Kg          R$ 1,50 por Kg

Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá 
ainda um desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de morangos 
e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente
'''

peso_morango = float(input('Digite o peso(Kg) dos morangos: '))
peso_maca = float(input('Digite o peso(Kg) das maças: '))

if peso_morango <= 5:
    preco_morango = peso_morango * 2.5
else:
    preco_morango = peso_morango * 2.2

if peso_maca <= 5:
    preco_maca = peso_maca * 1.8
else:
    preco_maca = peso_maca * 1.5

total = preco_morango + preco_maca
peso_total = peso_morango + peso_maca

if peso_total > 8 or total > 25:
    total *= 0.9

print(f'O valor a ser pago é: R$ {total:.2f}')