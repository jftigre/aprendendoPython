import moeda

num = float(input('Digite um valor: '))
taxa_aumento = float(input('Digite a taxa de aumento: '))
taxa_desconto = float(input('Digite a taxa de desconto: '))

print('\n')
print(f'Aumentando {taxa_aumento}%: {moeda.moeda(moeda.aumentar(num, taxa_aumento))}')
print(f'Diminuindo {taxa_desconto}%: {moeda.moeda(moeda.diminuir(num, taxa_desconto))}')
print(f'Dobro: {moeda.moeda(moeda.dobro(num))}')
print(f'Metade: {moeda.moeda(moeda.metade(num))}')