# Testando várias funções 'is' em Python

n = input('Digite algo: ')

print('É alfabético?', n.isalpha())      # Verifica se a string é alfabética
print('É numérico?', n.isdigit())        # Verifica se a string é numérica
print('Tem apenas espaços?', n.isspace())  # Verifica se a string contém apenas espaços
print('É minúsculo?', n.islower())      # Verifica se todos os caracteres são minúsculos
print('É maiúsculo?', n.isupper())      # Verifica se todos os caracteres são maiúsculos
print('Tem título?', n.istitle())       # Verifica se a string tem formato de título
print('É decimal?', n.isdecimal())      # Verifica se a string é decimal
print('É numérica (incluindo outros sistemas)?', n.isnumeric())  # Verifica se a string é numérica (inclusivo sistemas numéricos diferentes)
print('É um identificador válido?', n.isidentifier())  # Verifica se a string pode ser um identificador válido em Python
