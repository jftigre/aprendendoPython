'''
Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.
'''
def aumentar(valor, taxa):
    return valor * (1 +(taxa/100))

def diminuir(valor, taxa):
    return valor * (1 - (taxa/100))

def dobro(valor):
    return valor*2

def metade(valor):
    return valor/2

def moeda(valor = 0, moeda = 'R$'):
    return f'{moeda}{valor}'.replace('.', ',')