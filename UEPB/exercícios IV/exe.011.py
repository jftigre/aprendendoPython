'''
Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine quantos alunos com mais de 13 
anos possuem altura inferior à média de altura desses alunos.
'''
alturas = []
idades = []
soma_alturas = 0
alunos_com_13 = 0

quantidade = int(input('Digite a quantidade de alunos que deseja fazer o programa: ')) 

for i in range(1, quantidade + 1):
    idade = int(input(f'Digite a idade do {i}º aluno: '))
    altura = int(input(f'Digite a altura (cm) do {i}º aluno: '))
    idades.append(idade)
    alturas.append(altura)
    soma_alturas += altura

media_alturas = soma_alturas / quantidade

for i in range(quantidade):
    if idades[i] > 13 and alturas[i] < media_alturas:
        alunos_com_13 += 1

print(f'\nA média das alturas é: {media_alturas:.1f}cm')
print(f'há {alunos_com_13} alunos(s) com mais de 13 anos e altura abaixo da média.')
