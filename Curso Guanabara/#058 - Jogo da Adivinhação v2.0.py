'''
 Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. 
 Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites 
 foram necessários para vencer
'''
from random import randint

computador = randint(0, 10)

print(f'Inicie um jogo, um número aleatório entre 0 e 10 foi gerado.\nTente descobri-lo !!!')

acertou = False
tentativas = 0
while not acertou:
    tentativa = int(input('Digite um número entre 0 e 10: '))
    tentativas += 1
    
    if tentativa == computador:
        acertou = True
        print(f'PARABÉNS, você acertou depois de {tentativas} tentativas. \nO número escolhido foi {computador}')
    else:
        if tentativa > computador:
            print('O número é menor! Tente novamente.')
        else:
            print('O número é maior! Tente novamente.')