'''
Cada espectador de um cinema respondeu a um questionário no qual constava sua idade e a sua opinião 
em relação ao filme: ótimo - 3, bom - 2, regular - 1. Faça um programa que receba a idade e a opinião 
de 15 espectadores, calcule e imprima:

a) A média das idades das pessoas que responderam ótimo;

b) A quantidade de pessoas que responderam regular;

c) A porcentagem de pessoas que responderam bom entre todos os espectadores analisados.
'''
idades = []
opinioes = []

for i in range(1, 16):
    idade = int(input(f'A idade do {i}ª espectador: '))
    opiniao = int(input('''[1] REGULAR \n[2] BOM \n[3] ÓTIMO \nDigite a sua opinião: '''))

    idades.append(idade)
    opinioes.append(opiniao)

soma_idades_otimo = 0
cont_otimo = 0
qtd_regular = 0
qtd_bom = 0

for j in range(len(opinioes)):
    if opinioes[j] == 3:
        soma_idades_otimo += idades[j]
        cont_otimo += 1

    if opinioes[j] == 2:
        qtd_bom += 1

    if opinioes[j] == 1:
        qtd_regular += 1

if cont_otimo > 0:
    media_otimo = soma_idades_otimo / cont_otimo
else:
    media_otimo = 0

porcentagem_bom = (qtd_bom / len(opinioes)) * 100

print(f'A média das idades de quem respondeu ÓTIMO foi {media_otimo:.1f}')
print(f'A quantidade de pessoas que responderam REGULAR foi {qtd_regular}')
print(f'a porcentagem de pessoas que responderam BOM foi {porcentagem_bom:.1f}%')

