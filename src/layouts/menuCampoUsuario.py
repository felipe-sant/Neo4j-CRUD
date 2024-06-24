from src.classes.compra import Compra
from src.utils.limparTerminal import limparTerminal
from src.utils.formatarTexto import formatarTexto_negrito

def menuCampoUsuario(colecao: Compra) -> Compra:
    while True:
        limparTerminal()
        
        print("--" * 21)
        print(formatarTexto_negrito("Menu Campo Usuário"))
        print("1 - Setar Usuário")
        print("2 - Listar Usuários")
        print("--" * 21)
        
        opcao = input("\nDigite a opção desejada: ")
        
        match opcao:
            case "1":
                pass
                return colecao
            case "2":
                pass
            case _:
                print("Opção inválida")
                input()