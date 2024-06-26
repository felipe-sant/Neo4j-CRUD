from src.utils.criarCompra import criarCompra
from src.database.insert_compra import insert_compra
from src.utils.formatarTexto import formatarTexto_vermelho
from src.layouts.menuCampoUsuario import menuCampoUsuario
from src.database.count_nodes import count_nodes
from src.layouts.menuCampoProdutos import menuCampoProdutos

def cadastrarCompra():
    try:
        compra = criarCompra(isRequired=True)
        compra.id = count_nodes("Compra") + 1
        result = insert_compra(compra)
        menuCampoUsuario(compra)
        menuCampoProdutos(compra)
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