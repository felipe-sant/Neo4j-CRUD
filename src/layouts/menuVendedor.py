from src.utils.limparTerminal import limparTerminal
from src.utils.formatarTexto import formatarTexto_negrito
from src.functions.cadastrarVendedor import cadastrarVendedor
from src.functions.listarVendedor import listarVendedor

def menuVendedor():
    while True:
        limparTerminal()
        
        print("-=" * 20 + "-")
        print(formatarTexto_negrito("Menu Vendedor"))
        print("1 - Cadastrar Vendedor")
        print("2 - Listar Vendedores")
        print("0 - Voltar")
        print("-=" * 20 + "-")
        
        opcao = input("\nDigite a opção desejada: ")
        
        match opcao:
            case "1":
                cadastrarVendedor()
            case "2":
                listarVendedor()
            case "0":
                return
            case _:
                print("Opção inválida")
                input()
                
# Path: src/layouts/menuVendedor.py