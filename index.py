from src.utils.limparTerminal import limparTerminal
from src.utils.criarUsuario import criarUsuario
from src.database.create_usuario import create_usuario
from src.utils.formatarTexto import formatarTexto_azul
from src.database.search_nodes import search_nodes
from src.database.count_nodes import count_nodes
from src.database.connection import driver

def main():
    while True:
        limparTerminal()
        print("--- Menu ---")
        print("1 - Cadastrar usuário")
        print("2 - Listar usuários")
        print("3 - Contar usuários")
        print("0 - Sair")
        print("------------")
        opcao = input("Digite a opção desejada: ")
        if opcao == "1":
            usuario = criarUsuario(isRequired=False)
            result = create_usuario(usuario)
            print("\n" + formatarTexto_azul(result))
            input()
        elif opcao == "2":
            result = search_nodes("Usuario")
            print()
            if result:
                for usuario in result:
                    print(usuario)
            input()
        elif opcao == "3":
            result = count_nodes("Usuario")
            print()
            print("Total de usuários: " + str(result))
            input()
        elif opcao == "0":
            limparTerminal()
            driver.close()
            break
        else:
            print("Opção inválida")
            input()

if __name__ == "__main__":
    main()

# Path: index.py