'''
Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte. 
Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
'''
while True:
    numeros_por_extenso = (
        'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis',
        'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
        'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito',
        'dezenove', 'vinte')

    while True:
        num = int(input('Digite um número de 0 a 20: '))
        if 0 <= num <= 20:
            break
        print('Tente novamente', end = '')
    print(f'Você digitou o número {numeros_por_extenso[num]}')

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar ? [S/N]: ')).upper().strip()[0]
        if continuar == 'N':
            break