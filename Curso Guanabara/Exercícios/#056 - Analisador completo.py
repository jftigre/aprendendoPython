'''Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa,
mostre: a média de idade do grupo, qual é o nome do homem mais velho e 
quantas mulheres têm menos de 20 anos.'''

soma_idade = 0
idade_homem_velho = 0
homem_velho = ''
conta_mulheres_menor_20 = 0

for i in range(1, 5):
    print(f'----- {i}ª PESSOA -----')
    nome = str(input(f'NOME: '))
    idade = int(input(f'IDADE: '))
    sexo = str(input(f'SEXO[M/F]: '))
    
    soma_idade += idade

    #Homem mais velho
    if sexo.upper() == 'M' and idade > idade_homem_velho:
        idade_homem_velho = idade
        homem_velho = nome

    #Contar mulheres 20 anos
    if sexo.upper() == 'F' and idade < 20:
        conta_mulheres_menor_20 += 1

#Média de idade
media = soma_idade / 4

print(f'A média de idade é {media}')
print(f'O homem mais velho é {homem_velho}')
print(f'O número de mulheres com menos de 20 anos é {conta_mulheres_menor_20}')