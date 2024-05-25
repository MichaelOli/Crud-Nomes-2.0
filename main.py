# Programa de gerenciamento de lista de pessoas
#biblioteca importada do Python
import time
# Lista para armazenar os nomes das pessoas
pessoas = []

# Função para inserir uma nova pessoa
def inserir_pessoa(nome):
    pessoas.append(nome)
    print(f"{nome} adicionado com sucesso!")

# Função para listar todas as pessoas
def listar_pessoas():
    if not pessoas:
        print("Nenhuma pessoa cadastrada.")
    else:
        for i, pessoa in enumerate(pessoas):
            print(f"{i+1}. {pessoa}")

# Função para pesquisar uma pessoa pelo nome
def pesquisar_pessoa(nome):
    resultados = [p for p in pessoas if nome.lower() in p.lower()]
    if resultados:
        print("Pessoas encontradas:")
        time.sleep(1)
        for pessoa in resultados:
            print(pessoa)
    else:
        print(f"Nenhuma pessoa encontrada com o nome {nome}.")

# Função para ordenar a lista de pessoas em ordem alfabética
def ordenar_pessoas():
    pessoas.sort()
    print("Lista ordenada em ordem alfabética.")
    time.sleep(1)

# Função para atualizar o nome de uma pessoa
def atualizar_pessoa(index, novo_nome):
    if 0 <= index < len(pessoas):
        pessoas[index] = novo_nome
        time.sleep(1)
        print("Nome atualizado com sucesso!")
    else:
        print("Índice inválido.")

# Função para deletar uma pessoa da lista
def deletar_pessoa(index):
    if 0 <= index < len(pessoas):
        pessoa = pessoas.pop(index)
        time.sleep(1)
        print(f"{pessoa} deletado com sucesso!")
    else:
        print("Índice inválido.")
        time.sleep(1)

# Função para mostrar o menu e obter a escolha do usuário
def mostrar_menu():
    print("\nMenu:")
    print("1. Inserir Pessoa")
    print("2. Listar Pessoas")
    print("3. Pesquisar Pessoa")
    print("4. Ordenar Lista")
    print("5. Atualizar Pessoa")
    print("6. Deletar Pessoa")
    print("7. Sair")

# Função principal
def main():
    while True:
        mostrar_menu()
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            nome = input("Digite o nome da pessoa: ")
            inserir_pessoa(nome)
        elif escolha == '2':
            listar_pessoas()
        elif escolha == '3':
            nome = input("Digite o nome a ser pesquisado: ")
            pesquisar_pessoa(nome)
        elif escolha == '4':
            ordenar_pessoas()
        elif escolha == '5':
            listar_pessoas()
            index = int(input("Digite o índice da pessoa a ser atualizada: ")) - 1
            novo_nome = input("Digite o novo nome da pessoa: ")
            atualizar_pessoa(index, novo_nome)
        elif escolha == '6':
            listar_pessoas()
            index = int(input("Digite o índice da pessoa a ser deletada: ")) - 1
            deletar_pessoa(index)
        elif escolha == '7':
            print("Saindo do programa...")
            time.sleep(1)
            break
        else:
            print("Opção inválida. Tente novamente.")

# Executa o programa
if __name__ == "__main__":
    main()
