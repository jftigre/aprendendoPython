'''
Faça um programa que leia uma quantidade não determinada de números positivos. Calcule a quantidade de números 
pares e ímpares, a média de valores pares e a média geral dos números lidos. O número que encerrará a leitura 
será zero.
'''
num_pares = 0
num_impar = 0
cont_par = 0
cont_impar = 0

while True:

    num = int(input('Digite um número: '))

    if num < 0 or num == 0:
        break
    
    if num%2 == 0:
        num_pares += num
        cont_par += 1
    else:
        num_impar += num
        cont_impar += 1

print(f'''
A quantidade de números pares é {cont_par}
A quantidade de números impares é {cont_impar}
A média dos pares é igual a {num_pares/cont_par:.1f}
A média dos impares é igual a {num_impar/cont_impar:.1f}
A média geral é igual a {(num_impar + num_pares)/(cont_impar + cont_par):.1f}
''')