
nome = input('Digite seu nome completo: ').strip()

primeiro_nome = nome.split()[0]

ultimo_nome = nome.split()[-1] #para pegar o ultimo termo só colocar -1

print(f'''
Muito prazer em te conhecer! 
Seu primeiro nome é {primeiro_nome}
Seu último nome é {ultimo_nome}

''')
