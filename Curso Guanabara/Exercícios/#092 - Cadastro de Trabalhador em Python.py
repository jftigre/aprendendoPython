'''
Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
'''
from datetime import datetime

dados = {}

dados['nome'] = str(input('Digite o nome: '))
ano_de_nascimento = int(input(f'Ano de nascimento do {dados["nome"]}: '))
dados['idade'] = (datetime.now().year - ano_de_nascimento) 
dados['CTPS'] = int(input('Número da carteira de trabalho (0 não tem): '))
if dados['CTPS'] != 0:
    dados['ano de contratação'] = int(input('Ano de contratação: '))
    dados['salário'] = float(input('Digite o valor do saçário: R$'))
print(' ')
for k, v in dados.items():
    print(f'-{k} é igual a {v}')