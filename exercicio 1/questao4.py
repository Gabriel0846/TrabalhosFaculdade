# Mensagem de boas-vindas
print("Bem vindo a Livraria do Gabriel Lopes dos Santos")

# variável global com valor inicial 0
id_global = 0

# lista vazia de livros
lista_livro = []

# função para cadastrar livro
def cadastrar_livro(id):
    print('\n----------------------------------')
    print('------ MENU CADASTRO LIVRO -------')
    print(f'ID do livro: {id_global}')
    nome = input("Digite o nome do livro: ")
    autor = input("Digite o autor do livro: ")
    editora = input("Digite a editora do livro: ")
    livro = {'id': id, 'nome': nome, 'autor': autor, 'editora': editora}
    lista_livro.append(livro)
    print("Livro cadastrado com sucesso!")

# função para consultar livros de varias formas
def consultar_livro():
    while True:
        print('\n----------------------------------')
        print('------ MENU CONSULTAR LIVRO ------')
        print("1 - Consultar Todos os Livros")
        print("2 - Consultar Livro por Id")
        print("3 - Consultar Livros(s) por Autor")
        print("4 - Retornar")
        opcao = input("Escolha uma opção: ")
        if opcao == '1':
            # printa todos os livros cadastrados na lista
            print('\n----------------------------------')
            for livro in lista_livro:
                print(f'ID: {livro['id']}')
                print(f'NOME: {livro['nome']}')
                print(f'AUTOR: {livro['autor']}')
                print(f'EDITORA: {livro['editora']}')
                print()
        elif opcao == '2':
            # printa todos os livros por id com retorno caso id não estar na lista
            id = int(input("Digite o ID do livro: "))
            print('\n----------------------------------')
            for livro in lista_livro:
                if livro['id'] == id:
                    print(f'ID: {livro['id']}')
                    print(f'NOME: {livro['nome']}')
                    print(f'AUTOR: {livro['autor']}')
                    print(f'EDITORA: {livro['editora']}')
                    print()
                    break
            else:
                print("Livro não encontrado.")
        elif opcao == '3':
            # printa todos os livros por autor com retorno caso autor não estar na lista
            autor = input("Digite o autor: ")
            print('\n----------------------------------')
            for livro in lista_livro:
                if livro['autor'] == autor:
                    print(f'ID: {livro['id']}')
                    print(f'NOME: {livro['nome']}')
                    print(f'AUTOR: {livro['autor']}')
                    print(f'EDITORA: {livro['editora']}')
                    print()
            else:
                print("Autor não encontrado.")
        elif opcao == '4':
            break
        else:
            # retorna caso opção digitada seja invalida, e retorna a pergunta no laço
            print("Opção invalida. Tente novamente.")

# função para remover um livro
def remover_livro():
    id = int(input("Digite o ID do livro a ser removido: "))
    for livro in lista_livro:
        if livro['id'] == id:
            lista_livro.remove(livro)
            print("Livro removido com sucesso!")
            break
    else:
        print("ID inválido.")

# Menu principal
while True:
    print('\n----------------------------------')
    print('--------- MENU PRINCIPAL ---------')
    print("1 - Cadastrar Livro")
    print("2 - Consultar Livro(s)")
    print("3 - Remover Livro")
    print("4 - Sair")
    opcao = input(">> ")
    if opcao == '1':
        id_global += 1
        cadastrar_livro(id_global)
    elif opcao == '2':
        consultar_livro()
    elif opcao == '3':
        remover_livro()
    elif opcao == '4':
        print("Encerrando o programa...")
        break
    else:
        print("Opção inválida.")

