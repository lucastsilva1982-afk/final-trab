filmes = []
resp = "s"
# Menu Wachtlist #

while (resp == "s"):
    opcao = int(input("Informe a opção desejada (1 - Adicionar título, 2 - Visualizar watchlist, 3 - Ver quantidade de títulos, 4 - Verificar se um título está na lista, 5 - Remover título, 0 - Sair): " ))

# Adicionar Titulos #

    if opcao == 1:
        titulo = input("Informe o título do filme: ").strip().lower()
        if titulo not in filmes:
            filmes.append(titulo)
            print("Filme adicionado com sucesso!")
        else:
            print("Filme já cadastrado!")
        resp = input("Deseja cadastrar outro titulo ? (S/N): ").strip().lower()

# Visualizar Watchlist #

    elif opcao == 2:
        if len(filmes) == 0:
            print("Não há filmes cadastrados.")
        else:
            print("Watchlist:")
            for titulo in filmes:
                print("-", titulo)

# Ver a quantidade de Titulos na Watchlist #

    elif opcao == 3:
        print("Quantidade de títulos na watchlist:", len(filmes))

# Verificar o  nome do titulo que está na Watchlist #

    elif opcao == 4:
        titulo = input("Digite o título a verificar: ").strip().lower()
        if titulo in filmes:
            print("O título está na watchlist.")
        else:
            print("O título não está na watchlist.")

# Remover Titulo da Watchlist #

    elif opcao == 5:
        titulo = input("Informe o título que deseja remover da watchlist: ").strip().lower()
        if titulo in filmes:
            filmes.remove(titulo)
            print("Título removido com sucesso de sua watchlist!")
        else:
            print("Título não encontrado na watchlist.")

# Encerrar seção #

    elif opcao == 0:
        print("Sair...")
        
 # Opção Invalida #       
    else:
        print("Opção inválida!")