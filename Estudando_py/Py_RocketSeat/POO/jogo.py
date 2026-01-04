# Personagem: classe mae
# Heroi: controlado pelo usuario
# Inimigo: adversario do usuario

class Personagem:

    def __init__(self, nome, vida, nivel):
        self.__nome = nome
        self.__vida = vida
        self.__nivel = nivel

    def get_nome(self):
        return self.__nome

    def get_vida(self):
        return self.__vida

    def get_nivel(self):
        return self.__nivel
    
    def exibir_informacoes(self):
        return f"\nNome: {self.get_nome()}\nVida: {self.get_vida()}\nNivel: {self.get_nivel()}\n"
    
class Heroi(Personagem):
    def __init__(self, nome, vida, nivel, habilidade):
        super().__init__(nome, vida, nivel)
        self.__habilidade = habilidade

    def get_habilidade(self):
        return self.__habilidade
    
    def exibir_informacoes(self):
        return f"\n{super().exibir_informacoes()}Habilidade: {self.get_habilidade()}"
    
class Inimigo(Personagem):
    def __init__(self, nome, vida, nivel, tipo):
        super().__init__(nome, vida, nivel)
        self.__tipo = tipo

    def get_tipo(self):
        return self.__tipo

    def exibir_informacoes(self):
        return f"{super().exibir_informacoes()}Tipo: {self.get_tipo()}\n"


heroi = Heroi(nome="Joao", vida= 100, nivel= 3, habilidade="Peido fedido")
print(heroi.exibir_informacoes())
inimigo = Inimigo(nome="Rebeca", vida= 100, nivel= 2, tipo="Risada")
print(inimigo.exibir_informacoes())