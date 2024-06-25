from src.utils.formatarTexto import (formatarTexto_italico, formatarTexto_negrito,
    formatarTexto_vermelho)
from src.functions.pegarTodos import pegarTodos
from src.functions.pegarUm import pegarUm

def listarProduto():
    try:
        id = input(f"Digite o {formatarTexto_negrito("ID")} do produto: {formatarTexto_italico('(deixe em branco para listar todos) ')}")
        if id == "":
            produtos = pegarTodos("Produto")
            if produtos is None:
                raise Exception("Nenhum produto encontrado.")
            tamanhoTotal = len(produtos)
            count = 0
            print()
            for produto in produtos:
                print(formatarTexto_italico(f"- Produto {count + 1} de {tamanhoTotal} -"))
                print(produto)
                input()
                count += 1
        else:
            produto = pegarUm("Produto", id)
            if produto is not None:
                print()
                print(produto)
                input()
            else:
                raise Exception("Produto não encontrado.")
    except Exception as e:
        print(f"\nError in listarProduto: {formatarTexto_vermelho(str(e))}")
        input()
        return
    except KeyboardInterrupt:
        return

# Path: src/functions/listarProduto.py