from datetime import datetime

ano_atual = datetime.now().year

nascimento = int(input('Digite o ano que você nasceu: '))

idade = ano_atual - nascimento  # Corrigindo a ordem para calcular a idade corretamente

if idade == 18:
    print('Você deve se alistar este ano!')
elif idade < 18:
    faltam = 18 - idade  # Calcula quantos anos faltam
    print(f'Ainda não está na hora de se alistar. Faltam {faltam} ano(s).')
else:
    passou_tempo = idade - 18  # Calcula quantos anos passaram
    print(f'Você passou da hora de alistar-se. Passaram-se {passou_tempo} ano(s).')
