'''
exercício 006:
Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada

1 - receber o número
2 - multiplica por 2
3 - multiplica por 3
4 - eleva com ** por 1/2
5 - print disso tudo

'''
n = int(input('Digite um número: '))
d = n*2
t = n*3
r = n**(1/2)
print(f'O dobro de {n} é {d}\nO triplo de {n} é {t}\nA raiz quadrada de {n} é {r}')

