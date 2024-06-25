from src.utils.limparTerminal import limparTerminal
from src.layouts.menuCompra import menuCompra
from src.layouts.menuProduto import menuProduto
from src.layouts.menuUsuario import menuUsuario
from src.layouts.menuVendedor import menuVendedor
from src.utils.formatarTexto import formatarTexto_negrito

def menuPrincipal():
    while True:
        limparTerminal()

        print("==" * 21)
        print(formatarTexto_negrito("Menu Principal"))
        # print("1 - CRUD de Compras")
        print("2 - CRUD de Produtos")
        print("3 - CRUD de Usuários")
        # print("4 - CRUD de Vendedores")
        print("0 - Sair")
        print("==" * 21)
        
        opcao = input("\nDigite a opção desejada: ")
        
        match opcao:
            case "1":
                menuCompra()
            case "2":
                menuProduto()
            case "3":
                menuUsuario()
            case "4":
                menuVendedor()
            case "0":
                print("\nSaindo...\n")
                limparTerminal()
                return
            case _:
                print("Opção inválida")
                input()
                
# Path: src/layouts/menuPrincipal.py