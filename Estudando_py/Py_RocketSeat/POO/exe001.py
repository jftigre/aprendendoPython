class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def Apresentacao(self):
        print(f"Carro: {self.modelo}\nMarca: {self.marca}\nAno: {self.ano}")

    def Trancar(self):
        print("Carro Trancado!")
        
    def Destrancar(self):
        print("Carro destrancado!")

carro1 = Carro(marca= "RAM", modelo= "Rampage", ano= "2025/26")
carro1.Apresentacao()
carro2 = Carro(marca="Renault", modelo= "Logan", ano= "2017")
carro2.Apresentacao()