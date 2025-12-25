class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo = 0


    def depositar(self,valor):

        if valor > 0:
            self.saldo += valor
            print(f"R${valor} depositado com sucesso! \nSaldo: R${self.saldo}")
        else:
            print("Valor inválido!")
    
    def sacar(self,valor):

        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            print(f"R${valor} sacado com sucesso! \nSaldo: R${self.saldo}")
        else:
            print("Valor inválido!")
    
    def exibir_saldo(self):
        print(f"Saldo da conta: R${self.saldo}")
    
cliente1 = ContaBancaria(titular="Joao", saldo=0)
cliente1.exibir_saldo()
cliente1.depositar(10000)
cliente1.sacar(300)
