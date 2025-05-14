'''
Sendo H = 1 + 1/2 + 1/3 + 1/4 + ... + 1/N. 
Faça um programa para gerar e mostrar o número H. O número N será fornecido como entrada.
'''
print('Dada a expressão: H = 1 + 1/2 + 1/3 + ... + 1/N')
valor_N = int(input('Digite o valor de N: '))

h = 0
for i in range(1, valor_N + 1):
    h += 1 / i

print(f'O valor de H para N = {valor_N} é: {h:.1f}')