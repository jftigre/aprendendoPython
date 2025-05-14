'''
Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso
'''
num_1 = float(input('Digite o primeiro número: '))
num_2 = float(input('Digite o segundo número: '))

opcao = 0
while opcao != 5:
    opcao = int(input('[ 1 ] somar \n[ 2 ] multiplicar \n[ 3 ] maior \n[ 4 ] novos números \n[ 5 ] sair do programa \nopção: '))
    
    mensagem = ''

    if opcao == 1:
        soma = num_1 + num_2
        mensagem = f'A soma de {num_1} + {num_2} é {soma}'
    else:
        if opcao == 2:
            multiplicar = num_1 * num_2
            mensagem = f'O produto de {num_1} x {num_2} é {multiplicar}'
        else:
            if opcao == 3:
                if num_1 > num_2:
                    mensagem = f'{num_1} é maior que {num_2}'
                else:
                    mensagem = f'{num_2} é maior que {num_1}'
            else:
                if opcao == 4:
                    print('Escolha novos números...')
                    num_1 = float(input('Digite o primeiro número: '))
                    num_2 = float(input('Digite o segundo número: '))
                    mensagem = 'Números atualizados!'
                if opcao == 5:
                    mensagem = 'Finalizando o programa...'
                if opcao < 1 or opcao > 5:
                    mensagem = 'Opção inválida! Tente novamente.'

    print(mensagem)

print('Fim do programa! Volte sempre.')
