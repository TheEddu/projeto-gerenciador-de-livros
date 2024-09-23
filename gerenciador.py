# Gerenciador de Tarefas

# Lista para armazenar as tarefas
livros = []

# Função para adicionar uma tarefa à lista
def adicionar_livro():
    livro = input("Digite o novo livro: ")
    livros.append(livro)
    print(f"Livro '{livro}' adicionada com sucesso!\n")

# Função para remover uma tarefa da lista
def remover_livro():
    if not livros:
        print("Nenhum livro para remover.\n")
        return

    mostrar_livros()
    try:
        indice = int(input("Digite o número do livro que deseja remover: ")) - 1
        if 0 <= indice < len(livros):
            livro_removido = livros.pop(indice)
            print(f"Livro '{livro_removido}' removido com sucesso!\n")
        else:
            print("Índice inválido!\n")
    except ValueError:
        print("Erro! Por favor, insira um número.\n")

# Função para exibir todas as livros
def mostrar_livros():
    if not livros:
        print("Nenhum livro cadastrado.\n")
    else:
        print(" ===== Seus livros: =====")
        for i, livro in enumerate(livros, 1):
            print(f"{i}. {livro}")
        print("=========================")  # Quebra de linha

# Função principal para executar o menu de opções
def menu():
    while True:
        print("===== Gerenciador de livros =====")
        print("1. Adicionar livro")
        print("2. Remover livro")
        print("3. Ver todos os livros")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_livro()
        elif opcao == "2":
            remover_livro()
        elif opcao == "3":
            mostrar_livros()
        elif opcao == "4":
            print("Saindo do gerenciador de livros...")
            break
        else:
            print("Opção inválida!\n")

# Executar o programa
menu()












