'''Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.'''

num = int(input('Digite um número para ver a sua tabuada: '))

for i in range(1, 11):
    multi = i * num
    print(f'{num} x {i} = {multi}')