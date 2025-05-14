''''
Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média 
alcançada por aluno e apresentar:

A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;

A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;

A mensagem "Aprovado com Distinção", se a média for igual a 10.

'''

nota_1 = float(input('Digite a primeira nota: '))
nota_2 = float(input('Digite a segunda nota: '))
nota_3 = float(input('Digite a terceira nota: '))
media = (nota_1 + nota_2 + nota_3)/3
 

if media == 10:
    mensagem = ('Parabéns, você foi aprovado com louvor !!! Alcançou a média máxima')
else:
    if media >= 7:
        mensagem = ('Parabéns, você foi aprovado !!!')
    else:
        if media < 7:
            mensagem = ('Reprovado, estude mais')
        else:
            print('Valor Inválido !!!')
print(f'{mensagem}. A sua média foi igual a {media:.1f}')
