'''
exerccício 008:
Escreva um programa que leia um valor em metros e o exiba 
convertido em centímetros e milímetros.

1 - receba o número
2 - divida o número por 100 e 1000
3 - exiba o resultado

'''
n = float(input('Uma distância em metros: '))
cm = n * 100
mm = n * 1000
km = n/1000
print(f'''
{n}m equivale a:
- {cm}cm
- {mm}mm
- {km}km
''')


        