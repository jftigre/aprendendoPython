'''
Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.
'''
boletim = {}

boletim['nome'] = str(input('Nome do aluno(a): '))
boletim['nota'] = float(input(f'Nota de {boletim["nome"]}: '))

if 7 <= boletim['nota'] <= 10 :
    situacao = 'APROVADO'
else:
    if 0 < boletim['nota'] < 5:
        situacao = 'REPROVADO'
    else:
        situacao = 'RECUPERAÇÃO'

for k, v in boletim.items():
    print(f'{k} é igual a {v}')