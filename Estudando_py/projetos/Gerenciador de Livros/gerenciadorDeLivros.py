def adicionar_livro(biblioteca, titulo_livro, autor_livro, ano_livro):
    livro = {"título": titulo_livro, "autor": autor_livro, "ano" : ano_livro}
    biblioteca.append(livro)
    print(f"{titulo_livro}, {ano_livro} | {autor_livro}")

def visualizar_livros(biblioteca, titulo_livro, autor_livro, ano_livro):
    for i, livro in enumerate(biblioteca):
        numero_tarefa = i + 1
        print(f"{numero_tarefa}. {['título']}, {} | {autor_livro}")

biblioteca = []

while True:
    print("\nMenu do Gerenciador de lista de tarefas:\n")
    print("1. Adicionar livro.")
    print("2. Visualizar livro.")
    print("3. ")
    print("4. ")
    print("5. ")
    print("6. Sair\n")

    escolha = int(input("Digite a sua escolha: "))

    if escolha == 1:
        titulo_livro = str(input("Título: "))
        autor_livro = str(input("Autor: "))
        ano_livro = int(input("Ano: "))

    elif escolha == 2:
        visualizar_livros(biblioteca)


    elif escolha == 6:
        print("Programa encerrado!\n")
        break