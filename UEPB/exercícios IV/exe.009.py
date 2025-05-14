'''
Faça um Programa que leia duas listas com 10 elementos cada. Gere uma terceira lista de 20 elementos, cujos valores 
deverão ser compostos pelos elementos intercalados das duas outras listas.
'''
lista_1 = []
lista_2 = []

for i in range(1, 21):
    lista_1.append(int(input(f'Digite o {i}º número da lista 1: ')))
for i in range(1, 21):
    lista_2.append(int(input(f'Digite o {i}º número da lista 2: ')))
    nova_lista_1 = lista_1[::2]
    nova_lista_2 = lista_2[::2]
    soma_das_listas = nova_lista_1 + nova_lista_2

print(f'primeira lista: {lista_1} e {nova_lista_1} \nsegunda lista: {lista_2} e{nova_lista_2} \n{soma_das_listas}')