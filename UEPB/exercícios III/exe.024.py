'''
O cardápio de uma lanchonete é o seguinte:

Especificação Código Preço

Cachorro Quente 100 R$ 1,20

Bauru Simples 101 R$ 1,30

Bauru com ovo 102 R$ 1,50

Hambúrguer 103 R$ 1,20

Cheeseburguer 104 R$ 1,30

Refrigerante 105 R$ 1,00

Faça um programa que leia o código dos itens pedidos e as quantidades desejadas. Calcule e mostre o valor a ser
pago por item (preço * quantidade) e o total geral do pedido. Considere que o cliente deve informar quando o 
pedido deve ser encerrado.
'''
print("""
LANCHONETE TUDODEBOM
      
Especificação         Código   Preço
--------------------------------------
Cachorro Quente       100      R$ 1,20
Bauru Simples         101      R$ 1,30
Bauru com ovo         102      R$ 1,50
Hambúrguer            103      R$ 1,20
Cheeseburguer         104      R$ 1,30
Refrigerante          105      R$ 1,00
""")
valor = 0
total_geral = 0
especificacao = ' '
nomes = []
quantidades = []
subtotais = []


while True:
    especificacao = ' '
    pedido = int(input('Digite o código do produto: '))
    quantidade = int(input('Digite a quantidade: '))

    if pedido == 100:
        valor += 1.2 * quantidade
        especificacao += 'Cachorro Quente'
    else:
        if pedido == 101:
            valor += 1.3 *quantidade
            especificacao += 'Bauru Simples'
        else:
            if pedido == 102:
             valor += 1.5 *quantidade
             especificacao += 'Bauru com ovo'
            else:
                if pedido == 103:
                    valor += 1.2 * quantidade
                    especificacao += 'Hambúrguer'
                else:
                    if pedido == 104:
                        valor += 1.3 * quantidade
                        especificacao += 'Cheeseburguer'
                    else:
                        if pedido == 105:
                            valor += 1 * quantidade
                            especificacao += 'Refrigerante'
                        else:
                            print('Valor inválido')
    nomes.append(especificacao)
    quantidades.append(quantidade)
    subtotais.append(valor)
    total_geral += valor

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar ? [S/N]: ')).strip().upper()[0]
    if continuar == 'N':
        break

print("\nResumo do pedido:")
print("------------------------------------------")
for i in range(len(nomes)):
    print(f"{nomes[i]:<20} x{quantidades[i]:<3} - R$ {subtotais[i]:.2f}")
print("------------------------------------------")
print(f"Total a pagar: R$ {total_geral:.2f}")