from src.classes.produto import Produto
from src.classes.compra import Compra
from src.database.create_relation import create_relation
from src.utils.formatarTexto import formatarTexto_vermelho

def definirProdutoDaCompra(produto: Produto, compra: Compra):
    try:
        produto = "Produto {id: " + str(produto.id) + "}"
        compra = "Compra {id: " + str(compra.id) + "}"
        result = create_relation(produto, compra, "ESTA_EM")
        if result:
            print()
            print(result)
            input()
        else:
            raise
    except Exception as e:
        print(f"Erro ao criar relação: {formatarTexto_vermelho(str(e))}\n")
        input()
    except KeyboardInterrupt:
        return
    
# Path: src/functions/definirProdutoDaCompra.py    