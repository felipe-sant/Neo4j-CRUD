from src.utils.criarProduto import criarProduto
from src.database.insert_produto import insert_produto
from src.utils.formatarTexto import formatarTexto_vermelho

def cadastrarProduto():
    try:
        produto = criarProduto(isRequired=True)
        result = insert_produto(produto)
        print()
        print(result)
        input()
    except Exception as e:
        print(f"\nFalha ao cadastrar produto: {formatarTexto_vermelho(str(e))}")
        input()
        return  
    except KeyboardInterrupt:
        return
    
# Path: src/functions/cadastrarProduto.py