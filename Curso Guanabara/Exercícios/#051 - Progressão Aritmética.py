'''Desenvolva um programa que leia o primeiro termo e a razão de uma PA. 
No final, mostre os 10 primeiros termos dessa progressão.'''

a1 = float(input('Digite o primerio termo da PA: '))
r = float(input('Digite a razão da PA: '))

for i in range(1, 11):
    an = a1 + (i - 1) * r
    print(an)