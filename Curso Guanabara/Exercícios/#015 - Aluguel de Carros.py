'''
Exercício 15:
Escreva um programa que pergunte a quantidade de Km pecorridos por um carro 
alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço 
a pagar, sabendo que o carro custa R$60 por dia e R$0.15 por Km rodado

'''
km = float(input('Quantos Km rodados ? '))

dias = int(input('Quantos dias alugados ? '))

preço = (km * 0.15) + (dias * 60) 

print(f'''
 ========== RECIBO DO ALUGUEL ==========
Dias alugados     : {dias} x R$60
Km percorridos    : {km} x R$0.15
---------------------------------------
Total a pagar     : R${preço:.2f}
=======================================''')
