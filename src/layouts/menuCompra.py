from src.utils.limparTerminal import limparTerminal
from src.utils.formatarTexto import formatarTexto_negrito
from src.functions.cadastrarCompra import cadastrarCompra
from src.functions.listarCompra import listarCompra

def menuCompra():
    while True:
        limparTerminal()
        
        print("-=" * 20 + "-")
        print(formatarTexto_negrito("Menu Compra"))
        print("1 - Cadastrar Compra")
        print("2 - Listar Compras")
        print("0 - Voltar")
        print("-=" * 20 + "-")
        
        opcao = input("\nDigite a opção desejada: ")
        
        match opcao:
            case "1":
                cadastrarCompra()
            case "2":
                listarCompra()
            case "0":
                return
            case _:
                print("Opção inválida")
                input()
                
# Path: src/layouts/menuCompra.py