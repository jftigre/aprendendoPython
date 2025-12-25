
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def saudacao(self):
        return(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")

pessoa1 = Pessoa("João", 20)
mensagem = pessoa1.saudacao()
print(mensagem,"\n")

pessoa2 = Pessoa("Rebecão", 22)
mensagem = pessoa2.saudacao()
print(mensagem)