'''
Um posto está vendendo combustíveis com a seguinte tabela de descontos:

Álcool:

até 20 litros, desconto de 3% por litro

acima de 20 litros, desconto de 5% por litro

Gasolina:

até 20 litros, desconto de 4% por litro

acima de 20 litros, desconto de 6% por litro.

Escreva um programa que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte 
forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do 
litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90
'''
tipo_de_combustível = str(input('''
A = Álcool                                
G = Gasolina
Selecione o tipo de combustível: ''')).upper()

# Validação do tipo de combustível
if tipo_de_combustível != 'A' and tipo_de_combustível != 'G':
    print('Tipo de combustível inválido!')
else:
    litros = float(input('Digite quantos litros foram vendidos: '))
    # ÁLCOOL
    if tipo_de_combustível == 'A':
        tipo = 'álcool'
        if litros < 0:
            print('VALOR INVÁLIDO')
        else:
            if litros <= 20:
                valor = (1.9 * 0.97) * litros
            else:
                if litros > 20:
                    valor = (1.9 * 0.95) * litros
    # GASOLINA
    else:
        tipo = 'gasolina'
        if litros < 0:
            print('VALOR INVÁLIDO')
        else:
            if litros <= 20:
                valor = (2.5 * 0.96) * litros
            else:
                if litros > 20:
                    valor = (2.5 * 0.94) * litros

    print(f'Abastecendo {litros} de {tipo}, custará R${valor:.2f}')