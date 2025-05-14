'''
Você foi contratado para escrever um algoritmo que calcule quantos pontos fez um time num campeonato de futebol. Para os que não 
conhecem futebol uma vitória vale três pontos, um empate vale 1 ponto e a derrota não vale ponto. A entrada será composta por pares 
de números indicando o resultado de cada jogo. O primeiro número sempre corresponde ao total de gols que o time fez no jogo. A leitura
dos dados será finalizada quando for fornecido um número de gols negativo.
'''
saldo_gols_1 = []
saldo_gols_2 = []

while True:
    gols_1 = int(input('Digite o número de gol(s): '))
    gols_2 = int(input('Digite o número de gol(s) do outro time: '))

    if gols_1 < 0 or gols_2 < 0:
        break

    saldo_gols_1.append(gols_1)
    saldo_gols_2.append(gols_2)

print("\nResultados dos jogos:")
for i in range(len(saldo_gols_1)):
    print(f'{saldo_gols_1[i]} X {saldo_gols_2[i]} no {i+1}º jogo')