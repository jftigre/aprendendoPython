'''
Peça o nome e a nota de 5 alunos (um de cada vez) e armazene essas informações. No final, mostre uma lista apenas com os nomes dos alunos que tiraram nota igual ou maior que 7.0.
'''

notas = []
nomes = []

for i in range(1, 6):
    nota = float(input(f'Digite a nota do {i}ª aluno: '))
    nome = str(input(f'Digite o nome do {i}ª aluno: '))

    if nota >= 7:
        notas.append(nota)
        nomes.append(nome)

print(f'notas acima da média: {notas}')
print(f'nomes acima da média: {nomes}')