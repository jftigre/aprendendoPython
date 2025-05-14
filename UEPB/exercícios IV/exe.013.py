'''
Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. Após isto, 
calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual, e em que mês elas 
ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . )
'''
temperatras = []
meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho','Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
soma_temperaturas = 0

for i in range(12):
    temperatura = float(input(f'Digite a temperatura média de {meses[i]}: '))
    temperatras.append(temperatura)
    soma_temperaturas += temperatura

media_anual = soma_temperaturas / 12

print(f'\nMédia anual de temperatura: {media_anual:.1f}°C')
print('Meses com temperatura acima da média:\n')

for i in range(12):
    if temperatras[i] > media_anual:
        print(f'{meses[i]}: {temperatras[i]:.1f}°C')