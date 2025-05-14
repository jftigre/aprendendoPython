import math

num = float(input('Digite um número: '))

'''
raiz = math.sqrt(num)
print(f'A raiz de {num} é igual {raiz:.2f}')
'''

if num >= 0:
    raiz = math.sqrt(num) 
    raizr = math.ceil(num)
    print(f'A raiz de {num} é igual a {raiz:.2f}')
else:
    print('Não é possível calcular a raiz quadrada de um número negativo!')

