'''
Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a entrada de 
dados quando for informadoum valor igual a -1 (que não deve ser armazenado). Após esta entrada de dados, faça:

a. Mostre a quantidade de valores que foram lidos;

b. Exiba todos os valores na ordem em que foram informados

c. Exiba todos os valores na ordem inversa à que foram informados

d. Calcule e mostre a soma dos valores;

e. Calcule e mostre a média dos valores;

f. Calcule e mostre a quantidade de valores acima da média calculada;

g. Calcule e mostre a quantidade de valores abaixo de sete;

h. Encerre o programa com uma mensagem.
'''
notas = []
while True:
    nota = float(input("Digite uma nota (-1 para encerrar): "))
    if nota == -1:
        break
    notas.append(nota)

quantidade = len(notas)
soma = sum(notas)
media = soma / quantidade if quantidade > 0 else 0
acima_media = sum(1 for n in notas if n > media)
abaixo_sete = sum(1 for n in notas if n < 7)
notas_invertidas = nota[::-1]

print(f'\nQuantidade de valores lidos: {quantidade}')
print(f'List das valores: {notas}')
print(f'Valores na ordem decrescente: {notas_invertidas}')
print(f'Soma dos valores: {soma}')
print(f'A média fo: {media:.1f}')
print(f'Valores acima da média: {acima_media}')
print(f'Valores abaixo de sete: {abaixo_sete}') 
