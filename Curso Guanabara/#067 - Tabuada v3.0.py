'''
Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor 
digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo. 
'''

while True:
    numero = int(input('Digite a tabuada que gostaria de saber: '))
    print('-' * 15)
    for i in range (1, 11):
        print(f'{numero} X {i} = {numero * i}')
    print('-' * 15)