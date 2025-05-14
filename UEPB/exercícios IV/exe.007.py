'''
Faça um Programa que peça a idade e a altura de 10 pessoas, armazene cada informação na sua respectiva lista. 
Imprima a idade da pessoa que possui maior altura
'''
idades = []
alturas = []

for pessoa in range(1, 4):
    idades.append(int(input(f'Digite a idade da {pessoa}º pessoa: ')))
    alturas.append(int(input(f'Digite a altura(cm) da {pessoa}º pessoa: ')))
posicao_maior_altura = alturas.index(max(alturas))
idade_maior_altura = idades[posicao_maior_altura]

print(f'{idades} \n{alturas} \n{idade_maior_altura}')