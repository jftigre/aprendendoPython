'''
Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:

"Telefonou para a vítima?"

"Esteve no local do crime?"

"Mora perto da vítima?"

"Devia para a vítima?"

"Já trabalhou com a vítima?" 
O programa deve no final emitir uma classificação sobre a participação da 
pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como 
"Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como 
"Inocente".
'''
soma = 0

for i in range(1):
    print('RESPONDA COM S(SIM) OU N(NÃO)')
    tele = str(input('Telefonou para a vítima: ')).upper()
    local = str(input('Esteve no local do crime: ')).upper()
    perto = str(input('Mora perto da vítima: ')).upper()
    devia = str(input('Devia para a vítima: ')).upper()
    trabalhou = str(input('Já trabalhou com a vítima: ')).upper()

    if tele == 'S':
        soma += 1
    if local == 'S':
        soma += 1
    if perto == 'S':
        soma += 1
    if devia == 'S':
        soma += 1
    if trabalhou == 'S':
        soma += 1
    else:
        print('Valor inválido')
if soma == 2:
    situacao = ('SUSPEITA')
else:
    if 3 <= soma <= 4:
        situacao = ('CÚMPLICE')
    else:
        if soma == 5:
            situacao = ('ASSASSINO')
print(f'A situação do investigado é {situacao}, resultando em {soma} coincidências')
