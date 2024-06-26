from src.classes.compra import Compra
from src.functions.pegarUm import pegarUm
from src.functions.definirProdutoDaCompra import definirProdutoDaCompra
from src.utils.formatarTexto import formatarTexto_vermelho

def adicionarProdutoCompra(compra: Compra):
    try:
        id = input("Digite o id do produto: ")
        produto = pegarUm("Produto", id)
        if produto:
            definirProdutoDaCompra(produto, compra)
            return
        else:
            raise Exception("Produto não encontrado")
    except Exception as e:
        print(f"Erro ao adicionar produto: {formatarTexto_vermelho(str(e))}")
        input()
    except KeyboardInterrupt:
        return

# Path: src/functions/adicionarProdutoCompra.py