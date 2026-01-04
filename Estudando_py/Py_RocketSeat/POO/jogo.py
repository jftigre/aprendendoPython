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
    
    def receber_ataque(self, dano):
        self.__vida -= dano

        if self.__vida < 0:
            self.__vida = 0 

    def ataque(self, alvo):
        dano = self.__nivel * 5
        alvo.receber_ataque(dano)
        print(f"\n{self.get_nome()} atacou {alvo.get_nome()} e causou {dano} de dano!\n")
    


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

class Jogo:
    '''Classe orquestradora do jogo'''

    def __init__(self):
        self.heroi = Heroi(nome="Joao", vida= 100, nivel= 3, habilidade="Peido fedido")
        self.inimigo = Inimigo(nome="Rebeca", vida= 100, nivel= 2, tipo="Risada")


    def iniciar_batalha(self):
        """Gestão da batalha"""

        print("Iniciando Batalha!")

        while self.heroi.get_vida() > 0 and self.inimigo.get_vida() > 0:

            print("\nDetalhes do Personagem:")
            print(self.heroi.exibir_informacoes())
            print(self.inimigo.exibir_informacoes())

            input("Pressione ENTER para atacar...")
            escolha = input("\n1 - Ataque normal\n2 - Ataque especial\nEscolha: ")

            if escolha == '1':
                self.heroi.ataque(self.inimigo)
            
            else:
                print("Escolha inválida. Selecione uma opção válida")


        if self.heroi.get_vida() > 0:
            print(f"\nParabéns, {self.heroi.get_nome()}. Você ganhou!")
        else:
            print(f"\nVocê foi derrotado por {self.inimigo.get_nome()}")

#Criação instancia do jogo e iniciar a batalha
jogo = Jogo()
jogo.iniciar_batalha()  