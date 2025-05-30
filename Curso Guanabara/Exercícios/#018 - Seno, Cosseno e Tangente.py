import math

num = float(input('Digite o ângulo que você deseja: '))

sen = math.sin(math.radians(num))

cos = math.cos(math.radians(num))

tg = math.tan(math.radians(num))

print(f'''
      
O seno de {num} é igual a {sen:.2f}
O cosseno de {num} é igual a {cos:.2f}
A tangente de {num} é igual a {tg:.2f}
''')