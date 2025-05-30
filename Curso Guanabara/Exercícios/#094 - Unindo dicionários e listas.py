'''
Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: 
A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média
'''
lista_dados = []
idades = 0

while True:
    dados = {}
    dados['NOME'] = str(input('Nome: '))
    
    while True:
        dados['SEXO'] = str(input('Sexo [M/F]: ')).strip().upper()[0]
        if dados['SEXO'] in 'MF':
            break
        print('ERRO! Por favor, somente M ou F.')
    
    dados['idade'] = int(input('Idade: '))
    idades += dados['idade']
    lista_dados.append(dados.copy())

    while True:
        continuar = str(input('Deseja continuar [S/N]: ')).strip().upper()[0]
        if continuar in 'SN':
            break
        print('ERRO! Por favor, somente S ou N.')
    if continuar == 'N':
        break

print('-='*25)

# A) Total de pessoas
print(f'A) Total de pessoas cadastradas: {len(lista_dados)}')

# B) Média de idade
media_idade = idades / len(lista_dados)
print(f'B) Média de idade: {media_idade:.2f}')

# C) Lista de mulheres
mulheres = [pessoa['NOME'] for pessoa in lista_dados if pessoa['SEXO'] == 'F']
print(f'C) Mulheres cadastradas: {mulheres}')

# D) Pessoas com idade acima da média
acima_media = [pessoa for pessoa in lista_dados if pessoa['idade'] > media_idade]
print('D) Pessoas com idade acima da média:')
for pessoa in acima_media:
    print(f"   Nome: {pessoa['NOME']}, Idade: {pessoa['idade']}, Sexo: {pessoa['SEXO']}")