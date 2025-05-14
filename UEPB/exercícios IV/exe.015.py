'''
Uma empresa de pesquisas precisa tabular os resultados da seguinte enquete feita a uma grande quantidade de organizações:
"Qual o melhor Sistema Operacional para uso em servidores?"
As possíveis respostas são:
1- Windows Server

2- Unix

3- Linux

4- Netware

5- Mac OS

6- Outro


Você foi contratado para desenvolver um programa que leia o resultado da enquete e informe ao final o resultado da mesma. O programa deverá ler os valores até ser informado o valor 0, que encerra a entrada dos dados. Não deverão ser aceitos valores além dos válidos para o programa (0 a 6). Os valores referentes a cada uma das opções devem ser armazenados numa lista. Após os dados terem sido completamente informados, o programa deverá calcular o percentual de cada um dos concorrentes e informar o vencedor da enquete. O formato da saída foi dado pela empresa, e é o seguinte:
'''
sistemas = ["Windows Server","Unix","Linux","Netware","Mac OS","Outro"]

votos = [0] * 6 

while True:
    print('''Qual o melhor Sistema Operacional para uso em servidores?

1 - Windows Server
2 - Unix
3 - Linux
4 - Netware
5 - Mac OS
6 - Outro
0 - Encerrar votação''')

    escolha = int(input("Digite o número correspondente à sua escolha: "))

    if escolha == 0:
        break
    elif 1 <= escolha <= 6:
        votos[escolha - 1] += 1
    else:
        print("Opção inválida. Tente novamente.")

total_votos = sum(votos)

for i in range(len(sistemas)):
    percentual = (votos[i] / total_votos)*100 if total_votos > 0 else 0
    print(f"{sistemas[i]:<25} {votos[i]:<7} {percentual:.0f}%")

print(f"Total                      {total_votos}")

mais_votado = max(votos)
indice_vencedor = votos.index(mais_votado)
nome_vencedor = sistemas[indice_vencedor]
porcentagem_vencedor = (mais_votado / total_votos)*100 if total_votos > 0 else 0

print(f"\nO Sistema Operacional mais votado foi o {nome_vencedor}, com {mais_votado} votos, correspondendo a {porcentagem_vencedor:.0f}% dos votos.")