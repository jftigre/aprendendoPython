'''
A série de FETUCCINE é gerada da seguinte forma: os dois primeiros termos são fornecidos pelo usuário; a partir
daí, os termos são gerados com a soma ou subtração dos dois termos anteriores, ou seja:

Faça um programa em Python para mostrar os N primeiros termos da série de FETUCCINE, sabendo-se que para 
existir esta série serão necessários pelo menos três termos.
'''
num_1 = int(input("Digite o primeiro número: "))
num_2 = int(input("Digite o segundo número: "))
n_vezes = int(input("Digite quantos termos deseja ver: "))

print(num_1, end=" → ")
print(num_2, end=" → ")

anterior = num_1
atual = num_2

for i in range(3, n_vezes + 1):
    if i % 2 == 0:
        proximo = atual + anterior
    else:
        proximo = atual - anterior
    
    print(proximo, end=" → " if i < n_vezes else "\n")

    anterior = atual
    atual = proximo