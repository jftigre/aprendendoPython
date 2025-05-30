'''
Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.  
'''
def fatorial(num, mostrar):
    fat = 1
    for i in range(num, 0, -1):
        fat *= i
        if mostrar == 'S':
            print(i, end=' ')
            if i > 1:
                print('x', end=' ')
            else:
                print('= ', end='')

    print(f'{fat}')

num = int(input('Digite um número para calcular o seu fatorial: '))
mostrar = str(input('Deseja mostrar o cálculo [S/N]? ')).upper().strip()[0]
fatorial(num, mostrar)
