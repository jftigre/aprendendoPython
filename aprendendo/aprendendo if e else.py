nota_1 = float(input('Digita a primeira nota: '))
nota_2 = float(input('Digite a segunda nota: '))

media = (nota_1 + nota_2) / 2 

if media >= 7.0:
    print('Você está APROVADO nessa matéria')
else:
    print('Você está REPROVADO nessa matéria')