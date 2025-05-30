'''A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento 
de um atleta e mostre sua categoria, de acordo com a idade:
Até 9 anos: MIRIM
Até 14 anos: INFANTIL
Até 19 anos: JÚNIOR
Até 25 anos: SÊNIOR
Acima de 25 anos: MASTER'''

from datetime import datetime

ano_nascimento = int(input('Digite o ano do nascimento: '))

ano_atual = datetime.now().year  # Obtém o ano atual
idade = ano_atual - ano_nascimento

if idade <= 0:
    print('DATA DE NASCIMENTO INVÁLIDA')
else:
    if idade <= 9:
        print(f'A categoria do atleta com {idade} anos é MIRIM')
    else:
        if idade <= 14:
            print(f'A categoria do atleta com {idade} anos é INFANTIL')
        else:
            if idade <= 19:
                print(f'A categoria do atleta com {idade} anos é JÚNIOR')
            else:
                if idade <= 25:
                    print(f'A categoria do atleta com {idade} anos é SÊNIOR')
                else:
                    print(f'A categoria do atleta com {idade} anos é MASTER')
