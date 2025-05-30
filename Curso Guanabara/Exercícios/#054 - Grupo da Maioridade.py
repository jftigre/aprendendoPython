'''Crie um programa que leia o ano de nascimento de sete pessoas. 
No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores'''

import datetime

ano_atual = datetime.datetime.now().year
total_maior = 0
total_menor = 0

for i in range(1, 8):
    nascimento = int(input(f'Em que ano a {i}ª pessoa nasceu? '))
    idade = ano_atual - nascimento
    if idade < 0:
        print('IDADE INVÁLIDA')
    else:
        if idade >= 18:
            total_maior += 1
        else:
            total_menor += 1

print(f'''
Ao todo existem {total_maior} pessoas maiores de idade.
Além disso, existem {total_menor} pessoas menores de idade.
''')