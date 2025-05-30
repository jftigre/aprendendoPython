'''
Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre 
todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele
quer ou não continuar a digitar valores.
'''
escolha = 'S'
somatorio = contador = 0
numeros = []

while escolha == 'S':
    num = int(input('Digite um número: '))
    escolha = input('Deseja continuar? [S/N]: ').strip().upper()[0]
    somatorio += num
    contador += 1
    numeros.append(num)

if contador > 0:
    media = somatorio / contador
    maior = max(numeros)
    menor = min(numeros)

    print(f'Acabou! A soma é {somatorio}, a média é {media:.1f}, o menor e maior são {menor} e {maior}')
else:
    print('Nenhum número foi digitado.')