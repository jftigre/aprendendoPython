'''Faça um programa que calcule a soma entre todos os números que são múltiplos de
três e que se encontram no intervalo de 1 até 500.'''

soma = 0 # Variável para armazenar a soma dos valores
cont = 0 # Variável para contar quantos números atendem à condição

for i in range(1, 501, 2):
    if i % 3 == 0:
        soma = soma + i
        cont = cont + 1
print(f'A soma de todos os {cont} valores solicitados foi de {soma}')
