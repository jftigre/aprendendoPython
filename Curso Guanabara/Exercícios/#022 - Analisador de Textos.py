

nome = input('Digite seu nome completo: ')

print('ANALISANDO...')

print(f'Seu nome completo em maiúsculas é {nome.upper()}')

print(f'Seu nome completo em minúsculas é {nome.lower()}')

espacos = nome.count

print(f'Ao todo, {nome} tem {len(nome)} letras')

primeiro = nome.split()[0] #SPLIT separa os nomes apartir de 0
numero_primeeiro = len(primeiro) 

print(f'Seu primeiro nome tem {numero_primeeiro} letras')