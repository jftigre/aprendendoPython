'''
Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja 
realizar. O resultado da operação deve ser acompanhado de uma frase que diga se o número é:

par ou ímpar;

positivo ou negativo;

inteiro ou decimal.
'''
num_1 = float(input('Digite um número: '))
num_2 = float(input('Digite outro número: '))

decisao = input(''' 
Selecione a operação desejada:
[1] SOMA
[2] SUBTRAÇÃO
[3] MULTIPLICAÇÃO
[4] DIVISÃO

OPÇÃO: ''')

if decisao == '1':
    resultado = num_1 + num_2
    print(f'Resultado da soma: {resultado}')
else:
    if decisao == '2':
        resultado = num_1 - num_2
        print(f'Resultado da subtração: {resultado}')
    else:
        if decisao == '3':
            resultado = num_1 * num_2
            print(f'Resultado da multiplicação: {resultado}')
        else:
            if decisao == '4':
                if num_2 != 0:
                    resultado = num_1 / num_2
                    print(f'Resultado da divisão: {resultado}')
                else:
                    print('Erro: divisão por zero não é permitida.')
                    resultado = None
            else:
                print('Opção inválida.')
                resultado = None

if resultado is not None:
    if resultado % 2 == 0:
        print('O resultado é um número PAR.')
    else:
        print('O resultado é um número ÍMPAR.')

    if resultado > 0:
        print('O resultado é um número POSITIVO.')
    else:
        if resultado < 0:
            print('O resultado é um número NEGATIVO.')
        else:
            print('O resultado é ZERO.')

    if resultado == int(resultado):
        print('O resultado é um número INTEIRO.')
    else:
        print('O resultado é um número DECIMAL.')
