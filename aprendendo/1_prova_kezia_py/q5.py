'''
Peça ao usuário para digitar 10 números.
Armazene-os em uma lista na ordem contrária da entrada (sem usar reverse() nem [::-1]).
Ou seja, o último número digitado deve ser o primeiro da lista.
'''

numeros = []

for i in range(1, 5):
    numero = int(input(f'Digite o {i}ª número: '))
    numeros.insert(0, numero)

print(f'A ordem inversa é: {numeros} ')