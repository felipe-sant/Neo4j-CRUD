from src.utils.limparTerminal import limparTerminal
from src.utils.formatarTexto import formatarTexto_negrito
from src.functions.listarUsuario import listarUsuario
from src.functions.cadastrarUsuario import cadastrarUsuario

def menuUsuario():
    while True:
        limparTerminal()
        
        print("-=" * 20 + "-")
        print(formatarTexto_negrito("Menu Usuário"))
        print("1 - Cadastrar Usuário")
        print("2 - Listar Usuários")
        print("0 - Voltar")
        print("-=" * 20 + "-")
        
        opcao = input("\nDigite a opção desejada: ")
        
        match opcao:
            case "1":
                cadastrarUsuario()
            case "2":
                listarUsuario()
            case "0":
                return
            case _:
                print("Opção inválida")
                input()
                
# Path: src/layouts/menuUsuario.py