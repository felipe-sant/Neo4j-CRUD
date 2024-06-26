from src.utils.limparTerminal import limparTerminal
from src.utils.formatarTexto import formatarTexto_negrito
from src.classes.vendedor import Vendedor
from src.classes.compra import Compra
from src.functions.listarProduto import listarProduto
from src.functions.adicionarProdutoCompra import adicionarProdutoCompra

def menuCampoProdutos(colecao: Compra | Vendedor) -> Compra | Vendedor:
    while True:
        limparTerminal()
        
        print("--" * 21)
        print(formatarTexto_negrito("Menu Campo Produtos"))
        print("1 - Adicionar Produto")
        print("2 - Listar Produtos Atuais")
        print("3 - Listar Produtos Totais")
        print("0 - Concluir")
        print("--" * 21)
        
        opcao = input("\nDigite a opção desejada: ")
        
        match opcao:
            case "1":
                if colecao.__class__ == Vendedor:
                    pass
                if colecao.__class__ == Compra:
                    adicionarProdutoCompra(colecao)
            case "2":
                pass
            case "3":
                listarProduto()
            case "0":
                return colecao
            case _:
                print("Opção inválida")
                input()

# Path: src/layouts/menuCampoProdutos.py