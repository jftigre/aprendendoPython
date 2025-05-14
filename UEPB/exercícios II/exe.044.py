'''
Elabore um algoritmo que dada a idade de um nadador classifica-o em uma das seguintes categorias: 
infantil A = 5 - 7 anos; infantil B = 8-10 anos; juvenil A = 11-13 anos; juvenil B = 14-17 anos; 
adulto = maiores de 18 anos.
'''
idade = int(input('Digite a idade do nadador: '))

if idade < 0:
    print('VALOR INVÁLIDO')
else:
    if 5 <= idade <= 7:
        categoria = 'INFANTIL A'
    else:
        if 8 <= idade <= 10:
            categoria = 'INFANTIL B'
        else:
            if 11 <= idade <= 13:
                categoria = 'JUVENIL A'
            else:
                if 14 <= idade <= 17:
                    categoria = 'JUVENIL B'
                else:
                    if idade >= 18:
                        categoria = 'ADULTO'

    print(f'O nadador tem {idade} anos e pertence à categoria: {categoria}')

