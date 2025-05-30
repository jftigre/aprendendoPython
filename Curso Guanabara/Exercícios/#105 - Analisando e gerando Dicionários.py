'''
Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:

Quantidade de notas
A maior nota
A menor nota
A média da turma
A situação (opcional)

Adicione também as docstrings dessa função para consulta pelo desenvolvedor.
'''
def notas(*notas, situacao=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param notas: uma ou mais notas dos alunos (aceita várias).
    :param situacao: valor opcional, indicando se deve ou não adicionar a situação.
    :return: dicionário com várias informações sobre a situação da turma.
    """
    respostas = {}
    respostas['total'] = len(notas)
    respostas['maior'] = max(notas)
    respostas['menor'] = min(notas)
    respostas['média'] = sum(notas) / len(notas)
    
    if situacao:
        if respostas['média'] >= 7:
            respostas['situação'] = 'Boa'
        elif 5 <= respostas['média'] < 7:
            respostas['situação'] = 'Crítica'
        else:
            respostas['situação'] = 'Totalmente lascado'
    return respostas

# PROGRAMA PRINCIPAL
resposta = notas(2.4, 7.7, 6.1, 9.5, 3.8, situacao=True)
print(resposta)