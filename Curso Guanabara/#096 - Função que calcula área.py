'''
Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.
'''
def area(largura, comprimento):
    area = largura*comprimento
    print(f'A área de um terrano {largura}x{comprimento} é de {area}m2')


l = float(input('LARGURA(m): '))
c = float(input('COMPRIMENTO(m): '))
area(l, c)