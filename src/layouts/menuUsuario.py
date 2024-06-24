from src.utils.limparTerminal import limparTerminal
from src.utils.formatarTexto import formatarTexto_negrito
from src.functions.listarUsuario import listarUsuario

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
                pass
            case "2":
                listarUsuario()
            case "3":
                pass
            case "0":
                return
            case _:
                print("Opção inválida")
                input()
                
# Path: src/layouts/menuUsuario.py