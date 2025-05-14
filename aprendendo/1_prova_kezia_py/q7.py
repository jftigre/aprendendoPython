'''
Peça números inteiros ao usuário até que ele digite um valor negativo.
Armazene todos os valores em uma lista.
Depois:
– Mostre quantos números foram digitados
– Mostre a média dos valores
– Mostre apenas os números que são maiores que a média
'''

numeros = []

while True:
    numero = int(input('Digite um número (negativo para parar): '))
    if numero < 0:
        break
    numeros.append(numero)

quantidade = len(numeros)
media = sum(numeros) / quantidade

# Agora sim, filtrar os maiores que a média
numeros_maior_media = []

for num in numeros:
    if num > media:
        numeros_maior_media.append(num)

print(f'\nQuantidade de números digitados: {quantidade}')
print(f'Média dos valores: {media:.2f}')
print(f'Números maiores que a média: {numeros_maior_media}')
