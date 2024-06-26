from src.classes.produto import Produto
from src.classes.vendedor import Vendedor
from src.database.create_relation import create_relation
from src.utils.formatarTexto import formatarTexto_vermelho

def definirProdutoDoVendedor(produto: Produto, vendedor: Vendedor):
    try:
        produto = "Produto {id: " + str(produto.id) + "}"
        vendedor = "Vendedor {id: " + str(vendedor.id) + "}"
        result = create_relation(produto, vendedor, "PERTENCE_A")
        if result:
            print()
            print(result)
            input()
    except Exception as e:
        print(f"Erro ao criar relação: {formatarTexto_vermelho(str(e))}\n")
        input()
    except KeyboardInterrupt:
        return
    
# Path: src/functions/definirProdutoDoVendedor.py