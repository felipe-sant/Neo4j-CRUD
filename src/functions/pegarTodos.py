from typing import List
from src.classes.usuario import Usuario
from src.classes.vendedor import Vendedor
from src.classes.compra import Compra
from src.classes.produto import Produto
from src.utils.formatarTexto import formatarTexto_vermelho
from src.database.search_nodes import search_nodes

def pegarTodos(colecao: str) -> list[Compra] | list[Produto] | list[Usuario] | list[Vendedor] | None:
    try:
        result = search_nodes(colecao)
        if result == [] or result is None:
            raise
        
        dados = []
        
        match colecao:
            case "Usuario":
                for usuario in result:
                    dados.append(Usuario.fromDict(usuario))
            case "Vendedor":
                for vendedor in result:
                    dados.append(Vendedor.fromDict(vendedor))
            case "Compra":
                for compra in result:
                    dados.append(Compra.fromDict(compra))
            case "Produto":
                for produto in result:
                    dados.append(Produto.fromDict(produto))
            case _:
                raise Exception("Erro ao converter os dados.")
                
        if dados == []:
            raise Exception("Erro ao converter os dados.")
        
        return dados

    except:
        return None
    
# Path: src/functions/pegarTodos.py