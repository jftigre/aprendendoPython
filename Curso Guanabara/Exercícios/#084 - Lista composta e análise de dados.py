'''
Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.
'''
pessoas = []
dados = []

while True:
    nome = input('Nome: ')
    peso = float(input('Peso (Kg): '))
    dados.append(nome)
    dados.append(peso)
    pessoas.append(dados[:])
    dados.clear()

    continuar = ' '
    while continuar not in 'SN':
        continuar = input('Deseja continuar? [S/N]: ').strip().upper()[0]
    if continuar == 'N':
        break

print(f'Foram cadastradas {len(pessoas)} pessoas.')

pesos = [p[1] for p in pessoas]
maior = max(pesos)
menor = min(pesos)

print(f'\nO maior peso foi {maior}Kg. Peso de: ', end='')
for p in pessoas:
    if p[1] == maior:
        print(f'[{p[0]}] ', end='')

print(f'\nO menor peso foi {menor}Kg. Peso de: ', end='')
for p in pessoas:
    if p[1] == menor:
        print(f'[{p[0]}] ', end='')