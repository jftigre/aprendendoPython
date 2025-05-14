'''
Escreva um programa em Python para converter um número inteiro em binário de acordo com a representação de 
grandeza com sinal (sinal e magnitude). O programa deve receber um número inteiro e produzir como saída uma 
lista com os bits do número convertido (um bit para cada posição da lista). Além disso deve ser feita a 
verificação se o número pode ser representado, considere uma representação com 8 bits (um para o sinal e 7 
para a magnitude).
'''
# como a gente usa 8 bits, 1 é pro sinal e 7 são pra magnitude
# com 7 bits, o maior número que dá pra representar é 127 (porque 1111111 em binário = 127)
numero = int(input("Digite um número inteiro entre -127 e 127: "))

if numero < -127 or numero > 127:
    print("Erro: número fora do intervalo representável com 8 bits.")
else:
    sinal = 0 if numero >= 0 else 1
    magnitude = format(abs(numero), '07b')
    representacao = str(sinal) + magnitude
    bits = [int(bit) for bit in representacao]
    print(f"Representação em sinal e magnitude: {bits}")