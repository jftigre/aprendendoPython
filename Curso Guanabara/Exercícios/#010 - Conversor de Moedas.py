'''
exercício 010:
Crie um programa que leia quanto dinheiro 
uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar

1 - perguntar quanto tem na carteira
2 - c/cotação do dólar hoje
3 - print com resultado

'''

c = float(input('Quantos Reais tem na sua carteira ? '))

d = c/5.77
e = c/5.99
p = c/0.005

print(f'''
Com R${c} você pode comprar: 

- {d:.2f} Dólares
- {e:.2f} Euros
- {p:.2f} Pesos

''')


