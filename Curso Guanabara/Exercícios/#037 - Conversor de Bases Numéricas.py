'''Escreva um programa em Python que leia um número inteiro qualquer e peça para 
o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.'''


numero = int(input('Digite um número inteiro: '))

print('''[1] CONVERTER PARA BINÁRIO
[2] CONVERTER PARA OCTAL
[3] CONVERTER PARA HEXADECIMAL''')
opcao = input('ESCOLHA UMA DAS BASES PARA CONVERSÃO: ')

bina = bin(numero)[2:]
octa = oct(numero)[2:]
hexa = hex(numero)[2:]

if opcao ==  '1':
    print(f'{numero} convertido para BINÁRIO é igual a {bina}')
elif opcao == '2':
    print(f'{numero} convertido para OCTAL é igual a {octa}')
elif opcao == '3':
    print(f'{numero} convertido para HEXADECIMAL é igual a {hexa}')   
else:
    print('Opção inválida! Escolha uma das três opções: 1, 2 ou 3')