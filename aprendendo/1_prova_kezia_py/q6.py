'''
Peça ao usuário para digitar 5 números para a primeira lista e depois mais 5 números para uma segunda lista.
Crie uma terceira lista que contenha apenas os números que aparecem nas duas listas (sem repetições).
Ao final, mostre as três listas.
'''
lista_1 = []
lista_2 = []
lista_3 = []

for i in range(1, 4):
   numero = (int(input(f'Digite o {i}ª número: ')))
   lista_1.append(numero)
for i in range(1, 4):
   numero = (int(input(f'Digite o {i}ª número: ')))
   lista_2.append(numero)
for numero in lista_1:
    if numero in lista_2 and numero not in lista_3:
        lista_3.append(numero)  

print(f'lista 1:{lista_1}')
print(f'lista 2:{lista_2}')
print(f'lista 3:{lista_3}')