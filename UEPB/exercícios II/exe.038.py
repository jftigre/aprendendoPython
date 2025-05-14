'''
Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e 
depois informar quantas notas de cada valor serão fornecidas. As notas disponíveis serão 
as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. 
O programa não deve se preocupar com a quantidade de notas existentes na máquina.
'''

saque = float(input('Digite o valor que deseja sacar: '))

# Verificar se o valor é válido e inteiro
if saque < 10 or saque > 600 or saque % 1 != 0:
    print('Valor inválido! O saque deve ser um valor inteiro entre 10 e 600 reais.')
else:
    saque = int(saque)  # Converter para inteiro (garantido pela validação)

    # Calcular a quantidade de notas
    notas_100 = saque // 100
    saque %= 100

    notas_50 = saque // 50
    saque %= 50

    notas_10 = saque // 10
    saque %= 10

    notas_5 = saque // 5
    saque %= 5

    notas_1 = saque

    # Exibir resultado
    if notas_100 > 0 or notas_50 > 0 or notas_10 > 0 or notas_5 > 0 or notas_1 > 0:
        print('Notas fornecidas:')
        if notas_100 > 0:
            print(f'{notas_100} nota(s) de 100 reais')
        if notas_50 > 0:
            print(f'{notas_50} nota(s) de 50 reais')
        if notas_10 > 0:
            print(f'{notas_10} nota(s) de 10 reais')
        if notas_5 > 0:
            print(f'{notas_5} nota(s) de 5 reais')
        if notas_1 > 0:
            print(f'{notas_1} nota(s) de 1 real')

