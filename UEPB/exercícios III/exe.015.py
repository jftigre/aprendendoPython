'''
Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.
Um número primo é aquele que é divisível somente por ele mesmo e por 1.
'''
num = int(input('Digite um número inteiro: '))

eh_primo = True

if num > 1:
    for i in range(2, num):
        if num % i == 0:
            eh_primo = False

    if eh_primo:
        print(f'{num} é primo.')
    else:
        print(f'{num} não é primo.')
else:
    print(f'{num} não é primo.')