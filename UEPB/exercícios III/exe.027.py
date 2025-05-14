'''
Faça um programa para validar o login e a senha de um usuário. Caso o usuário informe algum valor inválido 
informar o erro e pedir novamente os dados. A leitura dos dados deve ser encerrada quando o usuário digitar 3 
vezes um valor inválido (login ou senha). Considere o login válido como "kezia" e a senha como "123".
'''
login = str(input('Digite o nome de usuário: '))
senha = int(input('Digite a senha: '))

if login == 'kezia' and senha == 123:
    print('Login realizado com sucesso!')
else:
    print('Dados inválidos!')
    
    for i in range(1, 3):
        login_1 = str(input('Digite o nome de usuário novamente: '))
        senha_1 = int(input('Digite a senha novamente: '))

        if login_1 == 'kezia' and senha_1 == 123:
            print('Login realizado')
            break
        else:
            print('atingiu o máximo de tentativas!')
            