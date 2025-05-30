''' Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço 
normal e condição de pagamento:
à vista dinheiro/cheque: 10% de desconto
à vista no cartão: 5% de desconto
em até 2x no cartão: preço formal
3x ou mais no cartão: 20% de juros'''

#valor do produto
valor_produto = float(input('Qual o valor do produto? R$ '))

#opções
print('''Escolha a forma de pagamento:
[1] À vista dinheiro/cheque (10% de desconto)
[2] À vista no cartão (5% de desconto)
[3] Em até 2x no cartão (preço formal)
[4] 3x ou mais no cartão (20% de juros)
''')

#opção do usuário
opcao = int(input('OPÇÃO: '))

if opcao == 1:
    total = valor_produto * 0.9
    print(f'O valor a ser pago com 10% de desconto será de R$ {total:.2f}')
else:
    if opcao == 2:
        total = valor_produto * 0.95
        print(f'O valor a ser pago com 5% de desconto será de R$ {total:.2f}')
    else:
        if opcao == 3:
            total = valor_produto
            print(f'O valor a ser pago será de R$ {total:.2f}')
        else:
            if opcao == 4:
                parcelas = int(input('Quantas parcelas? '))
                
                if parcelas < 3:
                    print('Número inválido! Para esta opção, as parcelas devem ser 3 ou mais.')
                else:
                    total = valor_produto * 1.2
                    valor_parcela = total / parcelas
                    print(f'Sua compra será parcelada em {parcelas}x de R$ {valor_parcela:.2f}')
                    print(f'O valor total com 20% de juros será de R$ {total:.2f}')
            else:
                print('Opção inválida! Escolha uma opção entre 1 e 4.')
