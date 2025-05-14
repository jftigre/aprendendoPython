'''
Faça um programa que receba um número e verifique se ele é ou não triangular. OBS: um número é triangular quando 
é resultado do produto de 3 números consecutivos. Exemplo: o número 24 é triangular, pois, 24 = 2 * 3 * 4.
'''
numero = int(input("Digite um número: "))
n = 1

while True:
    multiplicacao = n * (n + 1) * (n + 2)

    if multiplicacao == numero:
        print(f'O {numero} é triangular! ({n} x {n+1} x {n+2})')
        break
    else:
        if multiplicacao > numero:
            print(f'O {numero} não é triangular.')
            break
    n += 1
