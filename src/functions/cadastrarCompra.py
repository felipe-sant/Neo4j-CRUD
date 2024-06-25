from src.utils.criarCompra import criarCompra
from src.database.insert_compra import insert_compra
from src.utils.formatarTexto import formatarTexto_vermelho

def cadastrarCompra():
    try:
        compra = criarCompra(isRequired=True)
        result = insert_compra(compra)
        print()
        print(result)
        input()
    except Exception as e:
        print(f"\nFalha ao cadastrar compra: {formatarTexto_vermelho(str(e))}")
        input()
        return
    except KeyboardInterrupt:
        return
    
# Path: src/functions/cadastrarCompra.py