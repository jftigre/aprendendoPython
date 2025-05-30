'''Faça um programa que leia o peso de cinco pessoas. 
No final, mostre qual foi o maior e o menor peso lidos.'''

pesos = []

for i in range(1, 6):
    peso = float(input(f'Digite o peso da {i}ª pessoa: '))
    pesos.append(peso)

maior_peso = max(pesos)
menor_peso = min(pesos)

print(f''' 
Os pesos foram: {pesos} ' ' 
O maior peso foi igual a {maior_peso}
O menor peso foi igual a {menor_peso}
''')