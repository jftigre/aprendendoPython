'''
EXERCÍCIO 11:
Faça um programa que leia a largura e a altura de uma parede em metros. 
Calcule a sua área e a quantidade de tinta necessária para pinta-la, sabendo 
que cada litro de tinta pinta uma área de 2m2

1 - receber a largura e altura, em metros
2 - calcular a área
3 - quantidade de tinta = 2*metragem


'''

largura = float(input('Qual a largura da parede em metros ? '))

altura = float(input('Qual a altura da parede em metros ? '))

area = altura*largura

tinta = area/2

print(f'''
Sua parede tem: 

dimensão de {largura}x{altura}

área  de {area:.2f}m²

para pintar essa parede, você precisará de {tinta:.2f}l de tinta
      
 ''')

