'''
Faça um programa que receba o valor de uma dívida e mostre uma tabela com os seguintes dados: valor da dívida, 
valor dos juros, quantidade de parcelas e valor da parcela.

Os juros e a quantidade de parcelas seguem a tabela abaixo:

Quantidade de Parcelas % de Juros sobre o valor inicial da dívida
'''
print('''
A dívida será quitada de acordo com essa tabela:
      
Parcelas   % Juros
--------   --------
   1          0
   3          10
   6          15
''')

divida = float(input('Digite o valor da dívida: '))
parcelas = int(input('Digite a quantidade de parcelas: '))

if parcelas == 1:
    quita = divida
else:
    if parcelas == 3:
        juros = 10
        quita = divida*(1+(juros/100))
        parcela = quita/3
    else:
        if parcelas == 6:
            juros = 15
            quita = divida*(1+(juros/100))
            parcela = quita/6
print(f'O valor total é R${quita:.1f}, com parcelas de R${parcela:.1f} à juros de {juros}%')