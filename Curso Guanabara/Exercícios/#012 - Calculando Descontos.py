'''
Exercício 010:
Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto

'''

p = float(input('Qual o preço do produto ? R$'))

d = p* (95/100)

print(f'O produto que custava R${p}, na promoção de 5% custará R${d}')
