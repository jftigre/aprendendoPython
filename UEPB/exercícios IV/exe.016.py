'''
Escreva um programa em Python para encontrar o segundo maior elemento de uma lista com 20 números inteiros.
OBS: todos os valores informados serão de valores diferentes e a solução não deve fazer este tratamento das 
entradas. Além disso, a solução não deve modificar a lista original com a ordem fornecida dos números.
'''
numeros = []

for i in range(1, 21):
    numero = int(input(f"Digite o {i}º número: "))
    numeros.append(numero)

segundo_maior = sorted(set(numeros))[-2]

print(f"\nO segundo maior número da lista é: {segundo_maior}")