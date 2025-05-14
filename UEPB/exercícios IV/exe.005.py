'''
Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene numa lista a média de cada aluno, 
imprima o número de alunos com média maior ou igual a 7.0.
'''
medias = []
aprovados = 0
soma = 0

for aluno in range(1, 11):
    soma = 0
    for nota in range(1, 5): 
        valor = float(input(f'Digite a {nota}ª nota do {aluno}º aluno: '))
        soma += valor
    media = soma / 4
    medias.append(media)

    if media >= 7:
        aprovados += 1

print('As médias dos alunos:')
for i, m in enumerate(medias,):
    print(f'Aluno {i}: média = {m:.1f}')

print(f'\nNúmero de alunos com média maior ou igual a 7.0: {aprovados}')