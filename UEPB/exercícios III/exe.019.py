'''
O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia um conjunto 
indeterminado de temperaturas, e informe ao final a menor e a maior temperatura informada, bem como a média 
das temperaturas
'''
temperaturas = []
soma = 0

for i in range(1, 6):
    temperatura = float(input(f'Digite a {i}º temperatura: '))
    temperaturas.append(temperatura)
    soma += temperatura
maior_temperatura = max(temperaturas)
menor_temperatura = min(temperaturas)
media = soma/i

print(f'A maior temperatura é {maior_temperatura}')
print(f'A menor temperatura é {menor_temperatura}')
print(f'A média das temperaturas é igual a {media:.1f}')