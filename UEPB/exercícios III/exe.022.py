'''
A prefeitura de uma cidade fez uma pesquisa entre seus habitantes, coletando dados sobre o salário e número de filhos. 
A prefeitura deseja saber:

a) Média do salário da população;

b) Média do número de filhos;

c) Maior salário;

d) Percentual de pessoas com salário até R$250,00.

Desenvolver um programa para calcular e escrever o que foi pedido nos itens a, b, c e d. O final da leitura de dados se 
dará com a entrada de um salário negativo
'''

soma_salario = 0
soma_filhos = 0
lista_salario = []
soma_salario250 = 0
total_pessoas = 0

while True:
    salario = float(input('Digite o salário: '))
    if salario < 0:
        break
    filhos = int(input('Digite o número de filhos: '))

    soma_salario += salario
    soma_filhos += filhos
    lista_salario.append(salario)
    total_pessoas += 1

    if salario <= 250:
        soma_salario250 += 1  

if total_pessoas > 0:
    media_salario = soma_salario / total_pessoas
    media_filhos = soma_filhos / total_pessoas
    maior_salario = max(lista_salario)
    percentual_250 = (soma_salario250 / total_pessoas) * 100
    
    print(f'''
A média de filhos é {media_filhos:.2f}
A média salarial é R${media_salario:.2f}
O maior salário é R${maior_salario:.2f}
O percentual de pessoas com salário até R$250,00 é {percentual_250:.2f}%
''')

else:
    print('Dados inválidos!')