'''
Faça um programa que recebe o número real x como entrada e devolva uma aproximação do arco tangente de x (em 
radianos) através da série:
Considere a aproximação para 50 termos.
'''
x = float(input("Digite o valor de x: "))
arctan = 0
sinal = 1

for i in range(50):
    expoente = 2 * i + 1
    termo = (x ** expoente) / expoente
    arctan += sinal * termo
    sinal *= -1  # alterna o sinal

print(f"Aproximação de arctan({x}) com 50 termos: {arctan}")