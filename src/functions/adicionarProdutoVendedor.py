from src.classes.vendedor import Vendedor
from src.functions.pegarUm import pegarUm
from src.functions.definirProdutoDoVendedor import definirProdutoDoVendedor
from src.utils.formatarTexto import formatarTexto_vermelho

def adicionarProdutoVendedor(vendedor: Vendedor):
    try:
        id = input("Digite o id do produto: ")
        produto = pegarUm("Produto", id)
        if produto:
            definirProdutoDoVendedor(produto, vendedor)
            return
        else:
            raise Exception("Produto não encontrado")
    except Exception as e:
        print(f"Erro ao adicionar produto: {formatarTexto_vermelho(str(e))}")
        input()
    except KeyboardInterrupt:
        return

# Path: src/functions/adicionarProdutoVendedor.py