'''
Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será
o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

'''
print("=== CAIXA ELETRÔNICO ===")
saque = int(input('Digite o valor que deseja sacar: R$'))

while True:
    if saque > 0:
        cedulas_50 = saque // 50
        valor_1 = saque - (cedulas_50 * 50)
        cedulas_20 = valor_1 // 20
        valor_2 = valor_1 - (cedulas_20 * 20)
        cedulas_10 = valor_2 // 10
        valor_3 = valor_2 - (cedulas_10 * 10)
        cedulas_1 = valor_3 // 1
        break
    else:
        print('Valor inválido!')
print(f'de 50: {cedulas_50}')
print(f'de 20: {cedulas_20}')
print(f'de 10: {cedulas_10}')
print(f'de 1: {cedulas_1}')


'''
print("=== CAIXA ELETRÔNICO ===")
saque = int(input("Digite o valor que deseja sacar: R$"))

if saque > 0:
    cedulas = [50, 20, 10, 1]
    for cedula in cedulas:
        qtd = saque // cedula
        if qtd > 0:
            print(f"Cédulas de R${cedula}: {qtd}")
        saque %= cedula
else:
    print("Valor inválido! O valor deve ser maior que zero.")
'''
