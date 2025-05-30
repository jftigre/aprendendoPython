"""
exercício 005:
Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor

1-perguntar o número
2-analisar se o número é
*igual
*maior
*menor
3-aparecer na tela o resultado 

"""
n = int(input('Digite um número: '))
a = n - 1
s = n + 1
print(f'Analisando o valor {n}, o seu antecessor é {a} e o seu sucessor {s}')
