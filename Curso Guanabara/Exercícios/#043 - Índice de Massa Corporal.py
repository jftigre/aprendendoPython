'''Desenvolva uma lógica que leia o peso e a altura de uma pessoa, 
calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
IMC abaixo de 18,5: Abaixo do Peso
Entre 18,5 e 25: Peso Ideal
25 até 30: Sobrepeso
30 até 40: Obesidade
Acima de 40: Obesidade Mórbida'''

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