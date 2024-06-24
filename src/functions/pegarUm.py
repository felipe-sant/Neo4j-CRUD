from src.classes.compra import Compra
from src.classes.produto import Produto
from src.classes.usuario import Usuario
from src.classes.vendedor import Vendedor
from src.database.search_nodes import search_nodes
from src.utils.formatarTexto import formatarTexto_vermelho

def pegarUm(colecao: str, identificador: str) -> Compra | Produto | Usuario | Vendedor | None:
    try: 
        filtro = "id = " + identificador
        result = search_nodes(colecao, filtro)
        
        if result == [] or result is None:
            raise
        
        match colecao:
            case "Usuario":
                return Usuario.fromDict(result[0])
            case "Vendedor":
                return Vendedor.fromDict(result[0])
            case "Compra":
                return Compra.fromDict(result[0])
            case "Produto":
                return Produto.fromDict(result[0])
            case _:
                raise Exception("Erro ao converter os dados.")
            
    except:
        return None
    
# Path: src/functions/pegarUm.py