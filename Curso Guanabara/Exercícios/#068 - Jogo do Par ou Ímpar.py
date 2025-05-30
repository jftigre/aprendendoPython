'''
Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando 
o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo. 
'''
import random

placar = contador = 0

print('VAMOS JOGAR PAR OU ÍMPAR')
while True:
    jogada = int(input('Escolha um número: '))
    paridade = str(input('Par ou Ímpar ? [P/I]: ')).strip().upper()[0]
    contador += 1

    computador = random.randint(0, 10)
    soma = (jogada + computador)
    if soma % 2 == 0:
        situacao = 'P'
    else:
        situacao = 'I'
        if situacao == paridade:
            placar += 1
            print('VOCÊ GANHOU')
        else:
            print('VOCÊ PERDEU')
            break

print(f'{contador}, {placar} ')