
frase = str(input('Digite uma frase: ')).strip().upper()

quantas_vezes = frase.count('A') + 1
print(f'A letra A aparece {quantas_vezes} vezes na frase')

posicao_letra = frase.find('A') + 1
print((f'A primeira letra A apareceu na posição {posicao_letra}'))

posicao_final_letra = frase.rfind('A')
print(f'A última letra A aparece na posição {posicao_final_letra}')