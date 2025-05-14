'''
Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se a média de 
idade da turma varia entre 0 e 25, 26 e 60 e maior que 60; e então, dizer se a turma é jovem, adulta ou 
idosa, conforme a média calculada
'''
somador = 0

for i in range(1, 6):
    idade = int(input(f'Digite a idade da {i}ª pessoa: '))
    somador += idade
media = somador/i
if 0<= media <= 25:
    turma = 'jovem'
else:
    if 25 < media <= 60:
        turma = 'adulta'
    else:
        if media > 60:
            turma = 'idosa'

print(f'a turma é igual a: {turma}')