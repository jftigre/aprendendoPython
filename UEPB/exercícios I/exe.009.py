'''
Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Farenheit.
'''

celsius = float(input('Digite a temperatura em Celsius: '))
fahrenheit = ((celsius * (9/5))+32)

print(f'{celsius}°C equivale a {fahrenheit}F')