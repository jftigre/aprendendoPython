import moeda

num = float(input('Digite um valor: '))
taxa_aumento = float(input('Digite a taxa de aumento: '))
taxa_desconto = float(input('Digite a taxa de desconto: '))

print('\n')
print(f'Aumentando {taxa_aumento}%: {moeda.aumentar(num, taxa_aumento):.2f}')
print(f'Diminuindo {taxa_desconto}%: {moeda.diminuir(num, taxa_desconto):.2f}')
print(f'Dobro: {moeda.dobro(num):.2f}')
print(f'Metade: {moeda.metade(num):.2f}')