'''
Peça ao usuário para digitar números inteiros até digitar 0.
Armazene todos sem repetir valores, e ao final mostre a lista em ordem crescente.
'''
'''continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar ? [S/N]: ')).strip().upper()[0]
    
    if continuar == 'N':
    break'''

numeros = []

while True:

    numero = int(input('Digite um número: '))
    if numero == 0:
        break
    if numero not in numeros:
        numeros.append(numero)
        
print(f'acabou o programa\nA lista de números foi {sorted(numeros)} ')