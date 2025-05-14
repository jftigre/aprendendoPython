'''
Tendo como dados de entrada a altura e o sexo de uma pessoa, construa um algoritmo que calcule seu peso 
ideal, utilizando as seguintes fórmulas: para homens: (72.7*h) – 58 e para mulheres: (62.1*h) - 44.7 (h = altura)
'''


peso = float(input('Qual o peso ? (Kg): '))
altura = float(input('Qual a altura ? (m) '))
imc = peso / (altura**2)

if imc < 18.5:
    print(f'O IMC é {imc:.2f} e indica que está ABAIXO DO PESO IDEAL')
else:
    if 18.5 <= imc < 25:
        print(f'O IMC é {imc:.2f} e indica que está no PESO IDEAL')
    else:
        if 25 <= imc < 30:
            print(f'O IMC é {imc:.2f} e indica que está com SOBREPESO')
        else:
            if 30 <= imc < 40:
                print(f'O IMC é {imc:.2f} e indica que está com OBESIDADE')
            else:
                if imc > 40:
                    print(f'O IMC é {imc:.2f} e indica que está com OBESIDADE MÓRBIDA')