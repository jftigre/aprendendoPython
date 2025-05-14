'''
Escreva um programa que calcula a média de 30 alunos e informa a situação (reprovado, 
aprovado ou recuperação).
'''
soma_notas = 0

for i in range(1, 31):
    nota = float(input(f'Digite a nota do {i}ª aluno: '))
    soma_notas += nota
media = soma_notas/30

if media >= 7:
    situacao = ('APROVADO')
else:
    if 4 <= media < 7:
        situacao = ('RECUPERAÇÃO')
    else:
        if media < 4:
            situacao = ('REPROVADO')
print(f'A média da turma foi igual a {media} pontos e a situação geral foi {situacao}')