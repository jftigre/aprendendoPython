'''
Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições
'''

def voto(data):
    from datetime import date
    anos = date.today().year - nascimento
    
    if 0 <= anos < 15:
        situacao = 'NEGADO'
    else:
        if 18 <= anos <= 65:
            situacao = 'OBRIGATÓRIO'
        else:
            situacao = 'OPCIONAL'
    print(f'Com {anos} anos o seu voto é {situacao}')


nascimento = int(input('Digite o ano de nascimento: '))
voto(nascimento)