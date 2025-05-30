'''
Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá 
perguntar se o usuário quer ou não continuar. No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos. 
'''
pessoas_18 = 0
homens = 0
mulheres_menos_20 = 0

while True:
    idade = int(input('Idade: '))
    
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo[M/F]: ')).strip().upper()[0]
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar ? [S/N]: ')).strip().upper()[0]
    
    if continuar == 'N':
        break
    
    if idade > 18:
        pessoas_18 += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F':
        if idade < 20:
            mulheres_menos_20 += 1
print('-' * 40)
print(f'A) Total de pessoas com mais de 18 anos: {pessoas_18}')
print(f'B) Ao todo temos {homens} homem(ns) cadastrados')
print(f'C) E temos {mulheres_menos_20} mulher(es) com menos de 20 anos')